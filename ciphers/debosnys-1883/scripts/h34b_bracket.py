#!/usr/bin/env python3
"""H34 bracket (29 Sept 2026): the H34 mixed-design control re-run at the target's measured noise ceiling and beyond
(p 0.10, 0.20, 0.30; invented-type share f 0.5 and 1.0; rule 3's bracket requirement: the settled drafts carry
8.5-18 pct type noise), plus a homophonic variant: the same mixed design with every type of count >= 4 split into h
equiprobable variants chosen per token (h 2 and 3), pre-noise K set so the post-split K matches the target. Power:
the design
samples' repeat counts falling toward the shuffled level as noise/homophony rise. 100 samples per condition. Writes
h34_bracket.json."""
import os, json, random, collections, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
sys.path.insert(0, here)
import h3_unit_profile as h3, h10_mixed as h10, h13_newtype_noise as h13
tgt = json.load(open(os.path.join(root, 'h34_long_repeats.json'))); N, K = tgt['N'], tgt['K']; obs = {int(k): v['obs'] for k, v in tgt['stats'].items()}
def repeats(s):
    r = {}
    for n in (3, 4, 5):
        c = collections.Counter(tuple(s[i:i + n]) for i in range(len(s) - n + 1)); r[n] = sum(1 for v in c.values() if v >= 2)
    return r
def split_h(s, h, rng):
    c = collections.Counter(s); return [(t, rng.randrange(h)) if c[t] >= 4 else t for t in s]
rng = random.Random(341); W = h3.corpus_words(); out = {}
conds = [('mixed', p, f, 1) for p in (0.10, 0.20, 0.30) for f in (0.5, 1.0)] + [('homophonic', p, 0.5, h) for p in (0.0, 0.10, 0.20) for h in (2, 3)]
for design, p, f, h in conds:
    samp = []; K0 = max(10, int(K - round(p * f * N)))
    if h > 1:  # find a pre-split K giving about the target's K after splitting (one calibration sample)
        for trial_k in range(K0, 9, -5):
            o = rng.randrange(len(W) - N); s = h10.encode(W[o:o + N], 0.3, trial_k, rng)[:N]
            if len(set(split_h(s, h, rng))) <= K0: K0 = trial_k; break
    while len(samp) < 100:
        o = rng.randrange(len(W) - N); s = h10.encode(W[o:o + N], 0.3, K0, rng)[:N]
        if len(s) < N: continue
        if h > 1: s = split_h(s, h, rng)
        s = h13.noise_new(s, p, f, rng); samp.append((repeats(s), len(set(s))))
    key = f'{design}:p{p}:f{f}:h{h}'; d = {}
    for n in (3, 4, 5):
        x = sorted(r[n] for r, _ in samp); d[n] = dict(lo=x[2], hi=x[96], median=x[50], target_inside=x[2] <= obs[n] <= x[96])
    d['K_median'] = sorted(k for _, k in samp)[50]; out[key] = d
    print(key, 'K~', d['K_median'], ' '.join(f"n{n}:{d[n]['lo']}-{d[n]['hi']}{'(in)' if d[n]['target_inside'] else ''}" for n in (3, 4, 5)), flush=True)
print('target', obs, 'N', N, 'K', K)
json.dump(out, open(os.path.join(root, 'h34_bracket.json'), 'w'), indent=1)
