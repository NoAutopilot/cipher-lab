#!/usr/bin/env python3
"""R8-ROUS2 count-vector fit check of Hatzenberger 2015 p.326 values (see PREREG-R8-ROUS2.md)."""
import re, unicodedata, collections, pathlib
D = pathlib.Path(__file__).resolve().parent.parent
PAIRS = [("f213", "slip_f214r.txt"), ("f216v", "slip_f217r.txt"), ("f249", "slip_f250.txt"), ("f266r", "slip_f265r.txt")]
WORDS = {"republique": r"\brepublique\b|\brep\.?e\b", "senat": r"\bsenat\w*", "ambassadeur": r"\bambassad\w*"}
def norm(t): return unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
def groups(f):
    out = []
    for ln in (D / f).read_text().splitlines():
        if ln.startswith("#") or not ln.strip(): continue
        out += [g.split("|")[0] for g in ln.split()[1:]]
    return out
cv = collections.defaultdict(lambda: [0]*len(PAIRS)); wv = {w: [0]*len(PAIRS) for w in WORDS}
for i, (c, s) in enumerate(PAIRS):
    for g in groups(f"ciphertext_{c}.txt"): cv[g][i] += 1
    txt = norm(" ".join(l for l in (D / s).read_text().splitlines() if not l.startswith("#")))
    for w, rx in WORDS.items(): wv[w][i] = len(re.findall(rx, txt))
print("passages:", [c for c, _ in PAIRS], "distinct codes:", len(cv))
for w, v in wv.items():
    fit = sorted(g for g, x in cv.items() if x == v)
    print(f"{w}: slip vector {v}; codes with equal vector: {len(fit) if sum(v) else 'n/a (all-zero)'} {fit if sum(v) else ''}")
for g in ("136", "219", "404", "605"):
    print(f"code {g}: vector {cv.get(g, [0]*len(PAIRS))}")
f165 = groups("ciphertext_f165.txt")
for g in ("404", "219", "136", "605"):
    for i, x in enumerate(f165):
        if x == g: print(f"f165 {g} at {i}: ...{' '.join(f165[max(0,i-5):i])} [{g}] {' '.join(f165[i+1:i+6])}...")
