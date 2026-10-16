#!/usr/bin/env python3
"""HEID-1623A: fetch the native regions of NA 1.01.02 inv. 6022 scans 166/171 (cipher blocks, marginal note) once.
usage: python3 fetch_regions.py OUTDIR   (needs OUTDIR/i6022/mets_<id>.xml from screen_tools/na_fetch.py; >= 3.2 s apart)"""
import re, sys, time, os, urllib.request
O = sys.argv[1]; mid = "412b1414-afa2-42fe-b56d-2b5f705e5005"; UA = "cipher-lab research script (contact via repository)"
REG = [("u1_166_block", 166, "pct:61,16.5,39,16"), ("u2_171_block", 171, "pct:61.5,22,38.5,14"), ("u3_171_note", 171, "pct:50,18.5,11,14.5"),
       # widened once each (PREREG: U2 clipped the block's first line, U3 clipped the note's right edge)
       ("u2w_171_block", 171, "pct:61.5,19,38.5,17"), ("u3w_171_note", 171, "pct:49.5,18,13,15")]
x = open(f"{O}/i6022/mets_{mid}.xml", encoding="utf-8").read(); om = {}
for m in re.finditer(r'<(?:mets:)?div[^>]*ORDER="(\d+)"[^>]*>(.*?)</(?:mets:)?div>', x, re.S):
    f = re.search(r'FILEID="ID([0-9a-f-]+)DEF"', m.group(2))
    if f: om[int(m.group(1))] = f.group(1)
for name, scan, reg in REG:
    fn = f"{O}/{name}.jpg"
    if os.path.exists(fn): continue
    base = f"https://service.archief.nl/iip/iipsrv?IIIF={'/'.join(re.findall('..', mid.replace('-', '')))}/{om[scan]}.jp2"
    b = urllib.request.urlopen(urllib.request.Request(f"{base}/{reg}/full/0/default.jpg", headers={"User-Agent": UA}), timeout=90).read()
    print(name, len(b), b[:2] == b"\xff\xd8"); open(fn, "wb").write(b); time.sleep(3.2)
