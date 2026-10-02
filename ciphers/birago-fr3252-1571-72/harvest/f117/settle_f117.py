#!/usr/bin/env python3
"""Settle the value-blind reconciliation of f.117r passes A/B (NEVBIR-3252-B, 2 Oct 2026). The 70 unsettled rows of
recon_f117.tsv were settled by this worker by eye from the native crops (images/f117/f117_L*_s*.jpg) against
sign_sheet_blind_1572.png, BEFORE any decode was run. Caveat: this worker had seen part of the 1572 sign-id map while
setting up the pipeline (T42/T45/T36/T37/T33/T29/T26/T27/T24/T25 values), so this is a one-eye settlement, not a blind
third reader (no third subagent: account rate limit at allowed_warning). Every settled row is conf M (L where flagged).
Class rules: hash -> T60; 'p with crossbar'/'barred k' -> pass A's T95/T51 (B lumped them as T65); barred loop-on-stem
-> T90 where A saw the bar; phi stem-through-ring -> T98; x forms by shape on the crop: the curled-both-sides form
(ж) T83, the x-with-loop form T81; X_NEW vs X_S on long-s shapes -> X_S. Structural: L03 25-26 '8','5' are the
plain digits '85' = cell T11 (one sign); L03 tail = T52 X_S T81; L10 ends T84 ? X_S.
python3 settle_f117.py  -> recon_f117_final.tsv"""
import csv
S = {('L01', 8): 'T51', ('L01', 18): 'T76', ('L01', 19): 'X_NEW', ('L01', 22): 'T60', ('L01', 26): 'X_S', ('L01', 28): 'T83',
     ('L02', 1): 'T95', ('L02', 3): 'T60', ('L02', 6): 'T76', ('L02', 23): 'T81', ('L02', 26): 'T60', ('L02', 27): 'T98',
     ('L03', 1): 'T90', ('L03', 4): 'T83', ('L03', 9): 'T81', ('L03', 10): 'T95', ('L03', 11): 'T60', ('L03', 15): 'T60',
     ('L03', 16): 'T81', ('L03', 23): 'T98', ('L03', 28): 'T90',
     ('L04', 6): 'T95', ('L04', 7): 'T60', ('L04', 10): 'T90', ('L04', 12): 'T83', ('L04', 15): 'X_S', ('L04', 22): 'T83',
     ('L04', 23): 'T60', ('L04', 26): 'T83',
     ('L05', 1): 'X_S', ('L05', 2): 'T95', ('L05', 12): 'T95', ('L05', 16): 'T98', ('L05', 18): 'T51', ('L05', 20): 'X_S',
     ('L05', 22): 'T83', ('L05', 26): 'X_S', ('L05', 27): 'T66',
     ('L06', 10): 'T83', ('L06', 12): 'X_S', ('L06', 13): 'T51', ('L06', 18): 'T90', ('L06', 20): 'T81', ('L06', 21): 'T60',
     ('L06', 26): 'T90', ('L06', 31): 'T36',
     ('L07', 10): 'T60', ('L07', 21): 'T95', ('L07', 23): 'T60', ('L07', 27): 'T98', ('L07', 28): 'T60', ('L07', 29): 'T81',
     ('L08', 6): 'T83', ('L08', 10): 'T83', ('L08', 19): 'T83', ('L08', 23): 'T95', ('L08', 27): 'T29',
     ('L09', 11): 'T95', ('L09', 17): 'T60', ('L09', 20): 'T95', ('L09', 29): 'T95',
     ('L10', 1): 'T83'}
rows = list(csv.DictReader(open('recon_f117.tsv'), delimiter='\t'))
out = {}
for r in rows:
    k = (r['passage'], int(r['pos']))
    sid, conf = r['sign_id'], r['conf']
    if k in S:
        sid, conf = S[k], 'M'
    out.setdefault(r['passage'], []).append([sid, conf, r.get('note', '')])
l3 = out['L03']                       # positions are 1-based; edit from the tail so earlier indices hold
l3[28:31] = [['T52', 'M', 'n-shape'], ['X_S', 'M', 's-curl'], ['T81', 'M', 'x with loop; line end']]
l3[24:26] = [['T11', 'M', 'plain digits 85 (A: 8 + small s; B: 8 + long s)']]
l10 = out['L10']
l10[8:10] = [['T84', 'M', 'V/inverted triangle with bar'], ['?', 'L', 'triangle on cross: A T70, B T84']]
l10.append(['X_S', 'M', 'f/long s with dots; line end'])
with open('recon_f117_final.tsv', 'w') as f:
    f.write('passage\tpos\tsign_id\tconf\tnote\n')
    for p, seq in out.items():
        for i, (sid, conf, note) in enumerate(seq, 1):
            f.write(f'{p}\t{i}\t{sid}\t{conf}\t{note}\n')
n = sum(len(s) for s in out.values())
print(n, 'signs;', sum(1 for s in out.values() for x in s if x[0] == '?'), "'?';",
      sum(1 for s in out.values() for x in s if x[0].startswith('X_')), 'X_')
