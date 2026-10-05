#!/usr/bin/env python3
"""N9-GRAZ: list every `z` occurrence with its strip location and (fr.3040 no.6 only) the Le Grand print letter it aligns to under
N8-GRA2's registered aligner; cut one unlabelled strip per occurrence (+-3 sign widths, target column ticked, proportional position as in
split_shapes_crops.py) plus the key-table cells, shuffle and number them. Writes z_occ.tsv (private answer sheet: id -> source,
aligned letter), strips/<id>.jpg and sheet_<n>.jpg. Disk only.  python3 z_occ.py"""
import sys, random, collections
from pathlib import Path
from PIL import Image, ImageDraw
if "--help" in sys.argv: print(__doc__); sys.exit()
H = Path(__file__).resolve().parent; T = H.parent
sys.path.insert(0, str(T / "n8gra2")); sys.path.insert(0, str(T / "n8gra3"))
import score as S
import score3 as S3

key = S.load_key()
occ = []  # (src, line, image, x_frac, n_in_half, aligned)

def half_rows(f):
    d = {}
    for l in Path(f).read_text().splitlines()[1:]:
        r, c = l.split("\t"); d[r] = [t for t in c.split() if t not in ("/", ".")]
    return d

def aligned_tokens(rows, seg):
    """rows: list of (line, tokens); returns per (line, idx) aligned print string."""
    toks, own = [], []
    for ln, tt in rows:
        for i, t in enumerate(tt): toks.append(t); own.append((ln, i))
    dec, idx = [], []
    for k, t in enumerate(toks):
        d = S.decode([t], key)
        if d: dec.append(d[0]); idx.append(own[k])
    _, _, al = S.align_agree(dec, seg)
    return {idx[k]: (dec[k][1], al[k]) for k in range(len(dec))}

def recon(f): return [(l.split("\t")[0], l.split("\t")[1].split()) for l in Path(f).read_text().splitlines()[1:]]

# fr.3040 f.18r (N8-GRA2): halves s1/s2 from passA lengths
g2 = [(r, t) for r, t in recon(T / "n8gra2/recon.tsv") if r in S.ROWS]
pa2 = half_rows(T / "n8gra2/passA.tsv")
al2 = aligned_tokens(g2, S.load_print())
for ln, tt in g2:
    n1 = len(pa2[ln + "_s1"]); n2 = len(pa2[ln + "_s2"])
    for i, t in enumerate(tt):
        if t != "z": continue
        h, j, n = ("s1", i, n1) if i < n1 else ("s2", i - n1, n2)
        img = T / "images/fr3040_f18" / f"{ln}_{h}.jpg"
        occ.append(("fr3040", f"{ln} {i}", img, (j + 0.5) / max(n, 1), n, al2.get((ln, i), (None, "?"))[1]))
# fr.3040 f.18v/f.19r (N8-GRA3): halves _a/_b
pa3 = {}; pa3.update(half_rows(T / "n8gra3/passA_u1.tsv")); pa3.update(half_rows(T / "n8gra3/passA_u2.tsv"))
bl = collections.OrderedDict()
for r, tt in recon(T / "n8gra3/recon.tsv"): bl.setdefault(S3.BLOCK[r.split("_")[0]], []).append((r, tt))
for s, rows in bl.items():
    al3 = aligned_tokens(rows, S3.SEGS[s])
    for ln, tt in rows:
        na = len(pa3[ln + "_a"]); nb = len(pa3[ln + "_b"])
        for i, t in enumerate(tt):
            if t != "z": continue
            h, j, n = ("a", i, na) if i < na else ("b", i - na, nb)
            img = T / "images/fr3040_f18" / f"{ln}_{h}.jpg"
            occ.append(("fr3040", f"{ln} {i}", img, (j + 0.5) / max(n, 1), n, al3.get((ln, i), (None, "?"))[1]))
# f.30
pr = half_rows(T / "passR_f30.tsv")
for l in (T / "ciphertext_f30.tsv").read_text().splitlines()[1:]:
    line, pos, s, cf = l.split("\t")
    if s != "z": continue
    pos = int(pos); na = len(pr[line + "a"]); nb = len(pr[line + "b"])
    h, j, n = ("a", pos, na) if pos < na else ("b", pos - na, nb)
    occ.append(("f30", f"{line} {pos}", T / "images/crops_f30" / f"{line}{h}.jpg", (j + 0.5) / n, n, ""))

out = H / "strips"; out.mkdir(exist_ok=True)
rng = random.Random(20261005); ids = list(range(1, len(occ) + 1)); rng.shuffle(ids)
rows = ["id\tsrc\tline_pos\timage\tx_frac\taligned"]
strips = {}
for (src, lp, img, xf, n, alg), sid in zip(occ, ids):
    im = Image.open(img).convert("L"); w, h = im.size; sw = w / n; x = xf * w
    x0, x1 = max(0, int(x - 3 * sw)), min(w, int(x + 3 * sw))
    st = im.crop((x0, 0, x1, h)).convert("RGB"); d = ImageDraw.Draw(st); tx = x - x0
    d.line([(tx, 0), (tx, 14)], fill=(255, 0, 0), width=3); d.line([(tx, st.height - 14), (tx, st.height)], fill=(255, 0, 0), width=3)
    if st.height > 220: st = st.resize((int(st.width * 220 / st.height), 220))
    lab = Image.new("RGB", (st.width + 70, st.height), "white"); lab.paste(st, (70, 0))
    ImageDraw.Draw(lab).text((4, 4), f"#{sid}", fill=(0, 0, 0)); lab.save(out / f"{sid:03d}.jpg", quality=88)
    strips[sid] = lab; rows.append(f"{sid}\t{src}\t{lp}\t{img.relative_to(T)}\t{xf:.3f}\t{alg}")
(H / "z_occ.tsv").write_text("\n".join(rows) + "\n")
order = sorted(strips)
for k in range(0, len(order), 10):
    grp = [strips[i] for i in order[k:k + 10]]; W = max(g.width for g in grp); Ht = sum(g.height + 8 for g in grp)
    sh = Image.new("RGB", (W, Ht), (150, 150, 150)); y = 0
    for g in grp: sh.paste(g, (0, y)); y += g.height + 8
    sh.save(H / f"sheet_{k // 10 + 1}.jpg", quality=85)
c = collections.Counter((o[0], o[5]) for o in occ)
print(len(occ), "strips;", dict(c))
