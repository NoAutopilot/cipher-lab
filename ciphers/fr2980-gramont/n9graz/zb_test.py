#!/usr/bin/env python3
"""N9-GRAZ follow-on (post-hoc, outside the prereg's decision rule): rank of letters for `zb` (barred z, key NULL M) on f.30 when its
tokens are given a letter instead of dropped; same fr16 model and controls as f30_test.py; prints each zb context under R. Disk only."""
import sys, csv, glob
from pathlib import Path
if "--help" in sys.argv: print(__doc__); sys.exit()
H = Path(__file__).resolve().parent; T = H.parent; R = T.parents[1]
sys.path.insert(0, str(R / "tools")); import judge_plaintext as J
model = J.NgramModel([J.read_corpus(p) for p in sorted(glob.glob(str(R / "tools/data/fr16/*.gz")))])
rows = list(csv.DictReader(open(T / "reading_f30_extended_tokens.tsv"), delimiter="\t"))
val = lambda r: r["value"] if r["value"].isalpha() and r["value"] != "NULL" else ""
toks = [r for r in rows if val(r) or r["sign"] == "zb"]
st = lambda v: "".join(v if r["sign"] == "zb" else val(r) for r in toks)
sc = sorted(((model.score(st(L)), L) for L in "ABCDEFGHIKLMNOPQRSTVXYZ"), reverse=True)
base = model.score(st(""))
print("zb n =", sum(r["sign"] == "zb" for r in toks), "; as null", round(base, 4), "; top5", [(L, round(s, 4)) for s, L in sc[:5]],
      "; R rank", [L for _, L in sc].index("R") + 1, round(dict((L, s) for s, L in sc)["R"], 4))
for i, r in enumerate(toks):
    if r["sign"] != "zb": continue
    a = "".join(val(x) or "_" for x in toks[max(0, i - 5):i]).lower(); b = "".join(val(x) or "_" for x in toks[i + 1:i + 6]).lower()
    print(f"{r['folio']} {r['line']} {r['position']}\t{a}R{b}")
