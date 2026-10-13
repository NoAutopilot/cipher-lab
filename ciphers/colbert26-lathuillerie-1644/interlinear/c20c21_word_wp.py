"""COL26-WP (account 1, LANE DEFAULT-A1-1840, 13 Oct 2026): word-level pairing test of the canvas 20-21 leads 42 = si, 11 = le,
6 = je. Pre-registered with PREREG-COL26-WP.md: this file is pushed BEFORE stage 0 is run and before any pairing exists; nothing below
the docstring changes after the first run except a logged bug fix.

Material: interlinear/c20c21_reconciled.tsv (A4-RFCOL, 18 units; tokens as committed; gloss words = gloss_text split on spaces after
removing '[?]' / '[...]'). Units are the 18 reconciled rows (c20U01 ... c21U07).
Values (fixed now): 42 -> si, 11 -> le (a hit also on 'les' since 'le' starts it), 6 -> ie (je; j -> i, v -> u as word_da1.norm).
Known answers (positive control, not tested): 83 -> de, 31 -> que (key_f24 C, built from f.24 alone; A4-RFCOL known-answer 14/19).

Selection correction (the leads were picked by eye from this same leaf, so the test is in-sample on value choice): alpha = 0.05 / m,
  m = number of distinct codes occurring >= 2 times in the 18 units that are not grade C in key_period.tsv (the pool the leads were
  drawn from). Also printed at 0.05/3 for comparison, NOT gating.

STAGE 0 -- power bound BEFORE any pairing (decides whether vision is spent on a code). Idealised pairing: every occurrence of the code
  in a unit whose gloss holds a word w with v starting at offset 0 or 1 is assumed paired alone (k = 1) on w -> a hit; under Control W
  that occurrence hits with probability p = (# gloss words of the unit with v at offset 0 or 1) / (# gloss words). Occurrences in units
  with no such word are misses with p = 0. P_min = P(sum Bernoulli(p_i) >= H_ideal), exact by convolution. P_min >= alpha => the code is
  NON-TEST at this N: no pairing is read for it and it is not scored. The same bound is printed for the positive control 83+31.
  If all three codes are NON-TEST, the job stops here (no vision).

STAGE 1 -- only for codes that pass stage 0. Pairing data interlinear/c20c21_word_pairs.tsv (unit, word, first, last, conf), one
  blind Sonnet pass per canvas on line crops, no key shown, horizontal position only; reconciliation mechanical (in-row, ordered,
  non-overlapping). Statistic as siblings/word_da1.py: code c_j in a span of k slots and L letters predicted at o_j = round(j*L/k);
  HIT iff v starts in t at s in {o_j-1, o_j, o_j+1}, 0 <= s, s+len(v) <= L. Control W: within each unit the word texts permuted over
  the unit's spans (10000 draws, seed 20261013+1840). Instrument check: 83 de + 31 que pooled over the 18 units, H > p95 and P < 0.05,
  else NON-TEST (stop). Power: the positive-control occurrences (tested code masked -- it is never 83 or 31) subsampled to the code's
  N, 1000 subsets, power = share with P < alpha. GATE: PASS iff H > p95 and P < alpha; FAIL with power < 0.5 = FAIL-LOWPOWER.
Merge rule: no key file is edited by this script. A PASS goes to key_period.tsv only through tools/decode_key.py --try, grade M unless
  --try's own control passed for that value class.
Usage: python3 interlinear/c20c21_word_wp.py --stage 0|1
"""
import csv, os, re, sys, collections
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
TEST = {'42': 'si', '11': 'le', '6': 'ie'}; POS = {'83': 'de', '31': 'que'}
units = []
for r in csv.DictReader(open(f'{H}/c20c21_reconciled.tsv'), delimiter='\t'):
    words = [norm(w) for w in re.sub(r'\[[^\]]*\]', ' ', r['gloss_text']).split()]
    units.append((r['unit'], r['cipher_tokens'].split(), [w for w in words if w]))
grade = {r['code']: r['grade'] for r in csv.DictReader(open(f'{T}/key_period.tsv'), delimiter='\t')}
cnt = collections.Counter(t for _, tk, _ in units for t in tk)
pool = sorted(c for c, n in cnt.items() if n >= 2 and grade.get(c, 'M') != 'C' and c not in POS)
m = len(pool); ALPHA = 0.05 / m
print(f'pool m={m} (codes N>=2 on c20-21, not C): {" ".join(pool)}'); print(f'alpha = 0.05/{m} = {ALPHA:.5f}; comparison 0.05/3 = 0.01667 (not gating)')
def hits_at(w, v): return any(w.startswith(v, s) for s in (0, 1))
def stage0(code, v):
    ps, hmax = [], 0
    for u, tk, ws in units:
        for t in tk:
            if t != code: continue
            good = sum(hits_at(w, v) for w in ws)
            if good: hmax += 1; ps.append(good / len(ws))
            else: ps.append(0.0)
    dist = np.array([1.0])
    for p in ps: dist = np.convolve(dist, [1 - p, p])
    return len(ps), hmax, float(dist[hmax:].sum()) if hmax else 1.0, ps
stage = sys.argv[sys.argv.index('--stage') + 1] if '--stage' in sys.argv else '0'
print('STAGE 0 (idealised pairing bound)'); print('code\tvalue\tN\tH_ideal\tP_min\tverdict')
live = []
for code, v in list(POS.items()) + list(TEST.items()):
    n, h, pmin, ps = stage0(code, v)
    if code in POS: verdict = 'positive-control'
    else:
        verdict = 'NON-TEST' if pmin >= ALPHA else 'live'
        if verdict == 'live': live.append(code)
    print(f'{code}\t{v}\t{n}\t{h}\t{pmin:.5f}\t{verdict}\t(p_i {" ".join(f"{p:.2f}" for p in ps)})')
if not live: print('STAGE 0 VERDICT: all three codes NON-TEST at this N; no pairing read, no score (stop).'); sys.exit(0)
print(f'STAGE 0 VERDICT: live codes {live}')
if stage != '1': sys.exit(0)
# ---- stage 1 ----
rng = np.random.default_rng(20261013 + 1840)
spans = collections.defaultdict(list)
toks = {u: tk for u, tk, _ in units}
last = {}
for r in csv.DictReader(open(f'{H}/c20c21_word_pairs.tsv'), delimiter='\t'):
    u = r['unit']; a, b = int(r['first']), int(r['last']); tk = toks[u]
    assert 0 <= a <= b < len(tk) and a > last.get(u, -1), r; last[u] = b
    t = norm(r['word'])
    if t: spans[u].append((t, tk[a:b + 1]))
def score(assign, codes):  # assign: unit -> list of words over spans
    occ = []
    for u, sp in spans.items():
        for (t0, g), t in zip(sp, assign[u]):
            k, L = len(g), len(t)
            for j, c in enumerate(g):
                if c in codes:
                    v = codes[c]; o = round(j * L / k)
                    occ.append(any(0 <= s and s + len(v) <= L and t.startswith(v, s) for s in (o - 1, o, o + 1)))
    return occ
real = {u: [t for t, _ in sp] for u, sp in spans.items()}
D = 10000
def draws():
    for _ in range(D):
        yield {u: list(rng.permutation(w)) for u, w in real.items()}
ctl = list(draws())
def test(codes, alpha):
    r = np.array(score(real, codes)); cm = np.array([score(a, codes) for a in ctl])
    Hh = int(r.sum()); cs = cm.sum(1)
    return r, cm, Hh, cs.mean(), np.percentile(cs, 95), cs.max(), float((cs >= Hh).mean())
r, cm, Hh, mu, p95, mx, P = test(POS, 0.05)
inst = Hh > p95 and P < 0.05
print(f'INSTRUMENT 83 de + 31 que: N {len(r)} H {Hh} ctrl mean {mu:.2f} p95 {p95:.0f} max {mx} P {P:.4f} -> {"CLEARS" if inst else "NON-TEST"}')
if not inst: sys.exit(0)
print('code\tvalue\tN\tH\tctrl_mean\tp95\tmax\tP\tpower_at_N\tverdict')
for c in live:
    rr, cc, Hh, mu, p95, mx, P = test({c: TEST[c]}, ALPHA)
    n = len(rr); pw = 0
    if n:
        for _ in range(1000):
            idx = rng.choice(len(r), size=min(n, len(r)), replace=False)
            hs = r[idx].sum(); cs = cm[:, idx].sum(1)
            pw += (cs >= hs).mean() < ALPHA
        pw /= 1000
    v = 'PASS' if (Hh > p95 and P < ALPHA) else ('FAIL-LOWPOWER' if pw < 0.5 else 'FAIL')
    print(f'{c}\t{TEST[c]}\t{n}\t{Hh}\t{mu:.2f}\t{p95:.0f}\t{mx}\t{P:.4f}\t{pw:.3f}\t{v}')
