#!/usr/bin/env bash
# N4-NXS (4 Oct 2026): build the Noailles c510-516 sign-sorter page.  usage (repo root): bash ciphers/fr16142-noailles-constantinople-1571/sorter/build.sh WORKDIR
# Step 1 re-fetches the 7 Gallica canvases (7 requests, 2 s apart) and rebuilds the RUN2-NXATL atlas in WORKDIR (tolerant check).
set -euo pipefail
W=$(cd "$(dirname "$1")" && pwd)/$(basename "$1"); T=ciphers/fr16142-noailles-constantinople-1571; N=$T/run2/nxatl
bash $N/regen.sh "$W" --check
python3 $T/sorter/build_inputs.py "$W" "$W/sorter"
python3 -c "
import json,sys; w=sys.argv[1]; d=json.load(open(w+'/atlf/pages.json'))
json.dump({k: dict(v, image=v['image'] if v['image'].startswith('/') else w+'/'+v['image']) for k, v in d.items() if k.startswith('c51')},
          open(w+'/sorter/pages.json', 'w'))" "$W"
python3 tools/sign_sorter.py --atlas-topk "$W/sorter/topk.tsv" --pages "$W/sorter/pages.json" --marks "$W/atlf/marks.tsv" \
  --clusters $N/clusters.tsv --atlas $N/labels_clusterid.json --focus "$W/sorter/focus.tsv" \
  --focus-note "Where the two RUN2 readers split (NXTA c510; NXTB c516 and c515 L01-L20). Each reader position is placed on an atlas tile by its fraction of the line, so it is about +-2 tiles off: open the context view and check the neighbours. xN = how many columns the readers split on for that pair." \
  --title "Noailles 1574 Sign Sorter" \
  --lede "fr.16142 canvases 510-516, Noailles to the King, Pera, 6 July 1574: 9,863 tiles piled by family-atlas cluster (k=120, a deliberate over-split; pile names are cluster ids, not letters). Merge piles that are one sign, split piles that mix two, move single tiles, set aside non-signs and bad cuts." \
  --thumb 64 --tile-quality 55 --page-scale 0.45 --page-quality 45 \
  --out "$W/sorter/noailles_c510-516_sorter.html" --data-out "$W/sorter/data.json"
