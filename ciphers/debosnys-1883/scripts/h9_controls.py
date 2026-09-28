#!/usr/bin/env python3
"""H9 (28 Sept 2026): the two controls H3 lacked, on H3's seven statistics (scripts/h3_unit_profile.py):
  (a) coarse syllabary: French syllables with the rarest types merged into a frequent type until the sample's K equals
      the target's K (160 pooled at N 1264; 84 for c4 at N 282) -- a syllable code whose author reuses signs;
  (b) each unit control (letter, syllable, rime, word, coarse syllabary) with 15 pct type noise injected: a share p of
      tokens redrawn to another type, weighted by the sample's own type counts (the GOLD-D1 recipe's shape);
  (c) the same on VERSE (tools/data/fr19v, Baudelaire) instead of prose, for cryptogram 4 (couplets) and pooled.
200 samples per condition, seed 1; a statistic is consistent when the target sits inside the 2.5-97.5 pct band.
Writes h9_controls.json; prints one line per condition with the count of statistics inside the band (of 7).
"""
import os, sys, re, gzip, json, random, collections, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import h3_unit_profile as h3
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here); repo = os.path.dirname(os.path.dirname(root))
def verse_words():
    t = gzip.open(os.path.join(repo, 'tools/data/fr19v/pg6099_Les_Fleurs_du_Mal.txt.gz'), 'rt', encoding='utf-8', errors='ignore').read()
    return re.findall(r"[a-z]+", h3.fold(t))
def coarse(stream_syll, K, rng):
    """merge rare syllable types into frequent ones until K types remain, per sample"""
    cnt = collections.Counter(stream_syll); types = [t for t, _ in cnt.most_common()]
    if len(types) <= K: return stream_syll
    keep = types[:K]; m = {t: t for t in keep}
    for t in types[K:]: m[t] = rng.choice(keep)
    return [m[t] for t in stream_syll]
def noise(seq, p, rng):
    cnt = collections.Counter(seq); types = list(cnt); w = [cnt[t] for t in types]
    return [rng.choices(types, w)[0] if rng.random() < p else s for s in seq]
def main():
    rng = random.Random(1); out = {}
    corpora = {'prose': h3.corpus_words(), 'verse': verse_words()}
    T = h3.target('id160')
    for cname, W in corpora.items():
        streams = {u: f(W) for u, f in h3.UNITS.items() if u != 'shorthand'}
        for g in ('all', 'c4', 'c1'):
            seq = T[g]; N = len(seq); ts = h3.stats(seq)
            for u in list(streams) + ['coarse']:
                for p in (0.0, 0.15):
                    samp = []
                    for _ in range(200):
                        st = streams['syllable'] if u == 'coarse' else streams[u]
                        o = rng.randrange(len(st) - N); s = st[o:o + N]
                        if u == 'coarse': s = coarse(s, ts['K'], rng)
                        if p: s = noise(s, p, rng)
                        samp.append(h3.stats(s))
                    band = {}
                    for k in ts:
                        v = sorted(x[k] for x in samp); band[k] = dict(lo=v[4], hi=v[194], median=v[99], inside=bool(v[4] <= ts[k] <= v[194]))
                    inside = sum(b['inside'] for b in band.values())
                    out[f'{cname}:{g}:{u}:noise{p}'] = dict(N=N, target=ts, band=band, inside=inside)
                    print(f"{cname}\t{g}\tN={N}\t{u}\tnoise={p}\tinside {inside}/7\t" + ' '.join(f"{k}={'in' if band[k]['inside'] else ('lo' if ts[k] < band[k]['lo'] else 'hi')}" for k in ts), flush=True)
    json.dump(out, open(os.path.join(root, 'h9_controls.json'), 'w'), indent=1)
if __name__ == '__main__': main()
