#!/usr/bin/env python3
"""VERIFY-F61-V9 (29 Sept 2026, account 3): re-run of runner 10's CA letterform sort (H256/H260) with the verifier's own tiles and fresh readers.
Question under audit: do f.61's ten CA ('a'-shaped; Tomokiyo's nulls, H44) carry the letterform of the scribe's own clear-text a, and can a
'clear a drawn among the signs' be told from a 'null drawn as an a' from the leaf at all?

Design, fixed before any tile existed or any look (this file's first commit):
 tiles -- cut by this script from the NATIVE region image images/src_ark_12148_btv1b52509819x_f137_500_1880_3320_1420.jpg (3320 x 1420, one
   Gallica request of 27 Sept 2026, sha1 in family/MANIFEST.tsv), never from the runner's sheets or tiles: +-60 native px around the sign's x,
   the full line band (tools/iiif_lines.py --overlap 0 boxes, re-derived offline into the scratch), grey, autocontrast, height 180, red triangles
   above and below the centre. Sign x's: H253/H257's positions (scripts/f61_positions_all.tsv, scripts/f61_positions_L10.tsv), mapped from
   sheet to native by the segment boxes (nat_x below). Text letters: from a placement pass by a separate Sonnet helper (three calls, lines
   L01-L11, clear words only, x from a ruler) -- never the runner's words (auons parle amplement Cependant ella affere pas depar tances maintenant
   particulieres); the verifier looks at a strip of the TEXT tiles only, for placement, and discloses it in PROMPTS.md.
 sample -- CA 10 (all of f.61's), cipher controls 11 (PHI 4, C43 3, C6 2, SBS 1, INF 1: signs from the same runs), text a 12 (seeded random from the
   helper's list after exclusions, at most 2 per line), text non-a 10 (o, u, n, e, c, d: two each where available, seeded), and 6 repeats under new
   ids (2 CA, 2 text a, 2 cipher).  Three fresh Opus readers, each with its own shuffle and ids: setP and setQ with fixed categories, setR a free
   sort in the runner's own format (2-6 groups by letterform) as a like-for-like replication.
 categories (P, Q) -- A = a closed round or oval bowl with one upright stroke on its RIGHT side (the stroke may rise above the bowl or stop at its
   top); O = a closed ring alone, no stem; U = two uprights joined by a curve at the bottom or an n-like arch, no closed bowl; E = a small closed
   loop with an open tongue or crossbar (e- or c-like); S = a sign with a hash or bars, a phi-like loop crossed by a long vertical, a 43-like
   figure, a 6-like figure, a bracket, or any other shape not above; X = cannot tell.
 gates (each set) -- (1) text a in A >= 0.8 of the text a's, else CONTROL FAIL, nothing scored; (2) repeats: >= 5 of 6 same answer as the original;
   (3) hand check: text non-a letters in A <= 1 of 10, else NON-TEST (the reader put clear letters in A by hand, not shape).
 read-outs (each set that passes) -- Z1 'CA has the clear a's letterform': >= 8 of 10 CA in A and <= 1 of 11 cipher controls in A;
   Z2 'CA is a distinct glyph': <= 2 of 10 CA in A. Null: 20,000 within-leaf permutations of the answers over the CA + cipher tiles of
   S = #(CA & A) + #(cipher & not A); p reported. setR: G = the group holding most text a's; same counts and p; no gate 3 possible if the reader
   made one group of everything (reported as such).
 what the sort can and cannot show (fixed now) -- a PASS on Z1 says the null-or-letter is written as an a; it cannot separate 'clear a' from 'null
   drawn as an a', which is a question about function (does the plaintext carry an a there), answered only by the known spans (H259) and not by
   the leaf's ink. That separation is audited in AUDIT.md from the span table, not from this sort.
 ink measures (script-only, no reader) -- for every tile: ink height (rows with dark ink), ink width, and mean darkness of the ink pixels in the
   central 60 px, CA vs text a vs cipher, as a size/weight check on H63's hand verdict.
usage: python3 v9_ca_sort.py tiles SCRATCH | score [--check] | measure"""
import csv, json, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.abspath(f"{HERE}/.."); IM = f"{T}/images"
NAT = f"{IM}/src_ark_12148_btv1b52509819x_f137_500_1880_3320_1420.jpg"
KEEP_A = {"L01": [4, 5], "L03": [1, 2, 3], "L05": [2, 3, 4], "L07": [3, 4, 5], "L08": [1, 2], "L11": [1, 2]}   # images/regen_f61r_sheets.sh
X0_A = lambda s: (s - 1) * 605; X0_B = [0, 807, 1613, 2420]                                                    # f61s_/f61n_ segment boxes
RUNNER_WORDS = {"auons", "parle", "amplement", "cependant", "ella", "affere", "pas", "depar", "tances", "maintenant", "particulieres"}
def nat_x(sheet, line, seg, x):
    """sheet 'A' = images/f61sheet_Lxx.jpg (H253 positions), 'B' = images/f61sheetB_Lxx.jpg (H63/H260 L10 positions); x at 3x."""
    return (X0_A(KEEP_A[line][seg - 1]) if sheet == "A" else X0_B[seg - 1]) + x / 3
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def signs():
    P = rd(f"{T}/scripts/f61_positions_all.tsv") + [dict(r, src="L10") for r in rd(f"{T}/scripts/f61_positions_L10.tsv")]
    ctrl = {("PHI", "L01", 5), ("PHI", "L03", 4), ("PHI", "L05", 15), ("PHI", "L08", 1), ("C43", "L01", 3), ("C43", "L05", 9), ("C43", "L11", 5),
            ("C6", "L03", 11), ("C6", "L08", 3), ("SBS", "L05", 5), ("INF", "L08", 4)}
    out = []
    for r in P:
        key = (r["class"], r["line"], int(r["pos"]))
        if r["class"] == "CA" or key in ctrl:
            sh = "B" if r["line"] == "L10" else "A"
            xs = int(r["x"]) if sh == "A" else {2: (3, 1440), 9: (4, 980), 12: (4, 1840)}.get(int(r["pos"]), (0, 0))[1]
            seg = int(r["segment"]) if sh == "A" else {2: 3, 9: 4, 12: 4}[int(r["pos"])]
            if sh == "B" and r["class"] != "CA": continue
            out.append(dict(kind="CA" if r["class"] == "CA" else "CIPHER", cls=r["class"], line=r["line"], ref=f"{r['line']}p{r['pos']}",
                            x=round(nat_x(sh, r["line"], seg, xs))))
    return out
def text_items(rng):
    rows = rd(f"{HERE}/v9_text_letters.tsv")   # the helper's placement rows, merged, columns line word letter x
    rows = [r for r in rows if r["word"].strip("?").lower() not in RUNNER_WORDS]
    a = [r for r in rows if r["letter"] == "a"]; rng.shuffle(a); per = Counter(); ta = []
    for r in a:
        if per[r["line"]] < 2 and len(ta) < 12: ta.append(r); per[r["line"]] += 1
    tx = []
    for L in "ounecd":
        c = [r for r in rows if r["letter"] == L]; rng.shuffle(c); tx += c[:2]
    tx = tx[:10]
    return ([dict(kind="TEXT_A", cls=f"a:{r['word']}", line=r["line"], ref=f"{r['line']}x{r['x']}", x=int(float(r["x"]))) for r in ta] +
            [dict(kind="TEXT_X", cls=f"{r['letter']}:{r['word']}", line=r["line"], ref=f"{r['line']}x{r['x']}", x=int(float(r["x"]))) for r in tx])
def bands():
    b = json.load(open(f"{HERE}/v9_bands.json"))["iiif_lines"]; return {e["crop"]: e["box"] for e in b}
def band_of(B, line, x):
    for s in range(4, 0, -1):
        if x >= X0_B[s - 1]: return B[f"f61n_{line}_s{s}.jpg"]
def cut(it, nat, B):
    from PIL import ImageOps
    b = band_of(B, it["line"], it["x"]); w = nat.crop((it["x"] - 60, b[1], it["x"] + 60, b[3]))
    w = w.resize((360, max(1, int(w.height * 3)))); return ImageOps.autocontrast(w.convert("L"), cutoff=1).convert("RGB")
def sheet(tiles, path):
    from PIL import Image, ImageDraw
    W, cw, ch = 5, 380, 250; sh = Image.new("RGB", (W * cw, ((len(tiles) + W - 1) // W) * ch), "white"); d = ImageDraw.Draw(sh)
    for n, (tid, im) in enumerate(tiles):
        im = im.copy(); im.thumbnail((cw - 20, 190)); X, Y = (n % W) * cw, (n // W) * ch; sh.paste(im, (X + 10, Y + 30)); mx = X + 10 + im.width // 2
        d.polygon([(mx - 9, Y + 8), (mx + 9, Y + 8), (mx, Y + 27)], fill=(220, 0, 0)); d.polygon([(mx - 9, Y + 246), (mx + 9, Y + 246), (mx, Y + 226)], fill=(220, 0, 0))
        d.text((X + 6, Y + 4), tid, fill=(0, 0, 0))
    sh.save(path, quality=90)
SETS = (("setP", "P", 901), ("setQ", "Q", 902), ("setR", "R", 903))
def tiles(scratch):
    from PIL import Image
    rng = random.Random(9); its = signs() + text_items(rng); nat = Image.open(NAT).convert("RGB"); B = bands()
    dup = rng.sample([i for i, t in enumerate(its) if t["kind"] == "CA"], 2) + rng.sample([i for i, t in enumerate(its) if t["kind"] == "TEXT_A"], 2) + \
          rng.sample([i for i, t in enumerate(its) if t["kind"] == "CIPHER"], 2)
    key = ["set\tid\tkind\tcls\tline\tref\tx\trepeat_of"]; base = [(t, cut(t, nat, B)) for t in its]
    for name, pre, seed in SETS:
        r2 = random.Random(seed); order = list(range(len(its))) + [("dup", i) for i in dup]; r2.shuffle(order)
        os.makedirs(f"{scratch}/{name}", exist_ok=True); tl = []
        for n, o in enumerate(order, 1):
            i = o[1] if isinstance(o, tuple) else o; t, im = base[i]; tid = f"{pre}{n:03d}"; tl.append((tid, im))
            key.append(f"{name}\t{tid}\t{t['kind']}\t{t['cls']}\t{t['line']}\t{t['ref']}\t{t['x']}\t{'dup' if isinstance(o, tuple) else ''}")
        for s in range(0, len(tl), 20): sheet(tl[s:s + 20], f"{scratch}/{name}/sheet_{s // 20 + 1:02d}.jpg")
        print(name, len(tl), "tiles,", (len(tl) + 19) // 20, "sheets")
    open(f"{HERE}/v9_items.tsv", "w").write("\n".join(key) + "\n")
    # placement strip of the TEXT tiles only (the verifier may look at this)
    sheet([(t["cls"], im) for t, im in base if t["kind"].startswith("TEXT")], f"{scratch}/place_text.jpg")
def perm(rows, ans, n=20000, seed=99):
    lab = [ans[r["id"]] for r in rows]; S = lambda L: sum((L[i] == "A") == (r["kind"] == "CA") for i, r in enumerate(rows)); obs = S(lab)
    rng = random.Random(seed); byline = defaultdict(list)
    for i, r in enumerate(rows): byline[r["line"]].append(i)
    ge = 0
    for _ in range(n):
        L = lab[:]
        for idx in byline.values():
            v = [lab[i] for i in idx]; rng.shuffle(v)
            for i, x in zip(idx, v): L[i] = x
        ge += S(L) >= obs
    return obs, (ge + 1) / (n + 1)
def score():
    items = rd(f"{HERE}/v9_items.tsv"); out = []
    for name, pre, _ in SETS:
        f = f"{HERE}/v9_reply_{name}.tsv"
        if not os.path.exists(f): out.append(f"{name}: no reply file"); continue
        ans = {r["id"].strip(): r["answer"].strip() for r in rd(f)}; its = [r for r in items if r["set"] == name]
        orig = {(r["kind"], r["ref"]): r["id"] for r in its if not r["repeat_of"]}
        if name == "setR":   # free sort: A := the group holding most text a's
            G = Counter(ans.get(r["id"]) for r in its if r["kind"] == "TEXT_A" and not r["repeat_of"]).most_common(1)[0][0]
            ans = {k: ("A" if v == G else "N") for k, v in ans.items()}; out.append(f"{name}: G = group {G}")
        rep = sum(ans.get(r["id"]) == ans.get(orig[(r["kind"], r["ref"])]) for r in its if r["repeat_of"]); its = [r for r in its if not r["repeat_of"]]
        by = lambda k: [r for r in its if r["kind"] == k]; nA = lambda rs: sum(ans.get(r["id"]) == "A" for r in rs)
        ta, tx, ca, ci = by("TEXT_A"), by("TEXT_X"), by("CA"), by("CIPHER")
        out.append(f"{name}: by kind: " + "; ".join(f"{k} " + " ".join(f"{a} {c}" for a, c in sorted(Counter(ans.get(r['id'], '-') for r in rs).items()))
                                                 for k, rs in (("text a", ta), ("text non-a", tx), ("CA", ca), ("cipher", ci))))
        out.append(f"{name}: text a in A {nA(ta)}/{len(ta)}, repeats {rep}/6, text non-a in A {nA(tx)}/{len(tx)}, CA in A {nA(ca)}/{len(ca)}, cipher in A {nA(ci)}/{len(ci)}")
        g1 = nA(ta) >= 0.8 * len(ta); g2 = rep >= 5; g3 = nA(tx) <= 1
        if not g1: out.append(f"{name}: gate 1 CONTROL FAIL (text a's not in A); nothing scored"); continue
        if not g2: out.append(f"{name}: gate 2 repeat control FAIL ({rep}/6); nothing scored"); continue
        if not g3: out.append(f"{name}: gate 3 NON-TEST (text non-a letters in A {nA(tx)}); nothing scored"); continue
        obs, p = perm(ca + ci, ans)
        out.append(f"{name}: gates pass; S = #(CA & A) + #(cipher & not A) = {obs} of {len(ca) + len(ci)}, within-line permutation p {p:.2g}")
        out.append(f"{name}: Z1 CA has the clear a's letterform: {'YES' if nA(ca) >= 8 and nA(ci) <= 1 else 'no'}; Z2 CA is a distinct glyph: {'YES' if nA(ca) <= 2 else 'no'}")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/v9_ca_sort_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
def measure():
    from PIL import Image
    nat = Image.open(NAT).convert("L"); B = bands(); items = [r for r in rd(f"{HERE}/v9_items.tsv") if r["set"] == "setP" and not r["repeat_of"]]
    rows = ["kind\tcls\tref\tink_h\tink_w\tdark"]; agg = defaultdict(list)
    for r in items:
        x = int(r["x"]); b = band_of(B, r["line"], x); w = nat.crop((x - 30, b[1], x + 30, b[3])); px = w.load(); W, H = w.size
        thr = 110; ys = [y for y in range(H) if any(px[xx, y] < thr for xx in range(W))]; xs = [xx for xx in range(W) if any(px[xx, y] < thr for y in range(H))]
        dark = [px[xx, y] for xx in range(W) for y in range(H) if px[xx, y] < thr]
        h = (max(ys) - min(ys) + 1) if ys else 0; wd = (max(xs) - min(xs) + 1) if xs else 0; d = sum(dark) / len(dark) if dark else 255
        rows.append(f"{r['kind']}\t{r['cls']}\t{r['ref']}\t{h}\t{wd}\t{d:.0f}"); agg[r["kind"]].append((h, wd, d, len(dark)))
    for k, v in agg.items():
        n = len(v); rows.append(f"# {k}: n {n}, ink_h mean {sum(a[0] for a in v) / n:.1f}, ink_w mean {sum(a[1] for a in v) / n:.1f}, dark mean {sum(a[2] for a in v) / n:.0f}, ink px mean {sum(a[3] for a in v) / n:.0f}")
    open(f"{HERE}/v9_ink_measures.tsv", "w").write("\n".join(rows) + "\n"); print("\n".join(r for r in rows if r.startswith("#")))
if __name__ == "__main__":
    {"tiles": lambda: tiles(sys.argv[2]), "score": score, "measure": measure}[sys.argv[1]]()
