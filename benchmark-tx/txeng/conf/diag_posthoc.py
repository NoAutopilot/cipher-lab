#!/usr/bin/env python3
"""TXE-E post-hoc diagnostic (NOT a gate, not eligible for eval): the same dev_tune leave-one-line-out with lighter
smoothing (0.01) and a larger flip weight (S 1.0), to see whether the pre-registered setting failed on mechanism
(posterior mass diluted over 51 smoothed cells, under the lattice's 0.02 floor) or because the truth is not in the
readers' confusions at all. Prints truth-in-lattice and writes work/diag_*.tsv (uncommitted scratch)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_conf as R
K, tx_bench = R.K, R.tx_bench
from judge_plaintext import LANG_CORPORA, NgramModel, read_corpus

pages = R.prep()
key = K.read_key(R.H / "key_1572_sheet.tsv")
model = NgramModel([read_corpus(p) for p in LANG_CORPORA["it16dip"]]); lm = K.LM(model)
T = {(r["line"], int(r["pos"])): r for r in tx_bench.read_tsv(R.TRUTH)}
base = R.lattice(pages, R.DEV)
nb = K.read_confusion(R.H / "confusion_1572.tsv")
for smooth, S in ((0.01, 1.0),):
    out, n, inl, err, errin = [], 0, 0, 0, 0
    for h in R.DEV:
        rest = [x for x in R.DEV if x != h]
        rows, _ = K.learn_confusion([str(R.TMP / "f178v_A.tsv"), str(R.TMP / "f178v_B.tsv")], tx_bench.read_tsv(R.TRUTH),
                                    rest, "f178v", sorted(key), smooth=smooth)
        p = R.TMP / "diag_M.tsv"; K.write_matrix(rows, p, ["diag"]); M = K.read_matrix(p)
        a, b, ref = pages["f178v"]
        lr, _ = K.from_passes(a, b, ref, nb, False, M, S)
        lh = {}
        for ln, pos, c, pr in lr:
            lh.setdefault((ln, pos), {})[c] = pr
        mix = [(k, lh[k]) if k[0] == h else (k, c) for k, c in base]
        seq = K.viterbi(mix, key, lm, 4.0)[0]
        out += [(k, s) for (k, _), s in zip(mix, seq) if k[0] == h]
        for k, c in mix:
            t = T.get(k)
            if k[0] != h or not t or t["status"] != "scored":
                continue
            ts = set(filter(None, t["truth"].split("|"))); n += 1; hit = bool(ts & set(c)); inl += hit
            if max(c, key=c.get) not in ts:
                err += 1; errin += hit
    path = R.TMP / f"diag_s{smooth:g}_S{S:g}.tsv"
    with open(path, "w") as f:
        f.write("line\tpos\tsign\n")
        for (ln, pos), s in out:
            f.write(f"{ln}\t{pos}\t{s}\n")
    print(f"smooth {smooth} S {S}: truth in lattice {inl}/{n}; top1 wrong {err}, truth in lattice among them {errin}; {path}")
