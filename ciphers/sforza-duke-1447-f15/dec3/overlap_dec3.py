"""SFZ-DEC3 (14 Oct 2026): sign-stock overlap of a scat. 1597 key with the Duke's slips f.5+f.8 (no decode).
Statistic: coverage = share of the Duke's f.5+f.8 tokens (duke_labels.md labels; N7 and '?' dropped) whose label is in the key's stock.
Nulls: (1) the stocks of the 12 other 1597 keys already read blind by SFZ-R5323 (r5323/ctl_*.tsv, passA/passB_5323.tsv);
(2) 10,000 random stocks of the same size drawn from the duke_labels.md label table (seed 5350) -- this null CAN differ from the
target, since it changes which labels are in the stock, the thing coverage depends on. Usage: python3 overlap_dec3.py"""
import glob, os, random, re
H = os.path.dirname(os.path.abspath(__file__)); DUKE = os.path.join(H, '../../sforza-italien1584-1447/duke')
toks = []
for f in ('ciphertext_f5.tsv', 'ciphertext_f8.tsv'):
    for line in open(os.path.join(DUKE, f)):
        if line.startswith('#') or '\t' not in line: continue
        toks += [t.rstrip('^') for t in line.split('\t', 1)[1].split() if t not in ('N7', '?') and '/' not in t]
tab = open(os.path.join(DUKE, 'duke_labels.md')).read().split('| label | shape |')[1].split('\n\n')[0]
labels = sorted(set(re.findall(r'^\| ([^|]+?) \|', tab, re.M)) - {'---'})
pool = sorted({x for l in labels for x in l.split()})
def stock_tsv(p):
    s = set()
    for line in open(p):
        if line.startswith('#') or '\t' not in line: continue
        s |= {x.rstrip('^').rstrip('?') for x in line.split('\t', 1)[1].split()}
    return s & set(pool)
cov = lambda s: sum(t in s for t in toks) / len(toks)
tgt = set(l.split('\t')[0] for l in open(os.path.join(H, 'stock_r5350.tsv')) if not l.startswith('//') and not l.startswith('label'))
print(f'Duke tokens {len(toks)}, label pool {len(pool)}')
print(f'R5350 stock {len(tgt)} labels {sorted(tgt)}: coverage {cov(tgt):.3f}')
for p in sorted(glob.glob(os.path.join(H, '../r5323/*_53*.tsv'))):
    s = stock_tsv(p); print(f'{os.path.basename(p):18s} stock {len(s):2d}: coverage {cov(s):.3f}')
rng = random.Random(5350); null = sorted(cov(set(rng.sample(pool, len(tgt)))) for _ in range(10000))
ge = sum(x >= cov(tgt) for x in null)
print(f'random {len(tgt)}-label stocks: mean {sum(null)/len(null):.3f}, p95 {null[9499]:.3f}; P(>= R5350) = {ge/10000:.4f}')
