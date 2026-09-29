#!/usr/bin/env python3
"""Recovery pct of a solver output against a planted answer (token-level letter agreement)."""
import sys
out = open(sys.argv[1]).read().split('\n'); ans = open(sys.argv[2]).read().strip()
pt = [l for l in out if l and not l.startswith('score') and ' ' not in l][-1]
print('%.3f' % (sum(a == b for a, b in zip(pt, ans)) / len(ans)), out[0])
if len(sys.argv) > 3:
    idx = [i for i, a in enumerate(ans) if a != '{']
    print('letters_only %.3f' % (sum(pt[i] == ans[i] for i in idx) / len(idx)))
