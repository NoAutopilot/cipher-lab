"""FAM-COSCREM score (PREREG-COSCREM.md): R1166 C labels vs Cremonini n.1 rows matched blind; permuted-row-value null.
Usage: python3 coscrem_score.py  (from align/). Writes coscrem_score.tsv; exits 1 if the committed tsv is stale."""
import csv, random, sys, os
H = os.path.dirname(os.path.abspath(__file__))
vals = {r['row']: r['plain'].split()[0] for r in csv.DictReader(open(os.path.join(H, '../images/cremonini_n1/n1_values_worker.tsv')), delimiter='\t')
        if not r['signs as read by FAM-COSCREM from the 150 ppi plate (M: a 19th-c hand at about 13 px per row)'].startswith('(none)')}
key = {r['sign']: (r['value'], r['grade']) for r in csv.DictReader(open(os.path.join(H, 'key_n9cos2.tsv')), delimiter='\t')}
match = {r['ref']: r['match'].split(':')[0] for r in csv.DictReader(open(os.path.join(H, 'coscrem_match.tsv')), delimiter='\t')}
C = [s for s in ['+','T','a','b','c','d','g','o','y','z','W'] if key[s][1] == 'C']
def hits(v): return sum(1 for s in C if match.get(s) in v and v[match[s]] == key[s][0])
real = hits(vals)
rows, letters = list(vals), list(vals.values())
rng = random.Random(1); null = []
for _ in range(1000):
    rng.shuffle(letters); null.append(hits(dict(zip(rows, letters))))
null.sort(); mean = sum(null)/len(null); p95 = null[949]
verdict = 'PASS' if real >= 3 and real > p95 else 'FAIL'
lines = ['label\tour_value\tgrade\tn1_row\tn1_value\thit']
for s in ['+','T','a','b','c','d','g','o','y','z','W','4','8','L','TT','Z','q','x']:
    m = match.get(s, 'none'); lines.append(f"{s}\t{key[s][0]}\t{key[s][1]}\t{m}\t{vals.get(m,'-')}\t{int(s in C and vals.get(m)==key[s][0])}")
lines.append(f"# C labels {len(C)}; hits {real}; null mean {mean:.3f}; null p95 {p95}; {verdict}")
out = '\n'.join(lines) + '\n'; p = os.path.join(H, 'coscrem_score.tsv')
if '--check' in sys.argv:
    sys.exit(0 if open(p).read() == out else 1)
open(p, 'w').write(out); print(out)
