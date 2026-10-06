#!/usr/bin/env python3
"""AVS53, 3 Oct 2026: key_53 dictionary regrade of letter 53's M tokens, rule as pre-registered in prereg_avs53.md
(committed before this script was run). Writes regrade_53.tsv (one row per eligible token) and prints the aggregate
gate. --check exits 1 if the committed regrade_53.tsv is stale. Run from anywhere."""
import gzip, os, random, re, sys, unicodedata
from collections import Counter
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(D, '..', '..')
def tsv(p): return [l.rstrip('\n').split('\t') for l in open(os.path.join(D, p)) if not l.startswith('#')]
def fold(w):
    w = unicodedata.normalize('NFD', w.lower()); w = ''.join(c for c in w if c.isalpha() and ord(c) < 128)
    return w.replace('uu', 'w').replace('v', 'u').replace('j', 'i').replace('y', 'i')
def words(t): return [fold(x) for x in re.findall(r'[^\W\d_]+', t)]
dc = Counter()
for f in sorted(os.listdir(os.path.join(R, 'tools/data/de17'))):
    if f.endswith('.txt.gz'): dc.update(words(gzip.open(os.path.join(R, 'tools/data/de17', f), 'rt', errors='ignore').read()))
DICT = {w for w, n in dc.items() if n >= 2}
for f in ('align_74.txt', 'align_124.txt'):
    for l in open(os.path.join(D, f)):
        if l.startswith('#'): continue
        for e in l.split(';;'):
            if '|' in e: DICT.add(fold(''.join(e.split('|', 1)[1].split())))
for f in ('plaintext_74.txt', 'plaintext_98.txt'):
    DICT.update(words(''.join(l for l in open(os.path.join(D, f)) if not l.startswith('#'))))
DICT.discard('')
def indict(u): return u in DICT or any(u[:i] in DICT and u[i:] in DICT for i in range(3, len(u) - 2))
key = {r[0]: r[1] for r in tsv('key_53.tsv')[1:]}; n = {r[0]: int(r[4].split(';')[0][2:]) for r in tsv('key_53.tsv')[1:]}
exc = {(r[0], int(r[1])): r[2] for r in tsv('exceptions_53_s1.tsv')[1:] if 'AVS53' not in r[4]}
ct = tsv('ciphertext_53_s1.tsv')[1:]
alt = {(r[0], int(r[1])): r[4].split(':')[-1] for r in tsv('recon53/ciphertext_draft.tsv')[1:]}
# units: DOT-delimited, across line ends (a line end is not a separator, as in reading_53.txt)
units, cur = [], []
for r in ct:
    if r[2] == 'DOT':
        if cur: units.append(cur); cur = []
    elif r[2] != 'COL': cur.append(r)
if cur: units.append(cur)
def dec(u, k, sub=None):
    return fold(''.join(exc.get((r[0], int(r[1])), (k.get(sub[1], '?') if sub and sub[0] is r else k.get(r[2], '?'))) for r in u))
signs = sorted(key, key=lambda s: -n[s]); bands = [signs[i:i + 5] for i in range(0, 20, 5)]
rng = random.Random(53); draws = []
for _ in range(1000):
    k = {}
    for b in bands:
        v = [key[s] for s in b]; rng.shuffle(v); k.update(zip(b, v))
    draws.append(k)
real = [indict(dec(u, key)) for u in units]
ctrl_unit = [sum(indict(dec(u, k)) for k in draws) / 1000 for u in units]
agg = sum(real) / len(units); cagg = sorted(sum(indict(dec(u, k)) for u in units) / len(units) for k in draws)
p99 = cagg[989]; gate1 = agg > p99
out = ['line\tpos\tsign\tvalue\tunit\tin_dict\tctrl_rate\tdiffer_alt\talt_in_dict\tmove\twhy']
for ui, u in enumerate(units):
    for r in u:
        if r[3] != 'M' or r[2] not in key: continue
        why = r[4]; a = ''; aind = ''
        if why.startswith('differ'):
            # recon draft positions differ from settled positions only after settle_53.py drops; use the same line/pos
            a = alt.get((r[0], int(r[1])), '')
            a = a if a in key and a != r[2] else ''
            aind = str(indict(dec(u, key, (r, a)))) if a else ''
        mv = gate1 and real[ui] and ctrl_unit[ui] <= 0.05 and aind != 'True'
        out.append('\t'.join([r[0], r[1], r[2], key[r[2]], dec(u, key), str(real[ui]), f'{ctrl_unit[ui]:.3f}', a, aind,
                              'S' if mv else 'M', why]))
txt = '\n'.join(out) + '\n'
summary = (f'units {len(units)}; in-dict under key_53 {sum(real)} ({agg:.3f}); control mean {sum(cagg)/1000:.3f}, '
           f'p99 {p99:.3f}, max {cagg[-1]:.3f}; gate1 {"PASS" if gate1 else "FAIL"}; eligible {len(out)-1}; '
           f'move {sum(1 for l in out[1:] if l.split(chr(9))[9]=="S")}; dict types {len(DICT)}')
p = os.path.join(D, 'regrade_53.tsv')
if __name__ == '__main__':
    if '--check' in sys.argv:
        print(summary); sys.exit(0 if open(p).read() == txt else 1)
    open(p, 'w').write(txt); print(summary)
