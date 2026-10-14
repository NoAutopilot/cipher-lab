#!/usr/bin/env python3
"""SALV-MAP3 diagnostic (not pre-registered): whole-letter it16 4-gram score of the 2-of-3 key with each SALV-MAP3 row removed in
turn (the sign goes unread), against the full key. A row whose removal raises the score is not helping the 4-gram statistic."""
import csv, json, os, subprocess, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
new = [r["sign"] for r in csv.DictReader(open(os.path.join(D, "key_lasry.tsv"), encoding="utf-8"), delimiter="\t")
       if r["note"].startswith("SALV-MAP3") and r["class"] != "amb"]
sys.argv = ["x"]; import importlib.util
src = open(os.path.join(D, "score_lasry.py"), encoding="utf-8").read().split("tgt = scores(base)")[0]
g = {"__file__": os.path.join(D, "score_lasry.py")}; exec(src, g)
full = g["model"].score(g["text"](g["base"])); out = {"full": round(full, 4)}
for s in new:
    k = {a: b for a, b in g["base"].items() if a != s and not a.startswith(s + "|")}
    n = sum(1 for r in g["runs"] for _, x in r if x == s)
    out[s] = {"n": n, "without": round(g["model"].score(g["text"](k)), 4)}
json.dump(out, open(os.path.join(D, "map3", "ablate.json"), "w"), indent=1); print(json.dumps(out, indent=1))
