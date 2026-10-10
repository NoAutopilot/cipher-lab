#!/usr/bin/env python3
"""STEP0-RULE (LANE LEDGER-10, 10 Oct 2026): the orchestrator's Step-0 ruling applied retroactively. Disk only.

Ruling (.claude/briefs/runs/2026-10-10-acct1-lane-ledger10-jobs.md, Wave 3), per entry:
  (a) ordered overlap = LCS of content words (decoded body vs the holder transcription of THAT ENTRY'S LINES) / decoded content words
  (b) control = the same LCS against the window's words shuffled within the entry, 20 draws, p95 (19th of 20 sorted)
  (c) key-dependent words = decoded content words not in the window's transcription at all (count and list)
  hit = (a) >= 0.5 and (a) > (b).
Both sides: one case, letters only, stop words dropped, period abbreviations expanded (rule 3, PX-BRODEC), digits written as words.
Decoded body: the entry's body line in reading.md / reading-no2.md / reading-no9.md; {..} markup dropped (as HTX-SWEEP); [..] kept as the
reading's own expansions; '(-ed, -ing)', '= Er' and bare grade letters dropped.
Entry's lines: the page transcription split into blocks at blank lines (one telegram per block in these ledgers); candidate windows are
each block and each pair of adjacent blocks (a telegram the volunteer broke with a blank line, or one running over a page); the window
with the highest LCS is the entry's lines (its index is reported). b2 = selection-matched control (every window shuffled, max taken,
20 draws, p95) -- stricter than (b), reported beside it, not part of the ruling's gate.
Controls (must behave or the method is reported as not separating and no grade changes):
  positive: E74, E378, E381 (N1 by holder transcription at second audit) -> must hit;
  transposed: E321 against its wire-order copy at the foot of 5781 (real route transposition, AUDIT FV-FM10b s.1) -> must NOT hit by (a);
  plus E378 and E340 with their own matched window re-ordered by Cipher No. 1's routes (key.md s.6, page 3: 7 columns; page 5: 9 columns),
  i.e. constructed wire order of a real ledger text -> must NOT hit by (a). E321 against its reading-order copy 5782 is reported too.
Writes ms18/step0_ordered.tsv. Prints the entries with no page JSON on disk (listed, never fetched).
"""
import json, random, re, glob, os
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
STOP = set("""a an the and or of to in on at by for from with as is are was were be been it its that this these those you your
i he him his she her we they them their our not no so if but all any some will may can shall should would have has had do
did into than then there here what which who whom per one about more most very s st""".split())
ABBR = {"genl":"general","gen":"general","maj":"major","col":"colonel","lt":"lieutenant","lieut":"lieutenant","capt":"captain","cpt":"captain",
        "secy":"secretary","sec":"secretary","regt":"regiment","wash":"washington","washn":"washington","genls":"generals","brig":"brigadier",
        "comdg":"commanding","qm":"quartermaster","qr":"quartermaster","govt":"government","dept":"department","hd":"headquarters","qrs":"quarters",
        "recd":"received","msg":"message","telegm":"telegram","tel":"telegram","feby":"february","jany":"january","apl":"april","apr":"april",
        "sept":"september","oct":"october","nov":"november","dec":"december","aug":"august","mar":"march","hon":"honorable","asst":"assistant",
        "adjt":"adjutant","inf":"infantry","cav":"cavalry","tels":"telegrams","immy":"immediately","immedy":"immediately"}
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
def num(n):
    if n < 20: return ONES[n]
    if n < 100: return TENS[n//10] + ("" if n % 10 == 0 else " " + ONES[n % 10])
    if n < 1000: return ONES[n//100] + " hundred" + ("" if n % 100 == 0 else " " + num(n % 100))
    if n < 1000000: return num(n//1000) + " thousand" + ("" if n % 1000 == 0 else " " + num(n % 1000))
    return str(n)
def words(s):
    s = re.sub(r"\d+", lambda m: " " + num(int(m.group())) + " ", s.replace(",", ""))
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
def body(line):
    b = re.sub(r"\{[^}]*\}", " ", line); b = re.sub(r"</?unclear>", " ", b)
    code = " ".join(re.findall(r"\[([^\]]*)\]", b))
    clean = lambda s: re.sub(r"\(-ed, -ing\)|= ?Er|\bM\b|\b[HCSI]\b", " ", s)
    return words(clean(re.sub(r"[\[\]]", " ", b))), set(words(clean(code)))
pagefile = {}
for f in glob.glob(os.path.join(T, "sources/*/p*.json")): pagefile[int(re.search(r"p(\d+)\.json", f).group(1))] = f
def blocks(pages):
    out = []
    for p in pages:
        t = json.load(open(pagefile[p])).get("transc") or ""
        out += [words(b) for b in re.split(r"\n\s*\n", t) if words(b)]
    return out
def windows(bl): return [(str(i), bl[i]) for i in range(len(bl))] + [(f"{i}+{i+1}", bl[i]+bl[i+1]) for i in range(len(bl)-1)]
def route(ws, cols, order):
    """write ws row-wise in `cols` columns, copy columns off in `order` (+k = down the k-th, -k = up the k-th)"""
    rows = [ws[i:i+cols] for i in range(0, len(ws), cols)]
    out = []
    for o in order:
        col = [r[abs(o)-1] for r in rows if len(r) >= abs(o)]
        out += col if o > 0 else col[::-1]
    return out
ROUTE3 = (7, [-1, 6, -4, 2, -3, 5, -7]); ROUTE5 = (9, [-5, 2, -9, 6, -1, 3, -8, 4, -7])   # key.md s.6, pages 3 and 5
def measure(e, allw, codew, wins, seed):
    rnd = random.Random(seed)
    sc = [(lcs(allw, w), k, w) for k, w in wins]; best, k, w = max(sc, key=lambda x: x[0])
    a = best/len(allw)
    ctl = []; ctl2 = []
    for _ in range(20):
        s = w[:]; rnd.shuffle(s); ctl.append(lcs(allw, s)/len(allw))
        m = 0
        for _, ww in wins:
            s2 = ww[:]; rnd.shuffle(s2); m = max(m, lcs(allw, s2))
        ctl2.append(m/len(allw))
    b = sorted(ctl)[18]; b2 = sorted(ctl2)[18]
    tw = set(w); c = [x for x in allw if x not in tw]
    ck = sorted({x for x in c if x in codew}); cp = sorted({x for x in c if x not in codew})
    return dict(entry=e, a=a, lcs=best, n=len(allw), b=b, b2=b2, win=k, hit=(a >= 0.5 and a > b), c=len(c), ck=ck, cp=cp)
EXTRA = {"O9-DF": [9699, 9700]}
sweep = [l.split("\t")[0] for l in open(os.path.join(HERE, "htx_sweep.tsv")).read().split("\n")[1:] if l.strip()]
targets = [("sweep", e) for e in sweep] + [("fv-o9b", e) for e in ("O9-DA", "O9-DD", "O9-DF")] + [("positive", "E74")]
# S0-57XX (LEDGER-12, 10 Oct 2026): the nine FM entries whose page JSON was fetched after STEP0-RULE listed them as missing
targets += [("s057xx", e) for e in ("E302", "E305", "E306", "E307", "E309", "E312", "E318", "E319", "E320")]
rows = []; missing = []
for kind, e in targets:
    p, line = ents[e]; pages = EXTRA.get(e, [p])
    if any(q not in pagefile for q in pages): missing.append((e, p)); continue
    allw, codew = body(line)
    r = measure(e, allw, codew, windows(blocks(pages)), sum(map(ord, e))); r["kind"] = "positive" if e in ("E74", "E378", "E381") else kind
    r["pages"] = "+".join(map(str, pages)); rows.append(r)
# transposed controls
allw, codew = body(ents["E321"][1])
b5781 = blocks([5781])
r = measure("E321 vs 5781 foot (real wire order)", allw, codew, windows(b5781), 321); r["kind"] = "transposed"; r["pages"] = "5781"; rows.append(r)
r = measure("E321 vs 5782 (reading order)", allw, codew, windows(blocks([5782])), 3210); r["kind"] = "pair-check"; r["pages"] = "5782"; rows.append(r)
for e, (cols, order), tag in (("E378", ROUTE3, "route p.3, 7 cols"), ("E340", ROUTE5, "route p.5, 9 cols")):
    p, line = ents[e]; allw, codew = body(line)
    wins = windows(blocks([p])); _, k, w = max(((lcs(allw, w), k, w) for k, w in wins), key=lambda x: x[0])
    r = measure(f"{e} wire order ({tag}, constructed)", allw, codew, [(k + "R", route(w, cols, order))], sum(map(ord, e)) + 1)
    r["kind"] = "transposed"; r["pages"] = str(p); rows.append(r)
with open(os.path.join(HERE, "step0_ordered.tsv"), "w") as f:
    f.write("kind\tentry\tpages\twindow\ta_ordered\tlcs/n\tb_shuffle_p95\tb2_selmatched_p95\thit\tc_count\tc_key_meanings\tc_plain_absent\n")
    for r in rows:
        f.write(f"{r['kind']}\t{r['entry']}\t{r['pages']}\t{r['win']}\t{r['a']:.3f}\t{r['lcs']}/{r['n']}\t{r['b']:.3f}\t{r['b2']:.3f}\t"
                f"{'HIT' if r['hit'] else '-'}\t{r['c']}\t{' '.join(r['ck'])}\t{' '.join(r['cp'])}\n")
pos = [r for r in rows if r["kind"] == "positive"]; tr = [r for r in rows if r["kind"] == "transposed"]
print("positive controls:", [(r["entry"], round(r["a"], 3), r["hit"]) for r in pos])
print("transposed controls:", [(r["entry"], round(r["a"], 3), r["hit"]) for r in tr])
ok = all(r["hit"] for r in pos) and len(pos) == 3 and not any(r["a"] >= 0.5 for r in tr)
print("controls behave:", ok)
sw = [r for r in rows if r["kind"] in ("sweep", "fv-o9b", "positive")]
nw = [r for r in rows if r["kind"] == "s057xx"]
print("S0-57XX:", len(nw), "measured;", sum(r["hit"] for r in nw), "hit; not hit:", " ".join(r["entry"] for r in nw if not r["hit"]))
print(len(sw), "entries measured;", sum(r["hit"] for r in sw), "hit; not hit:", " ".join(r["entry"] for r in sw if not r["hit"]))
print("no page JSON on disk (listed, not fetched):", missing)
