#!/usr/bin/env python3
"""Leave-one-file-out real-prose false-negative check for the fr1810 corpus, and the same check on fr18 for comparison.

Same method as tools/data/es17c7/holdout_check.py (and tools/data/es17c/holdout_check.py before it), parametrised by
corpus: for each file in the corpus, build an NgramModel from the OTHER files only, compute that model's own real_p05
threshold from windows drawn from the in-model files (exactly as judge() does), then sample N-letter windows from the
held-out file (never used to build that model) and score them. A held-out window "false-negatives" if its score falls
at or below real_p05 -- real held-out prose that the judge would FAIL. Reports the blended rate AND the per-fold
spread, as CLAUDE.md rule 3's es17c/MJ paragraph requires before a FAIL/PASS against the corpus is trusted.

N defaults to 325, berthier-napoleon-1812's own group count (specs/berthier-napoleon-1812.json: 325 groups, about one
code per word, so the plaintext is longer in letters -- 325 is the conservative, shorter end of the band).

Usage: python3 tools/data/fr1810/holdout_check.py [--corpus fr1810|fr18] [--N 325] [--samples 200]
"""
import argparse
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from judge_plaintext import LANG_CORPORA, NgramModel, fold, pct, read_corpus  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--corpus", default="fr1810", help="LANG_CORPORA key (default fr1810; fr18 for the comparison)")
    ap.add_argument("--N", type=int, default=325)
    ap.add_argument("--samples", type=int, default=200)
    a = ap.parse_args()
    files = LANG_CORPORA[a.corpus]
    N, SAMPLES = a.N, a.samples
    total_fn, total = 0, 0
    per_fold = []
    for held_out in files:
        train = [read_corpus(f) for f in files if f != held_out]
        model = NgramModel(train)
        held_text = fold(read_corpus(held_out))
        real, _null, _cov = model.controls(N, samples=SAMPLES, seed=1)
        real_p05 = pct(real, 0.05)
        rnd = random.Random(2)
        fn = 0
        for _ in range(SAMPLES):
            if len(held_text) <= N:
                break
            j = rnd.randrange(0, len(held_text) - N)
            w = held_text[j:j + N]
            sc = model.score(w)
            if sc <= real_p05:
                fn += 1
            total += 1
        total_fn += fn
        per_fold.append(100 * fn / SAMPLES)
        print(f"corpus={a.corpus} held_out={held_out.name} N={N} samples={SAMPLES} real_p05={real_p05:.3f} "
              f"false_negatives={fn}/{SAMPLES} ({100*fn/SAMPLES:.1f}%)", flush=True)
    print(f"corpus={a.corpus} TOTAL false-negative rate: {total_fn}/{total} ({100*total_fn/total:.1f}%)")
    print(f"corpus={a.corpus} per-fold spread: {min(per_fold):.1f}-{max(per_fold):.1f}% "
          f"({max(per_fold)/max(min(per_fold), 0.01):.1f}x)")


if __name__ == "__main__":
    main()
