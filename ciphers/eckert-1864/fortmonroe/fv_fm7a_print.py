#!/usr/bin/env python3
"""FV-FM7a (9 Oct 2026): print check for E251 E252 E253 E256 E258 (Fort Monroe ledger). Greps the cached OR/Butler texts
(sources/ia-fulltext/print-check) plus volumes fetched once to SCRATCH (archive.org _djvu.txt, 2 s apart) for names and decoded
phrases; prints context. Usage: fv_fm7a_print.py SCRATCH_DIR. A miss is a search result, not a statement about print (rule 10)."""
import glob, gzip, os, re, sys, time, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
S = sys.argv[1]; n = 0
for ident in ('warofrebellion422unit', 'warofrebellion423unit', 'warofrebellion401unit', 'warofrebellion402unit'):
    p = os.path.join(S, ident + '_djvu.txt')
    if not os.path.exists(p):
        try:
            open(p, 'wb').write(urllib.request.urlopen(urllib.request.Request(
                f'https://archive.org/download/{ident}/{ident}_djvu.txt', headers=UA), timeout=180).read()); n += 1
        except Exception as e:
            print('FETCH', ident, 'ERROR', e); n += 1
        time.sleep(2)
files = glob.glob(os.path.join(os.path.dirname(__file__), '../../../sources/ia-fulltext/print-check/*.txt.gz')) + glob.glob(os.path.join(S, '*_djvu.txt'))
PH = [r'Bartonsville', r'Stephen Barton', r'Colonel Saunders', r'Major Carney', r'Fulton[^.]{0,80}(104th|One hundred and fourth)',
      r'(104th|One hundred and fourth) Pennsylvania[^.]{0,200}(Hilton Head|Fulton|Monroe|Alexandria)', r'T\. ?D\. Hart', r'Hart, (Lieut|lieutenant)',
      r'march thence to Washington', r'report by telegraph from', r'Morehead City[^.]{0,200}(fever|yellow)', r'Waterhouse', r'Pettes|Pettis|Pettus',
      r'Channing Clapp', r'Jamestown Island', r'pontoon bridge[^.]{0,80}taken up', r'Dealy']
for f in sorted(files):
    t = (gzip.open(f, 'rt', errors='ignore') if f.endswith('.gz') else open(f, errors='ignore')).read()
    t = ' '.join(t.split())
    for ph in PH:
        for m in list(re.finditer(ph, t, re.I))[:6]:
            print(os.path.basename(f)[:34], '|', ph[:30], '|', t[max(0, m.start()-260):m.end()+260])
print('requests archive.org', n)
