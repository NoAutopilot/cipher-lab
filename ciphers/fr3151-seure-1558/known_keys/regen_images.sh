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
# D1-SEURE (6 Oct 2026): Morvilliers cipher block re-cut with eye-set centres, slope following and neighbour masking (no network)
python3 tools/iiif_lines.py --image $O/src_ark_12148_btv1b90601662_f70_4800_700_2950_2850.jpg --centres 90,195,300,400,520,635,760,870,990,1130,1260,1390,1520,1650,1780,1910,2040,2190,2320,2450,2590,2730 --follow-slope 300 --mask-neighbours --top-margin 20 --bottom-margin 15 --max-width 1500 --overlap 0 --prefix mv --debug --out $O/mv
# R12A-SEUT (6 Oct 2026): Tournon cipher block (canvas 26 region above) re-cut into 13 lines x 2 non-overlapping halves (no network);
# L13 re-cut without slope following (its slope fit drifted -138 px onto L12), right half empty and dropped
python3 tools/iiif_lines.py --image $O/src_ark_12148_btv1b90601662_f26_1150_600_3000_1650.jpg --centres 94,205,338,458,582,706,829,973,1082,1199,1326,1452,1577 --follow-slope 300 --mask-neighbours --top-margin 20 --bottom-margin 15 --max-width 1500 --overlap 0 --prefix tv --debug --out $O/tv
T=$(mktemp -d)
python3 tools/iiif_lines.py --image $O/src_ark_12148_btv1b90601662_f26_1150_600_3000_1650.jpg --centres 1452,1590 --mask-neighbours --top-margin 20 --bottom-margin 15 --max-width 1500 --overlap 0 --prefix tvx --out $T
cp $T/tvx_L02_s1.jpg $O/tv/tv_L13_s1.jpg; rm -f $O/tv/tv_L13_s2.jpg; rm -rf $T
python3 ciphers/fr3151-seure-1558/known_keys/tournon/build_sheet.py
