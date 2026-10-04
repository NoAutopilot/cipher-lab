#!/usr/bin/env python3
"""NOX-ALN step 3 (exploratory, PREREG.md): rank owner piles by expected change to the reading and pick <= 3 piles + 40 tiles.
score(pile) = aligned train tiles off the pile's modal letter (results/target_after_counts.tsv) x reader mix, where reader mix =
share of the pile's reader-agreed signs (NOX-OWNERSORT placement P2) whose label is a different letter from the pile majority;
'?' labels are not counted as a letter (neither side); piles with < 8 letter-labelled agreed signs are not eligible as piles.
Writes next_targets.tsv and targets.json here. Run from this folder after `nox_aln.py target`."""
import csv, json, sys
from collections import Counter, defaultdict
sys.path.insert(0, '../nox')
import nox_ownersort as no

p1, p2 = no.placements()
ag = {t: l for t, l in no.agreed(p2).items() if no.owner[t] != 'BAD-CUT' and not l.startswith('?')}
byp = defaultdict(Counter)
for t, l in ag.items():
    byp[no.owner[t]][l] += 1
off = {}
for r in csv.DictReader(open('results/target_after_counts.tsv'), delimiter='\t'):
    c = {k: int(v) for k, v in r.items() if k != 'pile'}
    n = sum(c.values())
    m = max(c, key=c.get)
    off[r['pile']] = (n - c[m], n, m)
piles = []
for p, c in byp.items():
    n = sum(c.values())
    maj = c.most_common(1)[0][0]
    mix = sum(v for l, v in c.items() if no.differ(l, maj)) / n
    o, na, ml = off.get(p, (0, 0, '-'))
    piles.append(dict(pile=p, score=round(o * mix, 1), off=o, aligned=na, n_agreed=n, mix=round(mix, 2),
                      readers=' / '.join(f'{l}:{v}' for l, v in c.most_common(3)), eligible=n >= 8))
piles.sort(key=lambda d: -d['score'])
# NOX-ALN finding (exploratory): owner labels + merge k014->k077 make the aligner lock on (results/full_pair_k014_k077.json);
# whether the two piles are one sign is the single question that changes the reading most, so it leads, ahead of the score.
LOCK = dict(pile='k014+k077', score='lock-on', off='-', aligned='-', n_agreed='-', mix='-', eligible=True,
            readers='c262 provisional k014 i2 (6), k077 o1/e2 (2)')
chosen = [LOCK] + [d for d in piles if d['eligible']][:2]
rank = {d['pile']: d['score'] for d in piles}
old = [r for r in csv.DictReader((l for l in open('../nox/next_targets.tsv') if not l.startswith('#')), delimiter='\t')
       if r['kind'] == 'tile']
cp = ['k014', 'k077'] + [d['pile'] for d in chosen[1:]]
old.sort(key=lambda r: (r['pile'] not in cp, cp.index(r['pile']) if r['pile'] in cp else 0, -rank.get(r['pile'], 0)))
tiles = old[:40]
with open('next_targets.tsv', 'w') as f:
    f.write('# NOX-ALN step 3 (exploratory): at most 3 piles + 40 tiles ranked by expected change to the reading. No reading is claimed.\n')
    f.write('rank\tkind\tid\tpile\tscore\twhy\n')
    for i, d in enumerate(chosen, 1):
        if d is LOCK:
            f.write(f"{i}\tpile\tk014+k077\tk014\tlock-on\tcompare k014 (103 tiles) with k077 (112): merged into one, the owner's labels let the "
                    "aligner lock on (held-out 0.63 vs null p99 ~0.39); separate, it fails (0.355). Same sign -> merge; different -> say so, "
                    "the lock-on is then a search effect to explain\n")
            continue
        f.write(f"{i}\tpile\t{d['pile']}\t{d['pile']}\t{d['score']}\tsplit it: readers' agreed signs {d['readers']} "
                f"(mix {d['mix']}); {d['off']} of its {d['aligned']} aligned train tiles fall off its modal letter\n")
    for i, r in enumerate(tiles, 1):
        f.write(f"{i}\ttile\t{r['id']}\t{r['pile']}\t{rank.get(r['pile'], 0)}\tmove it out of {r['pile']}: {r['why'].split(';')[0]}\n")
def sids(p):
    return sorted(t for t in no.owner if no.owner[t] in p.split('+'))
json.dump(dict(note='NOX-ALN 4 Oct 2026: <=3 piles + 40 tiles for the owner; pile sids are every tile now in that owner pile',
               piles=[dict(pile=d['pile'], score=d['score'], readers=d['readers'], off=d['off'], aligned=d['aligned'],
                           sids=sids(d['pile'])) for d in chosen],
               tiles=[dict(sid=r['id'], pile=r['pile'], why=r['why'].split(';')[0]) for r in tiles],
               top_piles_all=piles[:10]), open('targets.json', 'w'), indent=1)
for d in piles[:8]:
    print(d)
print('chosen', cp, 'tiles', Counter(r['pile'] for r in tiles))
