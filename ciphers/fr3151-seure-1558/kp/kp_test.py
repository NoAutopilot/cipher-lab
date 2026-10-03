#!/usr/bin/env python3
"""SEURE-KP known-plaintext test (kp/PREREG.md): item 44's f85R clear prefix P against item 43's f81R cipher C.

Uses tools/interlinear_align.run_align (no private DP). Statistic S_r = share of code tokens with status
'agrees' in a single (P, C_r) pair, C_r = first round(r*|P|) signs, r in R; S* = max_r S_r.
Nulls: shuffled-gloss and rotated-gloss (word boundaries kept), N draws each, same max-over-r.
Positive control: P enciphered by a random homophonic key with K signs (K = distinct signs in C_1.00), at
injected sign error 0, 0.15, 0.40.

    python3 kp_test.py P.txt C.tsv OUT.json [--draws 200] [--ctl-seeds 5] [--ctl-draws 50] [--seed 1]
"""
import json, os, random, sys, unicodedata
from collections import Counter
from multiprocessing import Pool
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'tools'))
import interlinear_align as ia  # noqa: E402

R = (0.70, 0.85, 1.00)


def norm_plain(text):
    t = unicodedata.normalize('NFD', text)
    t = ''.join(c for c in t if not unicodedata.combining(c)).lower()
    words = []
    for w in t.split():
        w = ''.join(c for c in w if 'a' <= c <= 'z')
        if w:
            words.append(w)
    return words


def stat(words, signs):
    plain = ' '.join(words)
    nl = sum(len(w) for w in words)
    out = []
    for r in R:
        c = signs[:max(1, round(r * nl))]
        pairs = [{'plain_line': 'P', 'plain_raw': plain, 'cipher_line': 'C', 'cipher_raw': ' '.join('@' + s for s in c)}]
        prep, res, counts, shown = ia.run_align(pairs, code_prefix='@')
        rows = ia.token_rows(prep, res, counts, shown)
        codes = [x for x in rows if x[3] == 'code']
        out.append(sum(x[7] == 'agrees' for x in codes) / len(codes))
    return max(out), out


def reshape(letters, words):
    out, k = [], 0
    for w in words:
        out.append(letters[k:k + len(w)])
        k += len(w)
    return out


def null_draw(args):
    kind, words, signs, seed = args
    rng = random.Random(seed)
    letters = ''.join(words)
    if kind == 'shuffle':
        ls = list(letters)
        rng.shuffle(ls)
        letters = ''.join(ls)
    else:
        n = len(letters)
        off = rng.randint(n // 10, 9 * n // 10)
        letters = letters[off:] + letters[:off]
    return stat(reshape(letters, words), signs)[0]


def encipher(words, K, err, rng):
    letters = ''.join(words)
    freq = Counter(letters)
    alpha = sorted(freq, key=lambda c: -freq[c])
    K = max(K, len(alpha))
    homs = {c: 1 for c in alpha}
    for _ in range(K - len(alpha)):  # extra homophones to the most frequent letters, proportionally
        c = max(alpha, key=lambda c: freq[c] / homs[c])
        homs[c] += 1
    names, key, k = [], {}, 0
    for c in alpha:
        key[c] = ['g%d' % (k + i) for i in range(homs[c])]
        k += homs[c]
    allsigns = ['g%d' % i for i in range(k)]
    out = []
    for ch in letters:
        s = rng.choice(key[ch])
        if rng.random() < err:
            s = rng.choice([x for x in allsigns if x != s])
        out.append(s)
    return out


def dist(vals):
    v = sorted(vals)
    return {'mean': sum(v) / len(v), 'p95': v[int(0.95 * (len(v) - 1))], 'max': v[-1], 'n': len(v)}


def main():
    a = sys.argv[1:]
    ptxt, ctsv, out = a[:3]
    opt = lambda k, d: type(d)(a[a.index(k) + 1]) if k in a else d
    draws, cseeds, cdraws, seed = opt('--draws', 200), opt('--ctl-seeds', 5), opt('--ctl-draws', 50), opt('--seed', 1)
    lines = [l.split('\t', 1)[1] for l in open(ptxt, encoding='utf-8').read().splitlines() if '\t' in l]
    words = norm_plain(' '.join(lines))
    signs = []
    for l in open(ctsv, encoding='utf-8').read().splitlines():
        if '\t' in l and not l.startswith('line'):
            signs += l.split('\t', 1)[1].split()
    nl = sum(len(w) for w in words)
    K = len(set(signs[:nl]))
    res = {'P_letters': nl, 'C_signs': len(signs), 'K_C100': K, 'R': R, 'draws': draws}
    rng = random.Random(seed)
    with Pool(4) as pool:
        # control first (rule 3)
        res['control'] = {}
        for err in (0.0, 0.15, 0.40):
            rows = []
            for s in range(cseeds):
                syn = encipher(words, K, err, rng)
                real = stat(words, syn)[0]
                nd = pool.map(null_draw, [('shuffle', words, syn, seed * 100000 + s * 1000 + d) for d in range(cdraws)])
                d = dist(nd)
                rows.append({'S': real, 'null_p95': d['p95'], 'null_max': d['max'], 'pass': real > d['p95'] and real > d['max']})
            res['control'][str(err)] = {'runs': rows, 'pass_share': sum(r['pass'] for r in rows) / len(rows)}
            print('control err', err, res['control'][str(err)]['pass_share'], [round(r['S'], 3) for r in rows], flush=True)
        S, per = stat(words, signs)
        res['target'] = {'S_star': S, 'S_r': per}
        for kind in ('shuffle', 'rotate'):
            nd = pool.map(null_draw, [(kind, words, signs, seed * 7919 + d) for d in range(draws)])
            res['null_' + kind] = dist(nd)
        res['gate'] = all(S > res['null_' + k]['p95'] and S > res['null_' + k]['max'] for k in ('shuffle', 'rotate'))
    print(json.dumps({k: v for k, v in res.items() if k != 'control'}, indent=1))
    json.dump(res, open(out, 'w'), indent=1)


if __name__ == '__main__':
    main()
