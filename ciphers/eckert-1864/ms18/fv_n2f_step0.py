#!/usr/bin/env python3
"""FV-N2f step 0 (LANE LEDGER-10 Wave 3 Step-0 ruling), N2-JG JH JI, disk only.
 (a) ordered overlap = LCS of decoded content words (stop words dropped, one case) against the holder transcription of the
     entry's own lines (sources/mssEC18/p<ptr>.json, cut from the entry's header line to the next entry), / decoded content words
 (b) control = same LCS against that transcription's words shuffled within the entry, 20 draws, p95
 (c) key-dependent words = decoded content words not in the transcription at all
 hit = (a) >= 0.5 and (a) > (b). Numbers are compared as decoded (digits), so a code number counts in (c)."""
import json, random, re, os
T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STOP = set("""a an the and or of to in on at by for from with as is are was were be been it its that this these those you your
i he him his she her we they them their our not no so if but all any some will may can shall should would have has had do
did into than then there here what which who whom per one about more most very s st period sig stop toby ed ing""".split())
ENTRIES = {"N2-JG": (9765, "SH Beckwith"), "N2-JH": (9780, "F. T. Bickford"), "N2-JI": (9876, "Caldwell")}
def words(s): return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 1]
def lcs(a, b):
    m = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)):
        for j in range(len(b)):
            m[i+1][j+1] = m[i][j]+1 if a[i] == b[j] else max(m[i][j+1], m[i+1][j])
    return m[-1][-1]
rd = open(os.path.join(T, "reading-no2.md")).read()
def body(eid):
    b = re.search(r"\*\*%s \|.*?\*\*\n\n(.*?)\n\nCode-word tokens" % re.escape(eid), rd, re.S).group(1)
    b = re.sub(r"\{[^}]*\}", " ", b)          # time/date/tail metadata out
    return words(re.sub(r"[\[\]]", " ", b))
def entry_tx(ptr, head):
    t = json.load(open(os.path.join(T, "sources/mssEC18/p%d.json" % ptr)))["transc"]
    i = t.find(head); assert i >= 0, (ptr, head)
    rest = t[i:]; lines = rest.split("\n")
    out = [lines[0]]
    for ln in lines[1:]:
        if re.search(r"\b(Wash|Washn|Wash'n)\b.*\b(64|1864)\b", ln) and out: break   # next entry header
        out.append(ln)
    return " ".join(out)
random.seed(10)
print("entry\tpointer\ta_ordered\tb_shuffle_p95\thit\tc_count\tc_words")
for e, (p, h) in ENTRIES.items():
    d = body(e); tx = words(entry_tx(p, h)); n = lcs(d, tx); a = n/len(d)
    ctl = sorted(lcs(d, random.sample(tx, len(tx)))/len(d) for _ in range(20))[18]
    c = [w for w in d if w not in set(tx)]
    print(f"{e}\t{p}\t{a:.3f} ({n}/{len(d)})\t{ctl:.3f}\t{'yes' if a >= .5 and a > ctl else 'no'}\t{len(c)}\t{' '.join(c)}")
