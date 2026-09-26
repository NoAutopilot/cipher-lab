#!/bin/sh
# AX-4612 extension: calibrate H3 (free homophonic) -- its own shuffle floor on 4612, and the real letter 5811 cut to N=775.
cd "$(dirname "$0")/../../.." || exit 1
python3 tools/family_run.py specs/lodewijk-4612.json --family homophonic --param profile=target --seeds 3 --restarts 8 \
  --shuffle-target 1 --label "AX-4612 H3 shuffle floor"
echo "exit $?"
python3 tools/family_run.py specs/lodewijk-4612.json --family homophonic --param profile=target --seeds 3 --restarts 8 \
  --cipher ciphers/lodewijk-van-nassau-1573-74/ax4612/realctl_5811.tsv --label "AX-4612 H3 real 5811 N775"
echo "exit $?"
