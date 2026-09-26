#!/usr/bin/env bash
# Regenerate the images/ full-leaf renders removed on 26 Sept 2026 (bSALS, LANE B11) to shrink this
# folder under CLAUDE.md's 30 MB rule. Every one of these files is a plain Gallica IIIF fetch, URL
# recorded in images/manifest.json's `leaves` entries; the originals are still readable from git history
# (see NOTES.md section "bSALS: folder shrink (26 Sept 2026)" for the commit sha). Confirmed byte-identical
# regen for 2 of the 8 files (src_ark full native crop, f54v_ref1600.jpg) before deletion.
#
# Usage:
#   ./regen_images.sh page NAME     # re-fetch one full-leaf image by its images_manifest_full.tsv basename
#   ./regen_images.sh crop CROPNAME # re-cut one iiif_lines crop from its recorded parent + box
#   ./regen_images.sh all           # regenerate every deleted full-leaf image (8 files)
#
# Good-citizen rule: gallica.bnf.fr IIIF image API only, >= 2s between requests, browser User-Agent.
set -euo pipefail
cd "$(dirname "$0")"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

# name -> Gallica IIIF URL, from images/manifest.json's `leaves` entries (26 Sept 2026)
declare -A PAGE_URL=(
  [src_ark_12148_btv1b90600674_f55_4085_0_4086_5513.jpg]="https://gallica.bnf.fr/iiif/ark:/12148/btv1b90600674/f55/4085,0,4086,5513/full/0/native.jpg"
  [f54v_ref1600.jpg]="https://gallica.bnf.fr/iiif/ark:/12148/btv1b90600674/f56/pct:0,0,50,100/1600,/0/default.jpg"
  [f55r_ref1600.jpg]="https://gallica.bnf.fr/iiif/ark:/12148/btv1b90600674/f56/pct:50,0,50,100/1600,/0/default.jpg"
  [f55v_ref1600.jpg]="https://gallica.bnf.fr/iiif/ark:/12148/btv1b90600674/f57/pct:0,0,50,100/1600,/0/default.jpg"
  [f56r_ref1600.jpg]="https://gallica.bnf.fr/iiif/ark:/12148/btv1b90600674/f57/pct:50,0,50,100/1600,/0/default.jpg"
  [f56v_ref1600.jpg]="https://gallica.bnf.fr/iiif/ark:/12148/btv1b90600674/f58/pct:0,0,50,100/1600,/0/default.jpg"
  [f57r_ref1600.jpg]="https://gallica.bnf.fr/iiif/ark:/12148/btv1b90600674/f58/pct:50,0,50,100/1600,/0/default.jpg"
  [f57v_ref1600.jpg]="https://gallica.bnf.fr/iiif/ark:/12148/btv1b90600674/f59/pct:0,0,50,100/1600,/0/default.jpg"
)

fetch_page() {
  local name="$1"
  local url="${PAGE_URL[$name]:-}"
  [ -n "$url" ] || { echo "no recorded URL for $name" >&2; exit 1; }
  curl -sS -A "$UA" -o "images/$name" "$url"
  sleep 2
}

do_crop() {
  # cut one iiif_lines crop (images/manifest.json) from its parent image, already on disk
  local cropname="$1"
  python3 - "$cropname" <<'PYEOF'
import json, sys
from PIL import Image
cropname = sys.argv[1]
d = json.load(open('images/manifest.json'))
rec = next(e for e in d['iiif_lines'] if e['crop'] == cropname)
parent = f"images/{rec['source_file']}"
box = rec['box']
# leaves[].url for this source_file gives the crop's own top-left offset (x0 of the fetched region)
leaf = next(e for e in d['leaves'] if e.get('file', '').startswith(rec['source_file']))
url = leaf['url']
# e.g. ark:/.../f55/4085,0,4086,5513/full/... -> origin (4085,0)
region = url.split('/')[-4]
ox, oy = (int(v) for v in region.split(',')[:2])
local_box = (box[0]-ox, box[1]-oy, box[2]-ox, box[3]-oy)
im = Image.open(parent)
im.crop(local_box).save(f"images/{cropname}", quality=90)
print(f"cut {cropname} from {parent} local_box={local_box}")
PYEOF
}

case "${1:-}" in
  page) fetch_page "$2" ;;
  crop) do_crop "$2" ;;
  all)
    for name in "${!PAGE_URL[@]}"; do fetch_page "$name"; done
    ;;
  *)
    echo "usage: $0 {page NAME|crop CROPNAME|all}" >&2
    exit 1
    ;;
esac
