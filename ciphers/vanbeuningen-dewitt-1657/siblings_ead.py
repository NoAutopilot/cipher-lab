#!/usr/bin/env python3
"""VB-EAD: grep the NA 3.01.17 EAD snapshot for cipher terms and Van Beuningen items 1655-1660.
Usage: siblings_ead.py [--check]  -> writes siblings_ead.tsv; --check exits 1 if committed file is stale."""
import re, sys, os, xml.etree.ElementTree as ET
D = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(D, '../../sources/na-3.01.17/2026-10-09/3.01.17.xml')
TERMS = ['cijfer','cyfer','cypher','cipher','gecijferd','sleutel','chiffre','geheimschrift','ontcijfer','beuningen']
def txt(e): return re.sub(r'\s+',' ',''.join(e.itertext())).strip() if e is not None else ''
rows=[]
def walk(e, path):
    for c in e:
        if not re.fullmatch(r'c(\d\d)?', c.tag): continue
        did=c.find('did'); t=txt(did.find('unittitle')) if did is not None else ''
        ud=did.find('.//unitdate') if did is not None else None
        norm=(ud.get('normal') if ud is not None else '') or ''
        uid=[u.text for u in did.findall('unitid') if u.get('type') is None] if did is not None else []
        dao=did.find('dao') if did is not None else None
        odd=txt(c.find('odd')); scope=txt(c.find('scopecontent'))
        full=' '.join([t,odd,scope,' '.join(path[-3:])]).lower()
        yrs=[int(y) for y in re.findall(r'\b(16\d\d)\b',norm+' '+t)]
        inrange=any(1655<=y<=1660 for y in yrs)
        hit=[w for w in TERMS if w in full]
        cipher=[w for w in hit if w!='beuningen']
        if (cipher and (inrange or not yrs)) or ('beuningen' in hit and inrange):
            rows.append((uid[0] if uid else '', norm or t[:30], (t or '(untitled; parent: '+path[-1][:60]+')')[:140], odd[:80], ','.join(hit),
                         'y' if dao is not None else 'n', ' > '.join(p[:50] for p in path[-2:])))
        walk(c, path+[t or (uid[0] if uid else '')])
root=ET.parse(SRC).getroot()
walk(root.find('.//dsc'), [])
out='inv\tdate\ttitle\todd\tmatched_terms\tdigitised\tparents\n'+'\n'.join('\t'.join(r) for r in rows)+'\n'
p=os.path.join(D,'siblings_ead.tsv')
if '--check' in sys.argv:
    sys.exit(0 if os.path.exists(p) and open(p).read()==out else 1)
open(p,'w').write(out); print(len(rows),'rows')
for r in rows: print('\t'.join(r)[:230])
