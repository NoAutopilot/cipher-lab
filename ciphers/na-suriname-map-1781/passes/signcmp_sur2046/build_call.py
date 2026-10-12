# SUR-2046 (account 4, 12 Oct 2026): value-blind reference sheet of EVERY sign on the Nieuw Secreet Alphabet sheet
# (NA 1.05.03 inv. 86 scan 0003 left, images/inv86_0003_left_native.jpg; plain-letter column and word column cut away)
# plus the masked query list for one blind sign call on 4.VEL 2046: targets = the 31 U tokens (reader codes the key lacks),
# controls = 20 H tokens of 10 already-keyed reader codes whose sheet sign is on the reference sheet (known answer, mixed in
# blind). Tiles 1-26/28 reuse GAPS15/GAPS25 boxes; the rest are cut here from the 1/2-scale view of the sheet.
# Usage: python3 passes/signcmp_sur2046/build_call.py [--check]   (--check also writes a NON-blind labelled montage to
# the scratch path given in $CHECK_OUT, for the worker's own tile check; it is never shown to the reader)
import csv, json, os, random, sys
from PIL import Image, ImageDraw
D = 'passes/signcmp_sur2046/'
K = 'images/inv86_0003_left_native.jpg'
t0 = json.load(open('passes/signcmp_gaps15/ref_tiles.json'))
OLD = {'R_Dv': 'd', 'R_DW': 'd', 'R_Cs': 'c', 'R_Nij': 'n', 'R_Nl': 'n', 'R_Nh': 'n', 'R_My': 'm', 'R_Pq': 'p', 'R_Lg': 'l',
       'R_Lc': 'l', 'R_Bd': 'b', 'R_B6': 'b', 'R_Sps': 's', 'R_Tr': 't', 'R_Yt': 'y', 'R_Im': 'i', 'R_I8': 'i', 'R_G9': 'g',
       'R_Kb': 'k', 'R_Ok': 'o', 'R_S6': 's', 'R_Iff': 'i', 'R_AA': 'stukgeschut', 'R_Gamma': 'fort-amsterdam',
       'R_buskr': 'buskruit', 'R_barrect': 'affuiten', 'R_tower': 'paarden', 'R_trefoil': 'snaphanen'}
R = {k: (t0[k][0], tuple(t0[k][1]), v) for k, v in OLD.items()}
NEW = {  # name: (box on native sheet, value)
    'R_Adelta': ((215, 475, 295, 535), 'a'), 'R_Ap': ((295, 470, 380, 560), 'a'), 'R_Ax': ((410, 465, 475, 530), 'a'),
    'R_E3': ((178, 945, 220, 1012), 'e'), 'R_E7': ((248, 945, 292, 1012), 'e'), 'R_Ea': ((316, 955, 360, 1012), 'e'),
    'R_Edelta': ((352, 918, 444, 1012), 'e'), 'R_Ee': ((450, 972, 510, 1046), 'e'),
    'R_Famp': ((150, 1050, 262, 1150), 'f'), 'R_Fomega': ((292, 1040, 428, 1138), 'f'),
    'R_Hsh': ((112, 1232, 226, 1402), 'h'), 'R_Hdollar': ((222, 1290, 288, 1388), 'h'),
    'R_Ohash': ((212, 2100, 298, 2188), 'o'), 'R_Opi': ((302, 2100, 418, 2188), 'o'),
    'R_PS': ((104, 2160, 196, 2280), 'p'), 'R_Qx': ((128, 2378, 212, 2462), 'q'), 'R_Ro': ((122, 2500, 188, 2578), 'r'),
    'R_Tlambda': ((212, 2736, 298, 2818), 't'), 'R_U5': ((132, 2850, 208, 2938), 'v'), 'R_Ue': ((212, 2850, 308, 2938), 'v'),
    'R_W4': ((112, 2980, 178, 3068), 'w'), 'R_X1': ((112, 3080, 168, 3158), 'x'), 'R_Zn': ((112, 3296, 198, 3378), 'z'),
    'R_Pi': ((702, 842, 818, 958), 'fort-zelandia'), 'R_B': ((672, 1012, 788, 1118), 'fort-sommelsdijck'),
    'R_bull': ((672, 1312, 798, 1418), 'kogels'),
}
for k, (b, v) in NEW.items(): R[k] = (K, b, v)
rng = random.Random(20261012)
rk = sorted(R); rng.shuffle(rk)
key = {f'R{i+1}': [k, R[k][2], R[k][0], list(R[k][1])] for i, k in enumerate(rk)}
def tile(f, b, pad=6, H=100):
    im = Image.open(f).convert('L'); x0, y0, x1, y1 = b; im = im.crop((max(0, x0 - pad), max(0, y0 - pad), x1 + pad, y1 + pad))
    s = H / im.size[1]; return im.resize((max(20, int(im.size[0] * s)), H))
def montage(labels, out):
    W = 1400; x = y = 0; H = 100
    canvas = Image.new('L', (W, 1600), 255); d = ImageDraw.Draw(canvas)
    for lab, (k, v, f, b) in key.items():
        im = tile(f, tuple(b)); w = max(im.size[0], 60)
        if x + w + 16 > W: x = 0; y += H + 36
        canvas.paste(im, (x, y + 22)); d.rectangle([x - 1, y + 21, x + im.size[0], y + 22 + H], outline=128)
        d.text((x + 2, y + 4), labels(lab, k, v), fill=0); x += w + 16
    canvas.crop((0, 0, W, y + H + 30)).save(out, quality=90)
json.dump(key, open(D + 'blind_key.json', 'w'), indent=1)
montage(lambda lab, k, v: lab, D + 'blind_refs.jpg')
if '--check' in sys.argv: montage(lambda lab, k, v: f'{lab} {k}', os.environ['CHECK_OUT'])
# queries
codes = {}
for r in csv.reader((l for l in open('key_period_codes_nieuw.tsv') if not l.startswith('#')), delimiter='\t'):
    if r[0] != 'code': codes[r[0]] = r[1]
tok = {}
for r in csv.reader((l for l in open('reading_2046_legend_nieuw_tokens.tsv') if not l.startswith('#')), delimiter='\t'):
    if r[0] != 'line': tok[(r[0], int(r[1]))] = (r[2], r[3], r[4])
CTRL = ['3', '7', '[lambda]', '[psi]', '5', '[hash]', '6', '[delta]', 'h', 'o']
crng = random.Random(2046)
ctrl = set()
for c in CTRL:
    inst = sorted(k for k, (s, v, g) in tok.items() if s == c and g == 'H')
    ctrl.update(crng.sample(inst, 2))
targ = {k for k, (s, v, g) in tok.items() if g == 'U'}
CROP = {'2046_title1': 'L01', '2046_title2': 'L02', '2046_head1': 'L03', '2046_No1': 'L04', '2046_No2': 'L05',
        '2046_No3': 'L06', '2046_head2': 'L07', '2046_leg_abc': 'L08', '2046_leg_d': 'L09', '2046_leg_efgh': 'L10',
        '2046_leg_ki': 'L11'}
lines = {}
for r in csv.reader((l for l in open('ciphertext_2046_legend.tsv') if not l.startswith('#')), delimiter='\t'):
    if r[0] == 'line': continue
    lines.setdefault(r[0], []).append((int(r[1]), r[2]))
allq = sorted(targ | ctrl, key=lambda k: (CROP[k[0]], k[1]))
order = list(range(len(allq))); random.Random(46).shuffle(order)  # query numbers do not reveal target vs control
num = {k: order[i] + 1 for i, k in enumerate(allq)}
q = []; seqs = {}
for L in sorted(lines, key=lambda L: CROP[L]):
    out = []
    for pos, s in lines[L]:
        if (L, pos) in num:
            n = num[(L, pos)]; role = 'target' if (L, pos) in targ else 'control'
            q.append((f'#{n}', L, CROP[L], pos, s, role, tok[(L, pos)][1])); out.append(f'#{n}')
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
