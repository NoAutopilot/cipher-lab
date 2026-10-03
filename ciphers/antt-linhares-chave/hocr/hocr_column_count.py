#!/usr/bin/env python3
"""Count flush-left (headword) lines per column in an Internet Archive hOCR file.

A1B-LIN-HOCR, 3 Oct 2026, ciphers/antt-linhares-chave. Second instrument for the two
disputed column counts (p83 col2 rank 19 "cagar", p241 col3 rank 15 "justa") in
Vieyra's New Pocket Dictionary (London 1809, IA newpocketdiction00viey).

Method (pre-registered in NOTES.md, section "hOCR column counter (A1B-LIN-HOCR)"):
  * pages are hOCR ocr_page divs; ppageno == IA leaf number;
  * every ocrx_word is assigned to one of three columns by its centre x, the column
    borders being the two widest gaps in the page's word-centre histogram between
    20% and 80% of the text width (fallback: thirds of the text extent);
  * a line = the words of one ocr_line falling in one column (so a line OCR merged
    across a column rule is split); its x0 is its first word's x0;
  * lines whose bottom lies above 5% of the page height (running head) are dropped,
    as are lines with fewer than 2 alphabetic characters;
  * a column's margin is the 10th percentile of its line x0s; a line is flush-left
    (a headword) iff x0 <= margin + TOL (TOL = 20 px at the scan's 400 dpi).
Usage: hocr_column_count.py HOCR --leaf N --col C [--tol 20] [--show]
       hocr_column_count.py HOCR --calibrate calibration.tsv [--tol 20]
"""
import argparse, html, re, sys, unicodedata
from difflib import SequenceMatcher

BB = re.compile(r'bbox (\d+) (\d+) (\d+) (\d+)')

def load_pages(path, leaves):
    h = open(path, encoding='utf-8').read()
    out = {}
    for leaf in leaves:
        i = h.find('id="page_%06d"' % leaf)
        if i < 0:
            continue
        j = h.find('class="ocr_page"', i + 10)
        out[leaf] = h[i:j if j > 0 else len(h)]
    return out

def parse(page):
    W, H = map(int, BB.search(page).groups()[2:])
    lines = []
    for lm in re.finditer(r'<span class="ocr_line"[^>]*>(.*?)</span>\s*(?=<span class="ocr_line"|</p>)', page, re.S):
        words = []
        for wm in re.finditer(r'<span class="ocrx_word"[^>]*title="bbox (\d+) (\d+) (\d+) (\d+)[^"]*"[^>]*>(.*?)</span>', lm.group(1), re.S):
            x0, y0, x1, y1 = map(int, wm.groups()[:4])
            t = html.unescape(re.sub('<[^>]+>', '', wm.group(5))).strip()
            if t:
                words.append((x0, y0, x1, y1, t))
        if words:
            lines.append(words)
    return W, H, lines

def borders(lines, W):
    cs = sorted((w[0] + w[2]) / 2 for l in lines for w in l)
    if len(cs) < 30:
        return None
    lo, hi = cs[0], cs[-1]
    span = hi - lo
    # word-coverage profile: mark x covered by any word box
    cover = [0] * (W + 2)
    for l in lines:
        for w in l:
            for x in range(max(0, w[0]), min(W, w[2])):
                cover[x] += 1
    gaps = []
    x = int(lo + 0.2 * span)
    end = int(lo + 0.8 * span)
    while x < end:
        if cover[x] <= 1:
            s = x
            while x < end and cover[x] <= 1:
                x += 1
            gaps.append((x - s, (s + x) / 2))
        x += 1
    gaps.sort(reverse=True)
    if len(gaps) >= 2 and gaps[1][0] >= 8:
        return sorted([gaps[0][1], gaps[1][1]])
    return [lo + span / 3, lo + 2 * span / 3]

def columns(page, tol=20):
    W, H, lines = parse(page)
    b = borders(lines, W)
    cols = {1: [], 2: [], 3: []}
    for l in lines:
        frag = {1: [], 2: [], 3: []}
        for w in l:
            c = (w[0] + w[2]) / 2
            frag[1 if c < b[0] else 2 if c < b[1] else 3].append(w)
        for k, ws in frag.items():
            if not ws:
                continue
            ws.sort()
            y1 = max(w[3] for w in ws)
            text = ' '.join(w[4] for w in ws)
            if y1 < 0.05 * H or sum(ch.isalpha() for ch in text) < 2:
                continue
            cols[k].append((min(w[1] for w in ws), ws[0][0], text))
    out = {}
    for k, ls in cols.items():
        ls.sort()
        if not ls:
            out[k] = []
            continue
        xs = sorted(l[1] for l in ls)
        margin = xs[int(0.1 * (len(xs) - 1))]
        out[k] = [(l[2], l[1] <= margin + tol, l[1] - margin) for l in ls]
    return out, b

def norm(s):
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(ch for ch in s if not unicodedata.combining(ch)).lower().replace('ſ', 's')
    return re.sub('[^a-z]', '', s)

def heads(col):
    return [t for t, flush, _ in col if flush]

def locate(hw, hl, r=None):
    """rank (1-based) of the flush-left line whose first token best matches hw, ratio."""
    best = (0, None)
    for i, t in enumerate(hl):
        tok = norm(t.split()[0]) if t.split() else ''
        for cand in (tok, tok.replace('f', 's')):
            q = SequenceMatcher(None, norm(hw), cand).ratio()
            if q > best[0] or (q == best[0] and r is not None and best[1] is not None and abs(i + 1 - r) < abs(best[1] - r)):
                best = (q, i + 1)
    return best

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('hocr')
    ap.add_argument('--leaf', type=int)
    ap.add_argument('--col', type=int)
    ap.add_argument('--tol', type=int, default=20)
    ap.add_argument('--show', action='store_true')
    ap.add_argument('--calibrate')
    a = ap.parse_args()
    if a.calibrate:
        rows = [l.rstrip('\n').split('\t') for l in open(a.calibrate)][1:]
        pages = load_pages(a.hocr, {int(r[3]) for r in rows})
        hit = miss = unloc = 0
        print('src\tgroup\tleaf\tcol\trank\theadword\tcounter_rank\tratio\tline_at_rank\tverdict')
        for src, g, p, leaf, c, r, hw in rows:
            cols, _ = columns(pages[int(leaf)], a.tol)
            hl = heads(cols[int(c)])
            q, k = locate(hw, hl, int(r))
            at = hl[int(r) - 1][:40] if int(r) <= len(hl) else '-'
            if q < 0.5:
                v = 'unlocated'; unloc += 1
            elif k == int(r):
                v = 'hit'; hit += 1
            else:
                v = 'MISS'; miss += 1
            print(f'{src}\t{g}\t{leaf}\t{c}\t{r}\t{hw}\t{k}\t{q:.2f}\t{at}\t{v}')
        n = hit + miss + unloc
        ok = miss == 0 and unloc <= 3
        print(f'# tol {a.tol}: hit {hit}, MISS {miss}, unlocated {unloc} of {n} -> {"PASS" if ok else "FAIL"}')
        sys.exit(0 if ok else 1)
    cols, b = columns(load_pages(a.hocr, [a.leaf])[a.leaf], a.tol)
    n = 0
    for t, flush, dx in cols[a.col]:
        if flush:
            n += 1
        if a.show or flush:
            print(f'{n if flush else "":>3}\t{dx:+d}\t{t[:70]}')
    print(f'# leaf {a.leaf} col {a.col}: {n} flush-left lines (tol {a.tol}, borders {b})')

if __name__ == '__main__':
    main()
