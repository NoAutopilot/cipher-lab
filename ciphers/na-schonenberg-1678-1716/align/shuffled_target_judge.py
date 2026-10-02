#!/usr/bin/env python3
"""shuffled_target_judge.py -- the shuffled-target judge check (CLAUDE.md rule 3, ARM-C1 clause): decode L18+L19 with
key.tsv (plus the two sign-level exception values, ?9 = n and 8) = l) after shuffling the group order within the two
lines, and run tools/judge_plaintext.py on each shuffle. A PASS rate on shuffled targets near the real reading's
result would void the judge as a gate here. Usage: python3 .../shuffled_target_judge.py [--shuffles 20] [--seed 1]
"""
import argparse, csv, os, random, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); TARGET = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(TARGET))
ap = argparse.ArgumentParser(); ap.add_argument('--shuffles', type=int, default=20); ap.add_argument('--seed', type=int, default=1)
a = ap.parse_args()
key = {r['code']: r['value'] for r in csv.DictReader(open(os.path.join(TARGET, 'key.tsv'), encoding='utf-8'), delimiter='\t')}
key.update({'?9': 'n', '8)': 'l'})
groups = [r['group'] for r in csv.DictReader(open(os.path.join(TARGET, 'ciphertext.tsv'), encoding='utf-8'), delimiter='\t') if r['line'] in ('L18', 'L19')]
def decode(gs): return ''.join(key.get(g, '') if key.get(g, '[?]') != '[?]' else '' for g in gs)
spec = os.path.join(ROOT, 'specs', 'na-schonenberg-1678-1716.json')
def judge(text):
    p = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'judge_plaintext.py'), spec, '--text', text], capture_output=True, text=True)
    return p.returncode, p.stdout.strip().splitlines()
rc, out = judge(decode(groups)); print('REAL  ', decode(groups), 'exit', rc); print('\n'.join('  ' + l for l in out))
rng = random.Random(a.seed); passes = 0; scores = []
for i in range(a.shuffles):
    gs = groups[:]; rng.shuffle(gs); t = decode(gs); rc, out = judge(t); passes += (rc == 0)
    sc = [l for l in out if 'language' in l]; scores.append((t, rc, sc[0] if sc else ''))
for t, rc, sc in scores: print('SHUF  ', t, 'exit', rc, sc)
print('shuffled-target judge: %d PASS of %d (seed %d)' % (passes, a.shuffles, a.seed))
