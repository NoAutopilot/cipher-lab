#!/usr/bin/env python3
"""Leave-one-file-out real-prose false-negative check for the de19 corpus.

For each of the three de19 files, build an NgramModel from the OTHER two files only, then sample
N-letter windows from the held-out file (never used to build that model) and score them. A held-out
window "false-negatives" if its score falls at or below that model's own real_p05 threshold (computed
from windows drawn from the two in-model files) -- i.e. real held-out prose that the judge would FAIL.
Mirrors the es17c/pt18/en calibration check CLAUDE.md rule 3 asks for before trusting a FAIL/PASS, and
CLAUDE.md rule 3's fold-count amendment (report per-fold spread, not only the blended rate; a corpus
under ~5 source files gives a spread of unknown reliability).
"""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from judge_plaintext import NgramModel, fold, pct, read_corpus  # noqa: E402

HERE = Path(__file__).resolve().parent
FILES = [
    "pg2404_Italienische_Reise_Band1.txt.gz",
    "pg2405_Italienische_Reise_Band2.txt.gz",
    "pg31538_Peter_Schlemihl.txt.gz",
]
N = 164  # hessen-1824's own transcription length
SAMPLES = 200


def main():
    total_fn, total = 0, 0
    rates = []
    for held_out in FILES:
        train = [read_corpus(HERE / f) for f in FILES if f != held_out]
        model = NgramModel(train)
        held_text = fold(read_corpus(HERE / held_out))
        real, _null, _cov = model.controls(N, samples=SAMPLES, seed=1)
        real_p05 = pct(real, 0.05)
        rnd = random.Random(2)
        fn = 0
        n_this = 0
        for _ in range(SAMPLES):
            if len(held_text) <= N:
                break
            j = rnd.randrange(0, len(held_text) - N)
            w = held_text[j:j + N]
            sc = model.score(w)
            if sc <= real_p05:
                fn += 1
            n_this += 1
        total_fn += fn
        total += n_this
        rates.append(fn / n_this if n_this else float("nan"))
        print(f"held_out={held_out} N={N} samples={n_this} real_p05={real_p05:.3f} false_negatives={fn}/{n_this} ({100*fn/n_this:.1f}%)")
    print(f"BLENDED false-negative rate: {total_fn}/{total} ({100*total_fn/total:.1f}%)")
    print(f"per-fold spread: {max(rates) - min(rates):.3f} (min {100*min(rates):.1f}% max {100*max(rates):.1f}%)")
    print(f"fold count: {len(FILES)} (under the ~5-file reliability floor CLAUDE.md rule 3 names -- read this spread as of unknown reliability, not just wide or narrow)")


if __name__ == "__main__":
    main()
