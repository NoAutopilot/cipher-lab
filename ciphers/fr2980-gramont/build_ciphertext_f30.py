#!/usr/bin/env python3
"""Build ciphertext_f30.tsv from the reconciler's reading of the f.30 crops (passR_f30.tsv) and the two blind
passes (passA_f30.tsv, passB_f30.tsv); write the per-line agreement table and the per-sign disagreement log.
  python3 build_ciphertext_f30.py          write ciphertext_f30.tsv, reconciliation_f30_lines.tsv, reconciliation_f30_signs.tsv
  python3 build_ciphertext_f30.py --check  exit 1 if any of the three committed files is stale (rule 7)
passR_f30.tsv is the reading settled sign by sign from the crops (images/crops_f30/); the passes only set confidence:
  h = sign read firmly and at least one blind pass has the same code at the aligned position
  m = sign read firmly by the reconciler, neither pass agrees (settled from the image alone)
  l = reconciler marked the sign uncertain ('?') or illegible ('[?]')
Pass codes outside the atlas are normalised first (pass A wrote J for r3 and r for nr; pass B wrote sq for the box)."""
import sys, os, difflib, collections
H = os.path.dirname(os.path.abspath(__file__))
NORM = {'A': {'J': 'r3', 'r': 'nr', 'sq': 'BOX'}, 'B': {'sq': 'BOX', 'r': 'nr'}, 'R': {}}
def load(fn, who):
    d = {}
    for l in open(os.path.join(H, fn), encoding='utf-8'):
        p = l.rstrip('\n').split('\t')
        if len(p) < 2 or p[0] == 'row': continue
        d[p[0]] = [(NORM[who].get(t.rstrip('?'), t.rstrip('?')), t.endswith('?') and t != '[?]', t) for t in p[1].split()]
    return d
R, A, B = load('passR_f30.tsv', 'R'), load('passA_f30.tsv', 'A'), load('passB_f30.tsv', 'B')
def align(r, o):
    """map index in r (dots excluded from matching) -> aligned code in o or None"""
    ri = [i for i, t in enumerate(r) if t[0] != '.']; oi = [t[0] for t in o if t[0] != '.']
    rc = [r[i][0] for i in ri]
    m = {}
    sm = difflib.SequenceMatcher(None, rc, oi, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal' or (tag == 'replace' and i2 - i1 == j2 - j1):
            for k in range(i2 - i1): m[ri[i1 + k]] = oi[j1 + k]
    return m, sum(x.size for x in sm.get_matching_blocks()), len(rc), len(oi)
ct = ['line\tposition\tsign\tconfidence']; lines = ['line\tsigns\tagree_A\tagree_B\tA_B_agree\tpct_A\tpct_B\tpct_AB\th\tm\tl']
signs = ['line\tposition\tsettled\tpassA\tpassB\tbasis']
per = collections.defaultdict(lambda: [0] * 10)
for row in R:
    ln, half = row[:-1], row[-1]
    base = sum(1 for k in R if k[:-1] == ln and k[-1] < half and True for _ in R[k])  # offset of b-half positions
    r = R[row]; ma, na, _, _ = align(r, A.get(row, [])); mb, nb, _, _ = align(r, B.get(row, []))
    ab = difflib.SequenceMatcher(None, [t[0] for t in A.get(row, []) if t[0] != '.'], [t[0] for t in B.get(row, []) if t[0] != '.'], autojunk=False)
    nab = sum(x.size for x in ab.get_matching_blocks()); nlen = max(len([t for t in A.get(row, []) if t[0] != '.']), len([t for t in B.get(row, []) if t[0] != '.']))
    s = per[ln]
    for i, (c, unsure, raw) in enumerate(r):
        pos = base + i
        if c == '.': ct.append(f'{ln}\t{pos}\t.\th'); continue
        if unsure or c == '[?]': conf = 'l'
        elif ma.get(i) == c or mb.get(i) == c: conf = 'h'
        else: conf = 'm'
        ct.append(f'{ln}\t{pos}\t{c}\t{conf}'); s[0] += 1; s[7 + 'hml'.index(conf)] += 1
        a, b = ma.get(i, '-'), mb.get(i, '-')
        if not (a == b == c):
            signs.append(f'{ln}\t{pos}\t{raw}\t{a}\t{b}\t' + ('image: both passes differ' if a != c and b != c else
                         'image: agrees with pass A' if a == c else 'image: agrees with pass B'))
    s[1] += na; s[2] += nb; s[3] += nab; s[4] += len([t for t in r if t[0] != '.']); s[5] += nlen
for ln, s in per.items():
    lines.append(f'{ln}\t{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[1]/s[4]:.2f}\t{s[2]/s[4]:.2f}\t{s[3]/max(s[5],1):.2f}\t{s[7]}\t{s[8]}\t{s[9]}')
tot = [sum(s[k] for s in per.values()) for k in range(10)]
lines.append(f'TOTAL\t{tot[0]}\t{tot[1]}\t{tot[2]}\t{tot[3]}\t{tot[1]/tot[4]:.3f}\t{tot[2]/tot[4]:.3f}\t{tot[3]/tot[5]:.3f}\t{tot[7]}\t{tot[8]}\t{tot[9]}')
out = {'ciphertext_f30.tsv': '\n'.join(ct) + '\n', 'reconciliation_f30_lines.tsv': '\n'.join(lines) + '\n',
       'reconciliation_f30_signs.tsv': '\n'.join(signs) + '\n'}
if '--check' in sys.argv:
    ok = all(os.path.exists(os.path.join(H, f)) and open(os.path.join(H, f), encoding='utf-8').read() == s for f, s in out.items())
    print('f30 ciphertext up to date' if ok else 'STALE: run python3 build_ciphertext_f30.py'); sys.exit(0 if ok else 1)
for f, s in out.items(): open(os.path.join(H, f), 'w', encoding='utf-8').write(s)
print(lines[-1])
