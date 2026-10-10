#!/usr/bin/env python3
"""FV-L15b (10 Oct 2026, account 1, for LANE LEDGER-15; copy of fv_fm65b_print.py): letters-only phrase grep of decoded phrases of
E545 E560 E505 E567 E525 E572 over the cached print-check volumes (sources/ia-fulltext/print-check/*.gz) plus scratch djvu texts given
as arguments, then KWIC for rare names in OR I/46 pt 2, I/47 pt 2 (cache) and the scratch texts. A miss is a search result, not a
verdict (rule 10). Usage: fv_l15b_print.py [scratch.txt ...]"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E545': ['send one battery with each division', 'one battery with each division', 'let the others follow when convenient',
          'necessary to bring transportation from Washington', 'to follow the troops', 'if good mules cannot be obtained',
          'ask authority to bring those from Kentucky', 'bring those from Kentucky'],
 'E560': ['telegraph station be established at Yorktown', 'station be established at Yorktown', 'provide a battery and operator',
          'establish the office as speedily as practicable', 'Acting Chief Quartermaster'],
 'E505': ['Steamers all ready coaled and loaded with proper rations', 'wishes one of the going steamers', 'one of the going steamers',
          'for other service', 'with good supply of coal', 'no rations will be required', 'no rations required', 'send to this place one of'],
 'E567': ['two engines and some flat cars', 'some flat cars sent here at once', 'so that Colonel Wright can commence work',
          'Wright can commence work', 'none have arrived at this place or New Berne', 'none have arrived at this place'],
 'E525': ['the Baltic got off for Monroe', 'before I could countermand the order', 'she had better coal there and return to Annapolis',
          'where she can take troops', 'it is impossible for her to come up here', 'let me know what orders you give her'],
 'E572': ['steamship Champion arrived here from Wilmington', 'Champion arrived here', 'had reached Fayetteville North Carolina intact',
          'reached Fayetteville intact', 'reached Wilmington on the 11th', 'the Champion sailing the same day', 'no particulars could be obtained'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = norm(gzip.open(p, 'rt', errors='ignore').read())
raw = {}
for k in ['warofrebellion014602rootrich', 'warofrebellion431unit', 'warofrebellion452unit']:
    raw[k] = gzip.open(os.path.join(D, k + '_djvu.txt.gz'), 'rt', errors='ignore').read()
for p in sys.argv[1:]:
    k = os.path.basename(p)[:-4]; raw[k] = open(p, errors='ignore').read(); texts[k] = norm(raw[k])
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in texts.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
KW = [('E545', r'G\. W\. Schofield|Lieut(enant)?\.? ?-?Col(onel)?\.? (G\. W\. )?Schofield|Boyd', r'mules|Kentucky|batter|Willard|Washington|transportation'),
      ('E545', r'mules', r'Kentucky'), ('E560', r'Yorktown', r'telegraph|operator|station'), ('E560', r'D\. James|Wm\. D\. James|William D\. James', r''),
      ('E505', r'other service', r'steamer|Rawlins|coal'), ('E567', r'flat[- ]cars|flats', r'engine|Wright|Schofield|Wilmington|Newbern|New Berne|New Bern'),
      ('E567', r'Colonel Wright|Col\. Wright|W\. W\. Wright', r'engine|cars|rolling|work'), ('E525', r'Baltic', r'Annapolis|Newport|Monroe|coal'),
      ('E572', r'Champion', r'Wilmington|Fayetteville|steam'), ('E572', r'Fayetteville', r'scout|Wilmington|11th|eleventh')]
for e, pat, ctx in KW:
    for k, t in raw.items():
        for m in re.finditer(pat, t):
            s = ' '.join(t[max(0, m.start()-260):m.end()+260].split())
            if ctx and not re.search(ctx, s): continue
            print('KWIC', e, pat[:20], '|', k, '|', s)
