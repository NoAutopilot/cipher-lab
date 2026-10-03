# GAPS45-na-suriname-map-1781 (account-4), 3 Oct 2026: apply prereg.md to result.tsv (one blind same-hand n|m sorting call).
# Gate first on the 15 plain-letter references (m 4, n 6, y-dots 5, with leave-one-out); then the rule on the 17 [u-dots].
# Usage (from the target folder): python3 passes/signcmp_gaps45/apply.py [--dry]
import csv, sys
from collections import Counter
D = 'passes/signcmp_gaps45/'
Q = {r['query']: r for r in csv.DictReader(open(D + 'queries_key.tsv'), delimiter='\t')}
rows = [l for l in open(D + 'result.tsv') if l.strip() and not l.startswith('FORM') and '\t' in l]
R = {r['query'].strip(): r for r in csv.DictReader(rows, delimiter='\t')}
def f(x):
    try: return float(x)
    except: return 0.0
def ok(q):
    r = R.get(q); return r is not None and f(r['form_conf']) >= 0.6 and r['located'].strip() == 'sure'
form = {q: (R[q]['form'].strip() if q in R else '') for q in Q}
refs = {c: [q for q in Q if Q[q]['class'] == 'ref-' + c] for c in ('m', 'n', 'y-dots')}
def classform(qs):
    s = {form[q] for q in qs}; return s.pop() if len(s) == 1 else None
def gate_on(excl=None):
    rf = {c: [q for q in qs if q != excl] for c, qs in refs.items()}
    Fm, Fn, Fy = classform(rf['m']), classform(rf['n']), classform(rf['y-dots'])
    return Fm is not None and Fn is not None and Fy is not None and Fn != Fm and Fy != Fm, (Fm, Fn, Fy)
allref = [q for qs in refs.values() for q in qs]
g_main, (Fm, Fn, Fy) = gate_on()
g_ok = all(ok(q) for q in allref)
loo = all(gate_on(q)[0] and form[q] == {'ref-m': Fm, 'ref-n': Fn, 'ref-y-dots': Fy}[Q[q]['class']] for q in allref)
gate = g_main and g_ok and loo
print('ref forms:', {c: [(q, form[q], R.get(q, {}).get('form_conf'), R.get(q, {}).get('located')) for q in qs] for c, qs in refs.items()})
print(f'gate (a) {g_ok} (b-d) {g_main} {(Fm, Fn, Fy)} LOO {loo} ->', 'PASS' if gate else 'FAIL')
cq = [q for q in Q if Q[q]['class'] == 'cipher']
print('cipher by form:', dict(Counter(form[q] for q in cq)), 'mark_above:', dict(Counter(R.get(q, {}).get('mark_above', '').strip() for q in cq)))
ex = []; other = 0
with open(D + 'decisions.tsv', 'w') as o:
    o.write('query\tline\tpos\tclass\tform\tform_conf\tlocated\tmark_above\taction\n')
    for q, k in Q.items():
        r = R.get(q, {}); act = 'none'
        if gate and k['class'] == 'cipher' and ok(q):
            if form[q] == Fm: act = 'm H'
            elif form[q] in (Fn, Fy): act = 'n H(kept)'
            else: other += 1
        if act == 'm H':
            ex.append((k['line'], k['pos'], 'm', 'H', f"GAPS45 same-hand n|m sorting call (passes/signcmp_gaps45, prereg): {q} form {form[q]} {f(r.get('form_conf'))} = form of the 4 plain m refs; gate PASS"))
        o.write(f"{q}\t{k['line']}\t{k['pos']}\t{k['class']}\t{form[q]}\t{r.get('form_conf', '')}\t{r.get('located', '')}\t{r.get('mark_above', '')}\t{act}\n")
nonres = gate and sum(1 for q in cq if form[q] not in (Fm, Fn, Fy)) >= 12
print('cipher-only form count:', sum(1 for q in cq if form[q] not in (Fm, Fn, Fy)), 'NON-RESULT' if nonres else '')
print('exceptions:', len(ex))
if '--dry' in sys.argv or not ex or nonres: sys.exit(0)
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
