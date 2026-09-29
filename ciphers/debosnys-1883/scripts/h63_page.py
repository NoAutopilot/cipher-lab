#!/usr/bin/env python3
"""H63 (29 Sept 2026): build a FRESH known-answer page per h63/PREREG.md -- swarm/R2/R2-2/t_low.py's control() and
tiles() unchanged except seed 20260930 and R2-2's own page's source boxes excluded. Usage:
  OUT=<scratchpad dir> h63_page.py build      crops + truth_ctl.tsv under $OUT (truth never in the readers' list)
  OUT=<scratchpad dir> h63_page.py score R1.tsv R2.tsv   scores per PREREG (writes h63/result.json)"""
import os, sys, csv, json, inspect
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
T22 = os.path.join(root, 'swarm/R2/R2-2'); sys.path.insert(0, T22)
_argv = sys.argv; sys.argv = [sys.argv[0]]
import t_low
sys.argv = _argv
EXCL = {r['source_box'] for r in csv.DictReader(open(os.path.join(T22, 'control/truth.tsv')), delimiter='\t')}
BASE = {'PCT-SLASH': 'PCT', 'X-DOT': 'X', 'X-CURL': 'X'}; MARKS = {'BLOB', 'BAR-SOLID', 'HOOK-L', 'DASH-V', '_', 'MARK'}
COARSE = {}
for grp in (('EIGHT', 'VENUS', 'THREE'), ('C-BAR-X', 'ARCH-DASH'), ('CIRC-O', 'BLOB'), ('O-SLASH', 'PHI'), ('II-DASH', 'CC-DASH'), ('S-CURL', 'DOUBLE-LOOP')):
    for g in grp: COARSE[g] = '/'.join(grp)
def f_none(s): return s
def f_r22(s): s = BASE.get(s, s); return '_' if s in MARKS else s
def f_coarse(s):
    s = BASE.get(s, s)
    return COARSE[s] if s in COARSE else ('_' if s in MARKS else s)
def build():
    t_low.SEED = 20260930
    src = inspect.getsource(t_low.control).replace("ex = set();", "ex = set(EXCL);", 1)
    assert "ex = set(EXCL);" in src
    ns = dict(vars(t_low)); ns['EXCL'] = EXCL; exec(src, ns); ns['control'](); t_low.tiles()
def score(p1, p2):
    T = {r['crop']: r['true'] for r in csv.DictReader(open(os.path.join(t_low.OUT, 'truth_ctl.tsv')), delimiter='\t')}
    src = {r['crop']: r['source_box'] for r in csv.DictReader(open(os.path.join(t_low.OUT, 'truth_ctl.tsv')), delimiter='\t')}
    assert not (set(src.values()) & EXCL), 'overlap with R2-2 page'
    a, b = t_low.load_reads(p1), t_low.load_reads(p2); out = {}
    for name, f in (('unfolded', f_none), ('r22_folds_rule', f_r22), ('coarse', f_coarse)):
        n = len(T); e1 = sum(f(a.get(c, '?')) != f(t) for c, t in T.items()); e2 = sum(f(b.get(c, '?')) != f(t) for c, t in T.items())
        uns = sum(f(a.get(c, '?')) != f(b.get(c, '?')) for c in T); wrong = sum(f(a.get(c, '?')) == f(b.get(c, '?')) != f(t) for c, t in T.items())
        out[name] = dict(n=n, R1_err_pct=round(100 * e1 / n, 1), R2_err_pct=round(100 * e2 / n, 1), unsettled=uns, agreed_wrong=wrong,
                         two_reader_err_pct=round(100 * (uns + wrong) / n, 1),
                         residual=[(c, T[c], a.get(c), b.get(c)) for c in T if f(a.get(c, '?')) != f(b.get(c, '?')) or f(a.get(c, '?')) != f(T[c])])
        print(name, {k: v for k, v in out[name].items() if k != 'residual'})
    out['kill'] = out['coarse']['two_reader_err_pct'] >= 5.0; out['missing'] = dict(R1=len(set(T) - set(a)), R2=len(set(T) - set(b)))
    print('kill', out['kill'], 'missing', out['missing']); json.dump(out, open(os.path.join(root, 'h63', 'result.json'), 'w'), indent=1)
if __name__ == '__main__':
    {'build': build, 'score': lambda: score(*sys.argv[2:4])}[sys.argv[1]]()
