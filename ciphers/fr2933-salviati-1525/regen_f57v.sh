#!/usr/bin/env bash
# SALV-57V (13 Oct 2026): regenerate the f57v render and its plain-box line crops through openapi.bnf.fr
# (IIIF Image API v3; gallica.bnf.fr answers 403 since 11 Oct 2026). Same region and width as
# SALV-PLAIN3's Gallica fetch (canvas f59, left half, 2400 px wide -> 2400x3250), so crop_plain_leaf.py's
# (x+80,y+80)*1.5 transform still applies. Neither file is committed (folder-size rule; .gitignore).
# Fetched 13 Oct 2026 21:49 UTC: 1,088,166 bytes, sha1 865993376fd536fdddcbb59e95b818bd30974b94.
set -euo pipefail
cd "$(dirname "$0")"
UA="cipher-lab research script (contact via repository)"
curl -sS -f -A "$UA" -o images/f57v_ref2400.jpg \
  "https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b90600674/f59/pct:0,0,50,100/2400,/0/default.jpg"
sha1sum images/f57v_ref2400.jpg
python3 crop_plain_leaf.py f57v
