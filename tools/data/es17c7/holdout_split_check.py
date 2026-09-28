#!/usr/bin/env python3
"""Within-tome homogeneity split of the es17c7 leave-one-fold-out check (campaign espagnol142-mercy-1648 H4,
28 Sept 2026; the next step tools/data/es17c7/README.md names).

holdout_check.py folds by whole tome (7 folds) and finds a per-fold false-negative spread of 2.0-23.0 percent. The
Cartas inside a tome are chronological newsletters, so cutting each tome into C contiguous chunks makes C date-range
folds per tome (a 'by date range within a tomo' split) without parsing letter headers. For every chunk: build the
model from all text EXCEPT that chunk (the other chunks of the same tome stay in, so the fold tests register/date
homogeneity rather than tome identity), compute real_p05 from in-model windows exactly as holdout_check.py does,
then score SAMPLES held-out windows of length N from the chunk; a window at or below real_p05 is a false negative.
Prints per-fold rates, the blended rate and the spread, for the C values given.

  python3 tools/data/es17c7/holdout_split_check.py --chunks 2 4 [--samples 200] [--n 519]
"""
import argparse, random, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from judge_plaintext import NgramModel, fold, pct, read_corpus  # noqa: E402
HERE = Path(__file__).resolve().parent
FILES = ["memorialhistri13realuoft.txt.gz", "memorialhistri14realuoft.txt.gz", "memorialhistri15realuoft.txt.gz",
         "memorialhistri16realuoft.txt.gz", "memorialhistri17realuoft.txt.gz", "memorialhistri18realuoft.txt.gz",
         "memorialhistri19realuoft.txt.gz"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chunks", type=int, nargs="+", default=[2, 4]); ap.add_argument("--samples", type=int, default=200)
    ap.add_argument("--n", type=int, default=519)
    a = ap.parse_args()
    raw = {f: read_corpus(HERE / f) for f in FILES}
    for C in a.chunks:
        chunks = []  # (file, index, raw_text)
        for f in FILES:
            t = raw[f]; L = len(t)
            for i in range(C):
                chunks.append((f, i, t[i * L // C:(i + 1) * L // C]))
        rates, tot_fn, tot = [], 0, 0
        print(f"== {C} chunk(s) per tome: {len(chunks)} folds, N={a.n}, samples={a.samples}")
        for (f, i, held) in chunks:
            train = [c[2] for c in chunks if not (c[0] == f and c[1] == i)]
            model = NgramModel(train)
            real, _null, _cov = model.controls(a.n, samples=a.samples, seed=1)
            real_p05 = pct(real, 0.05)
            held_text = fold(held); rnd = random.Random(2); fn = 0
            for _ in range(a.samples):
                j = rnd.randrange(0, len(held_text) - a.n)
                if model.score(held_text[j:j + a.n]) <= real_p05:
                    fn += 1
            tot_fn += fn; tot += a.samples; rates.append(100 * fn / a.samples)
            print(f"held_out={f}#{i+1}/{C} real_p05={real_p05:.3f} false_negatives={fn}/{a.samples} ({100*fn/a.samples:.1f}%)")
        print(f"TOTAL false-negative rate ({C}/tome): {tot_fn}/{tot} ({100*tot_fn/tot:.1f}%)")
        print(f"per-fold spread ({C}/tome): {min(rates):.1f}-{max(rates):.1f}% ({max(rates)/max(min(rates),0.01):.1f}x); "
              f"folds over 10%: {sum(1 for r in rates if r>10)}/{len(rates)}")


if __name__ == "__main__":
    main()
