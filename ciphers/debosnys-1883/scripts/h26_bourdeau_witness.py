#!/usr/bin/env python3
"""H26 (28 Sept 2026): Bourdeau's independent read of the cipher verse (sources/bourdeau/cyphersolver-targets-debosnys/
verse_transcription.py, MIT, 20 lines) as a second witness for cryptogram 4. His punctuation tokens (, . -) and our
punctuation-class boxes (BLOB, HOOK-L, DASH-H, _, MULTI) are dropped; '?' stripped from his codes. Alignment per line:
first by relative position, then a concordance his-code -> our-id by majority co-occurrence, then a second pass with a
Needleman-Wunsch alignment scoring +2 for a concordant pair, 0 otherwise, -1 for a gap, iterated twice. Reports per
line the token counts and the share of our boxes whose aligned Bourdeau code maps (by the concordance) to our id;
the concordance's size and how many of his codes map one-to-one; writes h26_concordance.tsv and h26_alignment.tsv."""
import os, sys, csv, collections
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here); repo = os.path.dirname(os.path.dirname(root))
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
sys.path.insert(0, os.path.join(repo, 'sources/bourdeau/cyphersolver-targets-debosnys')); import verse_transcription as v
B = v.lines()
by = collections.OrderedDict()
for r in csv.DictReader(open(os.path.join(root, 'passA.tsv')), delimiter='\t'):
    if r['line'].startswith('c4'): by.setdefault(r['line'], []).append((int(r['position']), r['sign']))
keys = sorted(by, key=lambda k: (0 if k.startswith('c4a0') else 1 if k.startswith('c4a') else 2, k))
O = [[(p, s) for p, s in by[k] if s not in PUNCT] for k in keys]
assert len(O) == 20 == len(B)
def nw(a, b, score):
    n, m = len(a), len(b); S = [[0] * (m + 1) for _ in range(n + 1)]; T = [[None] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): S[i][0] = -i; T[i][0] = 'u'
    for j in range(1, m + 1): S[0][j] = -j; T[0][j] = 'l'
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d = S[i - 1][j - 1] + score(a[i - 1], b[j - 1]); u = S[i - 1][j] - 1; l = S[i][j - 1] - 1
            S[i][j] = max(d, u, l); T[i][j] = 'd' if S[i][j] == d else ('u' if S[i][j] == u else 'l')
    i, j = n, m; pairs = []
    while i > 0 or j > 0:
        t = T[i][j]
        if t == 'd': pairs.append((a[i - 1], b[j - 1])); i -= 1; j -= 1
        elif t == 'u': pairs.append((a[i - 1], None)); i -= 1
        else: pairs.append((None, b[j - 1])); j -= 1
    return pairs[::-1]
# pass 0: relative-position pairing
co = collections.Counter()
for o, b in zip(O, B):
    for k, (p, s) in enumerate(o):
        j = round(k * (len(b) - 1) / max(1, len(o) - 1)) if len(o) > 1 else 0; co[(b[j], s)] += 1
def concordance(co):
    best = {}
    for (bc, s), n in co.items():
        if bc not in best or n > best[bc][1]: best[bc] = (s, n)
    return {bc: s for bc, (s, n) in best.items()}
conc = concordance(co)
for it in range(2):
    co = collections.Counter(); aligned = []
    for li, (o, b) in enumerate(zip(O, B)):
        pairs = nw(o, b, lambda x, y: 2 if conc.get(y) == x[1] else 0)
        for x, y in pairs:
            if x and y: co[(y, x[1])] += 1
        aligned.append(pairs)
    conc = concordance(co)
tot = agree = 0; rows = []
for li, pairs in enumerate(aligned):
    n = a = 0
    for x, y in pairs:
        if x and y: n += 1; a += conc.get(y) == x[1]
    tot += n; agree += a; rows.append((li + 1, len(O[li]), len(B[li]), n, a))
print('line\tours\tbourdeau\taligned\tconcordant')
for r in rows: print('\t'.join(map(str, r)))
print(f"total aligned {tot}, concordant {agree} = {agree/tot:.3f}; our c4 boxes {sum(len(o) for o in O)}, his tokens {sum(len(b) for b in B)}")
inv = collections.Counter(conc.values()); one2one = sum(1 for bc, s in conc.items() if inv[s] == 1)
print(f"concordance: {len(conc)} of his codes mapped to {len(set(conc.values()))} of our ids; one-to-one {one2one}; many-to-one collisions {sum(1 for s, n in inv.items() if n > 1)}")
with open(os.path.join(root, 'h26_concordance.tsv'), 'w') as f:
    f.write('bourdeau_code\tour_id\tcooccurrences\n')
    for bc, s in sorted(conc.items(), key=lambda kv: -co[(kv[0], kv[1])]): f.write(f'{bc}\t{s}\t{co[(bc, s)]}\n')
with open(os.path.join(root, 'h26_alignment.tsv'), 'w') as f:
    f.write('verse_line\tour_line\tour_pos\tour_id\tbourdeau_code\tconcordant\n')
    for li, pairs in enumerate(aligned):
        for x, y in pairs: f.write(f"{li+1}\t{keys[li]}\t{x[0] if x else ''}\t{x[1] if x else ''}\t{y or ''}\t{'' if not (x and y) else int(conc.get(y) == x[1])}\n")

# held-out check (added the same session, before the row was logged): fit the concordance on one half of the lines
# (odd or even verse numbers), align and score the other half with it, both ways; the honest witness number.
def heldout():
    out = []
    for fold in (0, 1):
        train = [i for i in range(20) if i % 2 == fold]; test = [i for i in range(20) if i % 2 != fold]
        co = collections.Counter()
        for i in train:
            o, b = O[i], B[i]
            for k, (p, s) in enumerate(o):
                j = round(k * (len(b) - 1) / max(1, len(o) - 1)) if len(o) > 1 else 0; co[(b[j], s)] += 1
        c = concordance(co)
        for it in range(2):
            co = collections.Counter()
            for i in train:
                for x, y in nw(O[i], B[i], lambda x, y: 2 if c.get(y) == x[1] else 0):
                    if x and y: co[(y, x[1])] += 1
            c = concordance(co)
        n = a = m = 0
        for i in test:
            for x, y in nw(O[i], B[i], lambda x, y: 2 if c.get(y) == x[1] else 0):
                if x and y:
                    n += 1
                    if y in c: m += 1; a += c[y] == x[1]
        out.append((fold, n, m, a)); print(f"held-out fold {fold}: test boxes aligned {n}, his code known from the training half {m}, concordant {a} = {a/max(1,m):.3f} of known, {a/max(1,n):.3f} of all")
    return out
if __name__ == '__main__': heldout()
