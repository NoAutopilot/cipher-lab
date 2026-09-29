#!/usr/bin/env python3
"""VERIFY-F61-V11 part B (29 Sept 2026, written before the calls): fresh stem-foot bowl reads on fr.3982 f.101r and f.124r 4TRI tokens, tiles cut
by this verifier from the Gallica natives (btv1b9060543f f210 / f256; fr.3984 btv1b9060633d f328 for anchors, bands regenerated with cut_bands.py
per sheets/f176v_full/README.md), own tile format and own prompt (PREREG.md B). Anchors: h193_items.tsv CP/AN coordinates on f.176v (Desportes's hand,
known answer = period letter group). Pools: f.101r agreed 4TRI (recf101r draft, f101r_signsA geometry, as h365's pool incl. the H362 items);
f.124r agreed 4TRI (recf124r, f124r_signsA, f124r_drop excluded).
  python3 v11_bowl.py tiles SCRATCH      -> SCRATCH/cK/sheet_NN.jpg, v11_items.tsv
  python3 v11_bowl.py score [--check]    -> v11_bowl_result.txt (needs replies v11_reply_cK.tsv: id<TAB>answer)"""
import csv, json, os, random, string, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); FAM = f"{HERE}/../family"; P = f"{FAM}/passes"
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def pool(leaf, dy, drop_file=None):
    drop = {(r["line"], r["segment"]) for r in rd(f"{P}/{drop_file}")} if drop_file else set()
    A = {(r["line"], r["pos"]): r for r in rd(f"{P}/{leaf}_signsA.tsv")}; B = json.load(open(f"{FAM}/sheets/{leaf}_bands.json"))["boxes"]; out = []
    for r in rd(f"{P}/rec{leaf}/ciphertext_draft.tsv"):
        if r["sign"] != "4TRI" or not r["why"].startswith("agree"): continue
        a = A.get((r["line"], r["position"]))
        if not a or a["sign"] != "4TRI" or (a["line"], a["segment"]) in drop: continue
        bx = B[f"{leaf}_{a['line']}_{a['segment']}.jpg"]; out.append((leaf, r["line"], r["position"], bx[0] + int(float(a["x_px"])) // 2, bx[1] + dy))
    return out
def plan():
    t1 = pool("f101r", 80); t2 = pool("f124r", 70, "f124r_drop.tsv")
    r1 = random.Random(1111); r2 = random.Random(1112); T = r1.sample(t1, 40); U = r2.sample(t2, 24)
    anc = [r for r in rd(f"{FAM}/h193_items.tsv") if r["group"] in ("CP", "AN")]; cp = [a for a in anc if a["group"] == "CP"]; an = [a for a in anc if a["group"] == "AN"]
    calls = {"c1": (T[:20], T[:6], cp[:5] + an[:5]), "c2": (T[20:40], T[20:26], cp[5:] + an[5:]), "c3": (U, U[:6], cp[2:7] + an[2:7])}
    return calls, len(t1), len(t2)
def tile(img, x, y0, y1, w=110, sc=1.6):
    from PIL import Image, ImageDraw
    t = img.crop((x - w, y0, x + w, y1)); t = t.resize((int(t.width * sc), int(t.height * sc)))
    c = Image.new("RGB", (360, 262), "white"); c.paste(t.crop((0, 0, 352, min(t.height, 222))), (4, 36)); d = ImageDraw.Draw(c)
    mx = 4 + int(w * sc); d.polygon([(mx - 8, 16), (mx + 8, 16), (mx, 32)], fill=(0, 60, 220)); d.rectangle((0, 0, 359, 261), outline=(160, 160, 160))
    return c, d
def tiles(scratch):
    from PIL import Image, ImageDraw
    calls, n1, n2 = plan(); nat = {"f101r": Image.open(f"{FAM}/images/3982_f101r.jpg").convert("RGB"), "f124r": Image.open(f"{FAM}/images/3982_f124r.jpg").convert("RGB")}
    rid = random.Random(1113); used = set(); key = ["call\tid\trole\tleaf\tline\tpos_or_seg\tx\tgroup\trepeat_of"]
    def nid():
        while True:
            s = "".join(rid.choice(string.ascii_uppercase) for _ in range(3))
            if s not in used: used.add(s); return s
    for c, (tg, rep, an) in calls.items():
        items = [("T", t, "") for t in tg] + [("R", t, "") for t in rep] + [("A", a, a["group"]) for a in an]; random.Random(1114 + int(c[1:])).shuffle(items)
        ims = []; first = {}
        for role, it, grp in items:
            i = nid()
            if role == "A":
                im = Image.open(f"{scratch}/f176v/f176v_{it['line']}_{it['segment']}.jpg").convert("RGB"); x = int(it["x_px"])
                x = max(110, min(im.width - 110, x)); cv, d = tile(im, x, 0, im.height); key.append(f"{c}\t{i}\tanchor\t176v\t{it['line']}\t{it['segment']}\t{it['x_px']}\t{grp}\t")
            else:
                leaf, line, pos, x, yc = it; cv, d = tile(nat[leaf], x, yc - 75, yc + 60)
                k = (leaf, line, pos); rep_of = first.get(k, "") if role == "R" or k in first else ""
                if k not in first: first[k] = i
                key.append(f"{c}\t{i}\ttarget\t{leaf}\t{line}\t{pos}\t{x}\t\t{rep_of}")
            d.text((8, 6), i, fill=(0, 0, 0)); ims.append(cv)
        os.makedirs(f"{scratch}/{c}", exist_ok=True)
        for s in range(0, len(ims), 12):
            sh = Image.new("RGB", (4 * 360, 3 * 262), "white")
            for j, cv in enumerate(ims[s:s + 12]): sh.paste(cv, ((j % 4) * 360, (j // 4) * 262))
            sh.save(f"{scratch}/{c}/sheet_{s // 12 + 1:02d}.jpg", quality=90)
    open(f"{HERE}/v11_items.tsv", "w").write("\n".join(key) + "\n"); print("pools f101r", n1, "f124r", n2, "items", len(key) - 1)
if __name__ == "__main__":
    if sys.argv[1] == "tiles": tiles(sys.argv[2])
