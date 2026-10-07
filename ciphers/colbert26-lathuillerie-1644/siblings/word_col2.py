"""DA1-COL2 (account 1, LANE DEFAULT-account-1-20261007-1440, 7 Oct 2026): RE-SCORE of word_da1.py on the second blind pairing pass.
Byte-for-byte the statistic, Control W, seed, gate and power rule of siblings/word_da1.py (pre-registered by DA1-COL, eff0df6fd); only
three paths change: (1) pairs from siblings/word_pairs_col2.tsv (DA1-COL2's blind pass, made without reading word_pairs_da1.tsv);
(2) the key snapshot siblings/key_f23_preDA1COL.tsv = key_f23.tsv at eff0df6fd, i.e. BEFORE DA1-COL merged six codes at C, so the
C positive-control set and the 26 test codes are exactly DA1-COL's (with the current key_f23 the 26-vs-C disjointness assert fails);
(3) PASS codes go to siblings/key_f23_word_col2.tsv, not the key. Pre-registration: PREREG-DA1-COL2.md. Original docstring follows.
DA1-COL (account 1, LANE DEFAULT-account-1-20261007-1440, 7 Oct 2026): WORD-LEVEL positional test of the open f.23 codes on
c50, c3940 and c47. Pre-registered: this file is committed and pushed BEFORE the word pairings are read back or scored (rule 3);
nothing below the docstring is changed after the first run except a bug fix that is logged in NOTES.md with the before/after output.

Why: D22-COL26P scored the 26 single-valued key_f23_anchor_r10 hypotheses with a positional statistic on spans between key_f23 C
anchors (1-3 codes, up to 12 letters) and got 0 PASS (15 FAIL, 11 UNDERPOWERED). The Verdict line's next step is to shrink each span to
one gloss WORD by a by-eye pairing of gloss words to the numeral groups beneath them on the native crops of the three best-attested units.

Pairing data (input, produced blind): siblings/word_pairs_da1.tsv -- one row per gloss word: line, word, first, last (inclusive group
  indices into the row's tokens in the committed c5051/c3940/c4749 *_reconciled.tsv), conf, note. Made by one Sonnet pass per unit on
  the line crops cut with the commands recorded in NOTES.md (A2-COL13, A2-COL14, A2-COL15), judging horizontal position only; the
  passes were not shown any key. Reconciliation is mechanical only (index ranges inside the row, non-overlapping, in order); no
  boundary is moved by key knowledge.
Units: c50 (lines 50a*, 50b*), c3940 (39L*, 40L*, 40R*), c47 (47L*). Canvas 51 and the other cleared units are not paired here.

Word spans. A word span = (unit, word text t = norm(word), codes c_0..c_{k-1} = the digit-only groups in [first, last]); a span with
  k = 0 or an empty t is dropped. Unsettled groups ("9?", "3?", "?2", "13/15") are skipped (not codes) but keep their slot for k.
Positional statistic (word grain). Code c_j in a span of k slots and L letters is predicted at offset o_j = round(j * L / k). A
  span-occurrence of code c with hypothesised value v is a HIT iff v occurs in t starting at s in {o_j-1, o_j, o_j+1} with 0 <= s and
  s + len(v) <= L (not circular). H(c) = hits summed over every span-occurrence of c.
Control W (pairing shuffle; can differ from the target on this statistic): within each unit, the word texts are permuted uniformly
  at random over that unit's spans (codes, slots and span order fixed; only which word sits over which group run changes). It keeps
  each unit's words and code runs and breaks only the pairing -- the axis this job measured. 10000 draws, seed 20261007 + 1440.
Codes tested (fixed now): the 26 single-valued rows of key_f23_anchor_r10.tsv (D22-COL26P's set: 11 e, 15 e, 16 se, 20 i, 21 t,
  27 u, 29 r, 30 s, 31 t, 32 u, 39 e, 46 ce, 47 e, 54 e, 61 e, 67 leur, 70 e, 71 e, 75 la, 76 e, 77 l, 81 me, 83 mo, 85 na, 86 e,
  96 que). Bonferroni alpha = 0.05/26 = 0.00192.
Instrument check (positive control, per unit -- the Szembek per-unit lesson). The key_f23 C codes as committed (code -> value) are
  scored with the same statistic and Control W, pooled over C codes, separately in each unit. A unit CLEARS iff its C-code H > p95
  and P(ctrl >= real) < 0.05. Only cleared units are scored for the 26 test codes. If no unit clears, the run stops: NON-TEST.
Power. P_min = P(ctrl >= N occurrences) >= alpha => UNDERPOWERED. Also the positive control subsampled to each test code's own N
  (1000 random subsets of the pooled C-code occurrences in cleared units, P against the same control draws restricted to the subset):
  power = share of subsets with P < alpha. A FAIL with power < 0.5 is reported as FAIL-LOWPOWER (untestable at this N, not a negative).
GATE per test code: PASS iff H > p95 (Control W) AND P < 0.00192 AND its hits come from >= 2 cleared units. Else FAIL / UNDERPOWERED
  / FAIL-LOWPOWER as above.
Merge rule (registered now): a PASS code is written to key_f23_word_da1.tsv at grade C (its value comes from the period gloss, paired
  word by word, with the pairing-shuffle control passed); this script does not edit key_f23.tsv -- the worker merges a PASS code into
  key_f23.tsv only if it passed here, and regenerates the reading with tools/decode_key.py. No PASS -> no key change.
Leads (reported, not gated): every word span with k = 1 among the open codes (not key_f23 C), listed as code -> word.
Output: siblings/word_da1_out.txt (stdout). Usage: python3 siblings/word_da1.py
"""
import csv, os, re, collections
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
key = {r['code']: (norm(r['value']), r['grade']) for r in csv.DictReader(open(f'{H}/key_f23_preDA1COL.tsv'), delimiter='\t')}
C = {c: v for c, (v, g) in key.items() if g == 'C' and v}
HYP = {r['code']: norm(r['value']) for r in csv.DictReader(open(f'{T}/key_f23_anchor_r10.tsv'), delimiter='\t') if '|' not in r['value']}
assert len(HYP) == 26 and not (set(HYP) & set(C))
ALPHA = 0.05 / len(HYP)
toks = {}
for fn in ('c5051', 'c3940', 'c4749'):
    for r in csv.DictReader(open(f'{H}/{fn}_reconciled.tsv'), delimiter='\t'): toks[r['line']] = r['tokens'].split()
def unit_of(L): return 'c50' if L.startswith('50') else 'c3940' if L[:2] in ('39', '40') else 'c47' if L.startswith('47') else None
spans = collections.defaultdict(list)  # unit -> [(word, [(slot, code)], k)]
last = {}
for r in csv.DictReader(open(f'{H}/word_pairs_col2.tsv'), delimiter='\t'):
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
print('DA1-COL word-level positional test; units', {u: len(spans[u]) for u in sorted(spans)}, 'word spans')
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
    res[c] = v
    print(f'{c}\t{HYP[c]}\t{N}\t{hr}\t{ctrl.mean():.2f}\t{p95:.0f}\t{ctrl.max()}\t{P:.4f}\t{Pmin:.4f}\t{",".join(sorted(uh)) or "-"}\t{pw:.3f}\t{v}')
print('summary:', dict(collections.Counter(res.values())))
passed = [c for c, v in res.items() if v == 'PASS']
with open(f'{H}/key_f23_word_col2.tsv', 'w') as f:
    f.write('code\tvalue\tgrade\tsource\tnote\n')
    for c in sorted(passed, key=int):
        f.write(f'{c}\t{HYP[c]}\tC\tDA1-COL word-level pairing c50/c3940/c47, siblings/word_da1.py\tPASS vs pairing-shuffle control\n')
print('PASS codes written to siblings/key_f23_word_col2.tsv:', passed or 'none')
print('leads (not gated): k = 1 word spans of open codes (not key_f23 C)')
lead = collections.defaultdict(list)
for u in sorted(spans):
    for t, cs, k in spans[u]:
        if k == 1 and cs[0][1] not in C: lead[cs[0][1]].append(f'{t}({u})')
for c in sorted(lead, key=int): print(f'  {c}\t{"; ".join(lead[c])}')
