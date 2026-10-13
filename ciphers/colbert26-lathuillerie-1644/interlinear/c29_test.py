#!/usr/bin/env python3
"""COL26-C29 (account 1, LANE DEFAULT-A1-0640, 13 Oct 2026): canvas 29 (folio 26, extract of a letter of 30 Mar 1646) known-answer
tests. Pre-registered: this file and PREREG-COL26-C29.md are committed and pushed BEFORE the first run; nothing below changes after.
Scripts and disk only.

Input: interlinear/c29_units.tsv (unit, cipher_tokens, gloss_A, gloss_B): one unit per maximal run of cipher signs on one main-hand
line (clear words break a run), cipher_tokens from the reconciliation (interlinear/c29_reconciled.tsv); gloss_A / gloss_B = the text of
every gloss fragment that blind pass A / B attributed to that run (its own gloss_spans, below-side first, above-side when below is
empty), joined by a space; the glosses are NOT reconciled (V-BRANDT rule: scored per blind pass). A unit with no gloss in a pass is
skipped for that pass. Normalisation as interlinear/c20c21_positional_k26.py: NFD, lower case, letters only, '[?]' removed.

Statistic (D07-COL26K's positional statistic, WIN = 0.25): an occurrence of code c with value v at index i in a unit of n tokens is a
HIT iff len(v) <= L (gloss length) and some circular substring g[j:j+len(v)] == v with |(j + len(v)/2)/L - (i + 0.5)/n| <= WIN.

TEST 1 (key_f24 C codes as known answers): codes and values read from key_f24.tsv grade C at run time (16 m, 25 m, 31 que, 51 l,
  83 de, 92 comte on 13 Oct 2026). H1 = hits over all their occurrences in glossed units. Two controls, 20000 draws each:
  R  rotation: each unit's gloss rotated by an independent uniform offset (keeps letters, moves only where v sits);
  L  length-matched: each unit's gloss replaced by a window of the same length at a uniform start in the pooled reference gloss text
     (interlinear/f24_reconciled.tsv + interlinear/c20c21_reconciled.tsv glosses, normalised, concatenated; not canvas 29).
  Gate per pass: N1 >= 5 occurrences (else TOO-SHORT); P_min = P(ctrl >= N1) under either control >= 0.05 -> UNDERPOWERED;
  PASS iff H1 > p95 and P(ctrl >= H1) < 0.05 under BOTH R and L; else FAIL.
  Verdict: PASS iff both passes PASS; SPLIT if exactly one; otherwise FAIL (or TOO-SHORT/UNDERPOWERED if both are).
  Consequence: PASS -> canvas 29 tokens of key_f24 C codes read at grade C in reading_c29 (shared key supported on this leaf);
  any other verdict -> every canvas 29 token is M (exceptions_c29.tsv).

TEST 2 (held-out per-code check of the canvas 20-21 leads, D07-COL26K design): 42 = si, 11 = le, 6 = je. Per code, per pass, on
  canvas 29: rotation control R (20000 draws), alpha 0.05 per code (held-out side, as D07), N = 0 -> UNTESTABLE, P_min >= 0.05 ->
  UNDERPOWERED, PASS iff H > p95 and P < 0.05, else FAIL. Power reported, not gating beyond P_min: positive pool = canvas 29
  occurrences of 83 = de and 31 = que, subsampled to the code's N, 1000 subsamples x 500 rotation draws, share with P < 0.05.
  Pooled held-out (f.24 units + canvas 29 units of that pass) is also computed with the same rule.
  Code verdict: canvas29 PASS iff both passes PASS. Licence (grade S in key_period.tsv, as D07-COL26K specified): D07 scored side
  PASS (42, 11; 6 failed its scored side, so 6 cannot be licensed) AND canvas29 PASS AND pooled held-out PASS on both passes.
  Anything else leaves key_period.tsv's value and grade unchanged (a note with the numbers is added).
Seeds: 20261013 + 1 (test 1), + int(code) (test 2), + 99 (power). Output: interlinear/c29_test_out.txt (stdout).
Usage: python3 interlinear/c29_test.py
"""
import csv, os, random, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); WIN = 0.25; SEED = 20261013; NCTL = 20000; NSUB, NSUBCTL = 1000, 500
LEADS = [('42', 'si'), ('11', 'le'), ('6', 'je')]; POS = [('83', 'de'), ('31', 'que')]; D07_SCORED = {'42': 'PASS', '11': 'PASS', '6': 'FAIL'}
def norm(s): return ''.join(c for c in unicodedata.normalize('NFD', s.lower().replace('[?]', '')) if c.isalpha())
def rows(fn): return list(csv.DictReader(open(os.path.join(HERE, fn)), delimiter='\t'))
key = {r['code']: norm(r['value']) for r in csv.DictReader(open(os.path.join(HERE, '..', 'key_f24.tsv')), delimiter='\t') if r['grade'] == 'C'}
ref = ''.join(norm(r['gloss_text']) for fn in ('f24_reconciled.tsv', 'c20c21_reconciled.tsv') for r in rows(fn))
U = rows('c29_units.tsv')
def units(p): return [([t for t in r['cipher_tokens'].split() if t != '|'], norm(r['gloss_' + p])) for r in U if norm(r['gloss_' + p])]
f24 = [([t for t in r['cipher_tokens'].split() if t != '|'], norm(r['gloss_text'])) for r in rows('f24_reconciled.tsv')]
def occs(us, pairs): return [(u, i, v) for u, (toks, g) in enumerate(us) for i, t in enumerate(toks) for c, v in pairs if t == c]
def hitg(g, i, n, v):
    L = len(g)
    if not L or len(v) > L: return 0
    gg = g + g; p = (i + 0.5) / n
    return int(any(gg[j:j+len(v)] == v and abs((j + len(v) / 2) / L - p) <= WIN for j in range(L)))
def H(us, oc, gl): return sum(hitg(gl[u], i, len(us[u][0]), v) for u, i, v in oc)
def rot(us, rng): return [g[(k := rng.randrange(len(g))):] + g[:k] for _, g in us]
def lenm(us, rng): return [ref[(k := rng.randrange(len(ref) - len(g) + 1)):k + len(g)] for _, g in us]
def control(us, oc, n, rng, kind):
    real = H(us, oc, [g for _, g in us]); f = rot if kind == 'R' else lenm
    ctl = sorted(H(us, oc, f(us, rng)) for _ in range(n))
    return real, sum(ctl) / n, ctl[int(0.95 * n)], ctl[-1], sum(c >= real for c in ctl) / n, sum(c >= len(oc) for c in ctl) / n
def verdict(r, N, alpha=0.05, floor=0):
    if N < floor: return 'TOO-SHORT'
    if r[5] >= alpha: return 'UNDERPOWERED'
    return 'PASS' if r[0] > r[2] and r[4] < alpha else 'FAIL'
def combine(vs):
    if all(v == 'PASS' for v in vs): return 'PASS'
    if any(v == 'PASS' for v in vs): return 'SPLIT'
    return vs[0] if len(set(vs)) == 1 else 'FAIL'
print(f"units: {len(U)} runs; glossed in pass A {len(units('A'))}, pass B {len(units('B'))}; reference gloss {len(ref)} letters")
print(f"TEST 1 key_f24 C codes: {', '.join(f'{k}={v}' for k, v in sorted(key.items()))}")
print('pass\tN\tH\tctrl\tmean\tp95\tmax\tP\tP_min\tverdict'); t1 = []
for p in 'AB':
    us = units(p); oc = occs(us, key.items()); vs = []
    for kind in 'RL':
        r = control(us, oc, NCTL, random.Random(SEED + 1), kind); v = verdict(r, len(oc), floor=5); vs.append(v)
        print(f"{p}\t{len(oc)}\t{r[0]}\t{kind}\t{r[1]:.2f}\t{r[2]}\t{r[3]}\t{r[4]:.4f}\t{r[5]:.4f}\t{v}")
    per = {}
    for u, i, v in oc:
        c = us[u][0][i]; per.setdefault(c, [0, 0]); per[c][1] += 1; per[c][0] += hitg(us[u][1], i, len(us[u][0]), v)
    print(f"  pass {p} per code: " + ', '.join(f"{c}={key[c]} {a}/{b}" for c, (a, b) in sorted(per.items())))
    pv = vs[0] if vs[0] == vs[1] else ('FAIL' if 'FAIL' in vs else next(v for v in vs if v != 'PASS'))
    t1.append(pv); print(f"  pass {p} verdict: {pv}")
T1 = combine(t1); print(f"TEST 1 VERDICT: {T1}")
print('TEST 2 held-out leads\ncode\tvalue\tpass\tside\tN\tH\tmean\tp95\tmax\tP\tP_min\tpower\tverdict'); fin = {}
for code, val in LEADS:
    vc, vp = [], []
    for p in 'AB':
        us = units(p); pool = occs(us, POS)
        for side, S in (('canvas29', us), ('pooled', f24 + us)):
            oc = occs(S, [(code, norm(val))]); rng = random.Random(SEED + int(code))
            if not oc: v = 'UNTESTABLE'; print(f"{code}\t{val}\t{p}\t{side}\t0\t-\t-\t-\t-\t-\t-\t-\t{v}")
            else:
                r = control(S, oc, NCTL, rng, 'R'); v = verdict(r, len(oc)); pw = '-'
                if side == 'canvas29' and pool:
                    prng = random.Random(SEED + 99 + int(code)); ok = 0
                    for _ in range(NSUB):
                        sub = prng.sample(pool, len(oc)) if len(oc) <= len(pool) else [prng.choice(pool) for _ in oc]
                        ok += control(us, sub, NSUBCTL, prng, 'R')[4] < 0.05
                    pw = f"{ok / NSUB:.3f}"
                print(f"{code}\t{val}\t{p}\t{side}\t{len(oc)}\t{r[0]}\t{r[1]:.2f}\t{r[2]}\t{r[3]}\t{r[4]:.4f}\t{r[5]:.4f}\t{pw}\t{v}")
            (vc if side == 'canvas29' else vp).append(v)
    c29, pooled = combine(vc), combine(vp)
    lic = 'LICENSED (S)' if D07_SCORED[code] == 'PASS' and c29 == 'PASS' and pooled == 'PASS' else 'not licensed'
    fin[code] = (c29, pooled, lic)
print('TEST 2 VERDICT: ' + '; '.join(f"{c}={v}: canvas29 {fin[c][0]}, pooled {fin[c][1]}, D07 scored {D07_SCORED[c]} -> {fin[c][2]}" for c, v in LEADS))
