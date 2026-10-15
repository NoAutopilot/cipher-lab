#!/bin/bash
# OBRED-552 (15 Oct 2026): re-derive NL-HaNA 1.01.02 inv. 6019 scans 552-555 at 5000 px (5 requests incl. METS) and the one whole-line
# crop of 555 L15 that the two blind passes read. Images stay outside git. Run from this folder. Usage: bash screen_tools/regen_552.sh OUTDIR
set -e; O=${1:-scratch_552}; M=1ebb4182-2b80-4e37-a226-8b8c7e578c8b
python3 screen_tools/na_fetch.py $M $O 5000 552 553 554 555
python3 ../../tools/iiif_lines.py --image $O/s0555_5000.jpg --out $O/c555L15 --region 3060,2540,880,160 --prefix s555L15 --distance 200 --prominence 10 --debug
sha1sum $O/s055[2345]_5000.jpg
