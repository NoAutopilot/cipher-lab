# SHERWOOD-CELLS, 20 Oct 2026: Entick line bands, centres from book/entick_lines.tsv (the decode_entick grid). Run from the target folder.
python3 ../../tools/iiif_lines.py --image cells/pages/p360.png --region 0,1046,722,164 --out cells/crops/p360c1 --prefix p360c1_l31-35 --lines-per-crop 9 --centres 17,49,82,114,147
python3 ../../tools/iiif_lines.py --image cells/pages/p360.png --region 712,1047,698,164 --out cells/crops/p360c2 --prefix p360c2_l31-35 --lines-per-crop 9 --centres 17,49,82,114,147
python3 ../../tools/iiif_lines.py --image cells/pages/p165.png --region 0,410,662,162 --out cells/crops/p165c1 --prefix p165c1_l11-15 --lines-per-crop 9 --centres 17,49,81,113,145
python3 ../../tools/iiif_lines.py --image cells/pages/p165.png --region 652,384,758,162 --out cells/crops/p165c2 --prefix p165c2_l11-15 --lines-per-crop 9 --centres 17,49,81,113,145
python3 ../../tools/iiif_lines.py --image cells/pages/p53.png --region 0,1088,702,162 --out cells/crops/p53c1 --prefix p53c1_l33-37 --lines-per-crop 9 --centres 17,49,81,113,145
python3 ../../tools/iiif_lines.py --image cells/pages/p53.png --region 692,1087,718,163 --out cells/crops/p53c2 --prefix p53c2_l33-37 --lines-per-crop 9 --centres 17,49,81,114,146
python3 ../../tools/iiif_lines.py --image cells/pages/p412.png --region 0,1045,712,228 --out cells/crops/p412c1 --prefix p412c1_l31-37 --lines-per-crop 9 --centres 17,49,82,114,147,179,211
python3 ../../tools/iiif_lines.py --image cells/pages/p412.png --region 702,1054,708,229 --out cells/crops/p412c2 --prefix p412c2_l31-37 --lines-per-crop 9 --centres 17,49,82,114,147,179,212
python3 ../../tools/iiif_lines.py --image cells/pages/p225.png --region 0,550,671,229 --out cells/crops/p225c1 --prefix p225c1_l15-21 --lines-per-crop 9 --centres 17,49,82,114,147,179,212
python3 ../../tools/iiif_lines.py --image cells/pages/p225.png --region 661,551,749,229 --out cells/crops/p225c2 --prefix p225c2_l15-21 --lines-per-crop 9 --centres 17,50,82,114,147,179,212
