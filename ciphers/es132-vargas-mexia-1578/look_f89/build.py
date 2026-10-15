import sys, random, json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
T = Path('/home/user/cipher-lab/ciphers/es132-vargas-mexia-1578')
S = Path('/tmp/claude-0/-home-user-cipher-lab/b1463fe1-68c7-556f-8aa2-4455e54e5023/scratchpad')
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
cand_lines = {}
for r in cands:
    pg, ln, i = r[0].split(':'); cand_lines.setdefault((pg, ln), []).append(int(i))
align = [l.rstrip('\n').split('\t') for l in open(T/'dup_align.tsv', encoding='utf-8') if not l.startswith('#')]
pool = {}
for a in align:
    if a[0] == '-' or a[3] == '-': continue
    pg, ln, i = a[0].split(':')
    if pg not in ('f89r','f89v','f90r','f91r'): continue
    if a[1].endswith('?') or a[4].endswith('?'): continue
    if not a[6].startswith('differ'): continue
    if any(abs(int(i)-j) <= 2 for j in cand_lines.get((pg, ln), [])): continue
    pool.setdefault(a[6], []).append(a)
rng = random.Random(1589)
decoys = []
for c in ('differ-base', 'differ-vowel', 'differ-mark'):
    decoys += rng.sample(sorted(pool[c]), 4)
items = [dict(kind='cand', f89=r[0], x=r[1], P=r[2], dup=r[3], act=r[4]) for r in cands]
items += [dict(kind='decoy', f89=a[0], x=a[1], P=a[4], dup=a[3], act=a[6]) for a in decoys]
random.Random(15).shuffle(items)
BOX = {}
for dn in ('f89', 'dup'):
    for e in json.load(open(S/dn/'manifest.json'))['iiif_lines']: BOX[(dn, e['crop'])] = e['box']
def crop(dirn, pg, ln):
    a, b = (Image.open(S/dirn/f'{pg}_{ln}_s{k}.jpg').convert('L') for k in (1, 2))
    ba, bb = BOX[(dirn, f'{pg}_{ln}_s1.jpg')], BOX[(dirn, f'{pg}_{ln}_s2.jpg')]
    cut = ba[2] - bb[0]
    b = b.crop((cut, 0, b.width, b.height))
    out = Image.new('L', (a.width + b.width, max(a.height, b.height)), 255)
    out.paste(a, (0, 0)); out.paste(b, (a.width, 0))
    return out
def ctx(p):
    toks, i = tokat(p)
    b = ' '.join(t.rstrip('?') for t in toks[max(0, i-3):i-1]); a = ' '.join(t.rstrip('?') for t in toks[i:i+2])
    return i, len(toks), b, a
for n, it in enumerate(items, 1):
    it['id'] = f'I{n:02d}'
    pg, ln, _ = it['f89'].split(':'); dp, dl, _ = it['dup'].split(':')
    A, B = crop('f89', pg, ln), crop('dup', dp, dl)
    W = max(A.width, B.width); sc = min(1.0, 2600 / W)
    A = A.resize((int(A.width*sc), int(A.height*sc))); B = B.resize((int(B.width*sc), int(B.height*sc)))
    out = Image.new('L', (max(A.width, B.width), A.height + B.height + 120), 255)
    d = ImageDraw.Draw(out)
    try: f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 36)
    except Exception: f = ImageFont.load_default()
    d.text((10, 5), f'{it["id"]}  PANEL A', fill=0, font=f); out.paste(A, (0, 50))
    d.text((10, A.height + 65), f'{it["id"]}  PANEL B', fill=0, font=f); out.paste(B, (0, A.height + 110))
    out.save(S/'items'/f'{it["id"]}.jpg', quality=88)
    ia, na, ba, aa = ctx(it['f89']); ib, nb, bb, ab = ctx(it['dup'])
    it.update(A_idx=ia, A_n=na, A_before=ba, A_after=aa, B_idx=ib, B_n=nb, B_before=bb, B_after=ab)
json.dump(items, open(S/'items.json', 'w'), ensure_ascii=False, indent=1)
for b, sl in enumerate([items[:18], items[18:35], items[35:]], 1):
    with open(S/f'batch{b}.txt', 'w') as fh:
        for it in sl:
            fh.write(f"{it['id']}\timage={S}/items/{it['id']}.jpg\tA: token {it['A_idx']} of {it['A_n']} in the line; neighbours as transcribed: before [{it['A_before']}] after [{it['A_after']}]\tB: token {it['B_idx']} of {it['B_n']}; before [{it['B_before']}] after [{it['B_after']}]\tPROPOSAL P = {it['P']}\n")
print(len(items), sum(i['kind']=='decoy' for i in items), [sum(i['kind']=='decoy' for i in sl) for sl in (items[:18], items[18:35], items[35:])])
