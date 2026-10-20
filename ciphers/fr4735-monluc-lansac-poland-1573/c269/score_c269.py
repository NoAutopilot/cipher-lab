#!/usr/bin/env python3
"""MONL-C269A (20 Oct 2026): place a cipher token stream against a window of the ff.140r-141r clear text (PREREG-MONL-C269A.md).

Usage: python3 score_c269.py TOKENS.tsv --window f.140r:L26-f.141r:L11 [--lines L01,...] [--draws 200] [--seed 2690]
       python3 score_c269.py --c268 L21,...,L30 --window ...   (calibration on committed c268 tokens)
TOKENS.tsv: columns line, pos, sign (the reconciled read). Statistic: confirm share of keyed tokens under align_c268.py's DP (key.tsv,
same scores and folds), free start/end inside the window. Control: --draws windows of the same letter length placed at random in a
word-shuffled copy of the whole clear letter (leaf_score.py's control). Also: the whole-letter alignment span and f.139 (c270).
Gate: real > p95 and 0/draws at or above real. Prints one JSON object; writes nothing.
"""
import argparse, json, random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import align_c268 as A


def key():
    k = {}
    for l in list(open(HERE.parent / 'key.tsv', encoding='utf-8'))[1:]:
        f = l.rstrip('\n').split('\t'); k[f[0]] = f[2]
    return k


def tokens(path, c268, lines):
    k = key()
    if c268:
        rows = [l.rstrip('\n').split('\t') for l in open(HERE.parent / 'ciphertext_c268.tsv', encoding='utf-8')][1:]
        rows = [(f[0], f[1], f[2]) for f in rows if f[0] in c268]
    else:
        ls = [l.rstrip('\n').split('\t') for l in open(path, encoding='utf-8')]
        h = ls[0]; rows = [(f[h.index('line')], f[h.index('pos')], f[h.index('sign')]) for f in ls[1:] if f and f[0]]
        if lines:
            rows = [r for r in rows if r[0] in lines]
    return [{'line': a, 'pos': int(b), 'sign': s, 'conf': '', 'value': A.fold(k[s]) if k.get(s) else None} for a, b, s in rows]


def share(toks, clear):
    _, p, a, b = A.align(toks, clear)
    return A.stats(A.classify(toks, clear, p))['confirm_share'], a, b


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('tokens', nargs='?'); ap.add_argument('--c268'); ap.add_argument('--lines')
    ap.add_argument('--window', required=True); ap.add_argument('--draws', type=int, default=200)
    ap.add_argument('--seed', type=int, default=2690)
    a = ap.parse_args()
    toks = tokens(a.tokens, set(a.c268.split(',')) if a.c268 else None, set(a.lines.split(',')) if a.lines else None)
    words = A.load_clear(); keys = [f'{w[0]}:{w[1]}' for w in words]
    w0, w1 = a.window.split('-')
    i0 = keys.index(w0); i1 = len(keys) - 1 - keys[::-1].index(w1)
    clear = ''.join(w[2] for w in words[i0:i1 + 1])
    real, _, _ = share(toks, clear)
    rng = random.Random(a.seed); ws = [w[2] for w in words]; L = len(clear); ctl = []
    for _ in range(a.draws):
        rng.shuffle(ws); s = ''.join(ws); st = rng.randrange(0, len(s) - L + 1)
        ctl.append(share(toks, s[st:st + L])[0])
    ctl.sort(); p95 = ctl[int(0.95 * (len(ctl) - 1))]; ge = sum(c >= real for c in ctl)
    full = ''.join(w[2] for w in words); fs, fa, fb = share(toks, full)
    pos, spans = 0, []
    for w in words:
        if pos + len(w[2]) > fa and pos < fb:
            spans.append(f'{w[0]}:{w[1]}')
        pos += len(w[2])
    c270 = A.fold(open(HERE.parent / 'c270_text.txt', encoding='utf-8').read())
    print(json.dumps({'tokens': len(toks), 'keyed': sum(t['value'] is not None for t in toks), 'window': a.window,
                      'window_letters': L, 'real': real, 'ctl_mean': round(sum(ctl) / len(ctl), 4), 'p95': p95,
                      'max': ctl[-1], 'ge_real': ge, 'gate': bool(real > p95 and ge == 0),
                      'whole_letter': {'share': fs, 'span': [spans[0], spans[-1]] if spans else None},
                      'other_letter_c270': share(toks, c270)[0]}))


if __name__ == '__main__':
    main()
