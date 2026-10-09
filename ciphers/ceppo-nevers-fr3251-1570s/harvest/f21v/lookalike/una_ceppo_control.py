#!/usr/bin/env python3
"""UNA-CEPPO (9 Oct 2026): language-score gate and placement control for the one f.21v token the R-s witness-shape read decides,
L07.34 (passD S26 = s, conf L). Real pair: passD with L07.34 = S26 (s) vs L07.34 = X_NEW (unkeyed, U). Null S = one random
letter-bearing f.21v token (not L07.34) relabelled S26 (s), n draws, against the L07.34 = s score; null U = one random
letter-bearing token relabelled X_NEW, n draws, against the L07.34 = U score. Both nulls can vary on the score (the statistic).
  python3 una_ceppo_control.py [--n 500] [--seed 1]     (run from harvest/f21v/lookalike)"""
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
    t = idx['L07.34']; assert base[t]['sign_id'] == 'S26'
    s_score = dc.score(model, passages(base), m)
    rr = [dict(r) for r in base]; rr[t]['sign_id'] = 'X_NEW'; u_score = dc.score(model, passages(rr), m)
    print(f'L07.34 = S26 (s) {s_score:.4f}; L07.34 = X_NEW (U) {u_score:.4f}; s minus U {s_score - u_score:+.4f}')
    pool = [i for i, r in enumerate(base) if i != t and r['sign_id'] not in ('X_THETA2', 'S67', 'S73', 'S54', 'X_NEW', 'X_POUND', '?', '')]
    for lab, real in (('S26', s_score), ('X_NEW', u_score)):
        xs = []
        for _ in range(n):
            rr = [dict(r) for r in base]; rr[t]['sign_id'] = 'X_NEW' if lab == 'S26' else 'S26'
            rr[rng.choice(pool)]['sign_id'] = lab
            xs.append(dc.score(model, passages(rr), m))
        xs.sort(); ge = sum(x >= real for x in xs)
        print(f'null {lab}: L07.34 held at the other value, one random token -> {lab}, n={n}, pool {len(pool)}: mean {sum(xs)/n:.4f} '
              f'p95 {xs[int(.95*n)]:.4f} max {xs[-1]:.4f}; >= real {ge}/{n} (p={(ge+1)/(n+1):.3f})')

if __name__ == '__main__':
    main()
