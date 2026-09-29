#!/usr/bin/env python3
"""DEB-SWARM-A key fitter (the committed script behind every G-A key file). Reads ONLY the named ciphertext:
  a control part (swarm/controls/<ID>.tsv, lines c1_* and/or c2_*), or a real text (settled drafts via score.py's own
  conventions: '_' and MULTI dropped, clear spans dropped, trailing '?' stripped).
Fits a homophonic letter key with hsolve.c (5-gram French, fr19+fr18 prose, FLOOR -4, WF 0.3, T0 5), alphabet 26
(letters) or 27 (letters + word space; a space sign gets value ' ', which score.py reads as nothing).
usage: fitkey.py SOURCE OUT.tsv [--alpha 26|27] [--R 24] [--it 10000000] [--seed 7]
  SOURCE: control:FR-HOMO:c2  | control:FR-HOMO:c1+c2 | real:c1 | real:c2"""
import sys, os, csv, argparse, subprocess, re
H = os.path.dirname(os.path.abspath(__file__)); W = os.path.join(H, 'work'); ROOT = os.path.join(H, '..', '..')
ap = argparse.ArgumentParser(); ap.add_argument('source'); ap.add_argument('out')
ap.add_argument('--alpha', type=int, default=26); ap.add_argument('--R', type=int, default=24)
ap.add_argument('--it', type=int, default=10000000); ap.add_argument('--seed', type=int, default=7)
a = ap.parse_args()
kind, *rest = a.source.split(':')
if kind == 'control':
    cid, parts = rest[0], rest[1].split('+')
    toks = [r['sign'] for r in csv.DictReader(open(os.path.join(H, '..', 'controls', cid + '.tsv')), delimiter='\t')
            if r['line'].split('_')[0] in parts]
elif kind == 'real':
    if not re.search(r'^FROZEN [0-9a-f]{7,}', open(os.path.join(H, '..', 'README.md')).read(), re.M): sys.exit('refused: not frozen')
    sys.path.insert(0, os.path.join(ROOT, 'scripts')); from settled_lines import settled_lines
    toks = [s for l in settled_lines(ROOT, rest[0], drop_clear=True).values() for s in l if s not in ('_', 'MULTI')]
else: sys.exit('bad source')
signs = sorted(set(toks)); sid = {s: i for i, s in enumerate(signs)}
os.makedirs(W, exist_ok=True); cf = os.path.join(W, 'fit_' + re.sub(r'\W', '_', a.source) + f'_a{a.alpha}.cip')
open(cf, 'w').write(' '.join(str(sid[s]) for s in toks) + '\n')
if not os.path.exists(os.path.join(W, 'hsolve')):
    subprocess.run(['gcc', '-O3', '-march=native', '-o', os.path.join(W, 'hsolve'), os.path.join(H, 'hsolve.c'), '-lm'], check=True)
if not os.path.exists(os.path.join(W, 'train_sp.txt')): subprocess.run([sys.executable, os.path.join(H, 'prep_corpus.py')], check=True)
train = os.path.join(W, 'train_sp.txt' if a.alpha == 27 else 'train.txt')
o = subprocess.run([os.path.join(W, 'hsolve'), train, cf, str(a.R), str(a.it), str(a.seed), '0.3', '5'], capture_output=True, text=True,
                   env=dict(os.environ, ALPHA=str(a.alpha), FLOOR='-4')).stdout
rows = [l.split() for l in o.split('\n') if re.fullmatch(r'\d+ [a-z{]', l)]
with open(a.out, 'w') as f:
    f.write('sign\tvalue\n')
    for i, v in rows: f.write(f"{signs[int(i)]}\t{' ' if v == '{' else v}\n")
print(a.source, 'N', len(toks), 'K', len(signs), o.split('\n')[0])
