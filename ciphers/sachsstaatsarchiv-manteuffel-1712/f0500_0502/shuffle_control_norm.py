#!/usr/bin/env python3
"""RUN5-MANT5 (4 Oct 2026): PREREG-MANT5 -- PREREG-MANT4's statistic and pairing-shuffle control with gloss normalisation
(gloss_norm.tsv) applied to every gloss string before alignment, identically for the real pairing and every shuffle draw.
Usage: shuffle_control_norm.py PAIRS.tsv SEED OUT.tsv"""
import csv, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.argv, ARGS = sys.argv[:1] + ['x', '0'], sys.argv[1:]   # shuffle_control reads FR/SEED at import
import shuffle_control as sc
import random, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
NORM = {r['token']: r['expansion'] for r in csv.DictReader(open(os.path.join(HERE, 'gloss_norm.tsv')), delimiter='\t')}

def norm(g):
    toks = re.sub(r"[.,;:'\"]", ' ', g.lower()).split()
    return ' '.join(NORM.get(t, t) for t in toks)

def main():
    pairs_path, seed, out_path = ARGS[0], int(ARGS[1]), ARGS[2]
    pairs = [r for r in csv.reader(open(pairs_path), delimiter='\t')][1:]
    pairs = [[p[0], norm(p[1]), p[2], p[3]] for p in pairs]
    out = []
    with tempfile.TemporaryDirectory() as tmp:
        out.append(('real',) + sc.stat(sc.align(pairs, tmp), pairs))
        rng = random.Random(seed); gl = [p[1] for p in pairs]
        for d in range(200):
            g = gl[:]; rng.shuffle(g)
            sp = [[p[0], g[i], p[2], p[3]] for i, p in enumerate(pairs)]
            out.append((f'shuf{d:03d}',) + sc.stat(sc.align(sp, tmp), sp))
    with open(out_path, 'w') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(['draw', 'n_rec', 'n_cons', 'n_rec_multi', 'n_cons_multi']); w.writerows(out)
    S = lambda r: r[2] / r[1] if r[1] else 0.0; Sm = lambda r: r[4] / r[3] if r[3] else 0.0
    sh = sorted(S(r) for r in out[1:]); shm = sorted(Sm(r) for r in out[1:])
    p95 = sh[int(0.95 * len(sh)) - 1]; p95m = shm[int(0.95 * len(shm)) - 1]; real = out[0]
    print(f"real: N_rec {real[1]} consistent {real[2]} S {S(real):.3f}; multi N {real[3]} cons {real[4]} S_multi {Sm(real):.3f}")
    print(f"shuffle S mean {sum(sh)/len(sh):.3f} p95 {p95:.3f}; S_multi mean {sum(shm)/len(shm):.3f} p95 {p95m:.3f}")
    print('GATE', 'PASS' if real[1] >= 3 and S(real) > p95 else 'HELD (tie or miss)')

if __name__ == '__main__':
    main()
