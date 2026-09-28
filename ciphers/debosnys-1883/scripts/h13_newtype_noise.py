#!/usr/bin/env python3
"""H13 (28 Sept 2026): H9/H10 controls with a noise model that INVENTS types: a share p of tokens is replaced, a
fraction f of those by a fresh singleton type, the rest by a random existing type (weighted by count). Designs:
coarse syllabary at the target's K, and the H10 mixed design at q 0.3 and 0.4; p in 0.05..0.20, f in 0.5 and 1.0.
The target's K is matched BEFORE noise, so the noisy sample's K exceeds it by the invented types -- to compare
fairly, the pre-noise K is set to K_target - round(p*f*N) (v2, 28 Sept 21:5x UTC; v1 scaled by (1 - p*f), which under-subtracts at pooled N). 200 samples per condition. Writes h13_noise.json."""
import os, sys, json, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import h3_unit_profile as h3, h9_controls as h9, h10_mixed as h10
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
def noise_new(seq, p, f, rng):
    cnt = collections.Counter(seq); types = list(cnt); w = [cnt[t] for t in types]; out = []; fresh = 0
    for s in seq:
        if rng.random() < p:
            if rng.random() < f: fresh += 1; out.append(('NEW', fresh))
            else: out.append(rng.choices(types, w)[0])
        else: out.append(s)
    return out
def main():
    rng = random.Random(1); W = h3.corpus_words(); T = h3.target('id160'); out = {}
    groups = ('all', 'c4', 'c1') if ('--drop-x' not in sys.argv and '--merge-xx' not in sys.argv) else ('all',)
    for g in groups:
        seq = T[g]
        if '--drop-x' in sys.argv: seq = [s for s in seq if s != 'X']; g = g + '-noX'  # H14: X treated as a null/filler
        if '--merge-xx' in sys.argv:  # H22: adjacent X X as one token
            m = []; i = 0
            while i < len(seq):
                if seq[i] == 'X' and i + 1 < len(seq) and seq[i + 1] == 'X': m.append('XX'); i += 2
                else: m.append(seq[i]); i += 1
            seq = m; g = g + '-XX'
        N = len(seq); ts = h3.stats(seq)
        for design in ('coarse', 'mixed0.3', 'mixed0.4'):
            for p in (0.05, 0.10, 0.15, 0.20):
                for f in (0.5, 1.0):
                    K0 = max(10, int(ts['K'] - round(p * f * N))); samp = []
                    for _ in range(200):
                        o = rng.randrange(len(W) - N); words = W[o:o + N]
                        if design == 'coarse':
                            st = [s for w in words for s in h3.syll(w)][:N]; s = h9.coarse(st, K0, rng)
                        else:
                            s = h10.encode(words, float(design[5:]), K0, rng)[:N]
                        if len(s) < N: continue
                        samp.append(h3.stats(noise_new(s, p, f, rng)))
                    band = {}
                    for k in ts:
                        v = sorted(x[k] for x in samp); lo, hi = v[int(0.025 * len(v))], v[int(0.975 * len(v)) - 1]; band[k] = dict(lo=lo, hi=hi, median=v[len(v) // 2], inside=bool(lo <= ts[k] <= hi))
                    inside = sum(b['inside'] for b in band.values()); out[f'{g}:{design}:p{p}:f{f}'] = dict(N=N, K0=K0, band=band, inside=inside)
                    print(f"{g}\t{design}\tp={p}\tf={f}\tK0={K0}\tinside {inside}/7\t" + ' '.join(f"{k}={'in' if band[k]['inside'] else ('lo' if ts[k] < band[k]['lo'] else 'hi')}" for k in ts), flush=True)
    json.dump(out, open(os.path.join(root, 'h13_noise.json' if ('--drop-x' not in sys.argv and '--merge-xx' not in sys.argv) else ('h14_noise_noX.json' if '--drop-x' in sys.argv else 'h22_noise_XX.json')), 'w'), indent=1)
if __name__ == '__main__': main()
