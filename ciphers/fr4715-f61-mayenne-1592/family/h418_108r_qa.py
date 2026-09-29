#!/usr/bin/env python3
"""H418 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026), written before the call: H411's forced-choice class check on fr.3983 f.108r
(f.61's hand; images/f108sheetB_<row>.jpg bands, pass A positions scripts/pass108A_classes.tsv, H202's tile format with the marker UNDER the sign).
 references -- per class with overlay-confirmed tokens (pass-A code whose key v8 cell holds the overlay letter at an aligned pair, h416's alignment
   on pass A's unrelabelled codes): the first such token (seed-free, file order) for EBR, 4STEM, VBAR_A, ZHOOK, PHI, INF, C43, 4PI, 4TRI, BETA = R1-R10.
 known -- up to 2 further confirmed tokens per class (19).
 targets -- H416's transcription questions: L02/20 (4PI, overlay p), L02/36 (INF, overlay e), L03/3, L03/27, L03/37 (OTHER; overlay l, l, m) and L03/8
   (OTHER, the 'qui' word sign; expected 'none'), each at three widths (W1 300, W2 240, W3 360 px).  shuffled (seed 418), I01...
 score -- GATE >= 17/19 known. Per target, an answer at >= 2 of 3 windows is recorded (a class, none, P), else unclear. Descriptive; any class
   answer is a transcription proposal for f.108r (separate file only on a later row). No key change.
 python3 h418_108r_qa.py tiles SCRATCH | score [--check]"""
import csv, os, random, sys
from collections import defaultdict, Counter
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.abspath(f"{HERE}/.."); P = f"{HERE}/passes"; IM = f"{T}/images"; CHECK = "--check" in sys.argv
sys.argv = sys.argv[:1] + [a for a in sys.argv[1:] if a != "--check"]; sys.path.insert(0, HERE); sys.path.insert(0, f"{T}/scripts")
CLS = ["EBR", "4STEM", "VBAR_A", "ZHOOK", "PHI", "INF", "C43", "4PI", "4TRI", "BETA"]
TARGETS = [("L02", 20), ("L02", 36), ("L03", 3), ("L03", 27), ("L03", 37), ("L03", 8)]
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def plan():
    import build_key_v7 as b, build_key_v8 as b8
    from f61crib import align
    k = b8.load_key_v8(ebr="A"); A = defaultdict(list)
    for r in rd(f"{T}/scripts/pass108A_classes.tsv"): A[r["line"]].append(r)
    hits = defaultdict(list)
    for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{T}/scripts/tomokiyo_spans_3983.tsv") if l[0] == "T"):
        row = "L02" if s == "T1" else "L03"; seq = [r["sign"] for r in A[row]]; mm = m.translate(b.FOLD)
        for i, j in sorted(align(mm, seq, k)[1], key=lambda x: x[1]):
            if mm[i] in k.get(seq[j], ()) and (row, j + 1) not in TARGETS: hits[seq[j]].append((row, j + 1))
    refs = [(c, *hits[c][0]) for c in CLS]; known = [(c, *h) for c in CLS for h in hits[c][1:3]]
    return A, refs, known
def tile(A, row, pos, w, label):
    from PIL import Image, ImageDraw
    r = A[row][pos - 1]; seg, x = int(r["segment"]), int(r["x_px"])
    im = Image.open(f"{IM}/f108sheetB_{row}.jpg").convert("RGB"); st = (im.height + 12) // 4; y0 = (seg - 1) * st; y1 = y0 + st - 12
    x0 = x - w // 2; c0 = Image.new("RGB", (w, y1 - y0), "white"); c0.paste(im.crop((max(0, x0), y0, min(im.width, x0 + w), y1)), (max(0, -x0), 0))   # padded, not clamped (fixed before the call: clamped edge tiles put the marker off the sign)
    s = min(1.2, 150 / c0.height, 360 / w)
    c0 = c0.resize((int(w * s), int(c0.height * s))); c = Image.new("RGB", (370, 190), "white"); c.paste(c0, (5, 0)); d = ImageDraw.Draw(c)
    mx = 5 + int((x - x0) * s); y = c0.height; d.polygon([(mx - 9, y + 16), (mx + 9, y + 16), (mx, y + 2)], fill=(220, 0, 0)); d.text((6, y + 20), label, fill=(0, 0, 0))
    return c
def sheet(ims, path, rows):
    from PIL import Image
    sh = Image.new("RGB", (4 * 370, rows * 190), "white"); [sh.paste(c, ((k % 4) * 370, (k // 4) * 190)) for k, c in enumerate(ims)]; sh.save(path, quality=90)
def tiles(scratch):
    A, refs, known = plan(); os.makedirs(f"{scratch}/h418", exist_ok=True)
    sheet([tile(A, row, pos, 300, f"R{k}") for k, (c, row, pos) in enumerate(refs, 1)], f"{scratch}/h418/references.jpg", 3)
    its = [(w, "", row, pos, width) for row, pos in TARGETS for w, width in (("W1", 300), ("W2", 240), ("W3", 360))] + [("K", c, row, pos, 300) for c, row, pos in known]
    random.Random(418).shuffle(its); key = ["item\tkind\tcode\tline\tpos\tref"]; ims = []
    for n, (kind, c, row, pos, w) in enumerate(its, 1):
        ims.append(tile(A, row, pos, w, f"I{n:02d}")); code = A[row][pos - 1]["sign"]
        key.append(f"I{n:02d}\t{kind}\t{code}\t{row}\t{pos}\t{'R' + str(CLS.index(c) + 1) if kind == 'K' else ''}")
    for s in range(0, len(ims), 20): sheet(ims[s:s + 20], f"{scratch}/h418/items_{s // 20 + 1:02d}.jpg", 5)
    open(f"{HERE}/h418_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items;", len(known), "known;", "refs", [(c, r, p) for c, r, p in refs])
def score():
    ans = {r["id"]: r["answer"].strip().upper() for r in rd(f"{P}/h418_reply.tsv")}; it = rd(f"{HERE}/h418_items.tsv")
    kn = [r for r in it if r["kind"] == "K"]; g = sum(ans.get(r["item"]) == r["ref"] for r in kn); names = {f"R{k}": c for k, c in enumerate(CLS, 1)}
    out = [f"gate: {g}/{len(kn)} known f.108r items name their class's reference (>= {len(kn) - 2})"]
    if g < len(kn) - 2: out.append("CONTROL FAIL -- nothing scored")
    else:
        for row, pos in TARGETS:
            w = [ans.get(r["item"], "missing") for r in sorted((r for r in it if (r["line"], r["pos"]) == (row, str(pos))), key=lambda r: r["kind"])]
            top, n = Counter(w).most_common(1)[0]; code = [r["code"] for r in it if (r["line"], r["pos"]) == (row, str(pos))][0]
            out.append(f"{row}/{pos} (code {code}) W1-W3: {w} -> " + ((names.get(top, "punctuation" if top == "P" else top.lower())) if n >= 2 else "unclear"))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h418_108r_qa_result.txt"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]
    tiles(a[1]) if a[0] == "tiles" else score()
