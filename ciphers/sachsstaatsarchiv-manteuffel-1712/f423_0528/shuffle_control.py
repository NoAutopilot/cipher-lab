#!/usr/bin/env python3
"""GAPS195 (3 Oct 2026): PREREG-GAPS195 statistic S and its pairing-shuffle control for frame 0528.
S = share of codes with >=2 glossed positions whose aligned chunks are identical at every occurrence.
S_multi = same, restricted to codes occurring inside multi-code runs only. Control: gloss strings permuted
across glossed runs, re-aligned with identical options; 200 draws, seed 195. Writes shuffle_control.tsv."""
import csv, random, subprocess, sys, os, tempfile
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); TOOL = os.path.join(HERE, '../../../tools/interlinear_align.py')
OPTS = ['--floor', '0', '--max-chunk', '14', '--seg-bonus', '1.0', '--len-prior', '0.5']

def align(pairs, tmp):
    p = os.path.join(tmp, 'p.tsv'); a = os.path.join(tmp, 'a.tsv'); k = os.path.join(tmp, 'k.tsv')
    with open(p, 'w') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw'])
        w.writerows(pairs)
    subprocess.run([sys.executable, TOOL, 'align', p, a, k] + OPTS, check=True, capture_output=True)
    return list(csv.DictReader(open(a), delimiter='\t'))

def stat(rows, pairs):
    multi = {pl[2] for pl in pairs if len(pl[3].split()) > 1}
    ch = defaultdict(list); inmulti = set()
    for r in rows:
        ch[r['raw']].append(r['plain_chunk'])
        if r['cipher_line'] in multi: inmulti.add(r['raw'])
    rec = [c for c, v in ch.items() if len(v) >= 2]
    cons = [c for c in rec if len(set(ch[c])) == 1]
    recm = [c for c in rec if c in inmulti]; consm = [c for c in recm if c in cons]
    return len(rec), len(cons), len(recm), len(consm)

def main():
    pairs = [r for r in csv.reader(open(os.path.join(HERE, 'pairs.tsv')), delimiter='\t')][1:]
    out = []
    with tempfile.TemporaryDirectory() as tmp:
        real = stat(align(pairs, tmp), pairs); out.append(('real',) + real)
        rng = random.Random(195); gl = [p[1] for p in pairs]
        for d in range(200):
            g = gl[:]; rng.shuffle(g)
            sp = [[p[0], g[i], p[2], p[3]] for i, p in enumerate(pairs)]
            out.append((f'shuf{d:03d}',) + stat(align(sp, tmp), sp))
    with open(os.path.join(HERE, 'shuffle_control.tsv'), 'w') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(['draw', 'n_rec', 'n_cons', 'n_rec_multi', 'n_cons_multi']); w.writerows(out)
    S = lambda r: r[2] / r[1] if r[1] else 0.0; Sm = lambda r: r[4] / r[3] if r[3] else 0.0
    sh = sorted(S(r) for r in out[1:]); shm = sorted(Sm(r) for r in out[1:])
    p95 = sh[int(0.95 * len(sh)) - 1]; p95m = shm[int(0.95 * len(shm)) - 1]
    print(f"real: N_rec {real[0]} consistent {real[1]} S {S(out[0]):.3f}; multi N {real[2]} cons {real[3]} S_multi {Sm(out[0]):.3f}")
    print(f"shuffle S mean {sum(sh)/len(sh):.3f} p95 {p95:.3f}; S_multi mean {sum(shm)/len(shm):.3f} p95 {p95m:.3f}")
    ok = real[0] >= 3 and S(out[0]) > p95
    print('GATE', 'PASS' if ok else 'HELD (tie or miss)')

if __name__ == '__main__':
    main()
