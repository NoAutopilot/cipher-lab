#!/usr/bin/env python3
"""A2-RAA10 post-hoc (NOT pre-registered): T's POS power at N=370 on 40 fresh held-out windows (seed 20261004),
because the registered v2 run met the 18/20 gate exactly while v1 (other windows, same T) gave 16/20."""
import random, sys
from pathlib import Path
sys.argv = [sys.argv[0]]
p = Path(__file__).with_name("vowelcol2_test.py")
src = p.read_text().split("rng = random.Random(SEED)")[0]
ns = {"__file__": str(p)}; exec(src, ns)
ns["STATS"].pop("X")
rng = random.Random(20261004)
st = rng.sample(range(0, len(ns["held_raw"]) - 8000), 40)
ps = [ns["test"](ns["pos_cells"](ns["held_raw"][s:s + 8000], rng), rng)["T"][1] for s in st]
print(f"T POS power N=370, 40 fresh windows: {sum(x < .05 for x in ps)}/40")
