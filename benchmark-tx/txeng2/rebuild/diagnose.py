#!/usr/bin/env python3
"""TXP-REBUILD diagnostic (post hoc, read-free; declared AFTER the -kp/-jk scores were seen, so it changes no truth and no
gate): splits passZ's errors on each -kp truth by what key_print says about passZ's own sign at that position --
kp-same-below-gate (a key_print member of the reader label has majority L but misses agree/n >= 0.75 or n >= 3: S(L) is
incomplete, a homophone charged as an error), not-in-kp (primed, X_/NEW or other label key_print never saw), kp-other
(key_print gives passZ's sign another value: a misread, a decipherer slip or an alignment slip). For -jk: the same split
against the full-leaf key of the round-0b build (key_leaf rows from the default truth's own leaf key are not used; the
jackknife's other-lines key is rebuilt here). Usage: python3 benchmark-tx/txeng2/rebuild/diagnose.py"""
import csv, os, sys
from collections import Counter, defaultdict
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, 'benchmark-tx')); sys.path.insert(0, os.path.join(ROOT, 'tools'))
import truth_variant as tv  # noqa: E402
import tx_bench  # noqa: E402


def rows(p):
    with open(p) as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


lm = tv.reader_label_map()
members = defaultdict(list)
for k, v in lm.items():
    members[v].append(k)
kp = {r['sign']: r for r in csv.DictReader(open(tv.KP), delimiter='\t')}
for item in ('dint-f89-gloss', 'dint-f98v-gloss', 'dint-f113-gloss', 'bir1591-f23r-gloss'):
    var = 'jackknife' if item.startswith('bir') else 'keyprint'
    tr = rows(os.path.join(ROOT, 'benchmark-tx/%s.truth.%s.tsv' % (item, var)))
    sc = [r for r in tr if r['status'] == 'scored']
    err = [r for r in sc if r['ref_sign'] not in r['truth'].split('|')]
    c = Counter()
    if var == 'keyprint':
        for r in err:
            ms = [m for m in [r['ref_sign']] + members.get(r['ref_sign'], []) if m in kp]
            if not ms:
                c['not-in-kp'] += 1
            elif any(kp[m]['meaning'] == r['plain'].lower() for m in ms):
                c['kp-same-below-gate'] += 1
            else:
                c['kp-other'] += 1
    else:
        full = defaultdict(Counter)
        for r in tr:
            p = r['plain']
            if p and '?' not in p and not r['align_status'].startswith('null'):
                full[r['ref_sign']][p.lower()] += 1
        for r in err:
            cnt = full[r['ref_sign']]
            top = cnt.most_common(1)[0][0] if cnt else ''
            c['leaf-same' if top == r['plain'].lower() else 'leaf-other'] += 1
    print('%s-%s: scored %d, passZ errors %d (%.3f): %s' % (item, 'jk' if var == 'jackknife' else 'kp', len(sc), len(err),
                                                       len(err) / max(1, len(sc)), dict(c)))
