#!/usr/bin/env python3
"""F61-HASH4-FORMS (campaign step H162, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe). Does f.61's hand write two
hash forms that the passes lump as HASH4 -- the bare hash (period i on the family leaves, class H24) and the 4-over-hash
(period d/q)? One blind Opus vision call on tiles (the H98 design): every pass-A HASH4 of f.108v (family/passes/
f108v3z_signsA.tsv, crops family/sheets/f108v3y|3z_*) and every HASH4 of the H108 f.108r L04-L06 draft (stitched native
region), mixed with H98's own 20 period-labelled tiles (images/h98, set A = period i, set B = period d/q) as controls, cut back
out of their sheets. Shuffled (seed 162), ten per sheet in images/h162/; key scripts/f61hash4_forms_tiles.tsv never named.
Pre-registered: control gate >= 17/20 (H98's own level, 17/19) with 'four present' = set B and 'absent' = set A; on a PASS each
target is labelled 4-over-hash (four present) or bare hash (absent); 'none' keeps HASH4.
  python3 scripts/f61hash4_forms.py build ; python3 scripts/f61hash4_forms.py score scripts/read_call_H162.tsv [--check]"""
import csv, json, os, random, sys
import numpy as np
from PIL import Image, ImageDraw, ImageOps
HERE = os.path.dirname(os.path.abspath(__file__)); TGT = os.path.dirname(HERE); IMG = f"{TGT}/images"; FAM = f"{TGT}/family"
sys.path.insert(0, HERE)
def rows(p): return list(csv.DictReader((l for l in open(p) if not l.startswith("#")), delimiter="\t"))
def tile_from_crop(im, x, THR=140):
    a = np.asarray(im.convert("L"), float); g = a[:, max(0, int(x - 30)):int(x + 30)]
    pr = np.convolve((g < THR).sum(axis=1), np.ones(27) / 27, "same"); pk = [i for i in range(1, len(pr) - 1) if pr[i] >= pr[i - 1] and pr[i] >= pr[i + 1] and pr[i] >= 0.5 * pr.max()]
    cy = max(pk) if pk else a.shape[0] // 2
    paper = tuple(int(v) for v in np.median(np.asarray(im.convert("RGB")).reshape(-1, 3), axis=0))
    big = Image.new("RGB", (im.width + 400, im.height + 400), paper); big.paste(im.convert("RGB"), (200, 200))
    return big.crop((int(x - 165) + 200, int(cy - 120) + 200, int(x + 165) + 200, int(cy + 165) + 200))
def targets():
    out = []
    for r in rows(f"{FAM}/passes/f108v3z_signsA.tsv"):
        if r["sign"] != "HASH4": continue
        v = "3z" if r["line"] in ("L01", "L02") and r["segment"] == "s1" else "3y"
        im = Image.open(f"{FAM}/sheets/f108v{v}_{r['line']}_{r['segment']}.jpg"); out.append(("target", "f108v", r["line"], r["pos"], r["segment"], r["x_px"], tile_from_crop(im, float(r["x_px"]))))
    import f61loop108r as LR
    st = Image.open(f"{IMG}/stitch_f108r_f195_1250_450_3600_860.jpg").convert("RGB")
    bj = {"L04": json.load(open(f"{IMG}/f108g/f108g_bands.json")), "L05": json.load(open(f"{IMG}/f108g/f108g_bands.json")), "L06": json.load(open(f"{IMG}/f108h/f108h_bands.json"))}
    for r in rows(f"{HERE}/f61recon108r_draft.tsv"):
        if r["sign"] != "HASH4": continue
        L = r["line"]; j = bj[L]; pre = "f108g" if L != "L06" else "f108h"; box = j["boxes"][f"{pre}_{L}_{r['segment']}.jpg"]
        cx = box[0] + float(r["x_px"]) / j["scale"]; cy = box[1] + j["up"]
        g = np.asarray(st.crop((int(cx - 30), int(cy - 15), int(cx + 30), int(cy + 45))).convert("L")); pr = np.convolve((g < 140).sum(axis=1), np.ones(9) / 9, "same"); cy = cy - 15 + int(pr.argmax())
        out.append(("target", "f108r", L, r["position"], r["segment"], r["x_px"], st.crop((int(cx - 55), int(cy - 40), int(cx + 55), int(cy + 55))).resize((330, 285), Image.LANCZOS)))
    return out
def controls():
    out = []
    for r in rows(f"{HERE}/f61pair_h98_tiles.tsv"):
        k = int(r["tile"]) - 1; sh = Image.open(f"{IMG}/h98/pair_sheet{k // 10 + 1}.jpg").convert("RGB"); j = k % 10
        X, Y = (j % 5) * 340, (j // 5) * 329 + 34; a = np.asarray(sh.crop((X, Y, X + 330, Y + 285))).copy()
        red = (a[:, :, 0] > 150) & (a[:, :, 1] < 90) & (a[:, :, 2] < 90); a[red] = 255
        out.append(("control", r["leaf"], r["line"], r["draft_pos"], r["period_letter"], r["set"], Image.fromarray(a)))
    return out
def build():
    tiles = targets() + controls(); random.Random(162).shuffle(tiles)
    import f61loop108r as LR
    LR.write_sheets(tiles, "h162", "f61hash4_forms_tiles.tsv")
def score(path):
    key = {r["tile"]: r for r in rows(f"{HERE}/f61hash4_forms_tiles.tsv")}
    rd = {r["tile"].strip().replace("tile ", ""): r for r in rows(path)}
    ok = n = 0; lines = []; tg = []
    for t, k in key.items():
        f = rd.get(t, {}).get("four", "").strip().lower(); four = f.startswith("y") or f.startswith("present")
        if k["kind"] == "control":
            n += 1; exp = k["x_px"] == "B"; hit = (four == exp) and f not in ("", "none"); ok += hit
            lines.append(f"control tile {t} period {k['segment']} set {k['x_px']} -> four '{f}' {'ok' if hit else 'MISS'}")
        else: tg.append((k["line_or_sheet"], k["position_or_order"], k["code_or_h26group"], f))
    gate = ok >= 17
    out = [f"H162 controls {ok}/{n}; GATE (>= 17/20): {'PASS' if gate else 'FAIL'}"] + lines
    out += [f"target {a}/{b}/{c}: four '{f}' -> " + (("HASH4 (4-over-hash)" if (f.startswith("y") or f.startswith("present")) else ("H24 (bare hash)" if f.startswith(("n", "absent")) else "HASH4 kept")) if gate else "not relabelled") for a, b, c, f in tg]
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61hash4_forms_result.txt"
    if "--check" in sys.argv:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    build() if sys.argv[1] == "build" else score(sys.argv[2])
