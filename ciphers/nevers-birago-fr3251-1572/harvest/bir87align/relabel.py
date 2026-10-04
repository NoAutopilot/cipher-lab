#!/usr/bin/env python3
"""BIR87-ALIGN step 1 (4 Oct 2026): owner-labelled no.87 sequence + corrected 4 Oct sort labels. Disk only, deterministic.
  python3 relabel.py
(a) no.87: harvest/ciphertext_f178r/f178v/f179r.tsv copied to cipher_owner/ (primary: every sorter tile with status kept or
    moved whose atlas box maps 1:1 to a token in atlas/no87_box_token.tsv) and cipher_moved/ (sensitivity: moved tiles only),
    with `sign` replaced by "P:<owner pile>"; not-letter tiles -> "P:NOT-LETTER" is NOT used, they become their own per-tile
    code (sign "X_NOTLETTER"); bad-cut tiles and every token off the sorter keep the committed (atlas/line-read) label.
(b) sorter/owner-sort-2026-10-04/settled_labels.tsv with corrections.tsv applied (later row wins per tile) -> settled_corrected.tsv.
Counts -> relabel_counts.json."""
import csv, json, shutil
from collections import Counter
from pathlib import Path
D = Path(__file__).resolve().parent; T = D.parents[1]; HV = T / 'harvest'
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
bt = {r['sid']: r for r in rd(T / 'atlas/no87_box_token.tsv')}
st = rd(T / 'sorter/no87/owner-sort-2026-10-04/settled_no87.tsv')
cnt = {}
for name, ok in (('cipher_owner', ('kept', 'moved', 'not-letter')), ('cipher_moved', ('moved', 'not-letter'))):
    od = D / name; od.mkdir(exist_ok=True)
    lab = {}; c = Counter()
    for r in st:
        b = bt.get(r['sid'])
        if b is None: c['tile_no_token'] += 1; continue
        if b['op'] != '1:1': c['tile_not_1to1_' + b['op']] += 1; continue
        if r['status'] not in ok: c['tile_' + r['status'] + '_kept_committed'] += 1; continue
        lab[(b['fol'], b['line'], b['pos'])] = 'X_NOTLETTER' if r['status'] == 'not-letter' else 'P:' + r['new_sign']
        c['owner_' + r['status']] += 1
    tot = 0
    for fol in ('f178r', 'f178v', 'f179r'):
        rows = rd(HV / f'ciphertext_{fol}.tsv'); tot += len(rows)
        with open(od / f'ciphertext_{fol}.tsv', 'w') as f:
            f.write('line\tpos\tsign\tconf\n')
            for x in rows:
                s = lab.get((fol, x['line'], x['pos']), x['sign'])
                f.write(f"{x['line']}\t{x['pos']}\t{s}\t{x['conf']}\n")
    c['tokens'] = tot; c['tokens_owner_labelled'] = len(lab); c['tokens_atlas_or_lineread'] = tot - len(lab)
    c['piles'] = dict(Counter(v for v in lab.values()))
    cnt[name] = dict(c)
# (b) corrections
S = T / 'sorter/owner-sort-2026-10-04'
lab = rd(S / 'settled_labels.tsv'); cor = {}
for r in rd(S / 'corrections.tsv'): cor[r['owner_sid']] = r  # file is in time order: later row wins
n = 0
with open(D / 'settled_corrected.tsv', 'w') as f:
    f.write('sid\told_sign\tnew_sign\tstatus\tcorrected_from\n')
    for r in lab:
        c = cor.get(r['sid']); fr = ''
        if c:
            assert r['new_sign'] == c['from_pile'] or c['from_pile'] == 'T86', (r, c)
            fr = r['new_sign']; r['new_sign'] = c['to_pile'] if c['to_pile'] != 'UNPLACED' else ''
            r['status'] = 'moved' if r['new_sign'] else 'aside'; n += 1
        f.write(f"{r['sid']}\t{r['old_sign']}\t{r['new_sign']}\t{r['status']}\t{fr}\n")
cnt['corrections_applied'] = n; cnt['corrections_rows'] = len(rd(S / 'corrections.tsv'))
json.dump(cnt, open(D / 'relabel_counts.json', 'w'), indent=1); print(json.dumps(cnt, indent=1))
