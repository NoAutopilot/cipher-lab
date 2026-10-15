#!/bin/bash
# OBRED-6020 (15 Oct 2026): re-derive inv. 6020 scans 1,7,...,601 (stride 6; 101 scans) at 700 px and the 12 contact sheets
# (SHEET_SCANS=9, 4x3, seed 6020; sheets 1-11 were read). Run from this folder. Usage: bash screen_tools/regen_6020.sh OUTDIR  (images stay outside git; 102 requests)
set -e; O=${1:-scratch_6020}; I=images; M=6b71330d-279e-4fe8-904b-01493a2c93d1
ORD=$(python3 -c "print(' '.join(str(i) for i in range(1,605,6)))")
python3 screen_tools/na_fetch.py $M $O/i6020 700 $ORD
SHEET_SCANS=9 python3 screen_tools/contact_sheets.py $O/i6020 700 $O/sh $O/key.json 6020 $I/na_301_14_2016_p0031.jpg $I/na_101_02_6016_p0261.jpg $I/na_101_02_6016_p0187_1200.jpg $ORD
cmp $O/key.json $I/6020_screen_sheetkey.json && echo "sheet key reproduces"
