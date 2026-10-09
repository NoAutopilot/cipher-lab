# PREREG-V-MANT0490L (9 Oct 2026, 19:3x UTC by date -u, verifier V-MANT0490L, LANE FAMILY-A2k account 2; written before the score below is computed)

Rule-3 shuffle check on gate (b) of MANT-0490L (brief: "score the shuffled-target decode through the same judge; a PASS on the shuffle voids
the judge for this family at N=38").
Input: f0490_08/judge_L/ciphertext.tsv as committed at d2356c289 (FIX-YEYE), the 37 keyed letter tokens of the gutter run in block_1
(the '7'... order as gated; 356 nonletter excluded exactly as judge_gate_L.py does).
Statistic: exactly judge_gate_L.py's block test at L = 38 (fr18 4-gram score of the key.tsv decode vs 1000 permuted keys on the same token
list, PASS if real > p95), applied to the token list after a uniform random shuffle of token ORDER (the control varies the 4-gram score,
which depends on order, so it can differ from the target).
Draws: 200 order shuffles, seeds 1-200 (shuffle) with the permuted-key seed 490 for every draw (as the target).
Decision: the judge stays a usable gate for this family at N=38 only if the shuffled decode PASSes in <= 5% of draws (10/200; the gate's own
nominal false-positive rate). Above 10/200 -> judge VOID as a gate for this design at N=38, gate (b)'s PASS licenses nothing, the gutter
tokens fall from S to M in the audit. Reported either way: the pass count, the median shuffled real score, the target's -1.477.
Script: f0490_08/vmant0490L_shuffle.py (writes vmant0490L_shuffle.out; --check).
