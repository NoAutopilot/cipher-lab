#!/usr/bin/env python3
"""H38 (29 Sept 2026): does the homophonic mixed design fit the single-sign statistics AND the repeat counts together?
Target: settled drafts (settled_lines), '_'/MULTI dropped for H3's seven statistics (as H23: pooled N 1184), and
punctuation-class boxes also dropped for the repeat counts (as H34: N 1147). Design: h10_mixed.encode (fr19 prose, q
0.2/0.3/0.4), every type of count >= c (c 3 and 6) split into h variants (h 2, 3, 4) chosen per token equiprobably or
Zipf-weighted (p_j ~ 1/(j+1)), pre-split K searched so the post-noise K lands within 5 of the target's; invented-type
noise p 0, 0.10, 0.20 with f 0.5. 100 samples per condition; a condition 'fits' when the target is inside the
2.5-97.5 band on all seven statistics and on repeated 3-grams and 4-grams (nine in all). Many conditions are tried,
so a fit is read as consistency, not proof, and each fitting condition is re-run with a fresh seed (200 samples) to
confirm. Writes h38_homophonic_fit.json. --drop-x (H39): every X removed from the target before both counts (X as a
null or non-text sign, H14's test repeated under the homophonic design); writes h39_homophonic_noX.json."""
import os, json, random, collections, sys, itertools
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
sys.path.insert(0, here); from settled_lines import settled_lines
import h3_unit_profile as h3, h10_mixed as h10, h13_newtype_noise as h13
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
raw = settled_lines(root, 'c')
seq7 = [s for v in raw.values() for s in v if s not in ('_', 'MULTI')]
seqR = [s for v in raw.values() for s in v if s not in PUNCT]
DROPX = '--drop-x' in sys.argv
if DROPX: seq7 = [s for s in seq7 if s != 'X']; seqR = [s for s in seqR if s != 'X']
def repeats(s):
    r = {}
    for n in (3, 4):
        c = collections.Counter(tuple(s[i:i + n]) for i in range(len(s) - n + 1)); r[f'rep{n}'] = sum(1 for v in c.values() if v >= 2)
    return r
T = dict(h3.stats(seq7)); T.update(repeats(seqR)); N = len(seq7); KT = T['K']
print('target', {k: round(v, 3) for k, v in T.items()}, 'N', N)
W = h3.corpus_words()
def split(s, h, c, zipf, rng):
    cnt = collections.Counter(s); w = [1 / (j + 1) for j in range(h)] if zipf else [1] * h
    return [(t, rng.choices(range(h), w)[0]) if cnt[t] >= c else t for t in s]
def sample(q, h, c, zipf, p, K0, rng):
    while True:
        o = rng.randrange(len(W) - N); s = h10.encode(W[o:o + N], q, K0, rng)[:N]
        if len(s) == N: break
    s = split(s, h, c, zipf, rng); s = h13.noise_new(s, p, 0.5, rng) if p else s
    d = dict(h3.stats(s)); d.update(repeats(s)); return d
def calibrate(q, h, c, zipf, p, rng):
    lo, hi = 10, 400
    for _ in range(9):
        mid = (lo + hi) // 2; k = sorted(sample(q, h, c, zipf, p, mid, rng)['K'] for _ in range(5))[2]
        if k < KT: lo = mid + 1
        else: hi = mid
    return lo
def run(q, h, c, zipf, p, n, seed):
    rng = random.Random(seed); K0 = calibrate(q, h, c, zipf, p, rng)
    S = [sample(q, h, c, zipf, p, K0, rng) for _ in range(n)]; band = {}
    for k in T:
        v = sorted(x[k] for x in S); lo, hi = v[int(0.025 * n)], v[int(0.975 * n) - 1]
        band[k] = dict(lo=round(lo, 4), hi=round(hi, 4), inside=lo <= T[k] <= hi, side='in' if lo <= T[k] <= hi else ('lo' if T[k] < lo else 'hi'))
    return K0, band
def main():
  out = {}; fits = []
  for q, h, c, zipf, p in itertools.product((0.2, 0.3, 0.4), (2, 3, 4), (3, 6), (False, True), (0.0, 0.10, 0.20)):
      K0, band = run(q, h, c, zipf, p, 100, hash((q, h, c, zipf, p)) & 0xffff)
      ins = sum(b['inside'] for b in band.values()); key = f'q{q}:h{h}:c{c}:{"zipf" if zipf else "eq"}:p{p}'
      out[key] = dict(K0=K0, inside=ins, band=band)
      print(key, 'K0', K0, f'{ins}/9', ' '.join(f"{k}={b['side']}" for k, b in band.items()), flush=True)
      if ins == 9: fits.append((q, h, c, zipf, p))
  conf = {}
  for q, h, c, zipf, p in fits:
      K0, band = run(q, h, c, zipf, p, 200, 99991 + len(conf)); ins = sum(b['inside'] for b in band.values())
      conf[f'q{q}:h{h}:c{c}:{"zipf" if zipf else "eq"}:p{p}'] = dict(K0=K0, inside=ins, band=band); print('CONFIRM', q, h, c, zipf, p, f'{ins}/9')
  json.dump(dict(target=T, N=N, conditions=out, confirm=conf), open(os.path.join(root, 'h39_homophonic_noX.json' if DROPX else 'h38_homophonic_fit.json'), 'w'), indent=1)
if __name__ == '__main__': main()
