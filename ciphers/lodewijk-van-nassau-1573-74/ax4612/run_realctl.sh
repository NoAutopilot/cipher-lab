#!/bin/sh
# AX-4612 extension: block_homophonic w5 o0 on real sibling letters (5811, 4610) cut to N=775, same settings as H1.
cd "$(dirname "$0")/../../.." || exit 1
for nr in 5811 4610; do
  python3 tools/family_run.py specs/lodewijk-4612.json --family block_homophonic --param width=5 --param offset=0 \
    --param gap=80 --seeds 3 --restarts 8 --gate 0.6 --cipher ciphers/lodewijk-van-nassau-1573-74/ax4612/realctl_$nr.tsv \
    --label "AX-4612 real-letter positive control $nr (key.tsv design) cut to N=775"
  echo "exit $?"
done
