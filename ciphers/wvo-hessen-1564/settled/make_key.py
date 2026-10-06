#!/usr/bin/env python3
"""WVO-APPLY (6 Oct 2026): rebuild the f.23 key per the owner's settled sign (sorter/settled_labels.tsv,
tools/sign_sorter_apply.py) instead of per provisional k-means pile.

No re-alignment: each tile keeps the gloss letter the R10-WVOTX alignment put over it (r9align/tile_letters.tsv,
PREREG-R9-WVOALIGN parameters); only the sign label changes, by sid.  Grade per settled sign with the PREREG
statistic unchanged: C when the top letter is aligned >= 2 times on >= 2 rows and is >= 0.6 of the sign's aligned
occurrences, M otherwise (a 1-tile owner pile can never reach C).  Aside and bad-cut tiles get no key row (U).
Writes key.tsv, ciphertext.tsv (tools/decode_key.py tsv format), findings.tsv (a settled sign uniting tiles under
different gloss letters; a gloss letter spread over several settled signs) and compare.tsv (per tile: pile value and
grade from r9align/key.tsv vs settled value and grade).  Run from anywhere."""
import csv, os
from collections import Counter, defaultdict
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(D)
rd = lambda p: list(csv.DictReader(open(os.path.join(T, p)), delimiter='\t'))
tl = rd('r9align/tile_letters.tsv')
st = {r['sid']: r for r in rd('sorter/settled_labels.tsv')}
pk = {r['code']: r for r in rd('r9align/key.tsv')}
SKIP = {'aside', 'bad-cut'}
per, rows, tiles = defaultdict(Counter), defaultdict(lambda: defaultdict(set)), defaultdict(int)
for r in tl:
    if r['status'] == 'clear':
        continue
    s = st[r['sid']]
    if s['status'] in SKIP:
        continue
    tiles[s['new_sign']] += 1
    if r['gloss_letter']:
        per[s['new_sign']][r['gloss_letter']] += 1
        rows[s['new_sign']][r['gloss_letter']].add(r['row'])
key = {}
with open(os.path.join(D, 'key.tsv'), 'w') as f:
    f.write('code\tvalue\tgrade\tsource\tnote\n')
    for sg in sorted(tiles):
        if not per[sg]:
            key[sg] = ('', 'M')
            f.write('%s\t\tM\tf.23 gloss via settled sign (WVO-APPLY)\t%d tiles, none aligned\n' % (sg, tiles[sg]))
            continue
        (top, n), tot = per[sg].most_common(1)[0], sum(per[sg].values())
        ok = n >= 2 and len(rows[sg][top]) >= 2 and n >= 0.6 * tot
        key[sg] = (top, 'C' if ok else 'M')
        f.write('%s\t%s\t%s\tf.23 gloss via settled sign (WVO-APPLY)\t%d tiles; %d/%d aligned, %d rows; others %s\n' % (
            sg, top, key[sg][1], tiles[sg], n, tot, len(rows[sg][top]),
            ','.join('%s:%d' % kv for kv in per[sg].most_common()[1:]) or '-'))
letters = defaultdict(Counter)
for sg, c in per.items():
    for l, n in c.items():
        letters[l][sg] += n
with open(os.path.join(D, 'findings.tsv'), 'w') as f:
    f.write('kind\titem\tdetail\n')
    for sg in sorted(per):
        if len(per[sg]) > 1:
            f.write('sign-mixes-letters\t%s\t%s\n' % (sg, ','.join('%s:%d' % kv for kv in per[sg].most_common())))
    for l in sorted(letters):
        if len(letters[l]) > 1:
            f.write('letter-over-signs\t%s\t%s\n' % (l, ','.join('%s:%d' % kv for kv in letters[l].most_common())))
with open(os.path.join(D, 'ciphertext.tsv'), 'w') as g, open(os.path.join(D, 'compare.tsv'), 'w') as c:
    g.write('line\tpos\tsign\tconf\n')
    c.write('sid\trow\tidx\tgloss_letter\tpile\tpile_value\tpile_grade\tsettled_sign\tsettled_status\tsettled_value\tsettled_grade\n')
    for r in tl:
        s = st[r['sid']]
        if r['status'] == 'clear':
            sign = '[PLAIN:E.L.]'
        else:
            sign = s['new_sign'] if s['status'] not in SKIP else 'X-' + s['status']
        g.write('%s\t%d\t%s\t\n' % (r['row'], int(r['idx']) + 1, sign))
        p = pk.get(r['pile'], {'value': '', 'grade': ''})
        v, gr = key.get(sign, ('', 'U')) if r['status'] != 'clear' else ('E.L.', 'clear')
        c.write('\t'.join([r['sid'], r['row'], r['idx'], r['gloss_letter'], r['pile'], p['value'], p['grade'],
                           sign, s['status'], v, gr]) + '\n')
