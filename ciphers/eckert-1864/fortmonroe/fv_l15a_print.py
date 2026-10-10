#!/usr/bin/env python3
"""FV-L15a (10 Oct 2026): letters-only phrase grep of E555 E536 E568 E541 E576 E575 decoded phrases over every cached print-check
djvu text (sources/ia-fulltext/print-check: OR I/46 pts 1-3, I/47 pt 2, ORN I/11, Butler Corr. IV-V and the rest), then KWIC for rare
names in the 1865 volumes. A miss is a search result, not a novelty verdict (rule 10). Usage: fv_l15a_print.py"""
import gzip, os, re, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E555 5904/1': ['Meaghers division', "Meagher's division", 'shipped from here and Annapolis', '306 mule teams', '102 horse ambulances',
                 'staff officers 3 or 4 batteries', 'as soon as ships arrive', 'prepared and loaded', 'will sail from here tomorrow morning',
                 'one battery and 440 horses', '440 horses'],
 'E536 5879/0': ['Fort Fisher is ours', 'adjacent defenses of New Inlet', 'well sustained assault', 'Bell and Pennypacker',
                 'bright flash was seen', 'stunning report', 'nothing could withstand the bravery', 'picked South and North Carolina',
                 'powder magazine just outside', 'Vanderbilt was leaving', 'had expressed the belief that it was impregnable'],
 'E568 5923/1': ['double line from here to Goldsboro', 'double line from Morehead City', 'construction parties', 'good foreman',
                 'vices and straps', 'difficulty of getting operators', 'hurry the operators and instruments', 'line be built at once'],
 'E541 5887/0': ['steamer Nevada', 'Nevada will be at', 'Stromboli', 'no torpedoes of the kind', 'take months to prepare',
                 'for what purpose these are intended', 'rebel torpedoes on hand', 'sea going steam vessels', 'Commander Lynch', 'St Lawrence'],
 'E576 5933/0': ['guide Boyle', 'Broad Ford', 'Blackwater can be crossed', 'without bridging', 'twenty two miles from Suffolk',
                 '22 miles from Suffolk', '125 yards wide', 'one hundred and twenty five yards', 'Nottoway has several bridges'],
 'E575 5931/1': ['how much water can your gunboats', 'banks of the Nansemond', 'cavalry could land', 'carry pontoons',
                 'leave word where they had better land', 'come up tonight', 'come up to night', 'send answer to Mr Emerick', '500 cavalry'],
}
texts = {os.path.basename(p)[:-12]: gzip.open(p, 'rt', errors='ignore').read() for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz')))}
N = {k: norm(v) for k, v in texts.items()}
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [f'{v}[{t.count(norm(ph))}]' for v, t in N.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
Y65 = ['warofrebellion461unit', 'warofrebellion014602rootrich', 'warofrebellion463unit', 'warofrebellion431unit', 'officialrecordso0011unse',
       'privateofficialc05butl']
for name, rx in [('Meagher', r'Jan|Feb|Schofield|Annapolis|Rucker'), ('Rucker', r'Feb|Schofield|Annapolis|Meagher'),
                 ('Pennypacker', ''), ('Vanderbilt', r'Fisher|Jan'), ('Morehead', r'March|Mar\.|Goldsborough|Goldsboro|line|telegraph'),
                 ("O'Brien", r'telegraph|line|operator'), ('Stromboli', ''), ('Nevada', r'Jan|Monroe|recruit'), ('torpedoes', r'Lynch|Wise|Saint Lawrence|St\. Lawrence'),
                 ('Lynch', r'torpedo|Lawrence|Norfolk'), ('Boyle', r'guide|Gordon|Blackwater'), ('Broad Ford', ''), ('Nansemond', r'March|cavalry|gunboat|Gordon|Ord'),
                 ('Emerick', ''), ('pontoon', r'Gordon|Suffolk|Nansemond|Blackwater')]:
    for v in Y65:
        if v not in texts: continue
        t = texts[v]
        for m in list(re.finditer(re.escape(name), t))[:12]:
            ctx = ' '.join(t[max(0, m.start()-240):m.start()+280].split())
            if rx and not re.search(rx, ctx): continue
            print('KWIC', name, v, m.start(), '::', ctx)
