#!/usr/bin/env python3
"""FV-MS18p step 0 (LANE LEDGER-10 brief): does the Huntington's own page transcription carry the decoded body in clear?

For each entry: content words of the decoded body (reading.md, stop-words removed, one case) vs the words of the holder
transcription of the same pointer (sources/mssEC18/p<pointer>.json). Two figures:
  all  = decoded content words found in the transcription (in order, LCS) / decoded content words
  code = decoded meanings of code groups ([...] tokens) found in the transcription / code-group content words
A clear holder copy scores high on BOTH; a cipher transcription scores on plain words only and near 0 on `code`.
Control: `all` against 20 random other mssEC18 pages (p95). Disk only.
"""
import json, random, re, glob, os
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
STOP = set("""a an the and or of to in on at by for from with as is are was were be been it its that this these those you your
i he him his she her we they them their our not no so if but all any some will may can shall should would have has had do
did into than then there here what which who whom per one about more most very s st""".split())
ENTRIES = {"E372": 9907, "E373": 9878, "E376": 10013, "E377": 9774, "E379": 9759, "E380": 9732}
def words(s): return [w for w in re.findall(r"[a-z]+", s.lower()) if w not in STOP and len(w) > 1]
def lcs(a, b):
    m = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)):
        for j in range(len(b)):
            m[i+1][j+1] = m[i][j]+1 if a[i] == b[j] else max(m[i][j+1], m[i+1][j])
    return m[-1][-1]
rd = open(os.path.join(T, "reading.md")).read()
def body(eid):
    m = re.search(r"\*\*%s \|.*?\*\*\n\n(.*?)\n\nCode-word tokens" % eid, rd, re.S); b = m.group(1)
    b = re.sub(r"\{[^}]*\}", " ", b)  # header/tail markup
    code = " ".join(re.findall(r"\[([^\]]*)\]", b))
    code = re.sub(r"\(-ed, -ing\)|= ?Er", " ", code)
    return words(re.sub(r"[\[\]]", " ", b)), words(code)
def tx(p): return words(json.load(open(os.path.join(T, "sources/mssEC18/p%d.json" % p)))["transc"])
pages = sorted(int(re.search(r"p(\d+)", f).group(1)) for f in glob.glob(os.path.join(T, "sources/mssEC18/p*.json")))
random.seed(18)
print("entry\tpointer\tall_overlap\tcode_overlap\tcontrol_all_p95\tstep0")
for e, p in ENTRIES.items():
    allw, codew = body(e); t = tx(p)
    a = lcs(allw, t) / len(allw); c = sum(1 for w in codew if w in set(t)) / max(1, len(codew))
    ctl = sorted(lcs(allw, tx(q)) / len(allw) for q in random.sample([q for q in pages if q != p], 20))
    p95 = ctl[18]
    flag = "clear-copy" if (a >= 0.5 and c >= 0.5) else "cipher transcription (not a clear copy)"
    print(f"{e}\t{p}\t{a:.3f} ({lcs(allw,t)}/{len(allw)})\t{c:.3f}\t{p95:.3f}\t{flag}")
