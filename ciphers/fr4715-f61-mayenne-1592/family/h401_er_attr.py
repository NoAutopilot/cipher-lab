#!/usr/bin/env python3
"""H401/H402 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026), written before the look and before the call: does a visible attribute
separate the e form from the r form of PHI in f.61's own hand? The published table (keys/key_mayenne_1592.tsv) draws e and r as two symbols; the
free sort that failed on it (H71) is a retired instrument; this is H193's forced-choice design.
 anchors (H401) -- every f.108r PHI paired with a period overlay letter e or r (h202_bowl_108r.pairs() with the class set to PHI; f.61's hand;
   13 e, 7 r), cut exactly as H202 cuts its tiles (images/f108sheetB_<row>.jpg, 300 px, marker UNDER the sign), sheet SCRATCH/h401/anchors_by_group.jpg
   (e group rows 1-4, r group from row 5 on). The runner looks at this sheet ONLY and writes the attribute into h401_attribute.txt (question text and
   which group 'yes' names), or 'none visible'. Nothing else is looked at.
 call (H402) -- part 1: the 20 anchors shuffled (seed 401), P01..P20, marker UNDER. part 2: f.61's 17 PHI (13 inside Tomokiyo's spans, 4 not;
   scripts/f61_positions_all.tsv x mapped as h367, window -45/+92, marker ABOVE) and 20 f.101r PHI whose period letter is e or r (10 e, 10 r, seed 402;
   v11_crosstab.letter_map, draft agree positions, pass A geometry, window -60/+55, marker ABOVE), shuffled (seed 4021), R01..R37, 20 per sheet.
 score (H402) -- GATE: >= 16/20 anchors in the named direction, else CONTROL FAIL. Pre-stated on f.61's 13 lettered PHI (held out): "the attribute
   tracks e/r on f.61's hand" iff both r answered on the r side and >= 10 of 11 e on the e side; else "no e/r attribute at this N". The exact
   hypergeometric p of the observed r-side count among the r-side answers is reported. f.101r: agreement and permutation p, descriptive. On a pass,
   f.61's 4 unlettered PHI are listed with the attribute's letter as a PROPOSAL for the verifier. No key, cell or grade change.
 python3 h401_er_attr.py look SCRATCH | tiles SCRATCH | score [--check]"""
import csv, json, os, random, sys
from math import comb
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.abspath(f"{HERE}/.."); P = f"{HERE}/passes"; IM = f"{T}/images"
sys.path.insert(0, HERE); sys.path.insert(0, f"{T}/verify_v9"); sys.path.insert(0, f"{T}/verify_v11"); CHECK = "--check" in sys.argv
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def anchors():
    argv = sys.argv; sys.argv = ["x", "score"]; import h202_bowl_108r as h; sys.argv = argv
    h.FAM = ("PHI",); return [p for p in h.pairs() if p["letter"] in "er"]
def f61_phi():
    import v9_ca_sort as v
    B = v.bands(); sp = {}
    for line in open(f"{T}/scripts/f61_skeleton.txt"):
        pass
    out = []
    for r in rd(f"{T}/scripts/f61_positions_all.tsv"):
        if r["class"] != "PHI": continue
        x = round(v.nat_x("A", r["line"], int(r["segment"]), int(r["x"]))); b = v.band_of(B, r["line"], x); out.append((r["line"], r["pos"], x, (b[1] + b[3]) // 2))
    return out
def f61_letters():
    """Tomokiyo's letter by (line, pos) from scripts/f61_skeleton.txt (T:x tokens), positions 1-based in skeleton order."""
    L = open(f"{T}/scripts/f61_skeleton.txt").read().split("\n"); out = {}
    for i, l in enumerate(L):
        if l.startswith("L") and " signs): " in l:
            line = l.split()[0]; toks = l.split("): ", 1)[1].split(); cls = L[i + 1].split(": ", 1)[1].split()
            for k, (t, c) in enumerate(zip(toks, cls), 1): out[(line, str(k))] = (c, t[2:] if t.startswith("T:") else "")
    return out
def f101r_phi():
    import v11_crosstab as X
    lm = X.letter_map("f101r"); A = {(r["line"], r["pos"]): r for r in rd(f"{P}/f101r_signsA.tsv")}; B = json.load(open(f"{HERE}/sheets/f101r_bands.json"))["boxes"]
    pool = {"e": [], "r": []}
    for r in rd(f"{P}/recf101r/ciphertext_draft.tsv"):
        k = (r["line"], r["position"]); a = A.get(k)
        if r["sign"] != "PHI" or not r["why"].startswith("agree") or k not in lm or not a or a["sign"] != "PHI": continue
        L = lm[k][0]
        if L in pool: bx = B[f"f101r_{a['line']}_{a['segment']}.jpg"]; pool[L].append((r["line"], r["position"], bx[0] + int(float(a["x_px"])) // 2, bx[1] + 80, L))
    rng = random.Random(402); return rng.sample(pool["e"], 10) + rng.sample(pool["r"], 10), len(pool["e"]), len(pool["r"])
def anchor_tile(t, label):
    from PIL import Image, ImageDraw
    im = Image.open(f"{IM}/f108sheetB_{t['row']}.jpg").convert("RGB"); st = (im.height + 12) // 4; y0 = (t["seg"] - 1) * st; y1 = y0 + st - 12
    x0 = max(0, min(im.width - 300, t["x"] - 150)); w = im.crop((x0, y0, x0 + 300, y1)); s = 150 / w.height if w.height * 1.2 > 150 else 1.2
    w = w.resize((int(300 * s), int(w.height * s))); c = Image.new("RGB", (370, 190), "white"); c.paste(w, (5, 0)); d = ImageDraw.Draw(c)
    mx = 5 + int((t["x"] - x0) * s); y = w.height; d.polygon([(mx - 9, y + 16), (mx + 9, y + 16), (mx, y + 2)], fill=(220, 0, 0)); d.text((6, y + 20), label, fill=(0, 0, 0))
    return c
def strip(img, x, yc, up, dn, label):
    from PIL import Image, ImageDraw
    t = img.crop((x - 150, yc - up, x + 150, yc + dn)); t = t.resize((360, int(t.height * 1.2)))
    c = Image.new("RGB", (370, 190), "white"); c.paste(t.crop((0, 0, 360, min(t.height, 165))), (5, 22)); d = ImageDraw.Draw(c); mx = 5 + int(150 * 1.2)
    d.polygon([(mx - 9, 2), (mx + 9, 2), (mx, 18)], fill=(220, 0, 0)); d.text((330, 4), label, fill=(0, 0, 0)); return c
def sheet(ims, path, rows=5):
    from PIL import Image
    sh = Image.new("RGB", (4 * 370, rows * 190), "white")
    for k, c in enumerate(ims): sh.paste(c, ((k % 4) * 370, (k // 4) * 190))
    sh.save(path, quality=88)
def look(scratch):
    an = anchors(); os.makedirs(f"{scratch}/h401", exist_ok=True)
    e = [anchor_tile(t, f"e{n}") for n, t in enumerate([t for t in an if t["letter"] == "e"], 1)]; r = [anchor_tile(t, f"r{n}") for n, t in enumerate([t for t in an if t["letter"] == "r"], 1)]
    sheet(e + [None] * (16 - len(e)) if False else e, f"{scratch}/h401/anchors_e.jpg", 4); sheet(r, f"{scratch}/h401/anchors_r.jpg", 2)
    print(len(e), "e anchors,", len(r), "r anchors")
def tiles(scratch):
    from PIL import Image
    an = anchors(); random.Random(401).shuffle(an); key = ["item\tpart\tleaf\tline\tpos\tletter"]; ims1 = []
    for n, t in enumerate(an, 1): ims1.append(anchor_tile(t, f"P{n:02d}")); key.append(f"P{n:02d}\tanchor\tf108r\t{t['row']}\t{t['pos']}\t{t['letter']}")
    os.makedirs(f"{scratch}/h402", exist_ok=True); sheet(ims1, f"{scratch}/h402/part1.jpg")
    lets = f61_letters(); nat61 = Image.open(f"{IM}/src_ark_12148_btv1b52509819x_f137_500_1880_3320_1420.jpg").convert("RGB"); nat101 = Image.open(f"{scratch}/nat/f101r.jpg").convert("RGB")
    its = []
    for line, pos, x, yc in f61_phi():
        c, L = lets.get((line, pos), ("?", "")); assert c == "PHI", (line, pos, c); its.append(("f61", line, pos, x, yc, L))
    f1, ne, nr = f101r_phi(); its += [("f101r", l, p, x, yc, L) for l, p, x, yc, L in f1]; random.Random(4021).shuffle(its); ims = []
    for n, (leaf, line, pos, x, yc, L) in enumerate(its, 1):
        ims.append(strip(nat61, x, yc, 45, 92, f"R{n:02d}") if leaf == "f61" else strip(nat101, x, yc, 60, 55, f"R{n:02d}")); key.append(f"R{n:02d}\ttarget\t{leaf}\t{line}\t{pos}\t{L}")
    for s in range(0, len(ims), 20): sheet(ims[s:s + 20], f"{scratch}/h402/sheet_{s // 20 + 1:02d}.jpg")
    open(f"{HERE}/h402_items.tsv", "w").write("\n".join(key) + "\n"); print(len(an), "anchors;", len(its), "targets; f.101r pools e", ne, "r", nr)
def score():
    att = open(f"{HERE}/h401_attribute.txt").read(); yes_is = [l.split(":", 1)[1].strip() for l in att.split("\n") if l.startswith("yes_group:")][0]
    ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h402_reply.tsv")}; it = rd(f"{HERE}/h402_items.tsv")
    side = lambda a: None if a not in ("yes", "no") else (yes_is if a == "yes" else ("r" if yes_is == "e" else "e"))
    an = [r for r in it if r["part"] == "anchor"]; g = sum(side(ans.get(r["item"])) == r["letter"] for r in an)
    out = [f"attribute (yes = {yes_is}); gate: {g}/20 anchors on their letter's side (>= 16)"]
    if g < 16: out.append("CONTROL FAIL -- nothing scored")
    else:
        f = [r for r in it if r["leaf"] == "f61" and r["letter"] in ("e", "r")]; rr = [r for r in f if r["letter"] == "r"]; ee = [r for r in f if r["letter"] == "e"]
        hr = sum(side(ans.get(r["item"])) == "r" for r in rr); he = sum(side(ans.get(r["item"])) == "e" for r in ee); ans_r = sum(side(ans.get(r["item"])) == "r" for r in f)
        N, K, n = len(f), len(rr), ans_r; p = sum(comb(K, k) * comb(N - K, n - k) for k in range(hr, min(K, n) + 1)) / comb(N, n) if n else 1.0
        ok = hr == len(rr) and he >= len(ee) - 1
        out.append(f"f.61 lettered PHI {N} (e {len(ee)}, r {len(rr)}): r on r side {hr}/{len(rr)}, e on e side {he}/{len(ee)}; answered r-side {n}; hypergeometric p {p:.4f}")
        out.append("read-out: " + ("the attribute tracks e/r on f.61's hand" if ok else "no e/r attribute at this N"))
        out.append("f.61 per position: " + " ".join(f"{r['line']}/{r['pos']}:{r['letter'] or '?'}>{ans.get(r['item'], 'missing')}" for r in sorted((r for r in it if r["leaf"] == "f61"), key=lambda r: (r["line"], int(r["pos"])))))
        b = [r for r in it if r["leaf"] == "f101r"]; hb = sum(side(ans.get(r["item"])) == r["letter"] for r in b); nb = sum(side(ans.get(r["item"])) is not None for r in b)
        out.append(f"f.101r (another hand, descriptive): {hb}/{nb} answered on their letter's side")
        if ok: out.append("PROPOSAL for the verifier (no grade): " + " ".join(f"{r['line']}/{r['pos']} {side(ans.get(r['item'])) or 'n'}" for r in it if r["leaf"] == "f61" and not r["letter"]))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h402_er_attr_result.txt"
    if CHECK:
        ok2 = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok2 else "STALE"); sys.exit(0 if ok2 else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]
    look(a[1]) if a[0] == "look" else tiles(a[1]) if a[0] == "tiles" else score()
