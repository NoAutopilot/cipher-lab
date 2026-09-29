#!/usr/bin/env python3
"""H216 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026): H193's bowl question on every 4-family sign of fr.3983 f.108r L04-L06 (H108 draft,
scripts/f61recon108r_draft.tsv, 15 signs: 4TRI 1, C43 4, 4STEM 6, 4PI 4, as coded), f.61's hand, no letters. Written before the call. (The hash
half of the row is H212's: its 10 f.108r tiles are these L06 HASH4 positions, A 1 / B 9.)
 tiles SCRATCH: each sign cut from the local source image (L04/L05: images/src_ark_12148_btv1b9059406b_f195_1250_450_3600_720.jpg; L06:
   images/stitch_f108r_f195_1250_450_3600_860.jpg) at box x0 + x_px/3 (boxes from images/f108g|f108h bands json, scale 3), 250 native px wide,
   from 20 px below the box top to 20 px below its bottom (the 3x crops stop 34 px below the row and clip the bowl; 30 px pushed the item label off the cell), scaled 1.44, marker ABOVE
   pointing down (as H199), numbered P01.., shuffled (seed 216), one sheet <scratch>/h216/sheet_01.jpg; key h216_items.tsv committed before the call.
   Repeat control = H193's 60 strips.
 score: GATE repeat control >= 17/20, else CONTROL FAIL. Then bowl yes/no/n by pass code; per-position answers to h216_bowl_positions.tsv for H217.
   Descriptive.  python3 h216_bowl_108r.py tiles SCRATCH | score [--check]"""
import csv, json, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); IM = os.path.abspath(f"{HERE}/../images"); FAM = ("4TRI", "C43", "4STEM", "4PI")
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def tiles(scratch):
    from PIL import Image, ImageDraw
    B = {}
    for j in ("f108g/f108g_bands.json", "f108h/f108h_bands.json"): B.update(json.load(open(f"{IM}/{j}"))["boxes"])
    src = {"L04": "src_ark_12148_btv1b9059406b_f195_1250_450_3600_720.jpg", "L05": "src_ark_12148_btv1b9059406b_f195_1250_450_3600_720.jpg", "L06": "stitch_f108r_f195_1250_450_3600_860.jpg"}
    ts = [r for r in rd(f"{HERE}/../scripts/f61recon108r_draft.tsv") if r["sign"] in FAM]; random.Random(216).shuffle(ts)
    os.makedirs(f"{scratch}/h216", exist_ok=True); ims = []; key = ["item\tline\tposition\tcode"]; cache = {}
    for n, t in enumerate(ts, 1):
        nat = cache.setdefault(t["line"], Image.open(f"{IM}/{src[t['line']]}").convert("RGB"))
        bx = B[f"{'f108h' if t['line'] == 'L06' else 'f108g'}_{t['line']}_{t['segment']}.jpg"]; x = bx[0] + int(t["x_px"]) // 3
        y0, y1 = bx[1] + 20, min(nat.height, bx[3] + 20); s = 1.44; w = nat.crop((x - 125, y0, x + 125, y1)); w = w.resize((360, int((y1 - y0) * s)))
        c = Image.new("RGB", (370, 190), "white"); c.paste(w, (5, 20)); d = ImageDraw.Draw(c); mx = 5 + int(125 * s)
        d.polygon([(mx - 9, 2), (mx + 9, 2), (mx, 17)], fill=(220, 0, 0)); d.text((6, 20 + w.height + 3), f"P{n:02d}", fill=(0, 0, 0))
        ims.append(c); key.append(f"P{n:02d}\t{t['line']}\t{t['position']}\t{t['sign']}")
    sh = Image.new("RGB", (4 * 370, 5 * 190), "white")
    for k, c in enumerate(ims): sh.paste(c, ((k % 4) * 370, (k // 4) * 190))
    sh.save(f"{scratch}/h216/sheet_01.jpg", quality=88)
    open(f"{HERE}/h216_items.tsv", "w").write("\n".join(key) + "\n"); print(len(ts), "targets", Counter(t["sign"] for t in ts))
def score():
    ctl = {r["item"]: r for r in rd(f"{HERE}/h193_items.tsv")}; ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{HERE}/passes/h216_reply.tsv")}
    hit = sum((ans.get(m) == "yes") == (r["group"] == "CP") and ans.get(m) in ("yes", "no") for m, r in ctl.items() if r["group"] in ("CP", "AN"))
    out = [f"repeat control: {hit} of 20 f.176v anchors in their group's direction (gate >= 17): {'PASS' if hit >= 17 else 'CONTROL FAIL'}"]
    if hit >= 17:
        its = rd(f"{HERE}/h216_items.tsv"); t = defaultdict(Counter); pos = ["line\tposition\tcode\tbowl"]
        for r in sorted(its, key=lambda r: (r["line"], int(r["position"]))):
            a = ans.get(r["item"], "missing"); t[r["code"]][a] += 1; pos.append(f"{r['line']}\t{r['position']}\t{r['code']}\t{a}")
        out.append("by pass code: " + "; ".join(f"{c} yes {t[c]['yes']} no {t[c]['no']} n {t[c]['n']}" for c in sorted(t)))
        pp = f"{HERE}/h216_bowl_positions.tsv"; ptxt = "\n".join(pos) + "\n"
        if "--check" not in sys.argv: open(pp, "w").write(ptxt)
        elif not (os.path.exists(pp) and open(pp).read() == ptxt): print("check STALE (positions)"); sys.exit(1)
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h216_bowl_108r_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else score()
