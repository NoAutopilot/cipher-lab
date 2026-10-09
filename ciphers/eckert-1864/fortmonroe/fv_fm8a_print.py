#!/usr/bin/env python3
"""FV-FM8a (9 Oct 2026): print check for E254 E270 E272 E275 E277 (Fort Monroe ledger). Greps the cached OR/Butler texts
(sources/ia-fulltext/print-check) plus OR I/42 pt 3 fetched once to SCRATCH (archive.org _djvu.txt) for names and decoded
phrases; then IA be-api full-text (snippet only) on Grant Papers vols 11-13. Usage: fv_fm8a_print.py SCRATCH_DIR.
A miss is a search result, not a statement about print (rule 10)."""
import glob, gzip, json, os, re, sys, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
S = sys.argv[1]; n = 0; nb = 0
for ident in ('warofrebellion423unit',):
    p = os.path.join(S, ident + '_djvu.txt')
    if not os.path.exists(p):
        try:
            open(p, 'wb').write(urllib.request.urlopen(urllib.request.Request(
                f'https://archive.org/download/{ident}/{ident}_djvu.txt', headers=UA), timeout=180).read()); n += 1
        except Exception as e:
            print('FETCH', ident, 'ERROR', e); n += 1
        time.sleep(2)
files = glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../sources/ia-fulltext/print-check/*.txt.gz')) + glob.glob(os.path.join(S, '*_djvu.txt'))
PH = [r'Binney', r'Brice[^.]{0,120}(pay|Paymaster)', r'one month.s pay', r'make you whole',
      r'leave for Washington to-?night', r'Terry[^.]{0,120}Varina', r'Lieutenant-Colonel Smith[^.]{0,100}(attend|departmental)', r'departmental matters',
      r'Nineteenth (Army )?Corps[^.]{0,60}arrived', r'New Orleans troops', r'Shaffer[^.]{0,200}(Nineteenth|New Orleans|arrived)',
      r'(boots|boats) of any kind', r'transport (one thousand|1,000) cavalry', r'Captain (C\. ?)?James[^.]{0,80}quartermaster',
      r'style of gun', r'strength of each battery', r'Fred(\.|erick)? Martin', r'Howard, chief of artillery']
for f in sorted(files):
    t = (gzip.open(f, 'rt', errors='ignore') if f.endswith('.gz') else open(f, errors='ignore')).read()
    t = ' '.join(t.split())
    for ph in PH:
        for m in list(re.finditer(ph, t, re.I))[:5]:
            print(os.path.basename(f)[:34], '|', ph[:30], '|', t[max(0, m.start()-240):m.end()+240])
BQ = [('papersofulyssess0011gran', '"none of the Nineteenth"'), ('papersofulyssess0011gran', 'Shaffer "New Orleans"'),
      ('papersofulyssess0011gran', '"Nineteenth Corps" Shaffer'), ('papersofulyssess0012gran', 'Butler "leave for Washington"'),
      ('papersofulyssess0012gran', '"Fred Martin"'), ('papersofulyssess0013gran', 'Binney paymaster'), ('papersofulyssess0013gran', '"boats of any kind"')]
for ident, q in BQ:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        print('BEAPI', ident, q, '->', len(hits))
        for h in hits[:3]:
            hl = h.get('highlight', {}) if isinstance(h, dict) else {}
            for v in (hl.values() if isinstance(hl, dict) else []):
                for s in (v if isinstance(v, list) else [v])[:4]:
                    print('    ', ' '.join(str(s).split())[:400])
    except Exception as e:
        print('BEAPI', ident, q, 'ERROR', e)
    nb += 1; time.sleep(1.6)
print('requests archive.org', n, 'be-api', nb)
