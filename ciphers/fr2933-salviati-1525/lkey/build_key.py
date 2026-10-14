#!/usr/bin/env python3
"""SALV-LKEY (14 Oct 2026): reconcile the two blind mapping passes (passA_part*.tsv, passB_part*.tsv) into key_lasry.tsv.
A sign is keyed only where both passes name the same his_cell (not 'none'). Value = his cell's value (i1/i2 -> i, l1/l2 -> l,
p1/p2 -> p, et1/et2 -> et, u/v -> u; his '?' stripped). Grade H (published key) where his value is unmarked and neither pass
rated the match L; else M (his '?', a pass's L, or two cells 'a|b'). class: letter / syllable / other (che, et) / amb ('a|b':
graded M, not read by score_lasry.py). Combination marks in our transcription ('H^1|o') are keyed when every component
sign is keyed to the same value. Source column: 'published' (George Lasry, cyphersolver dde5b0ea, lasry_p031_1.png)."""
import csv, os, sys
D = os.path.dirname(os.path.abspath(__file__))
def load(p):
    d = {}
    for part in (1, 2):
        for r in csv.DictReader(open(os.path.join(D, f"pass{p}_part{part}.tsv"), encoding="utf-8"), delimiter="\t"):
            d[r["our_sign"].strip()] = (r["his_cell"].strip(), r["conf"].strip())
    return d
A, B = load("A"), load("B")
NORM = {"i1": "i", "i2": "i", "l1": "l", "l2": "l", "p1": "p", "p2": "p", "et1": "et", "et2": "et", "u/v": "u"}
# SALV-MAP3 (14 Oct 2026, PREREG-SALV-MAP3.md): a third blind pass (passC_part*.tsv, 22 types) settles an A/B disagreement when its
# normalised value set equals A's or B's exactly; settled rows are graded M, note names all three cells; settled 'none' stays unread.
C = {}
for part in (1, 2):
    f = os.path.join(D, f"passC_part{part}.tsv")
    if os.path.exists(f):
        for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"):
            C[r["our_sign"].strip()] = (r["his_cell"].strip(), r["conf"].strip())
def vset(cell):
    return "none" if cell in ("none", "") else "|".join(sorted({NORM.get(c.rstrip("?"), c.rstrip("?")) for c in cell.split("|")}))
rows = {}
for s in sorted(A):
    (ca, qa), (cb, qb) = A[s], B.get(s, ("none", ""))
    if ca != cb and s in C:
        cc, qc = C[s]; va, vb, vc = vset(ca), vset(cb), vset(cc)
        maj = va if va == vb else (vc if vc in (va, vb) else None)   # A = B after normalising also counts as 2 of 3
        if maj and maj != "none":
            vc = maj; vals = vc.split("|")
            cls = "amb" if len(vals) > 1 else ("other" if vc in ("che", "et") else ("letter" if len(vc) == 1 else "syllable"))
            rows[s] = (vc, "M", cls, f"SALV-MAP3 2-of-3 A:{ca}/{qa} B:{cb}/{qb} C:{cc}/{qc}")
        continue
    if ca != cb or ca == "none":
        continue
    cells = ca.split("|"); q = any(c.endswith("?") for c in cells) or "L" in (qa, qb) or len(cells) > 1
    vals = sorted({NORM.get(c.rstrip("?"), c.rstrip("?")) for c in cells})
    v = "|".join(vals)
    cls = "amb" if len(vals) > 1 else ("other" if v in ("che", "et") else ("letter" if len(v) == 1 else "syllable"))
    rows[s] = (v, "M" if q else "H", cls, f"A:{ca}/{qa} B:{cb}/{qb}")
# combination marks seen in the transcription
for t in csv.DictReader(open(os.path.join(D, "ciphertext_lasry.tsv"), encoding="utf-8"), delimiter="\t"):
    s = t["sign"]
    if "|" in s and "^" in s and s not in rows:
        b, m = s.split("^", 1); comp = [f"{b}^{x}" for x in m.split("|")]
        got = {rows[c][0] for c in comp if c in rows}
        if all(c in rows for c in comp) and len(got) == 1 and rows[comp[0]][2] != "amb":
            rows[s] = (got.pop(), "M" if any(rows[c][1] == "M" for c in comp) else "H", rows[comp[0]][2], "combination of " + ",".join(comp))
out = ["sign\tvalue\tgrade\tclass\tsource\tnote"] + [f"{s}\t{v}\t{g}\t{c}\tpublished\t{n}" for s, (v, g, c, n) in sorted(rows.items())]
txt = "\n".join(out) + "\n"; p = os.path.join(D, "key_lasry.tsv")
if "--check" in sys.argv:
    sys.exit(0 if open(p, encoding="utf-8").read() == txt else 1)
open(p, "w", encoding="utf-8").write(txt); print(len(rows), "keyed signs")
