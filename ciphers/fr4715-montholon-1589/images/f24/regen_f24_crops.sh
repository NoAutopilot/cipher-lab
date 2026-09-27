#!/bin/sh
# Regenerates no.6 f.24r's interlinear (gloss-above-cipher) reading crops from the cached
# native-resolution source region. MONT-KEY6, 27 Sept 2026. Extends MONT-4715's f.81r
# crop-legibility fix (ciphers/fr4715-montholon-1589/NOTES.md, MONT-4715 section) to an
# interlinear leaf.
#
# Tuning note (checked by eye against the debug overlay, whole page top/middle/bottom, then
# against the upscaled crop itself): f.24r's ink-density profile does NOT alternate cleanly
# gloss-peak/cipher-peak/gloss-peak/... at a regular pitch the way a single-layer cipher leaf
# does -- ascenders and loops inside a single handwritten row often produce two close ink peaks
# (40-60px apart) that are indistinguishable, by height/prominence alone, from the true (and
# highly irregular, 40-170px) gap between one real row and the next. A first attempt at pairing
# exactly 2 raw peaks per crop (one gloss + one cipher, --lines-per-crop 2) failed on inspection:
# band 1 turned out to be two sub-peaks of the SAME gloss row ("noster heur est trop"), with no
# cipher digits in the crop at all -- caught by opening the raw single-width segment before
# stacking, not by the debug overlay alone (the overlay looked plausible at a glance).
#
# Fix: --lines-per-crop 12 (about 5-6 gloss+cipher pairs per band, 7 bands total, generous
# margin at each edge so a boundary falls in whitespace even where individual peaks are noisy);
# the transcribing pass reads and labels the lines itself from what is visibly there, rather than
# this script asserting a pair boundary it cannot reliably compute. Width stays capped at 900px
# native per segment (5 segments/band, 35 crops total) -- upscaled 3x each, a segment displays at
# an effective ~1.57x native zoom after the vision pipeline's own long-edge downscale (checked
# directly: /tmp/l01_s1_full.jpg, every digit and gloss letter clearly legible), a smaller net
# zoom than MONT-4715's single-row 900px segments (~2.22x, shorter aspect ratio) but still a
# zoom-IN from native, confirmed legible by direct inspection, not assumed. No stacking into one
# composite sheet per band this time: a composite of five 900x1271 segments came to 2700x19065,
# far outside any reasonable single-image aspect ratio -- the 35 individual per-segment crops are
# handed to the transcribing pass directly instead.
set -e
cd "$(dirname "$0")/../../../.."
python3 tools/iiif_lines.py \
  --image ciphers/fr4715-montholon-1589/images/f24/src_ark_12148_btv1b52509819x_f61_100_80_3900_5800.jpg \
  --region 0,0,3900,5800 \
  --out ciphers/fr4715-montholon-1589/images/f24 \
  --prefix f24t --max-width 900 --lines-per-crop 12 --debug
python3 - <<'PYEOF'
from PIL import Image
import glob, re
for fn in sorted(glob.glob("ciphers/fr4715-montholon-1589/images/f24/f24t_L*_s*.jpg")):
    im = Image.open(fn)
    up = im.resize((im.width * 3, im.height * 3), Image.LANCZOS)
    out = fn.replace("f24t_", "f24zoom_")
    up.save(out, quality=90)
PYEOF
rm -f ciphers/fr4715-montholon-1589/images/f24/f24t_L*_s*.jpg
echo "regenerated f24zoom_L*_s*.jpg (35 crops, 3x upscaled)"
