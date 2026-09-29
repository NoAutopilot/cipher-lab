#!/usr/bin/env python3
"""DEB-SWARM-A Phase-1 hand-planted controls (score.py not frozen yet): French verse (Fleurs du Mal, never in the
solver's training corpus) enciphered homophonically so the sign-count curve equals the real text's (settled c1 or c2,
'_' dropped). Optional type noise: a fraction of tokens replaced by a random other sign (drawn from the same curve).
Writes work/plant_<tag>.cip (ids) and work/plant_<tag>.ans (plaintext)."""
import sys, os, random, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, '..', '..', 'scripts'))
from settled_lines import settled_lines
# LOG rows logged in commit 0a0060d7 used DROP={'_'} and CLEAR_DROP=False (c2 N 688 K 128); from commit c4631327 the real-text convention of realrun.py
DROP = {'_', 'MULTI'}; CLEAR_DROP = True
def curve(prefix):
    L = settled_lines(os.path.join(H, '..', '..'), prefix, drop_clear=CLEAR_DROP)
    return sorted(collections.Counter(s for l in L.values() for s in l if s not in DROP).values(), reverse=True)
def plant(prefix, seed, noise=0.0, text=None):
    rng = random.Random(seed); cv = curve(prefix); N = sum(cv)
    if text is None:
        lines = open(os.path.join(H, 'work', 'verse_lines.txt')).read().split('\n')[40:]
        st = rng.randrange(len(lines) - 200); text = ''
        i = st
        while len(text) < N: text += lines[i]; i += 1
        text = text[:N]
    lc = collections.Counter(text)
    # assign signs (by count, desc) to the letter with the largest remaining deficit
    deficit = dict(lc); owner = []
    for k, cnt in enumerate(cv):
        l = max(deficit, key=lambda x: deficit[x]); owner.append(l); deficit[l] -= cnt
    homs = collections.defaultdict(list)
    for k, l in enumerate(owner): homs[l].append(k)
    for l in lc:
        if l not in homs: homs[l].append(len(owner)); owner.append(l); cv.append(1)
    # per letter: a bag of sign ids with multiplicities proportional to the curve, shuffled
    bags = {}
    for l, ks in homs.items():
        w = [cv[k] for k in ks]; need = lc[l]; tot = sum(w)
        bag = []
        for k, x in zip(ks, w): bag += [k] * max(1, round(x * need / tot))
        while len(bag) < need: bag.append(rng.choice(ks))
        rng.shuffle(bag); bags[l] = bag[:need]
    ids = []; it = {l: iter(b) for l, b in bags.items()}
    for ch in text: ids.append(next(it[ch]))
    K = len(owner)
    for i in range(len(ids)):
        if rng.random() < noise: ids[i] = rng.randrange(K)
    return ids, text, owner
if __name__ == '__main__':
    prefix, seed, noise, tag = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
    ids, text, owner = plant(prefix, seed, noise)
    open(os.path.join(H, 'work', f'plant_{tag}.cip'), 'w').write(' '.join(map(str, ids)) + '\n')
    open(os.path.join(H, 'work', f'plant_{tag}.ans'), 'w').write(text + '\n')
    print(tag, 'N', len(ids), 'K', len(set(ids)), 'ownerK', len(owner))
