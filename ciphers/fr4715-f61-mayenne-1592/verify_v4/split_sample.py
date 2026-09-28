#!/usr/bin/env python3
"""VERIFY-F61-V4 step 3 (28 Sept 2026): blind re-sort of the tiles behind v4's relabel moves. Design fixed here before any
call. Five calls (one Opus vision subagent each, no letters, no class names, no family answers shown):
  sbs   10 tiles the family reader put in SBS (5 f.101r, 5 f.188r) + 5 decoys (PHI/INF), scored on the 10
  phi   10 family-PHI tiles (5+5) + 5 decoys (SBS/INF)
  inf   10 family-INF tiles (5+5) + 5 decoys (PHI/SBS)
  4tri  5 family-4TRI + 5 family-4HOOK (both leaves) + 2+2 more, all 14 scored
  f61   f.61r's own loop signs from H26's blind call (scripts/read_call_QO.tsv): all 7 G2 (-> SBS under --sbs) + 5 G1 (PHI),
        cut from images/f61sheetB_*.jpg -- the relabel that carries v4's +5 on the known spans
Tiles are re-cut from the committed family/recode query sheets (and anchor sheets for the reference forms), shuffled
(seed 4), labelled 'tile N'; reference forms carry neutral letters X/Y/Z mapped at random per call. The family's answers
(recode/*_read.tsv) and the key never reach the reader. Answer key: verify_v4/tiles/<call>_key.tsv.
  python3 verify_v4/split_sample.py build | score
"""
import csv, os, random, sys
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); TGT = os.path.dirname(HERE); REC = f"{TGT}/family/recode"; OUT = f"{HERE}/tiles"
ANC = {"f101r_loops": [("PHI", 12), ("SBS", 30), ("INF", 13)], "f188r_loops": [("PHI", 8), ("SBS", 14), ("INF", 13)],
       "f101r_4tri": [("4TRI", 6), ("4HOOK", 4)], "f188r_4tri": [("4TRI", 8), ("4HOOK", 7)]}
FORMS = {"f101r_loops": ("PHI", "SBS", "INF"), "f188r_loops": ("PHI", "SBS", "INF"), "f101r_4tri": ("4TRI", "4HOOK"), "f188r_4tri": ("4TRI", "4HOOK")}
def cell(stem, i):
    sh = Image.open(f"{REC}/{stem}{i // 10 + 1}.jpg").convert("RGB"); k = i % 10; X, Y = (k % 5) * 340, (k // 5) * 329
    return sh.crop((X, Y + 34, X + 330, Y + 34 + 285))
def rows(p): return [r for r in csv.DictReader((l for l in open(p) if not l.startswith("#")), delimiter="\t")]
def family(call):
    """query tiles with the family reader's form -> class"""
    key = {r["tile"]: r for r in rows(f"{REC}/{call}_key.tsv")}; out = []
    for r in rows(f"{REC}/{call}_read.tsv"):
        if key[r["tile"]]["kind"] != "query" or r["form"] not in ("1", "2", "3"): continue
        out.append((call, int(r["tile"]), FORMS[call][int(r["form"]) - 1]))
    return out
def anchors(calls, per, rng):
    out = []
    for call in calls:
        i0 = 0
        for cls, n in ANC[call]:
            idx = list(range(i0, i0 + n)); rng.shuffle(idx); out += [(cls, cell(f"{REC}/{call}_anchors".replace(REC + "/", ""), i)) for i in idx[:per]]; i0 += n
    return out
def f61_tiles():
    g = [r for r in rows(f"{TGT}/scripts/read_call_QO.tsv") if r["sheet"].startswith("f61")]
    return [r for r in g if r["group"] == "G2"], [r for r in g if r["group"] == "G1"]
def cut61(r):
    im = Image.open(f"{TGT}/images/{r['sheet']}.jpg").convert("RGB"); L = im.convert("L"); W, H = im.size
    bars = [y for y in range(H) if sum(1 for x in range(0, W, 10) if L.getpixel((x, y)) < 40) > 0.8 * W / 10]
    starts = [0] + [y + 1 for i, y in enumerate(bars) if i + 1 == len(bars) or bars[i + 1] - y > 1]
    ends = [y for i, y in enumerate(bars) if i == 0 or bars[i - 1] != y - 1] + [H]
    s = int(r["segment"]); top, bot = starts[s - 1] + 12, ends[s - 1] - 1; x = int(float(r["x_px"]))
    t = im.crop((max(0, x - 170), top, min(W, x + 170), bot)).resize((330, 285)); d = ImageDraw.Draw(t)
    cx = (x - max(0, x - 170)) * 330 // (min(W, x + 170) - max(0, x - 170)); d.line([cx, 0, cx, 10], fill=(220, 0, 0), width=3); d.line([cx, 275, cx, 285], fill=(220, 0, 0), width=3)
    return t
def sheet(tiles, path, lab):
    W, H = 340, 329; n = (len(tiles) + 4) // 5; sh = Image.new("RGB", (5 * W, n * H), "white"); d = ImageDraw.Draw(sh)
    for k, (l, t) in enumerate(tiles):
        X, Y = (k % 5) * W, (k // 5) * H; sh.paste(t, (X, Y + 34)); d.text((X + 6, Y + 8), lab(l), fill=(0, 0, 200))
    sh.save(path, quality=88)
def build():
    os.makedirs(OUT, exist_ok=True); rng = random.Random(4); summary = []
    loops = family("f101r_loops") + family("f188r_loops"); tri = family("f101r_4tri") + family("f188r_4tri")
    def pick(pool, cls, leafn):
        out = []
        for lf, n in leafn:
            c = [t for t in pool if t[2] == cls and t[0].startswith(lf)]; rng.shuffle(c); out += c[:n]
        return out
    plans = {
        "sbs": (pick(loops, "SBS", [("f101r", 5), ("f188r", 5)]), pick(loops, "PHI", [("f101r", 1), ("f188r", 2)]) + pick(loops, "INF", [("f101r", 1), ("f188r", 1)]), ("f101r_loops", "f188r_loops")),
        "phi": (pick(loops, "PHI", [("f101r", 5), ("f188r", 5)]), pick(loops, "SBS", [("f101r", 2), ("f188r", 1)]) + pick(loops, "INF", [("f101r", 1), ("f188r", 1)]), ("f101r_loops", "f188r_loops")),
        "inf": (pick(loops, "INF", [("f101r", 5), ("f188r", 5)]), pick(loops, "PHI", [("f101r", 1), ("f188r", 1)]) + pick(loops, "SBS", [("f101r", 2), ("f188r", 1)]), ("f101r_loops", "f188r_loops")),
        "4tri": (pick(tri, "4TRI", [("f101r", 4), ("f188r", 3)]) + pick(tri, "4HOOK", [("f101r", 4), ("f188r", 3)]), [], ("f101r_4tri", "f188r_4tri")),
    }
    for call, (tgt, dec, acalls) in plans.items():
        q = [(c, t, cls, "target") for c, t, cls in tgt] + [(c, t, cls, "decoy") for c, t, cls in dec]
        # remove tiles picked twice (a decoy of one call may be a target of another: fine; within a call no duplicates)
        rng.shuffle(q); forms = sorted({cls for _, _, cls in (loops if "loops" in acalls[0] else tri)})
        letters = ["X", "Y", "Z"][:len(forms)]; rng.shuffle(letters); lab = dict(zip(forms, letters))
        anc = anchors(acalls, 3 if len(forms) == 3 else 4, rng)
        sheet([(lab[c], t) for c, t in sorted(anc, key=lambda a: lab[a[0]])], f"{OUT}/{call}_ref.jpg", lambda l: f"form {l}")
        sheet([(i + 1, cell(f"{c}_query", t - 1)) for i, (c, t, _, _) in enumerate(q)], f"{OUT}/{call}_query.jpg", lambda l: f"tile {l}")
        with open(f"{OUT}/{call}_key.tsv", "w") as f:
            f.write("# answer key, never shown to the reader. forms: " + ", ".join(f"{v} = {k}" for k, v in sorted(lab.items())) + "\ntile\tsrc_call\tsrc_tile\tfamily_class\trole\n")
            for i, (c, t, cls, role) in enumerate(q, 1): f.write(f"{i}\t{c}\t{t}\t{cls}\t{role}\n")
        summary.append(f"{call}: {len(q)} tiles, forms {lab}")
    g2, g1 = f61_tiles(); rng.shuffle(g1); q = [(r, "SBS") for r in g2] + [(r, "PHI") for r in g1[:5]]; rng.shuffle(q)
    forms = ["INF", "PHI", "SBS"]; letters = ["X", "Y", "Z"]; rng.shuffle(letters); lab = dict(zip(forms, letters))
    anc = anchors(("f101r_loops", "f188r_loops"), 3, rng)
    sheet([(lab[c], t) for c, t in sorted(anc, key=lambda a: lab[a[0]])], f"{OUT}/f61_ref.jpg", lambda l: f"form {l}")
    sheet([(i + 1, cut61(r)) for i, (r, _) in enumerate(q)], f"{OUT}/f61_query.jpg", lambda l: f"tile {l}")
    with open(f"{OUT}/f61_key.tsv", "w") as f:
        f.write("# answer key, never shown to the reader. forms: " + ", ".join(f"{v} = {k}" for k, v in sorted(lab.items())) + "\ntile\tsheet\tsegment\tx_px\tH26_group\tv4_class\n")
        for i, (r, cls) in enumerate(q, 1): f.write(f"{i}\t{r['sheet']}\t{r['segment']}\t{r['x_px']}\t{r['group']}\t{cls}\n")
    summary.append(f"f61: {len(q)} tiles, forms {lab}")
    open(f"{OUT}/build.txt", "w").write("\n".join(summary) + "\n"); print("\n".join(summary))
def score():
    out = []
    for call in ("sbs", "phi", "inf", "4tri", "f61"):
        p = f"{OUT}/{call}_read.tsv"
        if not os.path.exists(p): out.append(f"{call}: no read"); continue
        hdr = open(f"{OUT}/{call}_key.tsv").readline(); lab = {kv.split(" = ")[0].strip(): kv.split(" = ")[1].strip() for kv in hdr.split("forms: ")[1].strip().split(", ")}
        key = {r["tile"]: r for r in rows(f"{OUT}/{call}_key.tsv")}; rd = {r["tile"]: r["form"].strip() for r in rows(p)}
        ok = n = 0; dok = dn = 0; det = []
        for t, r in key.items():
            want = r.get("family_class") or r.get("v4_class"); got = lab.get(rd.get(t, "none"), "none"); role = r.get("role", "target")
            if call == "f61" or role == "target": n += 1; ok += got == want
            else: dn += 1; dok += got == want
            if got != want: det.append(f"t{t} {want}->{got}")
        out.append(f"{call}: targets {ok}/{n} = {ok/n:.2f} agree with the v4 relabel" + (f"; decoys {dok}/{dn}" if dn else "") + ("; disagreements: " + ", ".join(det) if det else ""))
    txt = "\n".join(out) + "\n"; open(f"{HERE}/split_result.txt", "w").write(txt); print(txt, end="")
{"build": build, "score": score}[sys.argv[1]]()
