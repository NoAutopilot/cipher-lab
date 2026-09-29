#!/bin/sh
# DEB-SWARM-A exploratory: the word-space (a27) fit, real vs NULL, seeds 8-9, both directions (no harness control for this design).
cd "$(dirname "$0")"; S=../score.py
for sd in 8 9; do for t in c1 c2; do
  python3 fitkey.py real:$t keys/R27_${t}_s$sd.tsv --alpha 27 --seed $sd >/dev/null &
  python3 fitkey.py control:NULL:$t keys/N27_${t}_s$sd.tsv --alpha 27 --seed $sd >/dev/null &
done; wait; done
for sd in 8 9; do
  python3 $S keys/R27_c2_s$sd.tsv --fit c2 --test c1 | python3 summ.py | sed "s/^/real27 s$sd /"
  python3 $S keys/R27_c1_s$sd.tsv --fit c1 --test c2 | python3 summ.py | sed "s/^/real27 s$sd /"
  python3 $S keys/N27_c2_s$sd.tsv --control NULL --fit NULL.c2 --test NULL.c1 | python3 summ.py | sed "s/^/NULL27 s$sd /"
  python3 $S keys/N27_c1_s$sd.tsv --control NULL --fit NULL.c1 --test NULL.c2 | python3 summ.py | sed "s/^/NULL27 s$sd /"
done
