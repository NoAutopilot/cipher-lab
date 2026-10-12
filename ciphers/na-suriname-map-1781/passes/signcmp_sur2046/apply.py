# SUR-2046: apply the pre-registered rule (prereg.md) to result.tsv. Writes decisions.tsv; with --write, appends the 2046
# exception rows to exceptions_nieuw_image.tsv (only when the control gate passes).
import csv, json, sys
D = 'passes/signcmp_sur2046/'
key = json.load(open(D + 'blind_key.json'))
val = {lab: v for lab, (k, v, f, b) in key.items()}; nm = {lab: k for lab, (k, v, f, b) in key.items()}
q = {r['query']: r for r in csv.DictReader(open(D + 'queries_key.tsv'), delimiter='\t')}
res = {}
for r in csv.DictReader(open(D + 'result.tsv'), delimiter='\t'):
    r = {k.strip(): (v or '').strip() for k, v in r.items()}; qq = r['query'] if r['query'].startswith('#') else '#' + r['query']
    res[qq] = r
def V(lab): return 'NONE' if lab.upper() == 'NONE' else val.get(lab, '?')
def settled(r):
    try: bc = float(r['best_conf'])
    except ValueError: return False
    return bc >= 0.6 and r['located'] == 'sure' and (r['second'].upper() == 'NONE' or V(r['second']) != V(r['best']) or r['second'] == '')
rows = []; ctrl_ok = 0; nctrl = 0
for qq, m in q.items():
    r = res.get(qq)
    s = bool(r) and settled(r); bv = V(r['best']) if r else 'MISSING'
    if m['role'] == 'control':
        nctrl += 1; ok = s and bv == m['key_value']; ctrl_ok += ok
    rows.append((qq, m['line'], m['pos'], m['reader_code'], m['role'], m['key_value'], r['best'] if r else '', nm.get(r['best'], 'NONE') if r else '',
                 bv, r['best_conf'] if r else '', r['second'] if r else '', V(r['second']) if r else '', r['second_conf'] if r else '',
                 r['located'] if r else '', 'settled' if s else 'unsettled'))
gate = ctrl_ok >= 14
print(f'controls settled on key value: {ctrl_ok}/{nctrl}; gate >=14: {"PASS" if gate else "FAIL"}')
out = []
if gate:
    cls = {}
    for row in rows:
        if row[4] == 'target': cls.setdefault(row[3], []).append(row)
    for c, rs in sorted(cls.items()):
        st = [x for x in rs if x[14] == 'settled' and x[8] != 'NONE']
        vals = {x[8] for x in st}
        if len(rs) >= 2:
            okc = len(st) >= 2 / 3 * len(rs) and len(vals) == 1
        else:
            okc = len(st) == 1
        print(f'{c}: n={len(rs)} settled(non-NONE)={len(st)} values={sorted(vals)} -> {"RELABEL " + next(iter(vals)) if okc else "no change"}')
        if okc:
            for x in st: out.append(x)
# Reconciliation (worker's unit, may only withhold): control #30 (reader o, key r) was answered R_B6 (b) 0.75, runner-up
# R_Ro 0.15 -- the identical answer the three [o-flag] targets got, so the call does not separate [o-flag] from o here.
WITHHOLD = {'[o-flag]': 'control #30 (reader o, key r) got the identical R_B6 0.75 / R_Ro answer'}
for c, why in WITHHOLD.items():
    if any(x[3] == c for x in out): print(f'withheld by reconciliation: {c} ({why})')
out = [x for x in out if x[3] not in WITHHOLD]
print('relabels:', len(out))
ap = {x[0] for x in out}
with open(D + 'decisions.tsv', 'w') as f:
    f.write('query\tline\tpos\treader_code\trole\tkey_value\tbest\tbest_tile\tbest_value\tbest_conf\tsecond\tsecond_value\tsecond_conf\tlocated\tstate\tapplied\n')
    for row in sorted(rows, key=lambda r: (r[4], r[1], int(r[2]))): f.write('\t'.join(map(str, row)) + '\t' + ('yes' if row[0] in ap else ('withheld' if row[3] in WITHHOLD and row[14] == 'settled' else 'no')) + '\n')
if '--write' in sys.argv and gate and out:
    with open('exceptions_nieuw_image.tsv', 'a') as f:
        for x in out:
            f.write(f'{x[1]}\t{x[2]}\t{x[8]}\tM\tSUR-2046 blind sign call (passes/signcmp_sur2046, prereg 6b9676d75): reader {x[3]} = {x[7]} {x[9]}, runner-up {x[10]} ({x[11]}) {x[12]} ({x[0]}); controls {ctrl_ok}/{nctrl}\n')
