#!/usr/bin/env python3
"""R15-SUR758: re-score 0758 with only the image-labelled reader `s` / `i j` tokens changed (PREREG.md, pushed f53d915f1 before
any crop was looked at). Reuses ../inv373_alias_r15/alias_run.py's driver (and through it R14-SURDP's dp_align.py, unchanged):
same T (0693+0702+0730 sign tables + [sh-lig]={h}), same C1 (1,000 deranged-gloss draws, seed 758), same gate. Writes retok.out,
retok_r15.tsv (classes that PASS)."""
import os, re
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, '..')
src = open(os.path.join(P, 'inv373_alias_r15', 'alias_run.py'), encoding='utf-8').read().split('\nout = []; allp = []')[0]
ns = {'__file__': os.path.join(P, 'inv373_alias_r15', 'alias_run.py')}; exec(src, ns)
lab = [l.rstrip('\n').split('\t') for l in open(os.path.join(H, 'labels.tsv'), encoding='utf-8') if l[0] != '#' and not l.startswith('unit')]
S = {}; IJ = {}
for u, crop, _, label, _ in lab:
    (S if u.startswith('S') else IJ).setdefault(crop, []).append(label)
def per_token(pat, labels, yes, mark):
    def f(s, crop):
        L = list(labels.get(crop, [])); out = []
        for p in re.split(r'(\[[^\]]*\])', s):
            if p.startswith('['): out.append(p); continue
            out.append(re.sub(pat, lambda m: mark if L.pop(0) == yes else m.group(0), p))
        assert not L, (crop, L)
        return ''.join(out)
    return f
fS = per_token(r'(?<!\S)s s(?!\S)|(?<!\S)s(?!\S)', S, 'SH', '‹sh›')
fIJ = per_token(r'(?<!\S)i j(?!\S)', IJ, 'ONE', '‹ij›')
# alias_run's tokens() has no per-crop hook: wrap it so the per-token labels are applied first
_tok = ns['tokens']
def tokens(raw, crop, scan, alias):
    if alias: raw = fIJ(fS(raw, crop), crop)
    return _tok(raw, crop, scan, alias)
# _tok with alias truthy re-applies ALIASES (scans tuple empty below, so none fires); only the image labels above change tokens
ns['ALIASES'].clear(); ns['ALIASES'].update({'A2': ((), None, '[sh-lig] (image SH)'), 'A3': ((), None, '[ij] (image ONE)')})
ns['tokens'] = tokens
out = []; passed = ns['run']('0758', 'inv373_0758_r14', ['inv373_0693_r10', 'inv373_0702_r13', 'inv373_0730_r13'], 758, out)
open(os.path.join(H, 'retok.out'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
rows_ = ['# R15-SUR758 image-labelled classes that PASSed the PREREG gate (reader-code equivalences inside inv. 373 passes; not key values)',
         'scan\tclass\tn_al\tagree\tshare\tC1_p99']
rows_ += [f'{s}\t{a}\t{n}\t{k}\t{sh:.3f}\t{p:.3f}' for s, a, n, k, sh, p in passed]
open(os.path.join(H, 'retok_r15.tsv'), 'w').write('\n'.join(rows_) + '\n')
