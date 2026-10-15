#!/bin/bash
# OBRED-6021 (15 Oct 2026): re-derive inv. 6021 scans 1,7,...,805 (stride 6; 135 scans) at 700 px and the 15 contact sheets
# (SHEET_SCANS=9, 4x3, seed 6021; sheets 1-13 were read). Run from this folder. Usage: bash screen_tools/regen_6021.sh OUTDIR  (images stay outside git; 136 requests)
# The flagged scan 379 at 1200 px: python3 screen_tools/na_fetch.py c82b1eb5-6946-4ca9-8082-f13c2ab5f078 OUTDIR/i6021 1200 379
set -e; O=${1:-scratch_6021}; I=images; M=c82b1eb5-6946-4ca9-8082-f13c2ab5f078
ORD=$(python3 -c "print(' '.join(str(i) for i in range(1,811,6)))")
python3 screen_tools/na_fetch.py $M $O/i6021 700 $ORD
SHEET_SCANS=9 python3 screen_tools/contact_sheets.py $O/i6021 700 $O/sh $O/key.json 6021 $I/na_301_14_2016_p0031.jpg $I/na_101_02_6016_p0261.jpg $I/na_101_02_6016_p0187_1200.jpg $ORD
cmp $O/key.json $I/6021_screen_sheetkey.json && echo "sheet key reproduces"
