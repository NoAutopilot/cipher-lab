#!/usr/bin/env python3
"""AUD2-LEDGER15-1 (10 Oct 2026): KWIC over the print-check cache for the second audit of E555 E568 E541 E576 E575 -- ORN I/12
(officialrecords10librgoog, cached this session), Plum vol. II (militarytelegraph02plumrich), J. E. O'Brien, Telegraphing in Battle 1910
(telegraphinginba00obri), G. H. Gordon, A War Diary of Events 1882 (wardiaryevents00gordrich), and the Gordon/Ord telegrams of 14-16 Mar 1865 in OR I/46 pts 2-3. Writes aud2_l15_1_print.out.
A miss is a search result, not a novelty verdict (rule 10). Usage: aud2_l15_1_print.py"""
import gzip, os, re
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aud2_l15_1_print.out')
T = lambda i: ' '.join(gzip.open(os.path.join(D, i + '_djvu.txt.gz'), 'rt', errors='ignore').read().split())
TERMS = {'officialrecords10librgoog': ['Nansemond', 'Stromboli', 'Lynch', 'Suffolk', 'Blackwater', 'Nottoway', 'Boyle', 'Broad Ford', "O'Brien",
                                       'telegraph line', 'Meagher', 'Nevada', 'Sumner', 'Gordon, G.H.'],
         'militarytelegraph02plumrich': ["O'Brien", 'relays', 'Nansemond', 'Boyle', 'Stromboli', 'Meagher', 'Wilmington via Fort Fisher'],
         'telegraphinginba00obri': ['February 26th', 'diggers', 'shovels', 'double line', 'difficulty of getting', 'hurry the operators',
                                    'Boyle', 'Stromboli', 'Meagher', 'Sumner', 'Broad Ford', 'Nottoway'],
         'wardiaryevents00gordrich': ['Boyle', 'Broad Ford', 'Blackwater', 'Nottoway', 'South Quay', 'Sumner', 'Nansemond']}
with open(OUT, 'w') as f:
    for ident, terms in TERMS.items():
        t = T(ident)
        for k in terms:
            hs = [m.start() for m in re.finditer(re.escape(k), t)]
            f.write(f'{ident}\t{k}\t{len(hs)}\n')
            for h in hs[:3]: f.write('    :: ' + t[max(0, h - 200):h + 300] + '\n')
    for ident in ('warofrebellion014602rootrich', 'warofrebellion463unit'):
        t = T(ident)
        for m in re.finditer(r'March 1[456], 1865', t):
            seg = t[m.start() - 60:m.start() + 900]
            if re.search(r'GORDON|Gordon', seg[:200]) or 'Boyle' in seg or 'Blackwater' in seg[:400]:
                f.write(f'{ident}\tGordon/Ord window\n    :: {seg}\n')
print(open(OUT).read()[:3000])
