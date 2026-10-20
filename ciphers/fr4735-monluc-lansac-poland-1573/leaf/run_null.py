#!/usr/bin/env python3
"""MONL-LEAF post-hoc null: longest exact run between a read's table decode and the clear letter, vs 200 word-shuffled clears (seed 2710)."""
import random, sys
from difflib import SequenceMatcher
sys.path.insert(0, '..'); sys.path.insert(0, '.')
import align_c268 as A, leaf_score as S
words = A.load_clear(); ws = [w[2] for w in words]; rng = random.Random(2710)
for r in sys.argv[1:]:
    dec = ''.join(x['value'] or '' for x in S.tokens(f'passes/{r}_read.tsv'))
    lr = lambda c: SequenceMatcher(None, dec, c, autojunk=False).find_longest_match(0, len(dec), 0, len(c)).size
    real = lr(''.join(ws)); ctl = []
    for _ in range(200):
        rng.shuffle(ws); ctl.append(lr(''.join(ws)))
    ws = [w[2] for w in words]; ctl.sort()
    print(r, 'run', real, 'null p95', ctl[189], 'max', ctl[-1], 'ge', sum(c >= real for c in ctl))
