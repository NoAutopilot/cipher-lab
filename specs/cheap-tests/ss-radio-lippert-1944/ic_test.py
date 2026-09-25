#!/usr/bin/env python3
"""Cheap test 1 for ss-radio-lippert-1944: index of coincidence of the transcribed
six-line message (letters only, digits excluded as a separate sub-alphabet) against
a matched German-prose control (tools/data/de20, same N) and a uniform-random
control (same K), both at several seeds. LANE B3 worker bSSR, 25 Sept 2026.
"""
import argparse
import gzip
import random
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DE20 = ROOT / "tools" / "data" / "de20"

# ciphertext.txt lines, separators kept for the record but stripped for IC
GROUPS = [
    ("MASS", "QRLZ"),
    ("H9", "OSLY"),
    ("ALAP", "DETL"),
    ("27163", "KSSY"),
    ("J1", "EFLS"),
    ("KOMM", "P4SX"),
]


def ic(tokens):
    n = len(tokens)
    if n < 2:
        return None
    c = Counter(tokens)
    return sum(v * (v - 1) for v in c.values()) / (n * (n - 1))


def target_letters():
    letters = []
    digits = []
    for left, right in GROUPS:
        for grp in (left, right):
            for ch in grp:
                if ch.isdigit():
                    digits.append(ch)
                else:
                    letters.append(ch)
    return letters, digits


def load_de20_letters():
    text = []
    for gz in sorted(DE20.glob("*.txt.gz")):
        with gzip.open(gz, "rt", encoding="utf-8", errors="replace") as f:
            body = f.read()
        # drop Gutenberg header/footer boilerplate by trimming to the marked body if present
        text.append(body)
    joined = "\n".join(text)
    letters = [ch.upper() for ch in joined if ch.isalpha() and ch.isascii()]
    return letters


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", type=int, default=5)
    ap.add_argument("--trials-per-seed", type=int, default=200)
    args = ap.parse_args()

    letters, digits = target_letters()
    n = len(letters)
    k = len(set(letters))
    target_ic = ic(letters)

    print(f"N (letters, digits excluded): {n}")
    print(f"N_all (letters+digits): {n + len(digits)}   digits: {len(digits)} ({''.join(digits)}), distinct digits: {len(set(digits))}")
    print(f"K (distinct letters): {k}  -- {''.join(sorted(set(letters)))}")
    print(f"target IC (letters only, N={n}): {target_ic:.4f}")

    de_pool = load_de20_letters()
    print(f"de20 pool size: {len(de_pool)} ASCII letters")

    de_ics = []
    rng = random.Random(0)
    for seed in range(args.seeds):
        r = random.Random(1000 + seed)
        for _ in range(args.trials_per_seed):
            start = r.randrange(0, len(de_pool) - n)
            sample = de_pool[start:start + n]
            v = ic(sample)
            if v is not None:
                de_ics.append(v)
    de_ics.sort()
    de_mean = sum(de_ics) / len(de_ics)
    de_lo = de_ics[int(0.025 * len(de_ics))]
    de_hi = de_ics[int(0.975 * len(de_ics))]
    print(f"German control (de20, N={n}, {len(de_ics)} draws): mean {de_mean:.4f}  95% range [{de_lo:.4f}, {de_hi:.4f}]")

    unif_ics = []
    for seed in range(args.seeds):
        r = random.Random(2000 + seed)
        alphabet = [chr(ord('A') + i) for i in range(k)]
        for _ in range(args.trials_per_seed):
            sample = [r.choice(alphabet) for _ in range(n)]
            v = ic(sample)
            if v is not None:
                unif_ics.append(v)
    unif_ics.sort()
    unif_mean = sum(unif_ics) / len(unif_ics)
    unif_lo = unif_ics[int(0.025 * len(unif_ics))]
    unif_hi = unif_ics[int(0.975 * len(unif_ics))]
    print(f"Uniform-random control (K={k}, N={n}, {len(unif_ics)} draws): mean {unif_mean:.4f}  95% range [{unif_lo:.4f}, {unif_hi:.4f}]")
    print(f"(flat/uniform expectation 1/K = {1/k:.4f})")


if __name__ == "__main__":
    main()
