#!/usr/bin/env python3
"""VERIFY-F61-V13: build the blind sheets from tiles/ (cut.py). Panel A: 15 references (W1) under shuffled letters; panel B: the same minus
CROSS, LL and the 4-over-hash (the three classes runner 16 chose). Items get random 3-digit ids (seed 20261329). The answer key is written
OUTSIDE the repository (argv[1]) and only its sha256 is printed; sheets go to sheets/ (not committed; rerun to regenerate)."""
import csv, hashlib, json, os, random, sys
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); T = f"{HERE}/tiles"; OUT = f"{HERE}/sheets"; os.makedirs(OUT, exist_ok=True)
rnd = random.Random(20261329)
REFS = ["R_4STEM", "R_CROSS", "R_4PI", "R_HASHL", "R_HASH4O", "R_LL", "R_PHI", "R_C43", "R_ZHOOK", "R_4TRI", "R_BETA", "R_VBARA"]
DROP_B = {"R_CROSS", "R_LL", "R_HASH4O"}
TARGETS = [f"{t}_{w}" for t in ("T_L11_8", "T_L01_11", "T_L02_0") for w in ("W1", "W2", "W3")]
REPEATS = ["T_L11_8_W1", "T_L01_11_W1", "T_L02_0_W1"]
INSPAN_A = ["R_CROSS_W2", "R_4PI_W2", "R_LL_W3"]
ANCH_A = ["A_4STEM_W1", "A_HASHL_W1", "A_HASH4O_W1", "A_CROSS_W1", "A_4PI_W1", "A_PLAIN_IL_W1", "A_PLAIN_LES_W1", "A_C43_W2", "A_PHI_W2",
          "A_ZHOOK_W2", "A_4TRI_W2", "A_4STEM_W3", "A_HASH4O_W3"]
ITEMS_B = ["R_CROSS_W3", "R_LL_W2", "A_HASH4O_W2", "A_4STEM_W2", "A_4PI_W2", "T_L11_8_W2", "T_L01_11_W2", "T_L02_0_W2"]
def panel(refs, name):
    letters = list("ABCDEFGHJKLM")[:len(refs)]; order = refs[:]; rnd.shuffle(order); lab = dict(zip(letters, order))
    ts = [(l, Image.open(f"{T}/{lab[l]}_W1.png")) for l in letters]; cw = max(t.width for _, t in ts) + 12
    o = Image.new("L", (6 * cw, 2 * 215), 255); d = ImageDraw.Draw(o)
    for i, (l, t) in enumerate(ts): o.paste(t, ((i % 6) * cw, (i // 6) * 215)); d.text(((i % 6) * cw + 4, (i // 6) * 215 + 184), f"[{l}]", fill=0)
    o = o.resize((o.width * 3 // 2, o.height * 3 // 2)); o.save(f"{OUT}/{name}.png"); return {l: r.replace("R_", "") for l, r in lab.items()}
def items(names, prefix):
    ids = rnd.sample(range(100, 1000), len(names)); pairs = list(zip(ids, names)); rnd.shuffle(pairs); key = {}
    for k in range(0, len(pairs), 7):
        chunk = pairs[k:k + 7]; ts = [(i, Image.open(f"{T}/{n}.png")) for i, n in chunk]; cw = max(t.width for _, t in ts) + 12
        o = Image.new("L", (len(ts) * cw, 215), 255); d = ImageDraw.Draw(o)
        for j, (i, t) in enumerate(ts): o.paste(t, (j * cw, 0)); d.text((j * cw + 4, 186), f"#{i}", fill=0)
        o = o.resize((o.width * 3 // 2, o.height * 3 // 2)); o.save(f"{OUT}/{prefix}_{k // 7 + 1}.png")
    for i, n in pairs: key[str(i)] = n
    return key
if __name__ == "__main__":
    key = {"panelA": panel(REFS, "panelA"), "itemsA": items(TARGETS + REPEATS + INSPAN_A + ANCH_A, "itemsA"),
           "panelB": panel([r for r in REFS if r not in DROP_B], "panelB"), "itemsB": items(ITEMS_B, "itemsB")}
    s = json.dumps(key, indent=1, sort_keys=True); open(sys.argv[1], "w").write(s); print("key sha256", hashlib.sha256(s.encode()).hexdigest())
    print(sorted(os.listdir(OUT)))
