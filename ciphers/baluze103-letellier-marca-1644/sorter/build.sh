#!/usr/bin/env bash
# R9-BAL103 (6 Oct 2026): build the f.50 owner sign sorter. usage (repo root): bash ciphers/baluze103-letellier-marca-1644/sorter/build.sh OUTDIR
# No network: reads the two Gallica native pages already in images/. Not published by a worker (account-3 orchestrator, db capability).
set -euo pipefail
O=$1; T=ciphers/baluze103-letellier-marca-1644; mkdir -p "$O"
python3 $T/sorter/recut.py                       # signs/labels (boxes padded 6 px, so SMALL's height floor is 18+12)/clusters/focus_r8b.tsv, pages/ (tools/sorter_recut.py)
python3 -c "import sys;sys.path.insert(0,'tools');import sorter_recut as s;print(s.small_pile('$T/sorter',focus='focus_r8b.tsv',min_h=30),'small tiles')"
python3 tools/sign_sorter.py --signs $T/sorter/signs.tsv --labels $T/sorter/labels_small.tsv --pages $T/sorter/pages \
  --focus $T/sorter/focus_r8b.tsv --auto-clusters 4 --cipher-lines $T/sorter/cipher_lines.tsv \
  --focus-note "The 28 tiles two machine readers and a third look-alike reader could not settle on f.50 (confusable pairs m/mm/mt, tt/venus, venus/q, x/xc/xs/xbar, 9/venus). Your pick decides the sign." \
  --title "Baluze 103 f.50 Sign Sorter" \
  --lede "BnF Baluze 103 f.50r-v (Gallica btv1b9001389d canvases 111-112), Le Tellier to Marca, April 1644: 32 cipher lines cut one sign per tile from the ink. Piles start from the current settled transcription (pile name = the sign name in Tomokiyo's 1644 table as this folder names it); tiles no reader column lined up with start in the pile their shape most often sits in. Numbers written as two digits (14, 21, 23) are often cut as two tiles: merge them back. SMALL holds dots and specks. Merge piles that are one sign, split piles that mix two, move single tiles, set aside non-signs and bad cuts." \
  --thumb 80 --tile-quality 60 --page-scale 1.0 --page-quality 60 \
  --out "$O/baluze103_f50_sorter.html" --data-out "$O/baluze103_f50_data.json"
