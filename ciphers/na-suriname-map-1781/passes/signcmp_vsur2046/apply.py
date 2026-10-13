# V-SUR2046: apply PREREG-V-SUR2046.md to result.tsv -> decisions.tsv. With --write, removes the CONTRADICTED / reverting rows
# from exceptions_nieuw_image.tsv (only when the gate passes). Run from the target folder.
import csv, json, sys
D = 'passes/signcmp_vsur2046/'
key = json.load(open(D + 'blind_key.json'))
val = {lab: v for lab, (k, v, f, b) in key.items()}; nm = {lab: k for lab, (k, v, f, b) in key.items()}
q = {r['query']: r for r in csv.DictReader(open(D + 'queries_key.tsv'), delimiter='\t')}
res = {}
for r in csv.DictReader(open(D + 'result.tsv'), delimiter='\t'):
    r = {k.strip(): (v or '').strip() for k, v in r.items()}; qq = r['query'] if r['query'].startswith('#') else '#' + r['query']
    res[qq] = r
def V(lab): return 'NONE' if lab.upper() in ('NONE', '') else val.get(lab, '?')
def settled(r):
    try: bc = float(r['best_conf'])
    except ValueError: return False
    return bc >= 0.6 and r['located'] == 'sure' and (r['second'].upper() in ('NONE', '') or V(r['second']) != V(r['best']))
rows = []
for qq, m in q.items():
    r = res.get(qq) or {'best': '', 'best_conf': '', 'second': '', 'second_conf': '', 'located': '', 'note': 'MISSING'}
    rows.append(dict(m, best=r['best'], tile=nm.get(r['best'], 'NONE'), bval=V(r['best']), conf=r['best_conf'], second=r['second'],
                     sval=V(r['second']), sconf=r['second_conf'], located=r['located'], st=settled(r), note=r.get('note', '')))
C = [x for x in rows if x['role'] == 'control']; T = [x for x in rows if x['role'] == 'target']
ok = sum(x['st'] and x['bval'] == x['value_to_test'] for x in C); gate = ok >= 14
print(f'controls settled on key value: {ok}/{len(C)}; gate >=14: {"PASS" if gate else "FAIL"}')
for x in C:
    if not (x['st'] and x['bval'] == x['value_to_test']):
        print(f"  control miss {x['query']} {x['reader_code']} key {x['value_to_test']}: {x['tile']} {x['conf']} {x['located']} ({'settled' if x['st'] else 'unsettled'})")
for x in T:
    v = x['value_to_test']
    if not gate: x['verdict'] = 'held-M-unconfirmed (control below gate)'
    elif x['st'] and x['bval'] == v:
        bad = [c['query'] for c in C if c['st'] and c['tile'] == x['tile'] and c['value_to_test'] != v]
        x['verdict'] = f'held-M-unconfirmed (look-alike withhold: {",".join(bad)})' if bad else 'CONFIRMED'
    elif x['st']: x['verdict'] = 'CONTRADICTED-revert-U'
    elif x['bval'] == v: x['verdict'] = 'held-M-unconfirmed (not reproduced, best value same)'
    else: x['verdict'] = 'revert-U (not reproduced, best value differs)'
    print(f"{x['query']} {x['line']}:{x['pos']} {x['reader_code']} v={v}: {x['tile']}({x['bval']}) {x['conf']} 2nd {x['sval']} {x['sconf']} {x['located']} -> {x['verdict']}")
cols = ['query', 'line', 'pos', 'reader_code', 'role', 'value_to_test', 'best', 'tile', 'bval', 'conf', 'second', 'sval', 'sconf', 'located', 'st', 'verdict', 'note']
with open(D + 'decisions.tsv', 'w') as f:
    f.write('\t'.join(cols) + '\n')
    for x in sorted(rows, key=lambda r: (r['role'], r['line'], int(r['pos']))): f.write('\t'.join(str(x.get(c, '')) for c in cols) + '\n')
rev = {(x['line'], x['pos']) for x in T if 'revert' in x['verdict'].lower()}
print('revert:', sorted(rev))
if '--write' in sys.argv and gate and rev:
    L = open('exceptions_nieuw_image.tsv').read().split('\n'); out = []
    for l in L:
        p = l.split('\t')
        if len(p) > 4 and (p[0], p[1]) in rev and 'SUR-2046 blind sign call' in p[4]: continue
        out.append(l)
    open('exceptions_nieuw_image.tsv', 'w').write('\n'.join(out))
