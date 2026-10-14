#!/bin/bash
# OBRED-6018 (14 Oct 2026): re-derive inv. 6018 scans 1,4,...,577 (stride 3; 193 scans) at 700 px and the 22 contact sheets
# (SHEET_SCANS=9, 4x3, seed 6018). Run from this folder. Usage: bash screen_tools/regen_6018.sh OUTDIR  (images stay outside git; 194 requests)
set -e; O=${1:-scratch_6018}; I=images; M=8ab6959a-fc81-425b-8591-86e332ad1454
ORD=$(python3 -c "print(' '.join(str(i) for i in range(1,578,3)))")
python3 screen_tools/na_fetch.py $M $O/i6018 700 $ORD
SHEET_SCANS=9 python3 screen_tools/contact_sheets.py $O/i6018 700 $O/sh $O/key.json 6018 $I/na_301_14_2016_p0031.jpg $I/na_101_02_6016_p0261.jpg $I/na_101_02_6016_p0187_1200.jpg $ORD
cmp $O/key.json $I/6018_screen_sheetkey.json && echo "sheet key reproduces"
