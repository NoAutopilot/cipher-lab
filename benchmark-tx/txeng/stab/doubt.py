#!/usr/bin/env python3
"""TXE-J doubt table (read-free, after the dev decodes were committed): does stab < floor predict L's wrong positions on
dev_tune? Truth is read only through tools/tx_bench.py (position_errors). Positions: the truth's skeleton is passC
(BENCHMARK-TX.tsv notes), whose positions are L's and box_pos.tsv's; the script checks that per line."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
import tx_bench as T  # noqa: E402
import key_decode_lattice as K  # noqa: E402

HERE = Path(__file__).resolve().parent
truth = T.read_tsv(ROOT / "benchmark-tx/birago1572-no87.truth.tsv")
L = T.load_output([ROOT / "benchmark-tx/txeng/units/labels_dev_tune.tsv"])
C = T.load_output([ROOT / "benchmark-tx/outputs/birago1572-no87/passC.tsv"])
for ln in L:
    n = sum(1 for r in truth if r["line"] == ln)
    assert n == len(C[ln]) == len(L[ln]), (ln, n, len(C[ln]), len(L[ln]))
err = T.position_errors(truth, L)
st = K.read_stability(HERE / "stab_f178v.tsv", ROOT / "benchmark-tx/txeng/compare/box_pos.tsv")
rows = [(k, err[k], st.get((k[0], int(float(k[1]))))) for k in err]
mapped = [(k, e, s) for k, e, s in rows if s is not None]
print(f"scored {len(rows)}, L wrong {sum(e for _, e, _ in rows)}, mapped {len(mapped)}, "
      f"L wrong & mapped {sum(e for _, e, _ in mapped)}")
print("floor\tflagged\tshare\tL_wrong_flagged\trecall\tprecision")
for fl in (0.4, 0.6, 0.8, 1.0):
    f = [(e, s) for _, e, s in mapped if s < fl]
    tp = sum(e for e, _ in f); w = sum(e for _, e, _ in mapped)
    print(f"{fl}\t{len(f)}\t{len(f) / len(mapped):.3f}\t{tp}\t{tp / w:.3f}\t{(tp / len(f)) if f else float('nan'):.3f}")
print("L wrong positions:", sorted((k[0][-3:] + "." + k[1], s) for k, e, s in rows if e))
