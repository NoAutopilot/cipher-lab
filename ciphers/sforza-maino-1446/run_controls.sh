#!/bin/sh
# Matched-control matrix, 23 Sept 2026. Usage: sh run_controls.sh MODEL.npz
# Same solver settings as every target run (SET below).
M=$1
SET="--restarts 16 --iters 300000"
for n in 1 2 3; do
  T68=control/ctl${n}_f68.truth.json; T70=control/ctl${n}_f70.truth.json
  python3 campaign.py C$n-joint --model $M --truth $T68 $T70 -- control/ctl${n}_f68.txt control/ctl${n}_f70.txt $SET
  python3 campaign.py C$n-f68-alone --model $M --truth $T68 -- control/ctl${n}_f68.txt $SET
  python3 campaign.py C$n-f70-alone --model $M --truth $T70 -- control/ctl${n}_f70.txt $SET
  python3 campaign.py C$n-joint-shuffled1 --model $M -- control/ctl${n}_f68.txt control/ctl${n}_f70.txt $SET --shuffle 1
done
python3 campaign.py C1-joint-shuffled2 --model $M -- control/ctl1_f68.txt control/ctl1_f70.txt $SET --shuffle 2
python3 campaign.py C1-joint-clearctx --model $M --truth control/ctl1_f68.truth.json control/ctl1_f70.truth.json -- control/ctl1_f68.txt control/ctl1_f70.txt $SET --context clear
# profile-matched design (IC 0.060, 26/27 types), added 23 Sept 2026
TP68=control/ctlP_f68.truth.json; TP70=control/ctlP_f70.truth.json
python3 campaign.py CP-joint --model $M --truth $TP68 $TP70 -- control/ctlP_f68.txt control/ctlP_f70.txt $SET
python3 campaign.py CP-f68-alone --model $M --truth $TP68 -- control/ctlP_f68.txt $SET
python3 campaign.py CP-f70-alone --model $M --truth $TP70 -- control/ctlP_f70.txt $SET
python3 campaign.py CP-joint-shuffled1 --model $M -- control/ctlP_f68.txt control/ctlP_f70.txt $SET --shuffle 1
