#!/usr/bin/env python3
"""H399 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026), written before the call: f.97r rows L01-L16 (first cut, sheets/f97r, pass A
passes/f97r_signsA_c1/c2) were left out of H370-H377, so the f.97r shape draft is split on L17-L43 only.
 targets -- every draft 4TRI of L01-L16 with why 'agree*' (passes/recf97r): 65. Draft position -> pass-A row by a per-line difflib alignment of the
   draft signs with pass A's signs (only 'equal' blocks; the draft renumbers positions, so 100 of 149 pass-A 4TRI sit at a different position number
   than the draft's), x = box x0 + x_px/2, centre = box y0 + 70 (sheets/f97r/f97r_bands.json, scale 2), H359 geometry (300 native px, -60/+55, x1.2,
   red marker above), from the native f.97r (Gallica btv1b9060543f f202).
 known part-2 strips -- H377's 6 f.61 tiles (h377_items.tsv K rows, H367 window), gate 2.
 placement check before the call: one sheet of the first 20 targets is looked at by the runner for marker placement only (disclosed in NOTES).
 shuffled (seed 399), R01.., 20 per sheet. One blind Opus call, H359's prompt verbatim (part 1 H193's 60 strips).
 score -- GATE 1 >= 17/20, GATE 2 >= 5/6, else CONTROL FAIL. If both pass: (a) L01-L16 no-bowl share; (b) H397's second instrument (V10's order
   statistic, h397_shape_v10instrument.one, the f.97r arm, seed 397+2) on the completed f.97r draft: H397's f.97r answers + these, relabel design vs 20
   random relabellings of the same count from the same pool; pre-stated as H397: >= 19/20 'carries order information (second instrument)', <= 9/20
   'no better than random', else 'unclear'. Descriptive; no key change.   python3 h399_97r_firstcut.py tiles SCRATCH F61REGION | score [--check]"""
import csv, difflib, json, os, random, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE); CHECK = "--check" in sys.argv   # captured here: h397.leaves() rewrites sys.argv
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def targets():
    A = defaultdict(list)
    for c in (1, 2):
        for r in rd(f"{P}/f97r_signsA_c{c}.tsv"): A[r["line"]].append(r)
    D = defaultdict(list)
    for r in rd(f"{P}/recf97r/ciphertext_draft.tsv"): D[r["line"]].append(r)
    PB = defaultdict(list)
    for c in (1, 2):
        for r in rd(f"{P}/f97r_signsB_c{c}.tsv"): PB[r["line"]].append(r)
    bx_of = {}   # CHANGED after the placement look (NOTES H399): x = mean of pass A and pass B x where B's sign aligns (same segment), else A's
    for l in A:
        a, b = A[l], PB[l]
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, [x["sign"] for x in a], [x["sign"] for x in b], autojunk=False).get_opcodes():
            if tag == "equal":
                for k in range(i2 - i1):
                    if a[i1 + k]["segment"] == b[j1 + k]["segment"]: bx_of[id(a[i1 + k])] = float(b[j1 + k]["x_px"])
    B = json.load(open(f"{HERE}/sheets/f97r/f97r_bands.json"))["boxes"]; out = []
    for l in sorted(A):
        a, d = A[l], D[l]
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, [x["sign"] for x in d], [x["sign"] for x in a], autojunk=False).get_opcodes():
            if tag != "equal": continue
            for k in range(i2 - i1):
                dr, ar = d[i1 + k], a[j1 + k]
                if dr["sign"] == "4TRI" and dr["why"].startswith("agree"):
                    bx = B[f"f97r_{l}_{ar['segment']}.jpg"]; out.append(("T", "4TRI", l, dr["position"], bx[0] + int((float(ar["x_px"]) + bx_of.get(id(ar), float(ar["x_px"]))) / 2) // 2, bx[1] + 70, ""))
    return out
def known():
    return [("K", r["code"], r["line"], r["pos"], int(r["x_native"]), int(r["y_centre"]), r["kind"][1:]) for r in rd(f"{HERE}/h377_items.tsv") if r["kind"].startswith("K")]
def tiles(scratch, f61):
    from PIL import Image, ImageDraw
    its = targets() + known(); random.Random(399).shuffle(its)
    nat = {"T": Image.open(f"{scratch}/nat/f97r.jpg").convert("RGB"), "K": Image.open(f61).convert("RGB")}
    os.makedirs(f"{scratch}/h399", exist_ok=True); key = ["item\tkind\tcode\tline\tpos\tx_native\ty_centre\tref"]; ims = []
    for n, (kind, code, line, pos, x, yc, ref) in enumerate(its, 1):
        up, dn = (45, 92) if kind == "K" else (60, 55)
        t = nat[kind].crop((x - 150, yc - up, x + 150, yc + dn)); t = t.resize((360, int(t.height * 1.2)))
        c = Image.new("RGB", (370, 190), "white"); c.paste(t.crop((0, 0, 360, min(t.height, 165))), (5, 22)); d = ImageDraw.Draw(c); mx = 5 + int(150 * 1.2)
        d.polygon([(mx - 9, 2), (mx + 9, 2), (mx, 18)], fill=(220, 0, 0)); d.text((330, 4), f"R{n:02d}", fill=(0, 0, 0))
        ims.append(c); key.append(f"R{n:02d}\t{kind}\t{code}\t{line}\t{pos}\t{x}\t{yc}\t{ref}")
    for s in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 190), "white")
        for k, c in enumerate(ims[s:s + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 190))
        sh.save(f"{scratch}/h399/sheet_{s // 20 + 1:02d}.jpg", quality=88)
    # placement sheet: first 20 targets in pass order, marker only (the runner's look)
    open(f"{HERE}/h399_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items:", sum(i[0] == "T" for i in its), "targets + 6 known")
def score():
    ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h399_reply.tsv")}; it = rd(f"{HERE}/h399_items.tsv")
    g1 = sum((ans.get(r["item"]) == "yes") == (r["group"] == "CP") and ans.get(r["item"]) in ("yes", "no") for r in rd(f"{HERE}/h193_items.tsv") if r["group"] in ("CP", "AN"))
    g2 = sum(ans.get(r["item"]) == r["ref"] for r in it if r["kind"] == "K")
    out = [f"gate 1 (H193 anchors): {g1}/20 (>= 17); gate 2 (known f.61 strips): {g2}/6 (>= 5)"]
    tg = [r for r in it if r["kind"] == "T"]
    if g1 < 17 or g2 < 5: out.append("CONTROL FAIL -- nothing scored")
    elif len({ans.get(r["item"]) for r in tg} - {"n", None}) < 2: out.append("one-value chunk: re-read before use")
    else:
        y = sum(ans.get(r["item"]) == "yes" for r in tg); n = sum(ans.get(r["item"]) == "no" for r in tg)
        out.append(f"L01-L16 targets {len(tg)}: bowl {y}, no bowl {n}, n {len(tg) - y - n}; no-share {n / max(1, y + n):.2f}")
        import h397_shape_v10instrument as h
        L = h.leaves(); name, src, mode, lab = [x for x in L if x[0] == "f.97r"][0]; lab = dict(lab)
        for r in tg: lab[(r["line"], r["pos"])] = ans.get(r["item"])
        out.append("H397 f.97r arm as run: " + [l for l in open(f"{HERE}/h397_shape_v10instrument_result.txt") if l.startswith("f.97r")][0].strip())
        out.append("completed f.97r (L01-L43): " + h.one((2, ("f.97r", src, mode, lab))))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h399_97r_firstcut_result.txt"
    if CHECK:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]
    tiles(a[1], a[2]) if a[0] == "tiles" else score()
