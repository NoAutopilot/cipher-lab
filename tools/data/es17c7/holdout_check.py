#!/usr/bin/env python3
"""Leave-one-file-out real-prose false-negative check for the es17c7 corpus (all seven Cartas tomes).

Same method as tools/data/es17c/holdout_check.py, extended from 3 files/folds to 7: for each of the seven
es17c7 files, build an NgramModel from the OTHER six files only, then sample N-letter windows from the held-out
file (never used to build that model) and score them. A held-out window "false-negatives" if its score falls at
or below that model's own real_p05 threshold (computed from windows drawn from the six in-model files) -- i.e.
real held-out prose that the judge would FAIL. Mirrors the calibration check CLAUDE.md rule 3 (V6-PTCORP lesson,
extended by the es17c/MJ paragraph on fold count) asks for before trusting a FAIL/PASS.
"""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from judge_plaintext import NgramModel, fold, pct, read_corpus  # noqa: E402

HERE = Path(__file__).resolve().parent
FILES = [
    "memorialhistri13realuoft.txt.gz", "memorialhistri14realuoft.txt.gz", "memorialhistri15realuoft.txt.gz",
    "memorialhistri16realuoft.txt.gz", "memorialhistri17realuoft.txt.gz", "memorialhistri18realuoft.txt.gz",
    "memorialhistri19realuoft.txt.gz",
]
N = 519  # matches the target's own code-only reading length (m2/reading_codes_only.txt)
SAMPLES = 200


def main():
    total_fn, total = 0, 0
    per_fold = []
    for held_out in FILES:
        train = [read_corpus(HERE / f) for f in FILES if f != held_out]
        model = NgramModel(train)
        held_text = fold(read_corpus(HERE / held_out))
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
        print(f"held_out={held_out} N={N} samples={SAMPLES} real_p05={real_p05:.3f} false_negatives={fn}/{SAMPLES} ({100*fn/SAMPLES:.1f}%)")
    print(f"TOTAL false-negative rate: {total_fn}/{total} ({100*total_fn/total:.1f}%)")
    print(f"per-fold spread: {min(per_fold):.1f}-{max(per_fold):.1f}% ({max(per_fold)/max(min(per_fold), 0.01):.1f}x)")


if __name__ == "__main__":
    main()
