"""ES132-WIN scorer (PREREG-ES132-WIN.md): decoy gate >= 10/12 exact; candidates settle only where the window read == dup token.
Writes win_f89/result.json and win_f89/agree.tsv. --check: recompute and compare with the committed files (exit 1 if stale)."""
import sys, json, csv
from pathlib import Path
D = Path(__file__).resolve().parent
def norm(s): return s.strip().replace(' ', '')
items = [r for r in csv.DictReader((l for l in open(D/'items.tsv', encoding='utf-8') if not l.startswith('#')), delimiter='\t')]
reads = {}
for b in (1, 2, 3):
    for r in csv.DictReader(open(D/f'read_batch{b}.tsv', encoding='utf-8'), delimiter='\t'): reads[r['id']] = norm(r['read'])
dec = [(it['id'], it['cid'], it['truth'], reads[it['id']]) for it in items if it['kind'] == 'decoy']
right = [d for d in dec if d[3] == d[2]]
gate = len(right) >= 10
rows, cnt = [], dict(eq_dup=0, eq_cur=0, neither=0, unclear=0)
for it in items:
    if it['kind'] != 'cand': continue
    rd, cur, dup = reads[it['id']], it['cur'].rstrip('?'), it['dup']
    k = 'unclear' if rd == 'unclear' else 'eq_dup' if rd == dup else 'eq_cur' if rd == cur else 'neither'
    cnt[k] += 1; rows.append((it['id'], it['pos'], it['cur'], dup, rd, k))
res = dict(decoys_right=len(right), decoys=len(dec), gate_pass=gate, decoy_misses=[d for d in dec if d[3] != d[2]], candidates=cnt)
out_j = json.dumps(res, ensure_ascii=False, indent=1) + '\n'
out_t = 'id\tpos\tf89_cur\tdup_tok\twindow_read\tclass\n' + ''.join('\t'.join(r) + '\n' for r in rows)
if '--check' in sys.argv:
    ok = (D/'result.json').read_text(encoding='utf-8') == out_j and (D/'agree.tsv').read_text(encoding='utf-8') == out_t
    print('OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
(D/'result.json').write_text(out_j, encoding='utf-8'); (D/'agree.tsv').write_text(out_t, encoding='utf-8'); print(out_j)
