#!/bin/sh
# SYL-31 (13 Oct 2026): regenerate the key no.31 crops (fr.3995 f.62r, canvas f126). Run from the repository root.
# Neither the native region nor the crops are committed (folder size line, 30 MB); the first line refetches the region
# once from openapi.bnf.fr (IIIF v3) if it is not on disk, the rest cut from it with no network.
D=ciphers/fr15575-syllabic-1592-95/images/fr3995/no31
SRC=$D/src_image_v3_ark_12148_btv1b525085665_f126_1250_1700_2750_4457.jpg
[ -f $SRC ] || python3 tools/iiif_lines.py --ark btv1b525085665 --canvas 126 --iiif-host openapi --region 1250,1700,2750,4457 --out $D --prefix n31 --dry-run
python3 tools/iiif_lines.py --image $SRC --region 0,0,1800,3220 --out $D --prefix n31grid --lines-per-crop 5 --max-width 2400 --overlap 60 --debug
python3 tools/iiif_lines.py --image $SRC --region 1810,2010,940,1480 --out $D --prefix n31leg --lines-per-crop 7 --max-width 2400 --overlap 40 --debug
python3 tools/iiif_lines.py --image $SRC --region 0,3210,1200,1200 --out $D --prefix n31let --lines-per-crop 5 --max-width 2400 --overlap 40 --debug
