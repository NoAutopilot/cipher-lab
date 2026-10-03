#!/bin/sh
# Regenerates the survey images (not committed: Gallica images, re-fetchable). Usage: sh survey_fetch.sh OUTDIR
# 273 thumbnails c150-c422 at 300 px, 2 s apart (good-citizen rule), then 8-up contact sheets via PIL.
OUT=${1:-/tmp/fr16144-survey}; mkdir -p "$OUT"; cd "$OUT" || exit 1
for n in $(seq 150 422); do
  [ -s f$n.jpg ] || { curl -sS -A "Mozilla/5.0" -o f$n.jpg "https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060974c/f$n/full/300,/0/default.jpg"; sleep 2; }
done
python3 - <<'PY'
from PIL import Image, ImageDraw
for a,b in [(150,197),(198,245),(246,293),(294,341),(342,382),(383,422)]:
    ims=[(n,Image.open(f"f{n}.jpg")) for n in range(a,b+1)]
    W,H,c=300,440,8; S=Image.new("RGB",(c*W,((len(ims)+c-1)//c)*H),"white"); d=ImageDraw.Draw(S)
    for i,(n,im) in enumerate(ims):
        im.thumbnail((W-6,H-26)); x,y=(i%c)*W,(i//c)*H; S.paste(im,(x+3,y+24)); d.text((x+5,y+4),f"c{n}",fill="red")
    S.save(f"sheet_{a}_{b}.jpg",quality=80)
PY
