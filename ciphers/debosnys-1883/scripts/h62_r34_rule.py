#!/usr/bin/env python3
"""H62 (29 Sept 2026): D's R34 lead rechecked under swarm/R2/R2-2/RULE.md. Declared before running: the c2 reading is
the settled c2 drafts with clear spans dropped and RULE.md applied (BLOB, BAR-SOLID, HOOK-L, DASH-V, '_', MULTI, MARK
dropped as marks; BAR-THIN and DASH-H kept as signs), in two variants: 'rule' (no folds) and 'rule+folds' (PCT-SLASH->
PCT, X-DOT->X, X-CURL->X), primary = 'rule+folds'. Instrument unchanged: swarm/G-D/r34_replicate.py's scan (columns and
columnar heights R 2-60, frozen single-text score, 60 shuffles per reading). Control first: D's TRANS-7/19/33 planted
transpositions (escape.trans) rebuilt on this box set's line lengths and sign curve, 12 each; pass = each picks its own
height in >= 10 of 12; if the control fails, stop and log 'no passable control'. Then the real scan with a 200-scan
own-shuffle null (within-line shuffles, scan repeated), and D's halves check (grid rows 1-17 and 18-34 of the R34
reading, 1,000 shuffles each). Kill: p > 0.05 or either half <= 0. Writes h62/result.json.
--tolerant (H64, h64/PREREG.md): a planted height counts as found when the pick has the same column count ceil(N/R);
writes h64/result.json."""
import os, sys, json, random
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
GD = os.path.join(root, 'swarm/G-D'); sys.path.insert(0, GD); sys.path.insert(0, here)
os.chdir(GD)
import dcore, escape, math
TOL = '--tolerant' in sys.argv
_tol = '--tolerant' in sys.argv; sys.argv = [sys.argv[0], 'none']
import types; r34 = types.ModuleType('r34')
src = open(os.path.join(GD, 'r34_replicate.py')).read().split("mode = sys.argv[1]")[0]; exec(compile(src, 'r34_replicate.py', 'exec'), r34.__dict__)
from settled_lines import settled_lines
MARKS = {'BLOB', 'BAR-SOLID', 'HOOK-L', 'DASH-V', '_', 'MULTI', 'MARK'}; FOLDS = {'PCT-SLASH': 'PCT', 'X-DOT': 'X', 'X-CURL': 'X'}
def load(folds):
    raw = settled_lines(root, 'c2', drop_clear=True)
    return [l for l in ([FOLDS.get(s, s) if folds else s for s in v if s not in MARKS] for v in raw.values()) if l]
out = {}
for variant, folds in (('rule+folds', True), ('rule', False)):
    T = load(folds); L = [len(l) for l in T]; N = sum(L)
    escape.L2 = L; escape.N2 = N; escape.cv = dcore.curve_of(T)
    rng = random.Random(6262); escape.rng = rng; ctrl = {}
    for R in (7, 19, 33):
        picks = [r34.scan(escape.trans(R), rng)[0] for _ in range(12)]
        hit = lambda p: p == f'R{R}' or (_tol and p.startswith('R') and math.ceil(N / int(p[1:])) == math.ceil(N / R))
        ctrl[f'TRANS-{R}'] = dict(own_height=sum(hit(p) for p in picks), picks=picks)
    passed = all(v['own_height'] >= 10 for v in ctrl.values())
    res = dict(N=N, lines=len(T), control=ctrl, control_pass=passed); print(variant, 'control', {k: v['own_height'] for k, v in ctrl.items()}, passed, flush=True)
    if passed:
        rng = random.Random(4242); b, s = r34.scan(T, rng)
        nul = sorted(r34.scan([rng.sample(l, len(l)) for l in T], rng)[1] for _ in range(200))
        res.update(best=b, best_columns=(math.ceil(N / int(b[1:])) if b.startswith('R') else None), score=round(s, 2), null_median=round(nul[100], 2), null_p95=round(nul[190], 2), p_ge=sum(x >= s for x in nul) / 200)
        seq = [x for l in T for x in l]; rows = r34.grid(seq, 34); halves = {}
        for name, rr in (('rows1-17', rows[:17]), ('rows18-34', rows[17:])):
            z = dcore.zstats(rr, rng, 1000); halves[name] = round(z['mi1']['z'] + z['bg2']['z'] + z['rep3']['z'] - z['dbl']['z'], 2)
        res['halves'] = halves; res['kill'] = res['p_ge'] > 0.05 or min(halves.values()) <= 0
        print(variant, {k: v for k, v in res.items() if k != 'control'}, flush=True)
    out[variant] = res
json.dump(out, open(os.path.join(root, 'h64' if _tol else 'h62', 'result.json'), 'w'), indent=1)
