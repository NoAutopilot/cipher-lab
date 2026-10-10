#!/usr/bin/env python3
"""FV-L15a (10 Oct 2026): fetch the loc.gov OCR full text of New-York Daily Tribune pages (sn83030213) named on argv as DATE:SEQ and print the
lines around E536's phrases. One request per page JSON plus one per text file, 2 s apart. Usage: fv_l15a_loc.py 1865-01-18:1 [...]"""
import json, re, sys, time, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
for arg in sys.argv[1:]:
    d, sp = arg.split(':')
    url = f'https://www.loc.gov/resource/sn83030213/{d}/ed-1/?sp={sp}&st=text&fo=json'
    try:
        j = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90)); time.sleep(2)
        txt = ''
        ft = (j.get('page') or [{}])
        s = json.dumps(j)
        m = re.search(r'https://[^"]+ocr\.txt', s)
        if m:
            txt = urllib.request.urlopen(urllib.request.Request(m.group(0), headers=UA), timeout=90).read().decode('utf-8', 'ignore'); time.sleep(2)
        else:
            m2 = re.search(r'"full_text":\s*"((?:[^"\\]|\\.)*)"', s); txt = json.loads('"' + m2.group(1) + '"') if m2 else ''
        T = ' '.join(txt.split())
        print('PAGE', d, sp, 'chars', len(T), 'src', m.group(0) if m else 'json full_text')
        for k in ['Pennypacker', 'stunning', 'Vanderbilt', 'impregnable', 'adjacent', 'well sustained', 'E. H. H', 'Hall']:
            for mm in list(re.finditer(k, T))[:3]:
                print('  ', k, '::', T[max(0, mm.start()-500):mm.start()+500])
    except Exception as e: print('PAGE', d, sp, 'ERR', str(e)[:120])
