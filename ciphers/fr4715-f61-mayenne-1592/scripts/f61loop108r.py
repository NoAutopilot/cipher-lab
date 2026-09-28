#!/usr/bin/env python3
"""H108 call 4 (28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe): blind loop-arrangement classification of every
loop-on-stem sign (PHI, DBL, SBS, LOOPSTEM1, OTHER) in the reconciled f.108r L04-L06 draft (scripts/f61recon108r_draft.tsv),
with 18 control tiles from H26's own sort (scripts/read_call_QO.tsv: 9 G2 side-by-side, 9 G1/G3 drawn by seed 108), in the
H65 tile design (native crop 110 x 95 px around the sign, 3x, two red ticks; controls cut at the same scale from the 3x
sheets B). Tiles shuffled (seed 108), ten per sheet in images/h108/; the key scripts/f61loop108r_tiles.tsv is never named.

  python3 scripts/f61loop108r.py build
  python3 scripts/f61loop108r.py score scripts/read_call_H108.tsv [--check]   -> scripts/f61loop108r_result.txt, _relabel.tsv

Pre-registered (scripts/PROMPTS.md "H108", pushed before the call): control gate >= 15/18 on the side of H26's group
(G2 -> arrangement 'side by side'; G1/G3 -> single, stacked or trefoil; 'none'/other a miss). On a PASS every target the
reader puts 'side by side' becomes SBS, single/stacked/trefoil PHI, none/other keeps its draft code; on a FAIL no relabel.
"""
import csv, json, os, random, sys
import numpy as np
from PIL import Image, ImageDraw, ImageOps
HERE = os.path.dirname(os.path.abspath(__file__)); TGT = os.path.dirname(HERE); IMG = f"{TGT}/images"
LOOPS = {"PHI", "DBL", "SBS", "LOOPSTEM1", "OTHER"}; THR = 140
def rows(p): return list(csv.DictReader((l for l in open(p) if not l.startswith("#")), delimiter="\t"))
def target_tiles():
    st = Image.open(f"{IMG}/stitch_f108r_f195_1250_450_3600_860.jpg").convert("RGB"); out = []
    bj = {"L04": json.load(open(f"{IMG}/f108g/f108g_bands.json")), "L05": json.load(open(f"{IMG}/f108g/f108g_bands.json")),
          "L06": json.load(open(f"{IMG}/f108h/f108h_bands.json"))}
    for r in rows(f"{HERE}/f61recon108r_draft.tsv"):
        if r["sign"] not in LOOPS: continue
        L = r["line"]; j = bj[L]; pre = "f108g" if L != "L06" else "f108h"
        box = j["boxes"][f"{pre}_{L}_{r['segment']}.jpg"]; cx = box[0] + float(r["x_px"]) / j["scale"]; cy = box[1] + j["up"]
        g = np.asarray(st.crop((int(cx - 30), int(cy - 15), int(cx + 30), int(cy + 45))).convert("L"))
        pr = np.convolve((g < THR).sum(axis=1), np.ones(9) / 9, "same"); cy = cy - 15 + int(pr.argmax())
        t = st.crop((int(cx - 55), int(cy - 40), int(cx + 55), int(cy + 55))).resize((330, 285), Image.LANCZOS)
        out.append(("target", L, r["position"], r["sign"], r["segment"], r["x_px"], t))
    return out
def control_tiles(seed):
    qo = [r for r in rows(f"{HERE}/read_call_QO.tsv") if r.get("group") in ("G1", "G2", "G3")]
    rng = random.Random(seed); g2 = [r for r in qo if r["group"] == "G2"]; g13 = [r for r in qo if r["group"] != "G2"]
    pick = rng.sample(g2, min(9, len(g2))) + rng.sample(g13, 9); out = []
    for r in pick:
        im = Image.open(f"{IMG}/{r['sheet']}.jpg").convert("RGB"); a = np.asarray(im.convert("L"), float)
        bars = [i for i, v in enumerate(a.mean(axis=1)) if v < 40]; cuts = [0]
        for i in bars:
            if not cuts or i - cuts[-1] > 20: cuts.append(i)
        edges = [0] + [b + 12 for b in cuts[1:]]; segs = list(zip(edges, [c for c in cuts[1:]] + [a.shape[0]]))
        y0, y1 = segs[int(r["segment"]) - 1]; x = float(r["x_px"])
        g = a[y0:y1, max(0, int(x - 30)):int(x + 30)]; pr = np.convolve((g < THR).sum(axis=1), np.ones(27) / 27, "same")
        pk = [i for i in range(1, len(pr) - 1) if pr[i] >= pr[i - 1] and pr[i] >= pr[i + 1] and pr[i] >= 0.5 * pr.max()]
        cy = y0 + max(pk)   # the lowest strong ink peak: on f.108r the gloss rides ABOVE the cipher row
        paper = tuple(int(v) for v in np.median(np.asarray(im.crop((0, y0, im.width, y1))).reshape(-1, 3), axis=0))
        seg = Image.new("RGB", (im.width + 400, im.height + 400), paper); seg.paste(im.crop((0, y0, im.width, y1)), (200, y0 + 200))   # nothing outside the segment
        t = seg.crop((int(x - 165) + 200, int(cy - 120) + 200, int(x + 165) + 200, int(cy + 165) + 200))
        out.append(("control", r["sheet"], r["order_in_sheet"], r["group"], r["segment"], r["x_px"], t))
    return out
def build():
    tiles = target_tiles() + control_tiles(108); random.Random(108).shuffle(tiles)
    os.makedirs(f"{IMG}/h108", exist_ok=True); W, H = 330, 285 + 34
    for s in range(0, len(tiles), 10):
        sheet = Image.new("RGB", (5 * (W + 10), 2 * (H + 10)), "white"); d = ImageDraw.Draw(sheet)
        for k, tt in enumerate(tiles[s:s + 10]):
            t = ImageOps.autocontrast(tt[6].convert("L"), cutoff=1).convert("RGB"); dd = ImageDraw.Draw(t)   # grey, stretched: the f.61 sheets are colour, the f.108r ones grey   # grey for all: the f.61 sheets are colour, the f.108r ones grey
            dd.line([(165, 0), (165, 14)], fill=(220, 0, 0), width=3); dd.line([(165, t.height - 14), (165, t.height)], fill=(220, 0, 0), width=3)
            X, Y = (k % 5) * (W + 10), (k // 5) * (H + 10); sheet.paste(t, (X, Y + 34)); d.text((X + 6, Y + 6), f"tile {s + k + 1}", fill=(0, 0, 200))
            d.rectangle([X, Y + 34, X + W - 1, Y + 34 + t.height - 1], outline=(0, 0, 0))
        sheet.save(f"{IMG}/h108/loop_sheet{s // 10 + 1}.jpg", quality=88)
    with open(f"{HERE}/f61loop108r_tiles.tsv", "w") as f:
        f.write("tile\tkind\tline_or_sheet\tposition_or_order\tcode_or_h26group\tsegment\tx_px\n")
        for n, tt in enumerate(tiles, 1): f.write("\t".join(map(str, (n,) + tt[:6])) + "\n")
    print(f"{len(tiles)} tiles ({sum(t[0] == 'target' for t in tiles)} target, {sum(t[0] == 'control' for t in tiles)} control) on {(len(tiles) + 9) // 10} sheets images/h108/loop_sheet1..{(len(tiles) + 9) // 10}.jpg")
def side(a): return "side" in a.lower()
def score(path):
    key = {r["tile"]: r for r in rows(f"{HERE}/f61loop108r_tiles.tsv")}
    rd = {r["tile"].strip().replace("tile ", ""): r for r in rows(path)}
    ok = n = 0; lines, rel = [], []
    for t, k in key.items():
        a = rd.get(t, {}).get("arrangement", "none").strip()
        if k["kind"] == "control":
            n += 1; hit = (side(a) if k["code_or_h26group"] == "G2" else (not side(a) and a.split()[0].lower() in ("single", "two", "trefoil") if a else False))
            ok += hit; lines.append(f"control tile {t} {k['line_or_sheet']}/{k['position_or_order']} H26 {k['code_or_h26group']} -> '{a}' {'ok' if hit else 'MISS'}")
    gate = ok >= 15
    for t, k in sorted(key.items(), key=lambda kv: (kv[1]["line_or_sheet"], int(kv[1]["position_or_order"]) if kv[1]["kind"] == "target" else 0)):
        if k["kind"] != "target": continue
        a = rd.get(t, {}).get("arrangement", "none").strip(); al = a.lower()
        new = "SBS" if side(a) else ("PHI" if al.startswith(("single", "two stacked", "trefoil")) else k["code_or_h26group"])
        if not gate: new = k["code_or_h26group"]
        rel.append((k["line_or_sheet"], k["position_or_order"], k["code_or_h26group"], a, new))
    txt = [f"H108 loop classification: controls {ok}/{n} on H26's side; GATE (>= 15/18): {'PASS' if gate else 'FAIL'}"] + lines
    txt += [f"target {L}/{p}: draft {c} -> '{a}' -> {nw}" for L, p, c, a, nw in rel]
    from collections import Counter
    txt += ["relabel summary: " + " ".join(f"{a}->{b}:{m}" for (a, b), m in sorted(Counter((c, nw) for _, _, c, _, nw in rel).items()))]
    txt = "\n".join(txt) + "\n"; tsv = "line\tposition\tdraft\tarrangement\tcode\n" + "".join("\t".join(map(str, r)) + "\n" for r in rel)
    rp, tp = f"{HERE}/f61loop108r_result.txt", f"{HERE}/f61loop108r_relabel.tsv"
    if "--check" in sys.argv:
        good = os.path.exists(rp) and open(rp).read() == txt and open(tp).read() == tsv; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); open(tp, "w").write(tsv); print(txt, end="")

# H113 (28 Sept 2026, runner 5): the same 26 target tiles, controls from the f.108/family hands only -- 10 o + 10 e tiles of
# H65 (period gloss letters on f.101r/f.188r, cut back out of images/h65/sbs_sheet*.jpg, seed 113) and H26's f.108 signs
# (both G2 and 4 of G1/G3, seed 113). Gate (CAMPAIGN.md H113, pre-registered here before the call): >= 90% of controls
# on the expected side (o, G2 -> side by side; e, G1/G3 -> single/stacked/trefoil). On a PASS the targets are relabelled
# as in the H108 rule. build-h113 -> images/h113/loop_sheet*.jpg, scripts/f61loop108r_h113_tiles.tsv;
# score-h113 read_call_H113.tsv [--check] -> scripts/f61loop108r_h113_result.txt, _h113_relabel.tsv
def h65_tiles(seed):
    key = rows(f"{HERE}/f61sbs_tiles.tsv"); rng = random.Random(seed)
    o = [r for r in key if r["period_letter"] == "o"]; e = [r for r in key if r["period_letter"] == "e"]
    out = []
    for r in rng.sample(o, 10) + rng.sample(e, 10):
        k = int(r["tile"]) - 1; sh = Image.open(f"{IMG}/h65/sbs_sheet{k // 10 + 1}.jpg").convert("RGB"); j = k % 10
        X, Y = (j % 5) * 340, (j // 5) * 329 + 34
        t = sh.crop((X, Y, X + 330, Y + 285)); t = Image.composite(Image.new("RGB", t.size, "white"), t, Image.new("L", t.size, 0))
        a = np.asarray(t).copy(); red = (a[:, :, 0] > 150) & (a[:, :, 1] < 90) & (a[:, :, 2] < 90); a[red] = 255   # strip H65's ticks; ours are redrawn
        out.append(("control", r["leaf"], r["tile"], "period_" + r["period_letter"], r["segment"], r["x_px"], Image.fromarray(a)))
    return out
def build_h113():
    global IMG
    rng = random.Random(113); qo = [r for r in rows(f"{HERE}/read_call_QO.tsv") if r.get("group") in ("G1", "G2", "G3") and r["sheet"].startswith("f108")]
    g2 = [r for r in qo if r["group"] == "G2"]; g13 = rng.sample([r for r in qo if r["group"] != "G2"], 4)
    tiles = target_tiles() + h65_tiles(113) + [t for t in control_tiles_from(g2 + g13)]
    random.Random(113).shuffle(tiles); write_sheets(tiles, "h113", "f61loop108r_h113_tiles.tsv")
def control_tiles_from(pick):
    out = []
    for r in pick:
        im = Image.open(f"{IMG}/{r['sheet']}.jpg").convert("RGB"); a = np.asarray(im.convert("L"), float)
        bars = [i for i, v in enumerate(a.mean(axis=1)) if v < 40]; cuts = [0]
        for i in bars:
            if not cuts or i - cuts[-1] > 20: cuts.append(i)
        edges = [0] + [b + 12 for b in cuts[1:]]; segs = list(zip(edges, [c for c in cuts[1:]] + [a.shape[0]]))
        y0, y1 = segs[int(r["segment"]) - 1]; x = float(r["x_px"])
        g = a[y0:y1, max(0, int(x - 30)):int(x + 30)]; pr = np.convolve((g < THR).sum(axis=1), np.ones(27) / 27, "same")
        pk = [i for i in range(1, len(pr) - 1) if pr[i] >= pr[i - 1] and pr[i] >= pr[i + 1] and pr[i] >= 0.5 * pr.max()]
        cy = y0 + max(pk)
        paper = tuple(int(v) for v in np.median(np.asarray(im.crop((0, y0, im.width, y1))).reshape(-1, 3), axis=0))
        seg = Image.new("RGB", (im.width + 400, im.height + 400), paper); seg.paste(im.crop((0, y0, im.width, y1)), (200, y0 + 200))
        t = seg.crop((int(x - 165) + 200, int(cy - 120) + 200, int(x + 165) + 200, int(cy + 165) + 200))
        out.append(("control", r["sheet"], r["order_in_sheet"], r["group"], r["segment"], r["x_px"], t))
    return out
def write_sheets(tiles, tag, keyname):
    os.makedirs(f"{IMG}/{tag}", exist_ok=True); W, H = 330, 285 + 34
    for s in range(0, len(tiles), 10):
        sheet = Image.new("RGB", (5 * (W + 10), 2 * (H + 10)), "white"); d = ImageDraw.Draw(sheet)
        for k, tt in enumerate(tiles[s:s + 10]):
            t = ImageOps.autocontrast(tt[6].convert("L"), cutoff=1).convert("RGB"); dd = ImageDraw.Draw(t)
            dd.line([(165, 0), (165, 14)], fill=(220, 0, 0), width=3); dd.line([(165, t.height - 14), (165, t.height)], fill=(220, 0, 0), width=3)
            X, Y = (k % 5) * (W + 10), (k // 5) * (H + 10); sheet.paste(t, (X, Y + 34)); d.text((X + 6, Y + 6), f"tile {s + k + 1}", fill=(0, 0, 200))
            d.rectangle([X, Y + 34, X + W - 1, Y + 34 + t.height - 1], outline=(0, 0, 0))
        sheet.save(f"{IMG}/{tag}/loop_sheet{s // 10 + 1}.jpg", quality=88)
    with open(f"{HERE}/{keyname}", "w") as f:
        f.write("tile\tkind\tline_or_sheet\tposition_or_order\tcode_or_h26group\tsegment\tx_px\n")
        for n, tt in enumerate(tiles, 1): f.write("\t".join(map(str, (n,) + tt[:6])) + "\n")
    print(f"{len(tiles)} tiles ({sum(t[0] == 'target' for t in tiles)} target, {sum(t[0] == 'control' for t in tiles)} control) on {(len(tiles) + 9) // 10} sheets images/{tag}/")
def score_h113(path):
    key = {r["tile"]: r for r in rows(f"{HERE}/f61loop108r_h113_tiles.tsv")}
    rd = {r["tile"].strip().replace("tile ", ""): r for r in rows(path)}
    ok = n = 0; lines, rel = [], []
    for t, k in key.items():
        if k["kind"] != "control": continue
        a = rd.get(t, {}).get("arrangement", "none").strip(); exp_side = k["code_or_h26group"] in ("G2", "period_o"); n += 1
        hit = side(a) if exp_side else (bool(a) and not side(a) and a.lower().startswith(("single", "two stacked", "trefoil")))
        ok += hit; lines.append(f"control tile {t} {k['line_or_sheet']}/{k['position_or_order']} {k['code_or_h26group']} -> '{a}' {'ok' if hit else 'MISS'}")
    gate = ok >= 0.9 * n
    for t, k in sorted(key.items(), key=lambda kv: (kv[1]["line_or_sheet"], int(kv[1]["position_or_order"]) if kv[1]["kind"] == "target" else 0)):
        if k["kind"] != "target": continue
        a = rd.get(t, {}).get("arrangement", "none").strip(); al = a.lower()
        new = "SBS" if side(a) else ("PHI" if al.startswith(("single", "two stacked", "trefoil")) else k["code_or_h26group"])
        rel.append((k["line_or_sheet"], k["position_or_order"], k["code_or_h26group"], a, new if gate else k["code_or_h26group"]))
    from collections import Counter
    txt = [f"H113 loop classification: controls {ok}/{n} on the expected side; GATE (>= 90%): {'PASS' if gate else 'FAIL'}"] + lines
    txt += [f"target {L}/{p}: draft {c} -> '{a}' -> {nw}" for L, p, c, a, nw in rel]
    txt += ["relabel summary: " + " ".join(f"{a}->{b}:{m}" for (a, b), m in sorted(Counter((c, nw) for _, _, c, _, nw in rel).items()))]
    txt = "\n".join(txt) + "\n"; tsv = "line\tposition\tdraft\tarrangement\tcode\n" + "".join("\t".join(map(str, r)) + "\n" for r in rel)
    rp, tp = f"{HERE}/f61loop108r_h113_result.txt", f"{HERE}/f61loop108r_h113_relabel.tsv"
    if "--check" in sys.argv:
        good = os.path.exists(rp) and open(rp).read() == txt and open(tp).read() == tsv; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); open(tp, "w").write(tsv); print(txt, end="")
if __name__ == "__main__":
    {"build": lambda: build(), "score": lambda: score(sys.argv[2]), "build-h113": lambda: build_h113(), "score-h113": lambda: score_h113(sys.argv[2])}[sys.argv[1]]()
