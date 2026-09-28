#!/usr/bin/env python3
"""H10 (28 Sept 2026): does a MIXED design reproduce the target's seven token statistics (scripts/h3_unit_profile.py)?
Design: French text (fr19); each word is written either letter by letter (probability q per word, letters share one
sign each across the text) or syllable by syllable (a syllabary whose rare types are merged until the sample's total
K matches the target's K); variant 'e-only': a syllabary where the letter e alone, when it is a syllable of its own
(a lone vowel group), keeps a letter sign -- and variant 'top': the most frequent syllable types get 2-3 homophones.
200 samples per condition at pooled N and at c4's N; the design fits when all seven statistics sit inside the band.
Writes h10_mixed.json."""
import os, sys, re, json, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import h3_unit_profile as h3, h9_controls as h9
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
def encode(words, q, K, rng, variant=None):
    toks = []
    for w in words:
        if variant == 'e-only':
            for s in h3.syll(w): toks.append(('L', 'e') if s == 'e' else ('S', s))
        elif rng.random() < q:
            for c in w: toks.append(('L', c))
        else:
            for s in h3.syll(w): toks.append(('S', s))
    return h9.coarse(toks, K, rng)
def main():
    rng = random.Random(1); W = h3.corpus_words(); T = h3.target('id160'); out = {}
    for g in ('all', 'c4'):
        seq = T[g]; N = len(seq); ts = h3.stats(seq)
        for q in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 1.0, 'e-only'):
            samp = []
            for _ in range(200):
                o = rng.randrange(len(W) - N); words = W[o:o + N]  # more words than needed; cut after encoding
                s = encode(words, q if q != 'e-only' else 0.0, ts['K'], rng, variant='e-only' if q == 'e-only' else None)[:N]
                if len(s) < N: continue
                samp.append(h3.stats(s))
            band = {}
            for k in ts:
                v = sorted(x[k] for x in samp); band[k] = dict(lo=v[int(0.025 * len(v))], hi=v[int(0.975 * len(v)) - 1], median=v[len(v) // 2], inside=bool(v[int(0.025 * len(v))] <= ts[k] <= v[int(0.975 * len(v)) - 1]))
            inside = sum(b['inside'] for b in band.values())
            out[f'{g}:q={q}'] = dict(N=N, K=ts['K'], band=band, inside=inside)
            print(f"{g}\tN={N}\tq={q}\tinside {inside}/7\t" + ' '.join(f"{k}={'in' if band[k]['inside'] else ('lo' if ts[k] < band[k]['lo'] else 'hi')}({band[k]['median']:.3f})" for k in ts), flush=True)
    json.dump(out, open(os.path.join(root, 'h10_mixed.json'), 'w'), indent=1)
if __name__ == '__main__': main()
