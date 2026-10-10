#!/usr/bin/env python3
"""N2R-5 (10 Oct 2026): IA be-api full-text snippet search of Official Records volumes (identifiers of eckert-1862/ec18/or_volumes.tsv) for the N2R-5 rows, by
distinctive term bags in the volumes of the entry's date; >= 1.8 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
V = lambda k: {'32.2':'warofrebellion322unit','32.3':'warofrebellion323unit','33':'warofrebellion33unit','34.3':'warofrebellion013403rootrich','34.4':'warofrebellion013404rootrich',
 '36.2':'warofrebellion362unit','36.3':'warofrebellion363unit','37.1':'warofrebellion371unit','37.2':'warofrebellion372unit','40.2':'warofrebellion402unit','40.3':'warofrebellion403unit',
 '42.3':'warofrebellion423unit','42.2':'warofrebellion422unit','41.4':'warofrebellion414unit'}[k]
Q = [('Z1 9678/0 20 Feb 1864', ['32.2','32.3'], 'authorizing an Inspector to send for persons and take evidence Court of Inquiry Halleck Grant Nashville'),
 ('Z2 9757/1 11 Jun 1864', ['36.3','36.2'], 'McCook Hurlbut will be ordered to report Corps has been temporarily abolished open the railroad further than Monroe Halleck Canby'),
 ('Z3 9724/0 27 Apr 1864', ['34.3','34.4','33'], 'Banks return to New Orleans previous instructions Shreveport Steele Little Rock Halleck Chief of Staff gunboats out of Red River'),
 ('Z4 9771/0 3 Jul 1864', ['37.2','37.1'], 'Early Breckenridge Hunter Beverly Moorefield Romney Sigel Stahel Max Weber good defense Halleck'),
 ('Z5 9804/1 30 Jul 1864', ['37.2','40.2'], 'Averell McCausland Chambersburg crossing McCoys Ferry Williamsport Falling Waters Shepherdstown Greencastle Mercersburg Couch'),
 ('Z6 9727/0 30 Apr 1864', ['34.3','34.4','33'], 'Trans-Mississippi affairs Cairo Little Rock modifying telegram Canby Washburn Special Orders 150 Sixteenth Corps relieved Halleck Grant'),
 ('Z7 9765/2 25 Jun 1864', ['40.2','40.3','37.1'], 'ocean steamers New York Philadelphia sent to James River Hampton Roads City Point New Orleans Quartermaster blankets Meigs'),
 ('Z8 9780/0 8 Jul 1864', ['37.2'], 'Wallace reports enemy Urbana Early Breckinridge twenty thousand Hunter Parkersburg Halleck Dana pressure of business'),
 ('Z9 9876/0 24 Oct 1864', ['42.3','42.2','41.4'], 'appointments clearly in conflict with law most liberal construction act of Congress meritorious service confirmation Senate Meade'),
 ('Z10 9764/2 24 Jun 1864', ['37.1','40.2','40.3'], 'Stahel sent back by Hunter ammunition train escort perilous Shenandoah Valley Halleck Grant')]
n = 0
for lab, vols, q in Q:
    for v in vols:
        url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': V(v)})
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
            hits = d.get('hits', {}).get('hits', [])
            print(lab, '|', V(v), '|', len(hits))
            for h in hits[:3]:
                for s in (h.get('highlight', {}) or {}).get('text', [])[:2]: print('   ', s.replace('\n', ' ')[:300])
        except Exception as e: print(lab, '|', V(v), '| ERR', str(e)[:100])
        n += 1; time.sleep(1.8)
print('be-api requests', n)
