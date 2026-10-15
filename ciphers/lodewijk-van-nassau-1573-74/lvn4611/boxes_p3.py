"""LVN-L1 (15 Oct 2026): re-anchored line boxes for WVO 4611 p3, in transcription numbering, replacing shift_boxes.py for p3.

LVN-PIN found the committed 150-dpi boxes for p3 one line above the transcription. LVN-L1 re-anchored them on the ink: centres from
  python3 tools/iiif_lines.py --image p-3.png --out <scratch> --prefix p3 --region 0,150,2481,1500 --distance 45 --debug
(300-dpi render, sha1 add43302eb94...; centres 239 309 385 462 540 620 694 777 862, page y) plus physical line 10 ("quil vous doint",
too short for the detector) at 940 from the row ink profile (ink rows 904-958). The committed boxes 04611_p3_L01..L10 sit on physical
lines 1..10 (within 6 px of these midpoints); the transcription lacks physical line 1, so transcription p3_Lk = physical line k+1 for
k = 1..9, the new row p3_L00 = physical line 1 ("diy 78, 81, ..."), and p3_L11/L12 (subscription, date) keep their own boxes
04611_p3_L11/L12 -- shift_boxes.py moved those two as well, wrongly (no p3 token row read by LVN-PIN sits on L10-L12, so nothing it read
is affected).

Writes boxes_p3.tsv (line, phys, y0, y1 at 300 dpi, source) and, with --json OUT, a manifest-shaped JSON (150-dpi boxes, as crops.py
and blobs.py expect) in which 04611_p3_Lk carries the re-anchored box. --recheck TOK_TSV compares every token row's crop band under the
re-anchored boxes with the band it was cut from under shift_boxes.py and prints the vertical difference; a row whose band moves by more
than 20 px is checked: MOVED (re-grade M) when the re-anchored band's centre falls outside
the old band (a different physical line), else 'same line' ('band trimmed' when the old band was an over-tall box).
usage: python3 boxes_p3.py MANIFEST_JSON [--json OUT] [--recheck TOK_TSV]"""
import json, sys
C = [239, 309, 385, 462, 540, 620, 694, 777, 862, 940]          # physical lines 1..10, page y at 300 dpi
B = [C[0] - 37] + [(a + b) // 2 for a, b in zip(C, C[1:])] + [C[-1] + 50]
args = sys.argv[1:]; man = args[0]
def walk(o):
    if isinstance(o, dict):
        if 'crop' in o and 'box' in o: yield o
        for v in o.values(): yield from walk(v)
    elif isinstance(o, list):
        for v in o: yield from walk(v)
E = {e['crop']: e['box'] for e in walk(json.load(open(man)))}
rows = []                                                          # (line, phys, y0, y1, source) at 300 dpi
for k in range(0, 10):                                             # transcription p3_L00..L09 = physical 1..10
    rows.append(('p3_L%02d' % k, k + 1, B[k], B[k + 1], 'iiif_lines centre %d' % C[k]))
for k in (10, 11, 12, 13, 14, 15):
    c = '04611_p3_L%02d.jpg' % k
    if c in E: rows.append(('p3_L%02d' % k, '-', max(2 * E[c][1], B[-1]), 2 * E[c][3], 'committed box %s' % c))
with open(__file__.replace('.py', '.tsv'), 'w') as f:
    f.write('line\tphys\ty0\ty1\tsource\n')
    for r in rows: f.write('\t'.join(map(str, r)) + '\n')
x1 = E['04611_p3_L01.jpg'][2]
new = {'04611_%s.jpg' % r[0]: [0, r[2] // 2, x1, (r[3] + 1) // 2] for r in rows}
if '--json' in args:
    out = args[args.index('--json') + 1]
    J = [{'crop': c, 'box': b} for c, b in E.items() if not c.startswith('04611_p3_L')]
    J += [{'crop': c, 'box': b, 'reanchored': 'LVN-L1'} for c, b in new.items()]
    json.dump(J, open(out, 'w')); print(len(J), 'boxes written to', out)
if '--recheck' in args:
    tok = args[args.index('--recheck') + 1]; moved = 0
    for l in open(tok):
        if not l.strip(): continue
        ln, pos, cx, hw, dy = l.split('\t')
        k = int(ln[4:]); old = E.get('04611_p3_L%02d.jpg' % (k + 1))            # shift_boxes.py's band
        nb = new['04611_%s.jpg' % ln]
        d0, d1 = 2 * nb[1] - 2 * old[1], 2 * nb[3] - 2 * old[3]
        mid = nb[1] + nb[3]; m = not (2 * old[1] <= mid <= 2 * old[3]); moved += m   # new band centre outside the old band
        print('%s/%s\ttop %+d\tbottom %+d\t%s' % (ln, pos, d0, d1, 'MOVED' if m else
              ('same line, band trimmed' if max(abs(d0), abs(d1)) > 20 else 'same line')))
    print('moved:', moved)
