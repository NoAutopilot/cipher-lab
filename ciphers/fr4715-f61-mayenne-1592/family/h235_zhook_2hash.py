#!/usr/bin/env python3
"""H235 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026): is f.61's ZHOOK (3 signs; v5 i/x graded S, "no glyph link across hands", H178b)
the "2#" sign that reads i/x in two period decipherments (f.101r's H24, i 170; f.188r's 2-hook HASH4, i/x 8/8, H224)? H178b compared it with
Desportes's small cursive i-sign on f.176r and failed on size/hand; H222 sorted f.101r's H24 as a "2#" group at matched scale. Written before the call.
 tiles SCRATCH NATIVE101 NATIVE188: f.61 ZHOOK 3 and C43 3 (H178b's eye-placed positions on images/f61sheet_L*.jpg, x +-150 sheet px);
   f.101r H24 i 5 (h220 pool, positions not used in H220/H222, seed 235) and HASH4 4-head d/q 4 (H227 answers A with letter d/q, seed 235);
   f.188r 2-hook i/x 4 (H224 answers D, seed 235); f.101r/f.188r cut from the natives x +-60 by the band box. Every tile grey, autocontrast,
   scaled to height 180 (H178b's normalisation), a red triangle above and below the centre, numbered V01..V19, shuffled (seed 235), one sheet
   <scratch>/h235/sheet_01.jpg. Key h235_items.tsv committed before the call; the runner does not look at the sheet.
 One blind Opus call: free sort of the centre signs into 2-4 groups by shape, one-sentence criterion each, 'unclear' allowed; inline, no tools.
 score: G = the group holding most of the 9 "2#" tiles (H24 + 2-hook). Pre-stated: "f.61's ZHOOK is the 2# sign" iff G holds >= 7 of the 9 AND all
   3 f.61 ZHOOK AND at most 1 of the 7 others (f.61 C43, f.101r 4-head); else "no link shown". Reported: hypergeometric p of 3/3 ZHOOK in G.
   A PASS is a glyph link for a verifier (ZHOOK -> the period's i/x sign), no merge.  python3 h235_zhook_2hash.py tiles ... | score [--check]"""
import csv, json, os, random, sys
from math import comb
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
F61 = [("ZHOOK", "L07", 2, 1430), ("ZHOOK", "L07", 3, 2080), ("ZHOOK", "L11", 2, 1500), ("C43", "L05", 1, 2310), ("C43", "L05", 2, 500), ("C43", "L11", 1, 1565)]
NSEG = {"L05": 3, "L07": 3, "L11": 2}
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def tiles(scratch, n101, n188):
    from PIL import Image, ImageDraw, ImageOps
    import h220_hash_101r as h220, h224_hash_188r as h224
    rng = random.Random(235); its = []
    for cls, line, seg, x in F61:
        im = Image.open(f"{HERE}/../images/f61sheet_{line}.jpg").convert("L"); h = im.size[1] / NSEG[line]
        its.append((("f61", line, f"s{seg}", x, cls, "-"), im.crop((x - 150, int((seg - 1) * h) + 10, x + 150, int(seg * h) - 6))))
    used = {(r["line"], r["idx"]) for f in ("h220_items.tsv", "h222_items.tsv") for r in rd(f"{HERE}/{f}") if r["kind"] == "T"}
    B1 = json.load(open(f"{HERE}/sheets/f101r_bands.json"))["boxes"]; B8 = json.load(open(f"{HERE}/sheets/f188r_bands.json"))["boxes"]
    N1 = Image.open(n101).convert("L"); N8 = Image.open(n188).convert("L")
    def cut(N, B, pre, t): b = B[f"{pre}_{t['line']}_{t['seg']}.jpg"]; x = b[0] + t["x"] // 2; return N.crop((x - 60, b[1], x + 60, b[3]))
    for t in rng.sample([t for t in h220.pool()[("H24", "I")] if (t["line"], t["idx"]) not in used], 5): its.append((("f101r", t["line"], t["seg"], t["x"], "H24", t["letter"]), cut(N1, B1, "f101r", t)))
    a227 = {r["id"]: r["answer"].strip() for r in rd(f"{P}/h227_reply.tsv")}; p101 = {(t["line"], t["idx"]): t for t in h220.pool()[("HASH4", "DQ")]}
    A = [r for r in rd(f"{HERE}/h227_items.tsv") if r["kind"] == "T" and a227.get(r["item"]) == "A" and r["letter"] in "dq" and (r["line"], r["idx"]) in p101]
    for r in rng.sample(A, 4): t = p101[(r["line"], r["idx"])]; its.append((("f101r", t["line"], t["seg"], t["x"], "HASH4-A", t["letter"]), cut(N1, B1, "f101r", t)))
    a224 = {r["id"]: r["answer"].strip() for r in rd(f"{P}/h224_reply.tsv")}; p188 = {(t["line"], t["idx"]): t for k in ("IX", "DQ") for t in h224.pool()[k]}
    D = [r for r in rd(f"{HERE}/h224_items.tsv") if r["kind"] == "T" and a224.get(r["item"]) == "D" and r["letter"] in "ix"]
    for r in rng.sample(D, 4): t = p188[(r["line"], r["idx"])]; its.append((("f188r", t["line"], t["seg"], t["x"], "2HOOK", t["letter"]), cut(N8, B8, "f188r", t)))
    rng.shuffle(its); os.makedirs(f"{scratch}/h235", exist_ok=True); W, cw, ch = 5, 300, 240
    sh = Image.new("L", (W * cw, ((len(its) + W - 1) // W) * ch), 255); d = ImageDraw.Draw(sh); key = ["item\tleaf\tline\tsegment\tx\tclass\tletter"]
    for n, (k, im) in enumerate(its, 1):
        im = ImageOps.autocontrast(im.resize((int(im.size[0] * 180 / im.size[1]), 180)), cutoff=2); im.thumbnail((cw - 10, 180))
        X, Y = ((n - 1) % W) * cw, ((n - 1) // W) * ch; sh.paste(im, (X + 5, Y + 28)); mx = X + 5 + im.size[0] // 2
        d.polygon([(mx - 8, Y + 8), (mx + 8, Y + 8), (mx, Y + 24)], fill=0); d.polygon([(mx - 8, Y + 228), (mx + 8, Y + 228), (mx, Y + 212)], fill=0)
        d.text((X + 8, Y + 4), f"V{n:02d}", fill=0); key.append(f"V{n:02d}\t" + "\t".join(map(str, k)))
    sh = sh.convert("RGB"); d = ImageDraw.Draw(sh)
    sh.save(f"{scratch}/h235/sheet_01.jpg", quality=90); open(f"{HERE}/h235_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "tiles")
def score():
    its = {r["item"]: r for r in rd(f"{HERE}/h235_items.tsv")}; g = {r["tile"].strip(): r["group"].strip() for r in rd(f"{P}/h235_sort.tsv")}
    two = [m for m, r in its.items() if r["class"] in ("H24", "2HOOK")]; zh = [m for m, r in its.items() if r["class"] == "ZHOOK"]
    oth = [m for m, r in its.items() if r["class"] in ("C43", "HASH4-A")]; groups = [x for x in dict.fromkeys(g.values()) if x.lower() != "unclear"]
    G = max(groups, key=lambda x: (sum(g.get(m) == x for m in two), -groups.index(x)))
    a, z, o = sum(g.get(m) == G for m in two), sum(g.get(m) == G for m in zh), sum(g.get(m) == G for m in oth); size = sum(v == G for v in g.values())
    p = comb(size, 3) / comb(len(its), 3) if size >= 3 else 0.0
    out = ["by class: " + "; ".join(f"{c}: " + " ".join(f"{x} {n}" for x, n in sorted(Counter(g.get(m, '-') for m, r in its.items() if r['class'] == c).items())) for c in ("ZHOOK", "H24", "2HOOK", "C43", "HASH4-A")),
           f"G = {G}: 2# tiles {a}/9, f.61 ZHOOK {z}/3, others {o}/7; hypergeometric p (3 ZHOOK in a group of {size} of {len(its)}) {p:.3f}"]
    ok = a >= 7 and z == 3 and o <= 1
    out.append("read-out: " + ("f.61's ZHOOK is the 2# sign" if ok else "no link shown"))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h235_zhook_2hash_result.txt"
    if "--check" in sys.argv:
        ok2 = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok2 else "STALE"); sys.exit(0 if ok2 else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(*sys.argv[2:5]) if sys.argv[1] == "tiles" else score()
