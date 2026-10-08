#!/usr/bin/env python3
"""Score a blind primitive-level read of a joined-hand Duployé control against its printed known answer (D2-DUPL, 8 Oct 2026).

The control is the "VERSION 3" exercise of the Institut sténographique de France's Méthode de sténographie Duployé
perfectionnée (1905, Internet Archive cihm_84595), whose French translation the manual prints on the next page; the key
is dupl_control/version3_key.tsv. Statistic (pre-registered in PREREG-D2-DUPL.md): edit accuracy 1 - lev(key, read)/len(key)
over the whole exercise as one sequence (word boundaries dropped), plus a chance baseline of random same-length readings.
Diagnostics (not gated): the same with A/O and E/I merged (loop size), and R/L/G/K rising-slant confusions.

  python3 scripts/duploye_joined_control.py --key dupl_control/version3_key.tsv --read dupl_control/read_control.txt
"""
import argparse, random
from duploye_control import INVENTORY, lev


def load_key(p):
    seq = []
    for ln in open(p, encoding="utf-8"):
        if ln.startswith("#") or not ln.strip():
            continue
        seq += ln.rstrip("\n").split("\t")[1].split()
    return seq


def load_read(p):
    return [t for t in open(p, encoding="utf-8").read().replace("|", " ").split() if t in INVENTORY]


def acc(k, r):
    return 1 - lev(k, r) / len(k)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--key", required=True); ap.add_argument("--read", required=True)
    ap.add_argument("--seed", type=int, default=8); ap.add_argument("--trials", type=int, default=500)
    a = ap.parse_args()
    k, r = load_key(a.key), load_read(a.read)
    rng = random.Random(a.seed)
    null = sorted(acc(k, [rng.choice(INVENTORY) for _ in r]) for _ in range(a.trials))
    m = {"O": "A", "I": "E"}
    km, rm = [m.get(x, x) for x in k], [m.get(x, x) for x in r]
    print(f"key n={len(k)} read n={len(r)}")
    print(f"accuracy={acc(k, r):.3f} chance_mean={sum(null)/len(null):.3f} chance_p95={null[int(.95*len(null))]:.3f}")
    print(f"diag loop-merged (A=O, E=I) accuracy={acc(km, rm):.3f}")
    ks = [x for x in k if x in "RLGK"]; rs = [x for x in r if x in "RLGK"]
    print(f"diag rising-slant subsequence (R/L/G/K) key={''.join(ks)} read={''.join(rs)} accuracy={acc(ks, rs) if ks else 0:.3f}")


if __name__ == "__main__":
    main()
