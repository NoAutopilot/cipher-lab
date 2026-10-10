#!/usr/bin/env python3
"""L14-B (LEDGER-14): print search for the 8 rows E610-E617 in the cached OR/ORN djvu texts (sources/ia-fulltext/print-check/*.gz, 177 volumes):
letters-only phrase grep per row, plus a date + correspondent window search. A miss is a search result (rule 10), never a novelty verdict."""
import gzip, glob, os, re
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
ROWS = {
 'E610 9787/1': (['Hunter','Howe','Wright'], r'July\s+11\W{1,4}\s*1864', ['form a junction with General Howe','hold Maryland Heights and move down the Potomac','a junction with General Wright at or near Edwards Ferry','important that this junction be formed as early as possible','heavy force in the enemy\'s rear so as to intercept his retreat','retire above Harper\'s Ferry']),
 'E611 9733/1': (['Brown','Biggs','forage'], r'May\s+7\W{1,4}\s*1864', ['daily shipments of forage to Monroe should average','27,000 bushels of grain and 350 tons of hay','consign this forage to Colonel Biggs','supply at this point has lately been low','Brown assistant quartermaster in charge of forage New York']),
 'E612 9883/0': (['Allen','Ferry','Memphis'], r'N[ao]v(?:ember|\.)?\s+1\W{1,4}\s*1864', ['arrest him and report to the Secretary of War','Captain Ferry to Memphis without a day\'s delay','is not satisfied with your conduct','Secretary of War informs me that many days since','Captain Ferry has not yet gone to Memphis']),
 'E613 9802/1': (['Johnson','Gillem','Schurz'], r'July\s+2[78]\W{1,4}\s*1864', ['find a place for an officer of so high rank','appreciate him certainly as highly as you do','Carl Schurz','General A. C. Gillem just received','no place seeking him']),
 'E614 9874/2': (['Brown','Van Vliet','Hilton Head'], r'Oct(?:ober|\.)?\s+2[123]\W{1,4}\s*1864', ['shipment of supplies suspended by my telegraphic dispatch','sent to Hilton Head to be stored there','held afloat for instant transfer','storehouses are filled','Colonel Brown and Major Van Vliet']),
 'E615 9779/0': (['Hunter','Breckenridge','Frederick'], r'July\s+[89]\W{1,4}\s*1864', ['report the positions and numbers of your forces and when they will reach Harper\'s Ferry','has crossed the Monocacy','Boonsborough and Middletown on Frederick','unless your forces move forward rapidly they will not be in time','Breckenridge has crossed the Monocacy']),
 'E616 9743/1': (['Hunter','brigadier','cavalry'], r'May\s+2[234]\W{1,4}\s*1864', ['no vacant brigadier-generalships of volunteers','you have three generals of cavalry in your department','mustered out and I will endorse it','till some one else is mustered out','certainly enough for your cavalry force']),
 'E617 9686/2': (['Smith','Quadrant','Halleck'], r'March\s+(?:4|14)\W{1,4}\s*1864', ['nor any officer under your command will exercise authority over any troops not within the limits of your department','neither yourself nor any officer under your command','immediately revoked','assuming command of troops outside of such boundaries','when the order establishing it was received']),
}
T = {os.path.basename(p)[:-12]: gzip.open(p, 'rt', errors='ignore').read() for p in sorted(glob.glob(D + '/*_djvu.txt.gz'))}
print('volumes searched:', len(T))
for row, (terms, drx, ph) in ROWS.items():
    print('==', row)
    for p in ph:
        hits = [v for v, t in T.items() if norm(p) in norm(t)]
        print('PHRASE |', p, '|', ','.join(hits) or 'none')
    for v, t in T.items():
        if not v.startswith(('warofrebellion', 'officialrecords', 'ornavy', 'privateoff', 'official')): continue
        t2 = re.sub(r'\s+', ' ', t); n = h = 0; ex = []
        for m in re.finditer(drx, t2, flags=re.I):
            n += 1; w = t2[max(0, m.start()-200):m.end()+700]
            if sum(1 for x in terms if re.search(x, w, re.I)) >= 2: h += 1; ex.append(w[:480])
        if h: print(f'DATE | {v} | headings {n} | with >=2 of {terms}: {h}')
        for e in ex[:2]: print('     ', e)
