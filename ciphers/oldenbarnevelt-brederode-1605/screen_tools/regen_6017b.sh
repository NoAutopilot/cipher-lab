#!/bin/bash
# OBRED-6017B (14 Oct 2026): re-derive inv. 6017 scans 74-207 (those not = 1 mod 3; 90 scans) at 700 px, scan 80 at 1200 px, and the
# 15 contact sheets (seed 6074). Run from this folder. Usage: bash screen_tools/regen_6017b.sh OUTDIR  (images stay outside git; 92 requests)
set -e; O=${1:-scratch_6017b}; I=images; M=b060ccbc-a7f8-4174-a34f-c25e5ff9e526
ORD=$(python3 -c "print(' '.join(str(i) for i in range(74,208) if i%3!=1))")
python3 screen_tools/na_fetch.py $M $O/i6017 700 $ORD
python3 screen_tools/na_fetch.py $M $O/i6017 1200 80
python3 screen_tools/contact_sheets.py $O/i6017 700 $O/sh $O/key.json 6074 $I/na_301_14_2016_p0031.jpg $I/na_101_02_6016_p0261.jpg $I/na_101_02_6016_p0187_1200.jpg $ORD
cmp $O/key.json $I/6017_screen_s6_sheetkey.json && echo "sheet key reproduces"
