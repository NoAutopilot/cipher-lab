#!/usr/bin/env python3
"""Target runs T2-T3 for runs.tsv (23 Sept 2026): model score of the crib key, and a crib-seeded anneal
(S-grade signs of key.tsv fixed, all other signs free) with the control settings."""
import json, os, sys
import control as c
import subst_hillclimb as sh
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
tf = sh.load_cipher(os.path.join(HERE, "..", "ciphertext.txt"))
key = {}
for l in open(os.path.join(HERE, "..", "key.tsv")):
    if l.startswith(("#", "sign\t")) or not l.strip():
        continue
    s, v, g, _ = l.split("\t", 3); key[s] = (v, g)
# T2: score of the crib key over the read signs only (unread signs dropped from each fragment)
fr = [np.array([sh.IDX[key[t][0]] for t in f if key[t][0] != "?"]) for f in tf]
n = sum(len(x) for x in fr)
t2 = c.model.score_frags(fr) / n
fixed = {s: v for s, (v, g) in key.items() if g == "S"}
r = sh.anneal(tf, c.model, c.RESTARTS, c.ITERS, seed=2, fixed=fixed)
out = {"T2_crib_key_score_per_read_token": t2, "T2_read_tokens": n,
       "T3_seeded": {k: v for k, v in r.items() if k != "restart_scores"}}
json.dump(out, open(os.path.join(HERE, "target_crib_runs.json"), "w"), indent=1)
print(json.dumps({"T2": t2, "n": n, "T3": r["score_per_token"], "T3_reading": r["reading"],
                  "T3_free": {s: r["key"][s] for s in r["key"] if s not in fixed}}))
