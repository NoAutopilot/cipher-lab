#!/bin/bash
# BOXMAP-RESCORE (others), 11 Oct 2026, account 3: X6 (TXE2-SORT) cluster and pile curves re-run with only --map changed
# (atlas/no87_box_token_labelaware.tsv). The `none` curves never read the map and are not re-run. From the repo root:
#   bash benchmark-tx/txeng2/sorter/rescore_boxmapLA/run.sh [MAP] [OUTDIR] [SIGDIR]
# MAP = the old atlas/no87_box_token.tsv reproduces the committed summaries' a-d orderings exactly with today's tool (checked
# 11 Oct 2026; the tool has since gained TXE3-1's orders, which add rows to the curve files). SIGDIR = the tx_doubt signal
# tables (default the committed benchmark-tx/txeng/doubt; benchmark-tx/txeng/rescore_boxmapLA/doubt = rebuilt on the fixed map).
A=ciphers/nevers-birago-fr3251-1572/atlas; U=benchmark-tx/txeng/units
MAP=${1:-$A/no87_box_token_labelaware.tsv}; O=${2:-benchmark-tx/txeng2/sorter/rescore_boxmapLA}; D=${3:-benchmark-tx/txeng/doubt}
mkdir -p $O
for unit in dev_tune eval_heldout whole; do
  if [ $unit = whole ]; then L="$U/labels_dev_tune.tsv $U/labels_eval_heldout.tsv"; SG="$D/dev_tune_signals.tsv $D/eval_heldout_signals.tsv"
  else L="$U/labels_$unit.tsv"; SG="$D/${unit}_signals.tsv"; fi
  for mode in cluster pile; do for mask in x m; do
    X=""; [ $mask = x ] && X="--exclude-flagged"
    python3 tools/tx_sorter_curve.py --truth benchmark-tx/birago1572-no87.truth.tsv \
      --base benchmark-tx/outputs/birago1572-no87/labels.tsv --lines $L --map $MAP --clusters $A/clusters.tsv \
      --signals $SG --propagate $mode $X --out $O/curve_birago1572-no87_${unit}_${mode}_${mask}.tsv --json $O/summary_${unit}_${mode}_${mask}.json > /dev/null
  done; done
done
