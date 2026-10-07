#!/usr/bin/env python3
"""D07-CEP21 (7 Oct 2026): language-score control for the one f.21v flip the R-bar witness-shape read makes, L10.6 S69 (f) ->
X_THETA2 (r, two bars). Real = passD.tsv with L10.6 relabelled X_THETA2. Null A = passD.tsv with ONE random letter-bearing f.21v
token (any sign other than L10.6) relabelled X_THETA2, n draws: does putting an r anywhere gain as much? Null B (in-family) = each
other S13/S69 token relabelled X_THETA2 alone, so a score that simply prefers r over f/g shows up.
  python3 s13s69_control.py [--n 500] [--seed 1]     (run from harvest/f21v/lookalike)"""
import csv, random, sys
from pathlib import Path
H = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(H))
import decode_control as dc  # noqa: E402

def passages(rows):
    d = {}
    for r in rows: d.setdefault(r['passage'], []).append(r['sign_id'].strip())
    return d

def main():
    n = int(sys.argv[sys.argv.index('--n') + 1]) if '--n' in sys.argv else 500
    rng = random.Random(int(sys.argv[sys.argv.index('--seed') + 1]) if '--seed' in sys.argv else 1)
    base = list(csv.DictReader(open(H / 'f21v/passD.tsv'), delimiter='\t'))
    m = dc.load_map(['X_THETA2=r']); jp = dc.jp
    model = jp.NgramModel([jp.read_corpus(p) if hasattr(jp, 'read_corpus') else jp.load_text(p) for p in jp.LANG_CORPORA['it16dip']])
    idx, cnt = {}, {}
    for i, r in enumerate(base):
        cnt[r['passage']] = cnt.get(r['passage'], 0) + 1
        idx[f"{r['passage']}.{cnt[r['passage']]}"] = i
    t = idx['L10.6']; assert base[t]['sign_id'] == 'S69'
    cur = dc.score(model, passages(base), m)
    rr = [dict(r) for r in base]; rr[t]['sign_id'] = 'X_THETA2'; real = dc.score(model, passages(rr), m)
    print(f'passD (L10.6 S69 f) {cur:.4f}; L10.6 -> X_THETA2 (r) {real:.4f}; gain {real - cur:+.4f}')
    pool = [i for i, r in enumerate(base) if i != t and r['sign_id'] not in ('X_THETA2', 'S67', 'S73', 'S54', 'X_NEW', '?', '')]
    xs = []
    for _ in range(n):
        rr = [dict(r) for r in base]; rr[rng.choice(pool)]['sign_id'] = 'X_THETA2'
        xs.append(dc.score(model, passages(rr), m))
    xs.sort(); ge = sum(x >= real for x in xs)
    print(f'null A: one random token -> r, n={n}, pool {len(pool)}: mean {sum(xs)/n:.4f} p95 {xs[int(.95*n)]:.4f} max {xs[-1]:.4f}; '
          f'>= real {ge}/{n} (p={(ge+1)/(n+1):.3f})')
    for k in ('L06.2.15', 'L11.4', 'L11.22'):
        rr = [dict(r) for r in base]; rr[idx[k]]['sign_id'] = 'X_THETA2'
        print(f'null B: {k} ({base[idx[k]]["sign_id"]}) -> r alone: {dc.score(model, passages(rr), m) - cur:+.4f}')

if __name__ == '__main__':
    main()
