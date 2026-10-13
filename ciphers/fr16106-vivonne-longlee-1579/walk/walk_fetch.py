#!/usr/bin/env python3
"""VIV-WALK (13 Oct 2026): fetch 600-px canvas overviews of BnF fr.16107 / fr.16108 from openapi.bnf.fr (IIIF Image v3),
one at a time, >= 3 s apart, into images/walk/ (untracked: no image goes into git), appending one JSON line per fetch to
walk/fetch_log.jsonl (url, date, bytes, sha1, http). Re-running with the same list re-derives every overview (skips files present).
  python3 walk/walk_fetch.py walk/canvas_list.tsv [--max N]
canvas_list.tsv: volume<TAB>canvas. On 403/429/5xx or a non-JPEG body: one retry after 60 s, then stop (exit 2)."""
import sys, os, time, json, hashlib, datetime, urllib.request, argparse
ARK = {'16107': 'btv1b9009661v', '16108': 'btv1b9009660f'}
UA = 'cipher-lab research script (contact via repository)'
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
ap = argparse.ArgumentParser(); ap.add_argument('lst'); ap.add_argument('--max', type=int, default=200); a = ap.parse_args()
out = os.path.join(root, 'images', 'walk'); os.makedirs(out, exist_ok=True)
log = open(os.path.join(here, 'fetch_log.jsonl'), 'a'); n = 0
def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as r: return r.status, r.read()
    except urllib.error.HTTPError as e: return e.code, b''
    except Exception as e: return 0, b''
for line in open(a.lst):
    v, c = line.split()[:2]
    fn = os.path.join(out, f'fr{v}_c{int(c):03d}.jpg')
    if os.path.exists(fn): continue
    if n >= a.max: break
    url = f'https://openapi.bnf.fr/iiif/image/v3/ark:/12148/{ARK[v]}/f{c}/full/600,/0/default.jpg'
    st, b = get(url); n += 1
    if st != 200 or b[:2] != b'\xff\xd8':
        print('retry after 60 s', v, c, st, flush=True); time.sleep(60); st, b = get(url); n += 1
        if st != 200 or b[:2] != b'\xff\xd8':
            log.write(json.dumps({'url': url, 'http': st, 'stopped': True}) + '\n'); print('STOP', st); sys.exit(2)
    open(fn, 'wb').write(b)
    log.write(json.dumps({'file': 'images/walk/' + os.path.basename(fn), 'url': url, 'http': st, 'bytes': len(b),
        'sha1': hashlib.sha1(b).hexdigest(), 'date': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}) + '\n'); log.flush()
    print(v, c, st, len(b), flush=True); time.sleep(3.2)
print('requests', n)
