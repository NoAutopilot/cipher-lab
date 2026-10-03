#!/usr/bin/env python3
"""Periodicity test (GAPS149, 3 Oct 2026) on la-garde-1577's base codes: IC by period 1..20, the excess over IC_1,
a family-wise max-z statistic and the Friedman estimate, against matched controls at N=229, K=26, fr16, noise 0.23.
The decision rule was pre-registered in periodicity_prereg.md (commit e33a96cd) before this script was run.

Controls: masc, running key, homophonic K=26 (pooled aperiodic null, 40 seeds each) and periodic Vigenere p=2..12
(40 seeds each, power). The statistic depends on token order, and a periodic control can differ from an aperiodic one
on it by construction, so the controls can fail differently from the target (rule 3).

Run: python3 ciphers/la-garde-1577/families/periodicity_check.py [--check]   (seeded; --check exits 1 if stale)."""
import contextlib, io, os, random, statistics as st, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.append(os.path.join(ROOT, "tools", "families"))
import judge_plaintext as jp  # noqa: E402
import running_key as rk  # noqa: E402
from families import homophonic as h  # noqa: E402

ERR, SEEDS, PMAX, KP = 0.23, 40, 20, 0.0778
VIG_P = range(2, 13)


def col_ic(seq, p):
    v = []
    for j in range(p):
        c = seq[j::p]
        n = len(c)
        if n > 1:
            v.append(sum(k * (k - 1) for k in Counter(c).values()) / (n * (n - 1)))
    return sum(v) / len(v)


def profile(seq):
    ic = [col_ic(seq, p) for p in range(1, PMAX + 1)]
    return ic, [x - ic[0] for x in ic]


def friedman(seq, K=26):
    N, kr = len(seq), 1 / K
    d = (N - 1) * col_ic(seq, 1) - N * kr + KP
    return N * (KP - kr) / d if d > 0 else float("inf")


def noisy(seq, p, mode, rng):
    seq, types, pool = list(seq), sorted(set(seq)), list(seq)
    for i in range(len(seq)):
        if rng.random() < p:
            seq[i] = rng.choice(pool) if mode == "profile" else rng.choice([t for t in types if t != seq[i]] or types)
    return seq


def target():
    t = []
    for line in open(os.path.join(HERE, "basecode_cipher.txt")):
        if not line.startswith("#"):
            t += line.split()
    return t


def main():
    tgt = target()
    N = len(tgt)
    d = os.path.join(ROOT, "tools", "data", "fr16")
    files = sorted(f for f in os.listdir(d) if f.endswith(".gz"))
    corp = [jp.read_corpus(os.path.join(d, f)) for f in files]
    books = [rk.fold(c) for c in corp]
    rng = random.Random(149)

    def window():
        bi, ki = rng.sample(range(len(books)), 2)
        s = rng.randrange(len(books[bi]) - N)
        k = rng.randrange(len(books[ki]) - N)
        return books[bi][s:s + N], books[ki][k:k + N]

    null, power = {}, {}
    for s in range(SEEDS):
        P, K = window()
        null.setdefault("masc", []).append(noisy(list(P), ERR, "profile", rng))
        rkey = [rk.A[rk.encipher("vig", rk.IDX[a], rk.IDX[b])] for a, b in zip(P, K)]
        null.setdefault("running_key", []).append(noisy(rkey, ERR, "profile", rng))
        with contextlib.redirect_stdout(io.StringIO()):
            msgs, _, _ = h.make_control({}, s + 1, corp, {"N": N, "K": 26, "noise": ERR, "target_msgs": [tgt]})
        null.setdefault("homophonic_K26", []).append(list(msgs[0]))
        for p in VIG_P:
            key = [rng.randrange(26) for _ in range(p)]
            c = [rk.A[(rk.IDX[a] + key[i % p]) % 26] for i, a in enumerate(P)]
            for mode in ("profile", "uniform"):
                power.setdefault((p, mode), []).append(noisy(c, ERR, mode, rng))

    allnull = [profile(q)[1] for v in null.values() for q in v]
    mu = [st.mean(e[p] for e in allnull) for p in range(PMAX)]
    sd = [st.pstdev(e[p] for e in allnull) or 1e-9 for p in range(PMAX)]

    def zs(seq):
        e = profile(seq)[1]
        return [(e[p] - mu[p]) / sd[p] for p in range(PMAX)]  # index p-1 = period p

    def Z(seq):
        z = zs(seq)
        i = max(range(1, PMAX), key=lambda k: z[k])
        return z[i], i + 1, z

    nullZ = sorted(Z(q)[0] for v in null.values() for q in v)
    z95 = nullZ[int(0.95 * len(nullZ))]

    def detect(seq):
        zmax, pstar, z = Z(seq)
        if zmax <= z95:
            return None
        p0 = next((q for q in range(2, pstar + 1) if pstar % q == 0 and z[q - 1] > 2), pstar)
        mult = [m for m in range(2 * p0, PMAX + 1, p0)]
        if mult and sum(z[m - 1] > 2 for m in mult) < len(mult) / 2:
            return "ambiguous"
        return p0

    out = []
    ti, te = profile(tgt)
    tz, tp, tzz = Z(tgt)
    out.append(f"# GAPS149 periodicity, target N={N} K={len(set(tgt))}; controls fr16 N={N} noise {ERR}, {SEEDS} seeds each; prereg periodicity_prereg.md")
    out.append(f"# family-wise null (masc+running_key+homophonic, {len(nullZ)} seeds): Z p95={z95:.3f} max={nullZ[-1]:.3f}")
    out.append(f"# target: Z={tz:.3f} at p*={tp}; detect={detect(tgt)}; Friedman L_F={friedman(tgt):.2f}")
    out.append("period\ttarget_IC_p\ttarget_E_p\ttarget_z\tnull_E_mean\tnull_E_sd")
    for p in range(PMAX):
        out.append(f"{p+1}\t{ti[p]:.4f}\t{te[p]:+.4f}\t{tzz[p]:+.2f}\t{mu[p]:+.4f}\t{sd[p]:.4f}")
    out.append("design\tnoise\tseeds\tZ_mean\tZ_p05\tZ_p95\ttarget_Z_pct_rank\tdetect_rate(any)\tdetect_rate(divides_p)\tfriedman_median\tfriedman_p05\tfriedman_p95\ttarget_LF_pct_rank")
    tLF = friedman(tgt)

    def row(name, mode, seqs, p=None):
        Zs = sorted(Z(q)[0] for q in seqs)
        dets = [detect(q) for q in seqs]
        any_ = sum(isinstance(x, int) for x in dets) / len(seqs)
        div = (sum(isinstance(x, int) and p % x == 0 for x in dets) / len(seqs)) if p else float("nan")
        LF = sorted(friedman(q) for q in seqs)
        q_ = lambda v, f: v[min(len(v) - 1, int(f * len(v)))]
        rk_ = sum(x < tz for x in Zs) / len(Zs)
        rl = sum(x < tLF for x in LF) / len(LF)
        out.append(f"{name}\t{mode}\t{len(seqs)}\t{st.mean(Zs):.2f}\t{q_(Zs,.05):.2f}\t{q_(Zs,.95):.2f}\t{rk_:.3f}\t{any_:.3f}\t"
                   + (f"{div:.3f}" if p else "-") + f"\t{st.median(LF):.2f}\t{q_(LF,.05):.2f}\t{q_(LF,.95):.2f}\t{rl:.3f}")

    for n, v in null.items():
        row(n, "profile", v)
    for (p, mode), v in sorted(power.items()):
        row(f"vigenere_p{p}", mode, v, p)
    text = "\n".join(out) + "\n"
    path = os.path.join(HERE, "periodicity_check.tsv")
    if "--check" in sys.argv:
        ok = os.path.exists(path) and open(path).read() == text
        print("check:", "ok" if ok else "STALE")
        sys.exit(0 if ok else 1)
    open(path, "w").write(text)
    print(text, end="")


if __name__ == "__main__":
    main()
