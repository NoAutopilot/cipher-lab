#!/bin/sh
# R10-SEURE4 (6 Oct 2026): re-derive the fr. 3138 Tournon 1556 / Morvilliers 1549 captures (Gallica btv1b90601662).
# The folder is over 30 MB, so only the manifest and two downsized samples are committed.
set -e
cd "$(dirname "$0")/../../.."
O=ciphers/fr3151-seure-1558/known_keys/images
python3 tools/iiif_lines.py --ark btv1b90601662 --canvas 26 --region 1150,600,3000,1650 --prefix tournon_c26 --debug --out $O
sleep 2
python3 tools/iiif_lines.py --ark btv1b90601662 --canvas 25 --region 0,0,3313,1964 --prefix tournon_c25dec --debug --out $O
sleep 2
python3 tools/iiif_lines.py --ark btv1b90601662 --canvas 70 --region 4800,700,2950,2850 --prefix morv_c70 --debug --out $O
sleep 2
python3 tools/iiif_lines.py --ark btv1b90601662 --canvas 70 --region 4200,400,700,3850 --prefix morv_c70margin --debug --out $O
