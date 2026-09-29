#!/usr/bin/env python3
"""H407 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026), written before the call: the two Tomokiyo span letters key v8 misses on f.61
(L07/4, reader code BETA, his 'a' in 'jal'; the final 'e' of S2 'capable', no sign after L03/15) as transcription questions, with controls.
The runner has looked at the target lines (NOTES H407: L07/4 drawn like the 43 glyph; a PHI-like sign after L03/15's bracket); the reader has not.
 part A (sheet A1 = references, A2 = items): H367 geometry (300 native px, x1.2, marker ABOVE) from the f.61 native region image, x from
   scripts/f61_positions_all.tsv via verify_v9 (as h367). References: X = L11/1 (BETA, Tomokiyo m), Y = L03/8 (C43, Tomokiyo a). Items (shuffled,
   seed 407): L07/4 at three windows (W1 -45/+92, W2 -60/+55, W3 -70/+110); known Y = the C43 at L01/3, L05/9, L05/11, L05/13, L08/2, L08/7;
   known 'neither' = the PHI at L01/5, L05/15, L08/6 (L08/1 replaced before the call: marker between two signs). Question: same sign as X, as Y, or neither (n if it cannot be told).
 part B (sheet B): strips from a marked cipher sign rightwards (start x - 60 to x + 1100 native, the band's height), marker above the start sign:
   B1 = L03 from pos 10 (pass A: 6 signs to the line's clear text), B2 = L05 from pos 13 (pass A 6), B3 = L08 from pos 11 (pass A 4; CHANGED before the call from pos 9 after the runner looked at the strips for placement: L08 pos 10 is the letter-shaped CA null, which a reader could take for a clear word). Question:
   count the cipher signs from the marked one (inclusive) to the first word of ordinary handwriting, and describe the last one.
 score -- GATE A: >= 8/9 known items; GATE B: B2 count exactly 6 and B3 exactly 4. Pre-stated: A: W1-W3 majority 'Y' -> 'L07/4 is the 43 sign (C43,
   a/n): the BETA code there is a reader slip'; majority 'X' -> 'L07/4 is the beta sign: the conflict with Tomokiyo stands'; else undecided.
   B: B1 count 7 and the last described as loops/rings on a stem -> 'pass A missed a sign at L03/16 (PHI-like)'; B1 = 6 -> 'pass A stands'; else
   undecided. Transcription only; no key, grade or class change (the verifier's).  python3 h407_span_miss.py tiles SCRATCH | score [--check]"""
import csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.abspath(f"{HERE}/.."); P = f"{HERE}/passes"; sys.path.insert(0, f"{T}/verify_v9")
CHECK = "--check" in sys.argv
REG = f"{T}/images/src_ark_12148_btv1b52509819x_f137_500_1880_3320_1420.jpg"
KY = [("L01", "3"), ("L05", "9"), ("L05", "11"), ("L05", "13"), ("L08", "2"), ("L08", "7")]; KN = [("L01", "5"), ("L05", "15"), ("L08", "6")]   # L08/1 replaced by L08/6 before the call: its marker fell between two signs (placement look)
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def geo():
    import v9_ca_sort as v
    B = v.bands(); out = {}
    for r in rd(f"{T}/scripts/f61_positions_all.tsv"):
        x = round(v.nat_x("A", r["line"], int(r["segment"]), int(r["x"]))); b = v.band_of(B, r["line"], x); out[(r["line"], r["pos"])] = (r["class"], x, (b[1] + b[3]) // 2, b)
    return out
def crop(im, x0, y0, x1, y1):
    from PIL import Image
    c = Image.new("RGB", (x1 - x0, y1 - y0), "white"); c.paste(im.crop((max(0, x0), max(0, y0), min(im.width, x1), min(im.height, y1))), (max(0, -x0), max(0, -y0))); return c
def strip(im, x, yc, up, dn, label):
    from PIL import Image, ImageDraw
    t = crop(im, x - 150, yc - up, x + 150, yc + dn).resize((360, int((up + dn) * 1.2)))
    c = Image.new("RGB", (370, 190), "white"); c.paste(t.crop((0, 0, 360, min(t.height, 165))), (5, 22)); d = ImageDraw.Draw(c); mx = 5 + 180
    d.polygon([(mx - 9, 2), (mx + 9, 2), (mx, 18)], fill=(220, 0, 0)); d.text((320, 4), label, fill=(0, 0, 0)); return c
def tiles(scratch):
    from PIL import Image, ImageDraw
    G = geo(); im = Image.open(REG).convert("RGB"); os.makedirs(f"{scratch}/h407", exist_ok=True); key = ["item\tpart\tline\tpos\tcode\twindow\tknown"]
    refs = [strip(im, G[("L11", "1")][1], G[("L11", "1")][2], 45, 92, "REF X"), strip(im, G[("L03", "8")][1], G[("L03", "8")][2], 45, 92, "REF Y")]
    sh = Image.new("RGB", (2 * 370, 190), "white"); [sh.paste(c, (k * 370, 0)) for k, c in enumerate(refs)]; sh.save(f"{scratch}/h407/A1_references.jpg", quality=90)
    its = [("W1", "L07", "4", 45, 92, ""), ("W2", "L07", "4", 60, 55, ""), ("W3", "L07", "4", 70, 110, "")] + [("K", l, p, 45, 92, "Y") for l, p in KY] + [("K", l, p, 45, 92, "neither") for l, p in KN]
    random.Random(407).shuffle(its); ims = []
    for n, (w, l, p, up, dn, kn) in enumerate(its, 1):
        c, x, yc, _ = G[(l, p)]; ims.append(strip(im, x, yc, up, dn, f"A{n:02d}")); key.append(f"A{n:02d}\tA\t{l}\t{p}\t{c}\t{w}\t{kn}")
    sh = Image.new("RGB", (4 * 370, 3 * 190), "white"); [sh.paste(c, ((k % 4) * 370, (k // 4) * 190)) for k, c in enumerate(ims)]; sh.save(f"{scratch}/h407/A2_items.jpg", quality=90)
    ss = []
    for lab, (l, p, known) in zip(("B1", "B2", "B3"), (("L03", "10", ""), ("L05", "13", "6"), ("L08", "11", "4"))):
        c, x, yc, b = G[(l, p)]; t = crop(im, x - 60, b[1] - 25, x + 1100, b[3] + 30); t = t.resize((int(t.width * 1.2), int(t.height * 1.2)))
        cv = Image.new("RGB", (t.width + 10, t.height + 44), "white"); cv.paste(t, (5, 26)); d = ImageDraw.Draw(cv); mx = 5 + int(60 * 1.2)
        d.polygon([(mx - 10, 4), (mx + 10, 4), (mx, 22)], fill=(220, 0, 0)); d.text((cv.width - 40, 6), lab, fill=(0, 0, 0)); ss.append(cv)
        key.append(f"{lab}\tB\t{l}\t{p}\t{c}\t\t{known}")
    H = sum(c.height for c in ss); W = max(c.width for c in ss); sh = Image.new("RGB", (W, H + 20), "white"); y = 0
    for c in ss: sh.paste(c, (0, y)); y += c.height + 10
    sh.save(f"{scratch}/h407/B_strips.jpg", quality=90); open(f"{HERE}/h407_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "part A items; 3 strips")
def score():
    ans = {r["id"]: r for r in rd(f"{P}/h407_reply.tsv")}; it = rd(f"{HERE}/h407_items.tsv"); a = lambda i: ans.get(i, {}).get("answer", "missing").strip()
    kn = [r for r in it if r["part"] == "A" and r["known"]]; gA = sum(a(r["item"]).lower() == r["known"].lower() for r in kn)
    bs = {r["item"]: r for r in it if r["part"] == "B"}; cnt = lambda i: a(i).split(";")[0].strip()
    gB = cnt("B2") == "6" and cnt("B3") == "4"
    out = [f"gate A: {gA}/{len(kn)} known items (>= 8); gate B: control counts B2 {cnt('B2')}, B3 {cnt('B3')} (6 and 4: {'PASS' if gB else 'FAIL'})"]
    if gA >= 8:
        w = [a(r["item"]).upper() for r in it if r["part"] == "A" and r["window"].startswith("W")]; y, x = w.count("Y"), w.count("X")
        ro = "L07/4 is the 43 sign (C43, a/n): the BETA code there is a reader slip" if y >= 2 else "L07/4 is the beta sign: the conflict with Tomokiyo stands" if x >= 2 else "undecided"
        out.append(f"A: L07/4 windows {w} -> {ro}")
    else: out.append("A: CONTROL FAIL -- nothing scored")
    if gB:
        c1 = cnt("B1"); last = ans.get("B1", {}).get("note", "")
        ro = "pass A missed a sign at L03/16 (PHI-like)" if c1 == "7" and any(k in last.lower() for k in ("loop", "ring", "circle", "phi", "φ")) else "pass A stands" if c1 == "6" else "undecided"
        out.append(f"B: L03 from pos 10 count {c1} (pass A 6); last sign: {last} -> {ro}")
    else: out.append("B: CONTROL FAIL -- nothing scored")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h407_span_miss_result.txt"
    if CHECK:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]
    tiles(a[1]) if a[0] == "tiles" else score()
