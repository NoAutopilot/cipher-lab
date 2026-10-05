#!/usr/bin/env python3
"""N9-GRAZ f.30 test (PREREG-N9-GRAZ.md): substitute every f.30 `z` with each of 23 letters in the committed extended reading
(reading_f30_extended_tokens.tsv; NULL and unvalued tokens dropped), score the stream with tools/judge_plaintext.py's fr16 4-gram model,
report the rank of A and R; control = the H-graded sign of nearest frequency, ranked the same way. Prints the context of every z under A
and R, and Fisher's exact test on the fr.3040 class x aligned-letter table (z_occ.tsv + sort_sonnet.tsv). Disk only."""
import sys, csv, math, glob
from pathlib import Path
from collections import Counter
if "--help" in sys.argv: print(__doc__); sys.exit()
H = Path(__file__).resolve().parent; T = H.parent; R = T.parents[1]
sys.path.insert(0, str(R / "tools")); import judge_plaintext as J
J._ALPHA = None
model = J.NgramModel([J.read_corpus(p) for p in sorted(glob.glob(str(R / "tools/data/fr16/*.gz")))])
toks = [r for r in csv.DictReader(open(T / "reading_f30_extended_tokens.tsv"), delimiter="\t")]
val = lambda r: r["value"] if r["value"].isalpha() and r["value"] not in ("NULL",) else ""
toks = [r for r in toks if val(r)]
grade = Counter((r["sign"], r["grade"]) for r in toks)
LET = "ABCDEFGHIKLMNOPQRSTVXYZ"

def stream(sign, v): return "".join(v if r["sign"] == sign else val(r) for r in toks)
def ranks(sign):
    sc = sorted(((model.score(stream(sign, L)), L) for L in LET), reverse=True)
    return [L for _, L in sc], {L: s for s, L in sc}
zn = sum(1 for r in toks if r["sign"] == "z")
order, sc = ranks("z")
print(f"z on f.30: n={zn}; rank A={order.index('A')+1} ({sc['A']:.4f}), R={order.index('R')+1} ({sc['R']:.4f}); top5 {order[:5]}")
cand = sorted(((abs(n - zn), s) for (s, g), n in grade.items() if g == "H" and s != "z"))[:3]
key = {r["sign"]: val(r) for r in toks}
for _, s in cand:
    o, _ = ranks(s); n = sum(1 for r in toks if r["sign"] == s)
    print(f"control {s} (H, n={n}, value {key[s]}): own value rank {o.index(key[s])+1}; top5 {o[:5]}")
print("\ncontexts (5 letters each side), z=A | z=R:")
for i, r in enumerate(toks):
    if r["sign"] != "z": continue
    L = "".join(val(x) for x in toks[max(0, i - 5):i]).lower(); Rr = "".join(val(x) for x in toks[i + 1:i + 6]).lower()
    print(f"{r['folio']} {r['line']} {r['position']}\t{L}A{Rr}\t{L}R{Rr}")
s = {r["id"]: r["class"] for r in csv.DictReader(open(H / "sort_sonnet.tsv"), delimiter="\t")}
t = Counter()
for r in csv.DictReader(open(H / "z_occ.tsv"), delimiter="\t"):
    if r["src"] == "fr3040" and s[r["id"]] in ("K1", "K2"): t[(s[r["id"]], r["aligned"] == "R")] += 1
a, b, c, d = t[("K2", True)], t[("K2", False)], t[("K1", True)], t[("K1", False)]
def hyp(x): return math.comb(a + b, x) * math.comb(c + d, a + c - x) / math.comb(a + b + c + d, a + c)
p0 = hyp(a); p = sum(hyp(x) for x in range(max(0, a + c - c - d), min(a + b, a + c) + 1) if hyp(x) <= p0 + 1e-12)
print(f"\nfr.3040 on-target: K2 R {a} / not-R {b}; K1 R {c} / not-R {d}; Fisher two-sided p = {p:.4f}")
