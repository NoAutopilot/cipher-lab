#!/bin/bash
# OBRED-549 (15 Oct 2026): re-derive NL-HaNA 1.01.02 inv. 6019 scans 549-551 at 5000 px (4 requests incl. METS) and the two eye crops
# (550 docket, 549 opening lines). Images stay outside git. Run from this folder. Usage: bash screen_tools/regen_549.sh OUTDIR
set -e; O=${1:-scratch_549}; M=1ebb4182-2b80-4e37-a226-8b8c7e578c8b
python3 screen_tools/na_fetch.py $M $O 5000 549 550 551
python3 -c "
from PIL import Image
Image.open('$O/s0550_5000.jpg').crop((3200,150,4600,700)).save('$O/d550.jpg')
Image.open('$O/s0549_5000.jpg').crop((650,380,2600,1300)).save('$O/t549.jpg')"
sha1sum $O/s05[45][901]_5000.jpg
