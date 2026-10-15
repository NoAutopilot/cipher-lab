#!/usr/bin/env python3
"""MAT-ORL (15 Oct 2026): o relabel by shape (oA plain round / oB round with right stem), per orl/PREREG-MAT-ORL.md.

Labels = the agreed (consensus) labels of the two blind readers MAT-O3X and MAT-R2 (osplit/sort_answers_r2cons.tsv: both A -> oA,
both B -> oB; disagreement or X -> o unchanged). Those labels exist only for the 78 o tokens of the f.91-92 margin blocks
(osplit/sort_tokens.tsv); no reader crop covers any o of the 13 target leaves in ciphertext.txt, so there every o stays o.

  coverage            prints, per 13-leaf scope and per f.91 scope, the o / oA / oB counts and H-code counts (for the power control)
  build OUTDIR        writes a decode_key.py-ready copy of the f.91 blocks (A-F; E from f91e only, PREREG; non-H draft signs -> '?'),
                      o relabelled oA / oB by the agreed labels; key.tsv + decode.json copied, oA / oB left unkeyed.
Usage: python3 orl/make_orl.py coverage | build OUTDIR"""
import collections, csv, os, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
OS = os.path.join(T, 'osplit'); F91 = os.path.join(T, 'f91')
DRAFTS = ('f91', 'f91c', 'f91e')
BLOCK_DRAFT = {'A': 'f91', 'B': 'f91', 'D': 'f91', 'C': 'f91c', 'F': 'f91c', 'E': 'f91e'}

def agreed():
    ans = {r['id']: r['shape'].strip().upper() for r in csv.DictReader(open(os.path.join(OS, 'sort_answers_r2cons.tsv')), delimiter='\t')}
    lab = {}
    for r in csv.DictReader(open(os.path.join(OS, 'sort_tokens.tsv')), delimiter='\t'):
        s = ans.get(r['id'], 'X')
        if s in ('A', 'B'): lab[(r['draft'], r['line'], int(r['position']))] = 'o' + s
    return lab

def f91_lines():
    lab = agreed(); lines = collections.OrderedDict()
    for d in DRAFTS:
        for r in csv.DictReader(open(os.path.join(F91, f'ciphertext_draft_{d}.tsv')), delimiter='\t'):
            if BLOCK_DRAFT.get(r['line'][0]) != d: continue
            s = r['sign'] if r['confidence'] == 'H' else '?'
            if s == 'o': s = lab.get((d, r['line'], int(r['position'])), 'o')
            lines.setdefault(f"f91{d[3:]}-{r['line']}", []).append(s)
    return lines

def leaf_lines():
    out = collections.OrderedDict()
    for l in open(os.path.join(T, 'ciphertext.txt')):
        p = l.rstrip('\n').split('\t')
        if len(p) > 1: out[p[0]] = p[1].split()
    return out

def hkey():
    k = {}
    for r in csv.reader(open(os.path.join(T, 'key.tsv')), delimiter='\t'):
        if len(r) >= 3 and r[2] == 'H' and len(r[1]) == 1 and r[1].isalpha(): k[r[0]] = r[1]
    return k

def counts(lines):
    return collections.Counter(s for v in lines.values() for s in v)

if __name__ == '__main__':
    if sys.argv[1:2] == ['coverage']:
        hk = hkey()
        for name, ln in (('13 leaves (ciphertext.txt)', leaf_lines()), ('f.91 blocks A-F (E f91e only)', f91_lines())):
            c = counts(ln)
            print(f"{name}: tokens {sum(c.values())}, o {c['o']}, oA {c['oA']}, oB {c['oB']}, '?' {c['?']}")
            print('  H single-letter codes by count:', ', '.join(f'{k}={hk[k]}:{c[k]}' for k in sorted(hk, key=lambda k: -c[k]) if c[k]))
    elif sys.argv[1:2] == ['build']:
        out = sys.argv[2]; os.makedirs(out, exist_ok=True)
        for f in ('decode.json', 'key.tsv'): shutil.copy(os.path.join(T, f), os.path.join(out, f))
        with open(os.path.join(out, 'ciphertext.txt'), 'w') as fh:
            for k, v in f91_lines().items(): fh.write(f"{k}\t{' '.join(v)}\t\n")
        print('built', out)
    else:
        print(__doc__); sys.exit(2)
