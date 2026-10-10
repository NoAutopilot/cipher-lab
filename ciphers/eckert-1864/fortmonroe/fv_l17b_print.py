#!/usr/bin/env python3
"""FV-L17b (10 Oct 2026; copied from fv_l17a_print.py): letters-only phrase grep of E589-E594 decoded phrases over every cached print-check djvu
text (sources/ia-fulltext/print-check: OR I/46 pts 1-3, I/47 pts 2-3, ORN I/11-12, Butler Corr. IV-V and the rest), then KWIC for names in the
Feb-Mar 1865 volumes. A miss is a search result, not a novelty verdict (rule 10). Usage: fv_l17b_print.py"""
import gzip, os, re, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E589 5892/1': ['Monohansett will leave', 'will leave for Fort Monroe about', 'wishes you to meet him on arrival', 'to meet him on arrival', 'meet him on his arrival'],
 'E590 5896/0': ['I have sent the letter referred to', 'the letter referred to in our dispatch', 'by the hands of a staff officer', 'I retained no copy',
                 'retained no copy', 'by hands of a staff officer', 'to be delivered to you'],
 'E591 5908/0': ['no torpedoes on hand', 'telegraphed the Bureau of Ordnance', 'will forward immediately on receipt', 'forward immediately on receipt',
                 'Bureau of Ordnance for twenty', 'for 20 torpedoes', 'twenty torpedoes'],
 'E592 5910/1': ['Camman and Company', 'Camman & Co', 'Camman', 'sell gold', 'he is naval officer', 'he is a naval officer'],
 'E593 5936/2': ['ponchos are not on hand', 'the ponchos', 'ponchos', 'if that will suffice', 'are not on hand at present', 'on Sheridans arrival'],
 'E594 5941/2': ['I am going to see General Grant', 'expect to go back to Goldsboro', 'go back to Goldsborough', 'by way of New Berne from Old Point',
                 'from Old Point on Wednesday', 'Old Point on Wednesday', 'back to Goldsborough by way of'],
}
texts = {os.path.basename(p)[:-12]: gzip.open(p, 'rt', errors='ignore').read() for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz')))}
N = {k: norm(v) for k, v in texts.items()}
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [f'{v}[{t.count(norm(ph))}]' for v, t in N.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
Y65 = ['warofrebellion461unit', 'warofrebellion014602rootrich', 'warofrebellion462unit', 'warofrebellion463unit', 'warofrebellion431unit',
       'warofrebellion014703rootrich', 'officialrecordso0011unse', 'officialrecords10librgoog', 'officialrecordso0012unse', 'privateofficialc05butl']
print('Y65 present:', [v for v in Y65 if v in texts])
for name, rx in [('Monohansett', r'1865|February|Feb'), ('Secretary of State', r'Grant|staff officer|letter'), ('Lynch', r'torpedo|Radford|Ordnance'),
                 ('torpedoes', r'Radford|Ironsides|Lynch|requisition'), ('Camman', ''), ('Cooper', r'gold|naval officer|Norfolk|Monroe'),
                 ('ponchos', ''), ('Ingalls', r'ponchos|Sheldon|Canby'), ('John Sherman', r'Old Point|Goldsboro|City Point|Grant|March'),
                 ('Old Point', r'Sherman|Goldsboro|Wednesday'), ('Goldsborough', r'Old Point|Wednesday|City Point|New Berne')]:
    for v in Y65:
        if v not in texts: continue
        t = texts[v]
        for m in list(re.finditer(re.escape(name), t))[:40]:
            ctx = ' '.join(t[max(0, m.start()-240):m.start()+280].split())
            if rx and not re.search(rx, ctx): continue
            print('KWIC', name, v, m.start(), '::', ctx)
