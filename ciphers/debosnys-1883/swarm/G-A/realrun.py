#!/usr/bin/env python3
"""DEB-SWARM-A Phase 2 runner. Refuses to run until swarm/README.md carries a FROZEN line (brief: real texts only
after score.py is frozen). Builds the settled c1/c2 id streams (drop '_', MULTI and the clear spans), fits a key on
one text with pipeline.py (S2 search, order-shuffled-fit null), both directions, alphabet 26 (letters) and 27
(letters + word space), and writes each fitted key as a score.py key TSV (sign<TAB>value; value ' ' for a space).
usage: realrun.py [--alpha 26 27] [--nnull 20] [--R 24] [--it 10000000]"""
import sys, os, re, json, argparse, subprocess, collections
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(H, '..', '..'); W = os.path.join(H, 'work')
sys.path.insert(0, os.path.join(ROOT, 'scripts')); from settled_lines import settled_lines
ap = argparse.ArgumentParser(); ap.add_argument('--alpha', type=int, nargs='+', default=[26, 27])
ap.add_argument('--nnull', type=int, default=20); ap.add_argument('--R', type=int, default=24); ap.add_argument('--it', type=int, default=10000000)
a = ap.parse_args()
readme = os.path.join(H, '..', 'README.md')
if not (os.path.exists(readme) and re.search(r'^FROZEN [0-9a-f]{7,}', open(readme).read(), re.M)):
    sys.exit('refused: no FROZEN line in swarm/README.md')
DROP = {'_', 'MULTI'}
texts = {p: [s for l in settled_lines(ROOT, p, drop_clear=True).values() for s in l if s not in DROP] for p in ('c1', 'c2')}
signs = sorted(set(texts['c1']) | set(texts['c2'])); sid = {s: i for i, s in enumerate(signs)}
for p, t in texts.items(): open(os.path.join(W, f'real_{p}.cip'), 'w').write(' '.join(str(sid[s]) for s in t) + '\n')
open(os.path.join(H, 'real_signmap.tsv'), 'w').write('id\tsign\n' + ''.join(f'{i}\t{s}\n' for i, s in enumerate(signs)))
summary = {}
for al in a.alpha:
    for fit, test in (('c2', 'c1'), ('c1', 'c2')):
        out = os.path.join(W, f'real_{fit}fit_a{al}')
        r = subprocess.run([sys.executable, os.path.join(H, 'pipeline.py'), os.path.join(W, f'real_{fit}.cip'), os.path.join(W, f'real_{test}.cip'), out,
                            '--alpha', str(al), '--R', str(a.R), '--it', str(a.it), '--nnull', str(a.nnull)], capture_output=True, text=True)
        d = json.loads(r.stdout); summary[f'a{al}_{fit}->{test}'] = d
        key = [l.split() for l in open(out + '_real.key') if l.strip()]
        kt = os.path.join(H, f'key_{fit}fit_a{al}.tsv')
        open(kt, 'w').write('sign\tvalue\n' + ''.join(f"{signs[int(i)]}\t{' ' if v == '{' else v}\n" for i, v in key))
        print(f'a{al} {fit}->{test}', d['heldout'], d['rank_vs_orderfit_null'], flush=True)
json.dump(summary, open(os.path.join(H, 'realrun_summary.json'), 'w'), indent=1)
