#!/usr/bin/env python3
"""Build the Entick 1781 page/column/line grid for the Cossit/Summer code (SHERWOOD-READ, 18 Oct 2026).

Convention (gate passed on 8 anchors, NOTES.md "## Reading from Entick 1781"): a pair P-W names printed page P
and the W-th printed line of a column, counted from the top of that column (a wrapped continuation line counts as
a line). The column itself is not written in the pair, so every pair has two candidates, col 1 and col 2.

For each printed page this script finds the column rule in the scan (archive.org 11280377bsb_jp2.zip), finds the
text lines of each column from the row ink profile on a fitted regular grid, and attaches the djvu.xml OCR text
whose words fall in that line's band. Output: book/entick_lines.tsv (page, col, line, y, ocr), a few MB.

  python3 book/build_entick_lines.py --src DIR [--pages 364,138] [--debug]
DIR holds 11280377bsb_jp2/ (unzipped), 11280377bsb_djvu.xml and 11280377bsb_page_numbers.json, re-downloadable from
https://archive.org/download/11280377bsb/ (three requests). Needs numpy and Pillow.
"""
import argparse, json, os, statistics, sys
import xml.etree.ElementTree as ET
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
# top_fix.tsv: page<TAB>col<TAB>shift. shift +1 drops a grid row the scan read above line 1 (the running head);
# shift -1 adds a line 1 the ink profile missed. Each row was settled by eye on the page image (NOTES.md).
FIX = {}
if os.path.exists(os.path.join(HERE, 'top_fix.tsv')):
    for ln in open(os.path.join(HERE, 'top_fix.tsv')):
        if ln.strip() and not ln.startswith('#'):
            p_, c_, s_ = ln.split()[:3]
            FIX[(p_, int(c_))] = int(s_)


def load_ocr(src):
    pn = json.load(open(os.path.join(src, '11280377bsb_page_numbers.json')))['pages']
    leaf2page = {p['leafNum']: p['pageNumber'] for p in pn}
    pages, leaf = {}, -1
    for _, el in ET.iterparse(os.path.join(src, '11280377bsb_djvu.xml'), events=('end',)):
        if el.tag == 'OBJECT':
            leaf += 1
            words = []
            for w in el.iter('WORD'):
                c = [int(x) for x in w.get('coords').split(',')]
                words.append((c[0], c[3], c[2], c[1], (w.text or '').strip()))  # x0, top, x1, bottom, text
            if leaf2page.get(leaf):
                pages[leaf2page[leaf]] = (leaf, words)
            el.clear()
    return pages


def grid(profile, y0, y1):
    """Fit a regular line grid (pitch, phase) to a column's row-ink profile between y0 and y1."""
    seg = profile[y0:y1] - profile[y0:y1].mean()
    best = None
    for pitch in np.arange(28.0, 40.0, 0.1):
        ac = 0
        for phase in np.arange(0, pitch, 0.5):
            pos = np.arange(phase, len(seg), pitch).astype(int)
            s = seg[pos].sum()
            if best is None or s > best[0]:
                best = (s, pitch, phase)
    _, pitch, phase = best
    return pitch, y0 + phase


def page_lines(img, words, page_no=None):
    a = np.asarray(img.convert('L'), dtype=float)
    H, W = a.shape
    ink = a < 150
    # column rule: the darkest long vertical stripe in the middle of the page
    mid = ink[int(H * 0.1):int(H * 0.9), int(W * 0.35):int(W * 0.65)].sum(axis=0)
    rule = int(W * 0.35) + int(np.argmax(mid))
    out = []
    for col, (x0, x1) in enumerate(((int(W * 0.03), rule - 4), (rule + 4, int(W * 0.99)))):
        prof = ink[:, x0:x1].sum(axis=1).astype(float)
        prof = np.convolve(prof, np.ones(5) / 5, mode='same')
        # body: from below the running head to the bottom of the column rule
        rows = np.where(ink[:, max(rule - 3, 0):rule + 4].any(axis=1))[0]
        bot = int(rows.max()) if len(rows) else int(H * 0.95)
        rows_t = rows[rows > H * 0.03]
        top = int(rows_t.min()) if len(rows_t) else int(H * 0.06)
        pitch, first = grid(prof, top, bot)
        # first body line: the first grid row at or below the top of the rule with ink
        thr = 0.25 * np.percentile(prof[top:bot], 90)
        ys = []
        y = first
        while y < bot + pitch * 0.5:
            yi = int(round(y))
            if yi < H and prof[max(yi - 6, 0):yi + 7].max() > thr:
                ys.append(yi)
            elif ys:
                ys.append(yi)  # a blank grid row inside the column still counts as a line
            y += pitch
        # trim trailing blank rows
        while ys and prof[max(ys[-1] - 6, 0):ys[-1] + 7].max() <= thr:
            ys.pop()
        ys = ys[FIX.get((page_no, col + 1), 0):] if FIX.get((page_no, col + 1), 0) >= 0 else \
            [ys[0] - pitch * k for k in range(-FIX[(page_no, col + 1)], 0, -1)] + ys
        ys = [int(round(y)) for y in ys]
        for n, yc in enumerate(ys, 1):
            ws = [w for w in words if x0 - 10 <= w[0] < x1 and abs((w[1] + w[3]) / 2 - yc) < pitch / 2]
            ws.sort()
            out.append((col + 1, n, yc, ' '.join(w[4] for w in ws)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', required=True)
    ap.add_argument('--pages')
    ap.add_argument('--out', default=os.path.join(HERE, 'entick_lines.tsv'))
    args = ap.parse_args()
    ocr = load_ocr(args.src)
    want = args.pages.split(',') if args.pages else sorted((p for p in ocr if p.isdigit()), key=int)
    rows = []
    for p in want:
        leaf, words = ocr[p]
        img = Image.open(os.path.join(args.src, '11280377bsb_jp2', '11280377bsb_%04d.jp2' % leaf))
        try:
            lines = page_lines(img, words, p)
        except ValueError as e:
            print('page', p, 'skipped:', e, file=sys.stderr)
            continue
        for col, n, y, txt in lines:
            rows.append((p, col, n, y, leaf, txt.replace('\t', ' ')))
    with open(args.out, 'w', encoding='utf-8') as f:
        f.write('page\tcol\tline\ty\tleaf\tocr\n')
        for r in rows:
            f.write('\t'.join(map(str, r)) + '\n')
    print(len(rows), 'lines,', len(want), 'pages ->', args.out, file=sys.stderr)


if __name__ == '__main__':
    main()
