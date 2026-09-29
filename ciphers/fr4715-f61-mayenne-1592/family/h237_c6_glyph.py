#!/usr/bin/env python3
"""H237 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026): is f.61's C6 (a '6'; 8 tokens, unread since VERIFY-F61-V4) the same glyph as the C6
signs at which the period decipherments of f.101r and f.188r read e (all 3 lettered positions, H232)? Written before the call; n is small and flagged.
 tiles SCRATCH NATIVE101 NATIVE188: f.61 C6 3 (by the runner's eye: images/f61sheet_L01.jpg s1 x 1175, f61sheet_L08.jpg s1 x 1080 and s2 x 1222; both
   sheets 2 segments), glossed C6 (every pass-A-mapped C6 with a letter on f.101r and f.188r; draft sign C6 and pass A C6), controls 6 from f.101r
   (PHI 3, C43 3, pass-A-mapped, seed 237). H235's normalisation, shuffled (seed 237), Y01.., one sheet <scratch>/h237/. Key h237_items.tsv before the
   call; the runner does not look at the sheet.
 One blind Opus free sort (H235's prompt). score: G = the group holding most glossed C6. Pre-stated: "f.61's C6 is the glossed C6 glyph" iff G holds
   >= 2 of the glossed C6 (all if fewer than 3 mapped), all 3 f.61 C6, and <= 1 of the 6 controls; else "no link shown". A PASS is a glyph link to
   period e on n = 3 lettered signs, for the verifier; no merge.  python3 h237_c6_glyph.py tiles SCRATCH N101 N188 | score [--check]"""
import csv, json, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
F61 = [("L01", 1, 1175), ("L08", 1, 1080), ("L08", 2, 1222)]
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def pool(leaf, code, need_letter=True):
    S = defaultdict(list)
    for r in rd(f"{P}/rec{leaf}/ciphertext_draft.tsv"):
        if r["sign"] != "DASH": S[r["line"]].append(r)
    A = {(r["line"], int(r["pos"])): r for r in rd(f"{P}/{leaf}_signsA.tsv")}; out = []
    al = f"{P}/{leaf}_align_v4.tsv"
    for r in rd(al):
        if r["kind"] != "code" or r["value"] != code or (need_letter and not r["plain_chunk"]): continue
        s = S[r["cipher_line"]][int(r["idx"])]
        if s["sign"] != code: continue
        a = A.get((r["cipher_line"], int(s["position"])))
        if a and a["sign"] == code: out.append(dict(leaf=leaf, line=r["cipher_line"], letter=r["plain_chunk"], seg=a["segment"], x=int(a["x_px"])))
    return out
def tiles(scratch, n101, n188):
    from PIL import Image, ImageDraw, ImageOps
    rng = random.Random(237); its = []
    for line, seg, x in F61:
        im = Image.open(f"{HERE}/../images/f61sheet_{line}.jpg").convert("L"); h = im.size[1] / 2
        its.append((("f61", line, seg, x, "C6-f61", "-"), im.crop((x - 150, int((seg - 1) * h) + 10, x + 150, int(seg * h) - 6))))
    N = {"f101r": Image.open(n101).convert("L"), "f188r": Image.open(n188).convert("L")}
    B = {lf: json.load(open(f"{HERE}/sheets/{lf}_bands.json"))["boxes"] for lf in N}
    def cut(t): b = B[t["leaf"]][f"{t['leaf']}_{t['line']}_{t['seg']}.jpg"]; x = b[0] + t["x"] // 2; return N[t["leaf"]].crop((x - 60, b[1], x + 60, b[3]))
    for t in pool("f101r", "C6") + pool("f188r", "C6"): its.append(((t["leaf"], t["line"], t["seg"], t["x"], "C6-glossed", t["letter"]), cut(t)))
    for code in ("PHI", "C43"):
        for t in rng.sample(pool("f101r", code), 3): its.append(((t["leaf"], t["line"], t["seg"], t["x"], "CTRL-" + code, t["letter"]), cut(t)))
    rng.shuffle(its); os.makedirs(f"{scratch}/h237", exist_ok=True); W, cw, ch = 5, 300, 240
    sh = Image.new("L", (W * cw, ((len(its) + W - 1) // W) * ch), 255); d = ImageDraw.Draw(sh); key = ["item\tleaf\tline\tsegment\tx\tclass\tletter"]
    for j, (k, im) in enumerate(its):
        im = ImageOps.autocontrast(im.resize((int(im.size[0] * 180 / im.size[1]), 180)), cutoff=2); im.thumbnail((cw - 10, 180))
        X, Y = (j % W) * cw, (j // W) * ch; sh.paste(im, (X + 5, Y + 28)); mx = X + 5 + im.size[0] // 2
        d.polygon([(mx - 8, Y + 8), (mx + 8, Y + 8), (mx, Y + 24)], fill=0); d.polygon([(mx - 8, Y + 228), (mx + 8, Y + 228), (mx, Y + 212)], fill=0)
        d.text((X + 8, Y + 4), f"Y{j + 1:02d}", fill=0); key.append(f"Y{j + 1:02d}\t" + "\t".join(map(str, k)))
    sh.convert("RGB").save(f"{scratch}/h237/sheet_01.jpg", quality=90); open(f"{HERE}/h237_items.tsv", "w").write("\n".join(key) + "\n")
    print(len(its), "tiles", Counter(k[4] for k, _ in its))
def score():
    its = {r["item"]: r for r in rd(f"{HERE}/h237_items.tsv")}; g = {r["tile"].strip(): r["group"].strip() for r in rd(f"{P}/h237_sort.tsv")}
    gl = [m for m, r in its.items() if r["class"] == "C6-glossed"]; f61 = [m for m, r in its.items() if r["class"] == "C6-f61"]; ct = [m for m, r in its.items() if r["class"].startswith("CTRL")]
    groups = [x for x in dict.fromkeys(g.values()) if x.lower() != "unclear"]; G = max(groups, key=lambda x: (sum(g.get(m) == x for m in gl), -groups.index(x)))
    a, z, o = sum(g.get(m) == G for m in gl), sum(g.get(m) == G for m in f61), sum(g.get(m) == G for m in ct)
    out = ["by class: " + "; ".join(f"{c}: " + " ".join(f"{x} {n}" for x, n in sorted(Counter(g.get(m, '-') for m, r in its.items() if r['class'] == c).items())) for c in ("C6-f61", "C6-glossed", "CTRL-PHI", "CTRL-C43")),
           f"G = {G}: glossed C6 {a}/{len(gl)}, f.61 C6 {z}/3, controls {o}/{len(ct)}"]
    ok = a >= min(2, len(gl)) and z == 3 and o <= 1
    out.append("read-out: " + ("f.61's C6 is the glossed C6 glyph" if ok else "no link shown"))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h237_c6_glyph_result.txt"
    if "--check" in sys.argv:
        ok2 = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok2 else "STALE"); sys.exit(0 if ok2 else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(*sys.argv[2:5]) if sys.argv[1] == "tiles" else score()
