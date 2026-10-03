# GAPS25-na-suriname-map-1781 (account-4), 3 Oct 2026: apply prereg.md's rule to result.tsv (the one blind call).
# Writes decisions.tsv (every query) and appends 2077 exceptions to exceptions_nieuw_image.tsv (existing rows for the same
# token are replaced only if their grade is not C). Usage: python3 passes/signcmp_gaps25/apply.py [--dry]
import csv, sys
from collections import Counter, defaultdict
D = 'passes/signcmp_gaps25/'
import json
K = json.load(open(D + 'blind_key.json')); VAL = {r: v[1] for r, v in K.items()}
Q = {r['query']: r for r in csv.DictReader(open(D + 'queries_key.tsv'), delimiter='\t')}
R = {}
for r in csv.DictReader((l for l in open(D + 'result.tsv') if l.strip() and not l.startswith('#')), delimiter='\t'):
    R[r['query'].strip()] = r
def f(x):
    try: return float(x)
    except: return 0.0
dec = []
for q, k in Q.items():
    r = R.get(q)
    if r is None: dec.append((q, k, '', 0, '', 'missing')); continue
    b = r['best'].strip(); s = r['second'].strip(); bv = VAL.get(b); sv = VAL.get(s)
    settled = bv is not None and f(r['best_conf']) >= 0.6 and r['located'].strip() == 'sure' and (sv is None or sv != bv)
    dec.append((q, k, b, f(r['best_conf']), bv or 'NONE', 'settled' if settled else 'unsettled'))
cls = defaultdict(list)
for q, k, b, c, bv, st in dec:
    if st == 'settled': cls[k['reader_code']].append(bv)
moved = {}
for code, vs in cls.items():
    key = next(k['key_value'] for k in Q.values() if k['reader_code'] == code)
    v, n = Counter(vs).most_common(1)[0]
    if len(vs) >= 3 and v != key and n >= 2 * len(vs) / 3: moved[code] = v
ex = []
with open(D + 'decisions.tsv', 'w') as o:
    o.write('query\tline\tpos\treader_code\tkey_value\tbest\tbest_conf\tbest_value\tstatus\taction\n')
    for q, k, b, c, bv, st in dec:
        code, kv = k['reader_code'], k['key_value']; act = 'none'
        if code in moved:
            nv = moved[code]
            if st == 'settled' and bv == nv: act = f'{nv} H'
            elif st != 'settled': act = f'{nv} M'
        elif st == 'settled' and bv != kv: act = f'{bv} M'
        if act != 'none':
            v, g = act.split()
            why = (f"GAPS25 blind sign call (passes/signcmp_gaps25, prereg 12845ab7): {q} -> {b} ({bv}) {c:.2f}"
                   + (f"; class {code} moved to {moved[code]} by the 2/3 rule" if code in moved else "; class rule not met"))
            ex.append((k['line'], k['pos'], v, g, why))
        o.write(f"{q}\t{k['line']}\t{k['pos']}\t{code}\t{kv}\t{b}\t{c}\t{bv}\t{st}\t{act}\n")
print('settled per class:', {c: dict(Counter(v)) for c, v in cls.items()})
print('classes moved:', moved); print('exceptions:', len(ex))
if '--dry' in sys.argv: sys.exit(0)
EX = 'exceptions_nieuw_image.tsv'
lines = open(EX).read().splitlines()
keep = []; seen = {(l, str(p)) for l, p, *_ in ex}; skipped = 0
cgrade = set()
for ln in lines:
    p = ln.split('\t')
    if len(p) >= 4 and (p[0], p[1]) in seen:
        if p[3] == 'C': cgrade.add((p[0], p[1])); keep.append(ln); continue
        continue
    keep.append(ln)
for l, p, v, g, why in ex:
    if (l, str(p)) in cgrade: skipped += 1; continue
    keep.append(f'{l}\t{p}\t{v}\t{g}\t{why}')
open(EX, 'w').write('\n'.join(keep) + '\n')
print('written; skipped (C kept):', skipped)
