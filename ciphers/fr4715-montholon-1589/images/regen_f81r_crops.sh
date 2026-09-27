#!/bin/sh
# Regenerates f81r's cipher-passage line crops from the cached native-resolution source region.
# MONT-4715, 27 Sept 2026. Two-step process (rule 7 reproducibility):
#   1. tools/iiif_lines.py cuts native 900px-wide segments per detected line (5 segments x 36 lines).
#      A first attempt at --max-width 2400 (2 segments/line, prefix f81r_) was tried and abandoned:
#      two independent blind Sonnet passes on those crops both declined to transcribe, citing
#      illegible digit shapes at that width (the vision pipeline appears to downscale a wide image
#      before the model sees it, so packing ~13-15 sign-groups into one 2400px-wide crop leaves too
#      few effective pixels per digit). Narrowing to 900px (about 5 groups per crop) fixed this on
#      inspection (ciphers/fr4715-montholon-1589/NOTES.md, MONT-4715 section).
#   2. Each 900px crop is upscaled 3x (LANCZOS) to land just under the display's own ~2000px
#      downscale threshold -- narrowing alone was legible but small; narrowing + 3x upscale was
#      clearly the easiest to read (same fix as NEV-C3's "3x zoom" on ceppo-nevers-fr3251-1570s).
set -e
cd "$(dirname "$0")/../../.."
# `sh regen_f81r_crops.sh slope` runs only the second block, `... dots` only the third (running block 1 regenerates
# 180 crops, >30 MB).
MODE="${1:-all}"
if [ "$MODE" = all ]; then
python3 tools/iiif_lines.py \
  --image ciphers/fr4715-montholon-1589/images/src_ark_12148_btv1b52509819x_f177_326_1285_3630_2243.jpg \
  --region 0,0,3630,2243 \
  --out ciphers/fr4715-montholon-1589/images \
  --prefix f81rz --max-width 900
python3 - <<'PYEOF'
from PIL import Image
import glob
for fn in sorted(glob.glob("ciphers/fr4715-montholon-1589/images/f81rz_L*.jpg")):
    im = Image.open(fn)
    up = im.resize((im.width * 3, im.height * 3), Image.LANCZOS)
    out = fn.replace("f81rz_", "f81rzoom_")
    up.save(out, quality=92)
PYEOF
rm -f ciphers/fr4715-montholon-1589/images/f81rz_L*.jpg
echo "regenerated f81rzoom_L*.jpg (180 crops)"
fi

if [ "$MODE" = all ] || [ "$MODE" = slope ]; then
# --- Second block: MONT-RECROP, 27 Sept 2026 (does not replace the block above). ---
# The f81rsheet_Lnn.jpg sheets were cut at a fixed y per line, but f.81r's lines slope ~0.02 (60-100 px over the
# 3630 px region, more than the 52 px pitch), so the named line left the strip in segment 3 or 4 (MONT-READ-DIGITS).
# tools/iiif_lines.py --follow-slope 300 --slope-local tracks each line from its left end through 300 px windows and
# cuts every segment as a sheared strip centred on it (+6 px margin); only the four calibration lines are cut.
# Then the same 3x LANCZOS upscale and one vertically stacked sheet per line, prefix f81rslope_ (old sheets kept).
python3 tools/iiif_lines.py \
  --image ciphers/fr4715-montholon-1589/images/src_ark_12148_btv1b52509819x_f177_326_1285_3630_2243.jpg \
  --region 0,0,3630,2243 \
  --out ciphers/fr4715-montholon-1589/images \
  --prefix f81rsl --max-width 900 --follow-slope 300 --slope-local --slope-margin 6 --only-lines 3,8,13,15
python3 - <<'PYEOF'
import glob
from PIL import Image, ImageDraw
d = "ciphers/fr4715-montholon-1589/images"
for L in (3, 8, 13, 15):
    segs = sorted(glob.glob(f"{d}/f81rsl_L{L:02d}_s*.jpg"))
    ups = []
    for f in segs:
        im = Image.open(f)
        ups.append(im.resize((im.width * 3, im.height * 3), Image.LANCZOS))
    sh = Image.new("RGB", (max(u.width for u in ups), sum(u.height + 22 for u in ups)), (255, 255, 255))
    dr = ImageDraw.Draw(sh); y = 0
    for i, u in enumerate(ups, 1):
        dr.text((4, y + 4), f"L{L:02d} segment {i} of {len(ups)}", fill=(200, 0, 0)); y += 22
        sh.paste(u, (0, y)); y += u.height
    sh.save(f"{d}/f81rslope_L{L:02d}.jpg", quality=90)
PYEOF
rm -f ciphers/fr4715-montholon-1589/images/f81rsl_L*.jpg
echo "regenerated f81rslope_L03/L08/L13/L15.jpg"
fi

# --- Third block: MONT-DOTS, 27 Sept 2026 (does not replace the blocks above). ---
# Call C on the f81rslope_ sheets missed only the dotted gate (0.657 vs 0.70); the reader saw them at ~0.74x native.
# Same cut as block 2 but half-width segments (--max-width 450), so each dot carries about twice the displayed pixels.
# Same 3x LANCZOS upscale and stacking, prefix f81rdots_, but two sheets per line (segments 1-6 in ...a.jpg, 7-12 in
# ...b.jpg): one 12-segment stack is ~1350x2600, which a ~2000 px long-edge display cap would shrink to ~0.78x --
# no gain over call C's 0.74x. Each half is ~1350x1300 and shows at native.
if [ "$MODE" = all ] || [ "$MODE" = dots ]; then
python3 tools/iiif_lines.py \
  --image ciphers/fr4715-montholon-1589/images/src_ark_12148_btv1b52509819x_f177_326_1285_3630_2243.jpg \
  --region 0,0,3630,2243 \
  --out ciphers/fr4715-montholon-1589/images \
  --prefix f81rdh --max-width 450 --follow-slope 300 --slope-local --slope-margin 6 --only-lines 3,8,13,15
python3 - <<'PYEOF'
import glob
from PIL import Image, ImageDraw
d = "ciphers/fr4715-montholon-1589/images"
for L in (3, 8, 13, 15):
    # numeric order: 12 segments, and a plain sort puts s10-s12 before s2
    segs = sorted(glob.glob(f"{d}/f81rdh_L{L:02d}_s*.jpg"), key=lambda f: int(f.rsplit("_s", 1)[1].split(".")[0]))
    ups = []
    for f in segs:
        im = Image.open(f)
        ups.append(im.resize((im.width * 3, im.height * 3), Image.LANCZOS))
    half = (len(ups) + 1) // 2
    for part, lo, hi in (("a", 0, half), ("b", half, len(ups))):
        sel = ups[lo:hi]
        sh = Image.new("RGB", (max(u.width for u in sel), sum(u.height + 22 for u in sel)), (255, 255, 255))
        dr = ImageDraw.Draw(sh); y = 0
        for i, u in enumerate(sel, lo + 1):
            dr.text((4, y + 4), f"L{L:02d} segment {i} of {len(ups)}", fill=(200, 0, 0)); y += 22
            sh.paste(u, (0, y)); y += u.height
        sh.save(f"{d}/f81rdots_L{L:02d}{part}.jpg", quality=90)
PYEOF
rm -f ciphers/fr4715-montholon-1589/images/f81rdh_L*.jpg
echo "regenerated f81rdots_L{03,08,13,15}{a,b}.jpg"
fi
