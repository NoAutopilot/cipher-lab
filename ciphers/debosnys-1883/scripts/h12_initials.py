#!/usr/bin/env python3
"""H12 (28 Sept 2026): the initials crib. Cryptogram 2 (No.9) carries the clear "H.D.D.L.M.F." with dots beneath read
by Pelling (2015) as the counts of missing letters (4,8,7,6,6,5): Henry Deletnack Debosnys and three unknown names. If
the cipher near it (or anywhere) writes those names LETTER BY LETTER, the sign run must be an isomorph of the letter
pattern of "enry eletnack ebosnys" (19 letters: e in four places, n in three, y in two, s twice ...): equal letters
give equal signs and different letters different signs. Scan every offset of every cryptogram (160-id draft) for the
share of the 171 letter pairs whose equality is respected by the signs, take the best offset, and compare with 1000
shuffles of the sign sequence (max over offsets each). Under a syllable-scale design (H3-H13) no match is expected;
the test is cheap and its negative is control-backed only for the letter-level reading. Writes h12_initials.json."""
import os, sys, json, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import h3_unit_profile as h3
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
PAT = 'enryeletnackebosnys'
pairs = [(i, j, PAT[i] == PAT[j]) for i, j in itertools.combinations(range(len(PAT)), 2)]
def score(seq, o): return sum((seq[o + i] == seq[o + j]) == eq for i, j, eq in pairs) / len(pairs)
def best(seq): return max((score(seq, o), o) for o in range(len(seq) - len(PAT) + 1))
def main():
    rng = random.Random(1); T = h3.target('id160'); out = {}
    for g in ('c2', 'c1', 'c3', 'c4'):
        seq = T[g]; obs, off = best(seq); null = []
        for _ in range(1000):
            s = seq[:]; rng.shuffle(s); null.append(best(s)[0])
        null.sort(); q = null[974]
        # also: the exact-isomorph count (score 1.0) is what a true letter-level match would give
        out[g] = dict(N=len(seq), best=round(obs, 4), offset=off, null_p975=round(q, 4), null_max=round(null[-1], 4), clears=bool(obs > q))
        print(g, out[g])
    json.dump(out, open(os.path.join(root, 'h12_initials.json'), 'w'), indent=1)
if __name__ == '__main__': main()
