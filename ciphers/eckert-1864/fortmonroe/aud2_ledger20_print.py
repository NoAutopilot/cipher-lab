#!/usr/bin/env python3
"""AUD2-LEDGER-20 (9 Oct 2026): second audit of E293 (5822/0). Letters-only phrase grep and KWIC over djvu texts the first audit did not
search: JCCW 1865 vol. 2 'Fort Fisher Expedition' (reportofjointcom02unit), OR I/42 pt 1 (warofrebellion421unit), OR I/42 pt 3
(warofrebellion423unit, the 7-9 Dec span and the index), plus cached Butler V. Usage: aud2_ledger20_print.py DIR_WITH_<id>.txt.
Texts are fetched once to scratch from archive.org/download/<id>/<id>_djvu.txt. A miss is a search result, not a novelty verdict (rule 10)."""
import gzip, os, re, sys
D = sys.argv[1]
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check', 'privateofficialc05butl_djvu.txt.gz')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
T = {i: open(os.path.join(D, i + '.txt'), errors='ignore').read() for i in ('reportofjointcom02unit', 'warofrebellion421unit', 'warofrebellion423unit')}
T['privateofficialc05butl'] = gzip.open(B, 'rt', errors='ignore').read()
PH = ['Rice Dupont and Sedgwick', 'Rice, Dupont', 'headquarters boat', 'embarking the troops', 'all possible dispatch', 'remaining troops to Monroe',
      'river boats and transfer', 'seagoing steamers now', 'sea-going steamers now laying', 'Baltic to report to you', 'telegraphed to Annapolis',
      'Western Metropolis', 'John Rice', 'Admiral DuPont', 'Colonel Webster', 'Colonel Dodge']
for v, t in T.items():
    n = norm(t)
    print(v, '|', '; '.join(f'{p}={n.count(norm(p))}' for p in PH))
j = re.sub(r'\s+', ' ', T['reportofjointcom02unit'])
for k in ('We have here now the following boats', 'The Baltic is at Annapolis. Get her', 'On the 8th of December 1 received', 'We had to take a steamer'):
    i = j.find(k); print('\nJCCW KWIC:', k, '->', j[max(0, i - 120):i + 600] if i >= 0 else 'not found')
o = re.sub(r'\s+', ' ', T['warofrebellion423unit'])
for k in ('Dodge, George S. Correspondence', 'Webster, Ralph C. Correspondence'):
    i = o.rfind(k); print('\nOR I/42 pt 3 index:', o[i:i + 160] if i >= 0 else 'not found')
