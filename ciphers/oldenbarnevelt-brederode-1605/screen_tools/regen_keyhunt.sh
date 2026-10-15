#!/bin/bash
# OBRED-KEYHUNT (15 Oct 2026): re-derive NL-HaNA 1.01.02 inv. 6019 scans 533-548 and 558-565 at 1000 px (25 requests incl. METS),
# the stride-1 screen for the 1619 "instructie ende sleutel". Images stay outside git. Run from this folder. Usage: bash screen_tools/regen_keyhunt.sh OUTDIR
set -e; O=${1:-scratch_keyhunt}; M=1ebb4182-2b80-4e37-a226-8b8c7e578c8b
python3 screen_tools/na_fetch.py $M $O 1000 $(seq 548 -1 533) $(seq 558 565)
sha1sum $O/s05*_1000.jpg
