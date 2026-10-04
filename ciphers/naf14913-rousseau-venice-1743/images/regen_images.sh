#!/bin/sh
# Re-derive deleted images of ciphers/naf14913-rousseau-venice-1743/images from images_manifest_full.tsv
# (FT4q 3 Oct 2026 native regions; A3V2-ROUS2 4 Oct 2026 native regions of ft4h/, lowres/*_1000.jpg pages,
# lowres/s300/*_300.jpg pages -- AX2-SHRINK pattern, CLAUDE.md access playbook). Columns of the manifest:
# file bytes sha256 kind source_url_or_derivation cited_by status. Every file whose source column starts
# with https:// is a plain Gallica IIIF fetch and regenerates byte-identically (tested 4 Oct 2026 on one
# sample per class: ft4h/..._f440_650_650_3500_800.jpg, lowres/v440_213v_1000.jpg, lowres/s300/v516_251v_300.jpg;
# lowres/v439_213r_1000.jpg for the pattern-URL pages; the FT4q f514 region on 3 Oct 2026). NOT byte-identical on
# re-fetch, so kept in the tree: the 38 GAPS210 lowres/s300/v533-v592 pages (v533 differs; their fetch route was never
# recorded, the URL in their row is the pattern guess), f252r/src_f517_*.jpg
# (1,025,302 differing bytes from byte 830 on) and v424_1000.jpg (69 bytes longer); do not delete these.
# Crops (kind crop-lines / crop-eye) are not deleted; each one's recipe is in its row (source file, box, params)
# and in the manifest.json of its folder, so `crop` below re-cuts one from its on-disk or regenerated source
# (box px are native-canvas px when the source was fetched with --region -- subtract the region origin encoded
# in the source file name -- else px of the local source image); JPEG q85 as tools/iiif_lines.py writes them.
# Debug overlays (kind debug-overlay) come back from re-running the same tools/iiif_lines.py line with --debug.
# Good-citizen rule: one gallica.bnf.fr request at a time, 2 s apart, descriptive UA.
# Usage: sh regen_images.sh                 # every deleted URL-sourced row still missing on disk
#        sh regen_images.sh FILE ...        # only these rows
#        sh regen_images.sh crop CROP       # re-cut one crop from its source (needs python3 + Pillow)
cd "$(dirname "$0")"
UA="cipher-lab research script (contact via repository)"
M=images_manifest_full.tsv
if [ "$1" = "crop" ]; then
  python3 - "$2" "$M" <<'PY'
import sys, re, csv
from PIL import Image
crop, man = sys.argv[1], sys.argv[2]
row = next(r for r in csv.DictReader(open(man), delimiter='\t') if r['file'] == crop)
m = re.search(r'box \[(\d+), (\d+), (\d+), (\d+)\].*? of (\S+)', row['source_url_or_derivation'])
x0, y0, x1, y1 = map(int, m.groups()[:4]); src = m.group(5)
if 'local source' in row['source_url_or_derivation'] and '--region' not in row['source_url_or_derivation']:
    pass
off = re.search(r'_f\d+_(\d+)_(\d+)_\d+_\d+', src)
im = Image.open(src)
# native-canvas boxes: subtract the region origin when the box lies outside the source image
if off and (x1 > im.width or y1 > im.height):
    ox, oy = int(off.group(1)), int(off.group(2)); x0, y0, x1, y1 = x0 - ox, y0 - oy, x1 - ox, y1 - oy
im.crop((x0, y0, x1, y1)).save(crop + '.regen.jpg', quality=85)
print('wrote', crop + '.regen.jpg', 'from', src, (x0, y0, x1, y1))
PY
  exit $?
fi
tail -n +2 "$M" | while IFS="$(printf '\t')" read f bytes sha kind url cited status; do
  case "$status" in deleted*) ;; *) continue;; esac
  case "$url" in https://*) ;; *) continue;; esac
  if [ $# -gt 0 ]; then case " $* " in *" $f "*) ;; *) continue;; esac; fi
  [ -f "$f" ] && continue
  u=$(printf '%s' "$url" | cut -d' ' -f1)
  mkdir -p "$(dirname "$f")"
  curl -sS -A "$UA" -o "$f" "$u" && echo "$(sha256sum "$f" | cut -c1-64)  $f (expected $sha)"
  sleep 2
done
