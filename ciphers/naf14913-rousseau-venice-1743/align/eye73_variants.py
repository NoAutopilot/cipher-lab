#!/usr/bin/env python3
"""FT4m (account-4, 3 Oct 2026): before the eye check of f.213v L02 group 73 (second 368), list which readings of that
group make the f.213/f.214r pair fit with NO edit (E0), using one_edit_seg.solve unchanged. Candidates: every single-digit
substitution of 368, every 2-digit drop (36, 38, 68), and the group deleted. Output: one line per candidate, 'E0 True/False/None'."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import one_edit_seg as s
toks, text, words = s.load('f213')
G = 73
assert toks[G] == '368', toks[G]
cands = set()
for p in range(3):
    for d in '0123456789':
        c = '368'[:p] + d + '368'[p + 1:]
        if c != '368':
            cands.add(c)
cands |= {'36', '38', '68', 'DEL'}
for c in sorted(cands):
    t = toks[:G] + ([] if c == 'DEL' else [c]) + toks[G + 1:]
    r = s.solve(t, text, 0, 60, workers=4)
    print(c, 'E0', r, 'in-passage-count', toks.count(c) if c != 'DEL' else '-', flush=True)
