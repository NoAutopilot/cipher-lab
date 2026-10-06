#!/usr/bin/env python3
"""R12A-BALS (6 Oct 2026): inputs for the owner sign sorter of the Baluze 170 f.228r-v hand (Chavigny to d'Avaux, Amiens 25 Aug
1640), one tile per sign, via tools/sorter_recut.py. No network: reads the five Gallica native regions already in images/crops/
(D1-BAL170, D1-BAL170B). Each of the 13 cipher lines is copied as its own block (one pitch either side of its centre) into one grey
array; the x-ranges outside the cipher (clear words, the period, end-of-line dashes, margins) are blanked to the line's median paper tone, as eye-checked by
R12A-BALS on 400 px boundary panels (CIPHER below). Reader columns = passes/reconciled_b170f228{r,v}.tsv cipher tokens, split one
column per written glyph: a numeral is one column per digit, its mark (' acute, : diaeresis, = bar) on the last digit; "?" dropped
from the pile name (uncertainty goes to the focus box instead). Columns are spread evenly over each cipher span's own ink.
  python3 ciphers/baluze167-davaux-1637/sorter170/build_inputs.py [--debug DIR]
"""
import argparse, csv, re, sys
from pathlib import Path
import numpy as np
from PIL import Image
S = Path(__file__).resolve().parent; T = S.parent; R = S.parents[2]
sys.path.insert(0, str(R / 'tools')); sys.path.insert(0, str(T / 'r12bals'))
import sorter_recut as sr  # noqa: E402
from lines import geometry, LINES  # noqa: E402
PITCH = 170
# cipher x-spans per line, region pixels (everything else on the line is blanked)
CIPHER = {
    'b170f228r_a_L02': [(880, 2262)], 'b170f228r_c_L01': [(880, 1180)], 'b170f228r_b_L01': [(2560, 3200)],
    'b170f228r_b_L02': [(1012, 1905), (2095, 3230)],
    'b170f228v_a_L01': [(180, 2385)], 'b170f228v_a_L02': [(180, 715)], 'b170f228v_b_L01': [(1210, 2480)],
    'b170f228v_b_L02': [(200, 2440)], 'b170f228v_b_L03': [(200, 1350), (1765, 2480)], 'b170f228v_b_L04': [(200, 2480)],
    'b170f228v_b_L05': [(200, 712), (900, 1795)], 'b170f228v_b_L06': [(590, 1380), (1855, 2045)], 'b170f228v_b_L07': [(200, 1362)],
}


def glyph_cols(tok):
    """'73'' -> [('7','7'), ("3'", '3')]; 's:u4?' -> [('u4','u4')]; family = the bare sign (digit or letter sign)."""
    tok = tok.rstrip('?')
    if tok.startswith('s:'):
        s = tok[2:]
        if s.startswith('?('): s = 'ff' if 'ff' in s else s
        s = s.split('|')[0].rstrip('?') or 'unread'
        return [(s, s)]
    m = re.match(r'^(\d+)([\'=:]?)\??$', tok)
    if not m: return [(tok, tok)]
    d, mk = m.groups(); out = [(c, c) for c in d]
    out[-1] = (d[-1] + mk, d[-1]); return out


def spans_tokens(row):
    """Split a reconciled row into its cipher runs (between {clear} groups)."""
    runs, cur = [], []
    for part in re.split(r'(\{[^}]*\})', row):
        if part.startswith('{'):
            if cur: runs.append(cur); cur = []
        else: cur += part.split()
    if cur: runs.append(cur)
    return runs


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--debug'); a = ap.parse_args()
    rec = {}
    for f in ('passes/reconciled_b170f228r.tsv', 'passes/reconciled_b170f228v.tsv'):
        for ln in open(T / f):
            if ln.startswith('#') or ln.startswith('line\t'): continue
            k, v = ln.rstrip('\n').split('\t', 1); rec[k] = v
    g = geometry(); W = 3500; blk = 2 * PITCH + 1
    grey = np.full((blk * len(LINES), W), 255, np.uint8); traces, cols, centres, uncertain = [], [], [], []
    for i, ln in enumerate(LINES):
        v = g[ln]; im = np.array(Image.open(T / 'images/crops' / v['src']).convert('L'))
        y0 = v['yc'] - PITCH; a0 = max(0, y0); a1 = min(im.shape[0], v['yc'] + PITCH + 1)
        block = np.full((blk, W), 255, np.uint8); block[a0 - y0:a1 - y0, :im.shape[1]] = im[a0:a1]
        keep = np.zeros(W, bool)
        for x0, x1 in CIPHER[ln]: keep[x0:x1] = True
        block[:, ~keep] = int(np.median(block[:, keep]))   # paper tone, not white: a white fill skews the page's Otsu level
        grey[i * blk:(i + 1) * blk] = block
        traces.append(np.full(W, i * blk + PITCH, float))
        runs = spans_tokens(rec[ln])
        assert len(runs) == len(CIPHER[ln]), (ln, len(runs), CIPHER[ln])
        lc, lx = [], []
        for run, (x0, x1) in zip(runs, CIPHER[ln]):
            ink = (block[PITCH - 50:PITCH + 50, x0:x1] < 150).any(0); xs = np.nonzero(ink)[0]
            e0, e1 = (x0 + xs.min(), x0 + xs.max()) if len(xs) else (x0, x1)
            gl = []
            for t in run:
                for c in glyph_cols(t): gl.append((c, t.endswith('?') or '?' in t))
            n = len(gl)
            for j, ((pile, fam), unc) in enumerate(gl):
                lc.append((pile, fam)); lx.append(e0 + (j + 0.5) * (e1 - e0) / n)
                if unc: uncertain.append((ln, len(lc), pile))
        cols.append(lc); centres.append(lx)
    cfg = sr.Cfg(pitch=PITCH, half=110, xmin=150, xmax=3300, nclu=24, skip=60, clear=45)
    tiles, stats = sr.run(grey, traces, LINES, cols, centres, S, S / 'pages', cfg, debug=a.debug)
    with open(S / 'cipher_lines.tsv', 'w') as o:
        o.write('# R12A-BALS: the 13 cipher lines of Baluze 170 f.228r-v, with the cipher x-range (clear words, period, dashes blanked inside it)\n')
        o.writelines(f"{ln}\t{min(a for a, b in CIPHER[ln])}\t{max(b for a, b in CIPHER[ln])}\n" for ln in LINES)
    with open(S / 'uncertain_cols.tsv', 'w') as o:
        o.write('line\tcol\tpile\n'); o.writelines(f'{l}\t{c}\t{p}\n' for l, c, p in uncertain)
    for s in stats: print(*s, sep='\t')


if __name__ == '__main__':
    main()
