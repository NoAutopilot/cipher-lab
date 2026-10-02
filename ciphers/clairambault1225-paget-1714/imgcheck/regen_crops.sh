#!/bin/sh
# Re-cut the A2-PAG2 line crops (images/lines/<half>_Lnn.jpg + debug overlays) from the page-halves on disk.
# Not committed (they would take images/ over 30 MB); images/lines/manifest.json records every crop box.
cd "$(dirname "$0")/.." || exit 1
for f in f60R f61L f61R f65L f65R f66L f66R; do
  python3 ../../tools/iiif_lines.py --image images/$f.jpg --out images/lines --prefix $f --distance 60 \
    --prominence 60 --lines-per-crop 2 --top-margin 90 --debug
done
