#!/bin/sh
# F61-CAL, 27 Sept 2026: slope sheets of f.61r for the five spans Tomokiyo marks (lines L01 L03 L05 L07 L08 L11).
# Source: the native region 500,1880,3320,1420 of canvas f137 (one Gallica request, 27 Sept 2026; a second request
# for a taller region got a connection reset and was not retried in a loop). Cut with the shared tool (MONT-RECROP recipe: slope-following, 900 px segments), then 3x LANCZOS and one
# stacked sheet per line holding only the segments that carry cipher signs. Run from the repository root.
set -e
T=ciphers/fr4715-f61-mayenne-1592
python3 tools/iiif_lines.py --image $T/images/src_ark_12148_btv1b52509819x_f137_500_1880_3320_1420.jpg \
  --out $T/images --prefix f61s --max-width 900 --follow-slope 300 --slope-local --debug
python3 - <<'PY'
import glob, re
from PIL import Image, ImageDraw
T = "ciphers/fr4715-f61-mayenne-1592/images"
keep = {"L01": [4, 5], "L03": [1, 2, 3], "L05": [2, 3, 4], "L07": [3, 4, 5], "L08": [1, 2], "L11": [1, 2]}
for line, segs in keep.items():
    ims = [Image.open(f"{T}/f61s_{line}_s{s}.jpg").convert("RGB") for s in segs]
    ims = [im.resize((im.width * 3, im.height * 3), Image.LANCZOS) for im in ims]
    W = max(im.width for im in ims); H = sum(im.height for im in ims) + 12 * (len(ims) - 1)
    sheet = Image.new("RGB", (W, H), "white"); y = 0; d = ImageDraw.Draw(sheet)
    for i, im in enumerate(ims):
        sheet.paste(im, (0, y)); d.text((6, y + 4), f"segment {i+1}", fill=(200, 0, 0))
        y += im.height
        if i < len(ims) - 1:
            d.rectangle((0, y, W, y + 11), fill=(0, 0, 0)); y += 12
    sheet.save(f"{T}/f61sheet_{line}.jpg", quality=90)
    print(line, sheet.size, "segments", segs)
PY

# H2 (campaign, 27 Sept 2026): sheets B for the second blind read -- the whole of each span line, segments cut with
# --overlap 0 (the tool still spreads 4 segments of 900 px evenly over 3320 px, so 93 native px repeat) and each
# non-final segment TRIMMED to the next segment's x0 before the 3x scale, so no sign appears twice (a sign on a boundary
# is split, not doubled; the reader is told so). Crops go to a temp dir; only the six stacked sheets are committed.
NOOV=$(mktemp -d)
python3 tools/iiif_lines.py --image $T/images/src_ark_12148_btv1b52509819x_f137_500_1880_3320_1420.jpg \
  --out $NOOV --prefix f61n --max-width 900 --overlap 0 --follow-slope 300 --slope-local
NOOV=$NOOV python3 - <<'PY'
import json, os
from PIL import Image, ImageDraw
T = "ciphers/fr4715-f61-mayenne-1592/images"; N = os.environ["NOOV"]
box = {e["crop"]: e["box"] for e in json.load(open(f"{N}/manifest.json"))["iiif_lines"]}
for line in ["L01", "L03", "L05", "L07", "L08", "L11"]:
    segs = sorted(c for c in box if c.startswith(f"f61n_{line}_s"))
    ims = []
    for k, c in enumerate(segs):
        im = Image.open(f"{N}/{c}").convert("RGB")
        if k + 1 < len(segs):
            im = im.crop((0, 0, box[segs[k + 1]][0] - box[c][0], im.height))
        ims.append(im.resize((im.width * 3, im.height * 3), Image.LANCZOS))
    W = max(im.width for im in ims); H = sum(im.height for im in ims) + 12 * (len(ims) - 1)
    sheet = Image.new("RGB", (W, H), "white"); y = 0; d = ImageDraw.Draw(sheet)
    for i, im in enumerate(ims):
        sheet.paste(im, (0, y)); d.text((6, y + 4), f"segment {i+1}", fill=(200, 0, 0)); y += im.height
        if i < len(ims) - 1: d.rectangle((0, y, W, y + 11), fill=(0, 0, 0)); y += 12
    sheet.save(f"{T}/f61sheetB_{line}.jpg", quality=90); print(line, sheet.size, "segments", len(ims), "(B, no overlap)")
PY

# H19 (campaign, 27 Sept 2026): BnF fr.3983 f.108r, canvas 195 of ark btv1b9059406b (anchored by eye: ink '108' top right,
# clear lines match Tomokiyo's mayenne2.png strip). One native region fetch, 7 bands (pitch 96), sheets B as above.
NOOV2=$(mktemp -d)
python3 tools/iiif_lines.py --ark btv1b9059406b --canvas 195 --region 1250,450,3600,720 --out $NOOV2 --prefix f108 \
  --max-width 900 --overlap 0 --follow-slope 300 --slope-local --debug
NOOV=$NOOV2 PREFIX=f108 LINES="L01 L02 L03 L04 L05 L06 L07" python3 - <<'PY'
import json, os
from PIL import Image, ImageDraw
T = "ciphers/fr4715-f61-mayenne-1592/images"; N = os.environ["NOOV"]; P = os.environ["PREFIX"]
box = {e["crop"]: e["box"] for e in json.load(open(f"{N}/manifest.json"))["iiif_lines"]}
for line in os.environ["LINES"].split():
    segs = sorted(c for c in box if c.startswith(f"{P}_{line}_s")); ims = []
    for k, c in enumerate(segs):
        im = Image.open(f"{N}/{c}").convert("RGB")
        if k + 1 < len(segs): im = im.crop((0, 0, box[segs[k + 1]][0] - box[c][0], im.height))
        ims.append(im.resize((im.width * 3, im.height * 3), Image.LANCZOS))
    W = max(im.width for im in ims); H = sum(im.height for im in ims) + 12 * (len(ims) - 1)
    sheet = Image.new("RGB", (W, H), "white"); y = 0; d = ImageDraw.Draw(sheet)
    for i, im in enumerate(ims):
        sheet.paste(im, (0, y)); d.text((6, y + 4), f"segment {i+1}", fill=(200, 0, 0)); y += im.height
        if i < len(ims) - 1: d.rectangle((0, y, W, y + 11), fill=(0, 0, 0)); y += 12
    sheet.save(f"{T}/{P}sheetB_{line}.jpg", quality=90); print(line, sheet.size)
PY

# H34 (campaign, 28 Sept 2026): fr.3983 f.108r re-cut with the family cutter, a band per cipher row with its gloss riding above
# (six rows of the 720-px region on disk; a taller region was refused by Gallica twice, images/requests_h34.log), 3x, 24 crops
# under images/f108g/ (only f108g_bands.json, the debug overlay and one sample are committed).
mkdir -p ciphers/fr4715-f61-mayenne-1592/images/f108g
python3 ciphers/fr4715-f61-mayenne-1592/family/cut_bands.py ciphers/fr4715-f61-mayenne-1592/images/src_ark_12148_btv1b9059406b_f195_1250_450_3600_720.jpg 0,0,3600,720 \
  ciphers/fr4715-f61-mayenne-1592/images/f108g f108g --centres 198,294,411,504,618,712 --up 72 --down 34 --local 20 --seg 960 --overlap 80 --scale 3.0
