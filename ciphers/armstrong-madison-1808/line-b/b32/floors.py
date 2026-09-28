"""B32 floors 1-2 (the full run's process ended after floor 0): same solver, shuffled targets 901-902."""
import random, sys
sys.argv = ["x"]; import dict_solver as D
rng = random.Random(23)
for k in (2,):
    r2 = random.Random(900 + k); flat = [g for s in D.TARGET for g in s]; r2.shuffle(flat); it = iter(flat)
    sh = [[next(it) for _ in s] for s in D.TARGET]; s2, m2 = D.solve(sh, D.SIGNS, rng, 24, 25000)
    d2 = ["".join(m2[g] for g in s) for s in sh]
    print(f"shuffled floor {k}: score {s2:.1f}, dictionary words {sum(1 for d in d2 if d in D.DICT)}/54  e.g. {' '.join(d2[:10])}", flush=True)
