#!/bin/sh
# Re-cut the A2-PAG2 line crops (images/lines/<half>_Lnn.jpg + debug overlays) from the page-halves on disk.
# Not committed (they would take images/ over 30 MB); images/lines/manifest.json records every crop box.
cd "$(dirname "$0")/.." || exit 1
for f in f60R f61L f61R f65L f65R f66L f66R; do
  python3 ../../tools/iiif_lines.py --image images/$f.jpg --out images/lines --prefix $f --distance 60 \
    --prominence 60 --lines-per-crop 2 --top-margin 90 --debug
done
# A2-PAG3 (2 Oct 2026): the f66L gutter strip, cut from images/f66R.jpg's left 340 px, then x2 LANCZOS copies for the passes.
python3 ../../tools/iiif_lines.py --image images/f66R.jpg --region 0,150,340,1800 --out images/gutter --prefix f66Lg \
  --distance 40 --prominence 30 --lines-per-crop 3 --top-margin 40 --debug
python3 -c "
from PIL import Image; import glob
for f in sorted(glob.glob('images/gutter/f66Lg_L0?.jpg')):
    im=Image.open(f); im.resize((im.width*2,im.height*2),Image.LANCZOS).save(f.replace('.jpg','_x2.jpg'),quality=92)"
