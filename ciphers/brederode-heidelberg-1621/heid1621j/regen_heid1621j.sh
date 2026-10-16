#!/bin/bash
# HEID-1621J (16 Oct 2026): re-derive inv. 6022 scans and contact sheets. Run from ciphers/oldenbarnevelt-brederode-1605.
# Usage: bash ../brederode-heidelberg-1621/heid1621j/regen_heid1621j.sh OUTDIR   (129 service.archief.nl requests at >= 3.1 s;
# take/release lines in ROOM.md first; images stay outside git; compare sha1s with images/manifest.json heid_6022j)
set -e; O=${1:-scratch_heidj}; I=images; M=412b1414-afa2-42fe-b56d-2b5f705e5005
C="$I/na_301_14_2016_p0031.jpg $I/na_101_02_6016_p0261.jpg $I/na_101_02_6016_p0187_1200.jpg"
python3 screen_tools/na_fetch.py $M $O/i6022 700 40 80 120 160 200 $(seq 165 272) $(seq 152 164 | grep -v 160)
python3 screen_tools/na_fetch.py $M $O/i6022 1200 166 167 171 181
SHEET_SCANS=9 python3 screen_tools/contact_sheets.py $O/i6022 700 $O/sh1 $O/key1.json 16220 $C $(seq 165 218)
SHEET_SCANS=9 python3 screen_tools/contact_sheets.py $O/i6022 700 $O/sh2 $O/key2.json 16221 $C $(seq 219 272)
SHEET_SCANS=9 python3 screen_tools/contact_sheets.py $O/i6022 700 $O/sh3 $O/key3.json 16222 $C $(seq 152 164 | grep -v 160)
