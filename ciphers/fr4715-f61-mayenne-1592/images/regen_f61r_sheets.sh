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
