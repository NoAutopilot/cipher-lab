#!/usr/bin/env python3
"""SUR-2061 chance control: shuffle the letters inside every crib word (seeds 0-199) and count conflict-free spans with
>= 2 U/M covered anywhere on the sheet (placement ignored, so this over-counts chance), vs the real crib's count."""
import random, re, subprocess, sys, os
H = os.path.dirname(os.path.abspath(__file__)); src = [l for l in open(os.path.join(H, 'heijer_p362_legend.txt')) if not l.startswith('#')]
txt = ''.join(src)
def run(t):
    p = os.path.join(H, '.ctl.txt'); open(p, 'w').write(t)
    o = subprocess.run([sys.executable, os.path.join(H, 'align_heijer_p362.py'), p], capture_output=True, text=True).stdout
    os.remove(p); return len(o.strip().splitlines()) - 1
real = run(txt); ns = []
for s in range(200):
    r = random.Random(s)
    ns.append(run(re.sub(r'[a-zëé]+', lambda m: ''.join(r.sample(m.group(0), len(m.group(0)))), txt.lower())))
ns.sort(); print(f'real spans {real}; shuffled mean {sum(ns)/len(ns):.2f} p95 {ns[189]} max {ns[-1]}; at or above real {sum(n>=real for n in ns)}/200')
