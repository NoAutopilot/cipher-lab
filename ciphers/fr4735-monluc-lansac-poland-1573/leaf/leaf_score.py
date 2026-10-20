#!/usr/bin/env python3
"""MONL-LEAF (20 Oct 2026): score a 1-line decode of a candidate leaf against a window of the ff.140r-141r clear text.

Usage: python3 leaf_score.py SIGNS.tsv --window f.140r:L27-f.140r:L30 [--draws 200] [--seed 2710]
SIGNS.tsv: one sign id per row (column 'sign'), the blind read of one cipher line, or --c268 L26 to take a committed c268 line.
Statistic (PREREG-MONL-LEAF.md): align_c268.py's DP alignment (key.tsv, Tomokiyo's Cipher 1 table; same scores, same folds)
of the line against the window's letters; confirm share of keyed tokens. Control: --draws windows of the same letter length
placed at random in a word-shuffled copy of the whole clear letter (shuffle and placement redrawn every draw); p95 and margin.
Gate: real - p95 >= 0.229 (SUP-MONLUC's L26-L30 margin, 0.675 - 0.446). Prints one JSON line; writes nothing.
"""
import argparse, json, random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import align_c268 as A

GATE = 0.229


def tokens(path=None, c268=None):
    key = {}
    for l in list(open(HERE.parent / 'key.tsv', encoding='utf-8'))[1:]:
        f = l.rstrip('\n').split('\t'); key[f[0]] = f[2]
    if c268:
        rows = [l.rstrip('\n').split('\t') for l in open(HERE.parent / 'ciphertext_c268.tsv', encoding='utf-8')][1:]
        signs = [f[2] for f in rows if f[0] == c268]
    else:
        lines = [l.rstrip('\n').split('\t') for l in open(path, encoding='utf-8')]
        i = lines[0].index('sign'); signs = [f[i] for f in lines[1:] if len(f) > i and f[i]]
    return [{'line': 'X', 'pos': n + 1, 'sign': s, 'conf': '', 'value': A.fold(key[s]) if key.get(s) else None}
            for n, s in enumerate(signs)]


def window(spec):
    a, b = spec.split('-')
    words = A.load_clear(); keys = [f'{w[0]}:{w[1]}' for w in words]
    i0 = keys.index(a); i1 = len(keys) - 1 - keys[::-1].index(b)
    return ''.join(w[2] for w in words[i0:i1 + 1]), words


def share(toks, clear):
    _, p, _, _ = A.align(toks, clear)
    return A.stats(A.classify(toks, clear, p))['confirm_share']


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('signs', nargs='?'); ap.add_argument('--c268'); ap.add_argument('--window', required=True)
    ap.add_argument('--draws', type=int, default=200); ap.add_argument('--seed', type=int, default=2710)
    a = ap.parse_args()
    toks = tokens(a.signs, a.c268)
    clear, words = window(a.window)
    real = share(toks, clear)
    rng = random.Random(a.seed); ws = [w[2] for w in words]; L = len(clear); ctl = []
    for _ in range(a.draws):
        rng.shuffle(ws); s = ''.join(ws); st = rng.randrange(0, len(s) - L + 1)
        ctl.append(share(toks, s[st:st + L]))
    ctl.sort(); p95 = ctl[int(0.95 * (len(ctl) - 1))]
    print(json.dumps({'line': a.c268 or a.signs, 'window': a.window, 'keyed': sum(t['value'] is not None for t in toks),
                      'tokens': len(toks), 'real': real, 'ctl_mean': round(sum(ctl) / len(ctl), 4), 'p95': p95,
                      'max': ctl[-1], 'margin': round(real - p95, 4), 'gate': GATE,
                      'pass': real - p95 >= GATE}))


if __name__ == '__main__':
    main()
