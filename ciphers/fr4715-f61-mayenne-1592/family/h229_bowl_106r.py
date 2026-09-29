#!/usr/bin/env python3
"""H229 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026): H221's bowl call again, at H199's own strip geometry, after H221's control failed
(6/10 at a 3x, x +-60 window). Written before the call.
 tiles SCRATCH NATIVE106: the same 33 f.106r 4-family targets and the same 10 f.108v anchors as H221 (h221_items.tsv, set h221b), every strip cut as
   h199_bowl_108v.py cuts: a 250-native-px window, from 20 px below the band box top to 30 px below its bottom, scaled 1.44, one red triangle above
   the sign pointing down (f.106r: x = box x0 + x_px/3, sheets/f106r_bands.json; anchors: H199's own boxes and x). Shuffled (seed 229), P01..,
   20 per sheet, <scratch>/h229/. Key h229_items.tsv committed before the call; the runner does not look at the sheets.
 One blind Opus vision call, H221's bowl prompt with 'one red triangle above' in place of 'two red triangles'. Inline, no tool use.
 score: GATE anchors >= 8/10 as H199's answer; then H221's read-out ("f.106r's 4-family codes follow the bowl" iff answered 4TRI >= 0.8 yes AND
   answered C43 >= 0.8 no; 4STEM reported). Descriptive; no key change.  python3 h229_bowl_106r.py tiles SCRATCH NATIVE106 | score [--check]"""
import csv, json, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def tiles(scratch, native):
    from PIL import Image, ImageDraw
    import h199_bowl_108v as h199, h221_shapes_106r as h221
    old = [r for r in rd(f"{HERE}/h221_items.tsv") if r["set"] == "h221b"]
    T = {(t["line"], t["pos"]): t for t in h221.targets()}; i199 = {r["item"]: r for r in rd(f"{HERE}/h199_items.tsv")}
    B = json.load(open(f"{HERE}/sheets/f106r_bands.json"))["boxes"]; B108 = {}
    for j in ("f108v3y_bands.json", "f108v3z_bands.json"): B108.update(json.load(open(f"{HERE}/sheets/{j}"))["boxes"])
    nat = Image.open(native).convert("RGB"); n108 = Image.open(f"{HERE}/images/3983_f108v.jpg").convert("RGB")
    its = [dict(r) for r in old]; random.Random(229).shuffle(its); os.makedirs(f"{scratch}/h229", exist_ok=True); ims = []
    key = ["item\tkind\tref\tline\tpos\tcode\tgroup"]; s = 1.44
    for n, r in enumerate(its, 1):
        if r["kind"] == "T":
            t = T[(r["line"], r["pos"])]; bx = B[f"f106r_{t['line']}_{t['seg']}.jpg"]; x = bx[0] + t["x"] // 3; im = nat
        else:
            t = i199[r["ref"]]; bx = B108[os.path.basename(h199.crop(t["line"], t["segment"]))]; x = bx[0] + int(t["x_px"]) // 3; im = n108
        y0, y1 = bx[1] + 20, bx[3] + 30; w = im.crop((x - 125, y0, x + 125, y1)).resize((360, int((y1 - y0) * s)))
        c = Image.new("RGB", (370, 250), "white"); c.paste(w.crop((0, 0, 360, min(w.height, 225))), (5, 20)); d = ImageDraw.Draw(c); mx = 5 + int(125 * s)
        d.polygon([(mx - 9, 2), (mx + 9, 2), (mx, 17)], fill=(220, 0, 0)); d.text((330, 4), f"P{n:02d}", fill=(0, 0, 0)); ims.append(c)
        key.append(f"P{n:02d}\t{r['kind']}\t{r['ref']}\t{r['line']}\t{r['pos']}\t{r['code']}\t{r['group']}")
    for s0 in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 250), "white")
        for k, c in enumerate(ims[s0:s0 + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 250))
        sh.save(f"{scratch}/h229/sheet_{s0 // 20 + 1:02d}.jpg", quality=88)
    open(f"{HERE}/h229_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "tiles", Counter(r["kind"] for r in its))
def score():
    its = rd(f"{HERE}/h229_items.tsv"); ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h229_reply.tsv")}
    C = [r for r in its if r["kind"] == "C"]; hit = sum(ans.get(r["item"]) == r["group"] for r in C)
    out = [f"anchors: {hit} of {len(C)} as H199's answer (gate >= 8): {'PASS' if hit >= 8 else 'CONTROL FAIL'}",
           "anchor answers: yes-anchors " + " ".join(ans.get(r["item"], "-") for r in C if r["group"] == "yes") + " | no-anchors " + " ".join(ans.get(r["item"], "-") for r in C if r["group"] == "no")]
    if hit >= 8:
        t = defaultdict(Counter)
        for r in its:
            if r["kind"] == "T": t[r["code"]][ans.get(r["item"], "missing")] += 1
        out.append("by code: " + "; ".join(f"{c} " + " ".join(f"{k} {v}" for k, v in sorted(t[c].items())) for c in sorted(t)))
        sh = lambda c, a: t[c][a] / max(1, t[c]["yes"] + t[c]["no"])
        ok = sh("4TRI", "yes") >= 0.8 and sh("C43", "no") >= 0.8
        out.append(f"read-out: 4TRI yes-share {sh('4TRI', 'yes'):.2f}, C43 no-share {sh('C43', 'no'):.2f}, 4STEM yes-share {sh('4STEM', 'yes'):.2f} -> " + ("f.106r's 4-family codes follow the bowl" if ok else "does not follow"))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h229_bowl_106r_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(*sys.argv[2:4]) if sys.argv[1] == "tiles" else score()
