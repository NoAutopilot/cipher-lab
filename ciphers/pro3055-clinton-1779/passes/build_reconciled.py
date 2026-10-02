#!/usr/bin/env python3
"""Build cipher_reconciled.tsv from cipher_draft.tsv (reconcile_cipher_passes.py) and the reconciler's decisions on
the 26 disputed rows (GAPS2-pro3055-clinton-1779, 2 Oct 2026). 25 of the 26 disputes are the same clear words split
differently across written lines (pass A joined them, pass B kept one row per line); one is a figure (p184_c6a row 12,
A '-5' vs B '-15'). Decisions marked 'own read' were settled on the crop by the reconciler (crops p184_c6a, p185_c4a,
p184_c3a viewed); the rest take the joined form both passes contain. Rows a decision maps to None are dropped (the
fragment rows of a joined word). The reconciled file keeps every agreed row verbatim.
"""
import os, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from check_2894_key import read_tsv

# (crop, row) -> (first, second, clear, conf, note) or None to drop
DECISIONS = {
    ('p184_c1a.jpg', '10'): ('', '', 'of Novr', 'H', 'A of Nov. / B of Novr; clear opening words of the letter, not a margin gloss'),
    ('p184_c1a.jpg', '12'): ('', '', '1 Jany', 'M', 'both passes read the first stroke as 1; f.186 reads & January'),
    ('p184_c3a.jpg', '7'): ('', '', 'is supposed to', 'M', 'own read on the crop: is sup-/posed to; both passes read is imp-/possible'),
    ('p184_c4b.jpg', '10'): ('', '', '& from 20 to 25', 'H', 'two written lines joined (A)'),
    ('p184_c6a.jpg', '12'): ('', '5', '', 'H', 'own read on the crop: -5 (A); B -15'),
    ('p184_c6b.jpg', '1'): ('', '', '& that', 'H', 'own read on the crop: & that (B); A of that'),
    ('p184_c7b.jpg', '13'): ('', '', 'will be', 'H', 'two written lines joined (A)'),
    ('p184_c8b.jpg', '7'): ('', '', 'By Information', 'M', 'three written lines joined (A); B read -forma-/lation'),
    ('p184_c8b.jpg', '8'): ('', '', 'I have received here', 'H', 'three written lines joined (A)'),
    ('p185_c1b.jpg', '1'): ('', '', 'assemble', 'H', 'assem-/ble across the tick, written once'),
    ('p185_c2a.jpg', '3'): ('', '', 'a Division of which will', 'H', 'four written lines joined (A)'),
    ('p185_c4a.jpg', '6'): ('', '', '& No 4', 'M', 'own read on the crop: & No 4; A one 4, B & the 4; f.186 reads and No 4'),
    ('p185_c5a.jpg', '6'): ('', '', 'the other', 'M', 'two written lines joined (A); B the / other with "looks like & thes or others"'),
    ('p185_c6b.jpg', '1'): None,
    ('p185_c1a.jpg', '17'): None, ('p185_c2a.jpg', '4'): None, ('p185_c2a.jpg', '5'): None, ('p184_c8b.jpg', '9'): None,
    ('p184_c8b.jpg', '10'): None, ('p184_c8b.jpg', '11'): None, ('p184_c8b.jpg', '12'): None, ('p185_c5a.jpg', '7'): None,
    ('p184_c3a.jpg', '8'): None, ('p184_c4b.jpg', '11'): None, ('p184_c7b.jpg', '14'): None,
}

def main():
    rows = read_tsv(os.path.join(ROOT, 'cipher_draft.tsv'))
    out = ['crop\trow\tfirst\tsecond\tclear\trule_below\tconf\tnote']
    used = set(); n_drop = 0
    for r in rows:
        k = (r['crop'], r['row'])
        if r['status'] == 'agree':
            rule = r['rule_below'].split('|')[0] if '|' in r['rule_below'] else r['rule_below']
            out.append('\t'.join([r['crop'], r['row'], r['first'], r['second'], r['clear'], rule, r['conf'], r['note']]))
            continue
        if k not in DECISIONS or k in used:
            # a fragment row of a joined word carries the row number of its surviving neighbour: drop
            n_drop += 1; continue
        used.add(k)
        d = DECISIONS[k]
        if d is None:
            n_drop += 1; continue
        out.append('\t'.join([r['crop'], r['row'], d[0], d[1], d[2], r['rule_below'], d[3], d[4]]))
    open(os.path.join(ROOT, 'cipher_reconciled.tsv'), 'w').write('\n'.join(out) + '\n')
    print(f'reconciled rows {len(out) - 1}; disputes decided {len(used)}, dropped fragments {n_drop}; decisions unused: {sorted(set(DECISIONS) - used)}')

if __name__ == '__main__':
    main()
