#!/usr/bin/env bash
# PISANY-SORTER (4 Oct 2026): build the f.75 sign-sorter page.  usage (repo root): bash ciphers/fr16045-pisany-rome-1585/sorter/build.sh OUTDIR
# No network: reads the Gallica native region already on disk (images/src_ark_12148_btv1b9060906j_f156_680_1830_3060_3520.jpg).
set -euo pipefail
O=$1; T=ciphers/fr16045-pisany-rome-1585; mkdir -p "$O"
python3 $T/sorter/build_inputs.py
python3 $T/sorter/tighten_tiles.py
python3 tools/sign_sorter.py --signs $T/sorter/signs_tight.tsv --labels $T/sorter/labels.tsv --pages $T/sorter/pages \
  --focus $T/sorter/focus.tsv --auto-clusters 4 \
  --focus-note "Where the two blind machine readers split, the four look-alike groups both named first (S15/S40/S13/S61, S10/S41/S02, S36/S42/S23, S46/S48/S25). Tiles were cut from an ink profile and fitted to the readers' column count, so a tile can be one or two positions off its label: open the context view. The lines slope steeply down to the right." \
  --title "Pisany 1585 Sign Sorter" \
  --lede "BnF fr.16045 f.75r (Gallica canvas 156), Pisany to Henry III, Rome, 17 June 1585: 1,115 tiles from 22 cipher lines. Piles start from two blind machine readers who agreed on only 57% of signs: a plain name (S15) is a sign both read the same, S10/S41 a split, +1r a sign only one reader saw. Pile names are cells of the published 1585 table, shape labels, not letters. Merge piles that are one sign, split piles that mix two, move single tiles, set aside non-signs and bad cuts." \
  --thumb 80 --tile-quality 60 --page-scale 0.5 --page-quality 50 \
  --out "$O/pisany_f75_sorter.html" --data-out "$O/pisany_f75_data.json"
