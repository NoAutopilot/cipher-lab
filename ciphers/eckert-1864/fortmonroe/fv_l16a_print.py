#!/usr/bin/env python3
"""FV-L16a (10 Oct 2026): letters-only phrase grep of E509 E511 E514 E506 E508 E521 decoded phrases over every cached print-check djvu
text (sources/ia-fulltext/print-check: OR I/46 pts 1-3, I/42 pt 3, I/47 pt 2, ORN I/11-12, Butler Corr. IV-V and the rest), then KWIC for
vessel and person names in the Dec 1864-Jan 1865 volumes. A miss is a search result, not a novelty verdict (rule 10). Usage: fv_l16a_print.py"""
import gzip, os, re, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E509 5854/0': ['Ben De Ford is not here', 'Ben Deford is not here', 'full list was sent to', 'Ainsworth has a copy', 'ordered to send the C C Leary',
                 'Montauk is there', 'telegraph Bradley at once', 'no other vessel here except', 'except the Alliance', 'Western Metropolis',
                 'fully comply with the orders'],
 'E511 5855/2': ['light draft steamers', 'light-draught steamers', 'not over five feet', 'standing rough weather', 'stand rough weather',
                 'Eliza Hancox', 'Winants', 'held in readiness at Monroe', 'good supply of coal', 'whether these vessels are available'],
 'E514 5858/0': ['three hundred and fifty troops', '350 troops', 'for whom there is no transportation', 'sent in a river steamer',
                 'sea going steamer in time', 'in time to sail with the rest', 'required for special service', 'dispense with the Blackstone',
                 'turn her over to the medical department', 'turn over to the medical department'],
 'E506 5852/1': ['steamers named in your dispatch', 'have started yet for this point', 'not yet been reported from Jamestown',
                 'reported from Jamestown', 'General Rawlins wishes to know'],
 'E508 5853/1': ['Leary is just in', 'leaves immediately for City Point', 'answers the description you required', 'ten days coal',
                 'spare the Montauk', 'we need her here'],
 'E521 5861/2': ['if General Butler has left Monroe', 'Butler has left', 'when bound', 'do not mention that I inquired', "don't mention that I",
                 'that I enquired', 'keep me posted'],
}
texts = {os.path.basename(p)[:-12]: gzip.open(p, 'rt', errors='ignore').read() for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz')))}
N = {k: norm(v) for k, v in texts.items()}
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [f'{v}[{t.count(norm(ph))}]' for v, t in N.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
Y65 = ['warofrebellion423unit', 'warofrebellion461unit', 'warofrebellion014602rootrich', 'warofrebellion462unit', 'warofrebellion431unit',
       'officialrecordso0011unse', 'officialrecords10librgoog', 'privateofficialc05butl']
print('Y65 present:', [v for v in Y65 if v in texts])
for name, rx in [('De Ford', ''), ('Deford', ''), ('DeFord', ''), ('Leary', ''), ('Montauk', r'steamer|transport|Jan|Monroe|City Point'),
                 ('Hancox', ''), ('Winants', ''), ('Blackstone', r'steamer|medical|hospital|Jan'), ('Western Metropolis', ''),
                 ('Ainsworth', ''), ('Alliance', r'steamer|transport|Monroe|Jan'), ('Howell', r'quartermaster|Q\. ?M|City Point|steamer'),
                 ('Dodge', r'quartermaster|Q\. ?M|transport|steamer'), ('light-draught', r'Jan|Monroe|steamer'), ('light draught', r'Jan|Monroe|steamer'),
                 ('has left Fort Monroe', ''), ('left Fort Monroe', r'Butler'), ('Jamestown', r'steamer|Jan|report'),
                 ('Webster', r'quartermaster|Q\. ?M|Monroe|steamer')]:
    for v in Y65:
        if v not in texts: continue
        t = texts[v]
        for m in list(re.finditer(re.escape(name), t))[:15]:
            ctx = ' '.join(t[max(0, m.start()-240):m.start()+280].split())
            if rx and not re.search(rx, ctx): continue
            print('KWIC', name, v, m.start(), '::', ctx)
