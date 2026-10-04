#!/usr/bin/env bash
# LONGLEE-SORTER (4 Oct 2026): build the f.101v sign-sorter page.  usage (repo root): bash ciphers/fr16106-vivonne-longlee-1579/sorter/build.sh OUTDIR
# No network: reads the Gallica native region already on disk (images/src_ark_12148_btv1b9009661v_f107_550_550_3800_5350.jpg).
set -euo pipefail
O=$1; T=ciphers/fr16106-vivonne-longlee-1579; mkdir -p "$O"
python3 $T/sorter/build_inputs.py
python3 tools/sign_sorter.py --signs $T/sorter/signs.tsv --labels $T/sorter/labels.tsv --pages $T/sorter/pages \
  --focus $T/sorter/focus.tsv --auto-clusters 4 \
  --focus-note "Where the two blind machine readers split most often (reader A / reader B). Tiles were cut from an ink profile and fitted to the readers' column count, so a tile can be one or two positions off its label: open the context view." \
  --title "Longlee 1580 Sign Sorter" \
  --lede "BnF fr.16107 f.101v (Gallica canvas 107), Saint-Gouard to the King, Madrid, 2 March 1580: 1,493 tiles from 33 cipher lines. Piles start from two blind machine readers who agreed on only 42% of signs: a plain name is a sign both read the same, a/c is a split, +1r a sign only one reader saw; lines 30-33 are unplaced. Pile names are shape labels, not letters. Merge piles that are one sign, split piles that mix two, move single tiles, set aside non-signs and bad cuts." \
  --thumb 80 --tile-quality 60 --page-scale 0.5 --page-quality 50 \
  --out "$O/longlee_f101v_sorter.html" --data-out "$O/longlee_f101v_data.json"
