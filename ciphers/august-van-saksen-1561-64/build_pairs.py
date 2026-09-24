#!/usr/bin/env python3
"""Build ciphertext_<n>.tsv and pairs_<n>.tsv from align_<n>.txt (R21 aligner transcription).
align format: '<page> <line>: tokens | units ;; tokens | units ...'; one unit per token.
--check exits 1 if the committed TSVs differ from what this script regenerates."""
import sys, os, re
D = os.path.dirname(os.path.abspath(__file__))
def build(n):
    ct, pr = ["page\tline\tidx\tsign"], ["page\tline\tidx\tword\tsign\tunit"]
    for ln in open(f"{D}/align_{n}.txt", encoding="utf-8"):
        if ln.startswith("#") or not ln.strip(): continue
        head, body = ln.split(":", 1)
        page, line = head.split()
        idx = 0
        for w, seg in enumerate(body.split(";;")):
            toks, units = [x.split() for x in seg.split("|")]
            if len(toks) != len(units):
                sys.exit(f"{n} {page} {line} word {w}: {len(toks)} tokens vs {len(units)} units: {seg.strip()}")
            for t, u in zip(toks, units):
                idx += 1
                ct.append(f"{page}\t{line}\t{idx}\t{t}")
                pr.append(f"{page}\t{line}\t{idx}\t{w+1}\t{t}\t{u}")
    return {f"ciphertext_{n}.tsv": "\n".join(ct) + "\n", f"pairs_{n}.tsv": "\n".join(pr) + "\n"}
check = "--check" in sys.argv
ns = [a for a in sys.argv[1:] if not a.startswith("-")] or ["74", "98"]
bad = 0
for n in ns:
    if not os.path.exists(f"{D}/align_{n}.txt"): continue
    for fn, txt in build(n).items():
        p = f"{D}/{fn}"
        if check:
            if not os.path.exists(p) or open(p, encoding="utf-8").read() != txt: print("stale", fn); bad = 1
        else: open(p, "w", encoding="utf-8").write(txt); print("wrote", fn, txt.count("\n") - 1)
sys.exit(bad)
