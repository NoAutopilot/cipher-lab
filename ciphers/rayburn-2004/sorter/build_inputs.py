#!/usr/bin/env python3
"""Cut the Rayburn sign-sorter inputs from images/Rayburn-Cryptogram.jpg (no network, no vision model).
R9-RAYSORT, 6 Oct 2026. Ink (grey < THR) -> 8-connected components; the family member's rectangle round rows 1-2 is
dropped (components wider than 200 px or taller than 100 px); main-grid components are assigned to the nearest row
centre (R8-RAY2's centres, by eye on the debug overlay) and merged where they overlap in x (a letter with its
underline/strike and any small sign written under it = one tile); margin components (left, right) are merged where
they overlap in y. Boxes are matched in reading order to pass2/reconciled.tsv; a line whose box count differs from
the reconciled count is reported and its boxes started in '?' rather than forced.
Run: python3 ciphers/rayburn-2004/sorter/build_inputs.py [--write]"""
import csv, os, sys
from collections import deque
import numpy as np
from PIL import Image

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.join(T, 'sorter')
THR = int(os.environ.get("THR", 170))
ROWS = [68, 128, 200, 258, 330, 410, 485, 552, 618, 685]          # main-grid row centres (full-image y)
GRID_X = (130, 680)

im = Image.open(os.path.join(T, 'images', 'Rayburn-Cryptogram.jpg')).convert('L')
a = np.array(im)
ink = a < THR
H, W = ink.shape
seen = np.zeros_like(ink)
comps = []
for y0 in range(H):
    for x0 in np.nonzero(ink[y0] & ~seen[y0])[0]:
        if seen[y0, x0]:
            continue
        q = deque([(y0, x0)]); seen[y0, x0] = True
        xs, ys = [], []
        while q:
            y, x = q.popleft(); xs.append(x); ys.append(y)
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    yy, xx = y + dy, x + dx
                    if 0 <= yy < H and 0 <= xx < W and ink[yy, xx] and not seen[yy, xx]:
                        seen[yy, xx] = True; q.append((yy, xx))
        bx = [min(xs), min(ys), max(xs) + 1, max(ys) + 1, len(xs)]
        if bx[4] < 12 or bx[2] - bx[0] > 200 or bx[3] - bx[1] > 100:
            continue
        comps.append(bx)

def merge(cs, axis, slack=3):
    cs = sorted(cs, key=lambda c: c[axis])
    out = []
    for c in cs:
        if out and c[axis] <= out[-1][axis + 2] + slack:
            o = out[-1]; out[-1] = [min(o[0], c[0]), min(o[1], c[1]), max(o[2], c[2]), max(o[3], c[3]), o[4] + c[4]]
        else:
            out.append(list(c))
    return out

cx = lambda c: (c[0] + c[2]) / 2
cy = lambda c: (c[1] + c[3]) / 2
# row base lines through the first and last sign of each row (full-image px, read on the component overlay)
ROWLINES = [((155, 72), (480, 52)), ((155, 155), (625, 122)), ((165, 200), (330, 205)), ((165, 265), (630, 245)),
            ((175, 345), (625, 315)), ((180, 445), (460, 405)), ((180, 515), (650, 465)), ((190, 575), (690, 520)),
            ((190, 640), (690, 595)), ((190, 690), (720, 670))]
def row_y(r, x):
    (x0, y0), (x1, y1) = ROWLINES[r]
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

def frame(c):
    """a piece of the rectangle the family member drew round rows 1-2 (post body: not the writer's)."""
    w, h = c[2] - c[0], c[3] - c[1]
    thin = min(w, h) <= 16 and max(w, h) >= 3 * min(w, h)
    return thin and (cy(c) < 45 or (c[0] < 135 and cy(c) < 180) or (c[0] > 615 and cy(c) < 150)
                     or (420 < cx(c) < 600 and 133 < cy(c) < 160 and w > 60))

def union2d(cs, slack):
    cs = [list(c) for c in cs]
    changed = True
    while changed:
        changed = False
        for i in range(len(cs)):
            for j in range(i + 1, len(cs)):
                a_, b_ = cs[i], cs[j]
                if a_[0] - slack <= b_[2] and b_[0] - slack <= a_[2] and a_[1] - slack <= b_[3] and b_[1] - slack <= a_[3]:
                    cs[i] = [min(a_[0], b_[0]), min(a_[1], b_[1]), max(a_[2], b_[2]), max(a_[3], b_[3]), a_[4] + b_[4]]
                    del cs[j]; changed = True; break
            if changed:
                break
    return cs

lines = {}
EXCLUDED = []          # the vertical note word beside right-margin 2 and the circled mark below the grid (not in N)
for c in comps:
    if 40 < cy(c) < 720 and cx(c) < 130 and c[2] < 135:
        lines.setdefault('left', []).append(c)
    elif 40 < cy(c) < 720 and c[0] >= 695:
        lines.setdefault('right', []).append(c)
    elif GRID_X[0] <= cx(c) <= GRID_X[1] + 40 and 25 < cy(c) < 720:
        if frame(c):
            continue
        r = min(range(10), key=lambda k: abs(row_y(k, cx(c)) - cy(c)))
        lines.setdefault(f'main{r + 1:02d}', []).append(c)
    elif cy(c) >= 720:
        EXCLUDED.append(c)
# a small sign written just under a sign of the row above (k+r, A+m, R+H, a+v) belongs to that sign
for r in range(1, 10):
    up, me = lines[f'main{r:02d}'], lines[f'main{r + 1:02d}']
    for c in list(me):
        for u in up:
            if c[0] < u[2] and u[0] < c[2] and 0 <= c[1] - u[3] <= 12 and (c[3] - c[1]) < 35 and c[4] < 260 \
                    and cy(c) - row_y(r - 1, cx(c)) < 45:
                me.remove(c); up.append(c); break
boxes = {}
for ln, cs in lines.items():
    if ln in ('left', 'right'):
        if ln == 'right':                  # the vertical handwritten word ("Append"/"Approved") beside right 2
            note = [c for c in cs if c[2] <= 724 and 145 < cy(c) < 240]
            EXCLUDED.extend(note); cs = [c for c in cs if c not in note]
        m = sorted(union2d(cs, 6), key=lambda b: b[1])
        if ln == 'right':                  # the bottom sign is a stroke and a separate hook/dot ("?-dot", 1.?)
            low = [b for b in m if cy(b) > 620]
            m = [b for b in m if cy(b) <= 620] + union2d(low, 30)
    else:
        m = merge(cs, 0)
    boxes[ln] = [b for b in m if b[4] >= 40]

if __name__ == '__main__' and '--write' not in sys.argv:
    for ln in sorted(boxes):
        print(ln, len(boxes[ln]), [(b[0], b[1], b[2] - b[0], b[3] - b[1], b[4]) for b in boxes[ln]])


# ---------- labels and focus: pass2/reconciled.tsv (starting pile) and the two blind passes' readings ----------
# (pass A = ciphertext.tsv as transcribed, pass B = R8-RAY2's blind Sonnet pass; '-' = that pass has no sign there).
# Hand-aligned from pass2/passA.tsv, passB.tsv and disagreements.tsv; only positions where the passes differ.
SPLITS = {
    ('main01', 3): ('u', 'u or v'),
    ('main02', 6): ('i', 'I or i'), ('main02', 7): ('s', 'S'),
    ('main03', 2): ('rn', 'm'),
    ('main04', 4): ('a bold I', 'E'),
    ('main05', 2): ('-', 'n'), ('main05', 3): ('L (unsure)', 'L'), ('main05', 5): ('y or x', 'Y'),
    ('main05', 6): ('u', 'u or v'), ('main05', 7): ('a bold I', 'I'),
    ('main06', 1): ('w', 'W or m'), ('main06', 5): ('Y', 'Y or V'),
    ('main07', 1): ('b', 't or a cross'), ('main07', 3): ('k with r under it', 'k'), ('main07', 4): ('a cross or t', 't'),
    ('main08', 1): ('A with m under it', 'A'), ('main08', 2): ('c', 'c or r'), ('main08', 4): ('-', 'f'),
    ('main08', 7): ('Z', 'z'),
    ('main09', 1): ('-', 'C'), ('main09', 2): ('R with H under it', 'R'), ('main09', 5): ('-', 'X'),
    ('main09', 6): ('-', 'a'), ('main09', 7): ('-', 'Z'),
    ('main10', 2): ('f', 'f with r under it'), ('main10', 5): ('a with v under it', 'a with v under it'),
    ('main10', 7): ('r', '-'),
    ('left', 1): ('p', 'p or P'), ('left', 4): ('4 or h7', '4 or H'), ('left', 5): ('p with a loop', 'P or q'),
    ('left', 6): ('d with a loop', '@'), ('left', 7): ('Y with a tail', 'h or n'), ('left', 8): ('K or star', 'asterisk'),
    ('right', 1): ('crossed X', 'X'), ('right', 2): ('&', '8'), ('right', 3): ('#', '# or H'), ('right', 4): ('N', 'Z'),
    ('right', 5): ('K', 'V'), ('right', 6): ('H or #', '# or H'), ('right', 8): ('a hook and dot', '2 or ? and O or Q'),
}
RENAME = {'?-dot': 'hook-dot'}          # a pile id starting with '?' would read as unsorted on the page
PAD = 8


def write():
    import json
    rec = list(csv.DictReader(open(os.path.join(T, 'pass2', 'reconciled.tsv')), delimiter='\t'))
    want = {}
    for r in rec:
        ln = f"main{int(r['row']):02d}" if r['group'] == 'main' else r['group']
        want.setdefault(ln, []).append(r)
    order = [f'main{i:02d}' for i in range(1, 11)] + ['left', 'right']
    os.makedirs(os.path.join(S, 'pages'), exist_ok=True)
    signs, labels, focus, cl = [], [], [], []
    for ln in order:
        bs, rs = boxes[ln], want[ln]
        if len(bs) != len(rs):
            sys.exit(f'{ln}: {len(bs)} boxes vs {len(rs)} reconciled tokens -- fix the cut, do not force')
        x0 = max(0, min(b[0] for b in bs) - PAD); x1 = min(W, max(b[2] for b in bs) + PAD)
        y0 = max(0, min(b[1] for b in bs) - PAD); y1 = min(H, max(b[3] for b in bs) + PAD)
        im.crop((x0, y0, x1, y1)).save(os.path.join(S, 'pages', f'{ln}.png'))
        cl.append(f'{ln}')
        for k, (b, r) in enumerate(zip(bs, rs), 1):
            sid = f'{ln}_{k:02d}'
            sign = RENAME.get(r['sign'], r['sign'])
            fam = 'margin' if ln in ('left', 'right') else sign.split('+')[0].lower()
            signs.append((sid, ln, int(b[0] - x0), int(b[1] - y0), int(b[2] - b[0]), int(b[3] - b[1])))
            labels.append((sid, sign, fam))
            sp = SPLITS.get((ln, k))
            if sp:
                where = ln + ' margin' if ln in ('left', 'right') else 'row ' + str(int(ln[4:]))
                q = (f"{where}, sign {k}: started as '{sign}' from the reconciled reading; one blind reader saw "
                     f"'{sp[0]}', the other '{sp[1]}'. Which pile is it (or a pile of its own, or not a letter)?")
                if ln in ('left', 'right'):
                    q += ' The margin signs may have been written with the sheet turned 90 degrees.'
                focus.append((sid, q))
    def tsv(name, head, rows):
        with open(os.path.join(S, name), 'w', newline='') as f:
            w = csv.writer(f, delimiter='\t', lineterminator='\n')
            if head: w.writerow(head)
            w.writerows(rows)
    tsv('signs.tsv', ('sid', 'page', 'x', 'y', 'w', 'h'), signs)
    tsv('labels.tsv', ('sid', 'sign', 'family'), labels)
    tsv('focus.tsv', None, focus)
    open(os.path.join(S, 'cipher_lines.tsv'), 'w').write('\n'.join(cl) + '\n')
    print(f'{len(signs)} tiles on {len(cl)} lines, {len({l[1] for l in labels})} starting piles, {len(focus)} focus tiles')


if __name__ == '__main__' and '--write' in sys.argv:
    write()
