#!/usr/bin/env python3
"""Match mssEC 15 ledger pages (volunteer transcription, Huntington CONTENTdm `text` field) to Official Records
ser. I volume full text (Internet Archive _djvu.txt) by shared word 5-grams. GAPS113, 3 Oct 2026.

Usage: or_match.py PAGES_DIR OR_DIR [--min 6] > or_matches.tsv
  PAGES_DIR: <pointer>.json per page from https://hdl.huntington.org/digital/api/collections/p16003coll11/items/<pointer>/false
  OR_DIR: <ia_identifier>.txt from https://archive.org/download/<id>/<id>_djvu.txt
Not committed: the page texts (volunteer transcription, their credit) and the OR text (re-fetch). A 5-gram that occurs
more than 8 times across all volumes is treated as a formula and ignored. A page/volume pair is reported when >= --min
distinct 5-grams fall in one 400-word block of the volume. Calibration (3 Oct 2026): pairs that cannot be the same
telegram (vol. 7 against ledger pages after March 1862) share at most 3; T1/T2 against vol. 7 share 21 and 74.
"""
import json, re, glob, os, sys, collections, argparse
ap = argparse.ArgumentParser(); ap.add_argument('pages'); ap.add_argument('ordir'); ap.add_argument('--min', type=int, default=6)
a = ap.parse_args(); N = 5
def words(t):
    t = re.sub(r'<[^>]+>', ' ', t.lower().replace('&', ' and '))
    return re.findall(r'[a-z]+', t)
pages = {}
for f in sorted(glob.glob(os.path.join(a.pages, '*.json'))):
    try: d = json.load(open(f))
    except Exception: continue
    pages[int(os.path.basename(f)[:-5])] = (d.get('title') or '', d.get('text') or '')
vols, vline = {}, {}
HDR = re.compile(r'^\s*(\d{1,4})\s+[A-Z][A-Z .,\'-]{6,}|[A-Z.\]]\s+(\d{1,4})\s*$')
for f in sorted(glob.glob(os.path.join(a.ordir, '*.txt'))):
    v = os.path.basename(f)[:-4]; ws, pg, cur = [], [], ''
    for line in open(f, errors='ignore'):
        m = HDR.search(line)
        if m: cur = m.group(1) or m.group(2)
        w = words(line); ws += w; pg += [cur] * len(w)
    vols[v], vline[v] = ws, pg
idx = collections.defaultdict(list)
for v, w in vols.items():
    for i in range(len(w) - N + 1): idx[' '.join(w[i:i + N])].append((v, i))
common = {g for g, l in idx.items() if len(l) > 8}
print('pointer\tpage_title\tledger_head\tvolume\tor_page\tshared_5grams\tor_context')
for p, (title, text) in sorted(pages.items()):
    w = words(text); hits = collections.defaultdict(set); first = {}
    for i in range(len(w) - N + 1):
        g = ' '.join(w[i:i + N])
        if g in idx and g not in common:
            for v, j in idx[g]:
                hits[(v, j // 400)].add(g); first.setdefault((v, j // 400), j)
    best = {}
    for (v, b), gs in hits.items():
        if len(gs) >= a.min and len(gs) > best.get(v, (0,))[0]: best[v] = (len(gs), first[(v, b)])
    for v, (n, j) in sorted(best.items()):
        head = ' '.join(text.split('\n')[:2])[:60]
        print(f"{p}\t{title}\t{head}\t{v}\t{vline[v][j]}\t{n}\t{' '.join(vols[v][max(0, j - 20):j + 25])}")
