#!/bin/sh
# MAT-154, 15 Oct 2026: re-derive the f.154r cipher region (BnF fr.15572, btv1b9061879d canvas 161) and its 28 levelled line strips.
# Images are never committed (lane rule); run from the repository root. 2 requests to openapi.bnf.fr, >= 3 s apart.
# Region file sha1 3416510efc3517519b664e347064f6216c8c78b1 (3579x4090) as fetched 15 Oct 2026.
# Usage: sh ciphers/matignon-mayenne-1586/o154/regen_o154.sh OUTDIR
set -e
O=${1:?OUTDIR}; mkdir -p "$O"
UA='cipher-lab research script (contact via repository)'
B=https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9061879d/f161
[ -s "$O/c161_1600.jpg" ] || { curl -sS -A "$UA" -o "$O/c161_1600.jpg" "$B/full/1600,/0/default.jpg"; sleep 3.2; }
[ -s "$O/c161_pct.jpg" ] || curl -sS -A "$UA" -o "$O/c161_pct.jpg" "$B/pct:52.5,32.5,42,64.5/max/0/default.jpg"
python3 ciphers/matignon-mayenne-1586/o154/lines154.py "$O/c161_pct.jpg" "$O/lv"
