#!/usr/bin/env python3
"""Group B's own held-out proxy (score.py not frozen at the time): a key fitted on one text is applied to the other;
signs unseen in the fit text stay unread (gaps). Statistic: mean 5-gram conditional log10 per scored window
(model5_en.bin). Null: 1000 keys that permute the fitted values across the fit key's signs (value distribution kept).
  python3 heldout.py KEY.tsv --test c1 [--xnull]
Prints JSON: real statistic, null mean/p99.9, percentile. No plaintext of any control."""
import argparse, array, json, os, random, sys
sys.argv0 = sys.argv[0]
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gb

A = 26

def load5(space=False):
    global A
    A = 27 if space else 26
    a = array.array('f'); a.frombytes(open(os.path.join(HERE, 'model5s_en.bin' if space else 'model5_en.bin'), 'rb').read()[:A ** 5 * 4]); return a

def stat(Q, vals):
    s = n = 0
    for i in range(len(vals) - 4):
        w = vals[i:i + 5]
        if None in w: continue
        id_ = 0
        for c in w: id_ = id_ * A + c
        s += Q[id_]; n += 1
    return s / n if n else float('nan'), n

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('key'); ap.add_argument('--test', default='c1')
    ap.add_argument('--xnull', action='store_true'); ap.add_argument('--stream', help='test on this token file (one sign per line, _ = gap) instead of a real text'); ap.add_argument('--n', type=int, default=1000); ap.add_argument('--space', action='store_true', help='X is the word space (value {), 27-symbol model; X kept out of the permutation')
    a = ap.parse_args()
    key = {}
    for ln in open(a.key).read().split('\n')[1:]:
        if ln.strip():
            s, v = ln.split('\t'); key[s] = ord(v) - 97 if len(v) == 1 and (v.isalpha() or v == '{') else None
    st = gb.target_stream(a.test) if not a.stream else [None if t == '_' else t for t in open(a.stream).read().split('\n')]
    if a.xnull: st = [s for s in st if s not in ('X', 'NULLX')]
    Q = load5(a.space)
    real, nw = stat(Q, [key.get(s) if s is not None else None for s in st])
    signs = [x for x in key if not (a.space and x == 'X')]; vals = [key[s] for s in signs]; rng = random.Random(7); null = []
    for _ in range(a.n):
        rng.shuffle(vals); k2 = dict(zip(signs, vals))
        if a.space and 'X' in key: k2['X'] = key['X']
        null.append(stat(Q, [k2.get(s) if s is not None else None for s in st])[0])
    null.sort(); pct = 100.0 * sum(1 for x in null if x < real) / len(null)
    cov = sum(1 for s in st if s is not None and key.get(s) is not None) / sum(1 for s in st if s is not None)
    print(json.dumps({'key': os.path.basename(a.key), 'test': a.test, 'coverage': round(cov, 3), 'windows': nw,
                      'real': round(real, 4), 'null_mean': round(sum(null) / len(null), 4),
                      'null_p999': round(null[int(0.999 * len(null)) - 1], 4), 'percentile': pct}))

if __name__ == '__main__':
    main()
