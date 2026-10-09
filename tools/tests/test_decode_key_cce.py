#!/usr/bin/env python3
"""Offline tests for tools/decode_key.py --error-matrix (MQS-CCE-MATRIX, 9 Oct 2026). No network.

  python3 tools/tests/test_decode_key_cce.py                  offline tests (sibling-key loading, an identical key
                                                              examines nothing, one heavy planted fixture, one clean)
  python3 tools/tests/test_decode_key_cce.py --controls [--seeds 10] [--draws 200] [--rule best|gain] [--out FILE]
        the controls of tools/tests/PREREG-MQS-CCE-MATRIX.md (K3, K2, D0, DATE, POS; p = 1% row reported when K3 and
        K2 are both 10/10). Material: the Danzay stream in memory; never writes into a target folder.
"""
import argparse, os, random, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import test_decode_key_lookalike as tl   # the Danzay Crossword harness (fresh_cw), shared with --lookalike
dk = tl.dk
fails = []


def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok:
        fails.append(msg)


def own_key(cw):
    """{code: folded current value} for every code with a value."""
    return {c: cw.fold(cw.current(c)) for c in cw.count if cw.current(c) is not None}


def sibling(A, rnd, keep=0.25):
    """A synthetic key of the same office (PREREG): A's value kept on a random 25% of its single-letter and null
    codes and on every longer code; the other 75% of single-letter and null codes have their values permuted."""
    pool = sorted(c for c, v in A.items() if len(v) <= 1)
    moved = [c for c in pool if rnd.random() >= keep]
    vals = [A[c] for c in moved]
    rnd.shuffle(vals)
    S = dict(A)
    S.update(zip(moved, vals))
    return S


def plant(cw, A, S, p, rnd):
    """Rewrite round(p x N) single-letter positions with a sibling code for the same letter. Returns positions."""
    N = sum(len(s) for s in cw.S)
    want = round(p * N)
    cand = [(k, i) for k, s in enumerate(cw.S) for i, (t, v) in enumerate(s) if t is not None and v and len(v) == 1]
    rnd.shuffle(cand)
    done = set()
    for k, i in cand:
        if len(done) >= want:
            break
        L = cw.S[k][i][1]
        alts = sorted(c for c, v in S.items() if v == L and A.get(c) != L)
        if not alts:
            continue
        c2 = rnd.choice(alts)
        cw.S[k][i] = [c2, A[c2]]
        done.add((k, i))
    return done


def offline():
    cw = tl.fresh_cw()
    A = own_key(cw)
    with tempfile.TemporaryDirectory() as d:
        kp = os.path.join(d, 'sib.tsv')
        first = sorted(A)[:3]
        open(kp, 'w').write('code\tvalue\n' + ''.join(f'{c}\tx|y\n' for c in first) + 'NOTACODE\ta\n' + f'{first[0]}x\t?\n')
        sv = dk.cce_sibling(d, 'sib.tsv', cw)
        check(sorted(sv) == first and all(v == 'X' for v in sv.values()),
              'cce_sibling keys only document codes, first of a|b, folded')
    cg = dk.CceGains(cw)
    f, e = dk.cce_stat(cg, A)
    exc = sum(1 for s in cw.S for c, v in s if c in A and v is not None and v != A[c])
    check(e == exc, f'an identical sibling key examines only positions whose own value is not the key value '
          f'(exceptions: {e} = {exc})')
    rnd = random.Random(1)
    S = sibling(A, rnd)
    check(sum(S[c] != A[c] for c in A) > 0 and sorted(S.values()) == sorted(A.values()),
          'synthetic sibling keeps the value multiset and changes some codes')
    clean = dk.cce_test(dk.CceGains(cw), S, draws=50, seed=1)
    check(not clean['contaminating'], f"must NOT flag: clean Danzay stream vs a sibling (rate {clean['rate']:.3f}, "
          f"p95 {clean['null_p95']:.3f})")
    cw2 = tl.fresh_cw()
    pos = plant(cw2, A, S, 0.06, random.Random(2))
    heavy = dk.cce_test(dk.CceGains(cw2), S, draws=50, seed=1)
    check(heavy['contaminating'], f"catches: 6% planted from the sibling (rate {heavy['rate']:.3f}, p95 "
          f"{heavy['null_p95']:.3f}, {len(pos)} planted)")
    m = dk.cce_matrix(heavy['rows'])
    check(all(set(x) >= {'code', 'own', 'sibling', 'n', 'flagged', 'mean_gain', 'recurrent'} for x in m) and
          any(x['recurrent'] for x in m), 'the per-code matrix has its columns and at least one recurrent code')


def controls(seeds, draws, out, rule):
    rows = ['row\tseed\tplanted\tS_flagged\tS_examined\tS_rate\tS_null_p95\tS_p\tS_contaminating\tC_rate\tC_null_p95\tC_p'
            '\tC_contaminating\tplanted_flagged\tall_flagged']
    cw0 = tl.fresh_cw()
    A = own_key(cw0)
    tally = {}
    plist = [('K3', 0.03), ('K2', 0.02), ('D0', 0.0)]
    def run(name, p):
        res = []
        for sd in range(2000, 2000 + seeds):
            rs = random.Random(sd)
            S = sibling(A, rs)
            C = sibling(A, random.Random(sd + 50000))
            cw = tl.fresh_cw()
            pos = plant(cw, A, S, p, random.Random(sd + 90000)) if p else set()
            cg = dk.CceGains(cw)
            rS = dk.cce_test(cg, S, draws=draws, seed=sd, rule=rule)
            rC = dk.cce_test(cg, C, draws=draws, seed=sd, rule=rule)
            pf = sum(1 for r in rS['rows'] if r['flag'] and (r['stream'], r['index']) in pos)
            res.append((rS, rC, len(pos), pf))
            rows.append('\t'.join(map(str, [name, sd, len(pos), rS['flagged'], rS['examined'], f"{rS['rate']:.4f}",
                        f"{rS['null_p95']:.4f}", f"{rS['p']:.4f}", int(rS['contaminating']), f"{rC['rate']:.4f}",
                        f"{rC['null_p95']:.4f}", f"{rC['p']:.4f}", int(rC['contaminating']), pf, rS['flagged']])))
            print(rows[-1], flush=True)
        tally[name] = res
    for name, p in plist:
        run(name, p)
    k3 = sum(r[0]['contaminating'] for r in tally['K3']); k2 = sum(r[0]['contaminating'] for r in tally['K2'])
    d0 = sum(r[0]['contaminating'] for r in tally['D0'])
    date = sum(r[0]['p'] < r[1]['p'] for r in tally['K3']); cfl = sum(r[1]['contaminating'] for r in tally['K3'])
    pl = sum(r[2] for r in tally['K3']); pf = sum(r[3] for r in tally['K3']); af = sum(r[0]['flagged'] for r in tally['K3'])
    print(f'K3 {k3}/{seeds} (gate >= 8) {"PASS" if k3 >= 8 else "MISS"}')
    print(f'K2 {k2}/{seeds} (gate >= 7) {"PASS" if k2 >= 7 else "MISS"}')
    print(f'D0 {d0}/{seeds} (gate <= 1) {"PASS" if d0 <= 1 else "MISS"}')
    print(f'DATE p(S)<p(C) {date}/{seeds} (>= 8), C contaminating {cfl}/{seeds} (<= 1) '
          f'{"PASS" if date >= 8 and cfl <= 1 else "MISS"}')
    print(f'POS planted flagged {pf}/{pl} = {pf / max(pl, 1):.3f} (gate >= 0.50) {"PASS" if pf >= 0.5 * pl else "MISS"}; '
          f'precision {pf}/{af} = {pf / max(af, 1):.3f} (reported)')
    if k3 == seeds and k2 == seeds:
        run('K1', 0.01)
        k1 = sum(r[0]['contaminating'] for r in tally['K1'])
        print(f'K1 (p = 1%, reported, not gated) {k1}/{seeds}')
    if out:
        open(out, 'w').write('\n'.join(rows) + '\n')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--controls', action='store_true'); ap.add_argument('--seeds', type=int, default=10)
    ap.add_argument('--draws', type=int, default=200); ap.add_argument('--out'); ap.add_argument('--rule', choices=['best', 'gain'], default='best')
    a = ap.parse_args()
    if a.controls:
        controls(a.seeds, a.draws, a.out, a.rule)
    else:
        offline()
        print('all cce tests passed' if not fails else f'{len(fails)} failures')
        sys.exit(1 if fails else 0)
