#!/usr/bin/env python3
"""R14-SURDP: per-pair sign-to-letter DP alignment of inv. 373 blind cipher lines to their gloss lines, scored as agreement with a
fixed pooled sign table against a shuffled-gloss-line control re-aligned the same way (PREREG.md, pushed 1a3b32a91 first).
Runs scan 0746 (target, T = 0693+0702+0730) and scan 0702 (instrument check, T = 0693+0730). Writes dp.out, dp_pairs.tsv,
dp_sign_table.tsv, dp_candidates.tsv. No key edit."""
import os, re, random, collections
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, '..')
def rows(p):
    for l in open(p, encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        yield l.rstrip('\n').split('\t')
def table(scans):
    T = {}
    for s in scans:
        p = os.path.join(P, s, 'sign_table.tsv'); hdr = None
        for f in rows(p):
            if f[0] == 'code': hdr = f; continue
            col = hdr.index('letters_seen')
            T.setdefault(f[0], set()).update(x.split(':')[0] for x in f[col].split())
    T['[y-fam]'] = {'m', 'n'}
    return T
ALIAS = {'[ij]': '[y-fam]', 'y': '[y-fam]', 'ÿ': '[y-fam]', '[lambda]': 'λ', '[d-loop]': '[ezh-dot]', '[x-dots]': '[x-dot]'}
EQ = {'j': 'i', 'y': 'i', 'ij': 'i', 'u': 'v'}
def norm(c): return EQ.get(c, c)
TOK = re.compile(r'\[[^\]]+\]|\S')
DROP = {'-', '.', "'", '–', '"', ',', ';', ':', '|', '/', '%'}
def csigns(s, crop):
    s = s.replace('\\&', '&')
    s = re.sub(r'\[[^\]]+\]', lambda m: m.group(0).replace(' ', '_').replace(':', '='), s)
    if crop == 'L01' and SCAN == '0746': s = re.sub(r'^\s*2\s*o', '', s)  # PREREG: plain numbered point "2o"
    return [ALIAS.get(x, x) for x in TOK.findall(s) if x not in DROP]
def gletters(s):
    s = re.sub(r'[^A-Za-zÀ-ÿ]', '', s).lower(); out, i = [], 0
    while i < len(s):
        if s[i:i+2] == 'ij': out.append('ij'); i += 2
        else: out.append(s[i]); i += 1
    return [norm(x) for x in out]
def ok(c, x, T): return c in T and x in {norm(v) for v in T[c]}
def dp(cs, gs, T, band=6, gap=-0.5):
    n, m = len(cs), len(gs); NEG = -1e9
    S = [[NEG] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]
    inb = lambda i, j: abs(j - i * m / max(n, 1)) <= band
    S[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if (i or j) == 0 or not inb(i, j): continue
            c = []
            if i and j and S[i-1][j-1] > NEG: c.append((S[i-1][j-1] + (1 if ok(cs[i-1], gs[j-1], T) else 0), 'D'))
            if j and S[i][j-1] > NEG: c.append((S[i][j-1] + gap, 'G'))   # letter unmatched
            if i and S[i-1][j] > NEG: c.append((S[i-1][j] + gap, 'C'))   # sign unmatched
            if c:
                best = max(v for v, _ in c); S[i][j], B[i][j] = best, next(t for v, t in c if v == best)
    if S[n][m] <= NEG: return []
    i, j, al = n, m, []
    while i or j:
        t = B[i][j]
        if t == 'D': al.append((cs[i-1], gs[j-1])); i -= 1; j -= 1
        elif t == 'G': j -= 1
        else: i -= 1
    return al[::-1]
def score(pairs, T):
    k = [(c, x) for c, x in pairs if c in T]
    return (sum(ok(c, x, T) for c, x in k), len(k))
def A(lines, glosses, T):
    a = n = 0
    for cs, gs in zip(lines, glosses):
        x, y = score(dp(cs, gs, T), T); a += x; n += y
    return a / n if n else 0.0, n
def derange(rnd, k):
    while True:
        p = list(range(k)); rnd.shuffle(p)
        if all(p[i] != i for i in range(k)): return p
def run(scan, d, tabs, seed, out, write=False):
    global SCAN; SCAN = scan
    T = table(tabs)
    blind = {f[0]: f[2] for f in rows(os.path.join(P, d, 'passA_sonnet_blind.tsv')) if len(f) > 2 and f[1] == 'cipher'}
    gloss = {f[0]: f[1] for f in rows(os.path.join(P, d, 'gloss_reconciled.tsv')) if f[0] != 'crop'}
    crops = [c for c in sorted(gloss) if c in blind]
    L = [csigns(blind[c], c) for c in crops]; G = [gletters(gloss[c]) for c in crops]
    keep = [i for i in range(len(crops)) if L[i] and G[i]]
    crops = [crops[i] for i in keep]; L = [L[i] for i in keep]; G = [G[i] for i in keep]
    real, n = A(L, G, T)
    rnd = random.Random(seed); c1 = []
    for _ in range(1000):
        p = derange(rnd, len(G)); c1.append(A(L, [G[q] for q in p], T)[0])
    rnd = random.Random(seed * 10); c2 = []
    for _ in range(1000):
        gg = []
        for g in G: g = g[:]; rnd.shuffle(g); gg.append(g)
        c2.append(A(L, gg, T)[0])
    c1.sort(); c2.sort()
    gate = 'SAME SYSTEM (DP)' if real >= 0.50 and real > c1[989] else 'not shown'
    out.append(f'{scan}: pairs {len(crops)}, signs {sum(map(len, L))}, letters {sum(map(len, G))}, T from {"+".join(t[6:10] for t in tabs)} '
               f'({len(T)} codes); keyed aligned {n}, A {real:.3f}; C1 shuffled-gloss-lines mean {sum(c1)/1000:.3f} p99 {c1[989]:.3f} '
               f'max {c1[-1]:.3f}; C2 within-line permuted mean {sum(c2)/1000:.3f} p99 {c2[989]:.3f} -> {gate}')
    if write:
        pr = ['crop\tsigns\tletters\tkeyed\tagree\tA\tC1_pair_mean']
        tab = collections.defaultdict(collections.Counter)
        for i, c in enumerate(crops):
            al = dp(L[i], G[i], T); a, k = score(al, T)
            others = [score(dp(L[i], G[j], T), T) for j in range(len(G)) if j != i]
            om = sum(x / y for x, y in others if y) / max(1, sum(1 for _, y in others if y))
            pr.append(f'{c}\t{len(L[i])}\t{len(G[i])}\t{k}\t{a}\t{a/k if k else 0:.3f}\t{om:.3f}')
            for s, x in al: tab[s][x] += 1
        st = ['code\tin_T\tletters_aligned']; cand = ['# codes whose top DP-aligned letter (>=3) is outside the pooled table; for a verifier, NOT applied', 'code\ttop\tcount\tT\tall']
        for s in sorted(tab):
            mc = tab[s].most_common(); st.append(f"{s}\t{'|'.join(sorted(T.get(s, ())))}\t{' '.join(f'{x}:{k}' for x, k in mc)}")
            if mc[0][1] >= 3 and not ok(s, mc[0][0], T): cand.append(f"{s}\t{mc[0][0]}\t{mc[0][1]}\t{'|'.join(sorted(T.get(s, ())))}\t{' '.join(f'{x}:{k}' for x, k in mc)}")
        for fn, body in (('dp_pairs.tsv', pr), ('dp_sign_table.tsv', st), ('dp_candidates.tsv', cand)):
            open(os.path.join(H, fn), 'w').write('\n'.join(body) + '\n')
out = []
run('0702', 'inv373_0702_r13', ['inv373_0693_r10', 'inv373_0730_r13'], 702, out)
run('0746', 'inv373_0746_r14', ['inv373_0693_r10', 'inv373_0702_r13', 'inv373_0730_r13'], 746, out, write=True)
open(os.path.join(H, 'dp.out'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
