#!/bin/sh
# AX-4612 H1: block_homophonic width 5, offsets 0-4, control first (gate 0.6), 3 seeds, 8 restarts.
cd "$(dirname "$0")/../../.." || exit 1
for o in 0 1 2 3 4; do
  python3 tools/family_run.py specs/lodewijk-4612.json --family block_homophonic --param width=5 --param offset=$o \
    --param gap=80 --seeds 3 --restarts 8 --gate 0.6 --label "AX-4612 H1 w5 o$o"
  echo "exit $?"
done
