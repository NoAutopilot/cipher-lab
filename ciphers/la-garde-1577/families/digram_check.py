#!/usr/bin/env python3
"""Contact/digram test (R15-LAGDIG, 6 Oct 2026) on la-garde-1577's base codes: does a repeated-bigram excess over
within-sequence shuffles separate homophonic (K=26, target sign profile) from running key at N=229 and the measured
error band? Pre-registered in digram_prereg.md (commit 5ecf5fd21) before this script was run.

Step 1 (power) runs on the controls only; the target is scored only if power passes at e=0.23 (AUC >= 0.80 vs both
running-key variants). Statistics depend on token order, so the controls can differ from one another (rule 3).

Run: python3 ciphers/la-garde-1577/families/digram_check.py [--check]   (seeded; --check exits 1 if stale)."""
import contextlib, io, math, os, random, statistics as st, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.append(os.path.join(ROOT, "tools", "families"))
import judge_plaintext as jp  # noqa: E402
import running_key as rk  # noqa: E402
from families import homophonic as h  # noqa: E402

SEEDS, SHUF, ERRS, AUC_GATE = 40, 200, (0.0, 0.10, 0.23, 0.30), 0.80


def rep(seq):
    return sum(n * (n - 1) // 2 for n in Counter(zip(seq, seq[1:])).values())


def mi(seq):
    b = Counter(zip(seq, seq[1:])); n = sum(b.values())
    a, c = Counter(x for x, _ in b.elements()), Counter(y for _, y in b.elements())
    return sum(v / n * math.log(v * n / (a[x] * c[y])) for (x, y), v in b.items())


def zscores(seq, rng):
    r0, m0, R, M = rep(seq), mi(seq), [], []
    s = list(seq)
    for _ in range(SHUF):
        rng.shuffle(s); R.append(rep(s)); M.append(mi(s))
    return (r0 - st.mean(R)) / (st.pstdev(R) or 1e-9), (m0 - st.mean(M)) / (st.pstdev(M) or 1e-9)


def noisy(seq, e, rng):
    seq, pool = list(seq), list(seq)
    for i in range(len(seq)):
        if rng.random() < e:
            seq[i] = rng.choice(pool)
    return seq


def auc(pos, neg):
    return sum((p > q) + 0.5 * (p == q) for p in pos for q in neg) / (len(pos) * len(neg))


def target():
    t = []
    for line in open(os.path.join(HERE, "basecode_cipher.txt")):
        if not line.startswith("#"):
            t += line.split()
    return t


def main():
    tgt = target(); N = len(tgt)
    d = os.path.join(ROOT, "tools", "data", "fr16")
    corp = [jp.read_corpus(os.path.join(d, f)) for f in sorted(os.listdir(d)) if f.endswith(".gz")]
    books = [rk.fold(c) for c in corp]
    dn = os.path.join(ROOT, "tools", "data", "nl_repo")
    nl = rk.fold("\n".join(open(os.path.join(dn, f), encoding="utf-8", errors="replace").read()
                          for f in sorted(os.listdir(dn)) if f.endswith(".txt")))
    rng = random.Random(1577)
    clean = {"homophonic_K26": [], "running_key_fr": [], "running_key_nl": []}
    for s in range(SEEDS):
        with contextlib.redirect_stdout(io.StringIO()):
            msgs, _, _ = h.make_control({}, s + 1, corp, {"N": N, "K": 26, "noise": 0, "profile": "target",
                                                           "target_msgs": [tgt]})
        clean["homophonic_K26"].append(list(msgs[0]))
        bi, ki = rng.sample(range(len(books)), 2)
        a = rng.randrange(len(books[bi]) - N); P = books[bi][a:a + N]
        k = rng.randrange(len(books[ki]) - N); K = books[ki][k:k + N]
        clean["running_key_fr"].append([rk.A[rk.encipher("vig", rk.IDX[x], rk.IDX[y])] for x, y in zip(P, K)])
        k = rng.randrange(len(nl) - N); K = nl[k:k + N]
        clean["running_key_nl"].append([rk.A[rk.encipher("vig", rk.IDX[x], rk.IDX[y])] for x, y in zip(P, K)])
    res = {}
    for e in ERRS:
        for name, v in clean.items():
            res[(name, e)] = [zscores(noisy(q, e, rng), rng) for q in v]
    q_ = lambda v, f: sorted(v)[min(len(v) - 1, int(f * len(v)))]
    out = [f"# R15-LAGDIG digram test; target N={N} K={len(set(tgt))}; controls fr16 (+nl_repo key) N={N}, {SEEDS} seeds,"
           f" {SHUF} shuffles each; prereg digram_prereg.md (5ecf5fd21)",
           "design\terror\tseeds\tZR_mean\tZR_p05\tZR_p95\tZMI_mean\tZMI_p05\tZMI_p95"]
    for (name, e), v in sorted(res.items(), key=lambda x: (x[0][1], x[0][0])):
        R, M = [x[0] for x in v], [x[1] for x in v]
        out.append(f"{name}\t{e:.2f}\t{len(v)}\t{st.mean(R):.2f}\t{q_(R,.05):.2f}\t{q_(R,.95):.2f}\t"
                   f"{st.mean(M):.2f}\t{q_(M,.05):.2f}\t{q_(M,.95):.2f}")
    out.append("error\tAUC_ZR_homo_vs_rkfr\tAUC_ZR_homo_vs_rknl\tAUC_ZMI_homo_vs_rkfr\tAUC_ZMI_homo_vs_rknl")
    A = {}
    for e in ERRS:
        H = res[("homophonic_K26", e)]
        row = [auc([x[i] for x in H], [x[i] for x in res[(r, e)]]) for i in (0, 1) for r in ("running_key_fr", "running_key_nl")]
        A[e] = row
        out.append(f"{e:.2f}\t" + "\t".join(f"{x:.3f}" for x in row))
    power = min(A[0.23][0], A[0.23][1]) >= AUC_GATE
    out.append(f"# power at e=0.23 (min AUC_ZR {min(A[0.23][:2]):.3f} vs gate {AUC_GATE}): {'PASS' if power else 'FAIL'}")
    if power:
        tz = zscores(tgt, rng)
        H, F, L = ([x[0] for x in res[(n, 0.23)]] for n in clean)
        pct = lambda v: sum(x < tz[0] for x in v) / len(v)
        if tz[0] > max(q_(F, .95), q_(L, .95)) and tz[0] >= q_(H, .05):
            verdict = "favours homophonic"
        elif tz[0] < q_(H, .05) and tz[0] <= min(q_(F, .95), q_(L, .95)):
            verdict = "favours running key"
        else:
            verdict = "undecided"
        out.append(f"# target Z_R={tz[0]:.2f} Z_MI={tz[1]:.2f}; pct in homophonic {pct(H):.3f}, rk_fr {pct(F):.3f}, "
                   f"rk_nl {pct(L):.3f}; verdict: {verdict}")
    else:
        out.append("# target not scored (untestable by this statistic at this N/error)")
    text = "\n".join(out) + "\n"
    path = os.path.join(HERE, "digram_check.tsv")
    if "--check" in sys.argv:
        ok = os.path.exists(path) and open(path).read() == text
        print("check:", "ok" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(path, "w").write(text); print(text, end="")


if __name__ == "__main__":
    main()
