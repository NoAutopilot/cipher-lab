#!/usr/bin/env python3
"""Oracle ceiling for H66/H67: S (200 shuffles) on the control after deleting exactly its true null types,
on all lines and on one half of the lines; and S with no deletion. If the oracle is weak, no type selector can pass."""
import random, json, h66_null_types as H
H.T = 200; out = []
for q in (0.35, 0.5):
    for seed in range(1, 7):
        rng = random.Random(9900 + seed); lines, nq, nulls = H.control(q, rng); nz = set(nulls)
        clean = [[s for s in l if s not in nz] for l in lines]; clean = [l for l in clean if len(l) > 1]
        out.append(dict(q=q, seed=seed, S_raw=round(H.S(lines, rng), 2), S_oracle=round(H.S(clean, rng), 2),
                        S_oracle_half=round(H.S(clean[::2], rng), 2)))
        print(json.dumps(out[-1]), flush=True)
json.dump(out, open('oracle.json', 'w'), indent=1)
