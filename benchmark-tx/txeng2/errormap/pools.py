#!/usr/bin/env python3
"""Pool the TXP-AGREE error-map position tables (9 Oct 2026) into eval / dev / other pools; prints markdown.

    python3 benchmark-tx/txeng2/errormap/pools.py > benchmark-tx/txeng2/errormap/pools.md

eval = birago1572-no87 eval_heldout (f178v L13-23, f179r L01-03) + spinelli-c1519-confirm; dev = no87 dev_tune
(f178v L01-12) + dint-f128-print + ceppo-f87-S + ceppo-f36v-gloss; other = no87 f178r L01-03 (in neither split).
Only the baseline's errors (the first --pass of each run) are counted."""
import csv, os, re
from collections import Counter

D = os.path.dirname(os.path.abspath(__file__))
AC = ['all-same-wrong', 'all-wrong-split', 'majority-wrong', 'minority-wrong', 'baseline-only', 'no-other-pass']
EC = ['crop', 'look-alike', 'thin', 'other']


def no87_pool(line):
    m = re.match(r'f(\d+[rv])_L(\d+)', line)
    leaf, n = m.group(1), int(m.group(2))
    if leaf == '178v':
        return 'dev' if n <= 12 else 'eval'
    return 'eval' if leaf == '179r' else 'other'


ITEMS = [('birago1572-no87', None), ('spinelli-c1519-confirm', 'eval'), ('dint-f128-print', 'dev'),
         ('ceppo-f87-S', 'dev'), ('ceppo-f36v-gloss', 'dev')]
pools = {'eval': [], 'dev': [], 'other': []}
scored = Counter()
for item, pool in ITEMS:
    rows = list(csv.DictReader(open(os.path.join(D, item + '_positions.tsv')), delimiter='\t'))
    base = [k for k in rows[0] if k.startswith('err_')][0][4:]
    for r in rows:
        p = pool or no87_pool(r['line'])
        if r['err_' + base] == '':
            continue
        scored[(p, item)] += 1
        if r['err_' + base] == '1':
            r['_item'], r['_read'] = item, r['read_' + base]
            pools[p].append(r)
out = []
for p in ('eval', 'dev', 'other'):
    err = pools[p]
    n = len(err)
    per = Counter(r['_item'] for r in err)
    out += ['', '## Pool %s: %d baseline errors' % (p, n), '',
            'Per item (errors / scored): ' + '; '.join('%s %d/%d' % (i, per[i], scored[(p, i)]) for i, _ in ITEMS if scored[(p, i)]),
            '', '| agree_class | errors | share |', '|---|---|---|']
    ac = Counter(r['agree_class'] for r in err)
    for c in AC:
        if ac[c]:
            out.append('| %s | %d | %.1f%% |' % (c, ac[c], 100.0 * ac[c] / n))
    acs = [c for c in AC if ac[c]]
    out += ['', '| err_class | errors (share) | ' + ' | '.join(acs) + ' |', '|---|---|' + '---|' * len(acs)]
    ec = Counter(r['err_class'] for r in err)
    for e, k in ec.most_common():
        rs = [r for r in err if r['err_class'] == e]
        c = Counter(r['agree_class'] for r in rs)
        out.append('| %s | %d (%.0f%%) | %s |' % (e, k, 100.0 * k / n, ' | '.join(str(c[a]) for a in acs)))
    pc = Counter((r['_item'].split('-')[0], r['plain'], r['_read']) for r in err)
    out += ['', '| item | truth <- read | n | agree_class |', '|---|---|---|---|']
    for k, v in pc.most_common(10):
        c = Counter(r['agree_class'] for r in err if (r['_item'].split('-')[0], r['plain'], r['_read']) == k)
        out.append('| %s | %s <- %s | %d | %s |' % (k[0], k[1], k[2], v, ', '.join('%s %d' % kv for kv in c.most_common())))
print('\n'.join(out))
