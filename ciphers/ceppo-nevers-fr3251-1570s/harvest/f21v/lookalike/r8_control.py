#!/usr/bin/env python3
"""D22-CEPPO21 (6 Oct 2026): language-score control for the f.21v 8-family under the R-8 witness shape read.
Real = passD.tsv as labelled (the R-8 read agrees with every decided tile). Null = the same number of S65 (et) labels
placed at random among f.21v's S65/S80 positions (the value set is fixed; only WHICH 8s are et changes), n draws.
Also scores reader A's labelling (S65 at the 13 L01-06 split tiles) as the rejected alternative.
  python3 r8_control.py [--n 500] [--seed 1]     (run from harvest/f21v/lookalike)"""
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
    eights = [i for i, r in enumerate(base) if r['sign_id'] in ('S65', 'S80')]
    k = sum(base[i]['sign_id'] == 'S65' for i in eights)
    real = dc.score(model, passages(base), m)
    tiles = [r for f in ('f21v_L01-06_tiles.tsv', 'f21v_L07-11_tiles.tsv') for r in csv.DictReader(open(f), delimiter='\t')]
    a_s65 = {(t['passage'], t['pos']) for t in tiles if t['candidates'] in ('S65,S80', 'S80,S65') and t['A'] == 'S65'}
    pos_in = {}
    alt = [dict(r) for r in base]
    for r in alt:
        pos_in[r['passage']] = pos_in.get(r['passage'], 0) + 1
        if (r['passage'], str(pos_in[r['passage']])) in a_s65: r['sign_id'] = 'S65'
    a_score = dc.score(model, passages(alt), m)
    xs = []
    for _ in range(n):
        rr = [dict(r) for r in base]
        pick = set(rng.sample(eights, k))
        for i in eights: rr[i]['sign_id'] = 'S65' if i in pick else 'S80'
        xs.append(dc.score(model, passages(rr), m))
    xs.sort(); ge = sum(x >= real for x in xs)
    print(f'8-tokens {len(eights)}, S65 {k}; real (R-8 labels) {real:.4f}; reader A labels ({len(a_s65)} more S65) {a_score:.4f}')
    print(f'random placement of {k} S65 among the 8s: n={n} mean {sum(xs)/n:.4f} p95 {xs[int(.95*n)]:.4f} max {xs[-1]:.4f}; '
          f'>= real {ge}/{n} (p={(ge+1)/(n+1):.3f})')

if __name__ == "__main__" and "--per-token" not in sys.argv:
    main()

def per_token():
    """--per-token: flip each 8-token alone (S65<->S80) and print the score change (negative = the current label scores better)."""
    base = list(csv.DictReader(open(H / 'f21v/passD.tsv'), delimiter='\t'))
    m = dc.load_map(['X_THETA2=r']); jp = dc.jp
    model = jp.NgramModel([jp.read_corpus(p) if hasattr(jp, 'read_corpus') else jp.load_text(p) for p in jp.LANG_CORPORA['it16dip']])
    real = dc.score(model, passages(base), m); cnt = {}
    for i, r in enumerate(base):
        cnt[r['passage']] = cnt.get(r['passage'], 0) + 1
        if r['sign_id'] not in ('S65', 'S80'): continue
        rr = [dict(x) for x in base]; rr[i]['sign_id'] = 'S80' if r['sign_id'] == 'S65' else 'S65'
        print(f"{r['passage']}.{cnt[r['passage']]}\t{r['sign_id']}\tflip {dc.score(model, passages(rr), m) - real:+.4f}")

if __name__ == '__main__' and '--per-token' in sys.argv:
    per_token()
