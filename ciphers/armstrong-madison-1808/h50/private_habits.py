#!/usr/bin/env python3
"""H50: are the target's two unreproduced oddities (ARM-CODES, HYPOTHESES.md 'Target stats') a habit of period PRIVATE
codes? ARM-CODES found neither in the Department tables or THE=972 usage. Statistics, on 369-group streams:
  z0   share of tokens >= 100 whose last digit is 0 (target 92/237 = 0.388; flat would be 0.10)
  d01  share of all tokens with last digit 0 or 1 (target 159/369 = 0.431)
  gap  distinct values in 900-1099 (target 4, against 8-16 per neighbouring hundred)
Reference: the Madrid legation usage (h32 + h42 + h47 reads with h47's duplicate guard; 1,738 groups) as 1,000 random
contiguous 369-group windows (letters keep their own vocabulary), and WE028 usage (h29, 250 groups, whole stream) for
the record. Reports each statistic's band (p05-p95) and the target's percentile.
usage: python3 h50/private_habits.py"""
import os, random, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "h49"))
import importlib.util
spec = importlib.util.spec_from_file_location("pl", os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "h49", "particle_list.py"))
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    pl = importlib.util.module_from_spec(spec); spec.loader.exec_module(pl)
def stats(s):
    big = [x for x in s if x >= 100]
    return {"z0": sum(x % 10 == 0 for x in big) / max(1, len(big)),
            "d01": sum(x % 10 in (0, 1) for x in s) / len(s),
            "gap": len({x for x in s if 900 <= x <= 1099})}
t = stats(pl.tgt); rnd = random.Random(50); W = []
for _ in range(1000):
    i = rnd.randrange(0, len(pl.leg) - 369); W.append(stats(pl.leg[i:i + 369]))
print(f"target: " + ", ".join(f"{k} {v:.3f}" if k != "gap" else f"{k} {v}" for k, v in t.items()))
for k in ("z0", "d01", "gap"):
    v = sorted(w[k] for w in W); pct = sum(x < t[k] for x in v) / len(v) * 100
    print(f"legation 369-windows {k}: p05 {v[50]:.3f} median {v[500]:.3f} p95 {v[950]:.3f}; target percentile {pct:.1f}")
w = stats(pl.we); print("WE028 usage (250 groups, whole): " + ", ".join(f"{k} {x:.3f}" for k, x in w.items()))
