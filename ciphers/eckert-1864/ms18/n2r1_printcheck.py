#!/usr/bin/env python3
"""N2R-1 (10 Oct 2026): letters-only phrase grep of the ten N2R-1 rows' decoded phrases in the cached OR djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 9879/0': ['credibly reported to this Department', 'ballot-box stuffer', 'ballot box stuffer', 'engaged in frauds and forgeries', 'criminal operations'],
 'F2 9767/1': ['great accumulation of sick and wounded', 'hospital transports fit to carry them by sea', 'one service or duty must wait upon the other', 'more urgent than the New Orleans service'],
 'F3 9690/0': ['furloughed regiments', 'dismounted at St. Louis', 'have been diverted', 'interfere with his movements', 'rendezvous here'],
 'F4 9680/1': ['much anxiety is felt here about', 'will be so ordered as fast as reported ready', 'Johnston has ordered the evacuation', 'nothing of any movement on Selma'],
 'F5 9905/1': ['will be disembarked at once', 'will arrive here Tuesday', 'Third Division will arrive here', 'Rawlins, Chief of Staff'],
 'F6 9807/0': ['fit for carrying cavalry and infantry', 'not otherwise employed', 'does it need new and further provision of vessels', 'provision of vessels'],
 'F7 9782/2': ['serious defeat at Monocacy Junction', 'is in full retreat', 'Ricketts\' division is covering his retreat', 'covering his retreat', 'estimates the enemy\'s force'],
 'F8 9916/2': ['are ordered to report to', 'Cossack', 'Guide, Cossack', 'T. Collyer', 'Escort, Louise'],
 'F9 9690/2': ['regiments of heavy artillery', 'numbering about 3,000 men', 'can be replaced by men from other forts', 'where they are to land'],
 'F10 9798/0': ['Purcellville', 'formed a junction yesterday', 'taking about 60 prisoners', 'Snicker\'s Gap'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = norm(gzip.open(p, 'rt', errors='ignore').read())
for p in sys.argv[1:]:
    texts[os.path.basename(p)[:-4]] = norm(open(p, errors='ignore').read())
print('volumes searched:', len(texts), ' '.join(sorted(v for v in texts if 'warofrebellion' in v)))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in texts.items() if norm(ph) in t and 'warofrebellion' in v]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
