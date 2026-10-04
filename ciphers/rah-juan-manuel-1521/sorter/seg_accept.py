#!/usr/bin/env python3
"""RUN1-SEG acceptance (pre-registered in PREREG_seg.md): tools/glyph_atlas.py segment --cursive on one page's line crops,
per-line box count vs the two blind passes' token counts (passes/<page>_A.tsv, _B.tsv), and median box height vs the
page x-height estimate (median of the per-strip xh the tool records in pages.json).

  python3 ciphers/rah-juan-manuel-1521/sorter/seg_accept.py --page f194 --crops DIR --out DIR2 [-- extra segment args]

The crops are tools/iiif_lines.py line crops of the DECODE full-size image (not committed; commands in NOTES.md).
"""
import argparse, csv, json, os, statistics as st, subprocess, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(T))
DUP = {'f194': {9, 11, 23, 26}, 'f199': set()}   # duplicate crop rows, as scripts/test1.py


def counts(fn):
    return {int(r['line']): len(r['tokens'].split()) for r in csv.DictReader(open(fn), delimiter='\t')}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--page', required=True); ap.add_argument('--crops', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('extra', nargs='*')
    a = ap.parse_args()
    A = counts(f'{T}/passes/{a.page}_A.tsv'); B = counts(f'{T}/passes/{a.page}_B.tsv')
    lines = [l for l in sorted(A) if l not in DUP[a.page] and os.path.exists(f'{a.crops}/{a.page}_L{l:02d}.jpg')]
    pages = []
    for l in lines:
        pages += ['--page', f'{a.page}L{l:02d}={a.crops}/{a.page}_L{l:02d}.jpg']
    subprocess.run([sys.executable, f'{ROOT}/tools/glyph_atlas.py', 'segment', '--cursive', *pages, '--out', a.out, *a.extra],
                   check=True, capture_output=True)
    rows = list(csv.DictReader(open(f'{a.out}/signs.tsv'), delimiter='\t'))
    P = json.load(open(f'{a.out}/pages.json'))
    c = Counter(r['page'] for r in rows)
    res, ok, n, oka, na = [], 0, 0, 0, 0
    for l in lines:
        k = f'{a.page}L{l:02d}'; ref = (A[l] + B.get(l, A[l])) / 2
        if ref == 0:
            continue
        good = abs(c[k] - ref) <= 0.25 * ref
        n += 1; ok += good
        if A[l] == B.get(l):
            na += 1; oka += good
        res.append(dict(line=l, pass_a=A[l], pass_b=B.get(l), boxes=c[k], xh=P[k]['median_h'], within25=int(good)))
    xh = st.median(P[k]['median_h'] for k in P if P[k]['median_h'])
    mh = st.median(float(r['h']) for r in rows)
    out = dict(page=a.page, lines=n, within25=ok, share=round(ok / n, 3), lines_a_eq_b=na, within25_a_eq_b=oka,
               boxes=len(rows), tokens_ref=sum((A[l] + B.get(l, A[l])) / 2 for l in lines),
               median_box_h=mh, page_xh=xh, ratio=round(mh / xh, 3),
               verdict='PASS' if ok / n >= 0.70 and mh >= 0.6 * xh else 'FAIL', per_line=res, extra=a.extra)
    print(json.dumps({k: v for k, v in out.items() if k != 'per_line'}))
    for r in res:
        print('\t'.join(str(r[k]) for k in r))
    json.dump(out, open(f'{a.out}/accept_{a.page}.json', 'w'), indent=1)


if __name__ == '__main__':
    main()
