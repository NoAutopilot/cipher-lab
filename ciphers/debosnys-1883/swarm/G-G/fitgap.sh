#!/bin/sh
# DEB-SWARM-G fit-gap diagnostic: in-sample per-char score of the same fit on a text and on its order-shuffled copy
# (same tokens, so same N, K and curve). A language text fits far better than its shuffle; the gap is the signal.
cd "$(dirname "$0")"; mkdir -p keys/gap
export HSA_PERTURB=0.2 HSA_T0=0.3
for sh in 1 2; do
  for t in S:c2 PT-HOMO-N15.c2; do
    n=$(echo $t | tr ':.' '__')
    python3 gg.py solve ptall_f5 $t --keep-x --shuffle $sh --restarts 128 --iters 1500000 --seed 31 > keys/gap/${n}_shuf$sh.log
  done
done
# es / la on the real c2 (added 04:1x): their real-order fits are the seed-sweep logs keys/seed/KEY_fit_c2_{esall,laall}_f5_xs_s2*.log
for sh in 1 2; do for m in esall_f5 laall_f5; do
  python3 gg.py solve $m S:c2 --keep-x --shuffle $sh --restarts 128 --iters 1500000 --seed 31 > keys/gap/S_c2_${m}_shuf$sh.log
done; done
