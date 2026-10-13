#!/bin/bash
# OBRED-11851B (13 Oct 2026): re-derive the 88 scans (+4 probes) and the 16 contact sheets. Run from this folder.
# Usage: bash screen_tools/regen_11851b.sh OUTDIR    (images stay outside git; >= 2.1 s between NA requests)
set -e; O=${1:-scratch_11851b}; I=images
python3 screen_tools/na_fetch.py 69557eee-2aae-4284-98ff-db14579daf50 $O/i11851 700 $(seq 701 733)
python3 screen_tools/na_fetch_map.py screen_tools/na_11852_iiif_map.json $O/i11852 700 1 40 80 120 160 $(seq 50 104)
python3 screen_tools/contact_sheets.py $O/i11851 700 $O/sh1 $O/key1.json 11852 $I/na_301_14_2016_p0031.jpg $I/na_101_02_6016_p0261.jpg $I/na_101_02_6016_p0187_1200.jpg $(seq 701 733)
python3 screen_tools/contact_sheets.py $O/i11852 700 $O/sh2 $O/key2.json 1605 $I/na_301_14_2016_p0031.jpg $I/na_101_02_6016_p0261.jpg $I/na_101_02_6016_p0187_1200.jpg $(seq 50 104)
cmp $O/key1.json $I/sg_11851_screen4_sheetkey.json && cmp $O/key2.json $I/sg_11852_screen1_sheetkey.json && echo "sheet keys reproduce"
