#!/bin/sh
# RUN1-SEG (4 Oct 2026): rebuild the Juan Manuel sorter sheet. Needs the three DECODE full-size images (one browser
# login, tools/decode_browser_login.js 9528 DIR --fetch <filesrv URLs>; sha1s in ../images/manifest.json) in $DEC.
set -e
DEC=${DEC:?set DEC to the folder with IMG_R9528_I44887_P2.jpg IMG_R9529_I44892_P2.jpg IMG_R9501_I44762_P1.jpg}
W=${W:?set W to a scratch folder}
T=ciphers/rah-juan-manuel-1521/sorter
python3 tools/iiif_lines.py --image $DEC/IMG_R9528_I44887_P2.jpg --region 1860,200,1620,2200 --out $W/crops --prefix f194 --follow-slope 300 --slope-margin 22
python3 tools/iiif_lines.py --image $DEC/IMG_R9529_I44892_P2.jpg --region 1860,180,1620,2200 --out $W/crops --prefix f199 --follow-slope 300 --distance 48 --slope-margin 22
python3 tools/iiif_lines.py --image $DEC/IMG_R9501_I44762_P1.jpg --region 1820,205,1570,1870 --out $W/crops --prefix f34 --follow-slope 300 --slope-margin 22
python3 $T/seg_accept.py --page f194 --crops $W/crops --out $W/acc194          # the pre-registered gate (PREREG_seg.md)
P=""
for f in $W/crops/f194_L*.jpg $W/crops/f199_L*.jpg $W/crops/f34_L*.jpg; do
  n=$(basename $f .jpg)
  case $n in f194_L09|f194_L11|f194_L23|f194_L26|f199_L27) continue;; esac   # duplicate crops; f199 L27 blank margin
  P="$P --page $(echo $n | tr -d _)=$f"
done
python3 tools/glyph_atlas.py segment --cursive $P --out $W/atlas
python3 tools/glyph_atlas.py cluster --out $W/atlas --k 80 --k-marks 1
python3 $T/pile_names.py --atlas $W/atlas --out $W/sorter
python3 - "$W" <<'PY'
import json, sys
import numpy as np
from PIL import Image
W = sys.argv[1]; P = json.load(open(f'{W}/atlas/pages.json'))
for k, v in P.items():     # posterise: paper -> white, ink in 4 levels (keeps the page under 10 MB)
    g = np.array(Image.open(v['image']).convert('L')).astype(int)
    g = np.where(g > 175, 255, (g // 64) * 64 + 20).astype(np.uint8)
    v['image'] = f'{W}/{k}.png'; Image.fromarray(g).save(v['image'], optimize=True)
json.dump(P, open(f'{W}/pages_post.json', 'w'))
PY
python3 tools/sign_sorter.py --signs $W/atlas/signs.tsv --labels $W/sorter/labels.tsv --pages $W/pages_post.json \
  --clusters $W/atlas/clusters.tsv --focus $W/sorter/focus.tsv \
  --focus-note "Piles are shape clusters from glyph_atlas segment --cursive (over-split, k=80). Three piles carry a proposed name (Z=r, R=s) from a by-eye look; the rest are unnamed. These tiles come from piles that look mixed by eye: which sign is each?" \
  --title "Juan Manuel 1522 Sign Sorter" \
  --lede "DECODE records R9528 (f.194), R9529 (f.199) and R9501 (f.34): letters of Juan Manuel to Charles V, 1522, in a joined cursive hand. 1,781 cut-outs. Latin code words (sof, gap, qid ...) and non-Latin symbol signs are mixed; please pile the symbol signs by shape and set code words and bad cuts aside." \
  --out $T/index.html
