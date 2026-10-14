#!/bin/bash
# OBRED-6017E (14 Oct 2026): re-derive inv. 6017 scans 497-585 (those not = 1 mod 3; 60 scans, to the end) at 700 px and the
# 10 contact sheets (seed 6497). Run from this folder. Usage: bash screen_tools/regen_6017e.sh OUTDIR  (images stay outside git; 61 requests)
set -e; O=${1:-scratch_6017e}; I=images; M=b060ccbc-a7f8-4174-a34f-c25e5ff9e526
ORD=$(python3 -c "print(' '.join(str(i) for i in [i for i in range(497,586) if i%3!=1]))")
python3 screen_tools/na_fetch.py $M $O/i6017 700 $ORD
python3 screen_tools/contact_sheets.py $O/i6017 700 $O/sh $O/key.json 6497 $I/na_301_14_2016_p0031.jpg $I/na_101_02_6016_p0261.jpg $I/na_101_02_6016_p0187_1200.jpg $ORD
cmp $O/key.json $I/6017_screen_s9_sheetkey.json && echo "sheet key reproduces"
