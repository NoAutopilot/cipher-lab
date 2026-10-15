#!/bin/bash
# HEID-1621B (15 Oct 2026): re-derive inv. 6021 scans 361-397 at 700 px, 374-376 at 1200 px and the 5 contact sheets (seed 16211).
# Run from the target folder. Usage: bash heid1621/regen_heid1621b.sh OUTDIR  (images stay outside git; 41 service.archief.nl requests)
set -e; O=${1:-scratch_heidb}; I=images; M=c82b1eb5-6946-4ca9-8082-f13c2ab5f078
python3 screen_tools/na_fetch.py $M $O/i6021 700 $(seq 361 397)
python3 screen_tools/na_fetch.py $M $O/i6021 1200 374 375 376
SHEET_SCANS=9 python3 screen_tools/contact_sheets.py $O/i6021 700 $O/sh $O/key.json 16211 $I/na_301_14_2016_p0031.jpg $I/na_101_02_6016_p0261.jpg $I/na_101_02_6016_p0187_1200.jpg $(seq 361 397)
cmp $O/key.json $I/heid1621b_sheetkey.json && echo "sheet key reproduces"
