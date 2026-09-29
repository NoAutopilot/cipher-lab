#!/usr/bin/env python3
"""H273 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026), script-only. f.61 L07 opens, after the clear words 'ni mesme' (H63/H253 readers), with
CA (a null, H256-H260) and LOOPBAR (unread), then Tomokiyo's S4a 'jalousie au beau-pere' from L07 3. So the text runs 'ni mesme [null] [LOOPBAR] jalousie
au beau-pere'. If period French puts a determiner before 'jalousie' after 'ni mesme', LOOPBAR must carry a word or letter there; if 'ni mesme' + bare noun
is ordinary, LOOPBAR can be a null. Count in tools/data/fr16 (lower-cased, accents stripped, apostrophes split): after 'ni mesme' / 'ny mesme' / 'ni mesmes'
/ 'ny mesmes', the next word -- a determiner (la le les l un une de du des d ce cette ces sa son ses ma mon mes leur leurs vostre nostre) or not -- and the
word before 'jalousie' wherever it occurs. Pre-stated: 'LOOPBAR must be a word here' iff at least 20 'ni mesme' + next-word cases exist and the bare
(non-determiner) share is under 10 percent; 'a null is possible' iff the bare share is 30 percent or more; otherwise unsettled. Descriptive for the
null-band table; no value, no reading.  python3 h273_l07_head.py [--check]"""
import gzip, os, re, sys, unicodedata
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.abspath(f"{HERE}/../../../tools/data/fr16")
DET = set("la le les l un une de du des d ce cette ces sa son ses ma mon mes leur leurs vostre nostre".split())
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
toks = []
for f in sorted(os.listdir(D)):
    if f.endswith(".gz"): toks += re.findall(r"[a-z]+", norm(gzip.open(f"{D}/{f}", "rt", encoding="utf-8", errors="ignore").read()).replace("'", " "))
nxt = Counter(); bef = Counter()
for i in range(len(toks) - 2):
    if toks[i] in ("ni", "ny") and toks[i + 1] in ("mesme", "mesmes"): nxt[toks[i + 2]] += 1
    if toks[i + 2] == "jalousie": bef[toks[i + 1]] += 1
n = sum(nxt.values()); det = sum(v for w, v in nxt.items() if w in DET); bare = n - det
rows = [f"'ni/ny mesme(s)' + next word: {n} cases; determiner {det}, other {bare} ({bare / n:.2f} bare)" if n else "'ni mesme': 0 cases",
        "next words: " + ", ".join(f"{w} {v}" for w, v in nxt.most_common(15)),
        f"word before 'jalousie' ({sum(bef.values())} cases): " + ", ".join(f"{w} {v}" for w, v in bef.most_common(10))]
verdict = "LOOPBAR must be a word here" if n >= 20 and bare / n < 0.10 else ("a null is possible" if n and bare / n >= 0.30 else "unsettled")
rows.append("read-out: " + verdict)
txt = "\n".join(rows) + "\n"; p = f"{HERE}/h273_l07_head_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(txt); print(txt, end="")
