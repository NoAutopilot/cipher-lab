#!/bin/sh
# SYL-NOM (13 Oct 2026): regenerate the nomenclator crops from the committed native regions (no network).
# Run from the repository root. Crops are not committed (folder size line); the source regions are.
D=ciphers/fr15575-syllabic-1592-95/images/fr3995; O=$D/nomen
SRC=$D/src_image_v3_ark_12148_btv1b525085665_f188_250_1600_3650_4455.jpg
python3 tools/iiif_lines.py --image $SRC --region 80,0,780,4455 --out $O --prefix nomc1 --lines-per-crop 11 --max-width 2400 --overlap 60 --debug
python3 tools/iiif_lines.py --image $SRC --region 790,0,930,4455 --out $O --prefix nomc2 --lines-per-crop 11 --max-width 2400 --overlap 60 --debug
python3 tools/iiif_lines.py --image $SRC --region 1690,0,930,4455 --out $O --prefix nomc3 --lines-per-crop 11 --max-width 2400 --overlap 60 --debug
python3 tools/iiif_lines.py --image $SRC --region 2610,0,1040,4455 --out $O --prefix nomc4 --lines-per-crop 11 --max-width 2400 --overlap 60 --debug
python3 tools/iiif_lines.py --image $D/src_image_v3_ark_12148_btv1b525085665_f188_3550_2450_1450_1500.jpg --region 250,0,1200,1500 --out $O --prefix nomr --centres 135,708,1300 --lines-per-crop 3 --max-width 2400 --debug
cp $D/src_image_v3_ark_12148_btv1b525085665_f188_5500_1800_1750_450.jpg $O/nomn_nulles.jpg
