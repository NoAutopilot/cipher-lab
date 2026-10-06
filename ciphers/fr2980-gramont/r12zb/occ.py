#!/usr/bin/env python3
"""R12D-GRAZB: cut the blind-sort strips registered in PREREG-R12D-GRAZB.md (f.30 zb, fr.3040 barred z, plain z, decoys fh/n6),
shuffle and number them, write occ.tsv (private answer sheet) and sheet_<n>.jpg. Same strip method as n9graz/z_occ.py. Disk only.
python3 r12zb/occ.py"""
import sys, random, collections
from pathlib import Path
from PIL import Image, ImageDraw
if "--help" in sys.argv: print(__doc__); sys.exit()
H = Path(__file__).resolve().parent; T = H.parent
rng = random.Random(20261006)

def half_rows(f):
    d = {}
    for l in Path(f).read_text().splitlines()[1:]:
        r, c = l.split("\t"); d[r] = [t for t in c.split() if t not in ("/", ".")]
    return d
def recon(f): return [(l.split("\t")[0], l.split("\t")[1].split()) for l in Path(f).read_text().splitlines()[1:]]

def fr3040_occ(sign):
    out = []
    pa2 = half_rows(T / "n8gra2/passA.tsv")
    for ln, tt in recon(T / "n8gra2/recon.tsv"):
        if ln + "_s1" not in pa2: continue
        n1 = len(pa2[ln + "_s1"]); n2 = len(pa2[ln + "_s2"])
        for i, t in enumerate(tt):
            if t != sign: continue
            h, j, n = ("s1", i, n1) if i < n1 else ("s2", i - n1, n2)
            out.append((f"{ln} {i}", T / "images/fr3040_f18" / f"{ln}_{h}.jpg", (j + 0.5) / max(n, 1), n))
    pa3 = {}; pa3.update(half_rows(T / "n8gra3/passA_u1.tsv")); pa3.update(half_rows(T / "n8gra3/passA_u2.tsv"))
    for ln, tt in recon(T / "n8gra3/recon.tsv"):
        if ln + "_a" not in pa3: continue
        na = len(pa3[ln + "_a"]); nb = len(pa3[ln + "_b"])
        for i, t in enumerate(tt):
            if t != sign: continue
            h, j, n = ("a", i, na) if i < na else ("b", i - na, nb)
            out.append((f"{ln} {i}", T / "images/fr3040_f18" / f"{ln}_{h}.jpg", (j + 0.5) / max(n, 1), n))
    return out

pr = half_rows(T / "passR_f30.tsv")
def f30_occ(sign):
    out = []
    for l in (T / "ciphertext_f30.tsv").read_text().splitlines()[1:]:
        line, pos, s, cf = l.split("\t")
        if s != sign: continue
        pos = int(pos); na = len(pr[line + "a"]); nb = len(pr[line + "b"])
        h, j, n = ("a", pos, na) if pos < na else ("b", pos - na, nb)
        out.append((f"{line} {pos}", T / "images/crops_f30" / f"{line}{h}.jpg", (j + 0.5) / n, n))
    return out

def samp(lst, k): lst = sorted(lst, key=lambda o: o[0]); return rng.sample(lst, min(k, len(lst)))

occ = []  # (set, src, line_pos, img, xf, n)
for o in samp(f30_occ("zb"), 24): occ.append(("T1", "f30") + o)
# T2a / P from the N9-GRAZ sort
zo = {l.split("\t")[0]: l.split("\t") for l in (T / "n9graz/z_occ.tsv").read_text().splitlines()[1:]}
cl = {l.split("\t")[0]: l.split("\t")[1] for l in (T / "n9graz/sort_sonnet.tsv").read_text().splitlines()[1:]}
n9 = {}
for src in ("fr3040", "f30"):
    for o in fr3040_occ("z") if src == "fr3040" else f30_occ("z"): n9[(src, o[0])] = o
k2, k1f30, k1fr = [], [], []
for i, r in zo.items():
    o = n9[(r[1], r[2])]
    if cl[i] == "K2" and r[1] == "fr3040": k2.append(o)
    elif cl[i] == "K1" and r[1] == "fr3040": k1fr.append(o)
    elif cl[i] == "K1" and r[1] == "f30": k1f30.append(o)
for o in k2: occ.append(("T2a", "fr3040") + o)
for o in fr3040_occ("zb"):
    if o[1].parent.name == "fr3040_f18" and not o[0].startswith("f18r_"): occ.append(("T2b", "fr3040") + o)
for o in samp(k1f30, 10): occ.append(("P", "f30") + o)
for o in k1fr: occ.append(("P", "fr3040") + o)
for d in ("fh", "n6"):
    for o in samp(f30_occ(d), 6): occ.append((d, "f30") + o)
    for o in samp(fr3040_occ(d), 6): occ.append((d, "fr3040") + o)

out = H / "strips"; out.mkdir(exist_ok=True)
ids = list(range(1, len(occ) + 1)); rng.shuffle(ids)
rows = ["id\tset\tsrc\tline_pos\timage\tx_frac"]; strips = {}
for (st_, src, lp, img, xf, n), sid in zip(occ, ids):
    im = Image.open(img).convert("L"); w, h = im.size; sw = w / n; x = xf * w
    x0, x1 = max(0, int(x - 3 * sw)), min(w, int(x + 3 * sw))
    st = im.crop((x0, 0, x1, h)).convert("RGB"); d = ImageDraw.Draw(st); tx = x - x0
    d.line([(tx, 0), (tx, 14)], fill=(255, 0, 0), width=3); d.line([(tx, st.height - 14), (tx, st.height)], fill=(255, 0, 0), width=3)
    if st.height > 220: st = st.resize((int(st.width * 220 / st.height), 220))
    lab = Image.new("RGB", (st.width + 70, st.height), "white"); lab.paste(st, (70, 0))
    ImageDraw.Draw(lab).text((4, 4), f"#{sid}", fill=(0, 0, 0)); lab.save(out / f"{sid:03d}.jpg", quality=88)
    strips[sid] = lab; rows.append(f"{sid}\t{st_}\t{src}\t{lp}\t{img.relative_to(T)}\t{xf:.3f}")
(H / "occ.tsv").write_text("\n".join(rows) + "\n")
order = sorted(strips)
for k in range(0, len(order), 10):
    grp = [strips[i] for i in order[k:k + 10]]; W = max(g.width for g in grp); Ht = sum(g.height + 8 for g in grp)
    sh = Image.new("RGB", (W, Ht), (150, 150, 150)); y = 0
    for g in grp: sh.paste(g, (0, y)); y += g.height + 8
    sh.save(H / f"sheet_{k // 10 + 1}.jpg", quality=85)
print(len(occ), "strips;", dict(collections.Counter((o[0], o[1]) for o in occ)))
