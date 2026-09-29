#!/bin/sh
# DEB-SWARM-G Phase 2 fits (29 Sept 2026). Each key is fitted on ONE text only (c1 or c2, the scorer's own tokens),
# written to keys/KEY_fit_<text>_<model>_<xmode>.tsv; scoring is a separate step (phase2_score.sh), run after commit.
# xmode: xs = X kept as an ordinary sign (the harness controls' design); xn = X a null (keyed to empty, reads nothing).
cd "$(dirname "$0")"
export HSA_PERTURB=0.2 HSA_T0=0.3
for m in ptall_f5 esall_f5 laall_f5; do
  for t in c1 c2; do
    python3 gg.py solve $m S:$t --keep-x --restarts 128 --iters 1500000 --seed 11 --out keys/KEY_fit_${t}_${m}_xs.tsv > keys/KEY_fit_${t}_${m}_xs.log &
    python3 gg.py solve $m S:$t --restarts 128 --iters 1500000 --seed 11 --out keys/KEY_fit_${t}_${m}_xn.tsv > keys/KEY_fit_${t}_${m}_xn.log &
    wait
  done
done
