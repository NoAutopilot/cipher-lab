#!/usr/bin/env python3
"""D07-COL26K (account 1, LANE DEFAULT-account-1-20261007-0042, 7 Oct 2026): per-code POSITIONAL known-answer test of the three
canvas 20-21 leads in key_period.tsv (A4-RFCOL), with f.24 (canvas 27) as held-out material. Pre-registered: this file is committed and
pushed BEFORE its first run (rule 3); nothing below is changed after the run. Scripts and disk only, no images, no network.

Codes and hypothesised values (fixed now, from key_period.tsv's M leads): 42 = si, 11 = le (covers 'les'), 6 = je.
Bonferroni over the 3 codes on the scored side: alpha = 0.05/3 = 0.0167. Held-out side: alpha_h = 0.05 per code (a confirmation).

Material.
  Scored (discovery) units: interlinear/c20c21_reconciled.tsv, 18 units (canvas 20-21). These leads were OBSERVED there after the read,
    so a high count on this side is expected by construction; it is reported, and gated, but cannot license a value on its own.
  Held-out units: interlinear/f24_reconciled.tsv, 11 units (f.24, canvas 27, the same mixed design; key_f24's C codes predicted canvas
    20-21 at 14/19 vs control p95 6, A4-RFCOL). None of the three leads was picked from f.24. '|' tokens dropped from the cipher list.
Normalisation: as interlinear/c20c21_knownanswer.py -- NFD, lower case, letters only ('[?]' removed first); no u/v or i/j merge.

Statistic (A4-RFCOL's positional known-answer statistic, WIN = 0.25, unchanged). For an occurrence of code c at index i in a unit of
  n cipher tokens, predicted relative position p = (i + 0.5)/n. With gloss text g of length L (read circularly), the occurrence is a
  HIT iff len(v) <= L and for some start j in 0..L-1 the circular substring g[j:j+len(v)] == v and |(j + len(v)/2)/L - p| <= WIN.
  H(c) = hits over all occurrences of c (a code twice in one unit counts twice).
Control R (rotation; it can vary on this statistic): each unit's gloss is rotated circularly by an independent uniform offset 0..L-1,
  one offset per unit per draw (all occurrences in a unit share it). It keeps each gloss's letters and its set of circular n-grams, so
  "the gloss contains v" is held fixed, and moves only WHERE v sits relative to p -- the statistic's own axis. 20000 draws, seed
  20261007 + 42 (scored) and + 24 (held-out).
Power (rule 3 last paragraph), two parts per code and side:
  P_min = P(H_ctrl >= number of occurrences): if P_min >= alpha (alpha_h on the held-out side) the side is UNDERPOWERED.
  Positive-control power: the known-answer C codes 83 = de and 31 = que (key_f24 C; on canvas 20-21 they were predictions, 10/10 in
  place) form a positive pool on each side (scored side: their canvas 20-21 occurrences; held-out side: their f.24 occurrences). For
  the candidate's own occurrence count N on that side, draw N occurrences from the pool without replacement (with replacement if
  N > pool size), 1000 subsamples, each scored against its own 500-draw rotation control; power = share with P < the side's alpha.
  Reported, not gating beyond the P_min rule.
GATE per code: PASS iff (scored) H > p95 and P(ctrl >= H) < 0.0167 AND (held-out) N_h >= 1, H_h > p95_h and P_h < 0.05.
  N_h = 0 -> HELD-OUT-UNTESTABLE; held-out P_min >= 0.05 -> HELD-OUT-UNDERPOWERED; scored P_min >= 0.0167 -> UNDERPOWERED;
  otherwise FAIL. Only PASS licenses a value.
Grade rule: a PASS code is written as grade S in key_period.tsv with this evidence (no C: f.24 has no gloss word-aligned to it);
  FAIL/UNDERPOWERED/UNTESTABLE leave key_period.tsv unchanged. No counted reading exists for canvas 20-21 (decode.json covers f.23
  and f.24 only), so no reading changes. Output: interlinear/c20c21_positional_k26_out.txt (stdout).
Usage: python3 interlinear/c20c21_positional_k26.py
"""
import csv, os, random, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); WIN = 0.25; SEED = 20261007
CODES = [('42', 'si'), ('11', 'le'), ('6', 'je')]; POS = [('83', 'de'), ('31', 'que')]
ALPHA, ALPHA_H, NCTL, NSUB, NSUBCTL = 0.05 / 3, 0.05, 20000, 1000, 500
def norm(s): return ''.join(c for c in unicodedata.normalize('NFD', s.lower().replace('[?]', '')) if c.isalpha())
def load(fn): return [([t for t in r['cipher_tokens'].split() if t != '|'], norm(r['gloss_text']))
                      for r in csv.DictReader(open(os.path.join(HERE, fn)), delimiter='\t')]
def occs(units, code, val): return [(u, i, val) for u, (toks, g) in enumerate(units) for i, t in enumerate(toks) if t == code]
def hit(units, rot, u, i, v):
    toks, g = units[u]; L = len(g)
    if not L or len(v) > L: return 0
    r = rot[u] % L; g = g[r:] + g[:r]; gg = g + g; p = (i + 0.5) / len(toks)
    return int(any(gg[j:j+len(v)] == v and abs((j + len(v) / 2) / L - p) <= WIN for j in range(L)))
def H(units, oc, rot): return sum(hit(units, rot, u, i, v) for u, i, v in oc)
def control(units, oc, n, rng):
    zero = [0] * len(units); real = H(units, oc, zero)
    lens = [max(len(g), 1) for _, g in units]
    ctl = sorted(H(units, oc, [rng.randrange(l) for l in lens]) for _ in range(n))
    return real, ctl, sum(ctl) / n, ctl[int(0.95 * n)], ctl[-1], sum(c >= real for c in ctl) / n, sum(c >= len(oc) for c in ctl) / n
def power(units, pool, N, alpha, rng):
    if not N or not pool: return float('nan')
    ok = 0
    for _ in range(NSUB):
        sub = rng.sample(pool, N) if N <= len(pool) else [rng.choice(pool) for _ in range(N)]
        ok += control(units, sub, NSUBCTL, rng)[5] < alpha
    return ok / NSUB
sc, ho = load('c20c21_reconciled.tsv'), load('f24_reconciled.tsv')
pool_sc = [o for c, v in POS for o in occs(sc, c, v)]; pool_ho = [o for c, v in POS for o in occs(ho, c, v)]
for name, units, pool, a, s in (('scored canvas 20-21', sc, pool_sc, ALPHA, SEED + 42), ('held-out f.24', ho, pool_ho, ALPHA_H, SEED + 24)):
    rng = random.Random(s); r = control(units, pool, NCTL, rng)
    print(f"positive control 83=de+31=que on {name}: H {r[0]}/{len(pool)} ctrl mean {r[2]:.2f} p95 {r[3]} max {r[4]} P {r[5]:.4f}")
print('code\tvalue\tside\tN\tH\tctrl_mean\tp95\tmax\tP\tP_min\tpos_power_at_N\tside_verdict')
final = {}
for code, val in CODES:
    res = {}
    for name, units, pool, a, s in (('scored', sc, pool_sc, ALPHA, SEED + 42), ('heldout', ho, pool_ho, ALPHA_H, SEED + 24)):
        rng = random.Random(s + int(code)); oc = occs(units, code, val)
        if not oc: res[name] = 'UNTESTABLE'; print(f"{code}\t{val}\t{name}\t0\t-\t-\t-\t-\t-\t-\t-\tUNTESTABLE"); continue
        real, ctl, mean, p95, mx, P, Pmin = control(units, oc, NCTL, rng); pw = power(units, pool, len(oc), a, rng)
        v = 'UNDERPOWERED' if Pmin >= a else ('PASS' if real > p95 and P < a else 'FAIL')
        res[name] = v
        print(f"{code}\t{val}\t{name}\t{len(oc)}\t{real}\t{mean:.2f}\t{p95}\t{mx}\t{P:.4f}\t{Pmin:.4f}\t{pw:.3f}\t{v}")
    s_, h_ = res['scored'], res['heldout']
    final[code] = ('PASS' if s_ == 'PASS' and h_ == 'PASS' else 'UNDERPOWERED' if s_ == 'UNDERPOWERED' else
                   'HELD-OUT-UNTESTABLE' if h_ == 'UNTESTABLE' else 'HELD-OUT-UNDERPOWERED' if h_ == 'UNDERPOWERED' else 'FAIL')
print('GATE: ' + ', '.join(f"{c}={v} {final[c]}" for c, v in CODES))
