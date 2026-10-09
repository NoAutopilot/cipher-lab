#!/bin/sh
# UNA-NEVBIR (9 Oct 2026), run from harvest/: sh tx_decode/mix/run.sh  (PREREG-UNA-NEVBIR.md, fixed before any score)
set -e
O=tx_decode/mix; T=../../../tools/key_decode_lattice.py; K=key_1572_sheet.tsv
python3 $O/mix_build.py
for x in f144r:it16dip f168:it16dip f117:fr; do L=${x%%:*}; G=${x##*:}
  python3 $T decode $O/${L}_mix_topk.tsv --key $K --lang $G --shuffles 200 --seed 1 --lam 4 --beam 64 --out-prefix $O/${L}_mix_lam4 > /dev/null &
done
python3 $O/shuffled_target_mix.py &
wait
