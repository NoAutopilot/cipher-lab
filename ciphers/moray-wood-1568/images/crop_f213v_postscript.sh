#!/bin/sh
# Crop recipe for the cipher postscript of BL Add MS 32091 f.213v (DECODE R8345, image IMG_R8345_I38545_P4.jpg,
# 6971x9718 px, sha1 a4e848953a3afca88f015e0e8efe1395aea137af -- see manifest.json). Written 2 Oct 2026 by
# GAPS3-moray-wood-1568 (account-4). The full-size image is British Library material fetched through the owner's
# DECODE login and is NOT committed (sources/decode/NOTES.md, 28 Sept 2026); fetch it into a scratchpad dir with
#   NODE_PATH=$(npm root -g) node tools/decode_browser_login.js 8345 OUT --guess-fullsize --max-files 8
# (one login per session; absolute https://de-crypt.org/decrypt-custom/filesrv/?file=IMG_... URLs if --fetch is used).
# The crops are not committed either; only this recipe and the manifest entries are.
#
# How the region was found (no vision): a row ink profile (pixels < 150 grey) over the leaf shows a 36-line hand at
# about 160-175 px pitch between y 1947 and 8221; the text starts at x about 1650. The last five lines are: y 7459,
# 7653, 7824 (core ink 53-55k px each, against 25-42k for the body lines above), y 7965 (one short piece x 1674-2328,
# about 650 px, then a 1712 px gap -- the seven-sign closing line L4) and y 8221 (x 3772-5385, the signature, set off
# by a 256 px gap). Region 1500,7370,4300,720 then detects exactly four lines at region y 89, 283, 454, 595
# (native y 7459, 7653, 7824, 7965) = postscript L1-L4 of ciphertext.tsv; each band (plus 30 px above, for
# ascenders) is cut in 4 segments of <= 1200 px with 120 px overlap (never re-stitched, iiif_lines.py step 4), so a
# reader sees each glyph at about 80 px after the vision downscale.
#
# usage: sh ciphers/moray-wood-1568/images/crop_f213v_postscript.sh <dir holding IMG_R8345_I38545_P4.jpg> <out dir>
set -e
SRC="$1/IMG_R8345_I38545_P4.jpg"; OUT="$2"
python3 tools/iiif_lines.py --image "$SRC" --out "$OUT" --prefix f213v_ps --region 1500,7370,4300,720 --ink 150 --distance 120 --max-width 1200 --overlap 120 --top-margin 30 --debug
