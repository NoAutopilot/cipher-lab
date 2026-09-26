#!/bin/sh
# AX-4612 H2 (run because H1's control met the gate and every H1 target failed the judge):
# block_homophonic widths 4 and 6, every offset, control first (gate 0.6), 3 seeds, 8 restarts.
cd "$(dirname "$0")/../../.." || exit 1
for w in 4 6; do
  o=0
  while [ $o -lt $w ]; do
    python3 tools/family_run.py specs/lodewijk-4612.json --family block_homophonic --param width=$w --param offset=$o \
      --param gap=80 --seeds 3 --restarts 8 --gate 0.6 --label "AX-4612 H2 w$w o$o"
    echo "exit $?"
    o=$((o+1))
  done
done
