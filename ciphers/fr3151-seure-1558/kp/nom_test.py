#!/usr/bin/env python3
"""N8-SEU nomenclator-model known-plaintext test (kp/PREREG-N8.md): item 44's f85R clear prefix P against item
43's f81R cipher C, letter signs 0-1 letters, numerals >= FLOOR as word/name codes taking 0..MAXCH letters.

Uses tools/interlinear_align.run_align (--code-prefix @ with --word-code-prefix %, no private DP).
S_r = share of ALL code tokens (letter signs + word codes) with status 'agrees' in the single pair (P, C_r),
C_r = first round(r*|P|) signs, r in R; S* = max_r S_r. Nulls: shuffled and rotated gloss (kp_test.py).
Matched nomenclator control: P enciphered with word codes (numerals FLOOR-100) on the most frequent words until
the word-code token share matches the target's, letters homophonic over the target's letter-sign inventory,
optional null share, injected sign error at the levels given.

    python3 nom_test.py P.txt C.tsv [C2.tsv] OUT.json --err 0,E/2,E [--draws 200] [--ctl-seeds 5] [--ctl-draws 30]
        [--null-cost X (run_align's charge for a sign taking 0 letters; default -3.0 as before, R8-SEURE)]
        [--control-gate ERR:SHARE (stop before the targets unless the control passes >= SHARE at ERR for every null level)]
"""
import json, os, random, sys
from collections import Counter
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
sys.path.insert(0, HERE)
import interlinear_align as ia  # noqa: E402
from kp_test import norm_plain, reshape, dist  # noqa: E402

R = (0.85, 1.00, 1.13)
FLOOR, MAXCH = 12, 8
ia.WORD_PFX = '%'
NULL_COST = -3.0


def is_word(s):
    return s.isdigit() and int(s) >= FLOOR


def tok(s):
    return ('%' + s) if is_word(s) else ('@' + s)


def stat(words, signs, detail=False):
    plain = ' '.join(words)
    nl = sum(len(w) for w in words)
    out, wd = [], []
    for r in R:
        c = signs[:max(1, round(r * nl))]
        pairs = [{'plain_line': 'P', 'plain_raw': plain, 'cipher_line': 'C', 'cipher_raw': ' '.join(tok(s) for s in c)}]
        prep, res, counts, shown = ia.run_align(pairs, code_prefix='@', max_chunk=MAXCH, null_cost=NULL_COST)
        rows = ia.token_rows(prep, res, counts, shown)
        codes = [x for x in rows if x[3] in ('code', 'num')]
        out.append(sum(x[7] == 'agrees' for x in codes) / len(codes))
        if detail:
            wd.append([(x[2], x[3], x[5] if len(x) > 5 else '', x[7]) for x in rows if x[3] == 'num'])
    return (max(out), out, wd) if detail else (max(out), out)


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


def encipher_nom(words, k_letter, word_share, null_share, err, rng):
    """word codes on the most frequent words (ties random) until code tokens / all tokens >= word_share."""
    wf = Counter(words)
    order = sorted(wf, key=lambda w: (-wf[w], rng.random()))
    coded, ncode = set(), 0
    est_total = sum(len(w) for w in words)
    for w in order:
        if ncode / max(1, est_total) >= word_share:
            break
        coded.add(w)
        ncode += wf[w]
        est_total -= wf[w] * (len(w) - 1)
    nums = rng.sample(range(FLOOR, 101), len(coded))
    wkey = dict(zip(sorted(coded), [str(n) for n in nums]))
    letters = ''.join(w for w in words if w not in coded)
    freq = Counter(letters)
    alpha = sorted(freq, key=lambda c: -freq[c])
    K = max(k_letter, len(alpha))
    homs = {c: 1 for c in alpha}
    for _ in range(K - len(alpha)):
        c = max(alpha, key=lambda c: freq[c] / homs[c])
        homs[c] += 1
    key, k = {}, 0
    for c in alpha:
        key[c] = ['g%d' % (k + i) for i in range(homs[c])]
        k += homs[c]
    allsigns = ['g%d' % i for i in range(k)]
    out = []
    for w in words:
        if w in wkey:
            out.append(wkey[w])
        else:
            out += [rng.choice(key[ch]) for ch in w]
    if null_share:
        nn = round(null_share * len(out) / (1 - null_share))
        for _ in range(nn):
            out.insert(rng.randrange(len(out) + 1), 'n%d' % rng.randrange(3))
    pool_err = allsigns + list(wkey.values())
    out = [(rng.choice([x for x in pool_err if x != s]) if rng.random() < err else s) for s in out]
    return out


def read_signs(path):
    s = []
    for l in open(path, encoding='utf-8').read().splitlines():
        if '\t' in l and not l.startswith('line'):
            s += l.split('\t', 1)[1].split()
    return s


def main():
    a = sys.argv[1:]
    out = [x for x in a if x.endswith('.json')][0]
    pos = [x for x in a if not x.startswith('--') and x != out and (a.index(x) == 0 or not a[a.index(x) - 1].startswith('--'))]
    ptxt, readers = pos[0], pos[1:]
    opt = lambda k, d: type(d)(a[a.index(k) + 1]) if k in a else d
    draws, cseeds, cdraws, seed = opt('--draws', 200), opt('--ctl-seeds', 5), opt('--ctl-draws', 30), opt('--seed', 1)
    errs = [float(x) for x in opt('--err', '0').split(',')]
    nulls = [float(x) for x in opt('--nulls', '0,0.10').split(',')]
    global NULL_COST
    NULL_COST = opt('--null-cost', -3.0)
    gate = opt('--control-gate', '')
    lines = [l.split('\t', 1)[1] for l in open(ptxt, encoding='utf-8').read().splitlines() if '\t' in l]
    words = norm_plain(' '.join(lines))
    nl = sum(len(w) for w in words)
    sA = read_signs(readers[0])
    word_share = sum(is_word(s) for s in sA) / len(sA)
    k_letter = len(set(s for s in sA[:nl] if not is_word(s)))
    res = {'null_cost': NULL_COST, 'P_letters': nl, 'R': R, 'floor': FLOOR, 'max_chunk': MAXCH, 'word_share_A': word_share, 'K_letter_A': k_letter,
           'draws': draws, 'ctl_seeds': cseeds, 'ctl_draws': cdraws}
    rng = random.Random(seed)
    with Pool(4) as pool:
        res['control'] = {}
        for ns in nulls:
            for err in errs:
                rows = []
                for s in range(cseeds):
                    syn = encipher_nom(words, k_letter, word_share, ns, err, rng)
                    real = stat(words, syn)[0]
                    nd = pool.map(null_draw, [('shuffle', words, syn, seed * 100000 + s * 1000 + d) for d in range(cdraws)])
                    d = dist(nd)
                    rows.append({'S': real, 'n_signs': len(syn), 'n_word': sum(is_word(x) for x in syn), 'null_p95': d['p95'],
                                 'null_max': d['max'], 'pass': real > d['p95'] and real > d['max']})
                key = 'nulls%.2f_err%.3f' % (ns, err)
                res['control'][key] = {'runs': rows, 'pass_share': sum(r['pass'] for r in rows) / len(rows)}
                print('control', key, res['control'][key]['pass_share'], [round(r['S'], 3) for r in rows], flush=True)
        if gate:
            gerr, gshare = (float(x) for x in gate.split(':'))
            gk = ['nulls%.2f_err%.3f' % (ns, gerr) for ns in nulls]
            ok = all(res['control'][k]['pass_share'] >= gshare for k in gk)
            res['control_gate'] = {'cells': gk, 'share': gshare, 'pass': ok}
            if not ok:
                print('CONTROL BELOW GATE', gk, flush=True)
                json.dump(res, open(out, 'w'), indent=1, ensure_ascii=False)
                sys.exit(3)
        res['targets'] = {}
        for rp in readers:
            signs = read_signs(rp)
            S, per, wd = stat(words, signs, detail=True)
            t = {'C_signs': len(signs), 'n_word': sum(is_word(x) for x in signs), 'S_star': S, 'S_r': per,
                 'word_codes_at_best_r': wd[per.index(S)]}
            for kind in ('shuffle', 'rotate'):
                nd = pool.map(null_draw, [(kind, words, signs, seed * 7919 + d) for d in range(draws)])
                t['null_' + kind] = dist(nd)
            t['gate'] = all(S > t['null_' + k]['p95'] and S > t['null_' + k]['max'] for k in ('shuffle', 'rotate'))
            res['targets'][os.path.basename(rp)] = t
            print(os.path.basename(rp), json.dumps({k: v for k, v in t.items() if k != 'word_codes_at_best_r'}), flush=True)
    json.dump(res, open(out, 'w'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    main()
