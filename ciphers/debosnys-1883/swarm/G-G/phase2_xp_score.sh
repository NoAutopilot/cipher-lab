#!/bin/sh
# Held-out c2 -> c1 scoring of the committed xp/xq keys (phase2_xp.sh).
cd "$(dirname "$0")"
for k in keys/xp/KEY_fit_c2_*.tsv; do echo "$(basename $k): $(python3 ../score.py $k --fit c2 --test c1 | tee ${k%.tsv}.heldout.json | python3 summ.py)"; done
