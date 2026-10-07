#!/usr/bin/env python3
"""D07-PIST40: apply the pre-registered settlement rule (pist40/PREREG_pist40.md) to the blind reader's reply
(pist40/blind/reader.txt) -> pist40/t40_tokens.tsv. --check: exit 1 if the committed tsv is stale."""
import csv, os, sys
H = os.path.dirname(os.path.abspath(__file__))
lab = {r['label']: r['cell'] for r in csv.DictReader(open(f'{H}/blind/cell_labels.tsv'), delimiter='\t')}
ids = {r['id']: r for r in csv.DictReader(open(f'{H}/blind/token_ids.tsv'), delimiter='\t')}
rep = {}
for ln in open(f'{H}/blind/reader.txt'):
    p = ln.rstrip('\n').split('\t')
    if len(p) == 5 and p[0] in ids: rep[p[0]] = p
ADM = {('L06', '36'): {'T17', 'T40'}}
out = ['id\tline\ttok_index\tlabel\trole\tbest\tsecond\tconf\tadmissible\tstatus\tread_T40\tdescription']
ctrl_ok = ctrl_n = 0; rows = []
for i, r in sorted(ids.items(), key=lambda kv: (kv[1]['role'], kv[1]['line'], int(kv[1]['tok_index']))):
    _, b, s, c, d = rep[i]; best, sec = lab[b], lab[s]
    adm = {r['label']} if r['role'] == 'control' else ADM.get((r['line'], r['tok_index']), {'T17'})
    st = f'SETTLED-{best}' if c in ('medium', 'high') and best in adm else 'UNSETTLED'
    rt = 'READ-T40' if r['role'] == 'test' and best == 'T40' and c in ('medium', 'high') else ''
    if r['role'] == 'control': ctrl_n += 1; ctrl_ok += st == f"SETTLED-{r['label']}"
    rows.append([i, r['line'], r['tok_index'], r['label'], r['role'], best, sec, c, '|'.join(sorted(adm)), st, rt, d])
gate = ctrl_ok >= 4
for x in rows:
    if x[4] == 'test' and not gate: x[9] = 'UNSETTLED (control gate failed)'
    out.append('\t'.join(x))
out.append(f'# control gate: {ctrl_ok}/{ctrl_n} controls settled to own label (need >= 4): {"PASS" if gate else "FAIL"}')
txt = '\n'.join(out) + '\n'
f = f'{H}/t40_tokens.tsv'
if '--check' in sys.argv:
    ok = os.path.exists(f) and open(f).read() == txt; print('up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(f, 'w').write(txt); print(txt)
