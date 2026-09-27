#!/bin/sh
# Regenerates fol.58r's (BnF fr.3985, canvas 114) per-line reading sheets f58s_Lnn.jpg. LAU-F58B, 27 Sept 2026.
# LAU-F58 cut this leaf at --max-width 2000 with the detector's default spacing (pitch 140): 30 bands, each of which
# in the cipher-dense middle held parts of two physical rows (a numeral row and the lighter interlinear gloss row
# above it, about 75 px apart), and its passes agreed on 39.2 pct of numerals. Fixes, in order:
#   1. Deskew: the lines rise about 0.03 to the right (100+ px over the 3700 px region, more than one row pitch), so the
#      cached native region is rotated -1.9 deg (bicubic) first (the median of the tool's per-band --follow-slope fits in the dense middle, -0.035; -1.0 deg was tried first and left the rows still rising out of a 63 px band by segment 3). `--follow-slope 300 --slope-local` was tried and
#      rejected: in the dense middle its local tracking jumped between gloss and numeral rows (one numeral row
#      skipped, two bands duplicated), checked by eye.
#   2. tools/iiif_lines.py at --distance 45 --prominence 120 (one band per physical row, 48 bands) and 900 px
#      segments (MONT-4715's width).
#   3. Each segment upscaled 3x (LANCZOS) and the line's segments stacked into one sheet, labelled (Montholon block 2).
set -e
cd "$(dirname "$0")/../../.."
D=ciphers/fr3625-lauriere-1593/images
T=$(mktemp -d)
python3 - "$D" "$T" <<'PYEOF'
import sys
from PIL import Image
d, t = sys.argv[1:]
im = Image.open(f"{d}/src_ark_12148_btv1b90606498_f114_850_400_3700_5100.jpg")
im.rotate(-1.9, resample=Image.BICUBIC, fillcolor=235).save(f"{t}/f58_deskew.jpg", quality=95)
PYEOF
python3 tools/iiif_lines.py --image "$T/f58_deskew.jpg" --region 0,0,3700,5100 --out "$T" \
  --prefix f58seg --max-width 900 --distance 45 --prominence 120 --debug
python3 - "$D" "$T" <<'PYEOF'
import glob, re, sys
from PIL import Image, ImageDraw
d, t = sys.argv[1:]
lines = sorted({int(re.search(r"_L(\d+)_s", f).group(1)) for f in glob.glob(f"{t}/f58seg_L*_s*.jpg")})
for L in lines:
    segs = sorted(glob.glob(f"{t}/f58seg_L{L:02d}_s*.jpg"), key=lambda f: int(re.search(r"_s(\d+)", f).group(1)))
    ups = [Image.open(f).convert("L") for f in segs]
    ups = [u.resize((u.width * 3, u.height * 3), Image.LANCZOS) for u in ups]
    sh = Image.new("L", (max(u.width for u in ups), sum(u.height + 22 for u in ups)), 255)
    dr = ImageDraw.Draw(sh); y = 0
    for i, u in enumerate(ups, 1):
        dr.text((4, y + 4), f"L{L:02d} segment {i} of {len(ups)}", fill=0); y += 22
        sh.paste(u, (0, y)); y += u.height
    sh.save(f"{d}/f58s_L{L:02d}.jpg", quality=45)
Image.open(f"{t}/f58seg_lines_debug.jpg").save(f"{d}/f58s_lines_debug.jpg")
print(f"regenerated {len(lines)} sheets f58s_L01..L{lines[-1]:02d}.jpg")
PYEOF
rm -rf "$T"
