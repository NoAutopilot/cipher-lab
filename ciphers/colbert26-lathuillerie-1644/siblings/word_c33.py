"""COL26-C33 (account 2, LANE DEFAULT-A2-0911-14, 14 Oct 2026): word-grain test of 20 = i on canvas 33 (held out from every value
choice for 20; D2-COL26's line-grain test missed its gate narrowly, P 0.0093 vs 0.0083). Pre-registered with PREREG-COL26-C33.md: this
file is pushed BEFORE stage 0 is run and before any pairing exists; nothing below the docstring changes after the first run except a
logged bug fix.

Material: siblings/c33_reconciled.tsv (A2-COL10; 9 rows T1-T4, B1-B5; tokens and gloss as committed). One unit, c33 (all 9 rows).
Statistic, hit rule, Control W and power rule are siblings/word_col3.py's (word_da1.py's), unchanged: code c_j in a span of k slots and
  L letters predicted at o_j = round(j*L/k); HIT iff v starts at s in {o_j-1, o_j, o_j+1}, 0 <= s, s+len(v) <= L. Control W: the word
  texts permuted over the unit's word spans, 10000 draws, seed 20261014 + 911.
Positive control (instrument check): the C codes of siblings/key_f23_preDA1COL.tsv (the snapshot DA1-COL3 used; 20 is M there).
TEST: 20 -> i only. alpha = 0.05/6 = 0.00833 (D2-COL26's family gate, carried over unchanged). The >= 2 units rule of word_col3.py is
  dropped: there is one unit.

STAGE 0 -- power bound BEFORE any pairing (COL26-WP's rule): each occurrence of 20 in c33 is assumed paired alone (k = 1) on a gloss word
  with 'i' at offset 0 or 1 if the unit has one -> a hit; under Control W it hits with p = (# such words)/(# words in the unit).
  P_min = P(sum Bernoulli(p_i) >= H_ideal), exact. P_min >= alpha => NON-TEST, stop, no vision.
STAGE 1 -- pairing files siblings/word_pairs_c33_p1.tsv and _p2.tsv (two blind Sonnet passes on line crops, no key, no other pass's
  spans, horizontal position only); reconciliation mechanical (in-row, ordered, non-overlapping; offending row dropped). Each pass scored
  separately. Instrument check per pass: positive-control occurrences H > p95 and P < 0.05. If EITHER pass fails its instrument check
  -> NON-TEST for 20 at this N (third failure of the word-pairing instrument check in this folder -> the instrument is retired for the
  folder, rule 3). Else 20 = i PASS iff on BOTH passes H > p95 and P < alpha; else FAIL (FAIL-LOWPOWER if power at N < 0.5 on either).
  Diagnostic only, not gating: the pool of spans both passes agree on exactly, and reader agreement.
Merge rule: this script edits no key file; a PASS is applied only via tools/decode_key.py --try, by the worker.
Usage: python3 siblings/word_c33.py --stage 0|1
"""
import csv, os, re, sys, collections
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
key = {r['code']: (norm(r['value']), r['grade']) for r in csv.DictReader(open(f'{H}/key_f23_preDA1COL.tsv'), delimiter='\t')}
C = {c: v for c, (v, g) in key.items() if g == 'C' and v}
TEST = {'20': 'i'}; assert not (set(TEST) & set(C))
ALPHA = 0.05 / 6
rows = list(csv.DictReader(open(f'{H}/c33_reconciled.tsv'), delimiter='\t'))
toks = {r['line']: r['tokens'].split() for r in rows}
gwords = [w for r in rows for w in (norm(x) for x in r['gloss'].split()) if w]
print(f'COL26-C33 word-grain test, unit c33: {len(rows)} rows, {sum(map(len, toks.values()))} groups, {len(gwords)} gloss words')
print(f'positive-control C codes: {" ".join(sorted(C, key=int))}; alpha = 0.05/6 = {ALPHA:.5f}')
def hits_at(w, v): return any(w.startswith(v, s) for s in (0, 1))
def stage0(code, v):
    good = sum(hits_at(w, v) for w in gwords); p = good / len(gwords)
    n = sum(t == code for tk in toks.values() for t in tk)
    hmax = n if good else 0; ps = [p if good else 0.0] * n
    dist = np.array([1.0])
    for q in ps: dist = np.convolve(dist, [1 - q, q])
    return n, hmax, (float(dist[hmax:].sum()) if hmax else 1.0), good
stage = sys.argv[sys.argv.index('--stage') + 1] if '--stage' in sys.argv else '0'
print('STAGE 0 (idealised pairing bound)'); print('code\tvalue\tN\tH_ideal\twords_ok\tP_min\tverdict')
n, hmax, pmin, good = stage0('20', 'i')
v0 = 'NON-TEST' if pmin >= ALPHA or n == 0 else 'live'
print(f'20\ti\t{n}\t{hmax}\t{good}/{len(gwords)}\t{pmin:.5f}\t{v0}')
if v0 != 'live' or stage == '0':
    if v0 != 'live': print('NON-TEST at stage 0: stop, no vision.')
    raise SystemExit(0)
rng = np.random.default_rng(20261014 + 911); D = 10000
def load(fn):
    spans, last, dropped = [], {}, 0
    for r in csv.DictReader(open(f'{H}/{fn}'), delimiter='\t'):
        L = r['line']; a, b = int(r['first']), int(r['last']); tk = toks.get(L)
        if tk is None or not (0 <= a <= b < len(tk)) or a <= last.get(L, -1): dropped += 1; continue
        last[L] = b; t = norm(r['word']); g = tk[a:b + 1]
        cs = [(j, c) for j, c in enumerate(g) if c.isdigit()]
        if t and cs: spans.append((t, cs, len(g), L, a, b))
    return spans, dropped
def hit(t, j, k, v):
    L = len(t); o = round(j * L / k)
    return any(0 <= s and s + len(v) <= L and t[s:s + len(v)] == v for s in (o - 1, o, o + 1))
def score(spans, want, val, perms):
    W = [s[0] for s in spans]
    oc = [(c, j, k, i) for i, (t, cs, k, *_) in enumerate(spans) for j, c in cs if c in want]
    real = np.array([hit(W[i], j, k, val[c]) for c, j, k, i in oc], dtype=bool)
    M = np.array([[hit(W[p[i]], j, k, val[c]) for c, j, k, i in oc] for p in perms], dtype=bool) if oc else np.zeros((D, 0), bool)
    return real, M
out = {}
for tag, fn in (('p1', 'word_pairs_c33_p1.tsv'), ('p2', 'word_pairs_c33_p2.tsv')):
    spans, dropped = load(fn)
    perms = [rng.permutation(len(spans)) for _ in range(D)]
    PR, PM = score(spans, C, C, perms); hr = PR.sum(); ctrl = PM.sum(1); p95 = np.percentile(ctrl, 95); P = (ctrl >= hr).mean()
    ok = hr > p95 and P < 0.05
    print(f'{tag}: {len(spans)} word spans ({dropped} rows dropped); instrument C-code occ {len(PR)} H {hr} ctrl mean {ctrl.mean():.2f} '
          f'p95 {p95:.0f} max {ctrl.max()} P {P:.4f} -> {"CLEARS" if ok else "FAILS"}')
    R, M = score(spans, TEST, TEST, perms); N = len(R); h = R.sum(); c2 = M.sum(1)
    p95t = np.percentile(c2, 95) if N else 0; Pt = (c2 >= h).mean() if N else 1.0
    sub = 0
    for _ in range(1000):
        idx = rng.choice(len(PR), size=min(N, len(PR)), replace=False)
        sub += (PM[:, idx].sum(1) >= PR[idx].sum()).mean() < ALPHA
    pw = sub / 1000
    out[tag] = (ok, N, h, Pt, p95t, pw)
    print(f'{tag}: 20 i N {N} H {h} ctrl mean {c2.mean() if N else 0:.2f} p95 {p95t:.0f} P {Pt:.4f} power_at_N {pw:.3f}'
          + ('' if ok else '  (instrument failed: reported only)'))
    print(f'{tag}: 20 spans: ' + '; '.join(f'{t}[{L} {a}-{b}]' for t, cs, k, L, a, b in spans if any(c == "20" for _, c in cs)))
if not all(o[0] for o in out.values()):
    print('VERDICT 20 = i: NON-TEST (instrument check failed on at least one pass)')
elif all(o[2] > o[4] and o[3] < ALPHA for o in out.values()):
    print('VERDICT 20 = i: PASS (both passes)')
else:
    lp = any(o[5] < 0.5 for o in out.values())
    print(f'VERDICT 20 = i: {"FAIL-LOWPOWER" if lp else "FAIL"}')
s1 = {(L, t, a, b) for t, cs, k, L, a, b in load('word_pairs_c33_p1.tsv')[0]}
s2 = {(L, t, a, b) for t, cs, k, L, a, b in load('word_pairs_c33_p2.tsv')[0]}
w1 = {(L, t): (a, b) for L, t, a, b in s1}; w2 = {(L, t): (a, b) for L, t, a, b in s2}
both = set(w1) & set(w2)
ex = sum(w1[x] == w2[x] for x in both); near = sum(abs(w1[x][0] - w2[x][0]) <= 1 and abs(w1[x][1] - w2[x][1]) <= 1 for x in both)
print(f'diagnostic: words placed by both passes {len(both)}, exact span agreement {ex}, within one group each end {near}')
