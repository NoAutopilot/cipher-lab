#!/usr/bin/env python3
"""Build key.tsv and key_conflicts.tsv from the contemporary glosses (R17, 24 Sept 2026).

  python3 build_key.py           write key.tsv, key_conflicts.tsv, key_items.tsv, ciphertext_targets.tsv (BLA184/186/191 only)
  python3 build_key.py --check   exit 1 if any committed file is stale

Evidence: every ciphertext.tsv column graded H that carries a gloss (the interlinear decipherment written over the
group on the leaf, or on BLA189 p3 / BLA190 p5-p6 the letter's own bracketed clear phrase), normalised as in
settle.py. Grade C for every key row (known plaintext on the leaf, LANE W's ruling). Value = the majority gloss;
a tie between two glosses gives 'a|b' (decode_key grades it M). Rows seen once are kept with n=1.
key_items.tsv: one-system test, leave one item out: for each item, the share of its glossed columns whose gloss
equals the value the OTHER items give the same group (only groups the other items key).
"""
import csv, sys, io, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import settle

HERE = settle.HERE
TARGETS = ('BLA184', 'BLA186', 'BLA191')
BRACKET = ('BLA189_p3', 'BLA190_p5', 'BLA190_p6')


def item(line):
    return line.split('_')[0]


def main():
    ct = list(csv.DictReader(open(os.path.join(HERE, 'ciphertext.tsv')), delimiter='\t'))
    ev = [(r['line'], r['group'], r['gloss']) for r in ct if r['conf'] == 'H' and r['gloss'] and r['group'] not in ('?', '-')]
    per = collections.defaultdict(collections.Counter)
    src = collections.defaultdict(set)
    items = collections.defaultdict(set)
    for l, g, gl in ev:
        per[g][gl] += 1
        src[g].add('bracket' if l.rsplit('_', 1)[0] in BRACKET else 'gloss')
        items[g].add(item(l))
    key, conf_rows = [], []
    for g in sorted(per, key=int):
        mc = per[g].most_common()
        n = sum(per[g].values())
        if len(mc) > 1 and mc[0][1] == mc[1][1]:
            val = mc[0][0] + '|' + mc[1][0]
        else:
            val = mc[0][0]
        key.append((g, val, 'C', '+'.join(sorted(src[g])), 'n=%d items=%s%s' % (
            n, ','.join(sorted(items[g])), '' if len(mc) == 1 else ' other=' + ';'.join('%s:%d' % x for x in mc[1:4]))))
    val = {k[0]: k[1] for k in key}
    by_item = collections.defaultdict(lambda: [0, 0])
    for l, g, gl in ev:
        by_item[item(l)][0] += 1
        if gl not in val[g].split('|'):
            by_item[item(l)][1] += 1
    for it in sorted(by_item):
        conf_rows.append((it, by_item[it][0], by_item[it][1], '%.3f' % (by_item[it][1] / by_item[it][0])))
    # leave-one-item-out
    loo = []
    for it in sorted(set(item(l) for l, _, _ in ev)):
        other = collections.defaultdict(collections.Counter)
        for l, g, gl in ev:
            if item(l) != it:
                other[g][gl] += 1
        tested = agree = 0
        for l, g, gl in ev:
            if item(l) == it and g in other:
                tested += 1
                agree += other[g].most_common(1)[0][0] == gl
        own = sum(1 for l, _, _ in ev if item(l) == it)
        loo.append((it, own, tested, agree, '%.3f' % (agree / tested) if tested else ''))
    out = {}
    f = io.StringIO(); w = csv.writer(f, delimiter='\t', lineterminator='\n')
    w.writerow(['line', 'pos', 'group', 'conf'])
    w.writerows([(r['line'], r['pos'], r['group'], r['conf']) for r in ct if item(r['line']) in TARGETS])
    out['ciphertext_targets.tsv'] = f.getvalue()
    for name, hdr, rows in (('key.tsv', ['code', 'value', 'grade', 'source', 'note'], key),
                            ('key_conflicts.tsv', ['item', 'glossed_H_columns', 'differ_from_key', 'share'], conf_rows),
                            ('key_items.tsv', ['item', 'glossed_H_columns', 'groups_keyed_by_other_items', 'same_value', 'share'], loo)):
        f = io.StringIO(); w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(hdr); w.writerows(rows)
        out[name] = f.getvalue()
    if '--check' in sys.argv:
        bad = [n for n, s in out.items() if not os.path.exists(os.path.join(HERE, n)) or open(os.path.join(HERE, n)).read() != s]
        print('stale: %s' % bad if bad else 'ok'); sys.exit(1 if bad else 0)
    for n, s in out.items():
        open(os.path.join(HERE, n), 'w').write(s)
    print(len(key), 'key rows;', sum(1 for k in key if 'other=' in k[4]), 'with a second gloss;',
          sum(1 for k in key if '|' in k[1]), 'ties')


if __name__ == '__main__':
    main()
