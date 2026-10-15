"""ES132-WIN: native-resolution token windows on the f.89 side (PREREG-ES132-WIN.md). Images go to the scratchpad S (argv[1]), never into git.
Regenerate the line crops first: tools/iiif_lines.py --image images/src_* (four commands in NOTES.md "## ES132-WIN") into S/f89.
Usage: build.py S decoys  -> S/decoys_sheet1-2.jpg (eye check); build.py S batches -> win_f89/items.tsv, S/items/*.jpg, S/batch1-3.txt
"""
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
cands_all = [r for r in rows if r[5].startswith('keep:')]
assert len(cands_all) == 40
words = [r for r in cands_all if r[1].startswith('{') or r[2].startswith('{')]
cands = sorted(random.Random(89).sample([r for r in cands_all if r not in words], 24))
fr = [r for r in rows if r[5] == 'flag-removed']
decoy_order = random.Random(2026).sample(fr, len(fr))   # first 12 the eye check accepts are used (PREREG)
BOX = {e['crop']: e['box'] for e in json.load(open(S/'f89'/'manifest.json'))['iiif_lines']}
def line(pg, ln):
    a, b = (Image.open(S/'f89'/f'{pg}_{ln}_s{k}.jpg').convert('L') for k in (1, 2))
    ba, bb = BOX[f'{pg}_{ln}_s1.jpg'], BOX[f'{pg}_{ln}_s2.jpg']
    b = b.crop((ba[2] - bb[0], 0, b.width, b.height))
    out = Image.new('L', (a.width + b.width, max(a.height, b.height)), 255)
    out.paste(a, (0, 0)); out.paste(b, (a.width, 0)); return out
def window(pos):
    """Native-resolution window: estimated token centre (proportional along the inked span) +- 3 token widths."""
    pg, ln, i = pos.split(':'); toks, i = tokat(pos)
    L = line(pg, ln); w = L.width
    cols = [x for x in range(w) if min(L.crop((x, int(L.height*.25), x+1, int(L.height*.75))).getdata()) < 120]
    x0, x1 = (cols[0], cols[-1]) if cols else (0, w)
    tw = (x1 - x0) / len(toks); c = x0 + (i - 0.5) * tw
    lo, hi = max(0, int(c - 3.2*tw)), min(w, int(c + 3.2*tw))
    return L.crop((lo, 0, hi, L.height)), toks, i
try: F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 30)
except Exception: F = ImageFont.load_default()
def labelled(img, lab):
    out = Image.new('L', (img.width, img.height + 45), 255)
    ImageDraw.Draw(out).text((8, 4), lab, fill=0, font=F); out.paste(img, (0, 45)); return out
if __name__ == '__main__' and sys.argv[2] == 'decoys':
    # eye-check sheet: the first 16 decoys in order, labelled D01.. with position (the worker settles truth by eye before any read)
    ims = []
    for k, r in enumerate(decoy_order[:16], 1):
        W, toks, i = window(r[0])
        ims.append(labelled(W, f'D{k:02d} {r[0]} tok {i}/{len(toks)} nb {" ".join(t.rstrip("?") for t in toks[max(0,i-3):i-1])} [?] {" ".join(t.rstrip("?") for t in toks[i:i+2])}'))
    for half in (0, 1):
        part = ims[half*8:(half+1)*8]
        sheet = Image.new('L', (max(x.width for x in part), sum(x.height for x in part)), 255); y = 0
        for x in part: sheet.paste(x, (0, y)); y += x.height
        sheet.save(S/f'decoys_sheet{half+1}.jpg', quality=90)
    print('\n'.join(f'D{k:02d}\t{r[0]}\t{r[6]}' for k, r in enumerate(decoy_order[:16], 1)))
DECOYS = ['D01','D02','D04','D05','D06','D07','D08','D09','D11','D14','D15','D16']   # accepted by the eye check (PREREG-ES132-WIN.md)
TRUTH = {'D01':'6.@n','D02':'22.@s','D04':'22.@n','D05':'91@s','D06':'4@l','D07':'13@s','D08':'15ρ@s','D09':'15.@s','D11':'6.@s','D14':'15.',
         'D15':'7ρ@n','D16':'24ρ'}
if __name__ == '__main__' and sys.argv[2] == 'batches':
    reads = []
    for k, r in enumerate(decoy_order[:16], 1):
        d = f'D{k:02d}'
        if d in DECOYS: reads.append(dict(kind='decoy', cid=d, pos=r[0], truth=TRUTH[d], dup=r[2]))
    assert len(reads) == 12 and all(TRUTH[x['cid']] == x['truth'] for x in reads)
    for r in cands: reads.append(dict(kind='cand', cid=r[0], pos=r[0], truth='', dup=r[2]))
    random.Random(132132).shuffle(reads)
    dec = [x for x in reads if x['kind'] == 'decoy']; can = [x for x in reads if x['kind'] == 'cand']
    batches = [dec[g*4:(g+1)*4] + can[g*8:(g+1)*8] for g in range(3)]
    for g in range(3): random.Random(132132 + g).shuffle(batches[g])
    (S/'items').mkdir(exist_ok=True); n = 0
    for g, bl in enumerate(batches, 1):
        with open(S/f'batch{g}.txt', 'w') as fh:
            for it in bl:
                n += 1; it['id'] = f'W{n:02d}'; it['batch'] = g
                W, toks, i = window(it['pos'])
                labelled(W, it['id']).save(S/'items'/f"{it['id']}.jpg", quality=92)
                b = ' '.join(t.rstrip('?') for t in toks[max(0, i-3):i-1]); a = ' '.join(t.rstrip('?') for t in toks[i:i+2])
                it.update(before=b or '(line start)', after=a or '(line end)', cur=toks[i-1])
                fh.write(f"{it['id']}\timage={S}/items/{it['id']}.jpg\tneighbours as transcribed: before [{it['before']}] TARGET after [{it['after']}]\n")
    with open(T/'win_f89'/'items.tsv', 'w', encoding='utf-8') as fh:
        fh.write('# ES132-WIN reads (built by win_f89/build.py; kind, current token and the duplicate token were never shown to the reader)\n')
        fh.write('id\tbatch\tkind\tcid\tpos\ttruth\tcur\tdup\tbefore\tafter\n')
        for it in sorted(reads, key=lambda x: x['id']):
            fh.write('\t'.join(str(it[k]) for k in ('id','batch','kind','cid','pos','truth','cur','dup','before','after')) + '\n')
    print([len(b) for b in batches], [sum(x['kind'] == 'decoy' for x in b) for b in batches])
