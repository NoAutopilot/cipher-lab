#!/usr/bin/env python3
"""Apply Ormond-Longford Cipher 1/2/3 keys to the Ormond-Arran 1678 ~20 groups
and run a matched control: coverage of 1,000 random draws of 20 integers in
the same observed range [32,732] against each key's defined codes, so the
target's raw coverage count can be judged against chance (CLAUDE.md rule 3).
Exits non-zero if the target groups in this file drift from ciphertext.txt.
"""
import csv, random, sys, os

TARGET = [445, 342, 726, 91, 33, 425, 93, 57, 384, 54, 700, 720,
          732, 573, 526, 32, 643, 214, 55, 440]

HERE = os.path.dirname(os.path.abspath(__file__))
CIPHERTEXT = os.path.join(HERE, "..", "ciphertext.txt")


def check_target_matches_ciphertext():
    with open(CIPHERTEXT) as f:
        text = f.read()
    import re
    nums = [int(n) for n in re.findall(r"\d+", text)]
    if nums != TARGET:
        print(f"STALE: TARGET {TARGET} != ciphertext.txt groups {nums}", file=sys.stderr)
        sys.exit(1)


def load_key(path):
    key = {}
    with open(path) as f:
        r = csv.DictReader(f, delimiter="\t")
        for row in r:
            key[int(row["code"])] = (row["gloss"], row["grade"])
    return key


def coverage(codes, key):
    return sum(1 for c in codes if c in key)


def control(key, n_target, lo, hi, trials=1000, seed=1):
    rng = random.Random(seed)
    hits = []
    for _ in range(trials):
        draw = [rng.randint(lo, hi) for _ in range(n_target)]
        hits.append(coverage(draw, key))
    hits.sort()
    mean = sum(hits) / len(hits)
    p99 = hits[int(0.99 * len(hits))]
    return mean, p99, hits


def main():
    check_target_matches_ciphertext()
    lo, hi = min(TARGET), max(TARGET)
    for name in ["cipher1", "cipher2", "cipher3"]:
        path = os.path.join(HERE, f"{name}.tsv")
        key = load_key(path)
        cov = coverage(TARGET, key)
        mean, p99, hits = control(key, len(TARGET), lo, hi)
        matched = [(c, key[c]) for c in TARGET if c in key]
        print(f"\n== {name} (key entries: {len(key)}, observed range {lo}-{hi}) ==")
        print(f"target coverage: {cov}/{len(TARGET)} ({100*cov/len(TARGET):.1f}%)")
        print(f"control (1000 draws, same range): mean {mean:.2f}, 99th pctile {p99}")
        verdict = "ABOVE control 99th pctile" if cov > p99 else "at or below control 99th pctile"
        print(f"verdict: {verdict}")
        print("matched groups:", matched)


if __name__ == "__main__":
    main()
