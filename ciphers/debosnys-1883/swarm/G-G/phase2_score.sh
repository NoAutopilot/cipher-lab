#!/bin/sh
# Held-out scoring of every committed Phase 2 key, both directions, with the frozen scorer.
cd "$(dirname "$0")"
for k in keys/KEY_fit_c1_*.tsv; do echo "$(basename $k) c1->c2: $(python3 ../score.py $k --fit c1 --test c2 | tee ${k%.tsv}.heldout.json | python3 summ.py)"; done
for k in keys/KEY_fit_c2_*.tsv; do echo "$(basename $k) c2->c1: $(python3 ../score.py $k --fit c2 --test c1 | tee ${k%.tsv}.heldout.json | python3 summ.py)"; done
