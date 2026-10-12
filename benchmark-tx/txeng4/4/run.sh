#!/bin/sh
# TXE4-4 SELF-CHECK run arguments (rule 7). Run from the repo root. Dev only; no eval output is produced.
set -e
W=benchmark-tx/txeng4/4; A=ciphers/nevers-birago-fr3251-1572/atlas
DEV="f178v_L01 f178v_L02 f178v_L03 f178v_L04 f178v_L05 f178v_L06 f178v_L07 f178v_L08 f178v_L09 f178v_L10 f178v_L11 f178v_L12"
python3 tools/tx_selfcheck.py map --atlas $A --read benchmark-tx/outputs/birago1572-no87/passA.tsv --pages f178r f178v f179r --out $W/no87
python3 tools/tx_selfcheck.py map --atlas $A --read benchmark-tx/outputs/birago1572-f152r/passA.tsv --pages 'f152r:1:L01=cx>2520:L04=cx<2460' --out $W/f152r
python3 tools/tx_selfcheck.py classify --atlas $A --read benchmark-tx/outputs/birago1572-no87/passA.tsv --kept $W/no87_kept.tsv --out $W/topk/no87_A.tsv
python3 tools/tx_selfcheck.py classify --atlas $A --read benchmark-tx/outputs/birago1572-f152r/passA.tsv --kept $W/f152r_kept.tsv --out $W/topk/f152r_A.tsv
for s in $(seq 1 20); do
  python3 tools/tx_selfcheck.py classify --atlas $A --read benchmark-tx/outputs/birago1572-no87/passA.tsv --kept $W/no87_kept.tsv --out $W/topk/no87_A_perm$s.tsv --permute $s
  python3 tools/tx_selfcheck.py classify --atlas $A --read benchmark-tx/outputs/birago1572-f152r/passA.tsv --kept $W/f152r_kept.tsv --out $W/topk/f152r_A_perm$s.tsv --permute $s
done
python3 tools/tx_selfcheck.py fit --topk $W/topk/no87_A.tsv --read benchmark-tx/outputs/birago1572-no87/passA.tsv --truth benchmark-tx/birago1572-no87.truth.tsv --lines $DEV --out $W/calib_fit.json
python3 tools/tx_selfcheck.py ece --topk $W/topk/no87_A.tsv --read benchmark-tx/outputs/birago1572-no87/passA.tsv --fit $W/calib_fit.json --truth benchmark-tx/birago1572-no87.truth.tsv --lines $DEV
python3 $W/grid.py
python3 $W/dev_controls.py
# beside: pass B and L on dev with the same frozen fit and rule
for P in B L; do
  R=benchmark-tx/outputs/birago1572-no87/pass$P.tsv; [ $P = L ] && R=benchmark-tx/outputs/birago1572-no87/labels.tsv
  python3 tools/tx_selfcheck.py map --atlas $A --read $R --pages f178r f178v f179r --out $W/no87$P
  python3 tools/tx_selfcheck.py classify --atlas $A --read $R --kept $W/no87${P}_kept.tsv --out $W/topk/no87_$P.tsv
  python3 tools/tx_selfcheck.py apply --topk $W/topk/no87_$P.tsv --read $R --fit $W/calib_fit.json --tau 0.8 --eps 0.1 --out $W/dev/${P}_tau0.8_eps0.1.tsv --lines $DEV
done
python3 tools/tx_power.py --unit no87eval=birago1572-no87:benchmark-tx/txeng/units/passA_eval_heldout.tsv --unit f152r=birago1572-f152r:benchmark-tx/outputs/birago1572-f152r/passA.tsv --pool pool=no87eval,f152r --fix 0.3,0.5 --alpha 0.05
