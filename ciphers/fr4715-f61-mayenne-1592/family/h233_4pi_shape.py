#!/usr/bin/env python3
"""H233 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026): f.61's 'wider' tokens L01 11 (HASH4, d/q/i), L01 12 and L11 9 (4PI, d/a/q/n) and
f.101r's lettered 4PI positions (period gloss; pass-A-mapped as h220) by blind shape. Written before the call.
 tiles SCRATCH NATIVE101: H235's normalisation (grey, autocontrast, height 180, black triangles above/below the centre). f.61 positions placed by the
   runner's eye on images/f61sheet_L01.jpg / L11.jpg (both 2 segments; sheet px: L01 s2 x 1917 and 2214, L11 s2 x 864), x +-150. f.101r 4PI: every
   pass-A-mapped 4PI row with a letter; f.101r cut x +-60 by the band box. ANCHORS: H235's own 4-head hash tiles (4, reader group C there) and f.188r
   2-hook tiles (4, group A there), re-cut identically. Shuffled (seed 233), W01.., one or two sheets <scratch>/h233/. Key h233_items.tsv before the call.
 One blind Opus call, fixed categories: A = a 4-head on a stem crossed by hash bars (4 over #); D = a 2- or Z-shaped hooked head on two slanted
   strokes ('2#'); E = a figure-4 whose stem(s) are not crossed by hash bars (e.g. a 4 over two upright stems joined by a bar, or a plain 4);
   B = two small loops on a hash; N = none / cannot tell. Inline, no tools.
 score: GATE anchors >= 6 of 8 (4-head tiles A, 2-hook tiles D). Then f.101r 4PI forms x letters (d/q, a/n, other) and the three f.61 tokens' forms.
   Pre-stated read-out for 4PI: "4PI is the 4-head hash" iff >= 0.7 of answered f.101r 4PI are A; "4PI is its own sign" iff >= 0.7 are E;
   else "mixed". Descriptive; no key change.  python3 h233_4pi_shape.py tiles SCRATCH NATIVE101 | score [--check]"""
import csv, json, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
F61 = [("HASH4", "L01", 2, 1917), ("4PI", "L01", 2, 2214), ("4PI", "L11", 2, 864)]
def pool4pi():
    S = defaultdict(list)
    for r in rd(f"{P}/recf101r/ciphertext_draft.tsv"):
        if r["sign"] != "DASH": S[r["line"]].append(r)
    A = {(r["line"], int(r["pos"])): r for r in rd(f"{P}/f101r_signsA.tsv")}; out = []
    for r in rd(f"{P}/f101r_align_v4.tsv"):
        if r["kind"] != "code" or r["value"] != "4PI" or not r["plain_chunk"]: continue
        s = S[r["cipher_line"]][int(r["idx"])]
        if s["sign"] != "4PI": continue
        a = A.get((r["cipher_line"], int(s["position"])))
        if a and a["sign"] == "4PI": out.append(dict(line=r["cipher_line"], idx=r["idx"], letter=r["plain_chunk"], seg=a["segment"], x=int(a["x_px"])))
    return out
def tiles(scratch, n101):
    from PIL import Image, ImageDraw, ImageOps
    import h224_hash_188r as h224
    its = []; B1 = json.load(open(f"{HERE}/sheets/f101r_bands.json"))["boxes"]; N1 = Image.open(n101).convert("L")
    for cls, line, seg, x in F61:
        im = Image.open(f"{HERE}/../images/f61sheet_{line}.jpg").convert("L"); h = im.size[1] / 2
        its.append((("f61", line, f"s{seg}", x, cls, "-", "T"), im.crop((x - 150, int((seg - 1) * h) + 10, x + 150, int(seg * h) - 6))))
    for t in pool4pi():
        b = B1[f"f101r_{t['line']}_{t['seg']}.jpg"]; x = b[0] + t["x"] // 2
        its.append((("f101r", t["line"], t["seg"], t["x"], "4PI", t["letter"], "T"), N1.crop((x - 60, b[1], x + 60, b[3]))))
    # anchors: H235's 4-head (HASH4-A) and 2-hook tiles, same cut
    N8 = Image.open(os.environ.get("NATIVE188", "")).convert("L") if os.environ.get("NATIVE188") else None
    B8 = json.load(open(f"{HERE}/sheets/f188r_bands.json"))["boxes"]
    for r in rd(f"{HERE}/h235_items.tsv"):
        if r["class"] == "HASH4-A":
            b = B1[f"f101r_{r['line']}_{r['segment']}.jpg"]; x = b[0] + int(r["x"]) // 2
            its.append((("f101r", r["line"], r["segment"], r["x"], "ANCHOR-A", r["letter"], "C"), N1.crop((x - 60, b[1], x + 60, b[3]))))
        elif r["class"] == "2HOOK" and N8 is not None:
            b = B8[f"f188r_{r['line']}_{r['segment']}.jpg"]; x = b[0] + int(r["x"]) // 2
            its.append((("f188r", r["line"], r["segment"], r["x"], "ANCHOR-D", r["letter"], "C"), N8.crop((x - 60, b[1], x + 60, b[3]))))
    random.Random(233).shuffle(its); os.makedirs(f"{scratch}/h233", exist_ok=True); W, cw, ch = 5, 300, 240
    key = ["item\tleaf\tline\tsegment\tx\tclass\tletter\tkind"]; per = 20
    for s0 in range(0, len(its), per):
        chunk = its[s0:s0 + per]; sh = Image.new("L", (W * cw, ((len(chunk) + W - 1) // W) * ch), 255); d = ImageDraw.Draw(sh)
        for j, (k, im) in enumerate(chunk):
            n = s0 + j + 1; im = ImageOps.autocontrast(im.resize((int(im.size[0] * 180 / im.size[1]), 180)), cutoff=2); im.thumbnail((cw - 10, 180))
            X, Y = (j % W) * cw, (j // W) * ch; sh.paste(im, (X + 5, Y + 28)); mx = X + 5 + im.size[0] // 2
            d.polygon([(mx - 8, Y + 8), (mx + 8, Y + 8), (mx, Y + 24)], fill=0); d.polygon([(mx - 8, Y + 228), (mx + 8, Y + 228), (mx, Y + 212)], fill=0)
            d.text((X + 8, Y + 4), f"W{n:02d}", fill=0); key.append(f"W{n:02d}\t" + "\t".join(map(str, k)))
        sh.convert("RGB").save(f"{scratch}/h233/sheet_{s0 // per + 1:02d}.jpg", quality=90)
    open(f"{HERE}/h233_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "tiles", Counter(k[4] for k, _ in its))
def cell(L): return "d/q" if L in "dq" else "a/n" if L in "an" else "other"
def score():
    its = rd(f"{HERE}/h233_items.tsv"); ans = {r["id"]: r["answer"].strip().upper() for r in rd(f"{P}/h233_reply.tsv")}
    C = [r for r in its if r["kind"] == "C"]; hit = sum(ans.get(r["item"]) == ("A" if r["class"] == "ANCHOR-A" else "D") for r in C)
    out = [f"anchors: {hit} of {len(C)} (4-head -> A, 2-hook -> D; gate >= 6): {'PASS' if hit >= 6 else 'CONTROL FAIL'}"]
    if hit >= 6:
        T = [r for r in its if r["kind"] == "T" and r["leaf"] == "f101r"]; t = defaultdict(Counter)
        for r in T: t[ans.get(r["item"], "N")][cell(r["letter"])] += 1
        out.append("f.101r 4PI: " + "; ".join(f"{f} {sum(t[f].values())} (" + " ".join(f"{c} {n}" for c, n in sorted(t[f].items())) + ")" for f in sorted(t)))
        out.append("f.61 tokens: " + "; ".join(f"{r['line']} {r['class']} x{r['x']} -> {ans.get(r['item'], 'N')}" for r in its if r["leaf"] == "f61"))
        n = sum(sum(v.values()) for f, v in t.items() if f != "N"); a = sum(t["A"].values()) / max(1, n); e = sum(t["E"].values()) / max(1, n)
        out.append(f"read-out: 4PI answered {n}, A share {a:.2f}, E share {e:.2f} -> " + ("4PI is the 4-head hash" if a >= 0.7 else "4PI is its own sign" if e >= 0.7 else "mixed"))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h233_4pi_shape_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(*sys.argv[2:4]) if sys.argv[1] == "tiles" else score()
