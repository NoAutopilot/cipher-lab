#!/usr/bin/env python3
"""A1B-FILS-UPPER (3 Oct 2026): cut one word-window crop per M/U token of the upper letter (U01-U26, B11, M1-M4).

Tokens are read from clear_f35r.tsv: {..} = M (or U when it holds ' / '), [...] = U. Word positions were never
recorded, so each window is centred on the token's proportional character offset along the line image (s1 full +
s2 right half = 3600 px for U/B rows; the single margin strip for M rows) and is 1100 px wide (about three to four words), mapped inside the line's own ink extent (ruled margin lines masked), so the
target word sits inside it with its neighbours. Writes targets.tsv (crop id, row, token index, token, grade) and
crops/*.jpg via ImageMagick `convert` (PIL is not installed in this container). Usage: python3 verify/upper_mu/cut_mu.py
"""
import re, subprocess, os, sys
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(os.path.dirname(D)); IM = os.path.join(T, 'images')
os.makedirs(os.path.join(D, 'crops'), exist_ok=True); os.makedirs(os.environ.get('LINES_DIR', '/tmp/fils_lines'), exist_ok=True)
TOK = re.compile(r'<del>.*?</del>|\{[^}]*\}|\S+')
rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(T, 'clear_f35r.tsv')) if re.match(r'(U\d\d|B11|M\d)\t', l)]
WIN = 1100


def ink_extent(p):
    """Left/right ink bounds on the middle band of rows, ignoring ruled vertical lines (columns dark over >70% of rows)."""
    raw = subprocess.run(['convert', p, '-colorspace', 'gray', '-depth', '8', 'pgm:-'], capture_output=True).stdout
    hdr = raw.split(b'\n', 3); w, h = map(int, hdr[1].split()); px = hdr[3]
    rule = [sum(1 for y in range(h) if px[y * w + x] < 80) > 0.7 * h for x in range(w)]
    y0, y1 = int(h * .3), int(h * .7)
    cols = [0 if any(rule[max(0, x - 8):x + 8]) else sum(1 for y in range(y0, y1) if px[y * w + x] < 80) for x in range(w)]
    sm = [sum(cols[max(0, x - 20):x + 20]) for x in range(w)]
    ink = [x for x in range(w) if sm[x] >= 25]
    return ink[0], ink[-1]


out = ['crop\trow\ttok_idx\ttoken\tgrade\tx0\tline_w']
n = 0
for r, text, *_ in rows:
    if r.startswith('U'):
        a, b = f'{IM}/f43u_L{r[1:]}_s1.jpg', f'{IM}/f43u_L{r[1:]}_s2.jpg'
    elif r == 'B11':
        a, b = f'{IM}/f43b_L03_s1.jpg', f'{IM}/f43b_L03_s2.jpg'
    else:
        a, b = f'{IM}/f43m_L0{r[1:]}.jpg', None
    line = os.path.join(os.environ.get('LINES_DIR', '/tmp/fils_lines'), f'{r}.png')
    if b:
        subprocess.run(['convert', a, '(', b, '-crop', '1200x+1200+0', '+repage', ')', '+append', line], check=True)
    else:
        subprocess.run(['convert', a, line], check=True)
    W, H = map(int, subprocess.run(['identify', '-format', '%w %h', line], capture_output=True, text=True).stdout.split())
    a0, a1 = ink_extent(line)
    toks = TOK.findall(text); disp = [re.sub(r'<del>|</del>|[{}]', '', t).split(' / ')[0] for t in toks]
    total = sum(len(d) + 1 for d in disp); off = 0
    for i, (t, d) in enumerate(zip(toks, disp)):
        c = off + len(d) / 2; off += len(d) + 1
        if '{' in t or '[...]' in t:
            g = 'U' if ('[...]' in t or ' / ' in t) else 'M'
            n += 1; cid = f'w{n:02d}'
            x = int(a0 + c / total * (a1 - a0)); x0 = max(0, min(W - WIN, x - WIN // 2))
            subprocess.run(['convert', line, '-crop', f'{WIN}x{H}+{x0}+0', '+repage', os.path.join(D, 'crops', f'{cid}.jpg')], check=True)
            out.append(f'{cid}\t{r}\t{i}\t{t}\t{g}\t{x0}\t{W}')
open(os.path.join(D, 'targets.tsv'), 'w').write('\n'.join(out) + '\n')
print(n, 'crops')
