#!/bin/sh
# DEB-SWARM-G variant: X plus h31's pictogram class as nulls (xp), and additionally the punctuation-like BLOB/HOOK-L/DASH-H (xq).
# Fit on c2 only (the direction the controls show is reachable); keys committed before phase2_xp_score.
cd "$(dirname "$0")"; mkdir -p keys/xp
export HSA_PERTURB=0.2 HSA_T0=0.3
for s in 41 42; do
  for m in ptall_f5 esall_f5 laall_f5; do
    python3 gg.py solve $m S:c2 --nulls X,PICT --restarts 128 --iters 1500000 --seed $s --out keys/xp/KEY_fit_c2_${m}_xp_s$s.tsv > keys/xp/KEY_fit_c2_${m}_xp_s$s.log &
    python3 gg.py solve $m S:c2 --nulls X,PICT,PUNCT --restarts 128 --iters 1500000 --seed $s --out keys/xp/KEY_fit_c2_${m}_xq_s$s.tsv > keys/xp/KEY_fit_c2_${m}_xq_s$s.log &
  done
  wait
done
