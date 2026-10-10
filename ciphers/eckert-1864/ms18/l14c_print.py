#!/usr/bin/env python3
"""L14-C: print search for the nine L14-C rows in the cached OR/ORN/Butler djvu texts (sources/ia-fulltext/print-check/*_djvu.txt.gz): letters-only phrase grep
and a date-window search (heading date within +-1 day and two term groups within 700 chars). A miss is a search result (rule 10)."""
import gzip, glob, os, re
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 '9869/4 17 Oct 1864': ['no troops available to reinforce Paducah', 'unless sent from your district', 'assignment of General Meredith', 'not deemed judicious by the War Department', 'require a man of more military experience', 'up the Tennessee can be reached'],
 '9764/1 23 Jun 1864': ['carry out', 'attacked Lynchburg', 'repulsed with considerable loss', 'line of retreat', 'must be made with great caution', 'I have no orders to give'],
 '9897/1 15 Nov 1864': ['Beverly Tucker will cross', 'confidentially informed that Beverly Tucker', 'officer of sufficient discretion', 'dispatched to the falls'],
 '9862/0 7 Oct 1864': ['arms were sent from here to Harpers Ferry', 'been delayed on the Rail Road', 'sent from here to Harpers Ferry on the afternoon', 'no delay'],
 '9885/3 3 Nov 1864': ['think the matter will be settled now without trouble', 'settled now without trouble', 'departure from the command assigned in my order', 'A telegram from General Grant in relation to the troops'],
 '9848/0 21 Sep 1864': ['veteran regiment was sent from here yesterday', 'additional guard for prisoners of war', 'detailed by your direction to await the movement of General Sheridan', 'send them to City Point', 'would not be of much use to him in the pursuit'],
 '9811/0 4 Aug 1864': ['Had you asked my opinion in regard to General Hunter and General Sheridan', 'freely and frankly given', 'beg to be excused from deciding', 'lawfully and properly belong to your office', 'I await your orders and shall strictly carry them out'],
 '9688/0 16 Mar 1864': ['furloughs of veteran regiments', 'about to expire', 'bring any troops North from that Department', 'should not these wagons be retained'],
 '9850/2 26 Sep 1864': ['alleged frauds and inefficiencies', 'frauds and inefficiencies in Arkansas', 'especially at Fort Smith and the Indian Territory', 'full discretion to act'],
}
DW = [('9869/4 Oct 16-18 Paducah/Meredith', r'Oct(ober|\.)?\s+(16|17|18)\W{1,4}\s*1864', ['Paducah|Meredith'], ['Washburn|Halleck|Meredith']),
 ('9764/1 Jun 22-24 Stahel/Lynchburg', r'June?\s+(22|23|24)\W{1,4}\s*1864', ['Stahel'], ['Lynchburg|Hunter|retreat|caution']),
 ('9897/1 Nov 14-16 Tucker/Niagara/Dix', r'Nov(ember|\.)?\s+(14|15|16)\W{1,4}\s*1864', ['Tucker|Niagara'], ['Dix|Dana|Horner']),
 ('9862/0 Oct 6-8 arms Harpers Ferry Garrett', r'Oct(ober|\.)?\s+(6|7|8)\W{1,4}\s*1864', ['Garrett'], ['Harper|arms']),
 ('9885/3 Nov 2-4 Dix/Butler/Grant troops', r'Nov(ember|\.)?\s+(2|3|4)\W{1,4}\s*1864', ['Dix'], ['Butler']),
 ('9848/0 Sep 20-22 Imboden/prisoners/Sheridan', r'Sept(ember|\.)?\s+(20|21|22)\W{1,4}\s*1864', ['Imboden|prisoners'], ['Sheridan|Grant|Halleck']),
 ('9811/0 Aug 3-5 Hunter/Sheridan decide', r'Aug(ust|\.)?\s+(3|4|5)\W{1,4}\s*1864', ['Hunter'], ['Sheridan']),
 ('9688/0 Mar 15-17 furloughs veteran', r'Mar(ch|\.)?\s+(15|16|17)\W{1,4}\s*1864', ['furlough'], ['veteran|Department of the South']),
 ('9850/2 Sep 25-27 Canby Fort Smith frauds', r'Sept(ember|\.)?\s+(25|26|27)\W{1,4}\s*1864', ['Canby'], ['Fort Smith|fraud|Indian Territory'])]
T = {os.path.basename(p)[:-12]: gzip.open(p, 'rt', errors='ignore').read() for p in sorted(glob.glob(D + '/*_djvu.txt.gz'))}
print('volumes searched:', len(T))
nt = {v: norm(t) for v, t in T.items()}
for e, phs in PH.items():
    for ph in phs:
        print('PH', e, '|', ph, '|', ','.join(v for v, t in nt.items() if norm(ph) in t) or 'none')
for v, t in T.items():
    if not re.match(r'(warofrebellion|official|privateofficial|.*butl)', v): continue
    t2 = re.sub(r'\s+', ' ', t)
    for lab, dre, a, b in DW:
        n = h = 0; ex = []
        for m in re.finditer(dre, t2, flags=re.I):
            n += 1; w = t2[max(0, m.start()-150): m.end()+700]
            if all(re.search(x, w, re.I) for x in a) and all(re.search(x, w, re.I) for x in b): h += 1; ex.append(w[:330])
        if h: print(f'DW {v} | {lab} | date headings {n} | with terms {h}')
        for e in ex[:2]: print('     ', e)
