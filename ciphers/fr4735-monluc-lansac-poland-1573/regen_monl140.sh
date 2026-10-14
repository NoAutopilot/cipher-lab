#!/bin/sh
# MONL-140 (14 Oct 2026): re-fetch the untracked f.140-f.142 views from openapi.bnf.fr (>= 3 s apart).
set -e
cd "$(dirname "$0")"; D=images/scratch140; mkdir -p $D
B=https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060724s
UA="cipher-lab research script (contact via repository)"
for c in 272 273 274 275; do curl -sS -A "$UA" -o $D/c$c.jpg "$B/f$c/full/1400,/0/default.jpg"; sleep 3; done
curl -sS -A "$UA" -o $D/c272_l5-12.jpg "$B/f272/pct:13,30,67,17/1600,/0/default.jpg"
