#!/usr/bin/env python3
"""H254 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026): are f.108r's ZHOOK signs (f.61's hand; Tomokiyo's overlay reprint of the leaf's period gloss
reads ZHOOK i 7/7, KEY v5) the 2# sign, as H235 found for f.61's ZHOOK? Written before the call. Targets: every pass-A ZHOOK on f.108r L02/L03
(scripts/pass108A_classes.tsv, images/f108sheetB_<row>.jpg at its segment/x, x +-150), overlay letter where f61crib.align under v5 (EBR A) places one
(caveat: v5 has ZHOOK i/x, so pairs can follow the code). Anchors, categories, normalisation and gate as H239 (12 anchors, >= 10). Pre-stated: 'f.108r's
ZHOOK is the 2# sign' iff >= 0.8 of targets answer D. Descriptive, for the ZHOOK grade question VERIFY-F61-V7 left open. Base script follows:
H239 = H236 with a sturdier control (anchors 12: 4-head hash 6 from H227 answers A at d/q, 2-hook 6 from H224 answers D at i/x;
 gate >= 10/12; seed 239; key h254_items.tsv; reply passes/h254_reply.tsv). If this control fails too, the f.108r 4PI shape is logged untestable in this
 format and not retried. The rest as H236 below.
H236 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026): is f.108r's 4PI (f.61's hand; Tomokiyo's reprint of the leaf's period gloss reads it
d 4, p 1 at H202's aligned pairs, grade C) the '4 over a Pi' sign of f.61's two 4PI (H233: E) or the 4-head hash (f.101r's 4PI, H233: A)? Written before
the call.
 tiles SCRATCH NATIVE101 NATIVE188: f.108r's five 4PI pairs (h202_bowl_108r.pairs(), images/f108sheetB_<row>.jpg at pass A's segment/x, x +-150);
   f.61's two 4PI (H233's positions); anchors re-cut as h233 (H235's 4-head tiles 4, 2-hook tiles 4). H235/H233 normalisation, shuffled (seed 236),
   U01.., one sheet <scratch>/h239/. Key h254_items.tsv before the call; the runner does not look at the sheet.
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
    import build_key_v5 as bk
    from f61crib import align
    k5 = bk.load_key_v5(ebr="A"); A = {}
    for r in rd(f"{h202.S}/pass108A_classes.tsv"): A.setdefault(r["line"], []).append(r)
    let = {}
    for s_, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{h202.S}/tomokiyo_spans_3983.tsv") if l[0] == "T"):
        row = "L02" if s_ == "T1" else "L03"; seq = [r["sign"] for r in A[row]]; mm = m.translate(bk.FOLD)
        for i, j in align(mm, seq, k5)[1]: let[(row, A[row][j]["pos"])] = mm[i]
    for row, rs in sorted(A.items()):
        for r in rs:
            if r["sign"] != "ZHOOK": continue
            im = Image.open(f"{HERE}/../images/f108sheetB_{row}.jpg").convert("L"); st = (im.height + 12) // 4; y0 = (int(r["segment"]) - 1) * st; x = int(r["x_px"])
            its.append((("f108r", row, r["segment"], x, "ZHOOK", let.get((row, r["pos"]), "-"), "T"), im.crop((x - 150, y0, x + 150, y0 + st - 12))))
    N1 = Image.open(n101).convert("L"); N8 = Image.open(n188).convert("L")
    B1 = json.load(open(f"{HERE}/sheets/f101r_bands.json"))["boxes"]; B8 = json.load(open(f"{HERE}/sheets/f188r_bands.json"))["boxes"]
    import h220_hash_101r as h220, h224_hash_188r as h224
    rng = random.Random(254); p101 = {(t["line"], t["idx"]): t for t in h220.pool()[("HASH4", "DQ")]}
    a227 = {r["id"]: r["answer"].strip() for r in rd(f"{P}/h227_reply.tsv")}
    A = [p101[(r["line"], r["idx"])] for r in rd(f"{HERE}/h227_items.tsv") if r["kind"] == "T" and a227.get(r["item"]) == "A" and r["letter"] in "dq" and (r["line"], r["idx"]) in p101]
    p188 = {(t["line"], t["idx"]): t for k in ("IX", "DQ") for t in h224.pool()[k]}; a224 = {r["id"]: r["answer"].strip() for r in rd(f"{P}/h224_reply.tsv")}
    D = [p188[(r["line"], r["idx"])] for r in rd(f"{HERE}/h224_items.tsv") if r["kind"] == "T" and a224.get(r["item"]) == "D" and r["letter"] in "ix"]
    for cls, pool, N, B, pre in (("ANCHOR-A", A, N1, B1, "f101r"), ("ANCHOR-D", D, N8, B8, "f188r")):
        for t in rng.sample(pool, 6):
            b = B[f"{pre}_{t['line']}_{t['seg']}.jpg"]; x = b[0] + t["x"] // 2
            its.append(((pre, t["line"], t["seg"], t["x"], cls, t["letter"], "C"), N.crop((x - 60, b[1], x + 60, b[3]))))
    random.Random(254).shuffle(its); os.makedirs(f"{scratch}/h254", exist_ok=True); W, cw, ch = 5, 300, 240
    sh = Image.new("L", (W * cw, ((len(its) + W - 1) // W) * ch), 255); d = ImageDraw.Draw(sh); key = ["item\tleaf\tline\tsegment\tx\tclass\tletter\tkind"]
    for j, (k, im) in enumerate(its):
        im = ImageOps.autocontrast(im.resize((int(im.size[0] * 180 / im.size[1]), 180)), cutoff=2); im.thumbnail((cw - 10, 180))
        X, Y = (j % W) * cw, (j // W) * ch; sh.paste(im, (X + 5, Y + 28)); mx = X + 5 + im.size[0] // 2
        d.polygon([(mx - 8, Y + 8), (mx + 8, Y + 8), (mx, Y + 24)], fill=0); d.polygon([(mx - 8, Y + 228), (mx + 8, Y + 228), (mx, Y + 212)], fill=0)
        d.text((X + 8, Y + 4), f"U{j + 1:02d}", fill=0); key.append(f"U{j + 1:02d}\t" + "\t".join(map(str, k)))
    sh.convert("RGB").save(f"{scratch}/h254/sheet_01.jpg", quality=90); open(f"{HERE}/h254_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "tiles")
def score():
    its = rd(f"{HERE}/h254_items.tsv"); ans = {r["id"]: r["answer"].strip().upper() for r in rd(f"{P}/h254_reply.tsv")}
    C = [r for r in its if r["kind"] == "C"]; hit = sum(ans.get(r["item"]) == ("A" if r["class"] == "ANCHOR-A" else "D") for r in C)
    out = [f"anchors: {hit} of {len(C)} (gate >= 10): {'PASS' if hit >= 10 else 'CONTROL FAIL'}"]
    if hit >= 10:
        T = [r for r in its if r["kind"] == "T"]
        out.append("f.108r ZHOOK: " + "; ".join(f"{r['line']} x{r['x']} overlay {r['letter']} -> {ans.get(r['item'], 'N')}" for r in T))
        dd = sum(ans.get(r["item"]) == "D" for r in T)
        out.append(f"read-out: D {dd} of {len(T)} -> " + ("f.108r's ZHOOK is the 2# sign" if dd >= 0.8 * len(T) else "no 2# link shown"))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h254_zhook_108r_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(*sys.argv[2:5]) if sys.argv[1] == "tiles" else score()
