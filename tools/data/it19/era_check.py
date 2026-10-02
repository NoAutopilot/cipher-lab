#!/usr/bin/env python3
"""Era-match check for it19 (A2-CAS7, 2 Oct 2026): N-letter windows from each it19 file scored under another
corpus's model (default "it", the 16th-c. it16 default) against that model's own real_p05 -- the false-negative
rate a c.1800-1830 Italian text would meet under the era-mismatched corpus. Compare with holdout_check.py's
leave-one-file-out rate for it19 itself (same N, same sample count, same seeds).
  python3 tools/data/it19/era_check.py [--against it|it16dip] [--n 1000] [--samples 200]
"""
import argparse, random, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from judge_plaintext import LANG_CORPORA, NgramModel, fold, pct, read_corpus  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--against", default="it")
    ap.add_argument("--n", type=int, default=1000)
    ap.add_argument("--samples", type=int, default=200)
    a = ap.parse_args()
    model = NgramModel([read_corpus(f) for f in LANG_CORPORA[a.against]])
    real, _null, _cov = model.controls(a.n, samples=a.samples, seed=1)
    p05 = pct(real, 0.05)
    tot_fn = tot = 0
    rates = []
    for f in LANG_CORPORA["it19"]:
        t = fold(read_corpus(f))
        rnd = random.Random(2)
        fn = sum(model.score(t[j:j + a.n]) <= p05 for j in (rnd.randrange(0, len(t) - a.n) for _ in range(a.samples)))
        tot_fn += fn; tot += a.samples; rates.append(fn / a.samples)
        print(f"it19 file={Path(f).name} under {a.against} N={a.n} real_p05={p05:.3f} false_negatives={fn}/{a.samples} ({100*fn/a.samples:.1f}%)")
    print(f"TOTAL it19 prose under {a.against}: {tot_fn}/{tot} ({100*tot_fn/tot:.1f}%); per-file spread "
          f"{100*min(rates):.1f}-{100*max(rates):.1f}%")


if __name__ == "__main__":
    main()
