#!/usr/bin/env python3
"""N5-VIVK: per-code support for key_tomokiyo.tsv from the clerk decipherment (writes key.tsv).
Grades: C where the key value is the top aligned letter with >= 3 matches, else M (applied after the run by the
worker, N5-VIVK). Decodes f.102r+f.102v+f.103r (reconciled) with the published key, aligns the decode to tx/dec_norm.txt[j0:] with the
same semi-global banded DP as stream_align.nw_score, and counts per code how often the aligned plaintext letter equals
the key's value. Run: python3 ciphers/fr16104-vivonne-spain-1572/tx/key_support.py"""
import json, os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(1, '/home/user/cipher-lab/tools')
import numpy as np, vivk_test as v, stream_align as sa
r = json.load(open(os.path.join(HERE, 'vivk_result.json')))
seq = sum((v.tokens(os.path.join(HERE, f'{p}_rec.tsv')) for p in ('f102r', 'f102v', 'f103r')), [])
let = sa.letters(open(os.path.join(HERE, 'dec_norm.txt')).read())[r['j0']:]
rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(T, 'key_tomokiyo.tsv'))][1:]
tk = {f[0]: ord(f[1]) - 97 for f in rows}
dec = np.array([tk.get(c, -1) for c in seq]); d2 = np.where(dec < 0, 26, dec)
E = np.full((27, 26), -1.0); E[np.arange(26), np.arange(26)] = 2.0
N, M = len(d2), len(let)
ref = np.arange(N + 1) * (M / N)
path, _, _ = sa.band_dp(d2, let, E, ref, 400, 1.0, 1.0, free_start=True)
al = defaultdict(Counter)
for i, j in path:
    al[seq[i]][chr(97 + let[j])] += 1
with open(os.path.join(T, 'key.tsv'), 'w') as f:
    f.write('code\tmeaning\tgrade\tsource\tn_aligned\tn_match\ttop_aligned\tnote\n')
    for fr in rows:
        c, m = fr[0], fr[1]; a = al.get(c, Counter()); n = sum(a.values()); k = a.get(m, 0)
        top = ','.join(f'{x}:{y}' for x, y in a.most_common(3))
        ok = bool(a) and a.most_common(1)[0][0] == m and k >= 3
        note = fr[3] + ('' if ok else f'; NOT top-aligned (top {top}): label likely merges glyphs or misread in the passes (S/s split, swash y, b); listed, not settled (rule 4)')
        f.write(f'{c}\t{m}\t{"C" if ok else "M"}\tpublished key (Tomokiyo, henryiii_Vivonne1.png); support: clerk decipherment fr.16105 ff.105v-108v\t{n}\t{k}\t{top}\t{note}\n')
tot = sum(sum(a.values()) for c, a in al.items() if c in tk); hit = sum(a.get(chr(97 + tk[c]), 0) for c, a in al.items() if c in tk)
unk = Counter(c for c in seq if c not in tk)
print(f'signs {N}, aligned pairs {len(path)}, keyed aligned {tot}, matching key value {hit} ({hit / max(1, tot):.3f})')
print('codes outside the key (count):', ', '.join(f'{c}:{n}' for c, n in unk.most_common(15)))
