#!/usr/bin/env python3
"""Harvest HathiTrust volume ids for a named multi-volume series without touching HathiTrust's own
Cloudflare-protected search: look up the series' OCLC number(s) via the Open Library search API, then
list every volume HathiTrust holds under that OCLC record through the Bibliographic API
(catalog.hathitrust.org/api/volumes/brief/oclc/N.json), which often returns dozens of enumerated
volumes from one lookup (e.g. Calendar of State Papers Venetian, oclc 2056131, gives 40 htids in one
call). Good-citizen rule: one request at a time, >=1.5 s apart, to each host.

  python3 tools/htrc_series_harvest.py --series-file series.tsv --out out.tsv [--sleep 1.5] [--olkey-max 3]

series.tsv: series_name<TAB>openlibrary_query (one row per series; '#' first char comments out a row).
Writes out.tsv: series, oclc, record_id, htid, enumcron, title, publishDates.

python3 tools/htrc_series_harvest.py --oclc SERIES_NAME=OCLC[,OCLC...] [...] does the second step alone,
for when the Open Library query needs hand-picking (ambiguous titles, ampersands, ligatures).
"""
import argparse
import csv
import json
import sys
import time
import urllib.parse
import urllib.request

OL = 'https://openlibrary.org/search.json?q=%s&fields=title,oclc,first_publish_year&limit=20'
HT = 'https://catalog.hathitrust.org/api/volumes/brief/oclc/%s.json'
OL_UA = 'cipher-lab research script (contact via repository)'
HT_UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
         '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')


def get(url, ua, timeout=60):
    req = urllib.request.Request(url, headers={'User-Agent': ua})
    return json.load(urllib.request.urlopen(req, timeout=timeout))


def ol_oclcs(query, top_n):
    data = get(OL % urllib.parse.quote(query), OL_UA)
    oclcs = []
    for doc in data.get('docs', []):
        for o in doc.get('oclc', []):
            if o not in oclcs:
                oclcs.append(o)
    return oclcs[:top_n]


def ht_volumes(oclc):
    data = get(HT % oclc, HT_UA)
    rows = []
    records = data.get('records', {})
    for it in data.get('items', []):
        rid = it.get('fromRecord')
        rec = records.get(rid, {})
        rows.append({
            'oclc': oclc, 'record_id': rid, 'htid': it['htid'], 'enumcron': it.get('enumcron') or '',
            'title': (rec.get('titles') or [''])[0], 'publishDates': ','.join(rec.get('publishDates', [])),
        })
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--series-file', help='TSV: series_name<TAB>openlibrary_query per row')
    ap.add_argument('--oclc', action='append', default=[], help='SERIES_NAME=OCLC[,OCLC...], repeatable')
    ap.add_argument('--out', required=True)
    ap.add_argument('--sleep', type=float, default=1.5)
    ap.add_argument('--olkey-max', type=int, default=3, help='top N distinct OCLCs to take per OL query')
    a = ap.parse_args()

    jobs = []  # (series, [oclcs] or None-needing-OL, query)
    if a.series_file:
        with open(a.series_file) as fh:
            for line in fh:
                line = line.rstrip('\n')
                if not line or line.startswith('#'):
                    continue
                series, query = line.split('\t', 1)
                jobs.append((series, None, query))
    for spec in a.oclc:
        series, oclcs = spec.split('=', 1)
        jobs.append((series, oclcs.split(','), None))

    rows = []
    errors = []
    first = True
    for series, oclcs, query in jobs:
        if oclcs is None:
            if not first:
                time.sleep(a.sleep)
            first = False
            try:
                oclcs = ol_oclcs(query, a.olkey_max)
            except Exception as e:
                errors.append('%s: OL error %s' % (series, e))
                continue
            print('%s: OL query %r -> oclcs %s' % (series, query, oclcs), file=sys.stderr)
        for oclc in oclcs:
            time.sleep(a.sleep)
            try:
                vols = ht_volumes(oclc)
            except Exception as e:
                errors.append('%s oclc=%s: HT error %s' % (series, oclc, e))
                continue
            print('%s: oclc %s -> %d volumes' % (series, oclc, len(vols)), file=sys.stderr)
            for v in vols:
                v['series'] = series
                rows.append(v)

    seen = set()
    with open(a.out, 'w', newline='') as fh:
        w = csv.writer(fh, delimiter='\t')
        w.writerow(['series', 'oclc', 'record_id', 'htid', 'enumcron', 'title', 'publishDates'])
        for r in rows:
            if r['htid'] in seen:
                continue
            seen.add(r['htid'])
            w.writerow([r['series'], r['oclc'], r['record_id'], r['htid'], r['enumcron'], r['title'],
                        r['publishDates']])

    print('%d unique htids across %d jobs, %d errors' % (len(seen), len(jobs), len(errors)), file=sys.stderr)
    for e in errors:
        print('ERROR:', e, file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main())
