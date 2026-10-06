#!/usr/bin/env python3
"""R15-SURALIAS: reader-code alias pass (PREREG.md, pushed 6a47a554b first) on inv. 373 scans 0702, 0730, 0758, re-scored with
R14-SURDP's DP (../inv373_0746_dp_r14/dp_align.py, functions loaded unchanged) before and after aliasing, with the shuffled-gloss
control C1. Writes alias.out, alias_pairs_<scan>.tsv, alias_r15.tsv (only aliases that PASS). No key or transcription edit."""
import os, re, random
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, '..')
src = open(os.path.join(P, 'inv373_0746_dp_r14', 'dp_align.py'), encoding='utf-8').read().split('\nout = []')[0]
ns = {'__file__': os.path.join(P, 'inv373_0746_dp_r14', 'dp_align.py')}; exec(src, ns)
table, csigns0, gletters, dp, score, A, derange, rows, ok = (ns[k] for k in
    ('table', 'csigns', 'gletters', 'dp', 'score', 'A', 'derange', 'rows', 'ok'))
def csigns(s, crop): return [x for x in csigns0(s, crop) if not x.startswith('[plain')]
def outside(s, f):  # apply f to the text outside [...] only
    return ''.join(p if p.startswith('[') else f(p) for p in re.split(r'(\[[^\]]*\])', s))
ALIASES = {  # id: (scans, function on the raw blind string, alias code as dp sees it, value set label)
    'A1': (('0702', '0730', '0758'), lambda s: outside(s, lambda p: p.replace('K', '‹k›')), 'k'),
    'A2': (('0758',), lambda s: outside(s, lambda p: re.sub(r'(?<!\S)s(?!\S)', '‹sh›', re.sub(r'(?<!\S)s s(?!\S)', '‹sh›', p))), '[sh-lig]'),
    'A3': (('0758',), lambda s: outside(s, lambda p: re.sub(r'(?<!\S)i j(?!\S)', '‹ij›', p)), '[y-fam]'),
    'A4': (('0730',), lambda s: s.replace('[other: ss-like]', '‹sh›'), '[sh-lig]'),
    'A5': (('0730',), lambda s: s.replace('[other: f-like]', '‹f›'), 'f'),
}
MARK = {'‹k›': ('A1', 'k'), '‹sh›': (None, '[sh-lig]'), '‹ij›': ('A3', '[ij]'), '‹f›': ('A5', 'f')}
def tokens(raw, crop, scan, alias):
    """Return (dp tokens, alias id per token or None)."""
    s = raw
    if alias:
        for a, (scans, f, _) in ALIASES.items():
            if scan in scans: s = f(s)
    # split out markers so each becomes one bracket token, remembering which alias made it
    tag = {'‹k›': 'A1', '‹ij›': 'A3', '‹f›': 'A5', '‹sh›': 'A2' if scan == '0758' else 'A4'}
    code = {'‹k›': 'k', '‹ij›': '[ij]', '‹f›': '[ALIASF]', '‹sh›': '[sh-lig]'}
    ids = []; parts = re.split(r'(‹[a-z]+›)', s); out = []
    for p in parts:
        if p in tag:
            t = csigns(code[p], crop); out += t; ids += [tag[p]] * len(t)
        elif p:
            t = csigns(p, crop); out += t; ids += [None] * len(t)
    out = ['f' if x == '[ALIASF]' else x for x in out]
    return out, ids
def run(scan, d, tabs, seed, lines_out):
    ns['SCAN'] = scan; T = table(tabs); T['[sh-lig]'] = {'h'}
    blind = {f[0]: f[2] for f in rows(os.path.join(P, d, 'passA_sonnet_blind.tsv')) if len(f) > 2 and f[1] == 'cipher'}
    gloss = {f[0]: f[1] for f in rows(os.path.join(P, d, 'gloss_reconciled.tsv')) if f[0] != 'crop'}
    crops = [c for c in sorted(gloss) if c in blind]
    G0 = [gletters(gloss[c]) for c in crops]
    res = {}
    for alias in (False, True):
        TI = [tokens(blind[c], c, scan, alias) for c in crops]
        keep = [i for i in range(len(crops)) if TI[i][0] and G0[i]]
        L = [TI[i][0] for i in keep]; I = [TI[i][1] for i in keep]; G = [G0[i] for i in keep]; cr = [crops[i] for i in keep]
        def alias_share(glist):
            st = {}
            for cs, ids, gs in zip(L, I, glist):
                # dp returns aligned (sign, letter) pairs without indices; re-run the alignment and walk it with indices
                al = dp_idx(cs, gs, T)
                for i, x in al:
                    a = ids[i]
                    if a is None: continue
                    n, k = st.get(a, (0, 0)); st[a] = (n + 1, k + ok(cs[i], x, T))
            return st
        real, n = A(L, G, T); rnd = random.Random(seed); c1 = []; c1a = []
        for _ in range(1000):
            p = derange(rnd, len(G)); gg = [G[q] for q in p]; c1.append(A(L, gg, T)[0])
            if alias: c1a.append(alias_share(gg))
        c1s = sorted(c1)
        verdict = 'SAME SYSTEM (DP)' if real >= 0.50 and real > c1s[989] else 'not shown'
        res[alias] = dict(n=n, A=real, mean=sum(c1) / 1000, p99=c1s[989], mx=c1s[-1], verdict=verdict,
                          share=alias_share(G) if alias else {}, c1a=c1a, pairs=len(cr),
                          nal=sum(1 for ids in I for x in ids if x))
        lines_out.append(f"{scan} {'after ' if alias else 'before'}: pairs {len(cr)}, signs {sum(map(len, L))}, T {'+'.join(t[6:10] for t in tabs)}"
                         f"+[sh-lig] ({len(T)} codes); keyed aligned {n}, A {real:.3f}; C1 mean {sum(c1)/1000:.3f} p99 {c1s[989]:.3f} "
                         f"max {c1s[-1]:.3f} -> {verdict}" + (f"; aliased tokens {res[alias]['nal']}" if alias else ''))
    b, a = res[False], res[True]; passed = []
    for aid, (nal, k) in sorted(a['share'].items()):
        sh = k / nal if nal else 0
        dist = sorted((d.get(aid, (0, 0))[1] / d[aid][0]) if d.get(aid, (0, 0))[0] else 0.0 for d in a['c1a'])
        p99 = dist[989]; mean = sum(dist) / 1000
        scan_ok = a['A'] >= b['A'] - 0.010 and a['verdict'].startswith('SAME')
        g = 'non-test (n_al < 5)' if nal < 5 else 'PASS' if sh >= 0.60 and sh > p99 and scan_ok else 'FAIL'
        lines_out.append(f"  {scan} {aid} -> {ALIASES[aid][2]}: n_al {nal}, agree {k}, share {sh:.3f}; C1 share mean {mean:.3f} p99 {p99:.3f}; "
                         f"scan A {b['A']:.3f} -> {a['A']:.3f} -> {g}")
        if g == 'PASS': passed.append((scan, aid, nal, k, sh, p99))
    return passed
def dp_idx(cs, gs, T, band=6, gap=-0.5):
    """dp_align.dp() copied line for line, but the traceback returns (sign index, letter) so an aliased token is never
    confused with an unaliased token of the same code."""
    n, m = len(cs), len(gs); NEG = -1e9
    S = [[NEG] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]
    inb = lambda i, j: abs(j - i * m / max(n, 1)) <= band
    S[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if (i or j) == 0 or not inb(i, j): continue
            c = []
            if i and j and S[i-1][j-1] > NEG: c.append((S[i-1][j-1] + (1 if ok(cs[i-1], gs[j-1], T) else 0), 'D'))
            if j and S[i][j-1] > NEG: c.append((S[i][j-1] + gap, 'G'))
            if i and S[i-1][j] > NEG: c.append((S[i-1][j] + gap, 'C'))
            if c:
                best = max(v for v, _ in c); S[i][j], B[i][j] = best, next(t for v, t in c if v == best)
    if S[n][m] <= NEG: return []
    i, j, al = n, m, []
    while i or j:
        t = B[i][j]
        if t == 'D': al.append((i - 1, gs[j-1])); i -= 1; j -= 1
        elif t == 'G': j -= 1
        else: i -= 1
    return al[::-1]
out = []; allp = []
allp += run('0702', 'inv373_0702_r13', ['inv373_0693_r10', 'inv373_0730_r13'], 702, out)
allp += run('0730', 'inv373_0730_r13', ['inv373_0693_r10', 'inv373_0702_r13'], 730, out)
allp += run('0758', 'inv373_0758_r14', ['inv373_0693_r10', 'inv373_0702_r13', 'inv373_0730_r13'], 758, out)
open(os.path.join(H, 'alias.out'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
rows_ = ['# R15-SURALIAS aliases that PASSed the PREREG gate (reader-code equivalences inside inv. 373 passes; not key values)',
         'scan\talias\tn_al\tagree\tshare\tC1_p99']
rows_ += [f'{s}\t{a}\t{n}\t{k}\t{sh:.3f}\t{p:.3f}' for s, a, n, k, sh, p in allp]
open(os.path.join(H, 'alias_r15.tsv'), 'w').write('\n'.join(rows_) + '\n')
