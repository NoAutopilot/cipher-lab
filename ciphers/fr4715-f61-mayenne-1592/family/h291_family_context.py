#!/usr/bin/env python3
"""H291 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026), script-only: every LOOPSTEM1 and CH token in the f.101r and f.188r alignments
(family/passes/f101r_align.tsv, f188r_align.tsv; tools/interlinear_align.py output, one gloss chunk per cipher token) printed with the gloss chunks of
its two neighbours on each side, so the verifier sees whether the q/s and e/m letters sit inside gloss words on those leaves (letters there), the
contrast with f.61's 'que les [ ] [ ] trop' (H283/H286). Descriptive.  python3 h291_family_context.py [--check]"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
rows = []
for f in ("f101r_align.tsv", "f188r_align.tsv"):
    d = list(csv.DictReader(open(f"{P}/{f}"), delimiter="\t")); by = {}
    for r in d: by.setdefault(r["cipher_line"], []).append(r)
    for L, rs in by.items():
        for k, r in enumerate(rs):
            if r["value"] in ("LOOPSTEM1", "CH"):
                ctx = " ".join((rs[j]["plain_chunk"] or "-") if j != k else f"[{rs[j]['plain_chunk'] or '-'}]" for j in range(max(0, k - 2), min(len(rs), k + 3)))
                rows.append(f"{f[:5]} {L} idx {r['idx']} {r['value']}: {ctx} ({r['status']})")
n_in = sum(1 for r in rows if r.split(": ")[1].split(" (")[0].replace("[", "").replace("]", "").replace(" ", "").replace("-", "").isalpha() and "[-]" not in r)
rows.append(f"{len(rows)} tokens; {n_in} with a letter of their own and lettered neighbours on both sides (inside a gloss run)")
out = "\n".join(rows) + "\n"; p = f"{HERE}/h291_family_context_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(p) and open(p).read() == out; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(out); print(out, end="")
