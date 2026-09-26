#!/usr/bin/env bash
# Regenerate full-page renders and line crops for ciphers/lodewijk-van-nassau-1573-74
# that were removed from the working tree on 26 Sept 2026 (AX2-SHRINK, LANE AX2) to
# stay under CLAUDE.md's 30 MB-per-folder rule. The originals are still readable from
# git history (see NOTES.md's "AX2-SHRINK" section for the commit sha).
#
# Usage:
#   ./regen_images.sh page BRIEFNR PAGE      # re-fetch PDF + render one full page
#   ./regen_images.sh page300 BRIEFNR PAGE   # re-fetch PDF + render one 300dpi PNG page (images_wv2/crops_4612/ convention)
#   ./regen_images.sh crop  images_manifest_full.tsv PATH   # re-cut one crop from its recorded box
#   ./regen_images.sh all                    # do the whole folder (all briefs in both manifests)
#
# Sources: images/manifest.json (briefs 4610-4616, pdftoppm -png -r 150) and
# images_wv2/manifest.json (briefs 4503/5194/5797/5799/5810/5811, pymupdf render, JPEG q80, 150dpi).
# images_wv2/crops_4612/src_04612_p{1,2}.png is a third convention (AX-4612TR, 26 Sept 2026): pymupdf,
# 300dpi (zoom 300/72), PNG, 2481x3508 -- double the linear resolution of images/04612_p*.png, used for
# settling ambiguous numerals by eye. Its PDF url comes from images/manifest.json's briefnr=4612 entry
# (fetch_pdf already resolves it); only the render step differs (page300/render_pymupdf300 below).
# images_wv2/crops_comp/{04614,07205,05801}_* and ax2_5801/crops/* (AX-COMP lineage, 26 Sept 2026) are a
# FOURTH convention that AX2-SHRINK3 could not reconstruct: source page widths recorded in
# images_wv2/crops_comp/manifest.json (2153-2529px) match neither render_pdftoppm (1241px) nor
# render_pymupdf300 (2481px, confirmed against a fresh 04614.pdf re-render, all 3 pages) nor a
# whitespace-trim of the 300dpi render (2431/2380/2408px) -- likely a manual per-page crop region whose
# exact box was never logged. These crops were downscaled in place (<=1600px wide, JPEG q80) without a
# working regen recipe; do not add a `page_comp`/`crop` case for them without first re-deriving the
# render step (e.g. by asking whoever ran AX-COMP, or bisecting DPI/trim parameters against the
# recorded box widths) and checking a sha1 match the way page/page300 do above.
# Good-citizen rule: one resources.huygens.knaw.nl request at a time, >=2s apart.
set -euo pipefail
cd "$(dirname "$0")"
UA="cipher-lab research script (contact via repository)"

fetch_pdf() {
  local briefnr="$1" out="$2"
  local url
  url=$(python3 -c "
import json
for m in ('images/manifest.json','images_wv2/manifest.json'):
    d = json.load(open(m))
    for e in d['files']:
        if str(e['briefnr']) == '$briefnr':
            print(e['pdf_url']); raise SystemExit
")
  [ -n "$url" ] || { echo "briefnr $briefnr not found in either manifest" >&2; exit 1; }
  curl -sS -A "$UA" -o "$out" "$url"
  sleep 2
}

render_pdftoppm() {
  # images/ convention: pdftoppm -png -r 150, one file per page, 1-indexed
  local pdf="$1" outprefix="$2"
  pdftoppm -png -r 150 "$pdf" "$outprefix"
}

render_pymupdf() {
  # images_wv2/ convention: pymupdf, 150dpi, JPEG q80
  local pdf="$1" outdir="$2" briefnr="$3"
  python3 - "$pdf" "$outdir" "$briefnr" <<'PYEOF'
import sys, fitz
pdf, outdir, briefnr = sys.argv[1], sys.argv[2], sys.argv[3]
doc = fitz.open(pdf)
zoom = 150 / 72
mat = fitz.Matrix(zoom, zoom)
for i, page in enumerate(doc, start=1):
    pix = page.get_pixmap(matrix=mat)
    pix.save(f"{outdir}/{int(briefnr):05d}_p{i}.jpg", jpg_quality=80)
PYEOF
}

render_pymupdf300() {
  # images_wv2/crops_4612/ convention: pymupdf, 300dpi (zoom 300/72), PNG (AX-4612TR, 26 Sept 2026)
  local pdf="$1" outdir="$2" briefnr="$3"
  python3 - "$pdf" "$outdir" "$briefnr" <<'PYEOF'
import sys, fitz
pdf, outdir, briefnr = sys.argv[1], sys.argv[2], sys.argv[3]
doc = fitz.open(pdf)
zoom = 300 / 72
mat = fitz.Matrix(zoom, zoom)
for i, page in enumerate(doc, start=1):
    if i > 2:
        continue
    pix = page.get_pixmap(matrix=mat)
    pix.save(f"{outdir}/src_{int(briefnr):05d}_p{i}.png")
PYEOF
}

do_page300() {
  local briefnr="$1" page="$2" tmp
  tmp=$(mktemp -d)
  fetch_pdf "$briefnr" "$tmp/$briefnr.pdf"
  render_pymupdf300 "$tmp/$briefnr.pdf" "$tmp" "$briefnr"
  cp "$tmp/src_$(printf '%05d' "$briefnr")_p${page}.png" "images_wv2/crops_4612/src_$(printf '%05d' "$briefnr")_p${page}.png"
  rm -rf "$tmp"
  echo "rendered 300dpi briefnr=$briefnr page=$page"
}

do_page() {
  local briefnr="$1" page="$2" tmp
  tmp=$(mktemp -d)
  fetch_pdf "$briefnr" "$tmp/$briefnr.pdf"
  if python3 -c "
import json
d = json.load(open('images/manifest.json'))
import sys
sys.exit(0 if any(str(e['briefnr'])=='$briefnr' for e in d['files']) else 1)
" 2>/dev/null; then
    render_pdftoppm "$tmp/$briefnr.pdf" "$tmp/$(printf '%05d' "$briefnr")"
    cp "$tmp"/*"-$(printf '%02d' "$page")"*.png "images/$(printf '%05d' "$briefnr")_p${page}.png" 2>/dev/null || \
      cp "$tmp"/*"-${page}"*.png "images/$(printf '%05d' "$briefnr")_p${page}.png"
  else
    render_pymupdf "$tmp/$briefnr.pdf" "$tmp" "$briefnr"
    cp "$tmp/$(printf '%05d' "$briefnr")_p${page}.jpg" "images_wv2/$(printf '%05d' "$briefnr")_p${page}.jpg"
  fi
  rm -rf "$tmp"
  echo "rendered briefnr=$briefnr page=$page"
}

do_crop() {
  local manifest="$1" path="$2"
  python3 - "$manifest" "$path" <<'PYEOF'
import sys, csv, ast, os
manifest, path = sys.argv[1], sys.argv[2]
with open(manifest) as f:
    r = csv.DictReader(f, delimiter="\t")
    row = next((x for x in r if x["path"] == path), None)
if row is None:
    sys.exit(f"{path} not found in {manifest}")
src = row["source"]
if "box=" not in src:
    sys.exit(f"{path} has no recorded box (source: {src}); not a line crop")
parent = src.split("crop of ")[1].split(" box=")[0]
box = ast.literal_eval(src.split("box=")[1].split(" via")[0])
if not os.path.exists(parent):
    sys.exit(f"parent {parent} not on disk -- run: ./regen_images.sh page <briefnr> <page> (or page300 for images_wv2/crops_4612/src_*) first")
from PIL import Image
im = Image.open(parent)
cropped = im.crop(tuple(box))
# AX2-SHRINK2 convention (26 Sept 2026): stored crops are capped at 1600px wide, JPEG q80;
# a crop already under that (the images/ 04610-4616 line crops) keeps the original q85 behaviour.
if cropped.width > 1600:
    new_h = round(cropped.height * 1600 / cropped.width)
    cropped = cropped.resize((1600, new_h), Image.LANCZOS)
    cropped.save(path, quality=80)
else:
    cropped.save(path, quality=85)
print(f"cut {path} from {parent} box={box}")
PYEOF
}

case "${1:-}" in
  page) do_page "$2" "$3" ;;
  page300) do_page300 "$2" "$3" ;;
  crop) do_crop "$2" "$3" ;;
  all)
    python3 -c "
import json
for m in ('images/manifest.json','images_wv2/manifest.json'):
    d = json.load(open(m))
    for e in d['files']:
        for i in range(1, e.get('pages', e.get('pages_in_pdf', 0)) + 1):
            print(e['briefnr'], i)
" | while read -r briefnr page; do
      do_page "$briefnr" "$page"
    done
    ;;
  *)
    echo "usage: $0 {page BRIEFNR PAGE | page300 BRIEFNR PAGE | crop images_manifest_full.tsv PATH | all}" >&2
    exit 1
    ;;
esac
