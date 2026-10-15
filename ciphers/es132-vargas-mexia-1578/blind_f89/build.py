"""ES132-BLIND: build the 92 single-crop blind reads (PREREG-ES132-BLIND.md). Images go to the scratchpad S (argv[1]), never into git.
Regenerate the crops first with the commands in NOTES.md "## ES132-BLIND"."""
import sys, random, json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
T = Path(__file__).resolve().parent.parent
S = Path(sys.argv[1])
def lines(pg):
    L = {}
    for l in open(T/f'ciphertext_{pg}.tsv', encoding='utf-8'):
        if l.startswith('#') or '\t' not in l: continue
        a, b = l.rstrip('\n').split('\t', 1); L[a] = b.split()
    return L
CT = {}
def tokat(p):
    pg, ln, i = p.split(':'); CT.setdefault(pg, lines(pg)); return CT[pg][ln], int(i)
rows = [l.rstrip('\n').split('\t') for l in open(T/'dup_settled.tsv', encoding='utf-8') if not l.startswith('#')]
cands = [r for r in rows if r[5].startswith('keep:')]
assert len(cands) == 40
fr = sorted(r for r in rows if r[5] == 'flag-removed')
dec = random.Random(1578).sample(fr, 12)
reads = []
for k, r in enumerate(cands):
    reads.append(dict(kind='candA', cid=r[0], side='f89', pos=r[0], truth='', grp=k % 3))
    reads.append(dict(kind='candB', cid=r[0], side='dup', pos=r[3], truth='', grp=(k + 1) % 3))
for j, r in enumerate(dec):
    if j < 8: reads.append(dict(kind='decoy', cid=r[0], side='f89', pos=r[0], truth=r[6], grp=j % 3))
    else: reads.append(dict(kind='decoy', cid=r[0], side='dup', pos=r[3], truth=r[2], grp=j % 3))
random.Random(132).shuffle(reads)
batches = [[x for x in reads if x['grp'] == g] for g in range(3)]
BOX = {}
for dn in ('f89', 'dup'):
    for e in json.load(open(S/dn/'manifest.json'))['iiif_lines']: BOX[(dn, e['crop'])] = e['box']
def crop(dirn, pg, ln):
    a, b = (Image.open(S/dirn/f'{pg}_{ln}_s{k}.jpg').convert('L') for k in (1, 2))
    ba, bb = BOX[(dirn, f'{pg}_{ln}_s1.jpg')], BOX[(dirn, f'{pg}_{ln}_s2.jpg')]
    b = b.crop((ba[2] - bb[0], 0, b.width, b.height))
    out = Image.new('L', (a.width + b.width, max(a.height, b.height)), 255)
    out.paste(a, (0, 0)); out.paste(b, (a.width, 0)); return out
(S/'items').mkdir(exist_ok=True)
try: F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 36)
except Exception: F = ImageFont.load_default()
n = 0
for g, bl in enumerate(batches, 1):
    with open(S/f'batch{g}.txt', 'w') as fh:
        for it in bl:
            n += 1; it['id'] = f'R{n:02d}'; it['batch'] = g
            pg, ln, i = it['pos'].split(':')
            A = crop(it['side'], pg, ln); sc = min(1.0, 2600 / A.width)
            A = A.resize((int(A.width*sc), int(A.height*sc)))
            out = Image.new('L', (A.width, A.height + 55), 255)
            ImageDraw.Draw(out).text((10, 5), it['id'], fill=0, font=F); out.paste(A, (0, 55))
            out.save(S/'items'/f"{it['id']}.jpg", quality=88)
            toks, i = tokat(it['pos'])
            b = ' '.join(t.rstrip('?') for t in toks[max(0, i-3):i-1]); a = ' '.join(t.rstrip('?') for t in toks[i:i+2])
            it.update(idx=i, n=len(toks), before=b, after=a)
            fh.write(f"{it['id']}\timage={S}/items/{it['id']}.jpg\ttoken {i} of {len(toks)} in the line; neighbours as transcribed: before [{b}] after [{a}]\n")
with open(T/'blind_f89'/'items.tsv', 'w', encoding='utf-8') as fh:
    fh.write('# ES132-BLIND reads (built by blind_f89/build.py; kind, current token and the other copy were never shown to the reader)\n')
    fh.write('id\tbatch\tkind\tcid\tside\tpos\ttruth\tidx\tbefore\tafter\n')
    for it in sorted(reads, key=lambda x: x['id']):
        fh.write('\t'.join(str(it[k]) for k in ('id','batch','kind','cid','side','pos','truth','idx','before','after')) + '\n')
print([len(b) for b in batches], [sum(x['kind']=='decoy' for x in b) for b in batches])
