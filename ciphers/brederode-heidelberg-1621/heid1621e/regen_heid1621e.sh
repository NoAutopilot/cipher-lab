#!/bin/bash
# HEID-1621E (15 Oct 2026): re-derive inv. 6021 scans 4,10,...,358 and 400,...,802 at 700 px, scan 58 at 1200 px, and the 15 contact
# sheets (seed 16215). Run from ciphers/oldenbarnevelt-brederode-1605. Usage: bash ../brederode-heidelberg-1621/heid1621e/regen_heid1621e.sh OUTDIR
# (images stay outside git; 130 service.archief.nl requests at >= 3.1 s; take/release lines in ROOM.md first)
set -e; O=${1:-scratch_heide}; I=images; M=c82b1eb5-6946-4ca9-8082-f13c2ab5f078
python3 screen_tools/na_fetch.py $M $O/i6021 700 $(seq 4 6 358) $(seq 400 6 802)
python3 screen_tools/na_fetch.py $M $O/i6021 1200 58
SHEET_SCANS=9 python3 screen_tools/contact_sheets.py $O/i6021 700 $O/sh $O/key.json 16215 $I/na_301_14_2016_p0031.jpg $I/na_101_02_6016_p0261.jpg $I/na_101_02_6016_p0187_1200.jpg $(seq 4 6 358) $(seq 400 6 802)
cmp $O/key.json ../brederode-heidelberg-1621/heid1621e/sheetkey.json && echo "sheet key reproduces"
