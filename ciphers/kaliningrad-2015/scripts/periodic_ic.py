#!/usr/bin/env python3
"""Spec test 3: periodic IC on the convention-A sign sequence, periods 2-30, against a shuffle control
(3 seeds). A period whose coset IC beats every shuffle's max at that period by >=0.01 is worth a ROOM flag.
Usage: python3 periodic_ic.py
"""
import random
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ic_analysis import tokenize_signs  # noqa: E402

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "ciphertext.txt"


def ic(signs):
    n = len(signs)
    if n < 2:
        return 0.0
    counts = Counter(signs)
    num = sum(c * (c - 1) for c in counts.values())
    den = n * (n - 1)
    return num / den if den else 0.0


def mean_coset_ic(signs, period):
    vals = []
    for r in range(period):
        coset = signs[r::period]
        if len(coset) >= 2:
            vals.append(ic(coset))
    return sum(vals) / len(vals) if vals else 0.0


if __name__ == "__main__":
    text = SRC.read_text(encoding="utf-8")
    signs = tokenize_signs(text)
    n = len(signs)

    shuffles = []
    for seed in (1, 2, 3):
        s = signs[:]
        random.Random(seed).shuffle(s)
        shuffles.append(s)

    best_period, best_target, best_margin = None, None, -9
    print(f"N={n} periods 2-30, real vs 3 shuffles (seeds 1-3)")
    print(f"{'period':>6} {'real':>8} {'shuf_max':>8} {'margin':>8}")
    for period in range(2, 31):
        real_val = mean_coset_ic(signs, period)
        shuf_vals = [mean_coset_ic(s, period) for s in shuffles]
        shuf_max = max(shuf_vals)
        margin = real_val - shuf_max
        print(f"{period:>6} {real_val:>8.4f} {shuf_max:>8.4f} {margin:>8.4f}")
        if margin > best_margin:
            best_margin, best_period, best_target, best_shuf_max = margin, period, real_val, shuf_max

    print()
    if best_margin >= 0.01:
        print(f"FLAG: best period {best_period}: real {best_target:.4f} vs shuffle max {best_shuf_max:.4f} "
              f"(margin {best_margin:.4f} >= 0.01)")
    else:
        print(f"flat: best period {best_period} at {best_target:.4f} vs shuffle max {best_shuf_max:.4f} "
              f"(margin {best_margin:.4f} < 0.01)")
