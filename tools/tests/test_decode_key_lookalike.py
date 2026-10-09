#!/usr/bin/env python3
"""Offline tests for tools/decode_key.py --lookalike (MQS-LOOKALIKE-SLIPS, 9 Oct 2026). No network.

  python3 tools/tests/test_decode_key_lookalike.py                offline tests (parsing, one planted Danzay slip)
  python3 tools/tests/test_decode_key_lookalike.py --controls [--seeds 10] [--k 6] [--out FILE]
        the controls of tools/tests/PREREG-MQS-LOOKALIKE-SLIPS.md (R planted-slip recall, F false flags on the true
        pair, N shuffled-pair null at the planted positions, D unmodified stream). Never writes into a target folder.
"""
import argparse, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import decode_key as dk

DANZAY_CFG = os.path.join(HERE, 'decode_configs', 'fr20140-danzay-1557.json')
fails = []


def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok:
        fails.append(msg)


def danzay():
    cfg = json.load(open(DANZAY_CFG, encoding='utf-8'))
    target = os.path.join(ROOT, cfg['target'])
    return target, [dict(cfg.get('defaults', {}), **j) for j in cfg['jobs']]


_CW = {}


def fresh_cw():
    """A Crossword of the Danzay stream; the model and streams are built once and copied per use."""
    if 'base' not in _CW:
        target, jobs = danzay()
        _CW['base'] = dk.Crossword(target, jobs, dk.lm_load('fr16'))
        _CW['h'] = set()
        for job in jobs:
            recs, _ = dk.graded_recs(target, job)
            for r in recs:
                if r['kind'] == 'sign' and r['grade'] == 'H' and r['value'] and not r.get('null'):
                    _CW['h'].add(r['sign'])
    b = _CW['base']
    cw = object.__new__(dk.Crossword)
    cw.__dict__.update(b.__dict__)
    cw.S = [[list(e) for e in s] for s in b.S]
    cw._seg = b._seg   # cache keyed by the window string: safe to share
    return cw


def letter_codes(cw, nmin=5):
    """H-graded codes whose value is one letter, n >= nmin: {code: folded letter}."""
    out = {}
    for c, n in cw.count.items():
        v = cw.current(c)
        if c in _CW['h'] and n >= nmin and v is not None and len(cw.fold(v)) == 1:
            out[c] = cw.fold(v)
    return out


def plant(cw, a, b, k, rnd):
    """Rewrite k random occurrences of a as b (value b's). Returns the planted positions."""
    pos = rnd.sample(cw.occ(a), k)
    bv = cw.fold(cw.current(b))
    for kk, i in pos:
        cw.S[kk][i] = [b, bv]
    return set(pos)


def offline():
    check(dk.parse_pairs('A~B, c~d') == [('A', 'B'), ('c', 'd')], 'parse_pairs reads A~B,C~D')
    for bad in ('AB', 'A~A', '~B'):
        try:
            dk.parse_pairs(bad); ok = False
        except SystemExit:
            ok = True
        check(ok, f'parse_pairs refuses {bad!r}')
    cw = fresh_cw()
    L = letter_codes(cw)
    codes = sorted(L, key=lambda c: -cw.count[c])
    a = codes[0]; b = next(c for c in codes[1:] if L[c] != L[a])
    rnd = random.Random(1)
    pos = plant(cw, a, b, 1, rnd)
    rows = dk.lookalike_scan(cw, [(a, b)])
    hit = [r for r in rows if (r['stream'], r['index']) in pos]
    check(len(hit) == 1 and hit[0]['flag'], f'must catch: one planted {a}->{b} slip flagged (gain '
                                            f'{hit[0]["gain"]:.1f})' if hit else 'planted slip examined')
    other = [r for r in rows if (r['stream'], r['index']) not in pos]
    fr = sum(r['flag'] for r in other) / max(1, len(other))
    check(fr <= 0.10, f'must NOT flag: ordinary occurrences of {a}/{b} flagged {fr:.3f} (<= 0.10)')
    check(all(r['code'] in (a, b) for r in rows), 'only the declared pair is examined')
    cw2 = fresh_cw()
    check(not any(r['code'] == 'NO-SUCH' for r in dk.lookalike_scan(cw2, [('NO-SUCH', a)])),
          'a code with no twin value is skipped, never scored')


def controls(seeds, k, out):
    cw0 = fresh_cw()
    L = letter_codes(cw0)
    codes = sorted(L)
    rows_out = ['seed\tcontrol\tpair\tplanted\tflagged\texamined\tfalse_flags']
    R = [0, 0]; F = [0, 0]; N = [0, 0]; D = [0, 0]
    for seed in range(seeds):
        rnd = random.Random(1000 + seed)
        while True:
            a, b = rnd.sample(codes, 2)
            if L[a] != L[b] and cw0.count[a] >= k:
                break
        cw = fresh_cw()
        pos = plant(cw, a, b, k, rnd)
        rows = dk.lookalike_scan(cw, [(a, b)])
        hit = sum(r['flag'] for r in rows if (r['stream'], r['index']) in pos)
        oth = [r for r in rows if (r['stream'], r['index']) not in pos]
        ff = sum(r['flag'] for r in oth)
        R[0] += hit; R[1] += k; F[0] += ff; F[1] += len(oth)
        rows_out.append(f'{seed}\tR/F\t{a}~{b}\t{k}\t{hit}\t{len(oth)}\t{ff}')
        c = rnd.choice([x for x in codes if L[x] not in (L[a], L[b])])
        rowsN = dk.lookalike_scan(cw, [(b, c)])
        hn = sum(r['flag'] for r in rowsN if (r['stream'], r['index']) in pos)
        N[0] += hn; N[1] += k
        rows_out.append(f'{seed}\tN\t{b}~{c}\t{k}\t{hn}\t\t')
        cwd = fresh_cw()
        rowsD = dk.lookalike_scan(cwd, [(a, b)])
        dd = sum(r['flag'] for r in rowsD)
        D[0] += dd; D[1] += len(rowsD)
        rows_out.append(f'{seed}\tD\t{a}~{b}\t0\t\t{len(rowsD)}\t{dd}')
        print(rows_out[-3], rows_out[-2], rows_out[-1], sep='\n', flush=True)
    f = lambda x: x[0] / max(1, x[1])
    summ = (f'R {R[0]}/{R[1]} = {f(R):.3f} (gate >= 0.50); F {F[0]}/{F[1]} = {f(F):.3f} (gate <= 0.10); '
            f'N {N[0]}/{N[1]} = {f(N):.3f}, R - N = {f(R) - f(N):.3f} (gate >= 0.30); D {D[0]}/{D[1]} = {f(D):.3f} '
            f'(gate <= 0.10); k {k}, seeds {seeds}')
    print(summ)
    if out:
        open(out, 'w', encoding='utf-8').write('\n'.join(rows_out) + '\n# ' + summ + '\n')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--controls', action='store_true'); ap.add_argument('--seeds', type=int, default=10)
    ap.add_argument('--k', type=int, default=6); ap.add_argument('--out')
    a = ap.parse_args()
    if a.controls:
        controls(a.seeds, a.k, a.out)
    else:
        offline()
        print('FAILURES: ' + '; '.join(fails) if fails else 'all lookalike tests passed')
        sys.exit(1 if fails else 0)
