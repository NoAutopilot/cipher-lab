#!/usr/bin/env python3
"""MONL-KING2 exploratory placement (PREREG-MONL-KING2.md 'Secondary', not gated): longest exact run of the straight key decode
inside clear_f166.tsv and clear_f140.tsv vs 200 word-shuffled copies (seed 166); known-place control c268 L01-L10 vs f.140."""
import json, random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; T = HERE.parent
sys.path.insert(0, str(T)); sys.path.insert(0, str(HERE))
import king_f166 as KF, king2_score as ks
key = ks.load_key()
def dec(p, lines=None): return "".join(ks.decode(ks.load_tokens(p, lines), key))
out = []
for name, d, clear in (("c268 L01-L10 (control)", dec("ciphertext_c268.tsv", {f"L{i:02d}" for i in range(1, 11)}), "clear_f140.tsv"),
                       ("c258 L01-L10", dec("ciphertext_c258.tsv"), "clear_f166.tsv"),
                       ("c258 L01-L10", dec("ciphertext_c258.tsv"), "clear_f140.tsv")):
    ws = KF.letter(clear); text = "".join(ws); r = KF.longest_run(d, text)
    rng = random.Random(166); nl = []
    for _ in range(200):
        w = ws[:]; rng.shuffle(w); nl.append(KF.longest_run(d, "".join(w)))
    out.append({"read": name, "clear": clear, "run": r, "null_max": max(nl), "null_p95": sorted(nl)[189], "placed_run": r > max(nl)})
    print(json.dumps(out[-1]), flush=True)
(HERE / "results_king2_place.json").write_text(json.dumps(out, indent=1) + "\n")
