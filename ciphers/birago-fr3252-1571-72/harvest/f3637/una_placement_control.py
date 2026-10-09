#!/usr/bin/env python3
"""UNA-BIR3252 placement control (PREREG-UNA.md measure 3): the real-key score per letter of passD_v4 against n draws in which
the same number of changed rows is drawn at random from the open rule-pair rows of adjudicate_in.tsv (R-8, R-hash, R-6,
R-bar, R-dot pairs; r37_L01 pos 9 already settled) and each is set to a random member of its pair, on top of passD_v3.
Usage: python3 una_placement_control.py [--n 500] [--seed 1] [--base passD_v3.tsv --cand passD_v4.tsv]
UNA2-BIR3252 (9 Oct 2026) added --base/--cand: draws go on top of --base, k = rows where --cand differs from --base, and the
pool drops rule-pair rows already changed between passD_v3 and --base (so --base passD_v4 --cand passD_v5 tests the increment)."""
import argparse, csv, random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / 'ceppo-nevers-fr3251-1570s/harvest'))
import decode_control as dc  # noqa: E402
jp = dc.jp
PAIRS = [{'S65', 'S80'}, {'S24', 'S88'}, {'S54', 'S74'}, {'S69', 'X_THETA2'}, {'S23', 'S97'}]

def load(p):
    rows = list(csv.DictReader(open(p), delimiter='\t')); pas = {}
    for r in rows: pas.setdefault(r['passage'], []).append(r['sign_id'].strip())
    return rows, pas

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--n', type=int, default=500); ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--base', default='passD_v3.tsv'); ap.add_argument('--cand', default='passD_v4.tsv')
    a = ap.parse_args(); rng = random.Random(a.seed)
    m = dc.load_map(['X_THETA2=r'])
    model = jp.NgramModel([jp.read_corpus(p) if hasattr(jp, 'read_corpus') else jp.load_text(p) for p in jp.LANG_CORPORA['it16dip']])
    _, v3 = load(HERE / a.base); _, v4 = load(HERE / a.cand); _, v0 = load(HERE / 'passD_v3.tsv')
    k = sum(1 for p in v3 for a_, b in zip(v3[p], v4[p]) if a_ != b)
    pool = [(r['line'], int(r['pos']), sorted({r['cand_1'], r['cand_2']})) for r in csv.DictReader(open(HERE / 'adjudicate_in.tsv'), delimiter='\t')
            if {r['cand_1'], r['cand_2']} in PAIRS and not (r['line'] == 'r37_L01' and r['pos'] == '9')
            and v0[r['line']][int(r['pos']) - 1] == v3[r['line']][int(r['pos']) - 1]]
    real = dc.score(model, v4, m); base = dc.score(model, v3, m)
    draws = []
    for _ in range(a.n):
        p = {kk: list(v) for kk, v in v3.items()}
        for line, pos, cands in rng.sample(pool, k):
            p[line][pos - 1] = rng.choice(cands)
        draws.append(dc.score(model, p, m))
    ge = sum(1 for d in draws if d >= real); draws.sort()
    print(f"changed rows k={k}; pool {len(pool)} open rule-pair rows; base {a.base} {base:.4f}; cand {a.cand} (real) {real:.4f}; "
          f"draws n={a.n} median {draws[len(draws)//2]:.4f} p95 {draws[int(.95*len(draws))]:.4f} max {draws[-1]:.4f}; "
          f"p = {ge}/{a.n} = {ge/a.n:.3f}")
