#!/usr/bin/env bash
# Regenerate full-page renders and line crops for ciphers/malsburg-hessen-1636 that were
# removed from the working tree on 26 Sept 2026 (bMALS, LANE B10) to stay under CLAUDE.md's
# 30 MB-per-folder rule. The originals are still readable from git history (see NOTES.md's
# "bMALS: folder shrink (26 Sept 2026)" section for the commit sha) and, for full pages, are
# also byte-identically re-fetchable from HCPortal by the URL/sha1 recorded in
# images/manifest.json and images_manifest_full.tsv.
#
# Usage:
#   ./regen_images.sh page FOLIO              # re-fetch one full page from HCPortal (e.g. hstam_4_h_1411_0004)
#   ./regen_images.sh crop DIR CROPNAME       # re-cut one line crop from its recorded box (e.g. crop 0016 hstam_4_h_1411_0016_L01.jpg)
#   ./regen_images.sh all                     # do every file named in images_manifest_full.tsv
#
# Good-citizen rule: one api.hcportal.eu request at a time, >=1.5s apart, browser User-Agent
# and header `Origin: https://crypto.hcportal.eu` (NOTES.md item 4, confirmed 26 Sept 2026 for
# this host's API; the media host answers the same way).
set -euo pipefail
cd "$(dirname "$0")"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
ORIGIN="https://crypto.hcportal.eu"
MANIFEST="images_manifest_full.tsv"

url_for_folio() {
  local folio="$1"
  python3 -c "
import json
d = json.load(open('images/manifest.json'))
for e in d:
    if e['folio'] == '$folio':
        print(e['url']); break
"
}

fetch_page() {
  local folio="$1"
  local url
  url=$(url_for_folio "$folio")
  if [ -z "$url" ]; then
    echo "no URL recorded for folio $folio in images/manifest.json" >&2
    exit 1
  fi
  echo "fetching $folio <- $url" >&2
  curl -sS -A "$UA" -H "Origin: $ORIGIN" -o "images/${folio}.jpg" "$url"
}

do_page() {
  local folio="$1"
  fetch_page "$folio"
  echo "regenerated images/${folio}.jpg, sha1: $(sha1sum "images/${folio}.jpg" | cut -d' ' -f1)"
}

do_crop() {
  local dir="$1" cropname="$2"
  local mpath="crops/${dir}/manifest.json"
  python3 -c "
import json, sys
from PIL import Image
m = json.load(open('$mpath'))
entry = next((e for e in m['iiif_lines'] if e['crop'] == '$cropname'), None)
if entry is None:
    print('no manifest entry for $cropname in $mpath -- not regenerable this way', file=sys.stderr)
    sys.exit(1)
src = f\"images/{entry['source_file']}\"
box = entry['box']
im = Image.open(src)
im.crop((box[0], box[1], box[2], box[3])).convert('RGB').save('crops/${dir}/${cropname}', quality=85)
print(f\"regenerated crops/${dir}/${cropname} from {src} box={box}\")
"
}

do_all() {
  # full pages, one request at a time, 1.5s apart
  local folios
  folios=$(python3 -c "
import csv
seen = set()
for row in csv.DictReader(open('$MANIFEST'), delimiter='\t'):
    if row['kind'] == 'fullpage':
        seen.add(row['path'].split('/')[-1][:-4])
for f in sorted(seen):
    print(f)
")
  for folio in $folios; do
    if [ ! -f "images/${folio}.jpg" ]; then
      do_page "$folio"
      sleep 1.5
    fi
  done
  # crops, no network -- cut from whatever full page is now on disk
  python3 -c "
import csv
for row in csv.DictReader(open('$MANIFEST'), delimiter='\t'):
    if row['kind'] == 'crop-lines' and 'box=' in row['source']:
        print(row['path'])
" | while read -r cpath; do
    dir=$(basename "$(dirname "$cpath")")
    cropname=$(basename "$cpath")
    do_crop "$dir" "$cropname"
  done
}

case "${1:-}" in
  page) do_page "$2" ;;
  crop) do_crop "$2" "$3" ;;
  all) do_all ;;
  *) echo "usage: $0 {page FOLIO | crop DIR CROPNAME | all}" >&2; exit 1 ;;
esac
