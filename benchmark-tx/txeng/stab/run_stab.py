#!/usr/bin/env python3
"""TXE-J (9 Oct 2026) harness: jitter stability as a per-position prior in the lattice, Birago no.87 dev_tune, read-free.
Run from the repo root:  python3 benchmark-tx/txeng/stab/run_stab.py dev
Inputs as TXE-E (benchmark-tx/txeng/conf/run_conf.py dev, imported): passes A/B of f178v, committed passC as skeleton,
confusion_1572.tsv, printed key key_1572_sheet.tsv, it16dip LM, beam 64, lam 4.
Stability: stab_f178v.tsv = glyph_atlas.py classify --page f178v --topk 3 --holdout f178r_ --holdout f178v_
--holdout f179r_ --jitter 5 (px 2, scale 0.05, seed 1); boxes -> positions by benchmark-tx/txeng/compare/box_pos.tsv
(tx_compare.py map, label-blind). Fixed BEFORE any score: floor 0.6, gain 0.9; control = the same with the stab values
permuted over mapped positions, seeds 1-5 (seed 1 is the gating control; 2-5 reported).
Outputs are written to benchmark-tx/outputs/birago1572-no87/ and committed BEFORE tools/tx_bench.py scores them.
No vision call, no network, no truth read here."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "benchmark-tx/txeng/conf"))
import key_decode_lattice as K  # noqa: E402
import run_conf as RC  # noqa: E402
from judge_plaintext import LANG_CORPORA, NgramModel, read_corpus  # noqa: E402

RC.TMP = HERE / "work"
OUTD = RC.OUTD
FLOOR, GAIN, SEEDS = 0.6, 0.9, (1, 2, 3, 4, 5)


def as_rows(lat):
    return [(k[0], k[1], c, p) for k, cs in lat for c, p in cs.items()]


def as_lat(rows, order):
    d = {}
    for ln, pos, c, p in rows:
        d.setdefault((ln, pos), {})[c] = p
    return [(k, d[k]) for k in order]


def main(mode):
    assert mode == "dev", "eval only after the dev gate is met (one look)"
    pages = RC.prep()
    key = K.read_key(RC.H / "key_1572_sheet.tsv")
    lm = K.LM(NgramModel([read_corpus(p) for p in LANG_CORPORA["it16dip"]]))
    base = RC.lattice(pages, RC.DEV)
    order = [k for k, _ in base]
    st = K.read_stability(HERE / "stab_f178v.tsv", ROOT / "benchmark-tx/txeng/compare/box_pos.tsv")
    st = {k: v for k, v in st.items() if k[0] in RC.DEV}
    arms = {"passL_lattice_dev_tune_lam4": (base, None)}
    rows, n = K.apply_stability(as_rows(base), st, FLOOR, GAIN)
    arms["passR_stab_dev_tune"] = (as_lat(rows, order), n)
    for s in SEEDS:
        rows, n = K.apply_stability(as_rows(base), K.shuffle_stability(st, s), FLOOR, GAIN)
        arms[f"passR_stabshuf{s}_dev_tune"] = (as_lat(rows, order), n)
    print(f"positions {len(order)}, mapped {len(st)}, doubtful (< {FLOOR}) {sum(v < FLOOR for v in st.values())}")
    for name, (lat, n) in arms.items():
        RC.write_seq(OUTD / f"{name}.tsv", lat, K.viterbi(lat, key, lm, 4.0)[0])
        RC.write_topk(HERE / f"{name}_topk.tsv", lat)
        print(name, "sharpened", n, flush=True)


if __name__ == "__main__":
    main(sys.argv[1])
