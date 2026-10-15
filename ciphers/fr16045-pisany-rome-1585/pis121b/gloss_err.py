#!/usr/bin/env python3
"""PIS-121B (PREREG-PIS-121B.md): gloss two-reader disagreement, letters only, folded exactly as pis121/score.py.

  python3 pis121b/gloss_err.py            # writes pis121b/gloss_err.json
  python3 pis121b/gloss_err.py --check    # exit 1 if stale
Pairs: P1 vs P2 (the two blind line-per-call passes), RG (reconciled, = pis121b/gloss_pass.tsv) vs the PIS-121 gloss.
"""
import difflib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from score import load_gloss  # byte-identical copy of pis121/score.py


def err(a, b):
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    return 1 - sum(m.size for m in sm.get_matching_blocks()) / max(len(a), len(b), 1)


def pair(x, y):
    gx, gy = load_gloss(x), load_gloss(y)
    per = {k: round(err(gx.get(k, ''), gy.get(k, '')), 4) for k in sorted(set(gx) | set(gy))}
    allx, ally = ''.join(gx[k] for k in sorted(gx)), ''.join(gy[k] for k in sorted(gy))
    return {'per_block': per, 'overall': round(err(allx, ally), 4)}


res = {'P1_vs_P2': pair(os.path.join(HERE, 'p1', 'gloss_pass.tsv'), os.path.join(HERE, 'p2', 'gloss_pass.tsv')),
       'RG_vs_PIS121': pair(os.path.join(HERE, 'gloss_pass.tsv'), os.path.join(os.path.dirname(HERE), 'pis121', 'gloss_pass.tsv'))}
txt = json.dumps(res, indent=1, sort_keys=True)
out = os.path.join(HERE, 'gloss_err.json')
if '--check' in sys.argv:
    ok = os.path.exists(out) and open(out).read() == txt
    print('result up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(out, 'w').write(txt); print(txt)
