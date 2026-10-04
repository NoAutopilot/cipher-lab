#!/usr/bin/env python3
"""N7-VIV53L: per-tile window montages for the look-alike re-read (second instrument, after the first four calls echoed passC).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv53L_windows.py PAGE

Why: the first re-read calls (tx/lookalike53L/*/53L_*_reread_VOID1.tsv) were given an id-only sheet and 40-90 full line crops each;
all four copied the passC label instead of reading shapes. Here every SPLIT tile of the page (status 'split' in agreement.tsv; gaps
are not re-read and stay M, PREREG-N7VIV53L rule 2) gets a small window cut from its line: the line's segments (images/p53, boxes
from manifest.json) are stitched on source x, the ink extent is found from the column profile, the tile's x is estimated as
pos/len along the inked span, and a window of about +-6 sign widths is cut, upscaled 2x, with a red tick at the estimate.
Windows go 6 to a montage image, each captioned with its tile id. The prompt lists per tile the 3 labels before and after it
(from the reading, for locating the sign) and the candidate ids in alphabetical order with their SIGNS.md shape descriptions --
it never says which candidate is the current reading. Writes tx/lookalike53L/<PAGE>/win/*.png, 53L_<PAGE>_splits_tiles.tsv
(the packet's tiles restricted to splits, for `lookalike_pass.py reconcile`) and 53L_<PAGE>_win_prompt.md.
"""
import csv, json, os, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
IMG = os.path.join(T, 'images', 'p53')
DESC = {
    'a': 'plain a', 'b': 'plain b', 'c': 'plain c (small open c-stroke)', 'd': 'round body, ascender curling back left (like ∂)',
    'e': 'plain e', 'g': 'plain g (closed bowl, looped descender)', 'h': 'plain h', 'j': 'plain j', 'k': 'plain k', 'l': 'plain l',
    'm': 'three humps', 'n': 'two humps', 'o': 'small round o', 'p': 'p with a descender (like ꝑ)', 'r': 'plain r', 's': 'short closed s',
    'x': 'plain x', 'y': 'y, incl. long swash y with lead-in stroke', 'z': 'FLAT-topped z', 'tz': 't joined to a z-like descender',
    'to': 'joined t + closed loop', '3': 'ROUND-topped 3 with descender', '#': 'double-crossed sign like # / ‡', ':': 'two dots side by side',
    'P': 'pi-like, two uprights with a top bar (π / II)', 'S': 'long s ſ, tall stroke below the line, no crossbar', 'f': 'f with crossbar',
    'A': 'capital A', '@': 'a with a large curling loop on its left', 'V': 'long backslash / V stroke', 'R': 'r-like with a loop (Ꝛ, "rt")',
    'L': 'capital L / ℓ', '2': 'digit 2', '4': 'digit 4 / crossed-descender sign', '+': 'cross-shaped sign with crossed descender',
    '6': 'digit 6', '7': 'digit 7', '8': 'digit 8', 'u': 'plain u (two open strokes)', 'i': 'plain i',
}


def boxes(page):
    m = json.load(open(os.path.join(IMG, 'manifest.json')))['iiif_lines']
    out = {}
    for e in m:
        c = e['crop']
        if f'_{page}_L' in c:
            ln = c.split(f'_{page}_')[1].split('_s')[0]
            out.setdefault(ln, []).append((e['box'][0], c))
    return {k: sorted(v) for k, v in out.items()}


def strip(segs):
    x0 = segs[0][0]
    ims = [(x - x0, Image.open(os.path.join(IMG, c)).convert('L')) for x, c in segs]
    w = max(o + im.width for o, im in ims); h = max(im.height for _, im in ims)
    S = Image.new('L', (w, h), 255)
    for o, im in ims:
        S.paste(im, (o, 0))
    return S


def window(strips, bx, nline, passage, pos):
    page, ln = passage.split('_', 1)
    key = (page, ln)
    if key not in strips:
        S = strip(bx[page][ln])
        px = S.load(); W, H = S.size
        ink = [sum(1 for y in range(H) if px[x, y] < 110) for x in range(W)]
        cols = [x for x in range(W) if ink[x] >= 2]
        strips[key] = (S, cols[0] if cols else 0, cols[-1] if cols else W)
    S, a, b = strips[key]
    sw = (b - a) / max(1, nline[passage])
    x = a + (pos - 0.5) * sw
    lo, hi = int(max(0, x - 6.5 * sw)), int(min(S.width, x + 6.5 * sw))
    w = S.crop((lo, 0, hi, S.height)).convert('RGB')
    w = w.resize((w.width * 2, w.height * 2))
    dr = ImageDraw.Draw(w); tx = int((x - lo) * 2)
    dr.line((tx, 0, tx, 14), fill='red', width=3); dr.line((tx, w.height - 14, tx, w.height), fill='red', width=3)
    return w


def montage(wins, d, stem):
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 22)
    except OSError:
        font = ImageFont.load_default()
    pngs = []
    for k in range(0, len(wins), 6):
        grp = wins[k:k + 6]
        W = max(w.width for _, w in grp); Hh = sum(w.height + 34 for _, w in grp)
        M = Image.new('RGB', (W, Hh), 'white'); dr = ImageDraw.Draw(M); y = 0
        for tid, w in grp:
            dr.text((6, y + 4), tid, fill='blue', font=font); M.paste(w, (0, y + 32)); y += w.height + 34
        p = os.path.join(d, f'{stem}{k // 6 + 1:02d}.png'); M.save(p); pngs.append(p)
    return pngs


def audit():
    """Windows for tools/lookalike_pass.py audit items (tx/lookalike53L/audit/53L_audit_items.tsv): item id captions, alphabetical
    candidates, the shown label never singled out. Writes audit/win/ and audit/53L_audit_win_prompt.md."""
    d = os.path.join(HERE, 'lookalike53L', 'audit')
    items = list(csv.DictReader(open(os.path.join(d, '53L_audit_items.tsv')), delimiter='\t'))
    pc = list(csv.DictReader(open(os.path.join(HERE, 'lookalike53L', 'passC.tsv')), delimiter='\t'))
    nline, seqs = {}, {}
    for r in pc:
        nline[r['line']] = nline.get(r['line'], 0) + 1; seqs.setdefault(r['line'], []).append(r['sign'])
    bx = {p: boxes(p) for p in ('f170r', 'f170v', 'f171r', 'f171v')}
    strips, wins, lines = {}, [], []
    shown = {(it['line'], int(it['pos'])): it['shown'] for it in items}
    for it in sorted(items, key=lambda r: int(r['item'])):
        ln, pos = it['line'], int(it['pos'])
        wins.append((f"item {it['item']}", window(strips, bx, nline, ln, pos)))
        seq = [shown.get((ln, i + 1), s) for i, s in enumerate(seqs[ln])]
        cand = sorted(set(it['candidates'].split(',')))
        cd = '; '.join(f"{c} = {DESC.get(c, c.strip('{}') + ' (free description)')}" for c in cand)
        lines.append(f"{it['item']}\tbefore: {' '.join(seq[max(0, pos - 4):pos - 1])} | after: {' '.join(seq[pos:pos + 3])}\tcandidates: {cd}")
    os.makedirs(os.path.join(d, 'win'), exist_ok=True)
    pngs = montage(wins, os.path.join(d, 'win'), 'audit_win')
    prompt = f"""# Proofreading audit by window, 53L (value-blind)

{len(items)} items. Each item has its own window image: open the montages below IN ORDER (6 windows each, captioned in blue "item N").
In each window the red ticks mark the ESTIMATED position of the item's sign (can be off by 1-3 signs). Find the sign using the labels
of the 3 signs before and after it (keyboard look-alike ids, see SIGNS.md), then decide which candidate's SHAPE it is. Some items are
deliberately wrong in the reading; judge only the shape. Candidates are alphabetical.

Montages: {', '.join(pngs)}

Answer one TSV row per item, header: item<TAB>label<TAB>conf<TAB>second<TAB>note
  label = one candidate id, X_NEW if none fits, SPLIT:a|b if you cannot choose; conf H clear / M probable / L guess (L whenever you
  could not find the sign); second = runner-up or empty; note = the shape feature you SAW.

Items (item, context, candidates):
""" + '\n'.join(lines) + '\n'
    open(os.path.join(d, '53L_audit_win_prompt.md'), 'w').write(prompt)
    print('audit', len(items), 'items,', len(pngs), 'montages')


def main():
    if sys.argv[1] == 'audit':
        return audit()
    page = sys.argv[1]
    d = os.path.join(HERE, 'lookalike53L', page)
    tiles = list(csv.DictReader(open(os.path.join(d, f'53L_{page}_tiles.tsv')), delimiter='\t'))
    splits = [t for t in tiles if t['status'] == 'split']
    pc = list(csv.DictReader(open(os.path.join(d, 'passC.tsv')), delimiter='\t'))
    nline = {}
    for r in pc:
        nline[r['passage']] = nline.get(r['passage'], 0) + 1
    bx = boxes(page)
    strips = {}
    wins = []
    for t in splits:
        ln = t['passage'].split('_', 1)[1]
        if ln not in strips:
            S = strips[ln] = strip(bx[ln])
            px = S.load(); W, H = S.size
            ink = [sum(1 for y in range(H) if px[x, y] < 110) for x in range(W)]
            cols = [x for x in range(W) if ink[x] >= 2]
            strips[ln] = (S, cols[0] if cols else 0, cols[-1] if cols else W)
        S, a, b = strips[ln]
        n = nline[t['passage']]; pos = int(t['pos'])
        sw = (b - a) / max(1, n)
        x = a + (pos - 0.5) * sw
        lo, hi = int(max(0, x - 6.5 * sw)), int(min(S.width, x + 6.5 * sw))
        w = S.crop((lo, 0, hi, S.height)).convert('RGB')
        w = w.resize((w.width * 2, w.height * 2))
        dr = ImageDraw.Draw(w); tx = int((x - lo) * 2)
        dr.line((tx, 0, tx, 14), fill='red', width=3); dr.line((tx, w.height - 14, tx, w.height), fill='red', width=3)
        wins.append((f"{t['passage']}.{t['pos']}", w))
    os.makedirs(os.path.join(d, 'win'), exist_ok=True)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 22)
    except OSError:
        font = ImageFont.load_default()
    pngs = []
    for k in range(0, len(wins), 6):
        grp = wins[k:k + 6]
        W = max(w.width for _, w in grp); Hh = sum(w.height + 34 for _, w in grp)
        M = Image.new('RGB', (W, Hh), 'white'); dr = ImageDraw.Draw(M); y = 0
        for tid, w in grp:
            dr.text((6, y + 4), tid, fill='blue', font=font); M.paste(w, (0, y + 32)); y += w.height + 34
        p = os.path.join(d, 'win', f'{page}_win{k // 6 + 1:02d}.png'); M.save(p); pngs.append(p)
    with open(os.path.join(d, f'53L_{page}_splits_tiles.tsv'), 'w') as o:
        w = csv.DictWriter(o, fieldnames=list(tiles[0]), delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(splits)
    lines = []
    for t in splits:
        cand = sorted({x for x in t['candidates'].split(',') if x})
        cd = '; '.join(f"{c} = {DESC.get(c, c.strip('{}') + ' (free description)')}" for c in cand)
        lines.append(f"{t['passage']}\t{t['pos']}\tbefore: {t['before']} | after: {t['after']}\tcandidates: {cd}")
    prompt = f"""# Look-alike re-read by window, 53L {page} (value-blind, second instrument)

{len(splits)} tiles. Each tile has its own window image: open the montages below IN ORDER (6 windows each, captioned in blue with
the tile id passage.pos). In each window the red ticks top and bottom mark the ESTIMATED position of the tile's sign (the estimate
can be off by 1-3 signs). Find the sign using the labels of the 3 signs before and after it (keyboard look-alike ids, described in
SIGNS.md), then decide which candidate's SHAPE it is. The candidate list is alphabetical; nothing tells you which is "right".

Montages: {', '.join(pngs)}

Answer one TSV row per tile, header: passage<TAB>pos<TAB>label<TAB>conf<TAB>second<TAB>note
  label = one candidate id, X_NEW if none fits, SPLIT:a|b if you cannot choose; conf H clear / M probable / L guess (use L whenever
  you could not find the sign in its window); second = runner-up or empty; note = the shape feature you SAW (e.g. "flat top bar").

Tiles (passage, pos, context, candidates):
""" + '\n'.join(lines) + '\n'
    open(os.path.join(d, f'53L_{page}_win_prompt.md'), 'w').write(prompt)
    print(page, len(splits), 'split tiles,', len(pngs), 'montages')


if __name__ == '__main__':
    main()
