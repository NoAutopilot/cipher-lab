#!/bin/sh
# DEB-SWARM-A: the same a26 fit on c2 (seeds 8-10) for the real text, NULL and FR-HOMO-N15, each scored c2->c1 by score.py.
# Matched comparison for the real c2->c1 number; every real seed is a logged attempt.
cd "$(dirname "$0")"; S=../score.py; mkdir -p keys work
for sd in 8 9 10; do
  python3 fitkey.py real:c2 keys/R_c2_s$sd.tsv --seed $sd >/dev/null &
  python3 fitkey.py control:NULL:c2 keys/N_c2_s$sd.tsv --seed $sd >/dev/null &
  python3 fitkey.py control:FR-HOMO-N15:c2 keys/F_c2_s$sd.tsv --seed $sd >/dev/null &
  wait
done
python3 fitkey.py control:NULL:c2 keys/N_c2_s7.tsv --seed 7 >/dev/null
for sd in 8 9 10; do python3 $S keys/R_c2_s$sd.tsv --fit c2 --test c1 | python3 summ.py | sed "s/^/real s$sd /"; done
for sd in 7 8 9 10; do python3 $S keys/N_c2_s$sd.tsv --control NULL --fit NULL.c2 --test NULL.c1 | python3 summ.py | sed "s/^/NULL s$sd /"; done
for sd in 8 9 10; do python3 $S keys/F_c2_s$sd.tsv --control FR-HOMO-N15 --fit FR-HOMO-N15.c2 --test FR-HOMO-N15.c1 | python3 summ.py | sed "s/^/FRN15 s$sd /"; done
