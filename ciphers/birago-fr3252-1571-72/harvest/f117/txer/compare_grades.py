#!/usr/bin/env python3
"""TXE-R reporting glue (not an instrument): compare a new f.117r token table with the committed one by ALIGNED position.

    python3 compare_grades.py NEW_tokens.tsv [COMMITTED_tokens.tsv] [--out changes.tsv]

Per line, the new and committed sign sequences are aligned with difflib.SequenceMatcher (autojunk off). Every committed
token is paired with the new token aligned to it (equal or replace blocks, pairwise) or with nothing (deleted); every
unpaired new token is 'inserted'. Prints grade counts for both, a transition table (committed grade -> new grade), and
writes one row per pair whose sign, value or grade differs. Default committed table: the RD7 reading
(../nevers-birago-fr3251-1572/harvest/tx_decode/eye/apply/reading_f117_apply_tokens.tsv, S 190 / M 63 / U 26).
"""
import argparse, collections, csv, difflib, os

HERE = os.path.dirname(os.path.abspath(__file__))
COMMITTED = os.path.join(HERE, '../../../../nevers-birago-fr3251-1572/harvest/tx_decode/eye/apply/reading_f117_apply_tokens.tsv')


def load(path):
    rows = [r for r in csv.DictReader((l for l in open(path) if not l.startswith('#')), delimiter='\t')]
    by = collections.OrderedDict()
    for r in rows:
        by.setdefault(r['line'], []).append(r)
    return rows, by


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('new'); ap.add_argument('committed', nargs='?', default=COMMITTED); ap.add_argument('--out')
    a = ap.parse_args()
    nrows, nby = load(a.new); crows, cby = load(a.committed)
    for name, rows in (('committed', crows), ('new', nrows)):
        c = collections.Counter(r['grade'] for r in rows)
        print(f'{name}: tokens {len(rows)}: ' + ', '.join(f'{g} {c[g]}' for g in sorted(c)))
    trans = collections.Counter(); out = []
    for line in sorted(set(cby) | set(nby)):
        cs, ns = cby.get(line, []), nby.get(line, [])
        sm = difflib.SequenceMatcher(None, [r['sign'] for r in cs], [r['sign'] for r in ns], autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            pairs = []
            if op in ('equal', 'replace'):
                n = max(i2 - i1, j2 - j1)
                for k in range(n):
                    pairs.append((cs[i1 + k] if i1 + k < i2 else None, ns[j1 + k] if j1 + k < j2 else None))
            elif op == 'delete':
                pairs = [(cs[i], None) for i in range(i1, i2)]
            else:
                pairs = [(None, ns[j]) for j in range(j1, j2)]
            for c, n in pairs:
                cg = c['grade'] if c else '-'; ng = n['grade'] if n else '-'
                trans[(cg, ng)] += 1
                if c is None or n is None or c['sign'] != n['sign'] or c['value'] != n['value'] or cg != ng:
                    out.append([line, c['pos'] if c else '', c['sign'] if c else '', c['value'] if c else '', cg,
                                n['pos'] if n else '', n['sign'] if n else '', n['value'] if n else '', ng])
    print('transitions committed -> new (count):')
    for (cg, ng), k in sorted(trans.items()):
        print(f'  {cg} -> {ng}: {k}')
    s_gain = sum(k for (cg, ng), k in trans.items() if ng == 'S' and cg != 'S')
    s_loss = sum(k for (cg, ng), k in trans.items() if cg == 'S' and ng != 'S')
    print(f'aligned: tokens newly S {s_gain}, tokens no longer S {s_loss}; changed rows {len(out)}')
    if a.out:
        with open(a.out, 'w') as f:
            w = csv.writer(f, delimiter='\t', lineterminator='\n')
            w.writerow(['line', 'old_pos', 'old_sign', 'old_value', 'old_grade', 'new_pos', 'new_sign', 'new_value', 'new_grade'])
            w.writerows(out)


if __name__ == '__main__':
    main()
