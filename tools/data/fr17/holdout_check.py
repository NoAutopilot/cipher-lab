#!/usr/bin/env python3
"""Leave-one-file-out real-prose false-negative check for the fr17 corpus, and the same check on fr16 (the "fr" default) for comparison.

Same method as tools/data/es17c7/holdout_check.py (and tools/data/es17c/holdout_check.py before it), parametrised by
corpus: for each file in the corpus, build an NgramModel from the OTHER files only, compute that model's own real_p05
threshold from windows drawn from the in-model files (exactly as judge() does), then sample N-letter windows from the
held-out file (never used to build that model) and score them. A held-out window "false-negatives" if its score falls
at or below real_p05 -- real held-out prose that the judge would FAIL. Reports the blended rate AND the per-fold
spread, as CLAUDE.md rule 3's es17c/MJ paragraph requires before a FAIL/PASS against the corpus is trusted.

N defaults to 138, decode-2754-bnf-baluze156-1636's own symbol count (specs/decode-2754-bnf-baluze156-1636.json, N=138
K=38, a letter-level cipher, so 138 is the plaintext length in letters); run --N 300 and --N 600 for longer targets).

--against FILES...: instead of leave-one-out, score each --corpus file's windows against ONE model built from FILES (all of
them), with that model's own real_p05 -- the era-mismatch false-negative rate (the pt17-vs-pt18 comparison of V6-PTCORP),
e.g. --against tools/data/fr16/*.gz for what the fr16 fallback does to genuine 1617-1644 prose.

Usage: python3 tools/data/fr17/holdout_check.py [--corpus fr17|fr18] [--N 138] [--samples 200] [--against FILE ...]
"""
import argparse
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from judge_plaintext import LANG_CORPORA, NgramModel, fold, pct, read_corpus  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--corpus", default="fr17", help="LANG_CORPORA key (default fr17; fr, fr16 or fr18 for the comparison)")
    ap.add_argument("--N", type=int, default=138)
    ap.add_argument("--samples", type=int, default=200)
    ap.add_argument("--against", nargs="+", help="score every corpus file against one model built from these files")
    a = ap.parse_args()
    files = LANG_CORPORA[a.corpus]
    N, SAMPLES = a.N, a.samples
    total_fn, total = 0, 0
    per_fold = []
    fixed = NgramModel([read_corpus(f) for f in a.against]) if a.against else None
    for held_out in files:
        model = fixed or NgramModel([read_corpus(f) for f in files if f != held_out])
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
    if fixed:
        print(f"(all folds scored against one model built from: {' '.join(Path(f).name for f in a.against)})")
    print(f"corpus={a.corpus} TOTAL false-negative rate: {total_fn}/{total} ({100*total_fn/total:.1f}%)")
    print(f"corpus={a.corpus} per-fold spread: {min(per_fold):.1f}-{max(per_fold):.1f}% "
          f"({max(per_fold)/max(min(per_fold), 0.01):.1f}x)")


if __name__ == "__main__":
    main()
