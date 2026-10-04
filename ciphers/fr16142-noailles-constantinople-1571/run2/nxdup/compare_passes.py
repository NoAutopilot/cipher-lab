#!/usr/bin/env python3
"""RUN2-NXDUP: character-level two-reader disagreement per page for the Dupuy 521 221R-226R diplomatic passes.

usage: compare_passes.py PASSA_DIR PASSB_DIR [--out err_2reader.tsv]
Each dir holds d<canvas><L|R>.tsv rows "crop_id<TAB>text". Per page: both passes' rows joined with one space,
whitespace collapsed; err_2reader = Levenshtein(A, B) / mean(len A, len B). Also reported with [?]/CATCH:/HEAD:
markers stripped and lower-cased ("err_loose"), so marker placement and case do not count as disagreement.
"""
import sys, os, re, glob, argparse

def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]

def page(path):
    rows = [l.rstrip('\n').split('\t', 1) for l in open(path, encoding='utf-8') if l.strip()]
    return ' '.join(re.sub(r'\s+', ' ', r[1]).strip() for r in rows if len(r) == 2), len(rows)

def loose(s):
    s = re.sub(r'\[\?\]|CATCH:|HEAD:|\(blank\)|—', '', s).lower()
    return re.sub(r'\s+', ' ', s).strip()

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('a'); ap.add_argument('b'); ap.add_argument('--out')
    a = ap.parse_args()
    out = ['page\trows_A\trows_B\tchars_A\tchars_B\tlev\terr_2reader\tlev_loose\terr_loose']
    T = [0, 0, 0, 0]
    for pa in sorted(glob.glob(os.path.join(a.a, 'd*.tsv'))):
        pb = os.path.join(a.b, os.path.basename(pa))
        if not os.path.exists(pb):
            continue
        (ta, na), (tb, nb) = page(pa), page(pb)
        d = lev(ta, tb); m = (len(ta) + len(tb)) / 2
        la, lb = loose(ta), loose(tb); dl = lev(la, lb); ml = (len(la) + len(lb)) / 2
        T[0] += d; T[1] += m; T[2] += dl; T[3] += ml
        out.append(f'{os.path.basename(pa)[1:-4]}\t{na}\t{nb}\t{len(ta)}\t{len(tb)}\t{d}\t{d/m:.3f}\t{dl}\t{dl/ml:.3f}')
    out.append(f'ALL\t\t\t\t\t{T[0]}\t{T[0]/T[1]:.3f}\t{T[2]}\t{T[2]/T[3]:.3f}')
    txt = '\n'.join(out) + '\n'
    if a.out:
        open(a.out, 'w').write(txt)
    print(txt, end='')

if __name__ == '__main__':
    main()
