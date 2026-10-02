#!/usr/bin/env python3
"""key_all.tsv (evaluate.py --write) -> ../key.tsv, the per-code values the gloss alignment holds stable.
A code enters only when its top chunk agrees in >=2 aligned occurrences and is >=50% of them; grade C at >=3
agreeing occurrences (meaning taken from the period interlinear decipherment, no cryptanalysis), M at 2.
    python3 make_key.py [--check]     (--check: exit 1 if ../key.tsv differs from a regeneration)
"""
import csv, io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))


def build():
    out = io.StringIO()
    w = csv.writer(out, delimiter='\t', lineterminator='\n')
    w.writerow(['code', 'value', 'grade', 'source', 'note'])
    rows = list(csv.DictReader(open(os.path.join(HERE, 'key_all.tsv'), encoding='utf-8'), delimiter='\t'))
    for r in sorted(rows, key=lambda r: int(r['value'])):
        n, ag = int(r['n']), int(r['agree'])
        if ag >= 2 and ag * 2 >= n:
            w.writerow([r['value'], r['meaning'], 'C' if ag >= 3 else 'M',
                        'interlinear gloss alignment (align/, NEXT-PAG 2 Oct 2026)',
                        '%d/%d aligned occurrences agree; others %s' % (ag, n, r['others'] or '-')])
    return out.getvalue()


if __name__ == '__main__':
    path = os.path.join(HERE, '..', 'key.tsv')
    new = build()
    if '--check' in sys.argv:
        old = open(path, encoding='utf-8').read() if os.path.exists(path) else ''
        sys.exit(0 if old == new else 1)
    open(path, 'w', encoding='utf-8').write(new)
    print(new.count('\n') - 1, 'codes')
