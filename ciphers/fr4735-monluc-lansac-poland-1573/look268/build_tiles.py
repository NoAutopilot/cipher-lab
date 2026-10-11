#!/usr/bin/env python3
"""MONL-LOOK (11 Oct 2026): crop step + tiles for tools/lookalike_pass.py windows on c268 lines 1-5.
Crop step: the c268 line bands were cut by MONLUC-KEY as manual sloped bands (iiif_lines.py's row profile split this slanted
page wrongly, images/manifest.json); here each line's two segments (x 0-1450 and 1350-2800 of the source) are stitched on
source x into look268/strips/c268_<line>.jpg. Tiles: look268/ciphertext_draft.tsv (reconcile_passes A(K38) vs B) columns that
differ; passC = ciphertext_c268.tsv. Writes look268/strips/, look268/c268_tiles.tsv, look268/c268_gapB.tsv,
look268/c268_passC.tsv, look268/candidates.png. Run from the repo root."""
import csv, json, os
from PIL import Image
D = 'ciphers/fr4735-monluc-lansac-poland-1573'; L = D + '/look268'
os.makedirs(L + '/strips', exist_ok=True)
man = json.load(open(D + '/images/manifest.json'))['iiif_lines']
for ln in ['L01', 'L02', 'L03', 'L04', 'L05']:
    segs = sorted((e for e in man if e['crop'].startswith(f'c268cipher_{ln}_')), key=lambda e: e['x'][0])
    ims = [Image.open(D + '/images/' + e['crop']).convert('L') for e in segs]
    W = segs[-1]['x'][1]; H = max(i.size[1] for i in ims)
    S = Image.new('L', (W, H), 255)
    for e, im in zip(segs, ims):
        S.paste(im, (e['x'][0], 0))
    S.save(f'{L}/strips/c268_{ln}.jpg', quality=92)
pc = list(csv.DictReader(open(D + '/ciphertext_c268.tsv'), delimiter='\t'))
with open(L + '/c268_passC.tsv', 'w') as o:
    o.write('passage\tpos\tsign_id\tconf\n')
    for r in pc:
        o.write(f"{r['line']}\t{r['pos']}\t{r['sign']}\t{r['conf']}\n")
relab = {(r['line'], r['pos']) for r in pc if r['relabel']}
dr = list(csv.DictReader(open(L + '/ciphertext_draft.tsv'), delimiter='\t'))
# map draft columns to passC positions: a column advances passC unless A is '-'
cnt, tiles, gaps = {}, [], []
seq = {}
for r in pc:
    seq.setdefault(r['line'], []).append(r['sign'])
for r in dr:
    ln = r['line']; alt = r['alt']; why = r['why']
    if why == 'agree':
        cnt[ln] = cnt.get(ln, 0) + 1; continue
    other = alt.split(':', 1)[1] if ':' in alt else ''
    if alt.startswith('A:') and other == '-':           # B-only sign: no passC position
        gaps.append(dict(passage=ln, after_pos=cnt.get(ln, 0), B=r['sign'])); continue
    cnt[ln] = cnt.get(ln, 0) + 1; pos = cnt[ln]
    A = seq[ln][pos - 1]
    B = '' if other == '-' else (other if alt.startswith('B:') else r['sign'])
    if alt.startswith('A:'):
        A2 = other
        assert A2 == A, (ln, pos, A2, A)
    st = 'split' if B else 'single'
    cand = [x for x in dict.fromkeys([A, B] + (['K63', 'K19'] if (ln, str(pos)) in relab else [])) if x]
    s = seq[ln]
    tiles.append(dict(run='c268', passage=ln, pos=pos, passC=A, A=A, B=B, status=st, why=st, candidates=','.join(cand),
                      before=' '.join(s[max(0, pos - 4):pos - 1]), after=' '.join(s[pos:pos + 3]),
                      noteA='', noteB='relabel K38 (MONLUC-RELABEL)' if (ln, str(pos)) in relab else ''))
for ln in seq:
    assert cnt[ln] == len(seq[ln]), (ln, cnt[ln], len(seq[ln]))
F = ['run', 'passage', 'pos', 'passC', 'A', 'B', 'status', 'why', 'candidates', 'before', 'after', 'noteA', 'noteB']
with open(L + '/c268_tiles.tsv', 'w') as o:
    w = csv.DictWriter(o, F, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(tiles)
with open(L + '/c268_gapB.tsv', 'w') as o:
    w = csv.DictWriter(o, ['passage', 'after_pos', 'B'], delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(gaps)
# candidate sheet: every K id used, cut from the ids-only key sheet (8 cols, 136x176 cells)
ids = sorted({c for t in tiles for c in t['candidates'].split(',') if c.startswith('K')})
ks = Image.open(D + '/images/keysheet_monluc1_ids.png'); cw, ch = 136, 176
nc = 8; out = Image.new('RGB', (nc * cw, ((len(ids) + nc - 1) // nc) * ch), 'white')
for n, k in enumerate(ids):
    i = int(k[1:]) - 1
    out.paste(ks.crop(((i % 8) * cw, (i // 8) * ch, (i % 8 + 1) * cw, (i // 8 + 1) * ch)), ((n % nc) * cw, (n // nc) * ch))
out.save(L + '/candidates.png')
print(f'tiles {len(tiles)} (split {sum(t["status"]=="split" for t in tiles)}, single {sum(t["status"]=="single" for t in tiles)}); '
      f'B-only gaps {len(gaps)}; candidate ids {len(ids)}: {" ".join(ids)}; relabel tiles {sum(1 for t in tiles if t["noteB"])}')
