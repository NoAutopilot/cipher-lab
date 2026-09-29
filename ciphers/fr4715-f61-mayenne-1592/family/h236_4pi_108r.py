#!/usr/bin/env python3
"""H236 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026): is f.108r's 4PI (f.61's hand; Tomokiyo's reprint of the leaf's period gloss reads it
d 4, p 1 at H202's aligned pairs, grade C) the '4 over a Pi' sign of f.61's two 4PI (H233: E) or the 4-head hash (f.101r's 4PI, H233: A)? Written before
the call.
 tiles SCRATCH NATIVE101 NATIVE188: f.108r's five 4PI pairs (h202_bowl_108r.pairs(), images/f108sheetB_<row>.jpg at pass A's segment/x, x +-150);
   f.61's two 4PI (H233's positions); anchors re-cut as h233 (H235's 4-head tiles 4, 2-hook tiles 4). H235/H233 normalisation, shuffled (seed 236),
   U01.., one sheet <scratch>/h236/. Key h236_items.tsv before the call; the runner does not look at the sheet.
 One blind Opus call, H233's prompt and five categories (A 4 over #, D 2#, E 4 not crossed by hash bars, B looped, N). Inline, no tools.
 score: GATE anchors >= 6/8. Pre-stated: "f.108r's 4PI is f.61's 4-over-Pi" iff >= 4 of the 5 f.108r 4PI answer E; "f.108r's 4PI is the 4-head hash"
   iff >= 4 answer A; else "mixed". f.61's two tokens reported (a repeat of H233). Descriptive; no merge.  tiles ... | score [--check]"""
import csv, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def tiles(scratch, n101, n188):
    from PIL import Image, ImageDraw, ImageOps
    import h202_bowl_108r as h202, h233_4pi_shape as h233
    its = []
    for t in [t for t in h202.pairs() if t["code"] == "4PI"]:
        im = Image.open(f"{HERE}/../images/f108sheetB_{t['row']}.jpg").convert("L"); st = (im.height + 12) // 4; y0 = (t["seg"] - 1) * st
        its.append((("f108r", t["row"], t["seg"], t["x"], "4PI", t["letter"], "T"), im.crop((t["x"] - 150, y0, t["x"] + 150, y0 + st - 12))))
    for cls, line, seg, x in h233.F61:
        if cls != "4PI": continue
        im = Image.open(f"{HERE}/../images/f61sheet_{line}.jpg").convert("L"); h = im.size[1] / 2
        its.append((("f61", line, f"s{seg}", x, "4PI", "-", "T"), im.crop((x - 150, int((seg - 1) * h) + 10, x + 150, int(seg * h) - 6))))
    N1 = Image.open(n101).convert("L"); N8 = Image.open(n188).convert("L")
    B1 = json.load(open(f"{HERE}/sheets/f101r_bands.json"))["boxes"]; B8 = json.load(open(f"{HERE}/sheets/f188r_bands.json"))["boxes"]
    for r in rd(f"{HERE}/h235_items.tsv"):
        if r["class"] in ("HASH4-A", "2HOOK"):
            N, B, pre = (N1, B1, "f101r") if r["class"] == "HASH4-A" else (N8, B8, "f188r")
            b = B[f"{pre}_{r['line']}_{r['segment']}.jpg"]; x = b[0] + int(r["x"]) // 2
            its.append(((pre, r["line"], r["segment"], r["x"], "ANCHOR-A" if r["class"] == "HASH4-A" else "ANCHOR-D", r["letter"], "C"), N.crop((x - 60, b[1], x + 60, b[3]))))
    random.Random(236).shuffle(its); os.makedirs(f"{scratch}/h236", exist_ok=True); W, cw, ch = 5, 300, 240
    sh = Image.new("L", (W * cw, ((len(its) + W - 1) // W) * ch), 255); d = ImageDraw.Draw(sh); key = ["item\tleaf\tline\tsegment\tx\tclass\tletter\tkind"]
    for j, (k, im) in enumerate(its):
        im = ImageOps.autocontrast(im.resize((int(im.size[0] * 180 / im.size[1]), 180)), cutoff=2); im.thumbnail((cw - 10, 180))
        X, Y = (j % W) * cw, (j // W) * ch; sh.paste(im, (X + 5, Y + 28)); mx = X + 5 + im.size[0] // 2
        d.polygon([(mx - 8, Y + 8), (mx + 8, Y + 8), (mx, Y + 24)], fill=0); d.polygon([(mx - 8, Y + 228), (mx + 8, Y + 228), (mx, Y + 212)], fill=0)
        d.text((X + 8, Y + 4), f"U{j + 1:02d}", fill=0); key.append(f"U{j + 1:02d}\t" + "\t".join(map(str, k)))
    sh.convert("RGB").save(f"{scratch}/h236/sheet_01.jpg", quality=90); open(f"{HERE}/h236_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "tiles")
def score():
    its = rd(f"{HERE}/h236_items.tsv"); ans = {r["id"]: r["answer"].strip().upper() for r in rd(f"{P}/h236_reply.tsv")}
    C = [r for r in its if r["kind"] == "C"]; hit = sum(ans.get(r["item"]) == ("A" if r["class"] == "ANCHOR-A" else "D") for r in C)
    out = [f"anchors: {hit} of {len(C)} (gate >= 6): {'PASS' if hit >= 6 else 'CONTROL FAIL'}"]
    if hit >= 6:
        T = [r for r in its if r["leaf"] == "f108r"]
        out.append("f.108r 4PI: " + "; ".join(f"{r['line']} x{r['x']} letter {r['letter']} -> {ans.get(r['item'], 'N')}" for r in T))
        out.append("f.61 4PI: " + "; ".join(f"{r['line']} x{r['x']} -> {ans.get(r['item'], 'N')}" for r in its if r["leaf"] == "f61"))
        e = sum(ans.get(r["item"]) == "E" for r in T); a = sum(ans.get(r["item"]) == "A" for r in T)
        out.append(f"read-out: E {e}, A {a} of {len(T)} -> " + ("f.108r's 4PI is f.61's 4-over-Pi" if e >= 4 else "f.108r's 4PI is the 4-head hash" if a >= 4 else "mixed"))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h236_4pi_108r_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(*sys.argv[2:5]) if sys.argv[1] == "tiles" else score()
