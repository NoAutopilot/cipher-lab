#!/bin/bash
# BOXMAP-RESCORE (others), 11 Oct 2026, account 3: TXE3-1 re-run with only --map changed (atlas/no87_box_token_labelaware.tsv),
# the reproduce command of benchmark-tx/txeng3/1/VERIFY.md for every committed setting (eval and dev; pile, none, cluster; x and m;
# lam 1; plus dev pile x lam 4). The none model reads the map only for the margin order. From the repo root:
#   bash benchmark-tx/txeng3/1/rescore_boxmapLA/run.sh [OUTDIR] [SIGDIR]
O=${1:-benchmark-tx/txeng3/1/rescore_boxmapLA}; SD=${2:-benchmark-tx/txeng/doubt}
C=ciphers/nevers-birago-fr3251-1572; MAP=$C/atlas/no87_box_token_labelaware.tsv
run() { # unit mode mask lam
  unit=$1; mode=$2; mask=$3; lam=$4
  if [ $unit = eval ]; then L=benchmark-tx/txeng/units/labels_eval_heldout.tsv; SG=$SD/eval_heldout_signals.tsv
  else L=benchmark-tx/txeng/units/labels_dev_tune.tsv; SG=$SD/dev_tune_signals.tsv; fi
  X=""; [ $mask = x ] && X="--exclude-flagged"
  DD=""; [ $unit = eval ] && [ $mode = pile ] && DD="--dump-dir $O/$unit/dump_pile_${mask}_lam$lam"
  mkdir -p $O/$unit
  python3 tools/tx_sorter_curve.py --truth benchmark-tx/birago1572-no87.truth.tsv \
    --base benchmark-tx/outputs/birago1572-no87/passC.tsv --lines $L \
    --map $MAP --clusters $C/atlas/clusters.tsv --signals $SG \
    --margin $C/atlas/topk/no87_heldout.tsv --lattice $C/harvest/tx_decode/no87_topk.tsv --key $C/harvest/key_1572_sheet.tsv \
    --lang it16dip --lam $lam --propagate $mode --seeds 20 $X $DD --out $O/$unit/curve_${unit}_${mode}_${mask}_lam$lam.tsv \
    --json $O/$unit/summary_${unit}_${mode}_${mask}_lam$lam.json > /dev/null
}
for u in eval dev; do for mo in pile none cluster; do for ma in x m; do run $u $mo $ma 1; done; done; done
run dev pile x 4
