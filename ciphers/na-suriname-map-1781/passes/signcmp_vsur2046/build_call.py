# V-SUR2046 (verifier, account 2, 13 Oct 2026): independent blind re-call of SUR-2046's 16 M relabels on 4.VEL 2046 with a
# FRESH known-answer control set (20 H tokens not used by SUR-2046, seed 20461013), fresh reference relabelling (seed 20261013)
# and fresh query numbering (seed 1013). Same 54 sheet tiles as SUR-2046 (passes/signcmp_sur2046/blind_key.json boxes).
# Usage (from the target folder): python3 passes/signcmp_vsur2046/build_call.py
import csv, json, random
D = 'passes/signcmp_vsur2046/'; S = 'passes/signcmp_sur2046/'
old = json.load(open(S + 'blind_key.json'))
R = {k: (f, tuple(b), v) for lab, (k, v, f, b) in old.items()}
rk = sorted(R); random.Random(20261013).shuffle(rk)
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
for r in csv.reader((l for l in open('reading_2046_legend_nieuw_tokens.tsv') if not l.startswith('#')), delimiter='\t'):
    if r[0] != 'line': tok[(r[0], int(r[1]))] = (r[2], r[3], r[4])
prev = {(r['line'], int(r['pos'])): r for r in csv.DictReader(open(S + 'decisions.tsv'), delimiter='\t')}
used = {k for k, r in prev.items() if r['role'] == 'control'}
targ = {k: r for k, r in prev.items() if r['applied'] == 'yes'}
assert len(targ) == 16, len(targ)
# look-alike-weighted classes (prereg): o, 6, [delta], 5, 3, h (SUR-2046 classes nearest the winning tiles) + p, a (sheet A-row p
# and E-row a, the tiles [p-grave] and [a-grave] went to) + [hash], 7
CTRL = ['o', '6', '[delta]', '5', '3', 'h', 'p', 'a', '[hash]', '7']
crng = random.Random(20461013); ctrl = {}
for c in CTRL:
    inst = sorted(k for k, (s, v, g) in tok.items() if s == c and g == 'H' and k not in used and k not in targ)
    for k in crng.sample(inst, 2): ctrl[k] = tok[k][1]
CROP = {'2046_title1': 'L01', '2046_title2': 'L02', '2046_head1': 'L03', '2046_No1': 'L04', '2046_No2': 'L05',
        '2046_No3': 'L06', '2046_head2': 'L07', '2046_leg_abc': 'L08', '2046_leg_d': 'L09', '2046_leg_efgh': 'L10',
        '2046_leg_ki': 'L11'}
lines = {}
for r in csv.reader((l for l in open('ciphertext_2046_legend.tsv') if not l.startswith('#')), delimiter='\t'):
    if r[0] == 'line': continue
    lines.setdefault(r[0], []).append((int(r[1]), r[2]))
allq = sorted(set(targ) | set(ctrl), key=lambda k: (CROP[k[0]], k[1]))
order = list(range(len(allq))); random.Random(1013).shuffle(order)
num = {k: order[i] + 1 for i, k in enumerate(allq)}
q = []; seqs = {}
for L in sorted(lines, key=lambda L: CROP[L]):
    out = []
    for pos, s in lines[L]:
        if (L, pos) in num:
            n = num[(L, pos)]
            if (L, pos) in targ: role, kv = 'target', targ[(L, pos)]['best_value']
            else: role, kv = 'control', ctrl[(L, pos)]
            q.append((f'#{n}', L, CROP[L], pos, s, role, kv)); out.append(f'#{n}')
        elif s.startswith('w:'): out.append('<plain:%s>' % s[2:])
        else: out.append(s)
    if any(o.startswith('#') for o in out): seqs[CROP[L]] = ' '.join(out)
q.sort(key=lambda r: int(r[0][1:]))
with open(D + 'queries_key.tsv', 'w') as f:
    f.write('query\tline\tcrop\tpos\treader_code\trole\tvalue_to_test\n')
    for row in q: f.write('\t'.join(map(str, row)) + '\n')
with open(D + 'query_sequences.txt', 'w') as f:
    for L, s in seqs.items(): f.write(f'{L}: {s}\n')
print(len(q), 'queries (targets', len(targ), 'controls', len(ctrl), ') on', len(seqs), 'lines;', len(key), 'refs')
