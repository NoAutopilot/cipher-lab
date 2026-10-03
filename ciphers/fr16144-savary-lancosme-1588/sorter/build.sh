#!/bin/sh
# Rebuilds sorter/index.html from Gallica (SV-SORT, LANE-JM, 3 Oct 2026). Usage: sh sorter/build.sh SCRATCH  (run from the repo root)
# Pages are not committed (re-fetchable; index.html embeds the posterised copies). 7 IIIF requests, 2 s apart.
# Needs numpy pillow opencv-python-headless scikit-image scikit-learn.
set -e
S=${1:-/tmp/fr16144-sorter}; T=ciphers/fr16144-savary-lancosme-1588/sorter; mkdir -p "$S/pages" "$S/pages_s"
while read c reg; do
  [ -s "$S/pages/c$c.jpg" ] || { curl -sS -A "Mozilla/5.0" -o "$S/pages/c$c.jpg" "https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060974c/f$c/$reg/2400,/0/default.jpg"; sleep 2; }
done < $T/inputs/regions.txt
python3 tools/glyph_atlas.py segment $(for c in 370 371 372 373 374 375 380; do echo --page c$c=$S/pages/c$c.jpg; done) --out "$S/atlas"
python3 tools/glyph_atlas.py cluster --out "$S/atlas" --k 120 --k-marks 16
# per-page rescale to a median sign height of about 22 px, posterise (background > 190 -> white, 16 grey levels) to fit the 16 MB page limit
python3 - "$S" <<'PY'
import csv, json, os, sys
from PIL import Image, ImageOps
S = sys.argv[1]; pj = json.load(open(f'{S}/atlas/pages.json')); F = {}
for p, v in pj.items():
    f = min(1.0, 22 / v['median_h']); F[p] = f
    im = Image.open(v['image']); im = im.resize((round(im.width * f), round(im.height * f)), Image.LANCZOS)
    im = ImageOps.autocontrast(im.convert('L'), cutoff=1).point(lambda x: 255 if x > 190 else (x // 16) * 16)
    im.save(f'{S}/pages_s/{p}.png', optimize=True); v['image'] = f'{S}/pages_s/{p}.png'
json.dump(pj, open(f'{S}/pages_s.json', 'w'))
for src, dst in [('signs', 'signs_s'), ('marks', 'marks_s')]:
    rd = csv.DictReader(open(f'{S}/atlas/{src}.tsv'), delimiter='\t')
    w = csv.DictWriter(open(f'{S}/{dst}.tsv', 'w'), fieldnames=rd.fieldnames, delimiter='\t'); w.writeheader()
    for r in rd:
        for k in ('x', 'y', 'w', 'h'): r[k] = str(max(1, round(int(r[k]) * F[r['page']])))
        w.writerow(r)
PY
python3 tools/sign_sorter.py --signs "$S/signs_s.tsv" --labels $T/inputs/labels.tsv --marks "$S/marks_s.tsv" --pages "$S/pages_s.json" \
  --clusters "$S/atlas/clusters.tsv" --title "Lancosme 1587 Sign Sorter" --focus $T/inputs/focus.tsv \
  --focus-note "Pairs of piles whose average shapes are nearest (cosine >= 0.94): likely one sign split by the clustering." \
  --out "$S/index.html"
echo "compare $S/index.html with $T/index.html (the committed lede is longer; see NOTES.md SV-SORT)"
