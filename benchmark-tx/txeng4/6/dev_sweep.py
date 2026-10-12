#!/usr/bin/env python3
"""TXE4-6 unit 4 (dev, safety only; PREREG-txeng4-6 'Threshold rule'): freeze the margin t on no.87 dev_tune (f178v L01-L12).
Opens benchmark-tx/birago1572-no87.truth.tsv ONLY for the dev lines, through tx_bench's own align/position_signs (the TXE4-9
tx_calibrate precedent). Reads out/no87_R.decisions.tsv (t = 0, hashed in SHA256SUMS.prescore before this ran).
Per decided dev row: right = the picked sign is in the truth set at the truth position aligned to the base position.
Sweep t in {0, 0.05, ..., 1.0}: decided = margin > t; accuracy = right / decided; coverage = decided / reachable dev rows.
t_frozen = the smallest t with accuracy >= 0.90 and coverage >= 0.30, else STOP. Also: accuracy at t = 0 against the committed
adjudicator (35/36 on dev, TXE-K) and a coin (0.5); the tiebreak's agreement with the committed adjudication on dev.
Usage: python3 benchmark-tx/txeng4/6/dev_sweep.py  (from the repo root)"""
import csv, json, os, sys
sys.path.insert(0, 'tools')
import tx_bench as TB
DEV = {f'f178v_L{i:02d}' for i in range(1, 13)}
O = 'benchmark-tx/txeng4/6'
rd = lambda p: list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))
truth = [r for r in rd('benchmark-tx/birago1572-no87.truth.tsv') if r['line'] in DEV]
base = TB.load_output(['benchmark-tx/outputs/birago1572-no87/passC.tsv'])
base = {l: v for l, v in base.items() if l in DEV}
dec = [r for r in rd(f'{O}/out/no87_R.decisions.tsv') if r['line'] in DEV]
ts = {(r['line'], r['pos']): set(filter(None, r['truth'].split('|'))) for r in truth if r['status'] == 'scored'}
by_line = {}
for r in truth:
    by_line.setdefault(r['line'], []).append(r)
rows = []
for d in dec:
    if not d['pick'] or not d['base_pos']:
        continue
    trs = sorted(by_line[d['line']], key=lambda r: float(r['pos']))
    ref = [r['ref_sign'] for r in trs]
    tsl = [set(filter(None, r['truth'].split('|'))) for r in trs]
    b2t, j = {}, 0
    for ri, osg in TB.align(ref, tsl, base[d['line']]):
        if osg is None:
            continue
        b2t[j] = ri; j += 1
    ri = b2t.get(int(d['base_pos']) - 1)
    if ri is None or trs[ri]['status'] != 'scored':
        rows.append(dict(d, scored='no')); continue
    T = tsl[ri]
    rows.append(dict(d, scored='yes', right=d['pick'] in T, base_right=d['base_sign'] in T, A_right=d['A'] in T, B_right=d['B'] in T,
                     margin_f=float(d['margin'])))
sc = [r for r in rows if r['scored'] == 'yes']
reach = len(dec)
print(f'dev reachable split rows {reach}; decided at t=0 {len(rows)}; of which on scored truth positions {len(sc)}')
print(f"t=0: tiebreak right {sum(r['right'] for r in sc)}/{len(sc)} = {sum(r['right'] for r in sc)/max(1,len(sc)):.3f}; "
      f"committed adjudicator right at the same rows {sum(r['base_right'] for r in sc)}/{len(sc)} (TXE-K dev 35/36 = 0.972); coin 0.500; "
      f"rows where A right {sum(r['A_right'] for r in sc)}, B right {sum(r['B_right'] for r in sc)}, neither {sum((not r['A_right']) and (not r['B_right']) for r in sc)}")
print(f"agreement with the committed adjudication at decided rows: same {sum(r['applied']=='same' for r in rows)}, override {sum(r['applied']=='yes' for r in rows)}; "
      f"overrides right {sum(r['right'] for r in sc if r['applied']=='yes')}/{sum(r['applied']=='yes' for r in sc)}, overrides that break a right base {sum((not r['right']) and r['base_right'] for r in sc if r['applied']=='yes')}")
print('t      decided  coverage  right  accuracy')
frozen = None
for i in range(0, 21):
    t = i * 0.05
    dd = [r for r in sc if r['margin_f'] > t]
    cov = sum(1 for r in rows if float(r['margin']) > t) / max(1, reach)
    acc = sum(r['right'] for r in dd) / len(dd) if dd else 0.0
    flag = ''
    if frozen is None and dd and acc >= 0.90 and cov >= 0.30:
        frozen, flag = t, '  <- frozen t'
    print(f'{t:.2f}   {len(dd):3d}      {cov:.2f}      {sum(r["right"] for r in dd):3d}    {acc:.3f}{flag}')
verdict = f'FROZEN t = {frozen:.2f}' if frozen is not None else 'STOP: no t meets accuracy >= 0.90 at coverage >= 0.30 on dev'
print(verdict)
json.dump(dict(frozen_t=frozen, verdict=verdict, reachable=reach, decided_t0=len(rows), scored_t0=len(sc),
               right_t0=sum(r['right'] for r in sc), rows=[{k: (v if not isinstance(v, bool) else int(v)) for k, v in r.items()} for r in rows]),
          open(f'{O}/dev_sweep.json', 'w'), indent=1)
