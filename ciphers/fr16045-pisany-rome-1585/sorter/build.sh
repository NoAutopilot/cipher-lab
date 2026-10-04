#!/usr/bin/env bash
# PISANY-SORTER (4 Oct 2026): build the f.75 sign-sorter page.  usage (repo root): bash ciphers/fr16045-pisany-rome-1585/sorter/build.sh OUTDIR
# No network: reads the Gallica native region already on disk (images/src_ark_12148_btv1b9060906j_f156_680_1830_3060_3520.jpg).
set -euo pipefail
# SORTER-PAGEVIEW (4 Oct 2026): --region adds the "Whole page" larger view and writes <out stem>_region.jpg beside the page
# (publish it with the page as a supporting file). Rebuilding re-runs recut.py, which rewrites signs.tsv: re-run
# tools/sorter_apply_recuts.py afterwards if recuts were applied (SORTER-NUDGE).
O=$1; T=ciphers/fr16045-pisany-rome-1585; mkdir -p "$O"
# PIS-RECUT (4 Oct 2026): deskewed strips, one tile per sign cut from its own ink (recut.py; the v2 cut is signs_v2.tsv,
# made by build_inputs.py + tighten_tiles.py, kept for the record and no longer run here).
python3 $T/sorter/recut.py
python3 $T/sorter/small_pile.py
python3 -c "import sys;L=open(sys.argv[1]).read().split(chr(10));o=[]
for l in [x for x in L if x][:30]:
  sid,cap=l.split(chr(9),1); o.append(sid+chr(9)+cap.split(';')[0].split(':',1)[-1].strip()+'. Right pile, another sign, or a bad cut?')
open(sys.argv[2],'w').write(chr(10).join(o)+chr(10))" $T/sorter/focus.tsv $T/sorter/focus30.tsv   # 30 most useful, one-line captions (owner: efficient)
python3 tools/sign_sorter.py --signs $T/sorter/signs.tsv --labels $T/sorter/labels_small.tsv --pages $T/sorter/pages \
  --focus $T/sorter/focus30.tsv --auto-clusters 4 \
  --focus-note "Tiles the machine readers did not line up with, most frequent shapes first. Each started in the pile its shape most often sits in." \
  --title "Pisany 1585 Sign Sorter" \
  --lede "BnF fr.16045 f.75r (Gallica canvas 156), Pisany to Henry III, Rome, 17 June 1585: 1,290 tiles from 22 straightened cipher lines, one sign per tile. Piles start from two blind machine readers who agreed on only 57% of signs: a plain name (S15) is a sign both read the same, S10/S41 a split, +1r a sign only one reader saw. Pile names are cells of the published 1585 table, shape labels, not letters. Merge piles that are one sign, split piles that mix two, move single tiles, set aside non-signs and bad cuts." \
  --thumb 80 --tile-quality 60 --page-scale 0.5 --page-quality 50 \
  --region $T/sorter/region.json \
  --out "$O/pisany_f75_sorter.html" --data-out "$O/pisany_f75_data.json"
