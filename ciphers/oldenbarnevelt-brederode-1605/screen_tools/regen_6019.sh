#!/bin/bash
# OBRED-6019 (15 Oct 2026): re-derive inv. 6019 scans 1,4,...,649 (stride 3; 217 scans) at 700 px and the 25 contact sheets
# (SHEET_SCANS=9, 4x3, seed 6019; sheets 1-19 were read). Run from this folder. Usage: bash screen_tools/regen_6019.sh OUTDIR  (images stay outside git; 218 requests)
set -e; O=${1:-scratch_6019}; I=images; M=1ebb4182-2b80-4e37-a226-8b8c7e578c8b
ORD=$(python3 -c "print(' '.join(str(i) for i in range(1,650,3)))")
python3 screen_tools/na_fetch.py $M $O/i6019 700 $ORD
SHEET_SCANS=9 python3 screen_tools/contact_sheets.py $O/i6019 700 $O/sh $O/key.json 6019 $I/na_301_14_2016_p0031.jpg $I/na_101_02_6016_p0261.jpg $I/na_101_02_6016_p0187_1200.jpg $ORD
cmp $O/key.json $I/6019_screen_sheetkey.json && echo "sheet key reproduces"
