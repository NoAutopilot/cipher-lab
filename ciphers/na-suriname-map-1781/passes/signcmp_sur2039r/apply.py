# SUR-2039R: apply PREREG-SUR-2039R.md (pushed 691b7d363) to result.tsv -> decisions.tsv. With --write (gate PASS only), appends
# the licensed 2039_rem_* rows to exceptions_nieuw_image.tsv. Run from the target folder.
import csv, json, math, sys
D = 'passes/signcmp_sur2039r/'
key = json.load(open(D + 'blind_key.json'))
val = {lab: v for lab, (k, v, f, b) in key.items()}; nm = {lab: k for lab, (k, v, f, b) in key.items()}
q = {r['query']: r for r in csv.DictReader(open(D + 'queries_key.tsv'), delimiter='\t')}
res = {}
for r in csv.DictReader(open(D + 'result.tsv'), delimiter='\t'):
    r = {k.strip(): (v or '').strip() for k, v in r.items()}; qq = r['query'] if r['query'].startswith('#') else '#' + r['query']
    res[qq] = r
def V(lab): return 'NONE' if lab.upper() in ('NONE', '') else val.get(lab, '?')
def fl(s):
    try: return float(s)
    except ValueError: return 0.0
def settled(r):
    return fl(r['best_conf']) >= 0.6 and r['located'] == 'sure' and (r['second'].upper() in ('NONE', '') or V(r['second']) != V(r['best']))
rows = []
for qq, m in q.items():
    r = res.get(qq) or {'best': '', 'best_conf': '', 'second': '', 'second_conf': '', 'located': '', 'note': 'MISSING'}
    rows.append(dict(m, best=r['best'], tile=nm.get(r['best'], 'NONE'), bval=V(r['best']), conf=r['best_conf'], second=r['second'],
                     sval=V(r['second']), sconf=r['second_conf'], located=r['located'], st=settled(r), note=r.get('note', '')))
C = [x for x in rows if x['role'] == 'control']; T = [x for x in rows if x['role'] == 'target']
ok = sum(x['st'] and x['bval'] == x['key_value'] for x in C); gate = ok >= 14
print(f'controls settled on key value: {ok}/{len(C)}; gate >=14: {"PASS" if gate else "FAIL"}')
for x in C:
    if not (x['st'] and x['bval'] == x['key_value']):
        print(f"  control miss {x['query']} {x['reader_code']} key {x['key_value']}: {x['tile']}({x['bval']}) {x['conf']} {x['located']} ({'settled' if x['st'] else 'unsettled'})")
for x in sorted(T, key=lambda x: (x['reader_code'], x['line'], int(x['pos']))):
    print(f"  target {x['query']} {x['line']}:{x['pos']} {x['reader_code']}: {x['tile']}({x['bval']}) {x['conf']} 2nd {x['sval']} {x['sconf']} {x['located']} {'settled' if x['st'] else 'unsettled'}")
new = []
for cls in sorted({x['reader_code'] for x in T}):
    I = [x for x in T if x['reader_code'] == cls]; St = [x for x in I if x['st']]; need = math.ceil(2 * len(I) / 3)
    vals = {x['bval'] for x in St}
    if not gate: verdict = 'non-test (controls below gate)'
    elif vals == {'NONE'} and len(St) >= need: verdict = 'stays U: not on the sheet per the call'
    elif len(St) < need: verdict = f'stays U: {len(St)}/{len(I)} settled, need {need}'
    elif len(vals) != 1: verdict = f'stays U: settled values disagree {sorted(vals)}'
    else:
        v = vals.pop(); tiles = {x['tile'] for x in St}
        bad = sorted({c['query'] + ' ' + c['reader_code'] for c in C if c['st'] and c['tile'] in tiles and c['key_value'] != v})
        if bad: verdict = f'stays U: look-alike withhold ({", ".join(bad)} settle on the same tile)'
        else:
            g = 'H' if ok >= 18 and len(St) == len(I) and all(fl(x['conf']) >= 0.7 for x in I) else 'M'
            verdict = f'relabel settled -> {v} ({g})'
            for x in St: new.append((x, v, g))
    for x in I: x['verdict'] = verdict if x['st'] or 'relabel' not in verdict else 'stays U: unsettled instance of a relabelled class'
    print(f'class {cls}: {verdict}')
cols = ['query', 'line', 'pos', 'reader_code', 'role', 'key_value', 'best', 'tile', 'bval', 'conf', 'second', 'sval', 'sconf', 'located', 'st', 'verdict', 'note']
with open(D + 'decisions.tsv', 'w') as f:
    f.write('\t'.join(cols) + '\n')
    for x in sorted(rows, key=lambda r: (r['role'], r['line'], int(r['pos']))): f.write('\t'.join(str(x.get(c, '')) for c in cols) + '\n')
if '--write' in sys.argv and gate and new:
    with open('exceptions_nieuw_image.tsv', 'a') as f:
        for x, v, g in new:
            f.write(f"{x['line']}\t{x['pos']}\t{v}\t{g}\tSUR-2039R blind sign call (passes/signcmp_sur2039r, prereg 691b7d363): reader {x['reader_code']} = {x['tile']} {x['conf']}, runner-up {x['second']} ({x['sval']}) {x['sconf']} ({x['query']}); controls {ok}/20\n")
    print('appended', len(new), 'rows')
