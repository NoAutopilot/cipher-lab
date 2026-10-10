#!/usr/bin/env python3
"""FV-O9b step 0 (LANE LEDGER-10 brief): does the Huntington's own page transcription carry the decoded body in clear?

Same figures as ms18/fv_ms18p_step0.py, on reading-no9.md (Cipher No. 9):
  all  = decoded content words found in order (LCS) in the holder transcription / decoded content words
  code = decoded meanings of code groups ([...] tokens) found in the transcription / code-meaning content words
A clear holder copy scores high on BOTH; a ledger transcription that keeps the code words scores on plain words only.
Control: `all` against 20 random other mssEC18 pages (p95). Disk only.
"""
import json, random, re, glob, os
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
STOP = set("""a an the and or of to in on at by for from with as is are was were be been it its that this these those you your
i he him his she her we they them their our not no so if but all any some will may can shall should would have has had do
did into than then there here what which who whom per one about more most very s st period sig""".split())
ENTRIES = {"O9-DA": [9709], "O9-DD": [9687], "O9-DF": [9699, 9700]}
def words(s): return [w for w in re.findall(r"[a-z]+", s.lower()) if w not in STOP and len(w) > 1]
def lcs(a, b):
    m = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)):
        for j in range(len(b)):
            m[i+1][j+1] = m[i][j]+1 if a[i] == b[j] else max(m[i][j+1], m[i+1][j])
    return m[-1][-1]
rd = open(os.path.join(T, "reading-no9.md")).read()
def body(eid):
    m = re.search(r"\*\*%s \|.*?\*\*\n\n(.*?)\n\nCode-word tokens" % re.escape(eid), rd, re.S); b = m.group(1)
    b = re.sub(r"\{[^}]*\}", " ", b); b = re.sub(r"<[^>]*>", " ", b)
    code = " ".join(re.findall(r"\[([^\]]*)\]", b))
    return words(re.sub(r"[\[\]]", " ", b)), words(code)
def tx(ps): return sum((words(json.load(open(os.path.join(T, "sources/mssEC18/p%d.json" % p)))["transc"]) for p in ps), [])
pages = sorted(int(re.search(r"p(\d+)", f).group(1)) for f in glob.glob(os.path.join(T, "sources/mssEC18/p*.json")))
random.seed(19)
print("entry\tpointer\tall_overlap\tcode_overlap\tcode_words\tcontrol_all_p95\tstep0")
for e, ps in ENTRIES.items():
    allw, codew = body(e); t = tx(ps)
    a = lcs(allw, t) / len(allw); c = sum(1 for w in codew if w in set(t)) / max(1, len(codew))
    ctl = sorted(lcs(allw, tx([q])) / len(allw) for q in random.sample([q for q in pages if q not in ps], 20))
    flag = "clear-copy" if (a >= 0.5 and c >= 0.5) else "cipher transcription (not a clear copy)"
    print(f"{e}\t{'+'.join(map(str,ps))}\t{a:.3f} ({lcs(allw,t)}/{len(allw)})\t{c:.3f}\t{' '.join(codew)}\t{ctl[18]:.3f}\t{flag}")
