# GAPS29-na-suriname-map-1781 (account-4), 3 Oct 2026: apply prereg.md's rule to result.tsv (the one blind g|l call).
# Partner calibration gate first; then the g class rule; writes decisions.tsv and appends 2077 exceptions to
# exceptions_nieuw_image.tsv (existing rows for the same token replaced unless grade C). Usage: python3 passes/signcmp_gaps29/apply.py [--dry]
import csv, sys, json
from collections import Counter
D = 'passes/signcmp_gaps29/'
K = json.load(open(D + 'blind_key.json')); VAL = {r: v[1] for r, v in K.items()}
Q = {r['query']: r for r in csv.DictReader(open(D + 'queries_key.tsv'), delimiter='\t')}
R = {r['query'].strip(): r for r in csv.DictReader((l for l in open(D + 'result.tsv') if l.strip()), delimiter='\t')}
def f(x):
    try: return float(x)
    except: return 0.0
KEYV = {'g': 'g|l', 'c': 'l', '[u-dots]': 'n'}
dec = {}
for q, k in Q.items():
    r = R.get(q)
    if r is None: dec[q] = ('', 0.0, 'NONE', 'missing'); continue
    b, s = r['best'].strip(), r['second'].strip(); bv, sv = VAL.get(b), VAL.get(s)
    ok = bv is not None and f(r['best_conf']) >= 0.6 and r['located'].strip() == 'sure' and (sv is None or sv != bv)
    dec[q] = (b, f(r['best_conf']), bv or 'NONE', 'settled' if ok else 'unsettled')
part = [q for q, k in Q.items() if k['reader_code'] != 'g']
p_ok = sum(dec[q][3] == 'settled' and dec[q][2] == KEYV[Q[q]['reader_code']] for q in part)
gate = p_ok >= 2 * len(part) / 3
print(f'partners settled on key value: {p_ok}/{len(part)} -> gate', 'PASS' if gate else 'FAIL')
gs = [dec[q][2] for q in Q if Q[q]['reader_code'] == 'g' and dec[q][3] == 'settled']
gin = [v for v in gs if v in ('g', 'l')]
print('g settled:', dict(Counter(gs)))
mode, moved = None, None
if gin:
    v, n = Counter(gin).most_common(1)[0]
    if len(gin) >= 3 and n >= 2 * len(gin) / 3: mode, moved = 'class', v
    else: mode = 'mix'
print('g mode:', mode, moved)
ex = []
with open(D + 'decisions.tsv', 'w') as o:
    o.write('query\tline\tpos\treader_code\tkey_value\tbest\tbest_conf\tbest_value\tstatus\taction\n')
    for q, k in Q.items():
        b, c, bv, st = dec[q]; code = k['reader_code']; act = 'none'
        if code == 'g' and gate:
            if mode == 'class':
                if st == 'settled' and bv == moved: act = f'{moved} H'
                elif st == 'settled' and bv in ('g', 'l'): act = f'{bv} M'
                elif st != 'settled': act = f'{moved} M'
            elif mode == 'mix' and st == 'settled' and bv in ('g', 'l'): act = f'{bv} H'
        elif code != 'g' and st == 'settled' and bv != KEYV[code]: act = f'{bv} M'
        if act != 'none':
            v, g = act.split()
            ex.append((k['line'], k['pos'], v, g, f"GAPS29 blind g|l sign call (passes/signcmp_gaps29, prereg e8726900): {q} -> {b} ({bv}) {c:.2f}; mode {mode}"))
        o.write(f"{q}\t{k['line']}\t{k['pos']}\t{code}\t{KEYV[code]}\t{b}\t{c}\t{bv}\t{st}\t{act}\n")
print('exceptions:', len(ex), dict(Counter((e[2], e[3]) for e in ex)))
if '--dry' in sys.argv: sys.exit(0)
EX = 'exceptions_nieuw_image.tsv'
seen = {(l, str(p)) for l, p, *_ in ex}; keep, cg = [], set()
for ln in open(EX).read().splitlines():
    p = ln.split('\t')
    if len(p) >= 4 and (p[0], p[1]) in seen:
        if p[3] == 'C': cg.add((p[0], p[1])); keep.append(ln)
        continue
    keep.append(ln)
sk = 0
for l, p, v, g, why in ex:
    if (l, str(p)) in cg: sk += 1; continue
    keep.append(f'{l}\t{p}\t{v}\t{g}\t{why}')
open(EX, 'w').write('\n'.join(keep) + '\n'); print('written; skipped (C kept):', sk)
