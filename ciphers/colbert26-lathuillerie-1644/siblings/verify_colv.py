"""DA1-COLV verifier check (7 Oct 2026), registered in PREREG-DA1-COLV.md before it was run. Splits the word-grain positional hits of
the codes moved to key_f23 C today into canvases inside (IN) and outside (OUT) the R10-COL26B value-choice units (key_f23_anchor_r10
`units=`), with word_da1.py's statistic, hit rule, Control W and instrument check unchanged. Demotion-only check.
Usage: python3 siblings/verify_colv.py [--pairs1 word_pairs_da1.tsv]   (--pairs1 word_pairs_col2.tsv reports DA1-COL2's reader)
"""
import csv, os, re, sys, collections
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
P1 = sys.argv[sys.argv.index('--pairs1') + 1] if '--pairs1' in sys.argv else 'word_pairs_da1.tsv'
key = {r['code']: (norm(r['value']), r['grade']) for r in csv.DictReader(open(f'{H}/key_f23_preDA1COL.tsv'), delimiter='\t')}
C = {c: v for c, (v, g) in key.items() if g == 'C' and v}
A10 = {}; UNITS = {}
for r in csv.DictReader(open(f'{T}/key_f23_anchor_r10.tsv'), delimiter='\t'):
    if '|' in r['value']: continue
    A10[r['code']] = norm(r['value'])
    m = re.search(r'\(([^)]*)\)', r['note']); UNITS[r['code']] = set(m.group(1).split(',')) if m else set()
CODES = '16 20 67 81 96 30 85'.split(); ALPHA = 0.05 / len(CODES)
HYP = {c: A10[c] for c in CODES}
toks = {}
for fn in ('c5051', 'c3940', 'c4749'):
    for r in csv.DictReader(open(f'{H}/{fn}_reconciled.tsv'), delimiter='\t'): toks[r['line']] = r['tokens'].split()
for fn in ('c5456', 'c6263'):
    for r in csv.DictReader(open(f'{H}/{fn}_reconciled.tsv'), delimiter='\t'): toks[r['line']] = [x for x in r['tokens'].split() if x != '|']
def unit_of(L):
    p = L[:2]
    return 'c50' if p == '50' else 'c3940' if p in ('39', '40') else 'c47' if p == '47' else ('c' + p if p in ('54', '55', '56', '62', '63') else None)
spans = collections.defaultdict(list)
for fn in (P1, 'word_pairs_col3.tsv'):
    last = {}
    for r in csv.DictReader(open(f'{H}/{fn}'), delimiter='\t'):
        L = r['line']; u = unit_of(L); a, b = int(r['first']), int(r['last']); tk = toks[L]
        assert u and 0 <= a <= b < len(tk), r
        assert a > last.get(L, -1), ('overlap/order', r); last[L] = b
        t = norm(r['word']); g = tk[a:b + 1]
        cs = [(j, c) for j, c in enumerate(g) if c.isdigit()]
        if t and cs: spans[u].append((t, cs, len(g)))
def hit(t, j, k, v):
    L = len(t); o = round(j * L / k)
    return any(0 <= s and s + len(v) <= L and t[s:s + len(v)] == v for s in (o - 1, o, o + 1))
rng = np.random.default_rng(20261007 + 1440); D = 10000
perms = {u: np.array([rng.permutation(len(spans[u])) for _ in range(D)]) for u in sorted(spans)}
def occs(u, want): return [(c, j, k, i) for i, (t, cs, k) in enumerate(spans[u]) for j, c in cs if c in want]
def matrix(u, oc, val):
    W = [s[0] for s in spans[u]]
    real = np.array([hit(W[i], j, k, val[c]) for c, j, k, i in oc], dtype=bool)
    P = perms[u]
    M = np.array([[hit(W[P[d][i]], j, k, val[c]) for c, j, k, i in oc] for d in range(D)], dtype=bool) if oc else np.zeros((D, 0), bool)
    return real, M
print(f'DA1-COLV value-independence split; pairs {P1} + word_pairs_col3.tsv; spans', {u: len(spans[u]) for u in sorted(spans)})
cleared = []
for u in sorted(spans):
    oc = occs(u, C); real, M = matrix(u, oc, C); ctrl = M.sum(1); p95 = np.percentile(ctrl, 95); P = (ctrl >= real.sum()).mean()
    ok = real.sum() > p95 and P < 0.05; cleared += [u] if ok else []
    print(f'instrument {u}: H {real.sum()}/{len(oc)} p95 {p95:.0f} P {P:.4f} -> {"CLEARS" if ok else "FAILS"}')
print('code\tvalue\tR10_units\tside\tN\tH\tctrl_mean\tp95\tP\tper_canvas\tverdict(b)')
for c in CODES:
    for side in ('IN', 'OUT'):
        us = [u for u in cleared if (u in UNITS[c]) == (side == 'IN')]
        R = []; Ms = []; per = []
        for u in us:
            oc = occs(u, {c})
            if not oc: continue
            real, M = matrix(u, oc, HYP); R.append(real); Ms.append(M); per.append(f'{u}:{real.sum()}/{len(real)}')
        if not R: print(f'{c}\t{HYP[c]}\t{",".join(sorted(UNITS[c]))}\t{side}\t0\t-\t-\t-\t-\t-\t{"-" if side == "IN" else "OUT<3 -> M"}'); continue
        real = np.concatenate(R); M = np.concatenate(Ms, axis=1); ctrl = M.sum(1); p95 = np.percentile(ctrl, 95); P = (ctrl >= real.sum()).mean()
        v = '-' if side == 'IN' else ('OUT<3 -> M' if len(real) < 3 else ('keep C' if real.sum() > p95 and P < ALPHA else 'FAIL -> M'))
        print(f'{c}\t{HYP[c]}\t{",".join(sorted(UNITS[c]))}\t{side}\t{len(real)}\t{real.sum()}\t{ctrl.mean():.2f}\t{p95:.0f}\t{P:.4f}\t{" ".join(per)}\t{v}')
print('k = 1 spans where the code alone covers a word without its value (reported, not gated):')
for c in CODES:
    bad = [f'{t}({u})' for u in sorted(spans) for t, cs, k in spans[u] if k == 1 and cs[0][1] == c and HYP[c] not in t]
    good = sum(1 for u in spans for t, cs, k in spans[u] if k == 1 and cs[0][1] == c and HYP[c] in t)
    print(f'  {c} {HYP[c]}: contains {good}; not {len(bad)}: {"; ".join(bad)}')
