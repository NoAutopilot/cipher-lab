#!/bin/sh
# MONL-CENSUS (20 Oct 2026): re-fetch the untracked overview images used for the Cipher 1/2 leaf census
# (census_cipher1.tsv) from openapi.bnf.fr (>= 1.5 s apart).
set -e
cd "$(dirname "$0")"; D=images/scratchcensus; mkdir -p $D
B=https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060724s
UA="cipher-lab research script (contact via repository)"
for c in 174 390 392 394; do curl -sS -A "$UA" -o $D/c${c}_full.jpg "$B/f$c/full/1400,/0/default.jpg"; sleep 1.5; done
