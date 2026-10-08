#!/usr/bin/env python3
"""K8472: split the fetched volunteer page texts into entries and pick 10 per ledger (>= 8 code-shaped words, code share >= 0.25,
spread over the ledger by taking the best entry from 10 evenly spaced page strata). Writes obj<N>/entries.txt."""
import json, re, glob, sys
sys.path.insert(0, "k8472"); 
from pathlib import Path
import importlib.util
spec = importlib.util.spec_from_file_location("sc", "k8472_score.py"); sc = importlib.util.module_from_spec(spec); spec.loader.exec_module(sc)
vocab = set()
for k in sc.keys.values(): vocab |= {w for w in k if re.fullmatch(r"[a-z]+", w)}
vocab -= sc.FUNC
def pages(o):
    out = []
    for f in glob.glob(f"obj{o}/p[0-9]*.json"):
        j = json.load(open(f)); p = int(re.search(r"/p(\d+)", f).group(1))
        if j.get("transc"): out.append((p, j["title"], j["transc"]))
    return sorted(out)
for o in (9660,):
    cands = []
    for p, title, t in pages(o):
        for b, blk in enumerate(re.split(r"\n\s*\n", t)):
            tk = sc.entry_tokens(blk)
            code = [w for w in tk if w in vocab]
            if len(code) >= 8:
                cands.append((p, b, title, blk, len(code), len(code) / len(tk)))
    # strata by page order
    pl = sorted({c[0] for c in cands}); chosen = []
    n = 10; 
    for i in range(n):
        lo, hi = i * len(cands) // n, (i + 1) * len(cands) // n
        grp = cands[lo:hi]
        if grp: chosen.append(max(grp, key=lambda c: c[4]))
    with open(f"obj{o}/entries.txt", "w") as fh:
        for i, (p, b, title, blk, nc, fr) in enumerate(chosen, 1):
            fh.write(f"### K{o}-{i:02d} | {title} | {p} | code {nc} share {fr:.2f}\n{blk.strip()}\n\n")
    print(o, len(cands), "candidates;", len(chosen), "chosen:", [(c[0], c[4]) for c in chosen])
