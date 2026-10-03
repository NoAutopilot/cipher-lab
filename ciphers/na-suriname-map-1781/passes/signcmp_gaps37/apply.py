# GAPS37-na-suriname-map-1781 (account-4), 3 Oct 2026: apply prereg.md's rule to result.tsv (the one blind same-hand
# g|l sorting call). Gate first on the four C-known tokens (#12 g; #22 #27 #28 l); then the per-instance rule on the
# other 42; writes decisions.tsv and appends 2077 exceptions (C rows never overwritten).
# Usage (from the target folder): python3 passes/signcmp_gaps37/apply.py [--dry]
import csv, sys
from collections import Counter
D = 'passes/signcmp_gaps37/'
Q = {r['query']: r for r in csv.DictReader(open(D + 'queries_key.tsv'), delimiter='\t')}
rows = [l for l in open(D + 'result.tsv') if l.strip() and not l.startswith('FORM') and '\t' in l]
R = {r['query'].strip(): r for r in csv.DictReader(rows, delimiter='\t')}
def f(x):
    try: return float(x)
    except: return 0.0
def ok(q):
    r = R.get(q); return r is not None and f(r['form_conf']) >= 0.6 and r['located'].strip() == 'sure'
form = {q: (R[q]['form'].strip() if q in R else '') for q in Q}
G, L = '#12', ['#22', '#27', '#28']
gate = all(ok(q) for q in [G] + L) and len({form[q] for q in L}) == 1 and form[G] != form[L[0]]
print('gate forms:', {q: (form[q], R.get(q, {}).get('form_conf'), R.get(q, {}).get('located')) for q in [G] + L})
print('gate', 'PASS' if gate else 'FAIL')
Fl, Fg = form[L[0]], form[G]
print('form counts (all 46):', dict(Counter(form.values())))
ex = []
with open(D + 'decisions.tsv', 'w') as o:
    o.write('query\tline\tpos\tknown_C\tform\tform_conf\tlocated\taction\n')
    for q, k in Q.items():
        r = R.get(q, {}); act = 'none'
        if gate and not k['known_C'] and ok(q):
            if form[q] == Fl: act = 'l H'
            elif form[q] == Fg: act = 'g H'
        if act != 'none':
            v, g = act.split()
            ex.append((k['line'], k['pos'], v, g, f"GAPS37 same-hand g|l sorting call (passes/signcmp_gaps37, prereg 34dbb366): {q} form {form[q]} {f(r.get('form_conf'))} = form of C-known {'L10:61/L12:26/L12:48 (l)' if v == 'l' else 'L06:4 (g)'}; gate PASS"))
        o.write(f"{q}\t{k['line']}\t{k['pos']}\t{k['known_C']}\t{form[q]}\t{r.get('form_conf', '')}\t{r.get('located', '')}\t{act}\n")
others = [q for q in Q if not Q[q]['known_C']]
print('42 others by form:', dict(Counter(form[q] for q in others)), 'settled:', sum(ok(q) for q in others))
print('exceptions:', len(ex), dict(Counter((e[2], e[3]) for e in ex)))
if '--dry' in sys.argv or not ex: sys.exit(0)
EX = 'exceptions_nieuw_image.tsv'
seen = {(l, str(p)) for l, p, *_ in ex}; keep, cg = [], set()
for ln in open(EX).read().splitlines():
    p = ln.split('\t')
    if len(p) >= 4 and (p[0], p[1]) in seen:
        if p[3] == 'C': cg.add((p[0], p[1])); keep.append(ln)
        continue
    keep.append(ln)
for l, p, v, g, why in ex:
    if (l, str(p)) not in cg: keep.append(f'{l}\t{p}\t{v}\t{g}\t{why}')
open(EX, 'w').write('\n'.join(keep) + '\n'); print('written')
