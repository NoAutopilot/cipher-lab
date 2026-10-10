#!/usr/bin/env python3
"""HTX-SWEEP (LANE LEDGER-10, 10 Oct 2026): the step-0 test, run retroactively. Disk only.

Entries swept: E300+ and every N2-*/O9-* of reading.md / reading-no2.md / reading-no9.md whose AUDIT.md rows ever name N3, plus E346.
For each: content words of the decoded body (reading file; {..} markup dropped; [..] kept as decoded meanings; stop-words removed)
vs the holder transcription of the entry's pointer (sources/mssEC18|mssEC19/p<pointer>.json). Both sides: one case, letters only,
period abbreviations expanded (CLAUDE.md rule 3, PX-BRODEC). overlap = LCS(decoded, transcription)/decoded content words.
Control: same overlap for the entry against 20 random OTHER pages (both volumes pooled); report p95 (19th of 20 sorted).
flag = overlap > control p95 and overlap >= 0.5.  code = share of [..] decoded meanings found anywhere in the transcription (info only).
Flags are leads for the verifier lane, never a grade change.
"""
import json, random, re, glob, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
STOP = set("""a an the and or of to in on at by for from with as is are was were be been it its that this these those you your
i he him his she her we they them their our not no so if but all any some will may can shall should would have has had do
did into than then there here what which who whom per one about more most very s st""".split())
ABBR = {"genl":"general","gen":"general","maj":"major","col":"colonel","lt":"lieutenant","lieut":"lieutenant","capt":"captain","cpt":"captain",
        "secy":"secretary","sec":"secretary","regt":"regiment","wash":"washington","genls":"generals","brig":"brigadier","comdg":"commanding",
        "qm":"quartermaster","qr":"quartermaster","govt":"government","dept":"department","hd":"headquarters","qrs":"quarters","recd":"received",
        "msg":"message","telegm":"telegram","tel":"telegram","feby":"february","jany":"january","apl":"april","apr":"april","sept":"september",
        "oct":"october","nov":"november","dec":"december","aug":"august","mar":"march","sec'y":"secretary","hon":"honorable","asst":"assistant",
        "adjt":"adjutant","inf":"infantry","cav":"cavalry","artillery":"artillery","tels":"telegrams"}
def words(s):
    out = []
    for w in re.findall(r"[a-z]+", s.lower()):
        w = ABBR.get(w, w)
        if w not in STOP and len(w) > 1: out.append(w)
    return out
def lcs(a, b):
    prev = [0]*(len(b)+1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b): cur.append(prev[j]+1 if x == y else max(prev[j+1], cur[j]))
        prev = cur
    return prev[-1]
# ---- entries
HDR = re.compile(r"^\*\*(\S+) \| Page (-?\d+) \| (\d+) \|")
def parse(fn):
    L = open(os.path.join(T, fn)).read().split("\n"); out = {}
    for i, l in enumerate(L):
        m = HDR.match(l)
        if not m: continue
        j = i+1
        while j < len(L) and not L[j].strip(): j += 1
        out[m.group(1)] = (int(m.group(3)), L[j])
    return out
ents = {}
for fn in ("reading.md", "reading-no2.md", "reading-no9.md"): ents.update(parse(fn))
# ---- AUDIT.md classes
audit = open(os.path.join(T, "AUDIT.md")).read().split("\n"); cls = {}
for l in audit:
    m = re.match(r"\|\s*(?:\*\*)?((?:E\d+|N2-[A-Z]+|O9-[A-Z]+)(?:\s*part \d)?)(?:\*\*)?[\s,|]", l)
    if m:
        ids = re.findall(r"E\d+|N2-[A-Z]+|O9-[A-Z]+", l.split("|")[1])
        for i in ids: cls.setdefault(i, []).append(re.findall(r"N[0-5]", l))
def sel(i):
    if i == "E346": return True
    if i.startswith("E") and int(i[1:]) < 300: return False
    return any("N3" in c for c in cls.get(i, []))
# ---- transcriptions
tx = {}
for f in glob.glob(os.path.join(T, "sources/mssEC1[89]/p*.json")):
    d = json.load(open(f)); tx[int(re.search(r"p(\d+)\.json", f).group(1))] = words(d.get("transc") or "")
def body(line):
    b = re.sub(r"\{[^}]*\}", " ", line); b = re.sub(r"</?unclear>", " ", b)
    code = " ".join(re.findall(r"\[([^\]]*)\]", b)); code = re.sub(r"\(-ed, -ing\)|= ?Er|\bM\b|\b[HCSI]\b", " ", code)
    return words(re.sub(r"[\[\]]", " ", b)), words(code)
random.seed(1810)
pages = sorted(tx)
rows = []; missing = []
for e in sorted(ents, key=lambda s: (s[0], int(re.sub(r"\D", "", s.split("-")[-1]) or 0) if s[0]=="E" else s)):
    if not sel(e): continue
    p, line = ents[e]
    if p not in tx: missing.append((e, p)); continue
    allw, codew = body(line)
    if not allw: continue
    t = tx[p]; ov = lcs(allw, t)/len(allw)
    ctl = sorted(lcs(allw, tx[q])/len(allw) for q in random.sample([q for q in pages if q != p], 20)); p95 = ctl[18]
    code = sum(1 for w in codew if w in set(t))/len(codew) if codew else float("nan")
    last = (cls.get(e) or [[]])[-1]
    rows.append((e, p, ov, p95, code, len(allw), ov > p95 and ov >= 0.5, "/".join(sorted({c for cc in cls.get(e, []) for c in cc}))))
with open(os.path.join(HERE, "htx_sweep.tsv"), "w") as f:
    f.write("entry\tpointer\toverlap\tcontrol_p95\tflag\tstrong_code>=0.5\tdecoded_content_words\tcode_overlap_info\taudit_classes_seen\n")
    for e, p, ov, p95, code, n, fl, cs in rows:
        f.write(f"{e}\t{p}\t{ov:.3f}\t{p95:.3f}\t{'FLAG' if fl else '-'}\t{'STRONG' if fl and code>=0.5 else '-'}\t{n}\t{code:.3f}\t{cs}\n")
print(len(rows), "entries;", sum(r[6] for r in rows), "flagged; missing page JSON:", missing)
print("strong (flag and code>=0.5):", " ".join(r[0] for r in rows if r[6] and r[4]>=0.5))
print("flagged:", " ".join(r[0] for r in rows if r[6]))
