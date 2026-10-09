#!/usr/bin/env python3
"""V-MANT0490 audit sensitivity (9 Oct 2026; not a registered gate): re-score the PREREG statistic S (gloss_gate.py's align, key.tsv,
1000 permutations, seed 490) with the deciding-row spans' codes taken from each blind pass's raw digits instead of the solver's
reconciliation (the reconciler had seen key.tsv and the glosses). Variants: A = pass A's digits, B = pass B's, AB = digits only where both
passes agree, else the token is replaced by '?' (unkeyed). Writes vmant0490_sens.out; --check exits 1 if stale."""
import csv, difflib, os, random, sys, importlib.util
D = os.path.dirname(os.path.abspath(__file__))
argv = sys.argv; sys.argv = [argv[0], '--key', os.path.join(os.path.dirname(D), 'key.tsv')]
import io, contextlib
spec = importlib.util.spec_from_file_location('g', f'{D}/gloss_gate.py'); g = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(g)
sys.argv = argv
ct = list(csv.DictReader(open(f'{D}/ciphertext.tsv'), delimiter='\t'))
P = {n: list(csv.DictReader(open(f'{D}/pass{n}.tsv'), delimiter='\t')) for n in 'AB'}
def variant(n):  # per crop: reconciled token list -> pass token list (None where the pass has no aligned single token)
    out = {}
    for c in sorted(set(r['crop'] for r in ct)):
        r = [x['token'] for x in ct if x['crop'] == c]; p = [x['token'].rstrip('?') for x in P[n] if x['crop'] == c]
        v = list(r)
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=r, b=p, autojunk=False).get_opcodes():
            if op == 'equal': continue
            for k in range(i1, i2): v[k] = (p[j1 + (k - i1)] if (i2 - i1) == (j2 - j1) else '?')
        out[c] = (r, v)
    return out
def respan(var):
    sp = []
    for s in g.spans:
        if s['page'] != 'R' or s.get('r01line', 'n') == 'y': continue
        crop = 'c0490' + s['line'].split('+')[0]; r, v = var[crop]; codes = s['codes'].split()
        for i in range(len(r) - len(codes) + 1):
            if r[i:i + len(codes)] == codes: break
        else: raise SystemExit(f'span {s["span_id"]} not found in {crop}')
        sp.append(dict(s, codes=' '.join(v[i:i + len(codes)])))
    return sp
VA, VB = variant('A'), variant('B')
VAB = {c: (VA[c][0], [a if a == b else '?' for a, b in zip(VA[c][1], VB[c][1])]) for c in VA}
codes = list(g.key); vals0 = [g.key[c] for c in codes]; out = []
for name, var in (('reconciled', {c: (VA[c][0], VA[c][0]) for c in VA}), ('pass A digits', VA), ('pass B digits', VB), ('A=B only', VAB)):
    sp = respan(var); real = g.S(g.key, sp); nk = sum(c in g.key for s in sp for c in s['codes'].split())
    vals = list(vals0); rng = random.Random(490); ctl = []
    for _ in range(1000):
        rng.shuffle(vals); ctl.append(g.S(dict(zip(codes, vals)), sp))
    ctl.sort()
    out.append(f'{name}: S {real}/{nk} keyed; control mean {sum(ctl)/1000:.2f} p99 {ctl[989]} max {ctl[-1]}; '
               f'{"PASS" if real > ctl[989] and real >= 0.5 * nk else "FAIL"} (rule as PREREG)')
txt = '\n'.join(out) + '\n'; F = f'{D}/vmant0490_sens.out'
if '--check' in sys.argv:
    ok = open(F).read() == txt; print('up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(F, 'w').write(txt); print(txt, end='')
