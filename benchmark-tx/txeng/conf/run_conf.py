#!/usr/bin/env python3
"""TXE-E (9 Oct 2026) harness: learnt confusion matrix in tools/key_decode_lattice.py, Birago no.87, read-free.
Run from the repo root:  python3 benchmark-tx/txeng/conf/run_conf.py dev   (leave-one-line-out on dev_tune)
                         python3 benchmark-tx/txeng/conf/run_conf.py eval  (only if the dev gate passed; one look)
Inputs as TX-DECODE (harvest/tx_decode/run.sh): blind passes A/B of f178v (L01-10 + L11-23 files) and f179r, committed
passC as position skeleton only, confusion_1572.tsv, printed key key_1572_sheet.tsv, it16dip LM, lam 4 (lam 1 also).
The decodes are written here and committed BEFORE tools/tx_bench.py scores them; learn-confusion reads truth on
dev_tune lines only (the matrix files name their lines). No vision call, no network."""
import csv, os, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
import key_decode_lattice as K  # noqa: E402
import tx_bench  # noqa: E402
from judge_plaintext import LANG_CORPORA, NgramModel, read_corpus  # noqa: E402

H = ROOT / "ciphers/nevers-birago-fr3251-1572/harvest"
OUTD = ROOT / "benchmark-tx/outputs/birago1572-no87"
HERE = Path(__file__).resolve().parent
TMP = HERE / "work"
TRUTH = ROOT / "benchmark-tx/birago1572-no87.truth.tsv"
DEV = ["f178v_L%02d" % i for i in range(1, 13)]
EVAL = ["f178v_L%02d" % i for i in range(13, 24)] + ["f179r_L%02d" % i for i in range(1, 4)]
LAMS = (4.0, 1.0)


def cat(out, files):
    with open(out, "w") as f:
        for i, p in enumerate(files):
            ls = open(p).read().splitlines(True)
            f.writelines(ls if i == 0 else ls[1:])


def prep():
    TMP.mkdir(exist_ok=True)
    cat(TMP / "f178v_A.tsv", [H / "f178v/passA.tsv", H / "f178v/passA_L11-23.tsv"])
    cat(TMP / "f178v_B.tsv", [H / "f178v/passB.tsv", H / "f178v/passB_L11-23.tsv"])
    rows = K.read_tsv(OUTD / "passC.tsv")
    for page in ("f178v", "f179r"):
        with open(TMP / f"ref_{page}.tsv", "w") as f:
            f.write("line\tpos\tsign\n")
            for r in rows:
                if r["line"].startswith(page + "_"):
                    f.write(f"{r['line']}\t{r['pos']}\t{r['sign']}\n")
    return {"f178v": (TMP / "f178v_A.tsv", TMP / "f178v_B.tsv", TMP / "ref_f178v.tsv"),
            "f179r": (H / "f179r/passA.tsv", H / "f179r/passB.tsv", TMP / "ref_f179r.tsv")}


def lattice(pages, lines, matrix=None):
    nb = K.read_confusion(H / "confusion_1572.tsv")
    lat = {}
    for page, (a, b, ref) in pages.items():
        rows, _ = K.from_passes(a, b, ref, nb, False, matrix, 0.3)
        for ln, pos, c, p in rows:
            lat.setdefault((ln, pos), {})[c] = p
    keys = [k for k in lat if k[0] in lines]
    keys.sort(key=lambda k: (lines.index(k[0]), k[1]))
    return [(k, lat[k]) for k in keys]


def learn(lines, out, shuffle=None):
    passes = [str(TMP / "f178v_A.tsv"), str(TMP / "f178v_B.tsv")]
    rows, st = K.learn_confusion(passes, tx_bench.read_tsv(TRUTH), lines, "f178v",
                                 sorted(K.read_key(H / "key_1572_sheet.tsv")))
    hdr = ["learn-confusion (TXE-E): P(read | true), add-0.5 smoothing over %d sheet signs" % st["signs"],
           "learnt from lines: " + " ".join(lines), "passes: harvest f178v passA+passA_L11-23, passB+passB_L11-23"]
    if shuffle is not None:
        rows = K.shuffle_offdiag(rows, shuffle)
        hdr.append("CONTROL: off-diagonal cells permuted within each true row, seed %d" % shuffle)
    K.write_matrix(rows, out, hdr)
    return K.read_matrix(out), rows, st


def write_seq(path, lat, seq, only=None):
    with open(path, "w") as f:
        f.write("line\tpos\tsign\n")
        for ((ln, pos), _), s in zip(lat, seq):
            if only is None or ln in only:
                f.write(f"{ln}\t{pos}\t{s}\n")


def write_topk(path, lat):
    with open(path, "w") as f:
        f.write("line\tpos\tcand\tscore\n")
        for (ln, pos), c in lat:
            for k, v in c.items():
                f.write(f"{ln}\t{pos}\t{k}\t{v:.4f}\n")


def main(mode):
    pages = prep()
    key = K.read_key(H / "key_1572_sheet.tsv")
    model = NgramModel([read_corpus(p) for p in LANG_CORPORA["it16dip"]])
    lm = K.LM(model)
    if mode == "dev":
        md = HERE / "dev_loo"; md.mkdir(exist_ok=True)
        base = lattice(pages, DEV)
        write_topk(md / "base_topk.tsv", base)
        for lam in LAMS:
            write_seq(OUTD / f"passL_lattice_dev_tune_lam{lam:g}.tsv", base, K.viterbi(base, key, lm, lam)[0])
        arms = {"conf": None, "confshuf": 1}
        for arm, shuf in arms.items():
            out = {lam: {} for lam in LAMS}
            topk = []
            for h in DEV:
                rest = [x for x in DEV if x != h]
                M, rows, st = learn(rest, md / f"M_{arm}_minus_{h}.tsv", shuf)
                lh = lattice(pages, DEV, M)
                mix = [(k, dict(c2)) if k[0] == h else (k, c1) for (k, c1), (_, c2) in zip(base, lh)]
                topk += [(k, c) for k, c in mix if k[0] == h]
                for lam in LAMS:
                    seq = K.viterbi(mix, key, lm, lam)[0]
                    out[lam][h] = [(k, s) for (k, _), s in zip(mix, seq) if k[0] == h]
                print(arm, h, "positions", st["positions"], "misses", st["misses"], flush=True)
            write_topk(md / f"{arm}_topk.tsv", topk)
            for lam in LAMS:
                name = "passM_conf_dev_tune" if arm == "conf" else "passM_confshuf_dev_tune"
                path = OUTD / (name + ("" if lam == 4 else f"_lam{lam:g}") + ".tsv")
                with open(path, "w") as f:
                    f.write("line\tpos\tsign\n")
                    for h in DEV:
                        for (ln, pos), s in out[lam][h]:
                            f.write(f"{ln}\t{pos}\t{s}\n")
    elif mode == "eval":
        md = HERE / "eval"; md.mkdir(exist_ok=True)
        M, rows, st = learn(DEV, md / "M_conf_all_dev.tsv")
        lat = lattice(pages, EVAL, M)
        base = lattice(pages, EVAL)
        write_topk(md / "conf_topk.tsv", lat); write_topk(md / "base_topk.tsv", base)
        write_seq(OUTD / "passM_conf_eval_heldout.tsv", lat, K.viterbi(lat, key, lm, 4.0)[0])
        write_seq(OUTD / "passL_lattice_eval_heldout_lam4.tsv", base, K.viterbi(base, key, lm, 4.0)[0])
    elif mode == "keyctl":
        # rule-3 control (b): shuffled-key rank of the real key, whole no.87 f178v+f179r with the all-dev matrix
        M, _, _ = learn(DEV, TMP / "M_all_dev.tsv")
        lines = [r for r in dict.fromkeys(r["line"] for r in K.read_tsv(OUTD / "passC.tsv")) if not r.startswith("f178r")]
        for name, mm in (("conf", M), ("base", None)):
            lat = lattice(pages, lines, mm)
            c = K.control(lat, key, lm, model, 200, 1, 4.0, 64)
            print(name, "lattice rank %d z %.2f shuf mean %.3f max %.3f | top1 rank %d z %.2f" % (
                c["lattice"]["rank"], c["lattice"]["z"], c["lattice"]["shuf_mean"], c["lattice"]["shuf_max"],
                c["top1"]["rank"], c["top1"]["z"]), flush=True)


if __name__ == "__main__":
    main(sys.argv[1])
