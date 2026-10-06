#!/usr/bin/env bash
# R12A-BALS (6 Oct 2026): build the Baluze 170 f.228r-v owner sign sorter. usage (repo root): bash ciphers/baluze167-davaux-1637/sorter170/build.sh
# No network: reads the Gallica native regions already in images/crops/. Not published by a worker (account-3 orchestrator, db capability).
set -euo pipefail
T=ciphers/baluze167-davaux-1637/sorter170; mkdir -p $T/out
python3 $T/build_inputs.py > $T/build_inputs.log      # tools/sorter_recut.py tiles, pages/, cipher_lines.tsv
python3 $T/regroup.py > $T/regroup.log                # marks onto their signs, letter-sign pieces grouped, focus.tsv
python3 tools/sign_sorter.py --signs $T/signs.tsv --labels $T/labels.tsv --marks $T/marks.tsv --pages $T/pages --focus $T/focus.tsv \
  --auto-clusters 3 --cipher-lines $T/cipher_lines.tsv \
  --focus-note "The signs two machine readers and the reconciler could not settle on f.228 (D1-BAL170B): the crossed minim with a 4 (u4 or 4u), the q-shaped sign against the digit 9, the crossed double long s (ff), the three wave shapes (hook, wave, v), y+, h; then every 6, marked or not, because the curled top of this hand's 6 mimics an accent; then tiles no reader column lined up with. Your pick decides the sign." \
  --title "Baluze 170 f.228 Sign Sorter" \
  --lede "BnF Baluze 170 f.228r-v (Gallica btv1b90015040 canvases 239-240), Chavigny to d'Avaux, Amiens 25 Aug 1640: the 13 cipher lines cut one sign per tile from the ink; clear words are blanked. Piles start from the reconciled two-reader transcription (numbers are cut one digit per tile, the accent, diaeresis or bar going with the last digit: 6' is a 6 with an accent). Letter signs are named as this folder names them (u4, y+, h, q, ff, hook, wave, v, ll, m4, gam, g+, w, p, r); a letter sign wider than two and a half digits is cut in pieces, join them with Fix the cut. Merge piles that are one sign, split piles that mix two, move single tiles, set aside non-signs and bad cuts." \
  --thumb 80 --tile-quality 60 --page-quality 60 \
  --out $T/out/baluze170_f228_sorter.html --data-out $T/out/baluze170_f228_data.json | tee $T/preflight.txt
