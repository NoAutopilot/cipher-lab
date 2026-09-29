#!/usr/bin/env python3
"""H61 (29 Sept 2026): coarse folds on R2-2's known-answer page, per h61/PREREG.md (pushed f8ca3dc7 before scoring).
Re-scores swarm/R2/R2-2/control reads against truth.tsv under R2-2's folds + RULE.md marks, and under the six coarse
folds on top; reports two-reader control error, single-reader errors, and the folded K on the c1+c2 settled drafts.
Writes h61/result.json."""
import os, sys, csv, json, collections
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here); sys.path.insert(0, here)
from settled_lines import settled_lines
C = os.path.join(root, 'swarm/R2/R2-2/control')
BASE = {'PCT-SLASH': 'PCT', 'X-DOT': 'X', 'X-CURL': 'X'}
MARKS = {'BLOB', 'BAR-SOLID', 'HOOK-L', 'DASH-V', '_', 'MARK'}
COARSE = {}
for grp in (('EIGHT', 'VENUS', 'THREE'), ('C-BAR-X', 'ARCH-DASH'), ('CIRC-O', 'BLOB'), ('O-SLASH', 'PHI'), ('II-DASH', 'CC-DASH'), ('S-CURL', 'DOUBLE-LOOP')):
    for g in grp: COARSE[g] = '/'.join(grp)
def f_base(s):
    s = BASE.get(s, s); return '_' if s in MARKS else s
def f_coarse(s):
    s = BASE.get(s, s)
    if s in COARSE: return COARSE[s]          # fold first (CIRC-O/BLOB is one sign class, per PREREG)
    return '_' if s in MARKS else s
T = {r['crop']: r['true'] for r in csv.DictReader(open(os.path.join(C, 'truth.tsv')), delimiter='\t')}
def reads(p): return {r[0].strip(): r[1].strip() for r in csv.reader(open(os.path.join(C, p)), delimiter='\t') if len(r) >= 2 and not r[0].startswith('crop')}
a, b = reads('reads_R1_sonnet.tsv'), reads('reads_R2_opus.tsv'); out = {}
for name, f in (('base', f_base), ('coarse', f_coarse)):
    n = len(T); e1 = sum(f(a.get(c, '?')) != f(t) for c, t in T.items()); e2 = sum(f(b.get(c, '?')) != f(t) for c, t in T.items())
    uns = sum(f(a.get(c, '?')) != f(b.get(c, '?')) for c in T); wrong = sum(f(a.get(c, '?')) == f(b.get(c, '?')) != f(t) for c, t in T.items())
    out[name] = dict(n=n, R1_err_pct=round(100 * e1 / n, 1), R2_err_pct=round(100 * e2 / n, 1), unsettled=uns, agreed_wrong=wrong, two_reader_err_pct=round(100 * (uns + wrong) / n, 1))
    out[name]['residual'] = [(c, T[c], a.get(c), b.get(c)) for c in T if f(a.get(c, '?')) != f(b.get(c, '?')) or f(a.get(c, '?')) != f(T[c])]
toks = [s for k, v in settled_lines(root, 'c', drop_clear=True).items() if k.startswith(('c1', 'c2')) for s in v if s not in ('_', 'MULTI')]
kb = {f_base(s) for s in toks} - {'_'}; kc = {f_coarse(s) for s in toks} - {'_'}
out['c1c2'] = dict(N=len(toks), K_base=len(kb), K_coarse=len(kc), share_touched_by_coarse=round(sum(BASE.get(s, s) in COARSE for s in toks) / len(toks), 3))
out['kill'] = out['coarse']['two_reader_err_pct'] >= 5.0
for k in ('base', 'coarse'): print(k, {x: y for x, y in out[k].items() if x != 'residual'})
print('c1c2', out['c1c2'], 'kill', out['kill']); print('residual under coarse:', out['coarse']['residual'])
json.dump(out, open(os.path.join(root, 'h61/result.json'), 'w'), indent=1)
