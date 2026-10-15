#!/bin/bash
# HEID-1621G (15 Oct 2026): re-derive scans 375/423 at 1200 px, the two native block regions and the line crops; then the unit tables.
# Run from ciphers/oldenbarnevelt-brederode-1605. Usage: bash ../brederode-heidelberg-1621/heid1621g/regen_heid1621g.sh OUTDIR
# (5 service.archief.nl requests at >= 3.1 s; take/release lines in ROOM.md first; images stay outside git; sha1s in ../images/manifest.json heid_6021g)
set -e; O=${1:-scratch_heidg}; M=c82b1eb5-6946-4ca9-8082-f13c2ab5f078
python3 screen_tools/na_fetch.py $M $O/i6021 1200 375 423
python3 - "$O" <<'P'
import re, sys, time, urllib.request
O = sys.argv[1]; mid = "c82b1eb5-6946-4ca9-8082-f13c2ab5f078"; UA = "cipher-lab research script (contact via repository)"
x = open(f"{O}/i6021/mets_{mid}.xml", encoding="utf-8").read(); om = {}
for m in re.finditer(r'<(?:mets:)?div[^>]*ORDER="(\d+)"[^>]*>(.*?)</(?:mets:)?div>', x, re.S):
    f = re.search(r'FILEID="ID([0-9a-f-]+)DEF"', m.group(2))
    if f: om[int(m.group(1))] = f.group(1)
for scan, reg in [(375, "900,780,1780,1420"), (423, "760,2000,1900,720")]:
    time.sleep(3.2)
    base = f"https://service.archief.nl/iip/iipsrv?IIIF={'/'.join(re.findall('..', mid.replace('-', '')))}/{om[scan]}.jp2"
    open(f"{O}/s{scan}_block_native.jpg", "wb").write(urllib.request.urlopen(urllib.request.Request(f"{base}/{reg}/full/0/default.jpg", headers={"User-Agent": UA}), timeout=90).read())
P
python3 ../../tools/iiif_lines.py --image $O/s375_block_native.jpg --out $O/c375 --prefix h375 --debug
python3 ../../tools/iiif_lines.py --image $O/s423_block_native.jpg --out $O/c423 --prefix h423 --debug
sha1sum $O/i6021/s0375_1200.jpg $O/i6021/s0423_1200.jpg $O/s3*_block_native.jpg $O/s4*_block_native.jpg
python3 ../brederode-heidelberg-1621/heid1621g/units.py --check
