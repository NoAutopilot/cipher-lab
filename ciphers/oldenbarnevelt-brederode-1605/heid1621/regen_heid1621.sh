#!/bin/bash
# HEID-1621 (15 Oct 2026): re-derive inv. 6021 scans 378-380 at 1200 px, the two native regions of scan 379 and the line crops.
# Run from the target folder. Usage: bash heid1621/regen_heid1621.sh OUTDIR  (images stay outside git; 7 service.archief.nl requests)
set -e; O=${1:-scratch_heid}; M=c82b1eb5-6946-4ca9-8082-f13c2ab5f078
python3 screen_tools/na_fetch.py $M $O/i6021 1200 378 379 380
python3 - "$O" <<'P'
import re, sys, time, urllib.request
O = sys.argv[1]; mid = "c82b1eb5-6946-4ca9-8082-f13c2ab5f078"; UA = "cipher-lab research script (contact via repository)"
x = open(f"{O}/i6021/mets_{mid}.xml", encoding="utf-8").read(); om = {}
for m in re.finditer(r'<(?:mets:)?div[^>]*ORDER="(\d+)"[^>]*>(.*?)</(?:mets:)?div>', x, re.S):
    f = re.search(r'FILEID="ID([0-9a-f-]+)DEF"', m.group(2))
    if f: om[int(m.group(1))] = f.group(1)
base = f"https://service.archief.nl/iip/iipsrv?IIIF={'/'.join(re.findall('..', mid.replace('-', '')))}/{om[379]}.jp2"
for name, reg in [("block", "730,1640,1960,1420"), ("close", "2930,1180,1850,950")]:
    time.sleep(3.2)
    b = urllib.request.urlopen(urllib.request.Request(f"{base}/{reg}/full/0/default.jpg", headers={"User-Agent": UA}), timeout=90).read()
    open(f"{O}/s379_{name}_native.jpg", "wb").write(b)
P
python3 ../../tools/iiif_lines.py --image $O/s379_block_native.jpg --out $O/crops --prefix h379 --debug
python3 ../../tools/iiif_lines.py --image $O/s379_close_native.jpg --out $O/ccrops --prefix c379 --debug
sha1sum $O/i6021/s037*_1200.jpg $O/s379_*_native.jpg
