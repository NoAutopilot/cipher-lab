"""DA1-COL3 (account 1, LANE DEFAULT-account-1-20261007-1440, 7 Oct 2026): HELD-OUT word-level positional test on c54, c55, c56,
c62, c63. Pre-registered with PREREG-DA1-COL3.md; this file is committed and pushed BEFORE the word pairing of these canvases exists.
Statistic, Control W (within-unit permutation of gloss words over word spans, 10000 draws, seed 20261007 + 1440), instrument check per
unit, power rule (P_min and positive control subsampled to N) and the >= 2 cleared-units rule are word_da1.py's, unchanged. Changes:
(1) units are the five canvases c54, c55, c56, c62, c63 (lines 54a*, 55a*/55b*, 56a*, 62a*, 63a*); tokens from c5456_reconciled.tsv and
    c6263_reconciled.tsv with the gap marks "|" removed before indexing (they are not groups); "36(4)" is non-digit, skipped as unsettled;
    rows with no gloss (54a03, 55a06, 62a04) and the struck-gloss row 63a06 are not paired;
(2) pairs from siblings/word_pairs_col3.tsv (one blind Sonnet pass per canvas, no key shown);
(3) positive-control C set from the pre-DA1-COL snapshot siblings/key_f23_preDA1COL.tsv (so no code under test or report is in it);
(4) TEST codes (gated, Bonferroni 0.05/15 = 0.00333): DA1-COL's FAIL-LOWPOWER set 15 e, 21 t, 29 r, 32 u, 39 e, 54 e, 75 la, 76 e,
    77 l, 83 mo, 85 na, 86 e, plus 30 s, 31 t, 46 ce; REPORT codes (scored the same way, reported, never gated, never demoted):
    16 se, 20 i, 67 leur, 81 me, 96 que. Values from key_f23_anchor_r10.tsv;
(5) PASS codes go to siblings/key_f23_word_col3.tsv; the worker applies PREREG-DA1-COL3.md's merge rule to key_f23.tsv.
Output: siblings/word_col3_out.txt. Usage: python3 siblings/word_col3.py
"""
import csv, os, re, collections
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
key = {r['code']: (norm(r['value']), r['grade']) for r in csv.DictReader(open(f'{H}/key_f23_preDA1COL.tsv'), delimiter='\t')}
C = {c: v for c, (v, g) in key.items() if g == 'C' and v}
A10 = {r['code']: norm(r['value']) for r in csv.DictReader(open(f'{T}/key_f23_anchor_r10.tsv'), delimiter='\t') if '|' not in r['value']}
TEST = '15 21 29 32 39 54 75 76 77 83 85 86 30 31 46'.split(); REPORT = '16 20 67 81 96'.split()
HYP = {c: A10[c] for c in TEST + REPORT}
assert len(TEST) == 15 and not (set(HYP) & set(C))
ALPHA = 0.05 / len(TEST)
toks = {}
for fn in ('c5456', 'c6263'):
    for r in csv.DictReader(open(f'{H}/{fn}_reconciled.tsv'), delimiter='\t'): toks[r['line']] = [x for x in r['tokens'].split() if x != '|']
def unit_of(L): return 'c' + L[:2] if L[:2] in ('54', '55', '56', '62', '63') else None
spans = collections.defaultdict(list)  # unit -> [(word, [(slot, code)], k)]
last = {}
for r in csv.DictReader(open(f'{H}/word_pairs_col3.tsv'), delimiter='\t'):
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
# occurrence table per unit: list of (code, slot, k, span index)
def occs(u, want):
    return [(c, j, k, i) for i, (t, cs, k) in enumerate(spans[u]) for j, c in cs if c in want]
perms = {u: np.array([rng.permutation(len(spans[u])) for _ in range(D)]) for u in spans}
def matrix(u, oc, val):  # returns real hit vector and D x n control hit matrix
    W = [s[0] for s in spans[u]]
    real = np.array([hit(W[i], j, k, val[c]) for c, j, k, i in oc], dtype=bool)
    cache = {}
    def h(w, j, k, c):
        key_ = (w, j, k, c)
        if key_ not in cache: cache[key_] = hit(W[w], j, k, val[c])
        return cache[key_]
    P = perms[u]
    M = np.array([[h(P[d][i], j, k, c) for c, j, k, i in oc] for d in range(D)], dtype=bool) if oc else np.zeros((D, 0), bool)
    return real, M
print('DA1-COL3 held-out word-level positional test; units', {u: len(spans[u]) for u in sorted(spans)}, 'word spans')
print(f'k distribution: {collections.Counter(len(cs) for u in spans for _, cs, _ in spans[u]).most_common()}')
cleared = []; posC = {}
for u in sorted(spans):
    oc = occs(u, C); real, M = matrix(u, oc, C); hr = real.sum(); ctrl = M.sum(1)
    p95 = np.percentile(ctrl, 95); P = (ctrl >= hr).mean()
    ok = hr > p95 and P < 0.05
    print(f'instrument {u}: C-code occ {len(oc)} H {hr} ctrl mean {ctrl.mean():.2f} p95 {p95:.0f} max {ctrl.max()} P {P:.4f} -> {"CLEARS" if ok else "FAILS"}')
    if ok: cleared.append(u); posC[u] = (real, M)
if not cleared:
    print('NON-TEST: no unit clears its own positive control; no test code scored.'); raise SystemExit(0)
PR = np.concatenate([posC[u][0] for u in cleared]); PM = np.concatenate([posC[u][1] for u in cleared], axis=1)
print('code\tvalue\tN\tH\tctrl_mean\tp95\tmax\tP\tP_min\tunits_hit\tpower_at_N\tverdict')
res = {}
for c in sorted(HYP, key=int):
    R = []; Ms = []; uh = set()
    for u in cleared:
        oc = occs(u, {c}); real, M = matrix(u, oc, HYP)
        R.append(real); Ms.append(M)
        if real.any(): uh.add(u)
    real = np.concatenate(R); M = np.concatenate(Ms, axis=1); N = len(real)
    if N == 0:
        print(f'{c}\t{HYP[c]}\t0\t-\t-\t-\t-\t-\t-\t-\t-\tNO-OCCURRENCE'); continue
    hr = real.sum(); ctrl = M.sum(1); p95 = np.percentile(ctrl, 95); P = (ctrl >= hr).mean(); Pmin = (ctrl >= N).mean()
    sub_ok = 0
    for _ in range(1000):
        idx = rng.choice(len(PR), size=min(N, len(PR)), replace=False)
        sub_ok += (PM[:, idx].sum(1) >= PR[idx].sum()).mean() < ALPHA
    pw = sub_ok / 1000
    if Pmin >= ALPHA: v = 'UNDERPOWERED'
    elif hr > p95 and P < ALPHA and len(uh) >= 2: v = 'PASS'
    else: v = 'FAIL-LOWPOWER' if pw < 0.5 else 'FAIL'
    if c in REPORT: v = 'REPORT:' + v
    res[c] = v
    print(f'{c}\t{HYP[c]}\t{N}\t{hr}\t{ctrl.mean():.2f}\t{p95:.0f}\t{ctrl.max()}\t{P:.4f}\t{Pmin:.4f}\t{",".join(sorted(uh)) or "-"}\t{pw:.3f}\t{v}')
print('summary:', dict(collections.Counter(res.values())))
passed = [c for c, v in res.items() if v == 'PASS']
with open(f'{H}/key_f23_word_col3.tsv', 'w') as f:
    f.write('code\tvalue\tgrade\tsource\tnote\n')
    for c in sorted(passed, key=int):
        f.write(f'{c}\t{HYP[c]}\tC\tDA1-COL3 held-out word-level pairing c54/c55/c56/c62/c63, siblings/word_col3.py\tPASS vs pairing-shuffle control\n')
print('PASS codes written to siblings/key_f23_word_col3.tsv:', passed or 'none')
print('leads (not gated): k = 1 word spans of open codes (not key_f23 C)')
lead = collections.defaultdict(list)
for u in sorted(spans):
    for t, cs, k in spans[u]:
        if k == 1 and cs[0][1] not in C: lead[cs[0][1]].append(f'{t}({u})')
for c in sorted(lead, key=int): print(f'  {c}\t{"; ".join(lead[c])}')
