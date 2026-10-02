#!/usr/bin/env python3
"""Leave-one-file-out real-prose false-negative check (CLAUDE.md rule 3 fold-count paragraph) for a judge corpus given as
a LANG_CORPORA key (--lang sco16) or a file glob (--glob 'tools/data/en16_repo/*.txt'). Same method as
tools/data/es18/holdout_check.py: per file, a model from the OTHER files, its own real_p05 at N letters, and the share of
N-letter windows of the held-out file scoring at or below it. N defaults to 134 (ciphers/moray-wood-1568's glyph count).
  python3 tools/data/sco16/holdout_check.py [--lang sco16 | --glob GLOB] [--N 134] [--samples 200]
"""
import argparse, glob, random, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from judge_plaintext import LANG_CORPORA, NgramModel, fold, pct, read_corpus  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--lang", default="sco16"); ap.add_argument("--glob"); ap.add_argument("--N", type=int, default=134)
    ap.add_argument("--samples", type=int, default=200)
    a = ap.parse_args()
    files = sorted(glob.glob(a.glob)) if a.glob else LANG_CORPORA[a.lang]
    total_fn, total, rates = 0, 0, []
    for held in files:
        model = NgramModel([read_corpus(f) for f in files if f != held])
        ht = fold(read_corpus(held))
        if len(ht) <= a.N:
            print(f"held_out={Path(held).name} skipped: {len(ht)} letters <= N"); continue
        real, _n, _c = model.controls(a.N, samples=a.samples, seed=1)
        p05 = pct(real, 0.05); rnd = random.Random(2); fn = 0
        for _ in range(a.samples):
            j = rnd.randrange(0, len(ht) - a.N)
            fn += model.score(ht[j:j + a.N]) <= p05
        total += a.samples; total_fn += fn; rates.append(fn / a.samples)
        print(f"held_out={Path(held).name} letters={len(ht)} N={a.N} real_p05={p05:.3f} false_negatives={fn}/{a.samples} ({100*fn/a.samples:.1f}%)")
    print(f"TOTAL false-negative rate: {total_fn}/{total} ({100*total_fn/total:.1f}%); per-fold spread {100*min(rates):.1f}-{100*max(rates):.1f}% ({len(rates)} folds)")


if __name__ == "__main__":
    main()
