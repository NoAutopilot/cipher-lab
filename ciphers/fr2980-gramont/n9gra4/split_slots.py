#!/usr/bin/env python3
"""N9-GRA4 POST-HOC, NOT REGISTERED, NOT GATING: the print letter each reconciled '?' slot aligns to, tagged with the
pass A / pass B labels that split there (from reconcile.py's own SequenceMatcher opcodes). Written after the target score
to see what the z/zb, d/n6, f/fh and q/g splits read against the print. Writes n9gra4/split_slots.tsv."""
import difflib, sys, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import score4 as S4
S = S4.S
ns = {}
exec(compile((HERE / "reconcile.py").read_text().split("A = load")[0], "rec", "exec"), ns)  # norm(), load(), ALIAS, PAIRS
A = ns["load"]([str(HERE / "passA.tsv")]); B = ns["load"]([str(HERE / "passB.tsv")])
tags = []
for ln in sorted({r[:-2] for r in A}):
    a = A[ln + "_a"] + A[ln + "_b"]; b = B[ln + "_a"] + B[ln + "_b"]
    for op, a0, a1, b0, b1 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == "equal": tags += [None] * (a1 - a0)
        elif op == "replace" and a1 - a0 == b1 - b0:
            tags += [None if frozenset((x, y)) in ns["PAIRS"] else f"{x}/{y}" for x, y in zip(a[a0:a1], b[b0:b1])]
        else:
            tags += ["unequal"] * max(a1 - a0, b1 - b0)
rows = S4.rowtoks(HERE / "recon.tsv"); assert len(rows) == len(tags), (len(rows), len(tags))
key = S.load_key()
kept = [(r, d, tg) for (r, t), tg in zip(rows, tags) for d in S.decode([t], key)]
_, _, al = S.align_agree([d for _, d, _ in kept], S4.S3.SEGS["S1"])
out = ["row\tsplit\taligned"]; byp = collections.defaultdict(list)
for (r, (t, v), tg), x in zip(kept, al):
    if t == "?" and tg and tg != "unequal":
        out.append(f"{r}\t{tg}\t{x}"); byp[tg].append(x)
(HERE / "split_slots.tsv").write_text("\n".join(out) + "\n")
for k, L in sorted(byp.items(), key=lambda kv: -len(kv[1])):
    if len(L) >= 3: print(k, len(L), "".join(L), collections.Counter(L).most_common(3))
