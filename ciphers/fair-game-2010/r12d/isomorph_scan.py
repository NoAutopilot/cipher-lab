#!/usr/bin/env python3
"""R12D-FAIR (6 Oct 2026): isomorph scan of crib words against the Fair Game marked-letter strings.
Under simple substitution a plaintext word w can sit at offset i only if w's letter-repeat pattern equals the
ciphertext's at i..i+len(w)-1 (equal letters <-> equal letters). Counts consistent placements per crib, per
ciphertext order. Usage: python3 isomorph_scan.py [--null N]  (--null: same scan on N shuffles, for the expected count)."""
import random, sys, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ORDERS = {"scroll": open(os.path.join(HERE, "../test2/order_scroll.txt")).read().strip(),
          "column": open(os.path.join(HERE, "../test2/order_column.txt")).read().strip()}
CRIBS = ["DEMOCRACY", "DEMOCRACYONLYWORKSIFYOUDOYOURPART", "ONLYWORKS", "DOYOURPART", "YOURPART", "TAKEPART",
         "FAIRGAME", "VALERIE", "PLAME", "WILSON", "JOSEPHWILSON", "CIA", "IRAQ", "TRUTH", "SECRET", "SECRETS",
         "AGENT", "COVERT", "LIBBY", "CHENEY", "NIGER", "URANIUM", "YELLOWCAKE", "WASHINGTON", "AMERICA", "FREEDOM",
         "LIBERTY", "THEREISNO", "WATCHING", "PATRIOT", "DOUGLIMAN", "NAOMIWATTS", "SEANPENN", "HELLO", "CONGRATULATIONS"]
def pat(s):
    m = {}; return tuple(m.setdefault(ch, len(m)) for ch in s)
def scan(c, w):
    pw = pat(w); return [i for i in range(len(c) - len(w) + 1) if pat(c[i:i + len(w)]) == pw]
nnull = int(sys.argv[sys.argv.index("--null") + 1]) if "--null" in sys.argv else 0
out = {}
for name, c in ORDERS.items():
    for w in CRIBS:
        hits = scan(c, w)
        exp = None
        if nnull:
            rng = random.Random(1); tot = 0
            for _ in range(nnull):
                l = list(c); rng.shuffle(l); tot += len(scan("".join(l), w))
            exp = round(tot / nnull, 3)
        out.setdefault(w, {})[name] = {"hits": hits, "null_mean": exp}
for w, d in out.items():
    print(f"{w:34s} " + "  ".join(f"{k}: {v['hits']} (null {v['null_mean']})" for k, v in d.items()))
json.dump(out, open(os.path.join(HERE, "isomorph_scan.json"), "w"), indent=1)
