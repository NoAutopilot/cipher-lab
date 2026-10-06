#!/usr/bin/env python3
"""R14-SURDP2: R14-SURDP's per-pair DP (../inv373_0746_dp_r14/dp_align.py, functions loaded unchanged) on 0758 and on the
word-unaligned lines of 0730 and 0702, per PREREG.md (pushed 5e5d7eb75 first). Writes dp2.out and per-run tsv files. No key edit."""
import os, random, collections
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, '..')
src = open(os.path.join(P, 'inv373_0746_dp_r14', 'dp_align.py'), encoding='utf-8').read().split('\nout = []')[0]
ns = {'__file__': os.path.join(P, 'inv373_0746_dp_r14', 'dp_align.py')}; exec(src, ns)
table, csigns0, gletters, dp, score, A, derange, rows, ok = (ns[k] for k in
    ('table', 'csigns', 'gletters', 'dp', 'score', 'A', 'derange', 'rows', 'ok'))
def csigns(s, crop): return [x for x in csigns0(s, crop) if not x.startswith('[plain')]  # PREREG addition (a)
def run(tag, scan, d, tabs, seed, subset, out, write=True):
    ns['SCAN'] = scan; T = table(tabs)
    blind = {f[0]: f[2] for f in rows(os.path.join(P, d, 'passA_sonnet_blind.tsv')) if len(f) > 2 and f[1] == 'cipher'}
    gloss = {f[0]: f[1] for f in rows(os.path.join(P, d, 'gloss_reconciled.tsv')) if f[0] != 'crop'}
    crops = [c for c in sorted(gloss) if c in blind and (subset is None or c in subset)]
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
    gate = ('non-test (< 30 keyed)' if n < 30 else 'SAME SYSTEM (DP)' if real >= 0.50 and real > c1[989] else 'not shown')
    out.append(f'{tag} {scan}: pairs {len(crops)}, signs {sum(map(len, L))}, letters {sum(map(len, G))}, T from '
               f'{"+".join(t[6:10] for t in tabs)} ({len(T)} codes); keyed aligned {n}, A {real:.3f}; C1 shuffled-gloss-lines mean '
               f'{sum(c1)/1000:.3f} p99 {c1[989]:.3f} max {c1[-1]:.3f}; C2 within-line permuted mean {sum(c2)/1000:.3f} p99 {c2[989]:.3f} -> {gate}')
    if not write: return
    pr = ['crop\tsigns\tletters\tkeyed\tagree\tA\tC1_pair_mean']; tab = collections.defaultdict(collections.Counter)
    for i, c in enumerate(crops):
        al = dp(L[i], G[i], T); a, k = score(al, T)
        others = [score(dp(L[i], G[j], T), T) for j in range(len(G)) if j != i]
        om = sum(x / y for x, y in others if y) / max(1, sum(1 for _, y in others if y))
        pr.append(f'{c}\t{len(L[i])}\t{len(G[i])}\t{k}\t{a}\t{a/k if k else 0:.3f}\t{om:.3f}')
        for s, x in al: tab[s][x] += 1
    st = ['code\tin_T\tletters_aligned']
    cand = ['# codes whose top DP-aligned letter (>=3) is outside this run\'s pooled table; for a verifier, NOT applied', 'code\ttop\tcount\tT\tall']
    for s in sorted(tab):
        mc = tab[s].most_common(); st.append(f"{s}\t{'|'.join(sorted(T.get(s, ())))}\t{' '.join(f'{x}:{k}' for x, k in mc)}")
        if mc[0][1] >= 3 and not ok(s, mc[0][0], T): cand.append(f"{s}\t{mc[0][0]}\t{mc[0][1]}\t{'|'.join(sorted(T.get(s, ())))}\t{' '.join(f'{x}:{k}' for x, k in mc)}")
    for fn, body in ((f'dp2_{tag}_pairs.tsv', pr), (f'dp2_{tag}_sign_table.tsv', st), (f'dp2_{tag}_candidates.tsv', cand)):
        open(os.path.join(H, fn), 'w').write('\n'.join(body) + '\n')
out = []
run('regress', '0702', 'inv373_0702_r13', ['inv373_0693_r10', 'inv373_0730_r13'], 702, None, out, write=False)
run('R1', '0758', 'inv373_0758_r14', ['inv373_0693_r10', 'inv373_0702_r13', 'inv373_0730_r13'], 758, None, out)
run('R2', '0730', 'inv373_0730_r13', ['inv373_0693_r10', 'inv373_0702_r13'], 730, set('L03 L05 L06 L07 L08 L09 L10'.split()), out)
run('R3', '0702', 'inv373_0702_r13', ['inv373_0693_r10', 'inv373_0730_r13'], 7020, set(('L01 L06 L07 L08 L09 L12 L13 L14 L16 L17 L18 '
    'L19 L20 L22 R01 R02 R03 R04 R05 R06 R07 R09 R10 R11 R12 R13 R14 R15 R17 R18 R19 R20').split()), out)
open(os.path.join(H, 'dp2.out'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
