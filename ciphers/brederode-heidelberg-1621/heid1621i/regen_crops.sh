#!/bin/bash
# HEID-1621I (15 Oct 2026): re-derive the native numeral-block regions of NL-HaNA 1.01.02 inv. 6021 scans 375, 379, 423 and their line
# crops, so no later worker refetches. Run from the repository root. Usage: bash ciphers/brederode-heidelberg-1621/heid1621i/regen_crops.sh OUTDIR
# 4 service.archief.nl requests (METS + 3 regions), >= 3.2 s apart, skipped when the file is already in OUTDIR; take/release lines in ROOM.md
# first. Images stay outside git; region sha1s are checked against images/manifest.json (heid_6021, heid_6021g).
set -e; O=${1:?outdir}; M=c82b1eb5-6946-4ca9-8082-f13c2ab5f078; mkdir -p $O
python3 - "$O" "$M" <<'P'
import hashlib, json, os, re, sys, time, urllib.request
O, mid = sys.argv[1], sys.argv[2]; UA = "cipher-lab research script (contact via repository)"
def get(u):
    r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=90); b = r.read()
    open(f"{O}/requests.log", "a").write(f"{time.strftime('%H:%M:%S', time.gmtime())}\t{r.status}\t{u}\n"); time.sleep(3.2); return b
mp = f"{O}/mets_{mid}.xml"
if not os.path.exists(mp): open(mp, "wb").write(get(f"https://service.archief.nl/gaf/api/mets/v1/{mid}"))
x = open(mp, encoding="utf-8").read(); om = {}
for m in re.finditer(r'<(?:mets:)?div[^>]*ORDER="(\d+)"[^>]*>(.*?)</(?:mets:)?div>', x, re.S):
    f = re.search(r'FILEID="ID([0-9a-f-]+)DEF"', m.group(2))
    if f: om[int(m.group(1))] = f.group(1)
man = json.load(open("ciphers/brederode-heidelberg-1621/images/manifest.json"))
want = {(s["scan"], s.get("region")): s["sha1"] for k in ("heid_6021", "heid_6021g") for s in man[k]["scans"] if "region" in s}
p = "/".join(re.findall("..", mid.replace("-", "")))
for scan, reg in [(375, "900,780,1780,1420"), (379, "730,1640,1960,1420"), (423, "760,2000,1900,720")]:
    fn = f"{O}/s{scan}_block_native.jpg"
    if not os.path.exists(fn):
        b = get(f"https://service.archief.nl/iip/iipsrv?IIIF={p}/{om[scan]}.jp2/{reg}/full/0/default.jpg")
        assert b[:2] == b"\xff\xd8", f"not jpeg {scan}"; open(fn, "wb").write(b)
    h = hashlib.sha1(open(fn, "rb").read()).hexdigest()
    print(scan, reg, h, "MATCH" if h == want[(scan, reg)] else f"MISMATCH (manifest {want[(scan, reg)]})")
P
for s in 375 379 423; do python3 tools/iiif_lines.py --image $O/s${s}_block_native.jpg --out $O/c$s --prefix h$s --debug; done
