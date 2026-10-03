#!/bin/sh
# A2-PAL3, 3 Oct 2026: unconstrained solve + window list, then the crib test on the anchor's solver-optimum crib (A)
# and on 15 other windows, 6 restarts x 30000 iters (A2-PAL2's matched setting).
cd "$(dirname "$0")/.."
M=${M:-${TMPDIR:-/tmp}/fr4687_it16/it16_all.npz}  # built by ../run_full.sh
python3 cribs_window.py "$M" --list > runs_window/list.txt
for k in A $(seq 0 14); do python3 cribs_window.py "$M" --window $k > runs_window/w$k.txt; done
