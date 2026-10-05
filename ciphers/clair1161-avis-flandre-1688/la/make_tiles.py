#!/usr/bin/env python3
"""D2-C1161LA (5 Oct 2026): flag the look-alike tiles (packet-format la/c1161la_tiles.tsv) and build the crop manifest.
A tile = a passC position whose two readers split (status split/split_gap) with th, z, S or 4 on any side (merged, A, B).
Candidates = A, B, merged + merged label's two most frequent confusion partners (la/confusion.tsv), as in
tools/lookalike_pass.py packet. Crops: la/crops/<line>_sN.jpg symlinks to images/ (c186R block lines -> c186Rblk crops),
la/crops/manifest.json carrying each crop's source box for `lookalike_pass.py windows --manifest`.
Shape descriptions for the value-blind prompt: la/desc.tsv from tx/labels_v2.md.
  python3 la/make_tiles.py
"""
import csv, collections, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
TG = {"th", "z", "S", "4"}
rd = lambda p: list(csv.DictReader(open(p), delimiter="\t"))
al, conf = rd(os.path.join(HERE, "align_abc.tsv")), rd(os.path.join(HERE, "confusion.tsv"))
part = collections.defaultdict(list)
for r in conf:
    part[r["label_a"]].append(r["label_b"]); part[r["label_b"]].append(r["label_a"])
seq = collections.defaultdict(list)
for r in al:
    seq[r["passage"]].append(r["merged"])
tiles = []
for r in al:
    if not r["status"].startswith("split") or not (TG & {r["merged"], r["idA"], r["idB"]}):
        continue
    lab, i, s = r["merged"], int(r["pos"]), seq[r["passage"]]
    cand = [x for x in dict.fromkeys([r["idA"], r["idB"], lab] + part[lab][:2]) if x]
    tiles.append(dict(run="c1161la", passage=r["passage"], pos=r["pos"], passC=lab, A=r["idA"], B=r["idB"],
                      status="split", why="split", candidates=",".join(cand), before=" ".join(s[max(0, i - 4):i - 1]),
                      after=" ".join(s[i:i + 3]), noteA="", noteB=""))
with open(os.path.join(HERE, "c1161la_tiles.tsv"), "w") as f:
    w = csv.DictWriter(f, fieldnames=list(tiles[0]), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(tiles)
# crops
m = json.load(open(os.path.join(T, "images", "manifest.json")))
cd = os.path.join(HERE, "crops"); os.makedirs(cd, exist_ok=True); ents = []
for e in m["iiif_lines"]:
    c = e["crop"]
    if "debug" in c or c.startswith("c186R_") or c.startswith("c186Rmarg"):
        continue
    name = c.replace("c186Rblk_", "c186R_")
    dst = os.path.join(cd, name)
    if not os.path.lexists(dst):
        os.symlink(os.path.join("..", "..", "images", c), dst)
    ents.append(dict(crop=name, box=e.get("box"), source=c))
json.dump({"iiif_lines": ents}, open(os.path.join(cd, "manifest.json"), "w"), indent=0)
# descriptions
D = {}
for ln in open(os.path.join(T, "tx", "labels_v2.md")):
    mm = re.match(r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$", ln.strip())
    if mm and mm.group(1) not in ("label", "---"):
        for lab in mm.group(1).split():
            D[lab] = mm.group(2)
D.update({"a": "small a", "o": "small raised o", "x": "x", "l": "small l / dotless-i stroke", "f": "f with a descender",
          "0": "digit 0", "2": "digit 2 (with a hook arc)", "3": "digit 3 (includes a z-like 3)", "4": "digit 4",
          "6": "digit 6", "7": "digit 7", "8": "digit 8"})
D.update({"s": "small s / small long-s, much smaller than S, often just before z", "vdash": "v-like stroke with a short dash",
          "8S": "an 8 joined to an S-curl (free description)", "Rloop": "R-like sign with a loop (free description)"})
used = sorted({c for t in tiles for c in t["candidates"].split(",")})
with open(os.path.join(HERE, "desc.tsv"), "w") as f:
    for u in used:
        f.write(f"{u}\t{D.get(u, '(no sheet description; judge by the label name)')}\n")
print(len(tiles), "tiles;", collections.Counter(t["passC"] for t in tiles).most_common(), "; crops", len(ents))
print("no desc:", [u for u in used if u not in D])
