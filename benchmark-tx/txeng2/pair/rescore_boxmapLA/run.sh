#!/bin/sh
# BOXMAP-RESCORE (others), 11 Oct 2026, account 3: TXE2-PAIR X2 (secure-tile training) and X2b (dev_tune training, LOLO) re-run with
# only --map changed (atlas/no87_box_token_labelaware.tsv). With the old map the same commands reproduce all 30 committed files
# (passX2*/passX2b* outputs, touched and train reports) byte for byte (checked 11 Oct 2026). From the repo root:
#   sh benchmark-tx/txeng2/pair/rescore_boxmapLA/run.sh
set -e
M=ciphers/nevers-birago-fr3251-1572/atlas/no87_box_token_labelaware.tsv
X2=benchmark-tx/txeng2/pair/rescore_boxmapLA; X2B=benchmark-tx/txeng2/pair2/rescore_boxmapLA
python3 tools/tx_pair_clf.py apply --unit dev_tune --map $M --out-dir $X2 --touched-dir $X2
python3 tools/tx_pair_clf.py control --unit dev_tune --map $M --out-dir $X2 --touched-dir $X2
python3 tools/tx_pair_clf.py apply --unit dev_tune --train-domain dev_tune --loo-lines --map $M --out-dir $X2B --touched-dir $X2B
python3 tools/tx_pair_clf.py control --unit dev_tune --train-domain dev_tune --loo-lines --map $M --out-dir $X2B --touched-dir $X2B
for f in $X2/passX2_pair_dev_tune.tsv $X2/passX2_pair_ctrl?_dev_tune.tsv $X2B/passX2b_pair2_dev_tune.tsv $X2B/passX2b_pair2_ctrl?_dev_tune.tsv; do
  printf '%s\t' "$(basename $f)"; python3 tools/tx_bench.py $f --bench BENCHMARK-TX.tsv --item birago1572-no87 --exclude-flagged \
    --coverage-diagnostic --paired benchmark-tx/txeng/units/labels_dev_tune.tsv | grep -m1 -o 'base wrong [0-9]*, output wrong [0-9]*; fixed [0-9]*, broken [0-9]*; exact p = [0-9.]*'
done
