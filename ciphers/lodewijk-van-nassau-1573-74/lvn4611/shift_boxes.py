"""LVN-PIN (15 Oct 2026): on WVO 4611 p3 the committed 150-dpi line boxes run one line above the transcription's numbering: box
04611_p3_L01 is the page's first written line ("diy 78, 81, 28, 200, ...", absent from every 4611 transcription), and transcription line
p3_Lk is the ink of box p3_L(k+1) (checked by eye on the 300-dpi strips, LVN-PIN placement note in PREREG-LVN-4611.md).
Writes a manifest-shaped JSON in which 04611_p3_Lk carries box p3_L(k+1), for blobs.py / crops.py. Output goes to scratch.
usage: python3 shift_boxes.py MANIFEST_JSON OUT_JSON"""
import json, sys
man, out = sys.argv[1:3]
def walk(o):
    if isinstance(o, dict):
        if 'crop' in o and 'box' in o: yield o
        for v in o.values(): yield from walk(v)
    elif isinstance(o, list):
        for v in o: yield from walk(v)
E = {e['crop']: e['box'] for e in walk(json.load(open(man)))}
rows = []
for c, b in E.items():
    if c.startswith('04611_p3_L'):
        k = int(c[len('04611_p3_L'):-4]); nxt = '04611_p3_L%02d.jpg' % (k + 1)
        if nxt in E: rows.append({'crop': c, 'box': E[nxt], 'shifted_from': nxt})
    else:
        rows.append({'crop': c, 'box': b})
json.dump(rows, open(out, 'w'))
print(len(rows), 'boxes;', sum('shifted_from' in r for r in rows), 'p3 boxes shifted by one line')
