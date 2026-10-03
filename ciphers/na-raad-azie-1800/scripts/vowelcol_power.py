#!/usr/bin/env python3
"""A2-RAA8 post-hoc (NOT pre-registered): POS power of the vowel-column order test at larger N.
Same G, model and held-out file as vowelcol_test.py; 20 windows, 200 permutations, seed 20261003."""
import random, sys
from pathlib import Path
sys.argv = [sys.argv[0]]
import importlib.util
spec = importlib.util.spec_from_file_location("vt", Path(__file__).with_name("vowelcol_test.py"))
src = Path(spec.origin).read_text().split("rng = random.Random(SEED)")[0]
ns = {"__file__": spec.origin}; exec(src, ns)
for n in (370, 740, 1110):
    rng = random.Random(20261003)
    st = rng.sample(range(0, len(ns["held"]) - 15000), 20)
    ps = [ns["test"](ns["vowels"](ns["held"][s:s + 15000])[:n], rng)[1] for s in st]
    print(f"N={n}\tPOS power {sum(p < .05 for p in ps)}/20")
