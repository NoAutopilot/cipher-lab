#!/usr/bin/env python3
"""R7-MANTP (6 Oct 2026): pooled single-code-gloss gate per PREREG-MANTP.md.
Reads the four leaves' pairs.tsv + reconciled.tsv and ../key.tsv; writes pooled_runs.tsv, pooled_codes.tsv, shuffle_pooled.tsv,
per_leaf.tsv beside this script and prints the gate. Disk only. Usage: pooled_gate.py [--add0574 [--norm0574]]
R7-MANT463 (6 Oct 2026, PREREG-MANT463 addendum): --add0574 appends leaf 0574 (ff.463-463v) and writes the outputs with suffix
_0574; --norm0574 also applies ../f463_0574/gloss_norm_0574.tsv (non-gating sensitivity, suffix _0574n).
R7-MANT529 (6 Oct 2026, PREREG-MANT529 addendum): --add0529 appends leaf 0529 (ff.424v-425) after 0574 (implies --add0574), suffix _0529.
R8-MANT530 (6 Oct 2026, PREREG-MANT530 addendum): --add0530 appends leaf 0530 (ff.425v-426) after 0529 (implies --add0529), suffix _0530.
R10-MANT526 (6 Oct 2026, PREREG-MANT526 addendum): --add0526 appends leaf 0526 (f.422) after 0530 (implies --add0530), suffix _0526.
R10-MANT521 (6 Oct 2026, ../f0521/PREREG-MANT521.md addendum): --add0521 appends leaf 0521 after 0526 (implies --add0526), suffix _0521.
R10-MANTSCR (6 Oct 2026, ../r10mantscr/PREREG-R10-MANTSCR.md): --sp applies spelling rule SP1-SP6 after MANT5 to every gloss, suffix +sp."""
import csv, os, re, random, sys, unicodedata
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(HERE, '..')
LEAVES = [('0502', 'f0500_0502/pairs_0502.tsv', 'f0500_0502/reconciled_mant4.tsv'),
          ('0501', 'f0501/pairs.tsv', 'f0501/reconciled.tsv'),
          ('0527', 'f422v_0527/pairs.tsv', 'f422v_0527/reconciled.tsv'),
          ('0528', 'f423_0528/pairs.tsv', 'f423_0528/reconciled.tsv')]
PRIOR_CLEARED = {'0502', '0528'}
SUF = ''
if '--add0574' in sys.argv or '--add0529' in sys.argv or '--add0530' in sys.argv or '--add0526' in sys.argv or '--add0521' in sys.argv:
    LEAVES.append(('0574', 'f463_0574/pairs.tsv', 'f463_0574/reconciled.tsv')); SUF = '_0574'
if '--add0529' in sys.argv or '--add0530' in sys.argv or '--add0526' in sys.argv or '--add0521' in sys.argv:
    LEAVES.append(('0529', 'f424v_0529/pairs.tsv', 'f424v_0529/reconciled.tsv')); SUF = '_0529'
if '--add0530' in sys.argv or '--add0526' in sys.argv or '--add0521' in sys.argv:
    LEAVES.append(('0530', 'f425v_0530/pairs.tsv', 'f425v_0530/reconciled.tsv')); SUF = '_0530'
if '--add0526' in sys.argv or '--add0521' in sys.argv:
    LEAVES.append(('0526', 'f422_0526/pairs.tsv', 'f422_0526/reconciled.tsv')); SUF = '_0526'
if '--add0521' in sys.argv:
    LEAVES.append(('0521', 'f0521/pairs.tsv', 'f0521/reconciled.tsv')); SUF = '_0521'
DRAWS, SEED = 1000, 7101
NORM = {r['token']: r['expansion'] for r in csv.DictReader(open(os.path.join(T, 'f0500_0502/gloss_norm.tsv')), delimiter='\t')}
if '--norm0574' in sys.argv:
    NORM.update({r['token']: r['expansion'] for r in csv.DictReader(open(os.path.join(T, 'f463_0574/gloss_norm_0574.tsv')), delimiter='\t')}); SUF += 'n'
norm = lambda g: ' '.join(NORM.get(t, t) for t in re.sub(r"[.,;:'\"]", ' ', g.lower()).split())
def sp(g):
    g = ''.join(ch for ch in unicodedata.normalize('NFD', g) if not unicodedata.combining(ch))
    t = g.split()
    if len(t) > 1 and t[0] in ('le', 'la', 'les', 'l'): t = t[1:]
    t = [re.sub(r's(?=[bcdfghjklmnpqrstvwxz])', '', w.replace('y', 'i')) for w in t]  # SP4, SP5 within a word
    g = ''.join(t).replace('-', '')  # SP3
    return re.sub(r'(.)\1+', r'\1', g)
if '--sp' in sys.argv:
    _n0 = norm; norm = lambda g: sp(_n0(g)); SUF += 'sp'
rd = lambda p: [r for r in csv.DictReader((l for l in open(os.path.join(T, p)) if not l.startswith('#')), delimiter='\t')]

def load():
    runs = []
    for leaf, pp, rp in LEAVES:
        grades = defaultdict(list)
        for r in rd(rp):
            if r.get('frame') and leaf == '0502' and r['frame'] != '0502': continue
            c = r['codes'].replace('.', ' ').split()
            if len(c) == 1: grades[(c[0], norm(r['gloss']))].append(r['gloss_grade'])
        for r in rd(pp):
            c = r['cipher_raw'].split()
            if len(c) != 1: continue
            g = norm(r['plain_raw']); gg = grades.get((c[0], g), ['?'])
            runs.append({'leaf': leaf, 'line': r['cipher_line'], 'code': c[0], 'gloss': g, 'gloss_grade': 'C' if 'C' in gg else gg[0]})
    return runs

def stat(codes, glosses):
    d = defaultdict(list)
    for c, g in zip(codes, glosses): d[c].append(g)
    rec = [c for c, v in d.items() if len(v) >= 2]
    return len(rec), sum(len(set(d[c])) == 1 for c in rec), d

def gate(runs, seed, within_leaf=False):
    codes = [r['code'] for r in runs]; gl = [r['gloss'] for r in runs]
    n, k, _ = stat(codes, gl); s = k / n if n else 0.0
    rng = random.Random(seed); sh = []
    for _ in range(DRAWS):
        if within_leaf:
            g = gl[:]
            for leaf in {r['leaf'] for r in runs}:
                idx = [i for i, r in enumerate(runs) if r['leaf'] == leaf]; vals = [gl[i] for i in idx]; rng.shuffle(vals)
                for i, v in zip(idx, vals): g[i] = v
        else:
            g = gl[:]; rng.shuffle(g)
        nn, kk, _ = stat(codes, g); sh.append(kk / nn if nn else 0.0)
    sh.sort(); p95 = sh[int(0.95 * DRAWS) - 1]
    return n, k, s, sum(sh) / DRAWS, p95, sh

def main():
    runs = load(); key = {r['code']: r for r in rd('key.tsv')}
    with open(os.path.join(HERE, 'pooled_runs'+SUF+'.tsv'), 'w') as f:
        w = csv.DictWriter(f, ['leaf', 'line', 'code', 'gloss', 'gloss_grade'], delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(runs)
    n, k, s, mean, p95, sh = gate(runs, SEED)
    _, _, _, wmean, wp95, _ = gate(runs, SEED, within_leaf=True)
    passed = n >= 3 and s > p95
    with open(os.path.join(HERE, 'shuffle_pooled'+SUF+'.tsv'), 'w') as f:
        f.write('draw\tS\n' + ''.join(f'{i}\t{x:.4f}\n' for i, x in enumerate(sh)))
    print(f'POOLED: runs {len(runs)}, N_rec {n}, consistent {k}, S {s:.3f} vs shuffle mean {mean:.3f} p95 {p95:.3f} -> {"PASS" if passed else "HELD"}')
    print(f'  (not gating) within-leaf shuffle mean {wmean:.3f} p95 {wp95:.3f}')
    cleared = set(PRIOR_CLEARED); rows = []
    for leaf, _, _ in LEAVES:
        lr = [r for r in runs if r['leaf'] == leaf]
        ln, lk, ls, lm, lp, _ = gate(lr, SEED + int(leaf))
        ok = ln >= 3 and ls > lp
        if ok: cleared.add(leaf)
        rows.append([leaf, len(lr), ln, lk, f'{ls:.3f}', f'{lm:.3f}', f'{lp:.3f}', 'PASS' if ok else ('HELD (N floor)' if ln < 3 else 'HELD'),
                     'yes' if leaf in cleared else 'no'])
        print(f'  leaf {leaf}: runs {len(lr)}, N_rec {ln}, S {ls:.3f} vs p95 {lp:.3f} -> {rows[-1][7]}; cleared {rows[-1][8]}')
    with open(os.path.join(HERE, 'per_leaf'+SUF+'.tsv'), 'w') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['leaf', 'single_runs', 'n_rec', 'n_cons', 'S', 'shuffle_mean', 'shuffle_p95', 'own_gate', 'cleared']); w.writerows(rows)
    _, _, d = stat([r['code'] for r in runs], [r['gloss'] for r in runs])
    out = []
    for c in sorted(d, key=int):
        rr = [r for r in runs if r['code'] == c]; gls = sorted(set(r['gloss'] for r in rr))
        leaves = sorted({r['leaf'] for r in rr}); kv = key.get(c)
        if len(rr) < 2: lic = 'single-attested'
        elif len(gls) > 1: lic = 'disagree'
        elif not passed: lic = 'gate-held'
        else:
            lic = 'C' if (set(leaves) & cleared and any(r['gloss_grade'] == 'C' for r in rr)) else 'M'
        src = kv['source'] if kv else ''
        circ = 'circular' if kv and 'gloss' in src else ('known-answer' if kv and kv['grade'] == 'C' else '')
        out.append([c, len(rr), ','.join(leaves), ' | '.join(gls), ''.join(r['gloss_grade'] for r in rr), lic,
                    kv['value'] if kv else '', kv['grade'] if kv else '', circ])
    with open(os.path.join(HERE, 'pooled_codes'+SUF+'.tsv'), 'w') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['code', 'n_single', 'leaves', 'glosses_norm', 'gloss_grades', 'licence', 'key_value', 'key_grade', 'key_check']); w.writerows(out)
    for o in out: print('  ' + '\t'.join(map(str, o)))

if __name__ == '__main__':
    main()
