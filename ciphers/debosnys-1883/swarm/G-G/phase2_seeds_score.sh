#!/bin/sh
# Held-out c2 -> c1 scoring of the committed seed-sweep keys (phase2_seeds.sh): controls through --control, real directly.
cd "$(dirname "$0")"
for k in keys/seed/ctl_N15_c2_*.tsv; do echo "$(basename $k): $(python3 ../score.py $k --control PT-HOMO-N15 --fit PT-HOMO-N15.c2 --test PT-HOMO-N15.c1 | tee ${k%.tsv}.heldout.json | python3 summ.py)"; done
for k in keys/seed/ctl_clean_c2_*.tsv; do echo "$(basename $k): $(python3 ../score.py $k --control PT-HOMO --fit PT-HOMO.c2 --test PT-HOMO.c1 | tee ${k%.tsv}.heldout.json | python3 summ.py)"; done
for k in keys/seed/KEY_fit_c2_*.tsv; do echo "$(basename $k): $(python3 ../score.py $k --fit c2 --test c1 | tee ${k%.tsv}.heldout.json | python3 summ.py)"; done
