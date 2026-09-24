#!/usr/bin/env python3
"""Relabel passA.tsv / passB.tsv cipher rows onto physical cipher lines (reconciler's segmentation, 24 Sept 2026).

The two blind passes segmented the page differently (NOTES section 3). This maps each pass's rows onto the
physical cipher lines read from the image (f226r_C1-C2, f226v_C01-C14, f227r_C01-C14) so that
tools/reconcile_passes.py can align like with like. Writes passA_lines.tsv and passB_lines.tsv.
"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
# (pass line, slice of that line's cipher tokens) -> physical line
MAP = {
 'A': [('f226r_L10', 0, 5, 'f226r_C1'), ('f226r_L10', 5, None, 'f226r_C2')] +
      [(f'f226v_L{a}', 0, None, f'f226v_C{c:02d}') for a, c in
       [(4,1),(5,2),(8,3),(9,4),(10,5),(11,6),(12,7),(14,8),(15,9),(16,10),(17,11),(18,12),(19,13),(20,14)]] +
      [(f'f227r_L{a}', s, None, f'f227r_C{c:02d}') for a, s, c in
       [(5,0,1),(7,0,2),(8,0,3),(9,0,4),(10,0,5),(11,0,6),(12,0,7),(13,0,8),(14,0,9),(15,0,10),(16,0,11),(17,0,12),
        (19,1,13),(20,0,14)]],   # A's f227r_L19 token 0 is the clear word 'fait'
 'B': [('f226r_L10', 0, 5, 'f226r_C1'), ('f226r_L10', 5, None, 'f226r_C2'),
       ('f226v_L5', 0, 13, 'f226v_C01'), ('f226v_L5', 13, None, 'f226v_C02')] +
      [(f'f226v_L{a}', 0, None, f'f226v_C{c:02d}') for a, c in
       [(8,3),(9,4),(10,5),(11,6),(12,7),(14,8),(15,9),(16,10),(17,11),(18,12),(19,13),(20,14)]] +
      [(f'f227r_L{a}', s, e, f'f227r_C{c:02d}') for a, s, e, c in
       [(6,0,None,1),(7,0,None,2),(8,0,None,3),(9,0,None,4),(10,0,None,5),(11,0,None,6),(12,0,None,7),(13,0,None,8),
        (15,0,None,9),(16,0,None,10),(17,0,12,11),(17,12,None,12),(19,0,None,13),(20,0,None,14)]],
}
# B's f226v_L7 'Z' is the final letter of the clear word 'tempZ' (tempz), not a cipher sign: dropped.
DROP = {('B', 'f226v_L7')}

def main():
    for p in 'AB':
        rows = [r for r in csv.DictReader(open(os.path.join(HERE, f'pass{p}.tsv')), delimiter='\t')
                if r['position'] != 'clear']
        by = {}
        for r in rows:
            by.setdefault(r['line'], []).append(r)
        used = set()
        out = [['line', 'position', 'group', 'confidence']]
        for src, s, e, dst in MAP[p]:
            toks = by.get(src, [])[s:e]
            for i, r in enumerate(toks, 1):
                out.append([dst, str(i), r['group'], r['confidence']])
            used.add(src)
        left = [k for k in by if k not in used and (p, k) not in DROP]
        assert not left, (p, left)
        with open(os.path.join(HERE, f'pass{p}_lines.tsv'), 'w') as f:
            f.writelines('\t'.join(x) + '\n' for x in out)
        print(p, len(out) - 1, 'tokens')

if __name__ == '__main__':
    main()
