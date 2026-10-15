#!/bin/bash
# OBRED-OCT2 (15 Oct 2026): re-derive NL-HaNA 1.01.02 inv. 6019 scans 528-530 at 3000 px (4 requests incl. METS), the 2 Oct 1619
# Brederode letter of res. 1779, read for the memorie and the cipher. Images stay outside git. Run from this folder.
# Usage: bash screen_tools/regen_oct2.sh OUTDIR
set -e; O=${1:-scratch_oct2}; M=1ebb4182-2b80-4e37-a226-8b8c7e578c8b
python3 screen_tools/na_fetch.py $M $O 3000 528 529 530
sha1sum $O/s05*_3000.jpg
