#!/usr/bin/env python3
"""R9-WVOALIGN: from align_piles.tsv / key_piles.tsv (tools/interlinear_align.py, PREREG parameters) write
  tile_letters.tsv  one row per sorter tile: the gloss letter aligned over it (the owner's later sort relabels by sid);
  key.tsv           pile id -> letter: grade C when the letter is the pile's top chunk >= 2 times on >= 2 rows and
                    >= 0.6 of its aligned occurrences (the PREREG statistic), M otherwise (piles are provisional k-means
                    shape groups, several mix two shapes; see NOTES.md);
  ciphertext.tsv    the tile stream (pile ids, x order) in tools/decode_key.py 'tsv' format.
Run from the repo root."""
import csv, os
from collections import Counter, defaultdict
D = os.path.dirname(os.path.abspath(__file__))
order = {(r['row'], int(r['idx'])): r for r in csv.DictReader(open(os.path.join(D, 'tile_order.tsv')), delimiter='\t')}
al = list(csv.DictReader(open(os.path.join(D, 'align_piles.tsv')), delimiter='\t'))
per, rows = defaultdict(Counter), defaultdict(lambda: defaultdict(set))
with open(os.path.join(D, 'tile_letters.tsv'), 'w') as f, open(os.path.join(D, 'ciphertext.tsv'), 'w') as g:
    f.write('sid\trow\tidx\tpile\tgloss_letter\tstatus\n')
    g.write('line\tpos\tsign\tconf\n')
    for a in al:
        t = order[(a['cipher_line'], int(a['idx']))]
        f.write('%s\t%s\t%s\t%s\t%s\t%s\n' % (t['sid'], a['cipher_line'], a['idx'], t['pile'], a['plain_chunk'], a['status']))
        sign = '[PLAIN:%s]' % a['raw'] if a['kind'] == 'clear' else t['pile']
        g.write('%s\t%d\t%s\t\n' % (a['cipher_line'], int(a['idx']) + 1, sign))
        if a['kind'] == 'code' and a['plain_chunk']:
            per[t['pile']][a['plain_chunk']] += 1
            rows[t['pile']][a['plain_chunk']].add(a['cipher_line'])
with open(os.path.join(D, 'key.tsv'), 'w') as f:
    f.write('code\tvalue\tgrade\tsource\tnote\n')
    for p in sorted(per):
        (top, n), tot = per[p].most_common(1)[0], sum(per[p].values())
        ok = n >= 2 and len(rows[p][top]) >= 2 and n >= 0.6 * tot
        f.write('%s\t%s\t%s\tf.23 interlinear gloss (R9-WVOALIGN)\t%d/%d aligned, %d rows; others %s\n' % (
            p, top, 'C' if ok else 'M', n, tot, len(rows[p][top]),
            ','.join('%s:%d' % kv for kv in per[p].most_common()[1:]) or '-'))
