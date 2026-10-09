#!/usr/bin/env python3
"""TXE2-LATT step 2 (PREREG-txeng2-2 X3), fixed BEFORE any score of its output. Lattice d (step 1: 10/12, the widest >= 0.5).
Decode: per dev_tune line, an N-best beam (64 hypotheses kept by score, no state recombination) over lattice d with the
objective of tools/key_decode_lattice.viterbi (it16dip 4-gram LM + bonus; lam 4 x log10 prior; unk -0.5); at line end every
surviving hypothesis is re-scored + lam_w x share, share = letters inside lexicon words of >= 3 letters / letters, by
tools/segmenter.segment with lexicon it16dip (PREREG names `it16`, which is no corpus code here; it16dip is the 16th-c.
Italian corpus TXE-E/TX-DECODE use); the best re-scored hypothesis is the line's decode.
Fix rule: output = L (labels.tsv) everywhere, except at tx_doubt's disagree+latt positions (benchmark-tx/txeng/doubt/
dev_tune_signals.tsv, disagree == 1 OR latt == 1: the dev-chosen two-signal combination, 36 of 343, truth-free), where the
decoded sign replaces L's. Never blanket.
lam_w in {0.5, 1, 2, 4}: one output per value; plus the leave-one-line-out choice (lam_w for line h = the value with the
best fixed - broken vs L on the other 11 lines, ties -> smaller lam_w), scored as the registered dev result.
Control (rule 3): the same pipeline under 20 value-shuffled keys (lexicon and LM unchanged), per lam_w; it must not pass
the dev gate (fixed > broken, two-sided sign test p < 0.05 vs L).
  python3 benchmark-tx/txeng2/latt/run_word.py decode   (truth-free; writes outputs, commit before scoring)
  python3 benchmark-tx/txeng2/latt/run_word.py score    (tx_bench paired vs L; writes score.tsv)
"""
import csv, json, random, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(HERE)); sys.path.insert(0, str(ROOT / "benchmark-tx/txeng/conf"))
import key_decode_lattice as K  # noqa: E402
import segmenter as SG  # noqa: E402
from judge_plaintext import LANG_CORPORA, NgramModel, read_corpus  # noqa: E402
import run_conf as RC  # noqa: E402

LAMW = (0.5, 1.0, 2.0, 4.0)
LAM, BEAM, NSHUF = 4.0, 64, 20
DEV = RC.DEV
OUT = HERE / "out"


def rd(p):
    with open(p) as f:
        return list(csv.DictReader(f, delimiter="\t"))


def load_lat(path):
    lat = {}
    for r in rd(path):
        lat.setdefault((r["line"], int(r["pos"])), {})[r["cand"]] = float(r["score"])
    return lat


def nbest(cands_seq, key, lm, lam=LAM, beam=BEAM):
    hyps = [(0.0, "", (), "")]  # score, ngram state, signs, letters
    for cands in cands_seq:
        nxt = []
        for sc, st, sg, tx in hyps:
            for c, p in cands.items():
                pr = lam * K.math.log10(max(p, 1e-6))
                if c in key:
                    st2, s = lm.extend(st, key[c]); t2 = tx + key[c]
                else:
                    st2, s, t2 = st, lm.unk_cost, tx
                nxt.append((sc + pr + s, st2, sg + (c,), t2))
        nxt.sort(key=lambda h: -h[0])
        hyps = nxt[:beam]
    return hyps


def share(text, lex):
    if not text:
        return 0.0
    return sum(len(t) for t, ok in SG.segment(text, lex) if ok and len(t) >= 3) / len(text)


def decode_line(cands_seq, key, lm, lex):
    hyps = nbest(cands_seq, key, lm)
    sh = [share(h[3], lex) for h in hyps]
    out = {}
    for lw in LAMW:
        i = max(range(len(hyps)), key=lambda i: hyps[i][0] + lw * sh[i])
        out[lw] = hyps[i][2]
    return out


def flagged():
    return {(r["line"], int(r["pos"])) for r in rd(ROOT / "benchmark-tx/txeng/doubt/dev_tune_signals.tsv")
            if r["line"] in DEV and (r["disagree"] == "1" or r["latt"] == "1")}


def L_rows():
    return [r for r in rd(RC.OUTD / "labels.tsv") if r["line"] in DEV]


def apply_fix(Lr, dec, flags):
    out = []
    for r in Lr:
        k = (r["line"], int(r["pos"]))
        out.append((r["line"], r["pos"], dec.get(k, r["sign"]) if k in flags else r["sign"]))
    return out


def write(path, rows):
    with open(path, "w") as f:
        f.write("line\tpos\tsign\n")
        for ln, pos, s in rows:
            f.write(f"{ln}\t{pos}\t{s}\n")


def run_key(lat, key, lm, lex):
    """{lam_w: {(line,pos): sign}} decoded per line."""
    res = {lw: {} for lw in LAMW}
    for h in DEV:
        ks = sorted((k for k in lat if k[0] == h), key=lambda k: k[1])
        best = decode_line([lat[k] for k in ks], key, lm, lex)
        for lw in LAMW:
            for k, s in zip(ks, best[lw]):
                res[lw][k] = s
    return res


def decode():
    OUT.mkdir(exist_ok=True)
    lat = load_lat(HERE / "topk_d.tsv")
    key = K.read_key(RC.H / "key_1572_sheet.tsv")
    model = NgramModel([read_corpus(p) for p in LANG_CORPORA["it16dip"]])
    lm = K.LM(model); lex = SG.Lexicon.load("it16dip")
    flags = flagged(); Lr = L_rows()
    miss = [k for k in flags if k not in lat]
    print("flagged", len(flags), "of", len(Lr), "| flagged positions not in lattice:", len(miss))
    real = run_key(lat, key, lm, lex)
    for lw in LAMW:
        write(OUT / f"word_lw{lw:g}.tsv", apply_fix(Lr, real[lw], flags))
        write(OUT / f"word_lw{lw:g}_blanket.tsv", [(ln, p, real[lw].get((ln, int(p)), s)) for ln, p, s in
                                                     ((r["line"], r["pos"], r["sign"]) for r in Lr)])
    rnd = random.Random(20261009)
    for i in range(NSHUF):
        k2 = K.shuffled(key, rnd)
        sh = run_key(lat, k2, lm, lex)
        for lw in LAMW:
            write(OUT / f"shuf{i:02d}_lw{lw:g}.tsv", apply_fix(Lr, sh[lw], flags))
        print("shuffle", i, flush=True)


def score():
    import tx_bench as B
    T = B.read_tsv(RC.TRUTH)
    base = {k: v for k, v in B.load_output([str(RC.OUTD / "labels.tsv")]).items() if k in DEV}
    eb = B.position_errors(T, base)

    def pair(path, lines=None):
        o = B.load_output([str(path)])
        if lines is not None:
            o = {k: v for k, v in o.items() if k in lines}
            b = {k: v for k, v in base.items() if k in lines}
        else:
            b = base
        e0, e1 = B.position_errors(T, b), B.position_errors(T, o)
        com = set(e0) & set(e1)
        fx = sum(1 for k in com if e0[k] and not e1[k]); br = sum(1 for k in com if not e0[k] and e1[k])
        return fx, br, B.sign_test(fx, br), sum(e1[k] for k in com), len(com)

    rows = []
    for lw in LAMW:
        for tag in ("", "_blanket"):
            fx, br, p, w, n = pair(OUT / f"word_lw{lw:g}{tag}.tsv")
            rows.append(dict(arm=f"word_lw{lw:g}{tag}", fixed=fx, broken=br, p=f"{p:.4f}", wrong=w, n=n))
    # leave-one-line-out lam_w choice
    loo = []
    for h in DEV:
        rest = [x for x in DEV if x != h]
        sc = [(pair(OUT / f"word_lw{lw:g}.tsv", rest)[:2], lw) for lw in LAMW]
        lw = max(sc, key=lambda t: (t[0][0] - t[0][1], -t[1]))[1]
        loo.append((h, lw))
        loo_rows = [r for r in rd(OUT / f"word_lw{lw:g}.tsv") if r["line"] == h]
        with open(OUT / "word_loo.tsv", "a" if h != DEV[0] else "w") as f:
            if h == DEV[0]:
                f.write("line\tpos\tsign\n")
            for r in loo_rows:
                f.write(f"{r['line']}\t{r['pos']}\t{r['sign']}\n")
    fx, br, p, w, n = pair(OUT / "word_loo.tsv")
    rows.append(dict(arm="word_LOO (" + " ".join(f"{h[-3:]}:{lw:g}" for h, lw in loo) + ")", fixed=fx, broken=br,
                     p=f"{p:.4f}", wrong=w, n=n))
    for lw in LAMW:
        passes = []
        for i in range(NSHUF):
            fx, br, p, w, n = pair(OUT / f"shuf{i:02d}_lw{lw:g}.tsv")
            passes.append((fx, br, p))
        npass = sum(1 for fx, br, p in passes if fx > br and p < 0.05)
        rows.append(dict(arm=f"shuffled-key x{NSHUF} lw{lw:g}", fixed=sum(x[0] for x in passes) / NSHUF,
                         broken=sum(x[1] for x in passes) / NSHUF, p=f"passes {npass}/{NSHUF}", wrong="", n=""))
    with open(HERE / "score.tsv", "w") as f:
        w = csv.DictWriter(f, ["arm", "fixed", "broken", "p", "wrong", "n"], delimiter="\t"); w.writeheader(); w.writerows(rows)
    print("L wrong", sum(eb.values()), "of", len(eb))
    for r in rows:
        print("\t".join(str(r[c]) for c in ("arm", "fixed", "broken", "p", "wrong", "n")))


if __name__ == "__main__":
    {"decode": decode, "score": score}[sys.argv[1]]()
