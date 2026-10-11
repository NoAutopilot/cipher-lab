#!/bin/sh
# BOXMAP-RESCORE (others), 11 Oct 2026, account 3: TXE2-FEED's eval_heldout (no.87) feed rebuilt with the label-aware tile map
# (benchmark-tx/txeng/rescore_boxmapLA/box_pos.tsv, from atlas/no87_box_token_labelaware.tsv). Same command as ../build.sh's
# eval_heldout step with only --tile-map changed (old tile map -> byte-identical to ../eval_heldout_{feed,focus,feed_signals}.tsv,
# checked 11 Oct 2026); then the sorter tile boxes as ../tiles.py writes them. Read-free. From the repo root:
#   sh benchmark-tx/txeng2/feed/rescore_boxmapLA/build_la.sh
set -e
OUT=benchmark-tx/txeng2/feed/rescore_boxmapLA; D=benchmark-tx/txeng2/doubt
python3 benchmark-tx/txeng/rescore_boxmapLA/box_pos_la.py
python3 tools/tx_feed.py --base benchmark-tx/txeng/units/labels_eval_heldout.tsv --unit eval_heldout --out $OUT \
  --differ latt=benchmark-tx/txeng/doubt/passL_lattice_eval_heldout_lam4.tsv --differ vote4=$D/vote4_uniform_eval_heldout.tsv \
  --table $D/eval_heldout_signals3.tsv --combo latt+vote4+selfcons --tile-map benchmark-tx/txeng/rescore_boxmapLA/box_pos.tsv --pairs taxonomy
python3 - <<'PY'
import csv
rd = lambda p: list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))
O = 'benchmark-tx/txeng2/feed/rescore_boxmapLA'
boxes = {r['sid']: r for r in rd('ciphers/nevers-birago-fr3251-1572/atlas/signs.tsv')}
feed = {r['tile']: r for r in rd(O + '/eval_heldout_feed.tsv')}
with open(O + '/eval_heldout_tiles.tsv', 'w') as f:
    f.write('tile\tline\tpos\tpage\tx\ty\tw\th\tcrops\n')
    for t, _q in (l.rstrip('\n').split('\t') for l in open(O + '/eval_heldout_focus.tsv')):
        r, b = feed[t], boxes.get(t)
        f.write('\t'.join([t, r['line'], r['pos']] + ([b['page'], b['x'], b['y'], b['w'], b['h']] if b else [''] * 5) + ['']) + '\n')
PY
