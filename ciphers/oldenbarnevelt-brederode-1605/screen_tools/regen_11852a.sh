#!/bin/bash
# OBRED-11852A (13 Oct 2026): re-derive inv. 11852 scans 2-49 at 700 px and the 8 contact sheets (seed 1602). Run from this folder.
# Usage: bash screen_tools/regen_11852a.sh OUTDIR    (images stay outside git; >= 2.1 s between NA requests; 48 requests)
set -e; O=${1:-scratch_11852a}; I=images
python3 screen_tools/na_fetch_map.py screen_tools/na_11852_iiif_map.json $O/i11852 700 $(seq 2 49)
python3 screen_tools/contact_sheets.py $O/i11852 700 $O/sh3 $O/key3.json 1602 $I/na_301_14_2016_p0031.jpg $I/na_101_02_6016_p0261.jpg $I/na_101_02_6016_p0187_1200.jpg $(seq 2 49)
cmp $O/key3.json $I/sg_11852_screen2_sheetkey.json && echo "sheet key reproduces"
