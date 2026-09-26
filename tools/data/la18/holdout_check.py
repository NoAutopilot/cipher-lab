#!/usr/bin/env python3
"""Leave-one-file-out false-negative rate for tools/data/la18, per CLAUDE.md rule 3's fold-count paragraph.

Builds the judge's NgramModel from two of the three Zaluski tomes, samples 200 windows of N letters from the
third (held out, never used to fit that model), and counts how many of those genuine-prose windows would FAIL
the model's own real_p05 threshold -- a false negative. Repeats holding out each tome in turn.

Usage: python3 tools/data/la18/holdout_check.py [--n 400] [--samples 200]
"""
import argparse, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from judge_plaintext import NgramModel, read_corpus, pct

FILES = ["zaluski_epistolae_t1.txt.gz", "zaluski_epistolae_t2.txt.gz", "zaluski_epistolae_t3.txt.gz"]
HERE = Path(__file__).resolve().parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=400)
    ap.add_argument("--samples", type=int, default=200)
    a = ap.parse_args()

    total_fn, total_n = 0, 0
    rows = []
    for held in FILES:
        train = [read_corpus(HERE / f) for f in FILES if f != held]
        model = NgramModel(train)
        held_text = read_corpus(HERE / held)
        held_model = NgramModel([held_text])  # only to draw held-out windows from its own raw text
        real_p05 = pct(model.controls(a.n, samples=a.samples, seed=1)[0], 0.05)
        import random
        rnd = random.Random(2)
        raw = held_model.raw
        fn = 0
        for _ in range(a.samples):
            j = rnd.randrange(0, max(1, len(raw) - a.n))
            w = raw[j:j + a.n]
            if model.score(w) <= real_p05:
                fn += 1
        rows.append((held, a.n, a.samples, real_p05, fn))
        total_fn += fn
        total_n += a.samples

    for held, n, samples, real_p05, fn in rows:
        print(f"held_out={held} N={n} samples={samples} real_p05={real_p05:.3f} "
              f"false_negatives={fn}/{samples} ({100*fn/samples:.1f}%)")
    print(f"TOTAL false-negative rate: {total_fn}/{total_n} ({100*total_fn/total_n:.1f}%)")
    rates = [100 * fn / samples for _, _, samples, _, fn in rows]
    print(f"per-fold spread: {min(rates):.1f}% - {max(rates):.1f}% (3 files: fewer than 5 -- "
          f"CLAUDE.md rule 3, treat as a corpus of unknown reliability, not a single trustworthy number)")


if __name__ == "__main__":
    main()
