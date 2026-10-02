# BIRAGO-NUM3 dev log (solver settings tuned on dev seeds 101/102 only; the gate seeds 1-3 were not looked at before the gate run)

All on synthetic it16dip controls in the target's own 48 run lengths (985 digits), 5% strays. Recovery = right phase AND right letter.

| version | cells | restarts | iters/iters2/rounds | seed 101 | seed 102 |
|---|---|---|---|---|---|
| P(pair) prior | 55 | 8 | 30000/10000/4 | 0.077 | 0.342 |
| P(pair) prior | 55 | 8 | 100000/30000/8 | 0.097 | 0.691 |
| P(pair) prior | 40 | 8 | 100000/30000/8 | 0.927 | 0.913 |
| P(pair) prior | 55 | 32 | 100000/30000/8 | 0.054 | 0.844 |
| P(pair) prior, lam 0.5 | 55 | 32 | 200000/50000/8 | 0.120 | (killed) |
| P(pair given letter) (committed) | 55 | 8 | 100000/30000/8 | 0.000 | 0.558 |

Objective check, seed 101, 55 cells (scratch oracle.py): with the P(pair) prior the TRUE cut+key scored -3388.6, BELOW the
solver's wrong answer (-3328.9) -- a miscalibrated objective, fixed by the P(pair | letter) homophone term. After the fix the
true cut scores -2142.9 and the solver's wrong answer -2136.5: still level, so at 55 cells over ~476 pairs the joint
objective does not separate the true phase from a whole-stream phase flip. That is a model limit at this length, not a
search limit (an anneal on the TRUE cut alone reads 0.918 on the same seed). Failures are bimodal: a seed either locks the
right phase (0.83-0.93) or the wrong one (0.00-0.23).
