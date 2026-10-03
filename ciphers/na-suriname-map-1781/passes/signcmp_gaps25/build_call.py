# GAPS25-na-suriname-map-1781 (account-4), 3 Oct 2026: build the value-blind reference sheet and the masked query list
# for the one blind d/n/q (+ c/m/a) sign call. Refs: Nieuw Secreet sheet tiles (inv. 86 scan 0003 left page) from
# passes/signcmp_gaps15/ref_tiles.json plus three tiles cut here (A-row delta, A-row p, Q-row cross), shuffled labels.
# Queries: every 2077 token whose reader code the key reads d, n, q, a or c (no 2077 code reads m), masked as #k in the
# line's reader-code sequence; the line crops are the GAPS19 tools/iiif_lines.py crops images/crops_2077_leg/.
import csv, json, random
from PIL import Image, ImageDraw
D = 'passes/signcmp_gaps25/'
K = 'images/inv86_0003_left_native.jpg'
t0 = json.load(open('passes/signcmp_gaps15/ref_tiles.json'))
use = ['R_Dv', 'R_DW', 'R_Cs', 'R_Nij', 'R_Nl', 'R_Nh', 'R_My', 'R_Pq', 'R_Lg', 'R_Lc', 'R_Bd', 'R_B6', 'R_Sps',
       'R_Tr', 'R_Yt', 'R_Im', 'R_I8', 'R_G9', 'R_Kb', 'R_Ok', 'R_S6', 'R_Iff']
R = {k: (t0[k][0], tuple(t0[k][1])) for k in use}
R['R_Ax'] = (K, (410, 465, 475, 530)); R['R_Adelta'] = (K, (215, 475, 295, 535)); R['R_Ap'] = (K, (295, 470, 380, 560))
R['R_Qx'] = (K, (80, 2380, 185, 2475))
VAL = {'R_Dv': 'd', 'R_DW': 'd', 'R_Cs': 'c', 'R_Nij': 'n', 'R_Nl': 'n', 'R_Nh': 'n', 'R_My': 'm', 'R_Pq': 'p', 'R_Lg': 'l',
       'R_Lc': 'l', 'R_Bd': 'b', 'R_B6': 'b', 'R_Sps': 's', 'R_Tr': 't', 'R_Yt': 'y', 'R_Im': 'i', 'R_I8': 'i', 'R_G9': 'g',
       'R_Kb': 'k', 'R_Ok': 'o', 'R_S6': 's', 'R_Iff': 'i', 'R_Ax': 'a', 'R_Adelta': 'a', 'R_Ap': 'a', 'R_Qx': 'q'}
rng = random.Random(20261003)
rk = sorted(R); rng.shuffle(rk)
key = {f'R{i+1}': [k, VAL[k], R[k][0], list(R[k][1])] for i, k in enumerate(rk)}
json.dump(key, open(D + 'blind_key.json', 'w'), indent=1)
def tile(f, b, pad=6, H=110):
    im = Image.open(f).convert('L'); x0, y0, x1, y1 = b; im = im.crop((max(0, x0 - pad), max(0, y0 - pad), x1 + pad, y1 + pad))
    s = H / im.size[1]; return im.resize((max(20, int(im.size[0] * s)), H))
W = 1400; x = y = 0; H = 110
canvas = Image.new('L', (W, 1200), 255); d = ImageDraw.Draw(canvas)
for lab, (k, v, f, b) in key.items():
    im = tile(f, tuple(b)); w = max(im.size[0], 60)
    if x + w + 16 > W: x = 0; y += H + 36
    canvas.paste(im, (x, y + 22)); d.rectangle([x - 1, y + 21, x + im.size[0], y + 22 + H], outline=128); d.text((x + 2, y + 4), lab, fill=0); x += w + 16
canvas.crop((0, 0, W, y + H + 30)).save(D + 'blind_refs.jpg', quality=90)
# queries
codes = {}
for r in csv.reader((l for l in open('key_period_codes_nieuw.tsv') if not l.startswith('#')), delimiter='\t'):
    if r[0] != 'code': codes[r[0]] = r[1]
TV = {'d', 'n', 'q', 'a', 'c', 'm'}
lines = {}
for r in csv.reader((l for l in open('ciphertext_2077_legend.tsv') if not l.startswith('#')), delimiter='\t'):
    if r[0] == 'line': continue
    lines.setdefault(r[0], []).append((int(r[1]), r[2]))
q = []; seqs = {}; n = 0
for L in sorted(lines):
    out = []
    for pos, s in lines[L]:
        if codes.get(s) in TV:
            n += 1; q.append((f'#{n}', L, pos, s, codes[s])); out.append(f'#{n}')
        elif s.startswith('w:'): out.append('<plain:%s>' % s[2:])
        else: out.append(s)
    if any(o.startswith('#') for o in out): seqs[L] = ' '.join(out)
with open(D + 'queries_key.tsv', 'w') as f:
    f.write('query\tline\tpos\treader_code\tkey_value\n')
    for row in q: f.write('\t'.join(map(str, row)) + '\n')
with open(D + 'query_sequences.txt', 'w') as f:
    for L, s in seqs.items(): f.write(f'{L.replace("2077_", "")}: {s}\n')
print(len(q), 'queries on', len(seqs), 'lines;', len(key), 'refs')
