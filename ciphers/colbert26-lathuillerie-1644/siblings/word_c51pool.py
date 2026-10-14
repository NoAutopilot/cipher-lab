"""COL26-C51 (account 2, LANE DEFAULT-A2-0911-14, 14 Oct 2026): pooled held-out word-grain test of 20 = i over c33 + c51 + c63.
Pre-registered with PREREG-COL26-C51.md; pushed BEFORE stage 0 is run and before any pairing of c51 exists.

Units held out from every value choice for 20: c33 (COL26-C33 pairings, two passes), c51 (to be paired, two passes; 51L01 has no gloss,
so at most 2 of its 3 occurrences of 20 are pairable), c63 (DA1-COL3's single pass, which cleared its instrument check). c62 is EXCLUDED:
its DA1-COL3 pairing failed its own instrument check (8/37 vs p95 8, P 0.052), and a unit whose own control failed is not pooled
(CLAUDE.md rule 3, per-unit gate before a merge); its one 20-span is reported as a sensitivity line only.
Statistic, hit rule, Control W (within-unit permutation of word texts over that unit's spans) and the power rule are word_c33.py's
(word_col3.py's), unchanged; positive control = C codes of key_f23_preDA1COL.tsv; TEST 20 -> i; alpha 0.05/6 = 0.00833 (unchanged).

STAGE 0 (this file's only stage until the gate below is met; uses no hit count of 20):
  N_pool = pairable occurrences of 20 = c33's 20-spans (5, both passes) + c51 occurrences on glossed rows + c63's 20-spans in DA1-COL3.
  Power at N_pool under the registered rule: the positive-control C-code occurrences of the already-paired units (c33 pass 1 and c63;
  repeated with c33 pass 2) form the pool; 1000 subsamples of size N_pool (without replacement, keeping each occurrence's own unit for
  Control W); power = share of subsamples whose control P < alpha (10000 within-unit permutation draws, seed 20261014 + 1051).
  If power < 0.5 on either c33 pass -> "too-short at pooled N=<n>", stop, no vision.
Usage: python3 siblings/word_c51pool.py
"""
import csv, os, re
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
key = {r['code']: (norm(r['value']), r['grade']) for r in csv.DictReader(open(f'{H}/key_f23_preDA1COL.tsv'), delimiter='\t')}
C = {c: v for c, (v, g) in key.items() if g == 'C' and v}
assert '20' not in C
ALPHA = 0.05 / 6; D = 10000; rng = np.random.default_rng(20261014 + 1051)
def hit(t, j, k, v):
    L = len(t); o = round(j * L / k)
    return any(0 <= s and s + len(v) <= L and t[s:s + len(v)] == v for s in (o - 1, o, o + 1))
def load(fn, tokfiles, pref):
    toks = {}
    for f in tokfiles:
        for r in csv.DictReader(open(f'{H}/{f}'), delimiter='\t'): toks[r['line']] = [x for x in r['tokens'].split() if x != '|']
    spans, last = [], {}
    for r in csv.DictReader(open(f'{H}/{fn}'), delimiter='\t'):
        L = r['line']
        if not L.startswith(pref): continue
        a, b = int(r['first']), int(r['last']); tk = toks.get(L)
        if tk is None or not (0 <= a <= b < len(tk)) or a <= last.get(L, -1): continue
        last[L] = b; t = norm(r['word']); g = tk[a:b + 1]
        cs = [(j, c) for j, c in enumerate(g) if c.isdigit()]
        if t and cs: spans.append((t, cs, len(g)))
    return spans
c63 = load('word_pairs_col3.tsv', ['c6263_reconciled.tsv'], '63')
c62 = load('word_pairs_col3.tsv', ['c6263_reconciled.tsv'], '62')
n = lambda sp: sum(c == '20' for _, cs, _ in sp for _, c in cs)
c51rows = [r for r in csv.DictReader(open(f'{H}/c5051_reconciled.tsv'), delimiter='\t') if r['line'].startswith('51')]
n51 = sum(r['tokens'].split().count('20') for r in c51rows if norm(r['gloss']))
res = {}
for tag in ('p1', 'p2'):
    c33 = load(f'word_pairs_c33_{tag}.tsv', ['c33_reconciled.tsv'], '')
    N = n(c33) + n51 + n(c63)
    # positive-control occurrence matrix per unit under Control W
    real, ctrl = [], []
    for sp in (c33, c63):
        W = [s[0] for s in sp]; perms = [rng.permutation(len(sp)) for _ in range(D)]
        oc = [(c, j, k, i) for i, (t, cs, k) in enumerate(sp) for j, c in cs if c in C]
        real += [hit(W[i], j, k, C[c]) for c, j, k, i in oc]
        ctrl.append(np.array([[hit(W[p[i]], j, k, C[c]) for c, j, k, i in oc] for p in perms], dtype=bool))
    R = np.array(real); M = np.concatenate(ctrl, axis=1)
    pw = 0
    for _ in range(1000):
        idx = rng.choice(len(R), size=min(N, len(R)), replace=False)
        pw += (M[:, idx].sum(1) >= R[idx].sum()).mean() < ALPHA
    pw /= 1000; res[tag] = (N, pw)
    print(f'{tag}: N_pool 20 = c33 {n(c33)} + c51 {n51} + c63 {n(c63)} = {N}; positive-control pool {len(R)} occ, hit rate '
          f'{R.mean():.3f} vs ctrl {M.mean():.3f}; power_at_N {pw:.3f}')
print(f'sensitivity (not pooled): c62 20-spans {n(c62)} (instrument failed in DA1-COL3)')
lo = min(p for _, p in res.values()); Np = max(N for N, _ in res.values())
print(f'STAGE 0 VERDICT: {"too-short at pooled N=%d (power %.3f < 0.5): stop, no vision" % (Np, lo) if lo < 0.5 else "live (power %.3f): stage 1 may run" % lo}')
