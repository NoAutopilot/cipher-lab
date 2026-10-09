#!/usr/bin/env python3
"""FV-FM4 (9 Oct 2026), second block: dmGetItemInfo (full transcription) for the CONTENTdm hits that came back without a
transcription snippet -- possible clear received copies of E193 (sick prisoners / destination unknown) or E194 (corresponding order).
>= 3.2 s apart. Usage: fv_fm4_hdl2.py SCRATCH_DIR."""
import json, os, re, sys, time, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
P = ['9117', '2215', '2901', '5614', '3809', '4551', '3093', '3705', '2219', '4746', '13983']
KW = r'sick prisoners|destination unknown|corresponding order|langdon|webster|5700|exchanged'
out = sys.argv[1]; n = 0
for p in P:
    d = json.load(urllib.request.urlopen(urllib.request.Request(HB + f"dmGetItemInfo/p16003coll11/{p}/json", headers=UA), timeout=60)); n += 1
    json.dump(d, open(os.path.join(out, f'info_{p}.json'), 'w'))
    t = d.get('transc') if isinstance(d.get('transc'), str) else ''
    t = re.sub(r'\s+', ' ', t)
    print('##', p, d.get('title'), '| len', len(t))
    for m in re.finditer(KW, t, re.I):
        print('   ', t[max(0, m.start()-350):m.end()+250])
    time.sleep(3.2)
print('requests', n)
