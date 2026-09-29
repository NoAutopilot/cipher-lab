#!/usr/bin/env python3
"""H195 (runner 7, 29 Sept 2026): H193's design for the hash family. Written before the call. f.176v ANCHORS: 10 agreed-HASH4 columns the DP pairs
with i (group I) and 10 with d or q (group DQ), seed 195; f.176r TARGETS: 40 agreed-HASH4 columns (h183 alignment). Marked strips as H193, key
h195_items.tsv; the runner looks only at the anchors by group (<scratch>/h195/anchors_by_group.jpg) to fix one yes/no question, written to
PROMPTS section H195 with h195_yes_group.txt before the call. Scoring: anchors >= 17/20, then the f.176r targets split by the answer and counted
{i} vs {d,q} under fol. 177r (Fisher).  python3 h195_hash_attr.py tiles SCRATCH | score [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import h193_attr as H, h190_4fam as h190
g = H.g
def tiles(scratch):
    from PIL import Image, ImageDraw
    pv, pr = H.data(); rng = random.Random(195)
    gi = [p for p in pv if p[0] == "HASH4" and p[2] == "i"]; gd = [p for p in pv if p[0] == "HASH4" and p[2] in "dq"]; tg = [p for p in pr if p[0] == "HASH4"]
    its = [("I", "176v", p) for p in rng.sample(gi, 10)] + [("DQ", "176v", p) for p in rng.sample(gd, 10)] + [("T", "176r", p) for p in rng.sample(tg, min(40, len(tg)))]
    rng.shuffle(its); os.makedirs(f"{scratch}/h195", exist_ok=True); key = ["item\tgroup\tleaf\tline\tsegment\tx_px\tletter"]; ims = []
    for n, (grp, leaf, (s, (l, sg, x), L)) in enumerate(its, 1):
        f = f"{scratch}/f176v/f176v_{l}_{sg}.jpg" if leaf == "176v" else f"{scratch}/f176r/f176_{l}_{sg}.jpg"
        im = Image.open(f).convert("RGB"); x0 = max(0, min(im.width - 300, x - 150)); t = im.crop((x0, 0, x0 + 300, im.height)).resize((360, int(im.height * 1.2)))
        c = Image.new("RGB", (370, 190), "white"); c.paste(t, (5, 0)); d = ImageDraw.Draw(c); mx = 5 + int((x - x0) * 1.2); y = min(t.height, 150)
        d.polygon([(mx - 9, y + 16), (mx + 9, y + 16), (mx, y + 2)], fill=(220, 0, 0)); d.text((6, y + 22), f"H{n:02d}", fill=(0, 0, 0))
        ims.append(c); key.append(f"H{n:02d}\t{grp}\t{leaf}\t{l}\t{sg}\t{x}\t{L}")
    for s in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 190), "white")
        for k, c in enumerate(ims[s:s + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 190))
        sh.save(f"{scratch}/h195/sheet_{s // 20 + 1:02d}.jpg", quality=88)
    anc = Image.new("RGB", (4 * 370, 6 * 190), "white"); k = 0
    for grp in ("I", "DQ"):
        for n, it in enumerate(its, 1):
            if it[0] == grp: anc.paste(ims[n - 1], ((k % 4) * 370, (k // 4) * 190)); k += 1
        k = 12
    anc.save(f"{scratch}/h195/anchors_by_group.jpg", quality=88)
    open(f"{HERE}/h195_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items; I pool", len(gi), "DQ pool", len(gd), "targets", len(tg))
def score():
    key = {r["item"]: r for r in g.rd(f"{HERE}/h195_items.tsv")}; ans = {r["item"]: r["answer"].strip().lower() for r in g.rd(f"{H.b.P}/h195_attribute.tsv")}
    yg = open(f"{HERE}/h195_yes_group.txt").read().strip(); anc = [m for m, r in key.items() if r["group"] in ("I", "DQ")]
    hit = sum((ans.get(m) == "yes") == (key[m]["group"] == yg) and ans.get(m) in ("yes", "no") for m in anc)
    out = [f"anchors: {hit} of {len(anc)} answer in their group's direction (gate >= 17): {'PASS' if hit >= 17 else 'CONTROL FAIL'}"]
    if hit >= 17:
        c = {"yes": [0, 0], "no": [0, 0]}
        for m, r in key.items():
            if r["group"] == "T" and ans.get(m) in c and r["letter"] in "idq": c[ans[m]][0 if r["letter"] == "i" else 1] += 1
        p = h190.fisher(c["yes"][0], c["yes"][1], c["no"][0], c["no"][1])
        out.append(f"f.176r targets: answer yes ({yg}-like) i {c['yes'][0]} d/q {c['yes'][1]}; answer no i {c['no'][0]} d/q {c['no'][1]}; Fisher p {p:.2g}")
    txt = "\n".join(out) + "\n"; p_ = f"{HERE}/h195_hash_attr_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p_) and open(p_).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p_, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else score()
