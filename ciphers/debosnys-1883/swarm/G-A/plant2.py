#!/usr/bin/env python3
"""DEB-SWARM-A held-out control: one homophonic key, two verse spans shaped like c2 (N 688, K 128) and c1 (N 134).
About 10 pct of c1-shaped tokens use signs never seen in the c2-shaped text (real c1: 13 of 136 tokens have a sign
absent from c2). Same uniform noise on both. Writes work/hA_<tag>.cip/.ans (c2-shape) and work/hB_<tag>.cip/.ans."""
import sys, os, random, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from plant import curve
def main(seed, noise, tag):
    rng = random.Random(seed); cv = curve('c2'); N = sum(cv); NB = 134
    lines = open(os.path.join(H, 'work', 'verse_lines.txt')).read().split('\n')[40:]
    i = rng.randrange(len(lines) - 300); text = ''
    while len(text) < N + NB + 40: text += lines[i]; i += 1
    A, B = text[:N], text[N + 40:N + 40 + NB]
    lc = collections.Counter(A); deficit = dict(lc); owner = []
    for cnt in cv:
        l = max(deficit, key=lambda x: deficit[x]); owner.append(l); deficit[l] -= cnt
    homs = collections.defaultdict(list)
    for k, l in enumerate(owner): homs[l].append(k)
    for l in set(A + B):
        if l not in homs: homs[l].append(len(owner)); owner.append(l); cv.append(1)
    def enc(t):
        return [rng.choices(homs[ch], weights=[cv[k] for k in homs[ch]])[0] for ch in t]
    a, b = enc(A), enc(B)
    K = len(owner)
    # B: ~10 pct tokens on fresh signs (per letter one fresh sign)
    fresh = {}
    for j, ch in enumerate(B):
        if rng.random() < 0.10:
            if ch not in fresh: fresh[ch] = K + len(fresh)
            b[j] = fresh[ch]
    for arr in (a, b):
        for j in range(len(arr)):
            if rng.random() < noise: arr[j] = rng.randrange(K)
    for nm, arr, t in (('hA', a, A), ('hB', b, B)):
        open(os.path.join(H, 'work', f'{nm}_{tag}.cip'), 'w').write(' '.join(map(str, arr)) + '\n')
        open(os.path.join(H, 'work', f'{nm}_{tag}.ans'), 'w').write(t + '\n')
if __name__ == '__main__':
    main(int(sys.argv[1]), float(sys.argv[2]), sys.argv[3])
