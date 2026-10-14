#!/bin/bash
# OBRED-6017C (14 Oct 2026): re-derive inv. 6017 scans 209-351 (those not = 1 mod 3; 96 scans) at 700 px and the
# 16 contact sheets (seed 6209). Run from this folder. Usage: bash screen_tools/regen_6017c.sh OUTDIR  (images stay outside git; 97 requests)
set -e; O=${1:-scratch_6017c}; I=images; M=b060ccbc-a7f8-4174-a34f-c25e5ff9e526
ORD=$(python3 -c "print(' '.join(str(i) for i in [i for i in range(209,600) if i%3!=1][:96]))")
python3 screen_tools/na_fetch.py $M $O/i6017 700 $ORD
python3 screen_tools/contact_sheets.py $O/i6017 700 $O/sh $O/key.json 6209 $I/na_301_14_2016_p0031.jpg $I/na_101_02_6016_p0261.jpg $I/na_101_02_6016_p0187_1200.jpg $ORD
cmp $O/key.json $I/6017_screen_s7_sheetkey.json && echo "sheet key reproduces"
