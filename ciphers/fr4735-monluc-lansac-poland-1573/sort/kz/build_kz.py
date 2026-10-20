"""MONL-C268C-KZ (20 Oct 2026): cut the 9 L26-L30 K12|K22 lead tiles and 8 on-page H/H references, shuffle, write the blind sheet.
Inputs: images/scratch268f/ro268f.png (regen_monll26.sh's region rotated -4.3 deg, untracked; re-derive with
`sh regen_monll26.sh` then PIL rotate(-4.3, BICUBIC, fillcolor=255)) and the committed images/c268cipher_L0{1,2,3}_s{1,2}.jpg.
Sign x-centres were placed on numbered/ticked overlays by the worker (position only). Output: sort/kz/tiles/T??.png, sort/kz/sheet.png,
sort/kz/map.tsv (id -> token, role; NOT shown to the readers)."""
import os, random, sys
SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20261020  # round 1: 20261020; round 2 (KZ2): 20261021
SUF = '' if SEED == 20261020 else '2'
from PIL import Image, ImageDraw
H = os.path.dirname(os.path.abspath(__file__)); F = os.path.dirname(os.path.dirname(H))
ro = Image.open(f'{F}/images/scratch268f/ro268f.png').convert('L')
cents = dict(zip(range(26, 31), (202, 308, 422, 536, 649)))
leads = [(26, 17, 1520), (27, 15, 1365), (27, 33, 2775), (28, 6, 715), (28, 11, 1090), (28, 34, 2805), (29, 3, 480), (29, 23, 2045), (29, 29, 2585)]
refs = [(1, 26, 1900, 'K22'), (2, 11, 845, 'K22'), (2, 17, 1290, 'K22'), (3, 8, 630, 'K22'),
        (1, 29, 2160, 'K12'), (2, 21, 1580, 'K12'), (2, 28, 2005, 'K12'), (3, 6, 530, 'K12')]  # re-placed on a +-300 px ruler strip
if SUF == '2':  # KZ2: three reference ticks re-placed (reader B saw them between signs in round 1)
    fix = {(3, 8): 665, (2, 28): 2075, (1, 29): 2130, (1, 26): 1928}
    refs = [(l, p, fix.get((l, p), x), k) for l, p, x, k in refs]
    lfix = {(28, 11): 1115, (27, 15): 1335}
    leads = [(L, p, lfix.get((L, p), x)) for L, p, x in leads]
def refline(l):
    a = Image.open(f'{F}/images/c268cipher_L0{l}_s1.jpg').convert('L'); b = Image.open(f'{F}/images/c268cipher_L0{l}_s2.jpg').convert('L')
    ln = Image.new('L', (2800, 105), 255); ln.paste(a, (0, 0)); ln.paste(b.crop((100, 0, 1450, 105)), (1450, 0)); return ln
tiles = []
for L, p, x in leads:
    c = cents[L]; tiles.append((f'L{L}:{p}', 'lead', 'K12|K22', ro.crop((x - 130, c - 45, x + 130, c + 60))))
for l, p, x, k in refs:
    tiles.append((f'L0{l}:{p}', 'ref', k, refline(l).crop((x - 130, 0, x + 130, 105))))
random.Random(SEED).shuffle(tiles)
os.makedirs(f'{H}/tiles' + SUF, exist_ok=True)
sheet = Image.new('L', (3 * 540, 6 * 250), 255); d = ImageDraw.Draw(sheet)
with open(f'{H}/map' + SUF + '.tsv', 'w') as m:
    m.write('id\ttoken\trole\tid_known\n')
    for i, (tok, role, k, t) in enumerate(tiles):
        t = t.resize((520, 210), Image.LANCZOS); td = ImageDraw.Draw(t); td.polygon([(252, 0), (268, 0), (260, 16)], fill=0)
        tid = f'T{i:02d}'; t.save(f'{H}/tiles' + SUF + f'/{tid}.png'); m.write(f'{tid}\t{tok}\t{role}\t{k}\n')
        sheet.paste(t, ((i % 3) * 540, (i // 3) * 250 + 30)); d.text(((i % 3) * 540 + 5, (i // 3) * 250 + 8), tid, fill=0)
sheet.save(f'{H}/sheet' + SUF + '.png')
