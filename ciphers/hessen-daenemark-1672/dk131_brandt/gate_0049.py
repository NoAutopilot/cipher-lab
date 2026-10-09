"""BRANDT-GATE test 2 (PREREG-BRANDT-GATE.md, pushed 13865ab70 before 0049 was fetched or read): key_0020.tsv's single-letter
values applied to ciphertext_0049.tsv's glossed groups; score = groups whose key letter equals the period gloss letter, against
2000 random permutations of key_0020's value->letter assignments (seed 20261009). Gate: real > control p99. Not-a-test < 10
scorable. Also prints the sensitivity score without the 8 groups HDK-131 had already written into NOTES.md, and per-value rows."""
import csv, random, collections
FOLD = str.maketrans({'ä': 'a', 'ö': 'o', 'ü': 'u', 'j': 'i', 'v': 'u', 'y': 'i'})
def fold(s): return s.strip().lower().translate(FOLD)
key = {}
for r in csv.DictReader(open('key_0020.tsv'), delimiter='\t'):
    m = fold(r['meaning'])
    if len(m) == 1: key[r['value']] = m
rows = [r for r in csv.DictReader((l for l in open('ciphertext_0049.tsv') if not l.startswith('#')), delimiter='\t')]
data = []
for r in rows:
    g = fold(r['gloss'])
    if r['value'].isdigit() and len(g) == 1 and g.isalpha() and r['value'] in key:
        data.append((r['line'], r['pos'], r['value'], g))
def score(k, d): return sum(1 for _, _, v, g in d if k[v] == g)
N = 2000; rng = random.Random(20261009); vals = sorted(key); lets = [key[v] for v in vals]
def run(d, tag):
    real = score(key, d); c = []
    for _ in range(N):
        p = lets[:]; rng.shuffle(p); c.append(score(dict(zip(vals, p)), d))
    c.sort(); p99 = c[int(.99 * N)]
    nt = len(d) < 10
    print('%s: scorable %d; real %d; control mean %.2f, p99 %d, max %d, n %d; p = %.4f; gate %s' % (tag, len(d), real,
          sum(c) / N, p99, c[-1], N, (1 + sum(x >= real for x in c)) / (N + 1),
          'NOT-A-TEST' if nt else ('PASS' if real > p99 else 'FAIL')))
run(data, 'TEST2 0049 held-out letters')
seen = {('s49_L01', str(i)) for i in range(1, 9)}
run([x for x in data if (x[0], x[1]) not in seen], 'SENSITIVITY without HDK-131 8 groups (not the gate)')
print('unscorable glossed groups (value not single-letter keyed):',
      ' '.join('%s=%s' % (r['value'], fold(r['gloss'])) for r in rows if len(fold(r['gloss'])) == 1 and fold(r['gloss']).isalpha() and r['value'] not in key))
per = collections.defaultdict(list)
for _, _, v, g in data: per[v].append(g)
print('value\tkey0020\tgloss0049\tagree')
for v in sorted(per, key=int): print('%s\t%s\t%s\t%d/%d' % (v, key[v], ','.join(per[v]), sum(g == key[v] for g in per[v]), len(per[v])))
