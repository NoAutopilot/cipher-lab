#!/usr/bin/env python3
"""AVS53 test B, 3 Oct 2026: dictionary-segmentation regrade of letter 53's M tokens, rule pre-registered in
prereg_avs53.md "Test B" (committed before this script was run). Reuses regrade_53.py's dictionary, units, key, control
draws. Writes regrade_53b.tsv; --check exits 1 if stale."""
import os, sys
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D)
import regrade_53 as A
if open(os.path.join(D, 'regrade_53.tsv')).read() != A.txt: sys.exit('regrade_53.tsv is stale; run regrade_53.py first')
def seg(s):
    """per-position length of the covering piece (0 = uncovered); DP max covered letters, ties fewer pieces"""
    L = len(s); best = [(0, 0, None)] * (L + 1)
    for i in range(1, L + 1):
        b = (best[i - 1][0], best[i - 1][1], (i - 1, 0))
        for j in range(max(0, i - 24), i - 2):
            if s[j:i] in A.DICT:
                c = (best[j][0] + i - j, best[j][1] - 1, (j, i - j))
                if (c[0], c[1]) > (b[0], b[1]): b = c
        best[i] = b
    cov = [0] * L; i = L
    while i > 0:
        j, ln = best[i][2]
        for p in range(j, i): cov[p] = ln
        i = j
    return cov
def raw(u, k, sub=None):  # unfolded per-token letters (fold() would merge uu; keep one letter per token, w=uu stays 2)
    return [A.exc.get((r[0], int(r[1])), (k.get(sub[1], '?') if sub and sub[0] is r else k.get(r[2], '?'))) for r in u]
def covmap(u, k, sub=None):
    """coverage length per token: fold the unit with token boundaries tracked"""
    letters = raw(u, k, sub); s = ''; owner = []
    for t, v in enumerate(letters):
        v = A.fold(v) if v != '?' else '?'
        for ch in v: s += ch; owner.append(t)
    s2 = s.replace('uu', 'w')  # match fold(); map owners
    own2 = []; i = 0
    while i < len(s):
        if s[i:i + 2] == 'uu': own2.append((owner[i], owner[i + 1])); i += 2
        else: own2.append((owner[i],)); i += 1
    cov = seg(s2); out = [0] * len(letters)
    for p, ts in enumerate(own2):
        for t in ts: out[t] = max(out[t], cov[p])
    return out
tot = sum(len(u) for u in A.units)
real = [covmap(u, A.key) for u in A.units]
agg = sum(1 for c in real for x in c if x >= 3) / tot
ctrl = [[covmap(u, k) for u in A.units] for k in A.draws]
cagg = sorted(sum(1 for cu in cd for c in cu for x in [c] if x >= 3) / tot for cd in ctrl)
p99 = cagg[989]; gate1 = agg > p99
movedA = {(l.split('\t')[0], l.split('\t')[1]) for l in open(os.path.join(D, 'regrade_53.tsv')).read().splitlines()[1:] if l.split('\t')[9] == 'S'}
out = ['line\tpos\tsign\tvalue\tunit\tcover_len\tctrl_rate\tdiffer_alt\talt_cover_len\tmove\twhy']
for ui, u in enumerate(A.units):
    for ti, r in enumerate(u):
        if r[3] != 'M' or r[2] not in A.key or (r[0], r[1]) in movedA: continue
        cr = sum(1 for cd in ctrl if cd[ui][ti] >= 4) / 1000
        a = ''; ac = ''
        if r[4].startswith('differ'):
            a = A.alt.get((r[0], int(r[1])), ''); a = a if a in A.key and a != r[2] else ''
            ac = str(covmap(u, A.key, (r, a))[ti]) if a else ''
        mv = gate1 and real[ui][ti] >= 4 and cr <= 0.05 and not (ac and int(ac) >= 4)
        out.append('\t'.join([r[0], r[1], r[2], A.key[r[2]], A.dec(u, A.key), str(real[ui][ti]), f'{cr:.3f}', a, ac,
                              'S' if mv else 'M', r[4]]))
txt = '\n'.join(out) + '\n'
summary = (f'letters {tot}; covered (piece>=3) under key_53 {agg:.3f}; control mean {sum(cagg)/1000:.3f}, p99 {p99:.3f}, '
           f'max {cagg[-1]:.3f}; gate1 {"PASS" if gate1 else "FAIL"}; eligible {len(out)-1}; '
           f'move {sum(1 for l in out[1:] if l.split(chr(9))[9]=="S")}')
p = os.path.join(D, 'regrade_53b.tsv')
if __name__ == '__main__':
    print(summary)
    if '--check' in sys.argv and open(p).read() != txt: sys.exit(1)
    if '--check' not in sys.argv: open(p, 'w').write(txt)
# apply: exceptions_53.tsv keeps its own rows and carries one AVS53 row per token moved by test A or test B
ex = open(os.path.join(D, 'exceptions_53_s1.tsv')).read().splitlines()
keep = [l for l in ex if 'AVS53' not in l]
add = []
for name, text in (('A', A.txt), ('B', txt)):
    for l in text.splitlines()[1:]:
        f = l.split('\t')
        if f[9] == 'S':
            add.append('\t'.join([f[0], f[1], f[3], 'S', f'AVS53 test {name} (prereg_avs53.md): key_53 reads a period-German '
                                  f'dictionary word here, control rate {f[6]}; transcription flag kept in ciphertext_53.tsv']))
ex_txt = '\n'.join(keep + add) + '\n'
pe = os.path.join(D, 'exceptions_53_s1.tsv')
if __name__ == '__main__':
    if '--check' in sys.argv:
        sys.exit(0 if open(pe).read() == ex_txt else 1)
    open(pe, 'w').write(ex_txt)
