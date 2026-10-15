#!/bin/bash
# OBRED-6019B (15 Oct 2026): re-derive inv. 6019 stride-3 scans 514,517,...,649 (46 scans; 47 requests with the METS) at 700 px and
# rebuild all 25 OBRED-6019 sheets with blank placeholders for scans 1-511 (already read), so the seed-6019 shuffle and the sheet key
# reproduce byte-identical without anyone opening the key; only sheets 20-25 are real. Run from this folder.
# Usage: bash screen_tools/regen_6019b.sh OUTDIR   (images stay outside git)
set -e; O=${1:-scratch_6019b}; I=images; M=1ebb4182-2b80-4e37-a226-8b8c7e578c8b
ALL=$(python3 -c "print(' '.join(str(i) for i in range(1,650,3)))")
NEW=$(python3 -c "print(' '.join(str(i) for i in range(514,650,3)))")
python3 screen_tools/na_fetch.py $M $O/i6019 700 $NEW
python3 - "$O/i6019" <<'PY'
import sys, os
from PIL import Image
d = sys.argv[1]
for o in range(1, 512, 3):
    f = os.path.join(d, f"s{o:04d}_700.jpg")
    if not os.path.exists(f): Image.new("RGB", (700, 900), "white").save(f)
PY
SHEET_SCANS=9 python3 screen_tools/contact_sheets.py $O/i6019 700 $O/sh $O/key.json 6019 $I/na_301_14_2016_p0031.jpg $I/na_101_02_6016_p0261.jpg $I/na_101_02_6016_p0187_1200.jpg $ALL
cmp $O/key.json $I/6019_screen_sheetkey.json && echo "sheet key reproduces"
