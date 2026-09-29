#!/bin/sh
# DEB-SWARM-A: base-family fold (real signs folded to inventory base before fitting), seeds 7-9, both directions,
# against NULL folded into random groups of the same size profile (matched null). a26 letters, S2.
cd "$(dirname "$0")"; S=../score.py
for sd in 7 8 9; do for t in c1 c2; do
  python3 fitkey.py real:$t keys/RF_${t}_s$sd.tsv --fold base --seed $sd >/dev/null &
  python3 fitkey.py control:NULL:$t keys/NF_${t}_s$sd.tsv --fold random:$t --seed $sd >/dev/null &
done; wait; done
for sd in 7 8 9; do
  python3 $S keys/RF_c2_s$sd.tsv --fit c2 --test c1 | python3 summ.py | sed "s/^/realF s$sd /"
  python3 $S keys/RF_c1_s$sd.tsv --fit c1 --test c2 | python3 summ.py | sed "s/^/realF s$sd /"
  python3 $S keys/NF_c2_s$sd.tsv --control NULL --fit NULL.c2 --test NULL.c1 | python3 summ.py | sed "s/^/NULLF s$sd /"
  python3 $S keys/NF_c1_s$sd.tsv --control NULL --fit NULL.c1 --test NULL.c2 | python3 summ.py | sed "s/^/NULLF s$sd /"
done
