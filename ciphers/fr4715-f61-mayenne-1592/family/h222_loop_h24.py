#!/usr/bin/env python3
"""H222 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026): is f.108's looped hash (H212 form B) the same sign as fr.3982 f.101r's H24 (period i,
the "2 joined to a crossed 4") in another hand? H220's reader put 11 of 12 H24 strips in neither hash form, but its f.101r strips and f.108 tiles differed
in scale. Written before the call.
 tiles NATIVE SCRATCH: matched scale, one sign per tile. f.101r (Gallica native btv1b9060543f f210): window x +-60 by the full band box the readers saw
   (140 native px; a first +-45 window cut the sign off where rows drift), scaled 3x. f.108 (H212's crops, 3x): window x +-180 over the full crop
   height, unscaled, marker at the sign's own x when the window is clamped at a crop edge (checked on one tile of each kind before the call: the hash
   signs come out at about the same width, ~100 px). Items (seed 222): H212 group A 5 and group B 5 (tile 9 excluded;
   H212's group labels, from passes/h212_sort.tsv), f.101r H24 i 6 and HASH4 d/q 6 drawn from h220_hash_101r.py's pool excluding the H220 strips'
   positions. Red triangles above and below the target, numbered W01..W22, shuffled, leaf hidden, 20 + 2 on two sheets <scratch>/h222/.
 One blind Opus vision call, the H212 design: free sort of the pointed-at signs into 2-4 shape groups by shape alone, one-sentence criterion per group.
 score: G = the group holding most of the six H24 tiles (ties -> the group listed first in the reply). stat = (B tiles in G) + (A tiles not in G), 0-10.
   Exact null: all C(10,5) = 252 assignments of the A/B labels to the ten f.108 tiles. Pre-stated read-out: "f.108's looped hash sorts with f.101r's
   H24" iff G holds >= 4 of the 6 H24 tiles AND the exact p (share of assignments with stat >= observed) < 0.05; else "no link shown". Reported, not
   gated: where the six HASH4 d/q tiles fall. Descriptive; a PASS would give form B a period letter (i/x) by glyph identity, for a verifier, no merge.
  python3 h222_loop_h24.py tiles NATIVE SCRATCH | score [--check]"""
import csv, json, os, random, sys
from collections import Counter
from itertools import combinations
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def tiles(native, scratch):
    from PIL import Image, ImageDraw
    import h220_hash_101r as h220, h212_hash_sort as h212
    rng = random.Random(222); pl = h220.pool()
    used = {(r["line"], r["idx"]) for r in rd(f"{HERE}/h220_items.tsv") if r["kind"] == "T"}
    its = []
    for k, n in ((("H24", "I"), 6), (("HASH4", "DQ"), 6)):
        its += [dict(t, kind="T") for t in rng.sample([t for t in pl[k] if (t["line"], t["idx"]) not in used], n)]
    k212 = {r["item"]: r for r in rd(f"{HERE}/h212_items.tsv")}
    grp = {f"T{int(r['tile'].split()[-1]):02d}": r["group"].strip() for r in rd(f"{P}/h212_sort.tsv")}
    geo = {(t["leaf"], t["line"], t["seg"], t["x"]): t for t in h212.items()}; anc = {"A": [], "B": []}
    for m, r in sorted(k212.items()):
        if m == "T09" or grp.get(m) not in anc: continue
        anc[grp[m]].append(dict(geo[(r["leaf"], r["line"], r["segment"], int(r["x_px"]))], kind="C", h212=m, group=grp[m]))
    for G in ("A", "B"): its += rng.sample(anc[G], 5)
    rng.shuffle(its); os.makedirs(f"{scratch}/h222", exist_ok=True); B = json.load(open(f"{HERE}/sheets/f101r_bands.json"))["boxes"]
    nat = Image.open(native).convert("RGB"); ims = []; key = ["item\tkind\tref\tline\tidx\tcode\tletter\tgroup"]
    for n, t in enumerate(its, 1):
        c = Image.new("RGB", (370, 470), "white"); d = ImageDraw.Draw(c)
        if t["kind"] == "T":
            b = B[f"f101r_{t['line']}_{t['seg']}.jpg"]; x = b[0] + t["x"] // 2; yc = b[1] + 80
            w = nat.crop((x - 60, b[1], x + 60, b[3])).resize((360, 3 * (b[3] - b[1])))
            mx = 5 + 180
            key.append(f"W{n:02d}\tT\tf101r\t{t['line']}\t{t['idx']}\t{t['code']}\t{t['letter']}\t{'H24' if t['code'] == 'H24' else 'DQ'}")
        else:
            im = Image.open(t["crop"]).convert("RGB"); x0 = max(0, min(im.width - 360, t["x"] - 180))
            w = im.crop((x0, 0, x0 + 360, im.height))
            mx = 5 + (t["x"] - x0)
            key.append(f"W{n:02d}\tC\t{t['h212']}\t{t['line']}\t-\tHASH4\t-\t{t['group']}")
        c.paste(w, (5, 20)); y = 20 + w.height
        d.polygon([(mx - 8, 2), (mx + 8, 2), (mx, 17)], fill=(220, 0, 0)); d.polygon([(mx - 8, y + 18), (mx + 8, y + 18), (mx, y + 3)], fill=(220, 0, 0))
        d.text((330, 4), f"W{n:02d}", fill=(0, 0, 0)); ims.append(c)
    for s0 in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 470), "white")
        for k, c in enumerate(ims[s0:s0 + 20]): sh.paste(c, ((k % 4) * 370, (k // 4) * 470))
        sh.save(f"{scratch}/h222/sheet_{s0 // 20 + 1:02d}.jpg", quality=88)
    open(f"{HERE}/h222_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "tiles", Counter(t["kind"] for t in its))
def score():
    its = {r["item"]: r for r in rd(f"{HERE}/h222_items.tsv")}; rep = rd(f"{P}/h222_sort.tsv")
    g = {r["tile"].strip(): r["group"].strip() for r in rep}; order = list(dict.fromkeys(r["group"].strip() for r in rep))
    h24 = [m for m, r in its.items() if r["group"] == "H24"]; cnt = Counter(g.get(m) for m in h24)
    G = max(order, key=lambda x: (cnt.get(x, 0), -order.index(x)))
    C = [m for m, r in its.items() if r["kind"] == "C"]; inG = {m: g.get(m) == G for m in C}
    def stat(bset): return sum(inG[m] for m in bset) + sum(not inG[m] for m in C if m not in bset)
    real = stat({m for m in C if its[m]["group"] == "B"}); null = [stat(set(s)) for s in combinations(C, 5)]
    p = sum(v >= real for v in null) / len(null)
    by = lambda lab: " ".join(f"{x}:{sum(1 for m, r in its.items() if r['group'] == lab and g.get(m) == x)}" for x in order)
    out = [f"groups (reply order): {', '.join(order)}; G (most H24) = {G} with {cnt.get(G, 0)} of 6 H24",
           f"H24 i: {by('H24')} | HASH4 d/q (f.101r): {by('DQ')} | H212 A (f.108): {by('A')} | H212 B (f.108): {by('B')}",
           f"stat (B in G + A not in G) = {real} of 10; exact p = {p:.3f} over {len(null)} label assignments"]
    ok = cnt.get(G, 0) >= 4 and p < 0.05
    out.append("read-out: " + ("f.108's looped hash sorts with f.101r's H24" if ok else "no link shown"))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h222_loop_h24_result.txt"
    if "--check" in sys.argv:
        ok2 = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok2 else "STALE"); sys.exit(0 if ok2 else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2], sys.argv[3]) if sys.argv[1] == "tiles" else score()
