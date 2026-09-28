#!/usr/bin/env python3
"""H16 (28 Sept 2026): is H13's 7/7 fit for c4 specific to French? The same mixed design (q 0.3, coarse syllabary at
K_target - round(p f N), noise p 0.10 f 0.5 and p 0.05 f 0.5) with each corpus on disk: fr19 (French), la18 (Latin),
en18 (English), it16 (Italian), de19 (German); 200 samples; seven statistics; if every language passes, the test does
not discriminate language at N 282 and says so. Writes h16_language.json."""
import os, sys, re, gzip, json, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import h3_unit_profile as h3, h10_mixed as h10, h13_newtype_noise as h13
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here); repo = os.path.dirname(os.path.dirname(root))
def words_of(folder):
    W = []
    d = os.path.join(repo, 'tools/data', folder)
    for f in sorted(os.listdir(d)):
        if f.endswith('.gz'): W += re.findall(r"[a-z]+", h3.fold(gzip.open(os.path.join(d, f), 'rt', encoding='utf-8', errors='ignore').read()))
        elif f.endswith('.txt') and not f.startswith(('README', 'MANIFEST', 'LICENSE')): W += re.findall(r"[a-z]+", h3.fold(open(os.path.join(d, f), encoding='utf-8', errors='ignore').read()))
    return W
def main():
    rng = random.Random(1); T = h3.target('id160'); out = {}
    for lang in ('fr19', 'la18', 'en18', 'it16', 'de19'):
        try: W = words_of(lang)
        except FileNotFoundError: print(lang, 'no corpus'); continue
        if len(W) < 50000: print(lang, 'corpus too small', len(W)); continue
        for g in ('c4', 'c1'):
            seq = T[g]; N = len(seq); ts = h3.stats(seq)
            for p, f in ((0.05, 0.5), (0.10, 0.5)):
                K0 = max(10, int(ts['K'] - round(p * f * N))); samp = []
                for _ in range(200):
                    o = rng.randrange(len(W) - N); s = h10.encode(W[o:o + N], 0.3, K0, rng)[:N]
                    if len(s) < N: continue
                    samp.append(h3.stats(h13.noise_new(s, p, f, rng)))
                band = {}
                for k in ts:
                    v = sorted(x[k] for x in samp); lo, hi = v[int(0.025 * len(v))], v[int(0.975 * len(v)) - 1]; band[k] = dict(lo=lo, hi=hi, inside=bool(lo <= ts[k] <= hi))
                inside = sum(b['inside'] for b in band.values()); out[f'{lang}:{g}:p{p}'] = dict(words=len(W), N=N, band=band, inside=inside)
                print(f"{lang}\t{g}\tp={p}\tinside {inside}/7\t" + ' '.join(f"{k}={'in' if band[k]['inside'] else ('lo' if ts[k] < band[k]['lo'] else 'hi')}" for k in ts), flush=True)
    json.dump(out, open(os.path.join(root, 'h16_language.json'), 'w'), indent=1)
if __name__ == '__main__': main()
