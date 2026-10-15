#!/bin/bash
# HEID-1621F (15 Oct 2026): re-derive inv. 6021 scans 398-451 at 700 px, scans 423/424 at 1200 px and the 6 contact sheets
# (seeds 16216, 16217). Run from ciphers/oldenbarnevelt-brederode-1605. Usage: bash ../brederode-heidelberg-1621/heid1621f/regen_heid1621f.sh OUTDIR
# (images stay outside git; 57 service.archief.nl requests at >= 3.1 s; take/release lines in ROOM.md first)
set -e; O=${1:-scratch_heidf}; I=images; M=c82b1eb5-6946-4ca9-8082-f13c2ab5f078
C="$I/na_301_14_2016_p0031.jpg $I/na_101_02_6016_p0261.jpg $I/na_101_02_6016_p0187_1200.jpg"
python3 screen_tools/na_fetch.py $M $O/i6021 700 $(seq 398 451)
python3 screen_tools/na_fetch.py $M $O/i6021 1200 423 424
SHEET_SCANS=9 python3 screen_tools/contact_sheets.py $O/i6021 700 $O/sh1 $O/key1.json 16216 $C $(seq 398 424)
SHEET_SCANS=9 python3 screen_tools/contact_sheets.py $O/i6021 700 $O/sh2 $O/key2.json 16217 $C $(seq 425 451)
python3 -c "import json,sys;k=json.load(open('../brederode-heidelberg-1621/heid1621f/sheetkey.json'));assert k['batch1_seed16216']==json.load(open('$O/key1.json')) and k['batch2_seed16217']==json.load(open('$O/key2.json'));print('sheet keys reproduce')"
