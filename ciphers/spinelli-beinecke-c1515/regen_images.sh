#!/usr/bin/env bash
# Regenerate the page images and line crops of ciphers/spinelli-beinecke-c1515 from their sources
# (TXE2-SHRINK-SPIN, 9 Oct 2026, the AX2-SHRINK recipe; inventory in images_manifest_full.tsv).
# Nothing was deleted by TXE2-SHRINK-SPIN (every image is cited, see images/SHRINK-2026-10-09.md); this
# script exists so a later shrink can delete a file with a recorded way back.
#
# Usage:
#   ./regen_images.sh page CANVAS WIDTH OUT     # IIIF fetch of a full page at WIDTH px (network)
#   ./regen_images.sh region CANVAS X,Y,W,H OUT # IIIF fetch of a native-resolution region (network)
#   ./regen_images.sh canvas CANVAS OUT         # IIIF fetch of the full native canvas (network), for full-canvas crops
#   ./regen_images.sh crop CROPNAME [SRCFILE]   # re-cut one images/manifest.json iiif_lines crop (plain box only), offline
#   ./regen_images.sh verify                    # offline: re-cut every crop whose source is on disk and compare sha256
#
# Crop conventions (images/manifest.json "iiif_lines"):
#   - source_file src_2_<canvas>_<x>_<y>_<w>_<h>.jpg: box is in canvas coordinates; crop = box minus (x,y),
#     PIL crop -> RGB -> JPEG quality 85 (tools/iiif_lines.py default). Tested byte-identical 20/20, 9 Oct 2026.
#   - source_file src_2_<canvas>_full.jpg / p2_full.jpg: same cut at offset 0 from the full native canvas, which is
#     NOT kept on disk (fetch with `canvas` first). Untested: no host was allowed to TXE2-SHRINK-SPIN.
#   - p1v_* (--follow-slope sheared strip): not a plain box; re-run tools/iiif_lines.py with the manifest params.
#   - p2x_* (H33d deskewed): python3 passes/p2x_cut.py FULL_CANVAS.jpg OUT; NOT byte-identical (0.19 grey levels).
#   - *_lines_debug.jpg: re-run tools/iiif_lines.py --debug with the family's params.
# Good-citizen rule: one collections.library.yale.edu request at a time, >=2 s apart, browser UA (CLAUDE.md
# host table, Beinecke row). The network modes are never run by `verify`.
set -euo pipefail
cd "$(dirname "$0")"
UA="Mozilla/5.0"
BASE="https://collections.library.yale.edu/iiif/2"

fetch() { curl -sS -f -A "$UA" -o "$2" "$1"; sleep 2; }

case "${1:-}" in
  page)   fetch "$BASE/$2/full/$3,/0/default.jpg" "$4" ;;
  region) fetch "$BASE/$2/$3/full/0/default.jpg" "$4" ;;
  canvas) fetch "$BASE/$2/full/full/0/default.jpg" "$3" ;;
  crop|verify)
    python3 - "$@" <<'PYEOF'
import sys, json, re, io, hashlib, os
from PIL import Image
mode = sys.argv[1]
m = json.load(open('images/manifest.json'))
ent = {e['crop']: e for e in m['iiif_lines']}

def cut(e, src=None):
    sf = src or os.path.join('images', e['source_file'])
    mm = re.match(r'src_2_\d+_(\d+)_(\d+)_\d+_\d+\.jpg$', os.path.basename(e['source_file']))
    rx, ry = (int(mm.group(1)), int(mm.group(2))) if mm else (0, 0)
    if 'box' not in e or 'follow-slope' in e['method']:
        sys.exit(f"{e['crop']}: not a plain-box crop; see the header of this script")
    b = e['box']
    c = Image.open(sf).convert('RGB').crop((b[0] - rx, b[1] - ry, b[2] - rx, b[3] - ry))
    bio = io.BytesIO(); c.convert('RGB').save(bio, 'JPEG', quality=85)
    return bio.getvalue()

if mode == 'crop':
    e = ent[sys.argv[2]]
    data = cut(e, sys.argv[3] if len(sys.argv) > 3 else None)
    open(os.path.join('images', e['crop']), 'wb').write(data)
    print('wrote images/' + e['crop'])
else:
    ok = bad = 0
    for n, e in ent.items():
        sf = os.path.join('images', e['source_file'])
        if not os.path.exists(sf) or not os.path.exists(os.path.join('images', n)):
            continue
        same = hashlib.sha256(cut(e)).hexdigest() == hashlib.sha256(open(os.path.join('images', n), 'rb').read()).hexdigest()
        ok += same; bad += not same
        print(('OK   ' if same else 'DIFF ') + n)
    print(f'verify: {ok} byte-identical, {bad} differ')
    sys.exit(1 if bad else 0)
PYEOF
    ;;
  *) sed -n '2,25p' "$0"; exit 2 ;;
esac
