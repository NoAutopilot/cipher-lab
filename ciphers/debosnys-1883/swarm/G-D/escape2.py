#!/usr/bin/env python3
"""DEB-SWARM-D escape routes, round 2 (29 Sept 2026), c2 shape, 15 pct type noise, frozen c2 score (dcore.score 'c2'
parts) and the real c2's value beside it:
ANAGRAM: every French word's letters shuffled before a homophonic letter key (a word-internal transposition).
RUNKEY: a running-key Vigenere over the letters (key = another French passage), then a homophonic key over the sum.
AUTOKEY: plaintext-autokey Vigenere, then homophonic.
NULLS-q for q 0.5, 0.65: random nulls from the sign curve at share q (the boundary where the score reaches the
real text's level). Writes escape2.json."""
import dcore, escape, random, json, statistics as st
rng = random.Random(5151); L2 = escape.L2; N2 = escape.N2; cv = escape.cv; A = 'abcdefghijklmnopqrstuvwxyz'
def homo(us): return dcore.cut(dcore.noise(escape.homo_seq(us, cv, rng), 0.15, rng), L2)
def anagram():
    W = dcore.words('fr'); o = rng.randrange(len(W) - 3000); us = []
    for w in W[o:]:
        l = list(w); rng.shuffle(l); us += l
        if len(us) >= N2: break
    return homo(us[:N2])
def vig(auto):
    p = dcore.units('fr', N2, rng, 'letters'); k = p[:1] + p[:-1] if auto else dcore.units('fr', N2, rng, 'letters')
    return homo([A[(A.index(a) + A.index(b)) % 26] for a, b in zip(p, k)])
def c2s(lines):
    z = dcore.zstats(lines, rng, 100); return z['mi1']['z'] + z['bg2']['z'] + z['rep3']['z'] - z['dbl']['z']
ts = st.median(c2s(dcore.target('c2')) for _ in range(3)); res = {'target_c2_score': ts}
for name, gen in (('ANAGRAM', anagram), ('RUNKEY', lambda: vig(False)), ('AUTOKEY', lambda: vig(True)),
                  ('NULLS-0.5', lambda: escape.nulls(0.5)), ('NULLS-0.65', lambda: escape.nulls(0.65)),
                  ('FR-HOMO ref', lambda: homo(dcore.units('fr', N2, rng, 'letters')))):
    v = sorted(c2s(gen()) for _ in range(20))
    res[name] = dict(median=st.median(v), min=v[0], max=v[-1], share_le_target=sum(x <= ts for x in v) / len(v)); print(name, res[name], flush=True)
json.dump(res, open('escape2.json', 'w'), indent=1)
