#!/usr/bin/env python3
"""NZ-SURIJ: re-score inv. 373 0746 with only the image-labelled y-family / S tokens tagged (PREREG.md, pushed 898540e3c before any
0746 image was fetched). Reuses ../inv373_alias_r15/alias_run.py's driver (and through it R14-SURDP's dp_align.py, unchanged), as
R15-SUR758's retok_run.py did: T = 0693+0702+0730 sign tables + [sh-lig]={h}; C1 = 1,000 deranged-gloss draws, seed 746; same gate.
Run 1 (gated): IJ -> [ij] (tag A3), SH -> [sh-lig] (tag A4). Run 2 (descriptive, PREREG "also descriptive"): the Y-labelled tokens
tagged instead, to compare the plain y-form's m/n share with the IJ form's. Writes retok.out, retok_nz.tsv (classes that PASS)."""
import os, re
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, '..')
src = open(os.path.join(P, 'inv373_alias_r15', 'alias_run.py'), encoding='utf-8').read().split('\nout = []; allp = []')[0]
ns = {'__file__': os.path.join(P, 'inv373_alias_r15', 'alias_run.py')}; exec(src, ns)
lab = [l.rstrip('\n').split('\t') for l in open(os.path.join(H, 'labels.tsv'), encoding='utf-8') if l[0] != '#' and not l.startswith('unit')]
Y = {}; S = {}
for u, crop, cls, label, _ in lab:
    (Y if cls == 'Y' else S).setdefault(crop, []).append(label)
def apply(raw, crop, ytag):
    """Walk the reader string in order; each y-family unit consumes one Y label, each S unit one S label."""
    LY = list(Y.get(crop, [])); LS = list(S.get(crop, [])); out = []
    raw = raw.replace('[y-fam] j', '[y-fam]\x00')  # PREREG: L13 '[y-fam] j' is one unit
    for p in re.split(r'(\[[^\]]*\])', raw):
        if p == '[y-fam]':
            out.append('‹ij›' if LY.pop(0) == ytag else p)
        elif p == '[other: S-like]':
            out.append('‹sh›' if LS.pop(0) == 'SH' else p)
        elif p.startswith('['):
            out.append(p)
        else:
            p = re.sub(r'(?<!\S)y(?!\S)', lambda m: '‹ij›' if LY.pop(0) == ytag else 'y', p)
            p = re.sub(r'(?<!\S)S(?!\S)', lambda m: '‹sh›' if LS.pop(0) == 'SH' else 'S', p)
            out.append(p)
    assert not LY and not LS, (crop, LY, LS)
    s = ''.join(out)
    return s.replace('‹ij›\x00', '‹ij›').replace('\x00', ' j')
_tok = ns['tokens']; mode = {'ytag': 'IJ'}
def tokens(raw, crop, scan, alias):
    if alias: raw = apply(raw, crop, mode['ytag'])
    return _tok(raw, crop, scan, alias)
ns['ALIASES'].clear(); ns['ALIASES'].update({'A3': ((), None, '[ij] (image IJ)'), 'A4': ((), None, '[sh-lig] (image SH)')})
ns['tokens'] = tokens
tabs = ['inv373_0693_r10', 'inv373_0702_r13', 'inv373_0730_r13']
out = ['# run 1 (gated): IJ -> [ij], SH -> [sh-lig]']
passed = ns['run']('0746', 'inv373_0746_r14', tabs, 746, out)
mode['ytag'] = 'Y'; ns['ALIASES']['A3'] = ((), None, '[y-fam] (image Y, descriptive only, no gate)')
out.append('# run 2 (descriptive, no gate): Y-labelled y-forms tagged instead of IJ; SH as run 1')
ns['run']('0746', 'inv373_0746_r14', tabs, 746, out)
open(os.path.join(H, 'retok.out'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
rows_ = ['# NZ-SURIJ image-labelled classes that PASSed the PREREG gate on 0746 (reader-code equivalences inside inv. 373 passes; not key values)',
         'scan\tclass\tn_al\tagree\tshare\tC1_p99']
rows_ += [f'{s}\t{a}\t{n}\t{k}\t{sh:.3f}\t{p:.3f}' for s, a, n, k, sh, p in passed]
open(os.path.join(H, 'retok_nz.tsv'), 'w').write('\n'.join(rows_) + '\n')
