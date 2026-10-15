"""ES132-BLIND scorer (PREREG-ES132-BLIND.md): decoy gate + candidate agreement. Reads blind_f89/items.tsv and blind_f89/read_batch1-3.tsv;
writes blind_f89/result.json and blind_f89/agree.tsv. --check exits 1 if the committed outputs are stale. Applies nothing."""
import sys, json
from pathlib import Path
D = Path(__file__).resolve().parent
def tsv(p):
    L = [l.rstrip('\n').split('\t') for l in open(p, encoding='utf-8') if not l.startswith('#') and l.strip()]
    return [dict(zip(L[0], r)) for r in L[1:]]
items = {r['id']: r for r in tsv(D/'items.tsv')}
reads = {}
for b in (1, 2, 3):
    for r in tsv(D/f'read_batch{b}.tsv'): reads[r['id']] = r['read'].strip()
assert set(reads) == set(items), set(items) ^ set(reads)
norm = lambda s: s.replace(' ', '')
dec = [(i, items[i]['side'], items[i]['truth'], reads[i]) for i in sorted(items) if items[i]['kind'] == 'decoy']
right = [d for d in dec if norm(d[3]) == norm(d[2])]
cur = {}
for l in open(D.parent/'dup_settled.tsv', encoding='utf-8'):
    if l.startswith('#'): continue
    r = l.rstrip('\n').split('\t'); cur[r[0]] = r
rows = []
for cid in sorted({it['cid'] for it in items.values() if it['kind'] != 'decoy'}):
    a = next(i for i, it in items.items() if it['cid'] == cid and it['kind'] == 'candA')
    b = next(i for i, it in items.items() if it['cid'] == cid and it['kind'] == 'candB')
    ra, rb = reads[a], reads[b]
    st = 'unclear' if 'unclear' in (ra, rb) else ('agree' if norm(ra) == norm(rb) else 'disagree')
    old, dup = cur[cid][1], cur[cid][2]
    rel = '' if st != 'agree' else ('=current' if norm(ra) == norm(old.rstrip('?')) else ('=dup' if norm(ra) == norm(dup) else 'neither'))
    rows.append([cid, old, dup, a, ra, b, rb, st, rel])
res = dict(decoys_right=len(right), decoys=len(dec), f89_side=f"{sum(d[1]=='f89' for d in right)}/{sum(d[1]=='f89' for d in dec)}",
           dup_side=f"{sum(d[1]=='dup' for d in right)}/{sum(d[1]=='dup' for d in dec)}", gate_pass=len(right) >= 10,
           decoy_rows=[list(d) for d in dec],
           candidates={k: sum(r[7] == k for r in rows) for k in ('agree', 'disagree', 'unclear')},
           agreed_relation={k: sum(r[8] == k for r in rows) for k in ('=current', '=dup', 'neither')})
out_j = json.dumps(res, ensure_ascii=False, indent=1) + '\n'
out_t = '# ES132-BLIND agreement (blind_f89/score.py)\ncid\tf89_old\tdup_tok\tread_A\tA\tread_B\tB\tstatus\trelation\n' + ''.join('\t'.join(r) + '\n' for r in rows)
if '--check' in sys.argv:
    ok = (D/'result.json').read_text(encoding='utf-8') == out_j and (D/'agree.tsv').read_text(encoding='utf-8') == out_t
    print('OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
(D/'result.json').write_text(out_j, encoding='utf-8'); (D/'agree.tsv').write_text(out_t, encoding='utf-8')
print(json.dumps({k: v for k, v in res.items() if k != 'decoy_rows'}))
