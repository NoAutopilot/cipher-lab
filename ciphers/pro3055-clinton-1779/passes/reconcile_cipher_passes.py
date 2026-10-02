#!/usr/bin/env python3
"""Align blind passes A and B of the 2894 cipher (cipher_passA.tsv, cipher_passB.tsv) crop by crop and write
cipher_disagreements.tsv (what the reconciler must settle on the image) and cipher_draft.tsv (rows the passes agree
on, plus the disputed rows marked DISPUTE with both readings). GAPS2-pro3055-clinton-1779, 2 Oct 2026.
tools/reconcile_passes.py is line-crop shaped (one text per line crop); these passes are one row per cipher entry,
so the per-crop alignment is a small edit-distance over entry tuples here.
"""
import os, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)
sys.path.insert(0, ROOT)
from check_2894_key import read_tsv

def key(r):
    return (r['first'].strip(), r['second'].strip(), r['clear'].strip().lower())

def align(a, b):
    n, m = len(a), len(b); INF = 10 ** 9
    D = [[INF] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if D[i][j] == INF: continue
            if i < n and D[i][j] + 1 < D[i + 1][j]: D[i + 1][j], B[i + 1][j] = D[i][j] + 1, (i, j)
            if j < m and D[i][j] + 1 < D[i][j + 1]: D[i][j + 1], B[i][j + 1] = D[i][j] + 1, (i, j)
            if i < n and j < m:
                ka, kb = key(a[i]), key(b[j])
                c = 0 if ka == kb else (0.5 if (ka[1] == kb[1] and ka[2] == kb[2]) or (ka[0] == kb[0] and ka[2] == kb[2] and ka[1] and kb[1]) else 0.9)
                if D[i][j] + c < D[i + 1][j + 1]: D[i + 1][j + 1], B[i + 1][j + 1] = D[i][j] + c, (i, j)
    i, j, out = n, m, []
    while (i, j) != (0, 0):
        pi, pj = B[i][j]
        out.append((a[pi] if pi == i - 1 else None, b[pj] if pj == j - 1 else None) if (pi == i - 1 and pj == j - 1) else
                   ((a[pi], None) if pi == i - 1 else (None, b[pj])))
        i, j = pi, pj
    return out[::-1]

def main():
    A, B = read_tsv(P('cipher_passA.tsv')), read_tsv(P('cipher_passB.tsv'))
    crops = []
    for r in A + B:
        if r['crop'] not in crops: crops.append(r['crop'])
    draft = ['crop\trow\tfirst\tsecond\tclear\trule_below\tconf\tnote\tstatus\tA\tB']
    dis = ['crop\trowA\trowB\tA_first\tA_second\tA_clear\tB_first\tB_second\tB_clear\tA_note\tB_note']
    n_rows = n_agree = n_dis = 0
    for c in crops:
        a = [r for r in A if r['crop'] == c]; b = [r for r in B if r['crop'] == c]
        for ra, rb in align(a, b):
            n_rows += 1
            if ra and rb and key(ra) == key(rb):
                n_agree += 1
                rule = ra['rule_below'] if ra['rule_below'] == rb['rule_below'] else ra['rule_below'] + '|' + rb['rule_below']
                conf = 'H' if ra['conf'] == rb['conf'] == 'H' else 'M'
                draft.append('\t'.join([c, ra['row'], ra['first'], ra['second'], ra['clear'], rule, conf,
                                        (ra['note'] + ' | ' + rb['note']).strip(' |'), 'agree', '', '']))
            else:
                n_dis += 1
                fa = lambda r, k: r[k] if r else ''
                sa = f"{fa(ra,'first')}-{fa(ra,'second')} {fa(ra,'clear')}".strip() if ra else '(none)'
                sb = f"{fa(rb,'first')}-{fa(rb,'second')} {fa(rb,'clear')}".strip() if rb else '(none)'
                draft.append('\t'.join([c, fa(ra, 'row') or fa(rb, 'row'), '', '', '', fa(ra, 'rule_below') or fa(rb, 'rule_below'),
                                        'L', '', 'DISPUTE', sa, sb]))
                dis.append('\t'.join([c, fa(ra, 'row'), fa(rb, 'row'), fa(ra, 'first'), fa(ra, 'second'), fa(ra, 'clear'),
                                      fa(rb, 'first'), fa(rb, 'second'), fa(rb, 'clear'), fa(ra, 'note'), fa(rb, 'note')]))
    open(P('cipher_draft.tsv'), 'w').write('\n'.join(draft) + '\n')
    open(P('cipher_disagreements.tsv'), 'w').write('\n'.join(dis) + '\n')
    print(f'rows {n_rows} agree {n_agree} dispute {n_dis} agreement {n_agree / n_rows:.3f}; A rows {len(A)}, B rows {len(B)}')

if __name__ == '__main__':
    main()
