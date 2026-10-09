#!/bin/sh
# MANT-0309 (9 Oct 2026): one code strip and one gloss strip per run of runs.tsv, via tools/iiif_lines.py (run from the repo root).
D=ciphers/sachsstaatsarchiv-manteuffel-1712/f0309_08
tail -n +2 $D/runs.tsv | while IFS="$(printf '\t')" read run page x0 x1 yc yg ctx; do
  w=$((x1-x0+40)); python3 tools/iiif_lines.py --image $D/0309.jpg --region $((x0-20)),$((yc-30)),$w,64 --centres 32 --out $D/crops --prefix c0309$run --debug >/dev/null || exit 1
  gw=$((x1-x0+240)); python3 tools/iiif_lines.py --image $D/0309.jpg --region $((x0-120)),$((yg-26)),$gw,50 --centres 25 --out $D/crops --prefix g0309$run --debug >/dev/null || exit 1
done
