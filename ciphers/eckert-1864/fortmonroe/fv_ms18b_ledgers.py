#!/usr/bin/env python3
"""FV-MS18b (9 Oct 2026): grep the cached holder transcriptions of mssEC 18 and mssEC 19 (sources/mssEC18, sources/mssEC19)
for distinctive clear words of E322-E325, to find duplicates, parallel copies and siblings. Disk only, no network."""
import json, glob, re, os, sys
here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, '..', 'sources')
TERMS = {
 'E322': ['port royal', 'quadroon', 'esteem mates', 'requisite', 'temper airy', 'laution', 'garrisoned', 'compete aunt', 'opera shine', 'shady'],
 'E323': ['hurlbut', 'legends quitman', 'breaking up', 'recollecting', 'hopper paddle', 'dish venus', 'whinny', 'gwinn'],
 'E324': ['pulaski', 'seddon', 'sed don', 'camp bell', 'campbell', 'hunt her', 'galway', 'cuss toddy', 'cuss tady', 'custody'],
 'E325': ['kendall', 'kennedy', 'kennerly', 'ritchie', 'girardeau', 'new madrid', 'saint joseph', 'rebel agents', 'walpole agents', 'seizure', 'tunstall'],
}
for led in ('mssEC18', 'mssEC19'):
    for f in sorted(glob.glob(os.path.join(src, led, 'p*.json'))):
        d = json.load(open(f))
        t = re.sub(r'\s+', ' ', (d.get('transc') or '')).lower()
        for e, ts in TERMS.items():
            hits = [x for x in ts if x in t]
            if hits:
                print(f"{led}\t{os.path.basename(f)[1:-5]}\t{e}\t{','.join(hits)}")
