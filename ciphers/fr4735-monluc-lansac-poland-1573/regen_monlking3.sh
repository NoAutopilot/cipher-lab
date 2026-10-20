#!/bin/sh
# MONL-KING3 (20 Oct 2026): re-derive the untracked c258 (f.133) native page and the L11-L25 crops read in king3/ (1 request).
set -e
cd "$(dirname "$0")"; D=images/scratchking2; mkdir -p $D images/scratchking3; echo '*' > $D/.gitignore; echo '*' > images/scratchking3/.gitignore
[ -f $D/src_image_v3_ark_12148_btv1b9060724s_f258_full.jpg ] || curl -sS -A "cipher-lab research script (contact via repository)" -o $D/src_image_v3_ark_12148_btv1b9060724s_f258_full.jpg "https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060724s/f258/full/max/0/default.jpg"
python3 king3_crops.py
