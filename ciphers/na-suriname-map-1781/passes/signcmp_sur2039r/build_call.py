# SUR-2039R (account 4, LANE DEFAULT-A4-0935, 13 Oct 2026): one blind sign call on the 10 unkeyed K/O/&/[J-rev] tokens of the
# 4.VEL 2039 Remarque (GAPS16 native re-pass) against all 54 Nieuw Secreet sheet tiles (SUR-2046's boxes, fresh relabelling
# seed 20391013), with 20 known-answer H controls from the same Remarque hand (2 each of 10 classes, seed 2039), query numbers
# shuffled (seed 1039). Usage (from the target folder): python3 passes/signcmp_sur2039r/build_call.py
import csv, json, random
D = 'passes/signcmp_sur2039r/'; S = 'passes/signcmp_sur2046/'
old = json.load(open(S + 'blind_key.json'))
R = {k: (f, tuple(b), v) for lab, (k, v, f, b) in old.items()}
rk = sorted(R); random.Random(20391013).shuffle(rk)
key = {f'R{i+1}': [k, R[k][2], R[k][0], list(R[k][1])] for i, k in enumerate(rk)}
from PIL import Image, ImageDraw
def tile(f, b, pad=6, H=100):
    im = Image.open(f).convert('L'); x0, y0, x1, y1 = b; im = im.crop((max(0, x0 - pad), max(0, y0 - pad), x1 + pad, y1 + pad))
    s = H / im.size[1]; return im.resize((max(20, int(im.size[0] * s)), H))
W = 1400; x = y = 0; H = 100; canvas = Image.new('L', (W, 1600), 255); d = ImageDraw.Draw(canvas)
for lab, (k, v, f, b) in key.items():
    im = tile(f, tuple(b)); w = max(im.size[0], 60)
    if x + w + 16 > W: x = 0; y += H + 36
    canvas.paste(im, (x, y + 22)); d.rectangle([x - 1, y + 21, x + im.size[0], y + 22 + H], outline=128)
    d.text((x + 2, y + 4), lab, fill=0); x += w + 16
canvas.crop((0, 0, W, y + H + 30)).save(D + 'blind_refs.jpg', quality=90)
json.dump(key, open(D + 'blind_key.json', 'w'), indent=1)
tok = {}
for r in csv.reader((l for l in open('reading_2039_remarque_nieuw_tokens.tsv') if not l.startswith('#')), delimiter='\t'):
    if r[0] != 'line' and r[0].startswith('2039_rem'): tok[(r[0], int(r[1]))] = (r[2], r[3], r[4])
TCLS = ['K', 'O', '&', '[J-rev]']
targ = {k: s for k, (s, v, g) in tok.items() if s in TCLS and g == 'U'}
assert len(targ) == 10, len(targ)
# look-alike-weighted control classes (PREREG): o, [hash] (round signs, vs O), r, l, [lambda], 8, [psi], [delta], 3, 7
CTRL = ['o', '[hash]', 'r', 'l', '[lambda]', '8', '[psi]', '[delta]', '3', '7']
crng = random.Random(2039); ctrl = {}
for c in CTRL:
    inst = sorted(k for k, (s, v, g) in tok.items() if s == c and g == 'H')
    for k in crng.sample(inst, 2): ctrl[k] = tok[k][1]
CROP = {'2039_rem_head': 'L01', '2039_rem_L1': 'L02', '2039_rem_L2': 'L03', '2039_rem_L3': 'L04', '2039_rem_L4': 'L05',
        '2039_rem_L5': 'L06'}
lines = {}
for r in csv.reader((l for l in open('ciphertext_2039_remarque.tsv') if not l.startswith('#')), delimiter='\t'):
    if r[0] == 'line' or r[0] not in CROP: continue
    lines.setdefault(r[0], []).append((int(r[1]), r[2]))
allq = sorted(set(targ) | set(ctrl), key=lambda k: (CROP[k[0]], k[1]))
order = list(range(len(allq))); random.Random(1039).shuffle(order)
num = {k: order[i] + 1 for i, k in enumerate(allq)}
q = []; seqs = {}
for L in sorted(lines, key=lambda L: CROP[L]):
    out = []
    for pos, s in lines[L]:
        if (L, pos) in num:
            n = num[(L, pos)]
            if (L, pos) in targ: role, kv = 'target', ''
            else: role, kv = 'control', ctrl[(L, pos)]
            q.append((f'#{n}', L, CROP[L], pos, s, role, kv)); out.append(f'#{n}')
        elif s.startswith('w:'): out.append('<plain:%s>' % s[2:])
        else: out.append(s)
    if any(o.startswith('#') for o in out): seqs[CROP[L]] = ' '.join(out)
q.sort(key=lambda r: int(r[0][1:]))
with open(D + 'queries_key.tsv', 'w') as f:
    f.write('query\tline\tcrop\tpos\treader_code\trole\tkey_value\n')
    for row in q: f.write('\t'.join(map(str, row)) + '\n')
with open(D + 'query_sequences.txt', 'w') as f:
    for L, s in seqs.items(): f.write(f'{L}: {s}\n')
print(len(q), 'queries (targets', len(targ), 'controls', len(ctrl), ') on', len(seqs), 'lines;', len(key), 'refs')
