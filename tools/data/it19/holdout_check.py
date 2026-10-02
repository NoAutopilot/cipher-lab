#!/usr/bin/env python3
"""Leave-one-file-out real-prose false-negative check for it19 (A2-CAS7, 2 Oct 2026; copied from tools/data/it16dip/holdout_check.py).

Same method as tools/data/es17c/holdout_check.py: for each file, an NgramModel from the OTHER files only; N-letter
windows from the held-out file are scored; a window at or below that model's own real_p05 (windows from its in-model
files) is a false negative. N defaults to 1000. Prints each fold
and the blended rate (rule 3 fold-count paragraph: read the spread, not only the blend).
  python3 tools/data/it19/holdout_check.py [--lang it19|it|it16dip] [--n 1000] [--samples 200]
"""
import argparse, random, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from judge_plaintext import LANG_CORPORA, NgramModel, fold, pct, read_corpus  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lang", default="it19")
    ap.add_argument("--n", type=int, default=1000)
    ap.add_argument("--samples", type=int, default=200)
    a = ap.parse_args()
    files = LANG_CORPORA[a.lang]
    texts = {f: read_corpus(f) for f in files}
    total_fn = total = 0
    rates = []
    for held in files:
        model = NgramModel([texts[f] for f in files if f != held])
        held_text = fold(texts[held])
        real, _null, _cov = model.controls(a.n, samples=a.samples, seed=1)
        p05 = pct(real, 0.05)
        rnd = random.Random(2)
        fn = n = 0
        for _ in range(a.samples):
            if len(held_text) <= a.n:
                break
            j = rnd.randrange(0, len(held_text) - a.n)
            fn += model.score(held_text[j:j + a.n]) <= p05
            n += 1
        total_fn += fn; total += n
        rates.append(fn / max(1, n))
        print(f"held_out={Path(held).name} N={a.n} samples={n} real_p05={p05:.3f} false_negatives={fn}/{n} ({100*fn/max(1,n):.1f}%)")
    print(f"TOTAL {a.lang} false-negative rate: {total_fn}/{total} ({100*total_fn/total:.1f}%); per-fold spread "
          f"{100*min(rates):.1f}-{100*max(rates):.1f}% over {len(files)} folds")


if __name__ == "__main__":
    main()
