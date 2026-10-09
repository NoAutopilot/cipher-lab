#!/bin/sh
# TXE2-FEED (S4, 9 Oct 2026): regenerate the three sorter feeds read-free from the repo root.
#   sh benchmark-tx/txeng2/feed/build.sh
set -e
F=benchmark-tx/txeng2/f152r; O=benchmark-tx/outputs/spinelli-c1519-confirm; C=benchmark-tx/txeng/confirm
D=benchmark-tx/txeng2/doubt; OUT=benchmark-tx/txeng2/feed; H=ciphers/nevers-birago-fr3251-1572/harvest
# f152r plain lattice (lam 4, beam 64, it16dip, printed 1572 key; 20 value-shuffled keys as its control)
python3 tools/key_decode_lattice.py from-passes $F/passA.tsv $F/passB.tsv --confusion $H/confusion_1572.tsv --out $OUT/work/f152r_topk.tsv
python3 tools/key_decode_lattice.py decode $OUT/work/f152r_topk.tsv --key $H/key_1572_sheet.tsv --lang it16dip --lam 4 --beam 64 --shuffles 20 --out-prefix $OUT/work/f152r_latt
python3 tools/tx_feed.py --base benchmark-tx/txeng/units/labels_eval_heldout.tsv --unit eval_heldout --out $OUT \
  --differ latt=benchmark-tx/txeng/doubt/passL_lattice_eval_heldout_lam4.tsv --differ vote4=$D/vote4_uniform_eval_heldout.tsv \
  --table $D/eval_heldout_signals3.tsv --combo latt+vote4+selfcons --tile-map benchmark-tx/txeng/compare/box_pos.tsv --pairs taxonomy
python3 tools/tx_feed.py --base benchmark-tx/outputs/birago1572-f152r/passZ_pipeline.tsv --unit f152r --out $OUT --rename L=f152r_L \
  --differ latt=$OUT/work/f152r_latt.decode.tsv --differ readerA=$F/passA.tsv --differ readerB=$F/passB.tsv \
  --lowconf lowA=$F/passA.tsv --lowconf lowB=$F/passB.tsv --combo latt+vote4+selfcons --pairs taxonomy
python3 tools/tx_feed.py --base $O/passZ_pipeline.tsv --unit spinelli --out $OUT --differ readerA=$O/passA_txeq.tsv \
  --differ readerB=$O/passB_txeq.tsv --lowconf lowA=$C/passA.tsv --lowconf lowB=$C/passB.tsv --combo latt+vote4+selfcons
python3 $OUT/tiles.py
