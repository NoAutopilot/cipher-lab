#!/usr/bin/env python3
"""AX-COMP (26 Sept 2026): from tools/interlinear_align.py output for letter N, write key_N.tsv (period key,
grade H where >= 2 alignments agree on the value and they are >= 60% of its alignments, else M), and
axcomp/compare_N.tsv against key_full.tsv and key_5799.tsv (agree / new code / conflict).

    python3 axcomp/keys.py N           reads axcomp/align_N.tsv, axcomp/rawkey_N.tsv
    python3 axcomp/keys.py N --check   exit 1 if key_N.tsv or compare_N.tsv is stale
"""
import csv, os, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
TOP = os.path.dirname(HERE)


def norm(v):
    return v.lower().replace('v', 'u').replace('j', 'i').replace('y', 'i')


def load_key(path):
    out = {}
    if not os.path.exists(path):
        return out
    with open(path, encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            out[r['code']] = (r['value'], r.get('grade', ''))
    return out


def build(n):
    empty = Counter()
    total = Counter()
    with open(os.path.join(HERE, 'align_%s.tsv' % n), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['kind'] == 'num':
                total[r['value']] += 1
                if not r['plain_chunk']:
                    empty[r['value']] += 1
    rows = []
    with open(os.path.join(HERE, 'rawkey_%s.tsv' % n), encoding='utf-8') as f:
        raw = {r['value']: r for r in csv.DictReader(f, delimiter='\t')}
    for code in sorted(total, key=lambda c: int(c)):
        r = raw.get(code)
        tot, emp = total[code], empty[code]
        if r is None or (emp >= 2 and emp >= 0.6 * tot):
            val, agree, others = 'NULL', emp, (r['meaning'] + ':' + r['n'] if r else '')
        else:
            val, agree, others = r['meaning'], int(r['agree']), r['others']
        grade = 'H' if agree >= 2 and agree >= 0.6 * tot else 'M'
        rows.append([code, val, grade, tot, agree, emp, others])
    key = [['code', 'value', 'grade', 'occurrences', 'agree', 'empty', 'others']] + rows
    full = load_key(os.path.join(TOP, 'key_full.tsv'))
    k99 = load_key(os.path.join(TOP, 'key_5799.tsv'))
    cmp_ = [['code', 'value_%s' % n, 'grade', 'occurrences', 'key_full', 'vs_key_full', 'key_5799', 'vs_key_5799']]
    for code, val, grade, tot, agree, emp, others in rows:
        def rel(k):
            if code not in k:
                return '', 'new code'
            v = k[code][0]
            return v, ('agree' if norm(v) == norm(val) else 'conflict')
        fv, fr = rel(full)
        sv, sr = rel(k99)
        cmp_.append([code, val, grade, tot, fv, fr, sv, sr])
    return key, cmp_


def write(path, rows):
    import io
    b = io.StringIO()
    csv.writer(b, delimiter='\t', lineterminator='\n').writerows(rows)
    return b.getvalue()


def main():
    n = sys.argv[1]
    check = '--check' in sys.argv
    key, cmp_ = build(n)
    stale = False
    for path, rows in ((os.path.join(TOP, 'key_%s.tsv' % n), key), (os.path.join(HERE, 'compare_%s.tsv' % n), cmp_)):
        text = write(path, rows)
        if check:
            if not os.path.exists(path) or open(path, encoding='utf-8').read() != text:
                print('STALE', path); stale = True
        else:
            open(path, 'w', encoding='utf-8').write(text)
    c = Counter((r[5], r[7]) for r in cmp_[1:])
    lo = [r for r in cmp_[1:] if int(r[0]) <= 120]
    hi = [r for r in cmp_[1:] if int(r[0]) > 120]
    print('%s: %d codes (%d <=120, %d >120); <=120 vs key_full %s; vs key_5799 %s; >120 vs key_full %s'
          % (n, len(cmp_) - 1, len(lo), len(hi), dict(Counter(r[5] for r in lo)),
             dict(Counter(r[7] for r in lo)), dict(Counter(r[5] for r in hi))))
    sys.exit(1 if stale else 0)


if __name__ == '__main__':
    main()
