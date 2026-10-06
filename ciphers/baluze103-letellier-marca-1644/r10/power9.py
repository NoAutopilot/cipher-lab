#!/usr/bin/env python3
"""R10-BAL103C power check for the pre-registered 9 shape split (g-tail vs short) on the f.171r control.

Statistic: accuracy of the best one-to-one map from 2 shape classes to the 2 value groups {i} vs {r|s}.
Null: label permutation (the known values shuffled over the same tokens, shape classes fixed).
The gate needs observed accuracy > p95 of the null. For each control size (N tokens, k of value i) this prints
the null p95 when the observed split is perfect, i.e. the best case the shape read could ever give, and whether
a perfect split could pass. Exact enumeration over all C(N,k) label arrangements, for every shape split with
both classes non-empty that is perfect for the observed labels.

  python3 power9.py            # table + the actual f.171r control (N=3, k=1: values s, s, i)
  python3 power9.py --check    # exits non-zero if power9.tsv is stale
"""
import itertools, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "power9.tsv")

def acc(shape, lab):
    n = len(lab)
    a = sum(1 for s, l in zip(shape, lab) if s == l)
    return max(a, n - a) / n

def null_p95_perfect(n, k):
    lab = [1] * k + [0] * (n - k)          # observed labels; a perfect shape split equals them
    shape = lab[:]
    obs = acc(shape, lab)
    vals = sorted(acc(shape, [1 if i in c else 0 for i in range(n)])
                  for c in itertools.combinations(range(n), k))
    p95 = vals[min(len(vals) - 1, int(0.95 * len(vals)))]
    p_ge = sum(1 for v in vals if v >= obs) / len(vals)
    return obs, p95, p_ge, len(vals)

def rows():
    out = ["N\tk_i\tarrangements\tobs_perfect\tnull_p95\tP(null>=obs)\tperfect_can_pass"]
    for n in range(3, 13):
        for k in range(1, n // 2 + 1):
            obs, p95, pge, m = null_p95_perfect(n, k)
            out.append(f"{n}\t{k}\t{m}\t{obs:.3f}\t{p95:.3f}\t{pge:.3f}\t{'yes' if obs > p95 else 'no'}")
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    text = rows()
    if "--check" in sys.argv:
        ok = os.path.exists(OUT) and open(OUT).read() == text
        print("power9.tsv up to date" if ok else "power9.tsv STALE"); sys.exit(0 if ok else 1)
    open(OUT, "w").write(text)
    obs, p95, pge, m = null_p95_perfect(3, 1)
    print(f"f.171r control (calib/sign_table.tsv: 9 aligned s,s,i): N=3 k=1 arrangements={m} "
          f"perfect split acc={obs:.3f} null p95={p95:.3f} P(null>=obs)={pge:.3f} -> "
          f"{'CAN pass' if obs > p95 else 'CANNOT pass by construction'}")
    first = [l for l in text.splitlines()[1:] if l.endswith("yes")]
    print("smallest passable designs:", "; ".join(f"N={l.split()[0]} k={l.split()[1]}" for l in first[:6]))
