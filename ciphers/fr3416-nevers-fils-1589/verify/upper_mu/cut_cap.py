#!/usr/bin/env python3
"""A1B-FILS-UPPER2 (3 Oct 2026): capability-check crops for the blind Opus reader of the upper letter's M/U words.

Picks 6 H-graded words (plain tokens, >= 5 letters, no {..}/[...] token within 2 places either side) from rows U01-U26
with random.Random(20261003), and cuts each as the same 1100-px word window cut_mu.py uses (same line build, same ink
extent, same proportional placement), except OVERRIDE: c06 (U22) first cut at x0=0 showed only margin and the paper edge, since the line's ink extent
starts at a ruled line left of the text; set by eye to x0=700, before any read). Writes crops_cap/c01-c06.jpg and cap_targets.tsv. Usage:
LINES_DIR=<scratch> python3 verify/upper_mu/cut_cap.py
"""
import os, re, random, subprocess, sys
sys.argv = sys.argv[:1]
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(os.path.dirname(D)); IM = os.path.join(T, 'images')
L = os.environ.get('LINES_DIR', '/tmp/fils_lines'); os.makedirs(L, exist_ok=True); os.makedirs(os.path.join(D, 'crops_cap'), exist_ok=True)
import importlib.util
spec = importlib.util.spec_from_file_location('cm', os.path.join(D, 'cut_mu.py'))
src = open(os.path.join(D, 'cut_mu.py')).read()
ink_extent = None
exec(src.split('out = [')[0])  # TOK, WIN, ink_extent, rows (no crops cut)
cand = []
for r, text, *_ in rows:
    if not r.startswith('U'):
        continue
    toks = TOK.findall(text)
    for i, t in enumerate(toks):
        near = toks[max(0, i - 2):i + 3]
        if re.fullmatch(r"[A-Za-zÀ-ÿ']{5,}", t) and not any('{' in x or '[...]' in x or '<del>' in x for x in near):
            cand.append((r, i, t))
OVERRIDE = {'c06': 700}
pick = sorted(random.Random(20261003).sample(cand, 6), key=lambda c: (c[0], c[1]))
out = ['crop\trow\ttok_idx\ttoken\tgrade\tx0\tline_w']
for n, (r, i, t) in enumerate(pick, 1):
    text = dict((x[0], x[1]) for x in rows)[r]
    a, b = f'{IM}/f43u_L{r[1:]}_s1.jpg', f'{IM}/f43u_L{r[1:]}_s2.jpg'
    line = os.path.join(L, f'{r}.png')
    subprocess.run(['convert', a, '(', b, '-crop', '1200x+1200+0', '+repage', ')', '+append', line], check=True)
    W, H = map(int, subprocess.run(['identify', '-format', '%w %h', line], capture_output=True, text=True).stdout.split())
    a0, a1 = ink_extent(line)
    toks = TOK.findall(text); disp = [re.sub(r'<del>|</del>|[{}]', '', x).split(' / ')[0] for x in toks]
    total = sum(len(d) + 1 for d in disp); off = sum(len(d) + 1 for d in disp[:i]); c = off + len(disp[i]) / 2
    x = int(a0 + c / total * (a1 - a0)); cid = f'c{n:02d}'; x0 = OVERRIDE.get(cid, max(0, min(W - WIN, x - WIN // 2)))
    subprocess.run(['convert', line, '-crop', f'{WIN}x{H}+{x0}+0', '+repage', os.path.join(D, 'crops_cap', f'{cid}.jpg')], check=True)
    out.append(f'{cid}\t{r}\t{i}\t{t}\tH\t{x0}\t{W}')
open(os.path.join(D, 'cap_targets.tsv'), 'w').write('\n'.join(out) + '\n')
print(len(cand), 'candidates;', ', '.join(f'{r}:{t}' for r, i, t in pick))
