#!/bin/sh
# Re-derive images/crops/ (line crops and, with --overlays, the debug overlays) from openapi.bnf.fr into DIR.
# BAL167-SHRINK, 13 Oct 2026. See regen_images.py --help; images_manifest_full.tsv lists every file and who cites it.
# Usage: sh ciphers/baluze167-davaux-1637/regen_images.sh DIR [--offline] [--check] [--overlays] [--only SUBSTR]
set -e
OUT=${1:?usage: regen_images.sh DIR [options]}; shift
python3 "$(dirname "$0")/regen_images.py" --out "$OUT" "$@"
