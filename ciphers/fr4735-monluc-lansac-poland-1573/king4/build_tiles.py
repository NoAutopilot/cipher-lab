#!/usr/bin/env python3
"""MONL-KING4 (20 Oct 2026): crop step + tiles for tools/lookalike_pass.py windows on c258 (f.133) L01-L25 (PREREG-MONL-KING4.md).
Strips: each line's two segments (s1 = region x 0-1700, s2 = region x 1400-..., the king2/king3 crop convention, 300 px overlap)
stitched on region x into king4/strips/c258_<line>.jpg (crops from regen_monlking2.sh / regen_monlking3.sh, untracked).
Tiles: every ciphertext_c258.tsv row whose pass_a != pass_b (passC = the committed sign). Confusion: unordered A/B label pairs over those
rows (both labels present), counts -> king4/confusion.tsv. Candidates: A, B (when present) and, for a single tile, the label's two most
frequent confusion partners. Writes king4/strips/, king4/c258_tiles.tsv, king4/c258_passC.tsv, king4/confusion.tsv, king4/desc.tsv,
king4/candidates.png (ids only). Run from the repo root."""
import csv, os, collections
from PIL import Image
D = 'ciphers/fr4735-monluc-lansac-poland-1573'; K = D + '/king4'
os.makedirs(K + '/strips', exist_ok=True)
for i in range(1, 26):
    ln = f'L{i:02d}'; src = D + ('/images/scratchking2/crops' if i <= 10 else '/images/scratchking3/crops')
    a = Image.open(f'{src}/c258_{ln}_s1.jpg').convert('L'); b = Image.open(f'{src}/c258_{ln}_s2.jpg').convert('L')
    S = Image.new('L', (1400 + b.size[0], max(a.size[1], b.size[1])), 255)
    S.paste(b, (1400, 0)); S.paste(a.crop((0, 0, 1400 + 150, a.size[1])), (0, 0))   # s1 wins up to mid-overlap
    S.save(f'{K}/strips/c258_{ln}.jpg', quality=92)
pc = list(csv.DictReader(open(D + '/ciphertext_c258.tsv'), delimiter='\t'))
with open(K + '/c258_passC.tsv', 'w') as o:
    o.write('passage\tpos\tsign_id\tconf\n')
    for r in pc: o.write(f"{r['line']}\t{r['pos']}\t{r['sign']}\t{r['conf']}\n")
real = lambda x: bool(x) and x != '-' and not x.startswith(('A:', 'B:'))
conf = collections.Counter()
for r in pc:
    if r['pass_a'] != r['pass_b'] and real(r['pass_a']) and real(r['pass_b']):
        conf[tuple(sorted((r['pass_a'], r['pass_b'])))] += 1
with open(K + '/confusion.tsv', 'w') as o:
    o.write('a\tb\tcount\n')
    for (x, y), n in conf.most_common(): o.write(f'{x}\t{y}\t{n}\n')
part = collections.defaultdict(collections.Counter)
for (x, y), n in conf.items(): part[x][y] += n; part[y][x] += n
seq = collections.defaultdict(list)
for r in pc: seq[r['line']].append(r['sign'])
tiles = []
for r in pc:
    A, B = r['pass_a'], r['pass_b']
    if A == B: continue
    ln, pos = r['line'], int(r['pos'])
    labs = [x for x in (A, B) if real(x)]
    st = 'split' if len(labs) == 2 else 'single'
    cand = list(dict.fromkeys(labs + ([p for p, _ in part[labs[0]].most_common(2)] if st == 'single' else [])))
    s = seq[ln]
    tiles.append(dict(run='c258', passage=ln, pos=pos, passC=r['sign'], A=A if real(A) else '', B=B if real(B) else '', status=st, why=st,
                      candidates=','.join(cand), before=' '.join(s[max(0, pos - 4):pos - 1]), after=' '.join(s[pos:pos + 3]), noteA='', noteB=''))
F = ['run', 'passage', 'pos', 'passC', 'A', 'B', 'status', 'why', 'candidates', 'before', 'after', 'noteA', 'noteB']
with open(K + '/c258_tiles.tsv', 'w') as o:
    w = csv.DictWriter(o, F, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(tiles)
ids = sorted({c for t in tiles for c in t['candidates'].split(',') if c.startswith('K')})
with open(K + '/desc.tsv', 'w') as o:
    o.write('?double_slash\tnot on the sheet: two short parallel oblique strokes, like //\n')
    o.write('?h_bar\tnot on the sheet: a letter-h shape with a horizontal bar crossing its stem\n')
    for c in sorted({c for t in tiles for c in t['candidates'].split(',')}):
        if c.startswith('K'): o.write(f'{c}\tthe cell labelled {c} in candidates.png\n')
        elif c.startswith('?x['): o.write(f'{c}\tnot on the sheet: {c[3:-1].replace("_", " ")}\n')
        elif c.startswith('W:'): o.write(f'{c}\ta word written in clear letters: {c[2:]}\n')
ks = Image.open(D + '/images/keysheet_monluc1_ids.png'); cw, ch = 136, 176; nc = 8
out = Image.new('RGB', (nc * cw, ((len(ids) + nc - 1) // nc) * ch), 'white')
for n, k in enumerate(ids):
    i = int(k[1:]) - 1
    out.paste(ks.crop(((i % 8) * cw, (i // 8) * ch, (i % 8 + 1) * cw, (i // 8 + 1) * ch)), ((n % nc) * cw, (n // nc) * ch))
out.save(K + '/candidates.png')
print(f'tiles {len(tiles)} (split {sum(t["status"]=="split" for t in tiles)}, single {sum(t["status"]=="single" for t in tiles)}); '
      f'candidate ids {len(ids)}; top pairs {conf.most_common(6)}')
