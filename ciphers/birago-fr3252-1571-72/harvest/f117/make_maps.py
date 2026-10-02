#!/usr/bin/env python3
"""Sign-id maps for the f.117r first test (NEVBIR-3252-B, 2 Oct 2026). Reads the 1572 group's printed map
(../../../nevers-birago-fr3251-1572/harvest/sign_id_map_1572.json, Tomokiyo's printed table cut to the blind sheet) and
writes three variants beside this script: map_printed.json (as printed), map_T42m.json (T42 = m, GAPS3/87ALIGN),
map_clerkvar.json (the C-grade clerk-sheet variant NEVBIR-87ALIGN applied: T42 m, T50 s, T95 l, from
keys/key_1572_clerk.tsv rows with applied=yes), map_T88q.json (T88 = q: a value FITTED on f.117 itself by
decode_control.py --fit-sign T88 --fit-values q, best single letter; post-hoc, not pre-registered).  python3 make_maps.py [--check]"""
import csv, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
G = os.path.join(HERE, '../../../nevers-birago-fr3251-1572')
base = json.load(open(os.path.join(G, 'harvest/sign_id_map_1572.json')))
clerk = {r['sign']: r['value'] for r in csv.DictReader(open(os.path.join(G, 'keys/key_1572_clerk.tsv')), delimiter='\t')
         if r['applied'] == 'yes' and r['sign'].startswith('T')}
def variant(over):
    return [dict(e, value=over.get(e['id'], e['value'])) for e in base]
out = {'map_printed.json': variant({}), 'map_T42m.json': variant({'T42': 'm'}), 'map_clerkvar.json': variant(clerk),
       'map_T88q.json': variant({'T88': 'q'})}
stale = 0
for fn, data in out.items():
    p = os.path.join(HERE, fn); txt = json.dumps(data, indent=0)
    if '--check' in sys.argv:
        stale += (not os.path.exists(p) or open(p).read() != txt)
    else:
        open(p, 'w').write(txt)
print('clerk overrides:', clerk); sys.exit(1 if stale else 0)
