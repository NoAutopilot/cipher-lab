#!/usr/bin/env python3
"""R11A-AVS9C: read gates C, L, L2 (prereg_avs9c.md) from avs9c/control2_s1..10.json; writes avs9c/result.tsv.
--check: exit 1 if the committed result.tsv is stale."""
import json, os, sys
D = os.path.dirname(os.path.abspath(__file__))
rows, sh, low, two = ['seed\tstart\tshare\tcount<=3 signs (truth->read)\tcount-2 signs (truth->read)'], [], [], []
for s in range(1, 11):
    r = json.load(open(os.path.join(D, f'control2_s{s}.json')))
    best = r['restarts'][0]['key']
    l3 = [(x, r['truth'][x], best[x]) for x, c in r['counts'].items() if c <= 3]
    l2 = [t for t in l3 if r['counts'][t[0]] == 2]
    sh.append(r['share']); low += l3; two += l2
    f = lambda L: ' '.join(f'{x}:{a}->{b}' for x, a, b in L)
    rows.append(f"{s}\t{r['start']}\t{r['share']}\t{f(l3)}\t{f(l2)}")
C = sum(sh) / len(sh); L = sum(a == b for _, a, b in low) / len(low); L2 = sum(a == b for _, a, b in two) / len(two)
rows.append(f"# C mean share {C:.3f} (gate >= 0.90): {'PASS' if C >= .9 else 'FAIL'}")
rows.append(f"# L count<=3 {sum(a == b for _, a, b in low)}/{len(low)} = {L:.3f} (gate >= 0.80): {'PASS' if L >= .8 else 'FAIL'}")
rows.append(f"# L2 count==2 {sum(a == b for _, a, b in two)}/{len(two)} = {L2:.3f} (gate >= 0.80, n >= 10): "
            f"{'PASS' if L2 >= .8 and len(two) >= 10 else 'FAIL'}")
t = '\n'.join(rows) + '\n'
p = os.path.join(D, 'result.tsv')
if '--check' in sys.argv:
    sys.exit(0 if open(p).read() == t else 1)
open(p, 'w').write(t); print(t)
