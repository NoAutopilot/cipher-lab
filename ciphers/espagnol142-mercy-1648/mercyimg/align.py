#!/usr/bin/env python3
"""MERCY-IMG: align blind reader TSVs (crop, groups, notes; crops f22r_r16r24_Lnn_s1/s2) to ciphertext.tsv rows r16-r24.
Merges s1/s2 at the overlap, aligns digits (edit distance), and scores each token: digits reproduced, own group.
Usage: align.py readA.tsv [readB.tsv]  -> writes <read>_tokens.tsv beside each read and prints the control numbers."""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
ROWS = [f"r{n}" for n in range(16, 25)]
trans = {r: [] for r in ROWS}
for r in csv.DictReader(open(os.path.join(T, 'ciphertext.tsv')), delimiter='\t'):
    if r['line'] in trans: trans[r['line']].append((int(r['position']), r['sign'], r['confidence']))

def merge(s1, s2):
    a = [g for g in s1 if '|' not in g]; b = [g for g in s2 if '|' not in g]
    for k in range(min(5, len(a), len(b)), 0, -1):
        if a[-k:] == b[:k]: return a + b[k:], k
    return a + b, 0

def nw(t, r):
    n, m = len(t), len(r); INF = 1e9
    D = [[0.0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1): D[i][0] = i
    for j in range(1, m+1): D[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            c = 0 if (t[i-1] == r[j-1]) else (0.5 if r[j-1] == '?' else 1)
            D[i][j] = min(D[i-1][j-1]+c, D[i-1][j]+1, D[i][j-1]+1)
    i, j, pairs = n, m, []
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            c = 0 if (t[i-1] == r[j-1]) else (0.5 if r[j-1] == '?' else 1)
            if D[i][j] == D[i-1][j-1]+c: pairs.append((i-1, j-1)); i -= 1; j -= 1; continue
        if i > 0 and D[i][j] == D[i-1][j]+1: pairs.append((i-1, None)); i -= 1; continue
        pairs.append((None, j-1)); j -= 1
    return pairs[::-1]

def score(path):
    reads = {}
    for r in csv.DictReader(open(path), delimiter='\t'):
        ln, seg = r['crop'].replace('.jpg', '').split('_')[-2:]
        reads.setdefault(ln, {})[seg] = r['groups'].split()
    out, H, Hok, Hown = [], 0, 0, 0
    for k, row in enumerate(ROWS):
        rd = reads.get(f"L{k+1:02d}", {})
        groups, ov = merge(rd.get('s1', []), rd.get('s2', []))
        tch, ttok = [], []
        for idx, (pos, sign, conf) in enumerate(trans[row]):
            for ch in sign: tch.append(ch); ttok.append(idx)
        rch, rgrp = [], []
        for gi, g in enumerate(groups):
            for ch in g: rch.append(ch); rgrp.append(gi)
        pairs = nw(tch, rch)
        got = {i: [] for i in range(len(trans[row]))}; grp = {i: set() for i in range(len(trans[row]))}
        last_tok = None
        for ti, ri in pairs:
            if ti is not None:
                last_tok = ttok[ti]
                got[ttok[ti]].append(rch[ri] if ri is not None else '-')
                if ri is not None: grp[ttok[ti]].add(rgrp[ri])
            elif last_tok is not None and any(p[0] is not None and ttok[p[0]] == last_tok for p in pairs if p[1] is not None and p[1] > ri):
                got[last_tok].append('+' + rch[ri])
        tokens_of_group = {}
        for i, gs in grp.items():
            for g in gs: tokens_of_group.setdefault(g, set()).add(i)
        for i, (pos, sign, conf) in enumerate(trans[row]):
            d = ''.join(got[i]); gs = sorted(grp[i])
            own = len(gs) == 1 and tokens_of_group[gs[0]] == {i} and groups[gs[0]] == d
            cover = ' '.join(groups[g] for g in gs)
            out.append((row, pos, sign, conf, d, int(d == sign), int(own), cover))
            if conf == 'H': H += 1; Hok += d == sign; Hown += own
    op = path.replace('.tsv', '_tokens.tsv')
    with open(op, 'w') as f:
        f.write('line\tpos\tsign\tconf\treader_digits\tdigits_ok\town_group\tcovering_groups\n')
        for o in out: f.write('\t'.join(map(str, o)) + '\n')
    print(f"{os.path.basename(path)}: H tokens {H}; glyph reproduced {Hok} ({Hok/H:.3f}); own group {Hown} ({Hown/H:.3f}) -> {op}")
    return out

if __name__ == '__main__':
    for p in sys.argv[1:]: score(p)
