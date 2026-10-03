#!/bin/sh
# A2-PAL2, 3 Oct 2026: real target (-1) then 20 unit shuffles, 6 restarts x 30000 iters (box-sized; see NOTES.md).
cd "$(dirname "$0")/.."
M=${M:-${TMPDIR:-/tmp}/fr4687_it16/it16_all.npz}  # built by ../run_full.sh
for k in -1 $(seq 0 19); do python3 cribs_shuffle.py "$M" --shuffle $k --iters 30000 --restarts 6 > runs_shuffle/s$k.txt; done
