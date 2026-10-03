#!/usr/bin/env python3
"""A2-FLO3, 3 Oct 2026: clear-text-shuffle control for the c.127 block-1/2 pilot alignment.
Runs tools/interlinear_align.py (--code-prefix @ --keep-fs) on align/c127b1_pairs.tsv (real) and on 20 copies whose
plain lines have their letters shuffled within each line (same letters, same length, so the control can differ from
the target only through letter ORDER, which is what a consistent key depends on). Statistic: share of aligned code
tokens whose letter agrees with the code's majority meaning (status 'agrees')."""
import csv, random, subprocess, sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); TOOL = os.path.join(HERE, '..', '..', '..', 'tools', 'interlinear_align.py')
def run(pairs, tag):
    a = os.path.join('/tmp', f'c127_{tag}_align.tsv'); k = os.path.join('/tmp', f'c127_{tag}_key.tsv')
    out = subprocess.run([sys.executable, TOOL, 'align', pairs, a, k, '--code-prefix', '@', '--keep-fs'], capture_output=True, text=True).stdout
    m = re.search(r"'agrees': (\d+)", out); return int(m.group(1)) if m else 0
rows = list(csv.DictReader(open(os.path.join(HERE, 'c127b1_pairs.tsv')), delimiter='\t'))
real = run(os.path.join(HERE, 'c127b1_pairs.tsv'), 'real')
ctl = []
for seed in range(20):
    rng = random.Random(seed); p = f'/tmp/c127_shuf{seed}.tsv'
    with open(p, 'w') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(list(rows[0].keys()))
        for r in rows:
            L = list(r['plain_raw'].replace(' ', '')); rng.shuffle(L); r2 = dict(r); r2['plain_raw'] = ''.join(L); w.writerow(list(r2.values()))
    ctl.append(run(p, f's{seed}'))
ctl.sort()
print(f'real agrees {real} of 120; shuffle agrees min {ctl[0]} median {ctl[10]} p95 {ctl[18]} max {ctl[-1]} (20 seeds)')
