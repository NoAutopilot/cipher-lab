#!/usr/bin/env python3
"""R13-MANT85 (6 Oct 2026): PREREG-MANT27 statistic and pairing-shuffle control for file 0085 (Loc. 694/09); copy of f0521/shuffle_control_0521.py.
GAPS195/MANT5 shape: gloss normalisation (../f0500_0502/gloss_norm.tsv + gloss_norm_0085.tsv if present), interlinear_align.py
with --floor 0 --max-chunk 14 --seg-bonus 1.0 --len-prior 0.5; S, S_multi and (per class) S_single; 200 draws, seed 85.
Usage: shuffle_control_0085.py [pairs_line.tsv]  (reads pairs.tsv, writes shuffle_control.tsv and align_real.tsv beside it)"""
import csv, os, re, random, subprocess, sys, tempfile, shutil
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); TOOL = os.path.join(HERE, '../../../tools/interlinear_align.py')
OPTS = ['--floor', '0', '--max-chunk', '14', '--seg-bonus', '1.0', '--len-prior', '0.5']
NORM = {}
for f in (os.path.join(HERE, '../f0500_0502/gloss_norm.tsv'), os.path.join(HERE, 'gloss_norm_0085.tsv')):
    if os.path.exists(f):
        NORM.update({r['token']: r['expansion'] for r in csv.DictReader(open(f), delimiter='\t')})

def norm(g):
    return ' '.join(NORM.get(t, t) for t in re.sub(r"[.,;:'\"]", ' ', g.lower()).split())

def align(pairs, tmp, keep=None):
    p, a, k = (os.path.join(tmp, x) for x in ('p.tsv', 'a.tsv', 'k.tsv'))
    with open(p, 'w') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw']); w.writerows(pairs)
    subprocess.run([sys.executable, TOOL, 'align', p, a, k] + OPTS, check=True, capture_output=True)
    if keep: shutil.copy(a, keep)
    return list(csv.DictReader(open(a), delimiter='\t'))

def stat(rows, pairs):
    multi = {pl[2] for pl in pairs if len(pl[3].split()) > 1}
    ch = defaultdict(list); inmulti = set(); single = defaultdict(int)
    for r in rows:
        ch[r['raw']].append(r['plain_chunk'])
        if r['cipher_line'] in multi: inmulti.add(r['raw'])
        else: single[r['raw']] += 1
    rec = [c for c, v in ch.items() if len(v) >= 2]
    cons = [c for c in rec if len(set(ch[c])) == 1]
    recm = [c for c in rec if c in inmulti]; consm = [c for c in recm if c in cons]
    recs = [c for c in rec if single[c] >= 2]
    conss = [c for c in recs if len({x for x, r in zip(ch[c], [1]*len(ch[c]))}) == 1]
    # S_single: chunks over single-code positions only
    sch = defaultdict(list)
    for r in rows:
        if r['cipher_line'] not in multi: sch[r['raw']].append(r['plain_chunk'])
    conss = [c for c in recs if len(set(sch[c])) == 1]
    return len(rec), len(cons), len(recm), len(consm), len(recs), len(conss)

def main():
    PF = sys.argv[1] if len(sys.argv) > 1 else 'pairs.tsv'; SUF = '' if PF == 'pairs.tsv' else '_line'
    pairs = [r for r in csv.reader(open(os.path.join(HERE, PF)), delimiter='\t')][1:]
    pairs = [[p[0], norm(p[1]), p[2], p[3]] for p in pairs]
    out = []
    with tempfile.TemporaryDirectory() as tmp:
        out.append(('real',) + stat(align(pairs, tmp, os.path.join(HERE, f'align_real{SUF}.tsv')), pairs))
        rng = random.Random(85); gl = [p[1] for p in pairs]
        for d in range(200):
            g = gl[:]; rng.shuffle(g)
            sp = [[p[0], g[i], p[2], p[3]] for i, p in enumerate(pairs)]
            out.append((f'shuf{d:03d}',) + stat(align(sp, tmp), sp))
    with open(os.path.join(HERE, f'shuffle_control{SUF}.tsv'), 'w') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['draw', 'n_rec', 'n_cons', 'n_rec_multi', 'n_cons_multi', 'n_rec_single', 'n_cons_single']); w.writerows(out)
    fr = lambda a, b: (lambda r: r[b] / r[a] if r[a] else 0.0)
    S, Sm, Ss = fr(1, 2), fr(3, 4), fr(5, 6)
    def p95(fn):
        v = sorted(fn(r) for r in out[1:]); return sum(v) / len(v), v[int(0.95 * len(v)) - 1]
    real = out[0]
    for name, fn, n in (('S', S, 1), ('S_multi', Sm, 3), ('S_single', Ss, 5)):
        m, p = p95(fn); print(f"{name}: real {fn(real):.3f} (N {real[n]}, cons {real[n+1]}); shuffle mean {m:.3f} p95 {p:.3f}")
    print('GATE', 'PASS' if real[1] >= 3 and S(real) > p95(S)[1] else 'HELD (tie or miss)')

if __name__ == '__main__':
    main()
