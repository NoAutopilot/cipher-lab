#!/bin/sh
# MAT-F91E, 15 Oct 2026: re-derive the block E line crops of f.92r (BnF fr.15572, btv1b9061879d canvas 98) and the E1-E5 line images.
# Images are never committed (lane rule); run from the repository root. 1 request to openapi.bnf.fr (skipped if OUTDIR/c98_max.jpg exists;
# sha1 dfec5334995404682b478e338d522405ec8e32a2, 8722x6347). Usage: sh ciphers/matignon-mayenne-1586/f91/regen_f91e.sh OUTDIR
set -e
O=${1:?OUTDIR}; mkdir -p "$O/lines"
I="$O/c98_max.jpg"
[ -s "$I" ] || curl -sS -A 'cipher-lab research script (contact via repository)' -o "$I" \
  "https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9061879d/f98/full/max/0/default.jpg"
F='--deskew-region --band-extent --mask-neighbours --max-width 1600 --overlap 80 --debug'
python3 tools/iiif_lines.py --image "$I" --out "$O/crops" --region 5230,1200,2900,680 --prefix ciE $F
python3 tools/iiif_lines.py --image "$I" --out "$O/gl" --region 4470,1290,780,620 --prefix glE $F
# E1-E5 = bands L02-L06; s2 trimmed 200 px at its left (overlap 300 -> 100 px), s1 above s2 with a 6 px grey rule
python3 - "$O" <<'PY'
import sys; from PIL import Image, ImageDraw
O = sys.argv[1]
for i, L in enumerate(range(2, 7), 1):
    a = Image.open(f'{O}/crops/ciE_L0{L}_s1.jpg').convert('RGB'); b = Image.open(f'{O}/crops/ciE_L0{L}_s2.jpg').convert('RGB')
    b = b.crop((200, 0, b.width, b.height)); W = max(a.width, b.width)
    out = Image.new('RGB', (W, a.height + 6 + b.height), 'white'); out.paste(a, (0, 0))
    ImageDraw.Draw(out).rectangle([0, a.height, W, a.height + 5], fill=(150, 150, 150)); out.paste(b, (0, a.height + 6))
    out.save(f'{O}/lines/E{i}.jpg')
PY
