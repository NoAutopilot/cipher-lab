#!/usr/bin/env python3
"""TXE3-2 FLOOR (11 Oct 2026): cut the blind material for the 18 floor positions and 18 same-line controls on no.87.

Writes benchmark-tx/txeng3/2/items/: per line call <line>/ with marked crop(s), tiles, and a prompt-facing items table
(items.tsv: call, label, tile, crop, sheet line, bracketed sheet text, letter index) that says nothing about floor/control,
reads, key values or truth. key.tsv (floor/control, truth set, reads, flag) is for the scorer only, never a subagent.
Seed 20261011 (PREREG-txeng3-2.md step 2).
"""
import csv, json, random, difflib, re, os, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT = Path(__file__).resolve().parents[3]
B = ROOT / 'ciphers/nevers-birago-fr3251-1572'
OUT = Path(__file__).resolve().parent
ITEMS = OUT / 'items'; ITEMS.mkdir(exist_ok=True)
OFF = {'f178r': (4700, 3720), 'f178v': (1703, 848), 'f179r': (4800, 1000)}
SHEET_OFF = (4700, 680)
ERRS = ['err_L', 'err_A', 'err_B', 'err_C', 'err_E', 'err_F']

def tsv(p, comment='#'):
    return list(csv.DictReader((l for l in open(p) if not l.startswith(comment)), delimiter='\t'))

pos6 = tsv(OUT / 'positions6.tsv')
truth = {(r['line'], r['pos']): r for r in tsv(ROOT / 'benchmark-tx/birago1572-no87.truth.tsv')}
floor = [r for r in pos6 if all(r[k] == '1' for k in ERRS)]
assert len(floor) == 18, len(floor)
rng = random.Random(20261011)
controls = []
for f in floor:
    cands = [r for r in pos6 if r['line'] == f['line'] and all(r[k] == '0' for k in ERRS)
             and truth[(r['line'], r['pos'])]['flag'] == '' and (r['line'], r['pos']) not in {(c['line'], c['pos']) for c in controls}]
    controls.append(rng.choice(cands))
sel = [(f, 'floor') for f in floor] + [(c, 'control') for c in controls]

# --- sign boxes in source-image frame
boxes = {}
bt = tsv(B / 'atlas/no87_box_token.tsv'); sg = {r['sid']: r for r in tsv(B / 'atlas/signs.tsv')}
for r in bt:
    if r['sid'] in sg:
        s = sg[r['sid']]; boxes[(r['line'], r['pos'])] = (int(s['x']), int(s['y']), int(s['w']), int(s['h']), 'atlas')
seg = tsv(OUT / 'seg_f178r/signs.tsv')
committed = {}
for r in tsv(ROOT / 'benchmark-tx/outputs/birago1572-no87/passC.tsv'):
    committed[r['line']] = committed.get(r['line'], 0) + 1
for ln in ('1', '2', '3'):
    bx = sorted([r for r in seg if r['line'] == ln], key=lambda r: int(r['x']))
    line = f'f178r_L0{ln}'; n = committed[line]
    for p in range(1, n + 1):
        if len(bx) == n: s = bx[p - 1]; how = 'seg-exact'
        else: s = bx[min(len(bx) - 1, round((p - 0.5) / n * len(bx) - 0.5))]; how = f'seg-proportional({len(bx)}/{n})'
        boxes[(line, str(p))] = (int(s['x']), int(s['y']), int(s['w']), int(s['h']), how)

# --- crops the readers saw
man = {}
for leaf in OFF:
    for e in json.load(open(B / f'harvest/{leaf}/manifest.json'))['iiif_lines']:
        man[e['crop']] = e['box']
def crop_for(line, x):
    leaf = line.split('_')[0]; ox, oy = OFF[leaf]
    best = None
    for s in ('s1', 's2', 's3'):
        c = f'{line}_{s}.jpg'
        if c not in man: continue
        x0, y0, x1, y1 = man[c]; cx0, cx1 = x0 - ox, x1 - ox
        if cx0 <= x <= cx1:
            m = min(x - cx0, cx1 - x)
            if best is None or m > best[0]: best = (m, c, cx0, y0 - oy)
    return best[1], best[2], best[3]

# --- clerk sheet mapping: truth position -> align row -> letter in plain_raw -> sheet line/word
def fold(s): return re.sub(r'[^a-z]', '', s.lower().replace('ß', 'ss'))
pairs = {r['cipher_line']: r['plain_raw'] for r in tsv(B / 'harvest/align87/pairs.tsv')}
align = {}
for r in tsv(B / 'harvest/align87/align_real.tsv'):
    align.setdefault(r['cipher_line'], []).append(r)
sheet = tsv(B / 'harvest/f179r_sheet/decipherment_sheet.tsv')
sheet_letters = []  # (sheet line, word index, char index in word)
sheet_words = {}
for srow in sheet:
    words = srow['text'].split()
    sheet_words[srow['line']] = words
    for wi, w in enumerate(words):
        for ch in w:
            if ch.isalpha(): sheet_letters.append((srow['line'], wi, ch.lower()))
sheet_fold = ''.join(x[2] for x in sheet_letters)
line_offsets = {}
for leaf in ('f178r', 'f178v', 'f179r'):
    lines = sorted({r['line'] for r in pos6 if r['line'].startswith(leaf)} | {k[0] for k in truth if k[0].startswith(leaf)})
    off = 0
    for ln in lines:
        line_offsets[ln] = off; off += committed[ln]
def letter_index(line, pos):
    leaf = line.split('_')[0]; idx = line_offsets[line] + int(pos) - 1
    rows = align[leaf]; raw = pairs[leaf]; rf = fold(raw)
    cur = 0; hit = None
    for i, r in enumerate(rows):
        ch = fold(r['plain_chunk'])
        if not ch:
            if i == idx: hit = cur; break
            continue
        j = rf.find(ch, cur)
        if j < 0 or j - cur > 20: j = cur
        if i == idx: hit = j; break
        cur = j + len(ch)
    return rf, hit
def sheet_locate(line, pos):
    leaf = line.split('_')[0]
    rf, hit = letter_index(line, pos)
    sm = difflib.SequenceMatcher(None, rf, sheet_fold, autojunk=False)
    for a, b, n in sm.get_matching_blocks():
        if a <= hit < a + n:
            sl, wi, _ = sheet_letters[b + hit - a]
            # char index within the word among letters
            k = sum(1 for x in sheet_letters[:b + hit - a] if x[0] == sl and x[1] == wi)
            return sl, wi, k
    return None, None, None

font = ImageFont.load_default(28) if hasattr(ImageFont, 'load_default') else None
items = []; key = []
calls = {}
for r, kind in sel:
    calls.setdefault(r['line'], []).append((r, kind))
labels_all = 'ABCDEFGHJKLM'
for line, lst in calls.items():
    rng.shuffle(lst)
    leaf = line.split('_')[0]; ox, oy = OFF[leaf]
    src = Image.open(next((B / f'harvest/{leaf}').glob('src_*.jpg')))
    d = ITEMS / line; d.mkdir(exist_ok=True)
    marks = {}
    for li, (r, kind) in enumerate(lst):
        lab = labels_all[li]; x, y, w, h, how = boxes[(line, r['pos'])]
        cx = x + w // 2
        crop, cx0, cy0 = crop_for(line, cx)
        marks.setdefault(crop, []).append((lab, x - cx0, y - cy0, w, h))
        m = 14
        tile = src.crop((max(0, x - m), max(0, y - m), x + w + m, y + h + m)).resize(((w + 2 * m) * 3, (h + 2 * m) * 3), Image.LANCZOS)
        tf = d / f'tile_{lab}.png'; tile.save(tf)
        sl, wi, k = sheet_locate(line, r['pos'])
        words = list(sheet_words[sl]) if sl else []
        if sl is not None: words[wi] = '[' + words[wi] + ']'
        items.append(dict(call=line, label=lab, tile=str(tf.relative_to(ROOT)), crop=crop, box_how=how,
                          sheet_line=sl or '', sheet_text=' '.join(words), letter_index=('' if k is None else k + 1)))
        t = truth[(line, r['pos'])]
        key.append(dict(call=line, label=lab, kind=kind, line=line, pos=r['pos'], plain=r['plain'], truth=r['truth'],
                        reads='|'.join(r['read_' + p] for p in 'LABCEF'), flag=t['flag'], err_class=r['err_class'],
                        pos_class=r['pos_class'], seg_edge=r['seg_edge'], band_edge=r['band_edge'], stroke=r['stroke']))
    for crop, ms in marks.items():
        im = Image.open(B / f'harvest/{leaf}/{crop}').convert('RGB')
        W, H = im.size; pad = 46
        out = Image.new('RGB', (W, H + pad), 'white'); out.paste(im, (0, pad))
        dr = ImageDraw.Draw(out)
        for lab, bx, by, bw, bh in ms:
            dr.rectangle([bx - 2, pad + max(0, by) - 2, bx + bw + 2, pad + by + bh + 2], outline=(0, 114, 178), width=2)
            dr.line([bx + bw // 2, 30, bx + bw // 2, pad + max(0, by)], fill=(0, 114, 178), width=2)
            dr.text((bx + bw // 2 - 8, 2), lab, fill=(0, 114, 178), font=font)
        out.save(d / f'marked_{crop[:-4]}.png')
with open(OUT / 'items.tsv', 'w') as f:
    w = csv.DictWriter(f, fieldnames=list(items[0].keys()), delimiter='\t'); w.writeheader(); w.writerows(items)
with open(OUT / 'key.tsv', 'w') as f:
    f.write('# TXE3-2 scorer key: never shown to a subagent\n')
    w = csv.DictWriter(f, fieldnames=list(key[0].keys()), delimiter='\t'); w.writeheader(); w.writerows(key)
print(len(items), 'items in', len(calls), 'calls')
for it in items: print(it['call'], it['label'], it['crop'], it['box_how'], it['sheet_line'], it['letter_index'], it['sheet_text'][:90])
