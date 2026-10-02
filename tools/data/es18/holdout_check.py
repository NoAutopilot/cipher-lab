#!/usr/bin/env python3
"""Leave-one-file-out real-prose false-negative check for the es18 corpus (CLAUDE.md rule 3, V6-PTCORP / es17c
fold-count paragraphs). For each file, build an NgramModel from the OTHER files only, then sample N-letter windows
from the held-out file and count those scoring at or below that model's own real_p05 (false negatives: real
held-out prose the judge would FAIL). N defaults to 245, na-schonenberg-1678-1716's body length (GAPS4/GAPS5).
  python3 tools/data/es18/holdout_check.py [--lang es18|es17c7] [--N 245] [--samples 200]
"""
import argparse, random, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from judge_plaintext import LANG_CORPORA, NgramModel, fold, pct, read_corpus  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--lang", default="es18"); ap.add_argument("--N", type=int, default=245); ap.add_argument("--samples", type=int, default=200)
    a = ap.parse_args()
    files = LANG_CORPORA[a.lang]
    total_fn, total, rates = 0, 0, []
    for held_out in files:
        model = NgramModel([read_corpus(f) for f in files if f != held_out])
        held_text = fold(read_corpus(held_out))
        real, _null, _cov = model.controls(a.N, samples=a.samples, seed=1)
        real_p05 = pct(real, 0.05)
        rnd = random.Random(2); fn = 0
        for _ in range(a.samples):
            j = rnd.randrange(0, len(held_text) - a.N); w = held_text[j:j + a.N]
            if model.score(w) <= real_p05:
                fn += 1
            total += 1
        total_fn += fn; rates.append(fn / a.samples)
        print(f"held_out={Path(held_out).name} N={a.N} samples={a.samples} real_p05={real_p05:.3f} false_negatives={fn}/{a.samples} ({100*fn/a.samples:.1f}%)")
    print(f"TOTAL false-negative rate: {total_fn}/{total} ({100*total_fn/total:.1f}%); per-fold spread {100*min(rates):.1f}-{100*max(rates):.1f}% ({len(rates)} folds)")


if __name__ == "__main__":
    main()
