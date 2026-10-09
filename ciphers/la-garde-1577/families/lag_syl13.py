#!/usr/bin/env python3
"""LAG-SYL13 (9 Oct 2026): the LAG-SYL score-gap gate at control error 0.13 (PREREG-LAG-SYL.md, Amendment 2).

Reuses lag_syl.py's solver set-up. T and the 40 shuffled targets (b) are read from the committed families/lag_syl.tsv
(Amendment 1's own values, not re-solved). New solves: 40 matched controls at err 0.13 (seeds 1-40) and the power check at
err 0.13 (held-out seeds 101-110, each against 20 shuffles of its own ciphertext). Statistic: score per cipher token.
Writes families/lag_syl13.tsv and prints the read-out. --report re-prints from the TSV; --check re-solves and exits 1 if the
committed TSV differs. CPU only, 4 processes.
"""
import os, sys
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lag_syl as ls  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lag_syl13.tsv")
NOISE = "0.13"


def load(path):
    res = []
    for line in open(path, encoding="utf-8").read().splitlines()[1:]:
        k, n, s, sh, sc, rec = line.split("\t"); res.append((k, n, int(s), int(sh), float(sc), rec))
    return res


def main():
    jobs = [("ctrl", NOISE, s, 0) for s in range(1, 41)]
    jobs += [("power", NOISE, s, 0) for s in range(101, 111)]
    jobs += [("pshuf", NOISE, s, k) for s in range(101, 111) for k in range(1, 21)]
    with Pool(4, initializer=ls.init) as pool:
        res = pool.map(ls.job, jobs, chunksize=1)
    rows = ["kind\tnoise\tseed\tshuffle\tscore\trecovery"] + ["%s\t%s\t%d\t%d\t%.5f\t%s" % r for r in res]
    text = "\n".join(rows) + "\n"
    if "--check" in sys.argv:
        old = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        sys.exit(0 if old == text else 1)
    open(OUT, "w", encoding="utf-8").write(text)
    report(res)


def report(res):
    prior = load(ls.OUT)
    T = [r[4] for r in prior if r[0] == "target"][0]
    B = [r[4] for r in prior if r[0] == "shuf"]
    A = [r[4] for r in res if r[0] == "ctrl"]
    recs = [float(r[5]) for r in res if r[0] == "ctrl"]
    a05, b95 = ls.pct(A, 0.05), ls.pct(B, 0.95)
    print(f"T={T:.4f} (from lag_syl.tsv)  (b) n={len(B)} p95={b95:.4f} max={max(B):.4f}")
    print(f"(a13) n={len(A)} min={min(A):.4f} p05={a05:.4f} max={max(A):.4f}; recovery mean {sum(recs)/len(recs):.3f}"
          f" min {min(recs):.3f} max {max(recs):.3f}; {sum(r >= 0.60 for r in recs)}/{len(recs)} >= 0.60")
    print(f"  T pct in (a13) {sum(x <= T for x in A)/len(A):.4f}")
    print("COVERAGE 0.13:", "T < p05 (negative extends)" if T < a05 else "T >= p05 (negative does not extend)",
          f"(T={T:.4f}, p05={a05:.4f})")
    gated = passed = 0
    for r in [r for r in res if r[0] == "power"]:
        own = [x[4] for x in res if x[0] == "pshuf" and x[2] == r[2]]
        ok = r[4] > ls.pct(own, 0.95) and r[4] >= a05
        rec = float(r[5])
        if rec >= 0.60:
            gated += 1; passed += ok
        print(f"  power seed {r[2]}: rec {rec:.4f} score {r[4]:.4f} own-shuf p95 {ls.pct(own, 0.95):.4f} -> {'pass' if ok else 'fail'}")
    verdict = "PASS" if gated >= 5 and passed >= 0.8 * gated else ("UNDETERMINED (<5 gated)" if gated < 5 else "FAIL")
    print(f"POWER 0.13: {passed}/{gated} gated held-out controls pass -> {verdict}")


if __name__ == "__main__":
    if "--report" in sys.argv:
        report(load(OUT))
    else:
        main()
