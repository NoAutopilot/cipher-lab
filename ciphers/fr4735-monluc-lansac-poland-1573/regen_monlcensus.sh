#!/bin/sh
# MONL-CENSUS (20 Oct 2026): re-fetch the untracked overview images used for the Cipher 1/2 leaf census
# (census_cipher1.tsv) from openapi.bnf.fr (>= 1.5 s apart).
set -e
cd "$(dirname "$0")"; D=images/scratchcensus; mkdir -p $D
B=https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060724s
UA="cipher-lab research script (contact via repository)"
for c in 174 390 392 394; do curl -sS -A "$UA" -o $D/c${c}_full.jpg "$B/f$c/full/1400,/0/default.jpg"; sleep 1.5; done
# MONL-KING (20 Oct 2026): overviews c256/c257 (f.132), c314 (f.165), c316/c317 (f.166r-v, aid item 66 "un dechiffrement",
# 2 May 1573) at 1000 px, and f.166r-v at 2800 px, into images/scratchking/. (Five region requests with a malformed path 404'd.)
K=images/scratchking; mkdir -p $K
for c in 256 257 314 316 317; do curl -sS -A "$UA" -o $K/c${c}_1000.jpg "$B/f$c/full/1000,/0/default.jpg"; sleep 1.6; done
for c in 316 317; do curl -sS -A "$UA" -o $K/c${c}_2800.jpg "$B/f$c/full/2800,/0/default.jpg"; sleep 1.6; done
