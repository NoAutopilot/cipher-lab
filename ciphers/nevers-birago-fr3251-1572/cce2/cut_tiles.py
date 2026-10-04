#!/usr/bin/env python3
"""BIR-CCE2 step 1 (4 Oct 2026): value-blind material for the Fable glyph read, one view per query sign.
Reference A (cce2/ref_ceppo.png): the 54 non-blank cells of Tomokiyo's Ceppo-Nevers table (nevers_add1.png), cut WITHOUT the
header band (same geometry as cce/make_montage.py), labelled K01..K54 in a seeded random order; the K -> (column,row) map is
written to cce2/ref_ceppo_perm.tsv and is NOT read by the reader until cce2/glyph_map.tsv is pushed.
Reference B (cce2/ref_1572.png): column strips of the 1572 table's letter grid (NeversBirago.png, y 39-236, between the two
white-on-black header bands found by row profile), labelled N01.. in seeded random order (cce2/ref_1572_perm.tsv, same rule);
the word-code grid below the second header is NOT cut (its rows may carry printed labels).
Queries: (a) sorter tiles of the X_NEW*/T42/T50/T95 piles (sorter/signs.tsv + owner-sort settled labels); (b) one tile per
occurrence of every off-sheet shape class of harvest/offsheet/pool_*.tsv (nos.71/86/90 and no.87), cut from the native
line crops' source images by the sorter's column-ink-profile blob fit (approximate: a tile can be one position off, so each
tile carries a 5-blob context strip with the target underlined); (c) X_CE, the 7 no.87 tiles of exceptions_f178v.tsv;
(d) Ceppo-side off-key signs (X_THETA2, X_POUND, X_NEW) of fr.3251 f.21v/f.35/f.87, lines by row profile, same blob fit.
No value, no header, no plaintext anywhere in cce2/views/.   python3 cce2/cut_tiles.py"""
import csv, json, random, re
from collections import defaultdict
from pathlib import Path
from PIL import Image, ImageDraw, ImageOps
import numpy as np
T = Path(__file__).resolve().parents[1]; O = Path(__file__).resolve().parent; R = T.parents[1]; HV = T / "harvest"
V = O / "views"; V.mkdir(exist_ok=True)
rng = random.Random(20261004)
# ---------- reference A: Ceppo cells (make_montage.py geometry) ----------
img = Image.open(R / "sources/cryptiana/web/img/nevers_add1.png").convert("L")
cols = "abcdefghilmnopqrstuxyz"; x0, cw = 1, 33.95; rows = [(37, 73), (73, 109), (109, 145), (145, 181), (181, 217)]
cells = []
for ci, c in enumerate(cols):
    for ri, (y0, y1) in enumerate(rows):
        box = (int(x0 + ci * cw) + 2, y0 + 2, int(x0 + (ci + 1) * cw) - 2, y1 - 2)
        t = img.crop(box)
        if sum(1 for p in t.getdata() if p < 120) < 6: continue
        if ri == 4 and 6 <= ci <= 13: continue
        cells.append((c, ri + 1, t))
extra = [("et", 1, (775, 38, 800, 66))] + [("null", i + 1, (774 + 23 * i, 148, 798 + 23 * i, 184)) for i in range(6)]
for v, r, b in extra: cells.append((v, r, img.crop(b)))
assert len(cells) == 54, len(cells)
perm = list(range(54)); rng.shuffle(perm)
with open(O / "ref_ceppo_perm.tsv", "w") as f:
    f.write("klabel\tcolumn\trow\tcce_cell\n")
    for k, i in enumerate(perm):
        f.write(f"K{k+1:02d}\t{cells[i][0]}\t{cells[i][1]}\tC{i+1:02d}\n")
def montage(items, s=64, W=9, pad=28):
    n = len(items); hgt = (n + W - 1) // W
    M = Image.new("L", (W * (s + pad), hgt * (s + 18)), 255); d = ImageDraw.Draw(M)
    for i, (lab, t) in enumerate(items):
        t = ImageOps.contain(t, (s, s)); x, y = (i % W) * (s + pad), (i // W) * (s + 18)
        M.paste(t, (x + (s - t.width) // 2, y)); d.text((x + 2, y + s + 2), lab, fill=0)
    return M
refA = montage([(f"K{k+1:02d}", cells[i][2]) for k, i in enumerate(perm)]); refA.save(O / "ref_ceppo.png")
# ---------- reference B: 1572 letter grid column strips ----------
im2 = Image.open(R / "sources/cryptiana/web/img/NeversBirago.png").convert("L"); a = np.array(im2); h, w = a.shape
dark = a < 128; rows_ = dark.sum(1); bands = [y for y in range(h) if rows_[y] > 0.6 * w]
hdr1 = max(y for y in bands if y < 100); hdr2 = min(y for y in bands if y > 100)
grid = a[hdr1 + 1:hdr2 - 1]; gy0 = hdr1 + 1
colink = (grid < 128).sum(0); gaps = colink <= 0
segs, s = [], None
for x in range(w):
    if not gaps[x]: s = x if s is None else s
    elif s is not None: segs.append((s, x)); s = None
if s is not None: segs.append((s, w))
segs = [g for g in segs if g[1] - g[0] >= 8]
med = sorted(g[1] - g[0] for g in segs)[len(segs) // 2]; out = []
for g in segs:
    if g[1] - g[0] > 1.7 * med:
        m_ = min(range(g[0] + 10, g[1] - 10), key=lambda x: colink[x]); out += [(g[0], m_), (m_ + 1, g[1])]
    else: out.append(g)
segs = out
strips = [im2.crop((g[0] - 2, gy0, g[1] + 2, hdr2 - 1)) for g in segs]
permB = list(range(len(strips))); rng.shuffle(permB)
with open(O / "ref_1572_perm.tsv", "w") as f:
    f.write("nlabel\tstrip_index_left_to_right\tx0\tx1\n")
    for k, i in enumerate(permB): f.write(f"N{k+1:02d}\t{i+1}\t{segs[i][0]}\t{segs[i][1]}\n")
def montage_tall(items, sh=200, W=12):
    n = len(items); hgt = (n + W - 1) // W; cw_ = 70
    M = Image.new("L", (W * cw_, hgt * (sh + 18)), 255); d = ImageDraw.Draw(M)
    for i, (lab, t) in enumerate(items):
        t = ImageOps.contain(t, (cw_ - 6, sh)); x, y = (i % W) * cw_, (i // W) * (sh + 18)
        M.paste(t, (x + 3, y)); d.text((x + 2, y + sh + 2), lab, fill=0)
    return M
refB = montage_tall([(f"N{k+1:02d}", strips[i]) for k, i in enumerate(permB)]); refB.save(O / "ref_1572.png")
print("ref A", len(cells), "cells; ref B", len(strips), "strips, headers at", hdr1, hdr2)
# ---------- blob tools (sorter/build_inputs.py) ----------
def blobs(im, gap=4, minw=8, thr=120):
    a = np.array(im.convert('L')); h = a.shape[0]
    mid = a[int(h * .15):int(h * .85)] < thr
    col = (mid.sum(0) > 1) & (mid.mean(0) < .6)
    segs, s, last = [], None, -99
    for x, v in enumerate(col):
        if v: s = x if s is None else s; last = x
        elif s is not None and x - last > gap: segs.append([s, last]); s = None
    if s is not None: segs.append([s, last])
    return [g for g in segs if g[1] - g[0] >= minw]
def fit(segs, n):
    segs = [list(g) for g in segs]
    if not segs: return segs
    while len(segs) > n:
        i = min(range(len(segs)), key=lambda k: segs[k][1] - segs[k][0])
        if i == 0: j = 1
        elif i == len(segs) - 1: j = i - 1
        else: j = i - 1 if segs[i][0] - segs[i - 1][1] < segs[i + 1][0] - segs[i][1] else i + 1
        a_, b_ = sorted((i, j)); segs[a_] = [segs[a_][0], segs[b_][1]]; del segs[b_]
    while len(segs) < n:
        i = max(range(len(segs)), key=lambda k: segs[k][1] - segs[k][0]); a_, b_ = segs[i]; m = (a_ + b_) // 2
        segs[i:i + 1] = [[a_, m], [m + 1, b_]]
    return segs
def tile_ctx(im, bx, pos):
    """tile of blob pos (0-based) with margin + 5-blob context strip with the target underlined"""
    x0, x1 = bx[pos]; hh = im.height
    t = im.crop((max(0, x0 - 6), 0, min(im.width, x1 + 6), hh))
    lo = bx[max(0, pos - 2)][0]; hi = bx[min(len(bx) - 1, pos + 2)][1]
    c = im.crop((max(0, lo - 6), 0, min(im.width, hi + 6), hh)).convert("RGB"); d = ImageDraw.Draw(c)
    d.line([(x0 - lo + 6, hh - 3), (x1 - lo + 6, hh - 3)], fill=(255, 0, 0), width=4)
    return t, c
# ---------- line strips from harvest manifests ----------
def strip_1572(leaf, band):
    m = json.load(open(HV / leaf / "manifest.json"))["iiif_lines"]; es = [e for e in m if e["band"] == band]
    if not es: return None
    sf = es[0]["source_file"]; url = es[0].get("source_url") or ""
    if "/full/" in url: ox, oy = (int(v) for v in url.split("/full/")[0].split("/")[-1].split(",")[:2])
    else: ox = oy = 0
    x0 = min(e["box"][0] for e in es); y0 = min(e["box"][1] for e in es); x1 = max(e["box"][2] for e in es); y1 = max(e["box"][3] for e in es)
    if (HV / leaf / sf).exists():
        src = Image.open(HV / leaf / sf); return src.crop((x0 - ox, y0 - oy, x1 - ox, y1 - oy))
    # source gitignored (f184v, f185r, f174r: REGEN.sh): re-assemble the line from its segment crops by their boxes
    canvas = Image.new("L", (x1 - x0, y1 - y0), 255)
    for e in sorted(es, key=lambda e: e["segment"]):
        c = Image.open(HV / leaf / e["crop"]).convert("L"); canvas.paste(c, (e["box"][0] - x0, e["box"][1] - y0))
    return canvas
def leaf_band(letter, psg):
    if letter == "no71": return ("f139v", int(psg[1:]))
    if letter == "no87":
        n = int(re.sub(r"\D", "", psg)); return ({"L": "f178v", "R": "f178r", "V": "f179r"}[psg[0]], n)
    m = re.match(r"(f\d+[rv])_([LRV])(\d+)", psg)
    if not m: return None
    leaf, n = m.group(1), int(m.group(3))
    if leaf == "f174v": return ("f174v", n) if n <= 11 else ("f174vB", n - 11)
    if leaf == "f185r": return ("f185r", n) if n <= 8 else None
    if leaf == "f185v": return None
    return (leaf, n)
pools = {}
for k in ("no71", "no86", "no90", "no87"):
    for r in csv.DictReader(open(HV / f"offsheet/pool_{k}.tsv"), delimiter="\t"):
        pools.setdefault((k, r["passage"]), []).append(r["sign_id"])
occ = defaultdict(list)  # class -> [(letter, passage, pos)]
for (k, p), seq in pools.items():
    for i, sid in enumerate(seq):
        if sid.startswith("X_") and sid != "X_NEW": occ[sid].append((k, p, i + 1, len(seq)))
occ["X_CE"] = [("no87", f"L{l:02d}", p, len(pools[("no87", f"L{l:02d}")])) for l, p in [(1, 23), (3, 4), (4, 4), (5, 25), (7, 29), (8, 10), (10, 5)]]
queries = []  # (qid, group, source, tile, ctx)
strip_cache = {}
def get_strip(leaf, band):
    if (leaf, band) not in strip_cache:
        try: strip_cache[(leaf, band)] = strip_1572(leaf, band)
        except Exception as e: strip_cache[(leaf, band)] = None
    return strip_cache[(leaf, band)]
qrows = []
for cls in sorted(occ):
    picks, seen = [], defaultdict(int)
    for letter, psg, pos, n in occ[cls]:  # spread over letters
        if seen[letter] >= 2 and len(set(x[0] for x in occ[cls])) > 1: continue
        lb = leaf_band(letter, psg)
        if not lb: continue
        st = get_strip(*lb)
        if st is None: continue
        bx = fit(blobs(st), n)
        if len(bx) < n: continue
        picks.append((letter, psg, pos, st, bx)); seen[letter] += 1
        if len(picks) >= 5: break
    for letter, psg, pos, st, bx in picks:
        t, c = tile_ctx(st, bx, pos - 1); qid = f"{cls}#{len([q for q in queries if q[1]==cls])+1}"
        queries.append((qid, cls, f"{letter} {psg} pos{pos}", t, c)); qrows.append((qid, cls, letter, psg, pos, "blobfit"))
# sorter tiles
geo = {r["sid"]: r for r in csv.DictReader(open(T / "sorter/signs.tsv"), delimiter="\t")}
pile = defaultdict(list)
for r in csv.DictReader(open(T / "sorter/owner-sort-2026-10-04/settled_labels.tsv"), delimiter="\t"):
    if r["sid"] in geo and (r["new_sign"].startswith("X_NEW") or r["new_sign"].split("-")[0] in ("T42", "T50", "T95")):
        pile[r["new_sign"]].append(r["sid"])
for p in sorted(pile):
    sids = pile[p]; sids = sorted(sids, key=lambda s: s.split("_")[0])  # spread pages
    chosen, pc = [], defaultdict(int)
    for s in sids:
        pg = s.split("_")[0]
        if pc[pg] >= 2 and len(sids) > 4: continue
        chosen.append(s); pc[pg] += 1
        if len(chosen) >= 5: break
    for s in chosen:
        g = geo[s]; pg = Image.open(T / "sorter/pages" / f"{g['page']}.jpg").convert("L")
        x, y, w_, h_ = (int(g[k]) for k in "xywh")
        t = pg.crop((x - 4, max(0, y - 4), x + w_ + 4, y + h_ + 4)); c = pg.crop((max(0, x - 2 * w_ - 10), 0, x + 3 * w_ + 10, pg.height)).convert("RGB")
        d = ImageDraw.Draw(c); d.line([(x - max(0, x - 2 * w_ - 10), c.height - 3), (x + w_ - max(0, x - 2 * w_ - 10), c.height - 3)], fill=(255, 0, 0), width=4)
        qid = f"{p}#{len([q for q in queries if q[1]==p])+1}"; queries.append((qid, p, f"sorter {s}", t, c)); qrows.append((qid, p, "sorter", g["page"], s, "sorter box"))
# ---------- Ceppo-side off-key tiles ----------
CE = T.parent / "ceppo-nevers-fr3251-1570s/harvest"
ce_lines = defaultdict(list)
for fol, fn in (("f21v", "f21v/c23_cipher.jpg"), ("f35", "f35/c36_cipher.jpg"), ("f87", "f87/c88_cipher.jpg")):
    seq = defaultdict(list)
    for r in csv.DictReader(open(CE / f"ciphertext_{fol}.tsv"), delimiter="\t"):
        ln = r["line"].split("_L")[1].split(".")[0]; seq[int(ln)].append(r["sign"])
    im = Image.open(CE / fn).convert("L"); a = np.array(im) < 110; prof = a.sum(1).astype(float)
    nl = max(seq); pitch = im.height / nl; win = max(5, int(pitch / 3))
    sm = np.convolve(prof, np.ones(win) / win, mode="same")
    peaks = [y for y in range(1, len(sm) - 1) if sm[y] >= sm[y - 1] and sm[y] > sm[y + 1]]
    peaks.sort(key=lambda y: -sm[y]); keep = []
    for y in peaks:
        if all(abs(y - k) > 0.6 * pitch for k in keep): keep.append(y)
        if len(keep) == nl: break
    keep.sort(); bands_ = [(int(max(0, y - 0.45 * pitch)), int(min(im.height, y + 0.45 * pitch))) for y in keep]
    print(fol, "line peaks", keep, "pitch", round(pitch), "lines in passC", nl)
    if len(bands_) != nl: continue
    for li, (y0, y1) in enumerate(bands_, 1):
        st = im.crop((0, max(0, y0 - 8), im.width, min(im.height, y1 + 8))); n = len(seq[li]); bx = fit(blobs(st, gap=6, minw=10), n)
        if len(bx) < n: continue
        for i, sid in enumerate(seq[li]):
            if sid.startswith("X_"): ce_lines[sid].append((fol, li, i + 1, st, bx))
for cls in sorted(ce_lines):
    picks, pc = [], defaultdict(int)
    for fol, li, pos, st, bx in ce_lines[cls]:
        if pc[fol] >= 2: continue
        picks.append((fol, li, pos, st, bx)); pc[fol] += 1
        if len(picks) >= 5: break
    for fol, li, pos, st, bx in picks:
        t, c = tile_ctx(st, bx, pos - 1); qid = f"CEPPO-{cls}#{len([q for q in queries if q[1]=='CEPPO-'+cls])+1}"
        queries.append((qid, "CEPPO-" + cls, f"{fol} L{li:02d} pos{pos}", t, c)); qrows.append((qid, "CEPPO-" + cls, fol, f"L{li:02d}", pos, "blobfit"))
# ---------- views: one composite per query group ----------
groups = defaultdict(list)
for q in queries: groups[q[1]].append(q)
with open(O / "query_tiles.tsv", "w") as f:
    f.write("qid\tgroup\tletter\tpassage\tpos_or_sid\tmethod\n")
    for r in qrows: f.write("\t".join(str(x) for x in r) + "\n")
for g, qs in groups.items():
    ref = refB if g.startswith("CEPPO-") else refA
    TH = 110; parts = []
    for qid, _, src, t, c in qs:
        t2 = ImageOps.contain(t.convert("RGB"), (150, TH)); c2 = ImageOps.contain(c, (420, TH))
        P = Image.new("RGB", (t2.width + c2.width + 30, TH + 16), "white"); P.paste(t2, (0, 0)); P.paste(c2, (t2.width + 20, 0))
        ImageDraw.Draw(P).text((2, TH + 2), f"{qid}  [{src}]", fill=(0, 0, 0)); parts.append(P)
    Wd = max(max(p.width for p in parts), ref.width); Ht = sum(p.height + 6 for p in parts) + ref.height + 30
    M = Image.new("RGB", (Wd, Ht), "white"); y = 0
    for p in parts: M.paste(p, (0, y)); y += p.height + 6
    ImageDraw.Draw(M).text((2, y + 4), "reference cells (shuffled labels):", fill=(0, 0, 0)); y += 24
    M.paste(ref.convert("RGB"), (0, y)); M.save(V / f"{g}.png")
print(len(queries), "query tiles in", len(groups), "groups:", ", ".join(f"{g}({len(v)})" for g, v in sorted(groups.items())))
