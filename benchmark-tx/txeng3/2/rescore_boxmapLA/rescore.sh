#!/bin/sh
# BOXMAP-RESCORE (others), 11 Oct 2026, account 3: TXE3-2's read-free parts re-run with only the box map changed.
#   sh benchmark-tx/txeng3/2/rescore_boxmapLA/rescore.sh
# (1) positions6.tsv / positions6_summary.md: tools/tx_taxonomy.py over L A B C E F with --box-token = the label-aware map in the old
#     row convention (atlas/no87_map.py --compat, temp only: it carries the clerk alignment); with the old map the same command
#     reproduces the committed positions6.tsv and positions6_summary.md byte for byte (checked 11 Oct 2026).
# (2) items_tiles.tsv: for each of the 36 floor/control items, the atlas box build_items.py cut (old map) and the box the label-aware
#     map gives that position, plus the classifier's committed answer fields (floor.tsv), so the gate can be read on correct tiles.
# The blind classification itself (13 Sonnet calls) is NOT re-run (no model call in this job).
set -e
C=ciphers/nevers-birago-fr3251-1572; O=benchmark-tx/outputs/birago1572-no87; R=benchmark-tx/txeng3/2/rescore_boxmapLA; T=$(mktemp -d)
python3 $C/atlas/no87_map.py --compat $T/compat_map.tsv > /dev/null
python3 tools/tx_taxonomy.py --item birago1572-no87 --pass L=$O/labels.tsv --pass A=$O/passA.tsv --pass B=$O/passB.tsv \
  --pass C=$O/passC.tsv --pass E=$O/passE_sheet.tsv --pass F=$O/passF_fable.tsv --boxes $C/atlas/signs.tsv \
  --box-token $T/compat_map.tsv --harvest $C/harvest --out-tsv $R/positions6.tsv --md $R/positions6_summary.md > /dev/null
python3 - $T/compat_map.tsv $R <<'PY'
import csv, sys
rd = lambda p: list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))
C = 'ciphers/nevers-birago-fr3251-1572'
sg = {r['sid'] for r in rd(C + '/atlas/signs.tsv')}
def boxes(p):                     # build_items.py's rule: the last map row with that (line, pos) whose sid is an atlas box
    b = {}
    for r in rd(p):
        if r['sid'] in sg: b[(r['line'], r['pos'])] = r['sid']
    return b
bo, bn = boxes(C + '/atlas/no87_box_token.tsv'), boxes(sys.argv[1])
F = {(r['line'], r['pos']): r for r in rd('benchmark-tx/txeng3/2/floor.tsv')}
cols = ['call', 'label', 'kind', 'line', 'pos', 'old_box', 'new_box', 'wrong_tile', 'q1', 'q2', 'q3_top1', 'truth', 'readers_sign',
        'cause_class', 'invented_cause']
with open(sys.argv[2] + '/items_tiles.tsv', 'w') as f:
    f.write('\t'.join(cols) + '\n')
    for k in rd('benchmark-tx/txeng3/2/key.tsv'):
        p = (k['line'], k['pos']); r = F[p]
        ob, nb = bo.get(p, ''), bn.get(p, '')
        wt = '' if p[0].startswith('f178r') else str(int(ob != nb))
        f.write('\t'.join([k['call'], k['label'], k['kind'], p[0], p[1], ob, nb, wt] + [r.get(c, '') for c in cols[8:]]) + '\n')
PY
rm -rf $T
