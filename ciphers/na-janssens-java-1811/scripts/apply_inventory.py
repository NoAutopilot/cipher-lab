#!/usr/bin/env python3
"""Apply leaves_186-215_inventory.tsv (GAPS5, 2 Oct 2026) to images/manifest.json in place.

For each inventoried leaf: fill the IIIF/thumbnail ids and the local file fields from disk (and from the
invnr @12 page's scan list where the manifest row had none), and where the inventory's class or heading
disagrees with the earlier eye_check, move the old text to `eye_check_prev` (kept, never deleted) and
write the inventory row's reading as the new `eye_check`, tagged with the pass that made it.
    python3 scripts/apply_inventory.py [--scans scans.json]   # run from the target folder
"""
import csv, json, os, sys, argparse
ap = argparse.ArgumentParser(); ap.add_argument('--scans', default=None); ap.add_argument('--tsv', default='leaves_186-215_inventory.tsv')
a = ap.parse_args()
m = json.load(open('images/manifest.json'))
scans = {}
if a.scans and os.path.exists(a.scans):
    for k, v in json.load(open(a.scans)).items():
        scans[int(k)] = v
rows = {int(r['leaf']): r for r in csv.DictReader(open(a.tsv), delimiter='\t')}
by_order = {e['order']: e for e in m['leaves']}
changed = []
for leaf, r in sorted(rows.items()):
    e = by_order[leaf]
    s = scans.get(leaf)
    if s:
        e.setdefault('label', s['label']); e.setdefault('thumbnail_url', s['thumbnail']['url']); e.setdefault('iiif_info_url', s['iiif']['url'])
    for suf, key in (('', 'local_thumb'), ('_med', 'local_med'), ('_hi', 'local_hires_2561')):
        p = f'images/{leaf}{suf}.jpg'
        if os.path.exists(p):
            e[key] = p
        elif suf == '' and e.get('local_thumb') and not os.path.exists(e['local_thumb']):
            e['local_thumb'] = None
    new = f"{r['class']} ({r['confidence']}): heading {r['heading']}; no. {r['number']}; L: {r['left_page']}; R: {r['right_page']}; {r['note']}"
    old = e.get('eye_check', '')
    if r.get('changed', '').strip().lower() in ('yes', 'y', '1', 'true'):
        e['eye_check_prev'] = old
        e['eye_check'] = new + ' [GAPS5 re-inventory, 2 Oct 2026; replaces the eye_check_prev text]'
        changed.append(leaf)
    else:
        e['inventory_2oct_GAPS5'] = new
m['note_2oct_GAPS5'] = ('leaves 186-215 re-inventoried from contact sheets of the best file on disk per leaf (hi where it exists, else '
                        'medium) by four blind vision passes (leaves_186-215_inventory.tsv); 197 and 202-207 fetched at IIIF full/1200 this pass; '
                        'rows whose class or heading the earlier eye_check had wrong carry the old text in eye_check_prev: leaves ' + ', '.join(map(str, changed)))
json.dump(m, open('images/manifest.json', 'w'), indent=1, ensure_ascii=False)
print('updated', len(rows), 'rows; eye_check replaced on', changed)
