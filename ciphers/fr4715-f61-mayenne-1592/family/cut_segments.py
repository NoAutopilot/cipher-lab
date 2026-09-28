#!/usr/bin/env python3
"""F61-FAMILY-5 (28 Sept 2026): letter-aligned gloss segments for an interlined leaf whose cipher rows are already coded.
The gloss on de Diou's leaves is a letter-by-letter interlinear decipherment (one clear letter above each sign, a word
above a word-code sign), so the gloss is read AS LETTERS ALIGNED TO SIGNS, not as words (H45's word passes agreed on 42%).
For each band, the reconciled draft's signs (passes/rec<PRE>/ciphertext_draft.tsv, native x recovered from pass A, or
pass B where A has a gap) are grouped into segments of --n signs (6-10), and each segment is cut from the native leaf at
--scale (3x) as a band centred between the gloss row and the cipher row (cipher centre = the 2x band box's y0 + 70;
gloss centre = cipher centre - 40; band from cipher centre - --up to + --down). Under the crop a white strip carries a
red tick and the position number (1..k) at every sign's x, so a reader reports the letter(s) written above tick k.
Alongside, the v3 skeleton of the segment (family/<PRE>_decode_period_v3.tsv: the period letter set per position, '?'
where no period pair exists) is written, with --mask F of the covered positions hidden as '?' at random (seed = band
number x 100 + segment): the hidden positions are the positive control (a reader that reads letters, not the skeleton,
agrees with the hidden sets; the hidden and the truly uncovered positions look the same to it).
Output: sheets/<OUT>/<OUT>_L<nn>_g<k>.jpg and sheets/<OUT>_segments.json (band, segment, draft positions, classes,
skeleton shown, skeleton hidden, native box).
  python3 cut_segments.py PRE OUT --bands L01,L02,... [--n 8] [--scale 3] [--up 82] [--down 42] [--pad 28] [--mask 0.3]
"""
import csv, json, math, os, random, sys
from collections import defaultdict
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
a = sys.argv; pre, out = a[1], a[2]
def opt(n, d): return type(d)(a[a.index(n) + 1]) if n in a else d
N, SC, UP, DOWN, PAD, MASK = opt("--n", 8), opt("--scale", 3.0), opt("--up", 82), opt("--down", 42), opt("--pad", 28), opt("--mask", 0.3)
want = a[a.index("--bands") + 1].split(",") if "--bands" in a else None
bands = json.load(open(f"{HERE}/sheets/{pre}_bands.json")); sc2 = bands["scale"]; boxes = bands["boxes"]
img = Image.open(f"{HERE}/{bands['image']}").convert("L")
rd = lambda p: [r for r in csv.DictReader((l for l in open(p) if not l.startswith("#")), delimiter="\t")]
D = rd(f"{P}/rec{pre}/ciphertext_draft.tsv"); A = rd(f"{P}/{pre}_signsA.tsv"); B = rd(f"{P}/{pre}_signsB.tsv")
Ab = defaultdict(list); Bb = defaultdict(list)
for r in A: Ab[r["line"]].append(r)
for r in B: Bb[r["line"]].append(r)
skel = {(r["line"], int(r["pos"])): r for r in rd(f"{HERE}/{pre}_decode_period_v3.tsv")} if os.path.exists(f"{HERE}/{pre}_decode_period_v3.tsv") else {}
drop = set()
if os.path.exists(f"{P}/{pre}_drop.tsv"):
    for r in rd(f"{P}/{pre}_drop.tsv"): drop.add((r["line"], r["segment"]))
# native x per draft position: walk pass A and pass B in step with the draft's gap marks (alt 'A:-' = A has no token here)
signs = defaultdict(list)
for line in sorted({r["line"] for r in D}):
    ia = ib = 0
    for r in [r for r in D if r["line"] == line]:
        alt = r["alt"]; ra = rb = None
        if not alt.startswith("A:-") and ia < len(Ab[line]): ra = Ab[line][ia]; ia += 1
        if not alt.startswith("B:-") and ib < len(Bb[line]): rb = Bb[line][ib]; ib += 1
        src = ra or rb
        if src is None: continue
        seg = src["segment"]; box = boxes.get(f"{pre}_{line}_{seg}.jpg")
        if box is None or (line, seg) in drop: continue
        x = box[0] + float(src["x_px"]) / sc2; cc = box[1] + 70
        signs[line].append({"pos": int(r["position"]), "code": r["sign"], "x": x, "cc": cc, "seg": seg, "note": (ra or {}).get("note", "")})
os.makedirs(f"{HERE}/sheets/{out}", exist_ok=True)
try: font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
except Exception: font = ImageFont.load_default()
segs = []
for line in sorted(signs):
    if want and line not in want: continue
    ss = sorted(signs[line], key=lambda s: s["x"]); n = len(ss); k = max(1, math.ceil(n / N)); size = n / k
    for g in range(k):
        part = ss[int(round(g * size)):int(round((g + 1) * size))]
        if not part: continue
        x0 = int(min(s["x"] for s in part) - PAD); x1 = int(max(s["x"] for s in part) + PAD); cc = int(round(sum(s["cc"] for s in part) / len(part)))
        y0, y1 = cc - UP, cc + DOWN
        crop = img.crop((x0, y0, x1, y1)).convert("RGB"); crop = crop.resize((int(crop.width * SC), int(crop.height * SC)), Image.LANCZOS)
        strip = Image.new("RGB", (crop.width, 46), (255, 255, 255)); d = ImageDraw.Draw(strip)
        for i, s in enumerate(part, 1):
            tx = int((s["x"] - x0) * SC); d.line((tx, 0, tx, 16), fill=(220, 0, 0), width=3); d.text((tx - 6 if i < 10 else tx - 12, 18), str(i), fill=(220, 0, 0), font=font)
        sheet = Image.new("RGB", (crop.width, crop.height + strip.height), (255, 255, 255)); sheet.paste(crop, (0, 0)); sheet.paste(strip, (0, crop.height))
        name = f"{out}_{line}_g{g + 1}.jpg"; sheet.save(f"{HERE}/sheets/{out}/{name}", quality=90)
        rng = random.Random(int(line[1:]) * 100 + g + 1); shown = []; hidden = []
        for i, s in enumerate(part, 1):
            sk = skel.get((line, s["pos"])); letters = sk["period_letters"] if sk else "-"
            covered = bool(sk) and sk["grade"] in ("C", "C+", "M", "S")
            if covered and MASK and rng.random() < MASK: hidden.append([i, s["code"], letters]); shown.append([i, "?"])
            elif covered: shown.append([i, letters])
            else: shown.append([i, "?"])
        segs.append({"file": name, "band": line, "segment": g + 1, "positions": [s["pos"] for s in part], "classes": [s["code"] for s in part],
                     "notes": [s["note"] for s in part], "box": [x0, y0, x1, y1], "width_px": sheet.width, "height_px": sheet.height, "shown": shown, "hidden": hidden})
# merge into an existing segments file: the bands cut now replace their earlier entries, other bands are kept
JP = f"{HERE}/sheets/{out}_segments.json"; old = json.load(open(JP))["segments"] if os.path.exists(JP) else []
cut = {s["band"] for s in segs}; segs = [s for s in old if s["band"] not in cut] + segs; segs.sort(key=lambda s: (s["band"], s["segment"]))
json.dump({"leaf": pre, "scale": SC, "n": N, "up": UP, "down": DOWN, "mask": MASK, "segments": segs}, open(JP, "w"), indent=1)
print("segments", len(segs), "bands", len({s['band'] for s in segs}), "signs", sum(len(s["positions"]) for s in segs), "hidden", sum(len(s["hidden"]) for s in segs))
