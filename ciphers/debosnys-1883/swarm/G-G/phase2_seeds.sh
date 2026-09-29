#!/bin/sh
# DEB-SWARM-G: seed sweep, c2 -> c1 direction (the direction the control shows is reachable). Same method on the
# control (PT-HOMO-N15.c2, fit only on that part) and on the real c2; keys in keys/seed/, then held-out scoring.
cd "$(dirname "$0")"; mkdir -p keys/seed
export HSA_PERTURB=0.2 HSA_T0=0.3
fit(){ python3 gg.py solve $1 $2 $3 --restarts 128 --iters 1500000 --seed $4 --out keys/seed/$5.tsv > keys/seed/$5.log; }
for s in 21 22 23 24; do
  fit ptall_f5 PT-HOMO-N15.c2 --keep-x $s ctl_N15_c2_pt_s$s &
  fit ptall_f5 PT-HOMO.c2 --keep-x $s ctl_clean_c2_pt_s$s &
  fit ptall_f5 S:c2 --keep-x $s KEY_fit_c2_ptall_f5_xs_s$s &
  fit ptall_f5 S:c2 "" $s KEY_fit_c2_ptall_f5_xn_s$s &
  wait
  fit esall_f5 S:c2 --keep-x $s KEY_fit_c2_esall_f5_xs_s$s &
  fit esall_f5 S:c2 "" $s KEY_fit_c2_esall_f5_xn_s$s &
  fit laall_f5 S:c2 --keep-x $s KEY_fit_c2_laall_f5_xs_s$s &
  fit laall_f5 S:c2 "" $s KEY_fit_c2_laall_f5_xn_s$s &
  wait
done
