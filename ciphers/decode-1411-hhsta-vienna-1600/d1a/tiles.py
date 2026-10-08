#!/usr/bin/env python3
"""D1A-D1411: check tiles_spec.tsv against the two numbers.tsv and the posthoc alignment (disputed tiles = replace ops,
exemplars = equal-block numbers graded ok), cut tiles, write a labelled placement sheet (worker only) and the blind
montages (neutral ids, shuffled seed 1411) plus d1a/tile_key.tsv (id -> spec row; never given to the reader).
  python3 d1a/tiles.py [--check-sheet OUT.jpg] [--montage]"""
import csv, difflib, os, random, sys
from PIL import Image, ImageDraw
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, "..")
def rows(p): return list(csv.DictReader(open(os.path.join(R, p)), delimiter="\t"))
def load(p):
    out = []
    for r in rows(p):
        t = r["token"].rstrip("?")
        if t.isdigit() and "intext" not in (r.get("note") or ""):
            out.append((r["line"], int(r["pos"]), int(t), r["grade"]))
    return out
p2, p5 = load("def1411/numbers.tsv"), load("d1411p5/numbers.tsv")
L = [x for x in p5 if x[0].startswith("p5L")]
sm = difflib.SequenceMatcher(None, [x[2] for x in p2], [x[2] for x in L], autojunk=False)
eq2, eq5, rep2, rep5 = set(), set(), set(), set()
for t, a0, a1, b0, b1 in sm.get_opcodes():
    if t == "equal":
        eq2 |= {p2[i][:2] for i in range(a0, a1)}; eq5 |= {L[i][:2] for i in range(b0, b1)}
    if t == "replace":
        rep2 |= {p2[i][:2] for i in range(a0, a1)}; rep5 |= {L[i][:2] for i in range(b0, b1)}
idx2 = {x[:2]: x for x in p2}; idx5 = {x[:2]: x for x in L}
spec = rows("d1a/tiles_spec.tsv"); bad = 0
for s in spec:
    k = (s["line"], int(s["pos"])); ix = idx2 if s["copy"] == "p2" else idx5
    x = ix.get(k)
    if x is None or x[2] != int(s["value"]): print("VALUE MISMATCH", s, x); bad += 1; continue
    if s["kind"] == "D" and k not in (rep2 if s["copy"] == "p2" else rep5): print("NOT A REPLACE", s); bad += 1
    if s["kind"] == "E" and (k not in (eq2 if s["copy"] == "p2" else eq5) or x[3] != "ok"): print("NOT AGREED/OK", s, x); bad += 1
print("spec rows", len(spec), "D", sum(s["kind"] == "D" for s in spec), "E", sum(s["kind"] == "E" for s in spec), "bad", bad)
def tile(s):
    im = Image.open(os.path.join(R, "images", s["crop"])).convert("L")
    return im.crop((int(s["x0"]), int(s["y0"]), min(int(s["x1"]), im.width), min(int(s["y1"]), im.height)))
def sheet(items, out, cols=6, cell=(260, 190)):
    n = len(items); rws = (n + cols - 1) // cols
    sh = Image.new("RGB", (cols * cell[0], rws * cell[1]), "white"); d = ImageDraw.Draw(sh)
    for i, (lab, t) in enumerate(items):
        t = t.copy(); t.thumbnail((cell[0] - 10, cell[1] - 30))
        x, y = (i % cols) * cell[0], (i // cols) * cell[1]
        sh.paste(t.convert("RGB"), (x + 5, y + 25)); d.text((x + 5, y + 5), lab, fill="black")
        d.rectangle([x, y, x + cell[0] - 1, y + cell[1] - 1], outline="gray")
    sh.save(out, quality=90)
if "--check-sheet" in sys.argv:
    sheet([(f'{s["kind"]} {s["op"]} {s["copy"]} {s["value"]}', tile(s)) for s in spec], sys.argv[sys.argv.index("--check-sheet") + 1])
if "--montage" in sys.argv:
    order = list(range(len(spec))); random.Random(1411).shuffle(order)
    os.makedirs(os.path.join(H, "montage"), exist_ok=True)
    with open(os.path.join(H, "tile_key.tsv"), "w") as f:
        f.write("id\t" + "\t".join(spec[0].keys()) + "\n")
        items = []
        for j, i in enumerate(order):
            tid = f"T{j+1:02d}"; f.write(tid + "\t" + "\t".join(spec[i].values()) + "\n"); items.append((tid, tile(spec[i])))
    for m in range(0, len(items), 20):
        sheet(items[m:m + 20], os.path.join(H, "montage", f"montage_{m // 20 + 1}.jpg"), cols=5, cell=(300, 220))
    print("montages", (len(items) + 19) // 20)
sys.exit(1 if bad else 0)
