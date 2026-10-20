#!/usr/bin/env python3
"""MONL-KING4 (20 Oct 2026): fold the look-alike re-read into ciphertext_c258.tsv (PREREG-MONL-KING4.md). Concatenates
king4/reread_p1-3.tsv -> king4/c258_reread.tsv, runs tools/lookalike_pass.py reconcile (fixed 2-of-3 rule) -> king4/c258_passD.tsv,
king4/c258_passD_alt.tsv, king4/focus.tsv; keeps the pre-fold file as king4/ciphertext_c258_pre.tsv; writes the sign (and conf, for a
settled tile) back into ciphertext_c258.tsv, schema unchanged; splits king4/c258_L01-L10.tsv and king4/c258_L11-L25.tsv; prints the
residual, the echo shares and r (control noise = max(0.05, unsettled/signs)). Run from the repo root; idempotent (reads the _pre copy)."""
import csv, json, os, shutil, subprocess, sys
D = 'ciphers/fr4735-monluc-lansac-poland-1573'; K = D + '/king4'
rows = []
for k in (1, 2, 3):
    rows += [r for r in csv.DictReader(open(f'{K}/reread_p{k}.tsv'), delimiter='\t') if r.get('passage', '').startswith('L')]
F = ['passage', 'pos', 'label', 'conf', 'second', 'note']
with open(K + '/c258_reread.tsv', 'w') as o:
    w = csv.DictWriter(o, F, delimiter='\t', lineterminator='\n', extrasaction='ignore'); w.writeheader()
    for r in rows: w.writerow({f: (r.get(f) or '').strip() for f in F})
sys.path.insert(0, 'tools'); import lookalike_pass as lp
res = lp.reconcile(K + '/c258_tiles.tsv', K + '/c258_passC.tsv', K + '/c258_reread.tsv', K + '/c258_passD.tsv',
                   K + '/c258_passD_alt.tsv', K + '/focus.tsv')
if not os.path.exists(K + '/ciphertext_c258_pre.tsv'): shutil.copy(D + '/ciphertext_c258.tsv', K + '/ciphertext_c258_pre.tsv')
pre = list(csv.DictReader(open(K + '/ciphertext_c258_pre.tsv'), delimiter='\t')); hdr = list(pre[0].keys())
pd = {(r['passage'], r['pos']): r for r in csv.DictReader(open(K + '/c258_passD.tsv'), delimiter='\t')}
tiles = {(t['passage'], t['pos']): t for t in csv.DictReader(open(K + '/c258_tiles.tsv'), delimiter='\t')}
rr = {(r['passage'], r['pos']): r for r in rows}
new, firm, eA, eB, eC, eCdiff, nCdiff = [], 0, 0, 0, 0, 0, 0
for r in pre:
    k = (r['line'], r['pos']); r = dict(r); d = pd[k]
    if d['note'].startswith('lookalike') and 'UNSETTLED' not in d['note']: r['sign'], r['conf'] = d['sign_id'], d['conf']
    new.append(r)
    if k in tiles:
        t, x = tiles[k], rr[k]; lab = x['label'].strip()
        if x['conf'].strip() in ('H', 'M') and not lab.startswith('SPLIT'):
            firm += 1; eA += lab == t['A']; eB += lab == t['B']; eC += lab == t['passC']
            if t['status'] == 'split': nCdiff += 1; eCdiff += lab == t['passC']
def write(p, rs):
    with open(p, 'w') as o:
        w = csv.DictWriter(o, hdr, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(rs)
write(D + '/ciphertext_c258.tsv', new)
write(K + '/c258_L01-L10.tsv', [r for r in new if int(r['line'][1:]) <= 10])
write(K + '/c258_L11-L25.tsv', [r for r in new if int(r['line'][1:]) > 10])
ch = sum(a['sign'] != b['sign'] for a, b in zip(pre, new))
out = dict(reconcile=res, changed_in_file=ch, firm=firm, firm_eq_A=eA, firm_eq_B=eB, firm_eq_passC=eC,
           split_firm=nCdiff, split_firm_eq_passC=eCdiff, echo_share=round(eCdiff / max(1, nCdiff), 3),
           r=round(max(0.05, res['unsettled'] / res['signs']), 3))
json.dump(out, open(K + '/fold.json', 'w'), indent=1); print(json.dumps(out))
