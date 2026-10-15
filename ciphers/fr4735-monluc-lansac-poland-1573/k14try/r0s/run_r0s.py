#!/usr/bin/env python3
"""MONL-R0S (15 Oct 2026): positional null for the code-wide K14 = s --try (k14try/r0s/PREREG-MONL-R0S.md).
tools/decode_key.py's own null 1 needs n positions of K14's current value (p) and only 24 exist; this null instead draws n
non-s one-letter positions, reads them as a pseudo-code valued p, and takes the same statistic (s minus p). Controls PC (table-s
codes K17/K37/K67 set to p) and NC (table-p codes K34/K47) use the same construction. In memory only: key.tsv is never written.
Writes k14try/r0s/results.tsv and prints the decision. Usage: python3 k14try/r0s/run_r0s.py [--check] (from anywhere)."""
import argparse, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(T, '..', '..', 'tools'))
import decode_key as dk

VOW = set('AEIOUVY')   # Crossword folds values to upper case, u -> V
DRAWS, SEED, PSEUDO = 200, 1573, '\x00pseudo'
P, S = dk.lm_fold('p'), dk.lm_fold('s')

def crossword():
    a = argparse.Namespace(config=None, ciphertext=None, merge_mark=None, corrections=None)
    return dk.Crossword(T, dk.load_config(T, a), dk.lm_load(None), window=8)

def stat(cw, code, occ):
    s = cw.occ_scores(code, 's', {}, occ); p = cw.occ_scores(code, 'p', {}, occ)
    return sum(s) - sum(p), [x - y for x, y in zip(s, p)]

def run(name, codes):
    cw = crossword()
    occ = [(k, i) for k, s in enumerate(cw.S) for i, (t, _) in enumerate(s) if t in codes]
    for k, i in occ:
        cw.S[k][i] = [PSEUDO, P]            # the run's codes read p (K14, K34/K47 already are)
    st, per = stat(cw, PSEUDO, occ)
    for k, i in occ:
        cw.S[k][i] = ['\x00target', P]    # out of the pool, value p kept as background
    n = len(occ)
    pool1 = [(k, i) for k, s in enumerate(cw.S) for i, (t, v) in enumerate(s)
             if t is not None and not t.startswith('\x00') and v is not None and len(v) == 1 and v != S]
    pool2 = [x for x in pool1 if cw.S[x[0]][x[1]][1] not in VOW]
    out = dict(run=name, codes='+'.join(sorted(codes)), n=n, stat=st, broken=sum(d < -3 for d in per),
               pool1=len(pool1), pool2=len(pool2))
    for tag, pool in (('N1', pool1), ('N2', pool2)):
        rnd, xs = random.Random(SEED), []
        for _ in range(DRAWS):
            pick = rnd.sample(pool, n)
            saved = [(k, i, list(cw.S[k][i])) for k, i in pick]
            for k, i in pick:
                cw.S[k][i] = [PSEUDO, P]
            xs.append(stat(cw, PSEUDO, pick)[0])
            for k, i, e in saved:
                cw.S[k][i] = e
        xs.sort()
        out[tag + '_p95'] = xs[int(0.95 * len(xs))]; out[tag + '_mean'] = sum(xs) / len(xs)
        out[tag + '_p'] = sum(x >= st for x in xs) / len(xs)
    return out

def value_null():
    """R0s's value-class null recomputed with tools/decode_key.py try_value at 200 draws (null 1 still unbuildable)."""
    cw = crossword()
    r = dk.try_value(cw, 'K14', 's', list(cw.M.alpha) + ['NULL'], {}, DRAWS, 0, None,
                     sorted({v for v in 'abcdefghilmnopqrstuxyz'}))
    return r

def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--check', action='store_true', help='exit 1 if results.tsv differs from a fresh run')
    a = ap.parse_args()
    rows = [run('R0s', {'K14'}), run('PC', {'K17', 'K37', 'K67'}), run('NC', {'K34', 'K47'})]
    vn = value_null()
    cols = ['run', 'codes', 'n', 'stat', 'broken', 'pool1', 'N1_mean', 'N1_p95', 'N1_p', 'pool2', 'N2_mean', 'N2_p95', 'N2_p']
    f = lambda x: f'{x:.1f}' if isinstance(x, float) and not str(x).startswith('0.') else (f'{x:.3f}' if isinstance(x, float) else str(x))
    txt = '\t'.join(cols) + '\n' + ''.join('\t'.join(f(r[c]) for c in cols) + '\n' for r in rows)
    txt += f"# R0s via tools/decode_key.py try_value, {DRAWS} draws: stat {vn['stat']:.1f}, value-class p95 {vn['p95_val']:.1f}, " \
           f"broken {vn['broken']}/{vn['n']}, tool verdict {vn['verdict']} ({vn['why']})\n"
    R, PC, NC = rows
    if not (PC['stat'] > PC['N1_p95'] and PC['stat'] > PC['N2_p95']):
        d = 'NON-TEST: PC not above both null p95s (no power); R0s undecided, K14 stays p'
    elif NC['stat'] > NC['N1_p95']:
        d = 'NON-TEST: NC above the N1 p95 (null too lax); R0s undecided, K14 stays p'
    elif R['stat'] <= R['N1_p95']:
        d = 'REFUSED: R0s not above the N1 p95; K14 stays p'
    elif R['stat'] > R['N2_p95'] and R['stat'] > vn['p95_val'] and R['broken'] * 4 <= R['n']:
        d = 'LICENSED: K14 = s at grade S, lead file only (k14try/r0s/LEAD-K14s.tsv); key.tsv not edited'
    else:
        d = 'UNDECIDED: above N1 but not N2 / value class / breakage rule; K14 stays M where it faces s'
    txt += '# decision (PREREG-MONL-R0S): ' + d + '\n'
    path = os.path.join(HERE, 'results.tsv')
    if a.check:
        ok = os.path.exists(path) and open(path).read() == txt
        print('run_r0s: OK' if ok else 'run_r0s: STALE'); return 0 if ok else 1
    open(path, 'w').write(txt)
    print(txt, end='')
    if d.startswith('LICENSED'):
        open(os.path.join(HERE, 'LEAD-K14s.tsv'), 'w').write(
            'code\tvalue\tgrade\tn\tstat_bits_over_p\tN1_p95\tN2_p95\tvalue_p95\tbroken\tsource\n'
            f"K14\ts\tS\t{R['n']}\t{R['stat']:.1f}\t{R['N1_p95']:.1f}\t{R['N2_p95']:.1f}\t{vn['p95_val']:.1f}\t{R['broken']}\t"
            'MONL-R0S 15 Oct 2026 (PREREG-MONL-R0S); lead only, key.tsv K14 = p (Tomokiyo) unchanged: a verifier decides\n')
    return 0

if __name__ == '__main__':
    sys.exit(main())
