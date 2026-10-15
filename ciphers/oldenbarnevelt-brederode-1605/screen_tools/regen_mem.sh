#!/bin/bash
# OBRED-MEM (15 Oct 2026): re-derive NL-HaNA 1.01.02 inv. 6019 scans 532-515 at 1000 px and 530 at 3000 px (20 requests incl. METS),
# the stride-1 screen for the Brederode memorie Maurits had deciphered (res. 1779, 11 Oct 1619). Images stay outside git.
# Run from this folder. Usage: bash screen_tools/regen_mem.sh OUTDIR
set -e; O=${1:-scratch_mem}; M=1ebb4182-2b80-4e37-a226-8b8c7e578c8b
python3 screen_tools/na_fetch.py $M $O 1000 $(seq 532 -1 515)
python3 screen_tools/na_fetch.py $M $O 3000 530
sha1sum $O/s05*_1000.jpg $O/s0530_3000.jpg
