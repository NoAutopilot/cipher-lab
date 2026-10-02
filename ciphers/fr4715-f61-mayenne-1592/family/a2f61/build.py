#!/usr/bin/env python3
"""A2-F61 (2 Oct 2026): blind sheets for the L02-opening LL foil read. Reuses verify_v13/cut.py's tile() and V13 position rows unchanged, adds
one foil row (f.61 L07 in-word 'll' of '...della', placed by eye). Answer key goes OUTSIDE the repository (argv[1]); sha256 printed.
Sheets/tiles go to family/a2f61/sheets (not committed; rerun to regenerate, deterministic seed)."""
import hashlib, json, os, random, sys
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, f"{HERE}/../../verify_v13")
import cut
OUT = f"{HERE}/sheets"; os.makedirs(OUT, exist_ok=True); rnd = random.Random(20261002)
ROWS = {r["id"]: r for r in cut.rows()}
ROWS["F_LL_DELLA"] = {"id": "F_LL_DELLA", "src": "F61", "line": "L07", "pos": "w", "code": "PLAIN", "x": "1398", "y": "835", "role": "foil"}
REFS = ["R_4STEM", "R_CROSS", "R_4PI", "R_HASHL", "R_HASH4O", "R_LL", "R_PHI", "R_C43", "R_ZHOOK", "R_4TRI", "R_BETA", "R_VBARA"]
ITEMS = ([("T_L02_0", w) for w in ("W1", "W2", "W3")] + [("T_L02_0", "W1")] + [("F_LL_DELLA", w) for w in ("W1", "W2", "W3")] +
         [("F_LL_DELLA", "W1"), ("R_LL", "W3"), ("A_PLAIN_LES", "W1"), ("A_PLAIN_IL", "W1"), ("A_CROSS", "W1"), ("A_4PI", "W1"),
          ("A_C43", "W2"), ("A_PHI", "W2"), ("A_ZHOOK", "W2"), ("A_4TRI", "W2"), ("A_4STEM", "W1"), ("A_HASH4O", "W1")])
def t(i, w): return cut.tile(ROWS[i], w)
def panel():
    letters = list("ABCDEFGHJKLM"); order = REFS[:]; rnd.shuffle(order); lab = dict(zip(letters, order))
    ts = [(l, t(lab[l], "W1")) for l in letters]; cw = max(x.width for _, x in ts) + 12
    o = Image.new("L", (6 * cw, 2 * 215), 255); d = ImageDraw.Draw(o)
    for k, (l, x) in enumerate(ts): o.paste(x, ((k % 6) * cw, (k // 6) * 215)); d.text(((k % 6) * cw + 4, (k // 6) * 215 + 184), f"[{l}]", fill=0)
    o.resize((o.width * 3 // 2, o.height * 3 // 2)).save(f"{OUT}/panel.png"); return {l: r.replace("R_", "") for l, r in lab.items()}
def items():
    ids = rnd.sample(range(100, 1000), len(ITEMS)); pairs = list(zip(ids, ITEMS)); rnd.shuffle(pairs)
    for k in range(0, len(pairs), 7):
        chunk = pairs[k:k + 7]; ts = [(i, t(*n)) for i, n in chunk]; cw = max(x.width for _, x in ts) + 12
        o = Image.new("L", (len(ts) * cw, 215), 255); d = ImageDraw.Draw(o)
        for j, (i, x) in enumerate(ts): o.paste(x, (j * cw, 0)); d.text((j * cw + 4, 186), f"#{i}", fill=0)
        o.resize((o.width * 3 // 2, o.height * 3 // 2)).save(f"{OUT}/items_{k // 7 + 1}.png")
    return {str(i): f"{n}_{w}" for i, (n, w) in pairs}
if __name__ == "__main__":
    key = {"panel": panel(), "items": items()}
    s = json.dumps(key, indent=1, sort_keys=True); open(sys.argv[1], "w").write(s); print("key sha256", hashlib.sha256(s.encode()).hexdigest())
    print(sorted(os.listdir(OUT)))
