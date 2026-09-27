#!/usr/bin/env python3
"""bench_score_baseline.py: scores tools/key_crossmatch.py's existing statistic against BENCHMARK.tsv, per
split, with a 95 percent Wilson interval (BENCH-FREEZE, 27 Sept 2026, unit U4). No new solver: every row's
`gate_admitted` column in BENCHMARK.tsv already records whether tools/key_crossmatch.py's operating gate
(stat >= 3.292 for ciphertexts of >= 100 tokens and coverage >= 0.5, KEY-CROSSMATCH.md XMATCH-CAL) admits that
pair, taken straight from KEY-CROSSMATCH.tsv / KEY-CROSSMATCH-CAL.tsv at the time the benchmark was built.

`truth=positive` rows are the only-correct-key relations; `truth=wrong-key`/`wrong-period` rows are relations
that should NOT be admitted. `gate_admitted=yes` on a positive row is a true positive; on a negative row it is
a false positive. Answers CODEX-REVIEW-2026-09-27.md section 7's point directly: the 13/13 in-sample number is
not an out-of-sample rate -- this script reports the eval-split number instead, whatever it is.

Usage:
  python3 tools/bench_score_baseline.py [BENCHMARK.tsv]
"""
import argparse
import csv
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT = ROOT / 'BENCHMARK.tsv'
Z = 1.96  # 95 percent


def wilson(x, n, z=Z):
    if n == 0:
        return (float('nan'), float('nan'), float('nan'))
    p = x / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    margin = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (p, max(0.0, center - margin), min(1.0, center + margin))


def fmt(w):
    p, lo, hi = w
    return f"{p:.3f} [{lo:.3f},{hi:.3f}]" if p == p else "n/a"


def load_rows(path):
    lines = Path(path).read_text().splitlines()
    return list(csv.DictReader(lines[1:], delimiter='\t'))


def score(rows, split):
    pos = [r for r in rows if r['split'] == split and r['truth'] == 'positive']
    neg = [r for r in rows if r['split'] == split and r['truth'] in ('wrong-key', 'wrong-period')]
    tp = sum(1 for r in pos if r['gate_admitted'] == 'yes')
    fn = len(pos) - tp
    fp = sum(1 for r in neg if r['gate_admitted'] == 'yes')
    tn = len(neg) - fp
    prec = wilson(tp, tp + fp)
    rec = wilson(tp, tp + fn)
    by_kind = {}
    for kind in ('wrong-key', 'wrong-period'):
        sub = [r for r in neg if r['truth'] == kind]
        admit = sum(1 for r in sub if r['gate_admitted'] == 'yes')
        by_kind[kind] = (admit, len(sub), wilson(admit, len(sub)) if sub else None)
    return dict(tp=tp, fn=fn, fp=fp, tn=tn, precision=prec, recall=rec, by_kind=by_kind,
                n_pos=len(pos), n_neg=len(neg))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('benchmark', nargs='?', default=str(DEFAULT))
    args = ap.parse_args()
    rows = load_rows(args.benchmark)
    for split in ('dev', 'eval'):
        s = score(rows, split)
        print(f"== {split} ==")
        print(f"  positives: {s['n_pos']} (admitted {s['tp']}) -> recall {fmt(s['recall'])} (Wilson 95%)")
        print(f"  negatives: {s['n_neg']} (admitted/FP {s['fp']})")
        print(f"  precision (TP/(TP+FP)): {fmt(s['precision'])}  TP={s['tp']} FP={s['fp']} FN={s['fn']} TN={s['tn']}")
        for kind, (admit, n, w) in s['by_kind'].items():
            if n:
                print(f"  {kind}: {n} cases, {admit} admitted (false positive) -> FP rate {fmt(w)}")
            else:
                print(f"  {kind}: 0 cases in this split")


if __name__ == '__main__':
    main()
