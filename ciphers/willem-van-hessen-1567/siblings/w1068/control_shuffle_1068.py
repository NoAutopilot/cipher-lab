#!/usr/bin/env python3
"""Control (a), rule 3, WVO-1068-KEY: shuffle-consistency of recurring-sign / recurring-gloss pairing (the bSZL check,
szembek-bk1560 NOTES.md). Statistic = share of glossed occurrences of every recurring class (>= 2 glossed occurrences)
that carry that class's most common gloss. Null = the same gloss letters permuted across the same slots (class
labels fixed), 10000 draws, seed 1068. Two token sets: (H) the tokens both blind passes glossed identically, and (all)
every reconciled token with a letter value. A real rate at or under the null p95 is non-discriminating, not a pass.

Usage: python3 control_shuffle_1068.py [--draws 10000] [--seed 1068]
"""
import argparse, collections, csv, random
from pathlib import Path

HERE = Path(__file__).parent


def stat(cls, vals):
    by = collections.defaultdict(list)
    for c, v in zip(cls, vals):
        by[c].append(v)
    return sum(collections.Counter(v).most_common(1)[0][1] for v in by.values()) / len(vals)


def run(toks, draws, rng):
    cnt = collections.Counter(c for c, _ in toks)
    toks = [(c, v) for c, v in toks if cnt[c] >= 2]
    cls = [c for c, _ in toks]; vals = [v for _, v in toks]
    real = stat(cls, vals)
    null = []
    for _ in range(draws):
        v = vals[:]; rng.shuffle(v); null.append(stat(cls, v))
    null.sort()
    return len(toks), len(set(cls)), real, sum(null) / draws, null[int(0.95 * draws)], sum(x >= real for x in null) / draws


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--draws", type=int, default=10000); ap.add_argument("--seed", type=int, default=1068)
    a = ap.parse_args()
    with open(HERE / "reconcile_1068.tsv", encoding="utf-8") as f:
        rec = list(csv.DictReader(f, delimiter="\t"))
    ok = [r for r in rec if r["value"] not in ("-", "?")]
    for name, toks in (("H (both passes same gloss)", [(r["sign_class"], r["value"]) for r in ok if r["grade"] == "H"]),
                       ("all reconciled", [(r["sign_class"], r["value"]) for r in ok]),
                       ("H, pass B's own raw labels per band (no merging by the reconciler)",
                        [(("b1" if int(r["line"]) <= 3 else "b2" if int(r["line"]) <= 6 else "b3") + r["passB_label"], r["value"])
                         for r in ok if r["grade"] == "H"])):
        n, k, real, mean, p95, p = run(toks, a.draws, random.Random(a.seed))
        verdict = "PASS (real > p95)" if real > p95 else "NON-DISCRIMINATING (real <= p95)"
        print(f"{name}: {n} tokens in {k} recurring classes; real {real:.3f}; shuffled mean {mean:.3f}, p95 {p95:.3f}; "
              f"p {p:.4f} -> {verdict}")


if __name__ == "__main__":
    main()
