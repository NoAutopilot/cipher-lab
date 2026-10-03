#!/usr/bin/env bash
# Regenerate image files for ciphers/na-suriname-map-1781 from their Nationaal Archief
# (service.archief.nl) IIIF / default-image sources, or from a regenerated parent file.
# Written 2 Oct 2026 (GAPS7, account-4) for the AX2-SHRINK-shape shrink of images/.
# images_manifest_full.tsv lists every file the folder has carried, its sha1, its recipe
# kind and which NOTES/glyphs line cites it.
#
# Usage:
#   ./regen_images.sh NAME [OUTDIR]   # regenerate one file (basename under images/), default OUTDIR images
#   ./regen_images.sh list            # show every recipe
#   ./regen_images.sh all [OUTDIR]    # every recipe, in order (parents before children)
#
# Recipe kinds:
#   iiif   INVNR REGION SIZE      service.archief.nl IIIF image API, <base>/<REGION>/<SIZE>/0/default.jpg
#                                 (byte-identical: tested 2 Oct 2026 on a sample, see NOTES.md GAPS7)
#   default INVNR                 the item's default_full_url (capped at 5000 px by the server)
#   pil    PARENT BOX|WIDTH       local PIL crop (x0,y0,x1,y1) or downscale to WIDTH of a parent file,
#                                 saved JPEG q90: same pixels region and dimensions, not byte-identical
#   lines  PARENT                 the tools/iiif_lines.py command recorded in images/manifest.json for
#                                 that parent (crops_2038/, crops_2042/, and the uncommitted crops_2039*)
# Not regenerable from a recipe (no box or URL recorded by the worker that made them):
#   images/strips/*.png (64 local upscaled crops of the 2007A legend blocks, added at commit
#   fc921145c1f2da5eef74c28edd0f69ca46dc1434); 63 were uncited and deleted on 2 Oct 2026 --
#   `git show fc921145:ciphers/na-suriname-map-1781/images/strips/<name>.png > <name>.png` restores one.
#   The 2007A/2039/2046/2061/2076/2078 VX-CS04/RD03 crops and overviews of 25 Sept 2026: kept in the tree.
# Good-citizen rule: one service.archief.nl request at a time, >= 1.5 s apart.
set -euo pipefail
cd "$(dirname "$0")"
UA="cipher-lab research script (contact via repository)"

recipes() { cat <<'R'
2038_overview.jpg	iiif	4.VEL 2038	full	2800,
2040_overview.jpg	iiif	4.VEL 2040	full	2800,
2042_overview.jpg	iiif	4.VEL 2042	full	2800,
2045A_overview.jpg	iiif	4.VEL 2045A	full	2800,
2038_legend_native.jpg	iiif	4.VEL 2038	8400,7540,2360,3380	full
2042_legend_native.jpg	iiif	4.VEL 2042	4590,4010,1390,990	full
2039_legend_native.jpg	iiif	4.VEL 2039	780,980,2100,2800	full
2039_legend_right_native.jpg	iiif	4.VEL 2039	2800,980,1300,2800	full
2039_remarque_native.jpg	iiif	4.VEL 2039	1180,6760,2500,800	full
2061_battery_legend_native.jpg	iiif	4.VEL 2061	2800,820,2300,900	full
2007a_nota_af_block.jpg	iiif	4.VEL 2007A	3900,2550,2300,1050	full
2007a_remarque_af_block.jpg	iiif	4.VEL 2007A	300,5800,2500,900	full
2007b_full.jpg	default	4.VEL 2007B
2077_full.jpg	default	4.VEL 2077
2007b_overview.jpg	pil	2007b_full.jpg	1600
2077_legend_5000.jpg	pil	2077_full.jpg	3250,60,5000,700
2039_cartouche_word2_native.jpg	pil	2039_cartouche.jpg	822,135,920,222
crops_2038	lines	2038_legend_native.jpg
crops_2042	lines	2042_legend_native.jpg
R
}

field() { python3 - "$1" "$2" <<'PY'
import json, sys
inv, key = sys.argv[1], sys.argv[2]
for it in json.load(open('images/manifest.json'))['items']:
    if it['invnr'] == inv:
        v = it.get(key, '')
        print(v[:-len('/info.json')] if key == 'iiif_info' else v); break
PY
}

regen() {
  local name="$1" out="${2:-images}" line kind a b c
  line=$(recipes | awk -F'\t' -v n="$name" '$1==n')
  [ -n "$line" ] || { echo "no recipe for $name (see header: strips are restored from git history)" >&2; return 1; }
  IFS=$'\t' read -r _ kind a b c <<<"$line"
  mkdir -p "$out"
  case "$kind" in
    iiif)    curl -sSf -A "$UA" -o "$out/$name" "$(field "$a" iiif_info)/$b/$c/0/default.jpg"; sleep 1.5 ;;
    default) curl -sSfL -A "$UA" -o "$out/$name" "$(field "$a" default_full_url)"; sleep 1.5 ;;
    pil)     python3 - "images/$a" "$out/$name" "$b" <<'PY'
import sys
from PIL import Image
src, dst, spec = sys.argv[1:4]
im = Image.open(src)
if ',' in spec:
    im = im.crop(tuple(int(v) for v in spec.split(',')))
else:
    w = int(spec); im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
im.convert('RGB').save(dst, quality=90)
PY
             ;;
    lines)   case "$name" in
               crops_2038) python3 ../../tools/iiif_lines.py --image images/2038_legend_native.jpg --out "$out/crops_2038" \
                             --prefix leg2038 --region 60,40,1950,3240 --distance 40 --prominence 20 --lines-per-crop 5 --debug ;;
               crops_2042) python3 ../../tools/iiif_lines.py --image images/2042_legend_native.jpg --out "$out/crops_2042" \
                             --prefix leg2042 --region 110,110,1155,760 --prominence 20 --distance 40 --lines-per-crop 20 --top-margin 60 --debug ;;
             esac ;;
  esac
  echo "regenerated $out/$name ($kind)"
}

case "${1:-}" in
  list) recipes ;;
  all)  recipes | cut -f1 | while read -r n; do regen "$n" "${2:-images}"; done ;;
  ""|-h|--help) sed -n 2,27p "$0" ;;
  *)    regen "$1" "${2:-images}" ;;
esac
