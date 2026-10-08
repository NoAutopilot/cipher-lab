#!/usr/bin/env python3
"""FM-R2a (8 Oct 2026): letters-only phrase grep of the FM-R2a entries' hand-read phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments); prints volume, offset and a 140-char context of the first hit.
A miss is a search result, not a verdict (rule 10). Usage: python3 fm_r2a_printcheck.py [extra.txt ...]"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5806/1 E170': ['would be killed if sent without stalls', 'horses of one battery', 'steamer Babcock', 'broke down off the capes', 'only four pieces of artillery remain'],
 'F2 5779/1 E171': ['arrived at Port Royal in steamer Arago', 'Arago with the 103d New York', 'wait as ordered two hours for orders', 'W. Heine', 'Colonel Heine'],
 'F3 5787/2 E172': ['extend the railroad beyond Warren Station to Peebles House', 'beyond Warren to Peebles House', 'sending ties to Alexandria', 'E. L. Wentz', 'Peebles House'],
 'F4 5840/0 E173': ['No troops had landed', 'forty days rations have been sent since the expedition sailed', 'no ordnance stores sent yet', 'large supply of ammunition at Newbern', 'No orders were left here about it'],
 'F5 5747/2 E174': ['am sawing two inch lumber', 'all ferry boats to', 'list of vessels containing lumber', 'sent over 200,000 feet of lumber', 'as fast as possible will continue to forward'],
 'F6 5838/0 E175': ['journal brasses cut', 'Pontoosuc most anxious to join', 'Saugus at Norfolk ready for sea', 'send Pontoosuc or Nereus with her', 'can not go to sea under four days'],
 'F7 5820/0 E176': ['second Division Twenty-fourth Corps will embark', 'Louisa Moore', 'Weybosset', 'steamers Hayes', 'Idaho, 350'],
 'F8 5823/0 E177': ['hold the Dupont at Fortress Monroe', 'Albany and United States leave immediately', 'get two good ocean steamers and have them ready', 'remaining infantry to Fort Monroe on river steamers'],
 'F9 5838/2 E178': ['City of Albany, Hero of Jersey', 'Hero of Jersey', 'C. Vanderbilt and Mary Washington', 'ordered to Hilton Head in obedience to dispatch of the 17th', 'prospects are fair for their getting out tonight'],
 'F10 5600/0 E179': ['shelter tents at once to fill requisition', 'City of Norwich or George Leary', 'George Leary', 'drawing not over nine feet', 'large amount of water'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = gzip.open(p, 'rt', errors='ignore').read()
for p in sys.argv[1:]:
    texts[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
N = {v: norm(t) for v, t in texts.items()}
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in N.items() if norm(ph) in t]
        ctx = ''
        if hits and len(norm(ph)) > 14 and len(hits) <= 3:
            v = hits[0]; i = N[v].find(norm(ph)); ctx = ' ~ ' + N[v][max(0, i-30):i+60]
        print(e, '|', ph, '|', ','.join(hits[:6]) + (' +%d' % (len(hits)-6) if len(hits) > 6 else '') or 'none', ctx)
