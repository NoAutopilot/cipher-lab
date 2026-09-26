#!/bin/sh
# AX-4612 H3: free homophonic at the target's K, control profile matched to the target's own sign counts.
cd "$(dirname "$0")/../../.." || exit 1
python3 tools/family_run.py specs/lodewijk-4612.json --family homophonic --param profile=target \
  --seeds 3 --restarts 8 --gate 0.6 --label "AX-4612 H3 free homophonic"
echo "exit $?"
