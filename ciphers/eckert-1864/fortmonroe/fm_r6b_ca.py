#!/usr/bin/env python3
"""FM-R6b (9 Oct 2026): Chronicling America (loc.gov JSON) full-text queries for F1 (5662/0, press telegram 9-10 May 1864) and F2/F3 (June 1864 wire).
>= 2 s apart, descriptive UA. A miss is a search result (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('Heckman splendid charge Swift Creek', '1864-05-10', '1864-05-14'),
     ('Longstreet wounded Jenkins killed Richmond extra Butler enthusiasm', '1864-05-10', '1864-05-13'),
     ('Walthall Brewster magazine gunboat blown up', '1864-05-10', '1864-05-14'),
     ('Fortress Monroe Swift Creek Kautz Gillmore tore up railroad', '1864-05-10', '1864-05-12')]
n = 0
for q, a, b in Q:
    u = 'https://www.loc.gov/collections/chronicling-america/?fo=json&c=8&dates=%s/%s&q=%s' % (a, b, urllib.parse.quote(q))
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90))
    except Exception as e:
        print(q, 'ERR', str(e)[:80]); n += 1; time.sleep(5); continue
    n += 1
    print(q, '| total', d.get('pagination', {}).get('total'))
    for r in d.get('results', [])[:5]:
        print('  ', r.get('date'), r.get('title', '')[:60], r.get('id'))
    time.sleep(2.5)
print('requests', n)
