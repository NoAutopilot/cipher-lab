#!/bin/sh
# DEB-SWARM-G hand-planted matched controls for the languages the harness has no control for (es, la), and pt as a
# cross-check against the harness PT-HOMO numbers. Real pooled sign curve (N 790, K 136, X kept), 15 pct noise,
# fitted on the c2-shaped part only; the key (restricted to fit signs) is put through the frozen scorer's own evaluate()
# on the c1-shaped part (1000 shuffles, both nulls) -- the c2 -> c1 held-out test -- and recovery is reported beside it.
# Models: each language's model WITHOUT its held-out file (ptv_f5: Garrett verse held out; es_f5: Tristana; la_f5: Zaluski t.3).
cd "$(dirname "$0")"
export HSA_PERTURB=0.2 HSA_T0=0.3
python3 gg.py hcontrol es --model es_f5 --noise 0.15 --seeds 4 --restarts 128 --iters 1500000 > keys/hc_es_n15.json &
python3 gg.py hcontrol la --model la_f5 --noise 0.15 --seeds 4 --restarts 128 --iters 1500000 > keys/hc_la_n15.json &
python3 gg.py hcontrol ptv --model ptv_f5 --noise 0.15 --seeds 4 --restarts 128 --iters 1500000 > keys/hc_pt_n15.json &
wait
