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
