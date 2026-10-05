#!/usr/bin/env python3
"""D2-C1161PRU shape test (pru/PREREG_pruneaux.md): fr.3281 f.4 Des Pruneaux key vs key.tsv. Exit 0 always; prints result."""
import csv, random, os
D = os.path.dirname(os.path.abspath(__file__))
key = {r['sign']: r['value'] for r in csv.DictReader(open(os.path.join(D, '..', 'key.tsv')), delimiter='\t')}
cells = [(r['label'], set(r['fr3281_letters'].split(','))) for r in csv.DictReader(open(os.path.join(D, 'cells.tsv')), delimiter='\t')]
cells = [(l, s) for l, s in cells if l in key]
vals = [key[l] for l, _ in cells]
obs = sum(key[l] in s for l, s in cells)
rng = random.Random(1); null = []
for _ in range(10000):
    v = vals[:]; rng.shuffle(v); null.append(sum(x in s for x, (_, s) in zip(v, cells)))
null.sort(); p99 = null[int(0.99 * len(null)) - 1]; mean = sum(null) / len(null)
pge = sum(n >= obs for n in null) / len(null)
for l, s in cells: print(f"{l}\t{','.join(sorted(s))}\t{key[l]}\t{'HIT' if key[l] in s else ''}")
fit = obs > p99 and obs >= 4
print(f"# cells {len(cells)}; obs {obs}; null mean {mean:.2f}, p99 {p99}, P(null>=obs) {pge:.4f} -> {'FIT' if fit else 'NO FIT'}")
