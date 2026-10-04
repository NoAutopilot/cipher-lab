#!/bin/sh
# NEAR3-C1POOL step (b), serial, order as pre-registered
cd "$(dirname "$0")/.."
for s in 1 2 3 4 5; do python3 pool/pool.py anneal --arm real --seed $s; done
for k in 1 2 3 4 5; do for s in 1 2; do python3 pool/pool.py anneal --arm shuf --shuf $k --seed $s; done; done
echo DONE
