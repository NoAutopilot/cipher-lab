#!/usr/bin/env python3
"""SFZ-G1 (14 Oct 2026): key_r5323.tsv from SFZ-R5323B's two blind passes (agreed cells only), plus the 11 control keys.
Rule fixed in ../PREREG-SFZ-G1.md before this ran.   python3 build_key.py [--check]"""
import os, re, sys, glob
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, '..', 'r5323b')
LABELS = set()
for g in ('labels_G1.md', 'labels_G2.md'):
    for l in open(os.path.join(R, g)):
        m = re.match(r'\|\s*(\S+)\s*\|', l)
        if m and m.group(1) not in ('label', '---'): LABELS.add(m.group(1))
SHEETS = {}
for l in open(os.path.join(R, 'sheet_map.tsv')).read().split('\n')[1:]:
    if l: s, rec, b = l.split('\t'); SHEETS[s] = rec

def cells(p):
    out = {}
    for f in glob.glob(os.path.join(R, f'pass{p}_G*_b*.tsv')):
        for l in open(f):
            parts = l.rstrip('\n').split('\t')
            if len(parts) < 3: continue
            sh, let, toks = parts[0], parts[1], parts[2]
            for t in toks.split():
                if t in LABELS: out.setdefault(sh, set()).add((t, let))
    return out

def build(sheet, A, B):
    agreed = A.get(sheet, set()) & B.get(sheet, set())
    union = A.get(sheet, set()) | B.get(sheet, set())
    by = {}
    for lab, let in agreed: by.setdefault(lab, set()).add(let)
    prim = {lab: next(iter(v)) for lab, v in by.items() if len(v) == 1}
    conf = {lab: sorted(v) for lab, v in by.items() if len(v) > 1}
    uby = {}
    for lab, let in union: uby.setdefault(lab, set()).add(let)
    loose = dict(prim)
    for lab, v in uby.items():
        if lab not in prim and lab not in conf and len(v) == 1: loose[lab] = next(iter(v))
    return prim, conf, loose

def write(path, key, grades):
    s = 'sign\tvalue\tgrade\n' + ''.join(f'{k}\t{key[k]}\t{grades[k]}\n' for k in sorted(key))
    return path, s

def main(check):
    A, B = cells('A'), cells('B'); files = []
    prim, conf, loose = build('sheet_03', A, B)
    files.append(write('key_r5323.tsv', prim, {k: 'S' for k in prim}))
    files.append(write('key_r5323_loose.tsv', loose, {k: ('S' if k in prim else 'M') for k in loose}))
    log = [f'# R5323 (sheet_03): {len(prim)} agreed single-letter rows; conflicts (left out): ' +
           (', '.join(f'{k}:{"/".join(v)}' for k, v in sorted(conf.items())) or 'none') + f'; loose adds {len(loose)-len(prim)} M rows']
    for sh in sorted(SHEETS):
        if sh == 'sheet_03': continue
        p, c, _ = build(sh, A, B); rec = SHEETS[sh]
        files.append(write(f'ctl/key_{rec}.tsv', p, {k: 'S' for k in p}))
        log.append(f'# {rec} ({sh}): {len(p)} rows; conflicts {len(c)}')
    files.append(('build.log', '\n'.join(log) + '\n'))
    bad = 0
    for rel, s in files:
        path = os.path.join(H, rel)
        if check:
            if not os.path.exists(path) or open(path).read() != s: print('STALE', rel); bad = 1
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True); open(path, 'w').write(s)
    print('\n'.join(log)); return bad

if __name__ == '__main__': sys.exit(main('--check' in sys.argv))
