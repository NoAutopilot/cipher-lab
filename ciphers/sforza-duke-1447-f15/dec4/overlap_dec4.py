"""SFZ-DEC4 (14 Oct 2026): SFZ-DEC3's sign-stock overlap test (dec3/overlap_dec3.py, same statistic, same null) on DECODE R5398.
Statistic: share of the Duke's f.5+f.8 tokens (duke_labels.md labels; N7 and '?' dropped) whose label is in the key's stock.
Null: 10,000 random stocks of the same size from the duke_labels.md label pool (seed 5398); it changes which labels are in the
stock, the thing coverage counts, so it can differ from the target. Run for the full stock and the firm-only stock.
Usage: python3 dec4/overlap_dec4.py"""
import os, random, re
H = os.path.dirname(os.path.abspath(__file__)); DUKE = os.path.join(H, '../../sforza-italien1584-1447/duke')
toks = []
for f in ('ciphertext_f5.tsv', 'ciphertext_f8.tsv'):
    for line in open(os.path.join(DUKE, f)):
        if line.startswith('#') or '\t' not in line: continue
        toks += [t.rstrip('^') for t in line.split('\t', 1)[1].split() if t not in ('N7', '?') and '/' not in t]
tab = open(os.path.join(DUKE, 'duke_labels.md')).read().split('| label | shape |')[1].split('\n\n')[0]
labels = sorted(set(re.findall(r'^\| ([^|]+?) \|', tab, re.M)) - {'---'})
pool = sorted({x for l in labels for x in l.split()})
cov = lambda s: sum(t in s for t in toks) / len(toks)
rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(H, 'stock_r5398.tsv')) if not l.startswith('//') and not l.startswith('label')]
assert all(r[0] in pool for r in rows), [r[0] for r in rows if r[0] not in pool]
print(f'Duke tokens {len(toks)}, label pool {len(pool)}')
for name, stock in (('full', {r[0] for r in rows}), ('firm', {r[0] for r in rows if r[1] == '1'})):
    c = cov(stock); rng = random.Random(5398); null = sorted(cov(set(rng.sample(pool, len(stock)))) for _ in range(10000))
    print(f'R5398 {name} stock {len(stock)} labels {sorted(stock)}: coverage {c:.3f}; random {len(stock)}-label stocks mean '
          f'{sum(null)/len(null):.3f}, p95 {null[9499]:.3f}; P(>= R5398) = {sum(x >= c for x in null)/10000:.4f}')
