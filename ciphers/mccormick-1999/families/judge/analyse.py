"""analyse.py -- MCC-JUDGE: margin rule of PREREG-MCC-JUDGE.md on ncbe_null.json, and the judge renderings (A, B) of the
target and of the two shuffled-control decodes (draws 7000 and 8000). Usage: python3 analyse.py ncbe_null.json"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ncbe_null import render  # noqa: E402

d = json.load(open(sys.argv[1]))
t = d["target"]
res = {}
for st in ("coverage", "spl"):
    nc = [r[st] for r in d["ncbe"]]; tm = [r[st] for r in d["tm"]]
    mn, mt = sum(nc) / len(nc), sum(tm) / len(tm)
    res[st] = {"target": t[st], "ncbe_mean": mn, "ncbe_p95": sorted(nc)[int(0.95 * len(nc)) - 1], "ncbe_max": max(nc),
               "p_ncbe": (1 + sum(x >= t[st] for x in nc)) / (len(nc) + 1),
               "tm_mean": mt, "tm_max": max(tm), "p_tm": (1 + sum(x >= t[st] for x in tm)) / (len(tm) + 1),
               "share_ncbe": (mn - mt) / (t[st] - mt)}
above = all(res[s]["target"] > res[s]["ncbe_max"] for s in res)
neg = all(res[s]["p_ncbe"] >= 0.05 for s in res)
res["outcome"] = "not carried by NCBE alone" if above else ("carried by NCBE" if neg else "mixed")
print(json.dumps(res, indent=1))
out = Path(sys.argv[1]).parent
dec = {"target": t["decode"], "ncbe7000": next(r for r in d["ncbe"] if r["seed"] == 7000)["decode"],
       "tm8000": next(r for r in d["tm"] if r["seed"] == 8000)["decode"]}
for name, s in dec.items():
    for tag, ro in (("A", False), ("B", True)):
        (out / f"render_{name}_{tag}.txt").write_text(render(s, ro) + "\n")
