#!/usr/bin/env python3
"""FV-FM65a (10 Oct 2026): letters-only phrase grep of E504 E516 E519 E531 E534 E535 decoded phrases over the cached print-check djvu texts
(sources/ia-fulltext/print-check) plus scratch *.txt given as argv (OR I/46 pts 1-3, I/47 pts 1-2, ORN I/11), then KWIC for rare
names in the argv volumes. A miss is a search result, not a novelty verdict (rule 10). Usage: fv_fm65a_print.py SCRATCH/*.txt"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E504 5851/0': ['ordered to report to Colonel Bradley', 'Euterpe', 'Weybossett', 'Weybosset', 'Towanda', 'H. Livingston', 'draws too much water',
                 'rationed for 1400', 'Prometheus', 'DeMolay', 'De Molay'],
 'E516 5860/1': ['overcoat pocket', 'large package of papers', 'report of the Wilmington expedition', 'kept by Mr Phillips', 'had my coat off',
                 'inquiries made at both places'],
 'E519 5866/0': ['soonest ship troops', 'use your own judgment after seeing the captain', 'cannot approach the docks at Annapolis',
                 'coal at Annapolis', 'more readily at Baltimore'],
 'E531 5873/1': ['Suwo Nada', 'Oriental has sailed', 'will start in half an hour', 'this makes six vessels', 'all as ordered'],
 'E534 5877/2': ['Haze and Sentinel', 'are all we have', 'sufficient for the teams', 'have you nothing at City Point', 'fifteen days rations on such',
                 'as the quartermaster designates', 'how many men each vessel will carry', 'as each vessel is rationed'],
 'E535 5878/1': ['returned from the expedition disabled', 'enough are here to carry', 'ready by tomorrow noon', 'when each vessel leaves here',
                 'Fort Fisher news change your instructions', 'in regard to mortars'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = gzip.open(p, 'rt', errors='ignore').read()
extra = []
for p in sys.argv[1:]:
    k = os.path.basename(p)[:-4]; texts[k] = open(p, errors='ignore').read(); extra.append(k)
N = {k: norm(v) for k, v in texts.items()}
print('volumes searched:', len(texts), '(argv:', ' '.join(extra) + ')')
for e, phs in PH.items():
    for ph in phs:
        hits = [f'{v}[{t.count(norm(ph))}]' for v, t in N.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
for name in ['Euterpe', 'Weybosset', 'Towanda', 'Suwo Nada', 'Sentinel', 'Haze', 'overcoat', 'Phillips', 'Baltic', 'mortars', 'disabled',
             'Howell', 'Bradley', 'Small']:
    for v in extra:
        t = texts[v]
        for m in list(re.finditer(re.escape(name), t))[:6]:
            ctx = ' '.join(t[max(0, m.start()-220):m.start()+260].split())
            if name in ('Phillips', 'Baltic', 'mortars', 'disabled', 'Howell', 'Bradley', 'Small', 'Haze', 'Sentinel') and not re.search(r'Jan|January|Monroe|City Point|Sheldon|Morgan|Rawlins|Beckwith', ctx):
                continue
            print('KWIC', name, v, m.start(), '::', ctx)
