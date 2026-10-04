#!/usr/bin/env bash
# ARM-SORTER (4 Oct 2026): build the shorthand-mark sorter page.  usage (repo root): bash ciphers/armstrong-madison-1808/sorter/build.sh OUTDIR
# No network: reads the NARA M34 roll 14 frames already on disk (images/M34-014-0030/0031/0033.jpg). Numerals are not on the page.
set -euo pipefail
O=$1; T=ciphers/armstrong-madison-1808; mkdir -p "$O"
python3 $T/sorter/segment_marks.py
python3 $T/sorter/cluster_marks.py --k 26
python3 tools/sign_sorter.py --signs $T/sorter/signs.tsv --labels $T/sorter/labels.tsv --pages $T/images \
  --focus $T/sorter/focus.tsv --auto-clusters 3 \
  --focus-note "Where the two transcriptions disagree on how many marks stand between two numbers (ciphertext_ms.txt vs codex glyphs.tsv), marks cut against the binding edge, and tiles that sit between two piles. Open the context view: a tile may be half a mark, or two." \
  --title "Armstrong 1808 Mark Sorter" \
  --lede "Armstrong to Madison, Paris, 20 February 1808 (NARA M34 roll 14, frames 0030, 0031, 0033): the shorthand marks written between the numbered groups, 263 tiles from 36 runs. Numbers are left off. Two transcriptions count these marks differently (218 vs 257, about 16%): your piles settle how many marks there are and which are the same sign. Pile names M01, M02 ... are machine shape groups, not values. Merge piles that are one sign, split piles that mix two, move single tiles, set aside non-marks and bad cuts (a tile that is half a mark, or two marks together)." \
  --thumb 72 --tile-quality 70 --page-scale 0.5 --page-quality 55 \
  --out "$O/armstrong1808_marks_sorter.html" --data-out "$O/armstrong1808_marks_data.json"
