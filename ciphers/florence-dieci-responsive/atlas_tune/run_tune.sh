#!/bin/sh
# R9-FLOR (6 Oct 2026): glyph_atlas segment on c.127 line crops, default vs tuned (--mark-h 0.7 --min-area 0.25).
# Run from ciphers/florence-dieci-responsive; writes segment output to $1 (scratch, not committed). Box counts per crop
# are in atlas_tune/coverage.tsv. Needs opencv-python-headless scikit-image scikit-learn pillow.
set -e
OUT=${1:-/tmp/r9flor}
for T in default tuned; do
  X=""; [ "$T" = tuned ] && X="--mark-h 0.7 --min-area 0.25"
  P=""; for f in images/c127/c127b1_L0*_s*.jpg images/c127b2/c127b2_L0[2-9]_s*.jpg images/c127b2/c127b2_L1*_s*.jpg; do
    k=$(basename "$f" .jpg); P="$P --page $k=$f"; done
  python3 ../../tools/glyph_atlas.py segment --out "$OUT/$T" $X $P 2>/dev/null
  awk -F'\t' 'NR>1{c[$2]++}END{for(k in c)print k"\t"c[k]}' "$OUT/$T/signs.tsv" | sort > "$OUT/$T.counts"
done
paste "$OUT/default.counts" "$OUT/tuned.counts" | cut -f1,2,4
