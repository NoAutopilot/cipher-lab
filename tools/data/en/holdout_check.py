#!/usr/bin/env python3
"""Leave-one-file-out real-prose false-negative / shuffled-null false-positive check for the
LANG_CORPORA["en"] judge corpus (CLAUDE.md rule 3 fold-count amendment, 25 Sept 2026 20:01 UTC).

For each file in FILES, build an NgramModel from the OTHER file(s) only, draw SAMPLES windows of N
letters from the held-out file (never used to build that model), and for each window:
  - false negative: the real window fails judge()'s PASS condition (score <= real_p05, using
    thresholds computed from the training model's own controls -- mirrors tools/data/es17c/holdout_check.py).
  - false positive (null): the SAME window, letter-shuffled, clears both thresholds (score > null_p99
    and score > real_p05) -- mirrors tools/data/fr18/README.md's method, which reports both rates.

Run with --files to name >2 files (after extending the corpus) and --dir to point at a different folder.
"""
import argparse
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from judge_plaintext import NgramModel, fold, pct, read_corpus  # noqa: E402

HERE = Path(__file__).resolve().parent
DEFAULT_FILES = ["../pg1661_holmes.txt", "../pg2701_mobydick.txt"]
NS = [200, 500]
SAMPLES = 200


def run(files, ns=NS, samples=SAMPLES):
    paths = [HERE / f for f in files]
    for N in ns:
        total_fn = total_fp = total = 0
        rows = []
        for held_out in paths:
            train = [read_corpus(p) for p in paths if p != held_out]
            model = NgramModel(train)
            held_text = fold(read_corpus(held_out))
            real, null, _cov = model.controls(N, samples=samples, seed=1)
            real_p05, null_p99 = pct(real, 0.05), pct(null, 0.99)
            rnd = random.Random(2)
            fn = fp = n = 0
            for _ in range(samples):
                if len(held_text) <= N:
                    break
                j = rnd.randrange(0, len(held_text) - N)
                w = held_text[j:j + N]
                sc = model.score(w)
                if sc <= real_p05:
                    fn += 1
                ws = list(w)
                rnd.shuffle(ws)
                ssc = model.score("".join(ws))
                if ssc > null_p99 and ssc > real_p05:
                    fp += 1
                n += 1
            total_fn += fn; total_fp += fp; total += n
            row = f"N={N} held_out={held_out.name} samples={n} real_p05={real_p05:.3f} null_p99={null_p99:.3f} false_negatives={fn}/{n} ({100*fn/n:.1f}%) null_false_positives={fp}/{n} ({100*fp/n:.1f}%)"
            print(row)
            rows.append((held_out.name, fn, fp, n))
        print(f"N={N} TOTAL false-negative rate: {total_fn}/{total} ({100*total_fn/total:.1f}%); "
              f"TOTAL null false-positive rate: {total_fp}/{total} ({100*total_fp/total:.1f}%)")
        spread = max(r[1] / r[3] for r in rows) - min(r[1] / r[3] for r in rows)
        print(f"N={N} per-fold false-negative spread: {spread:.3f}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--files", nargs="+", default=DEFAULT_FILES, help="corpus files, relative to this script's dir")
    ap.add_argument("--n", nargs="+", type=int, default=NS)
    ap.add_argument("--samples", type=int, default=SAMPLES)
    a = ap.parse_args()
    run(a.files, ns=a.n, samples=a.samples)


if __name__ == "__main__":
    main()
