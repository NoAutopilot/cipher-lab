#!/usr/bin/env python3
"""C1 known-answer control of the kp2 truth recipe on dint-f128-print (TXP-KP2C, LANE TX-ENGINEER-2, 9 Oct 2026;
PREREG benchmark-tx/PREREG-txeng2-4.md section C1, TX-RED F3). Read-free: no reader, no vision, no network.

The kp2 recipe (benchmark-tx/truth_variant.py keyprint_rows(variant='kp2'), unchanged) is run on f.128r with the 1882 print's
letters at the aligned positions (f128/print_align/align_print.tsv plain_chunk) standing in for the gloss, the alignment's
own status as align_status (neighbour conflict:* rule as in kp2), fold as build_dint-f89-gloss.py. The print truth
(benchmark-tx/dint-f128-print.truth.tsv, built by build_dint128.py) is put through benchmark-tx/dint128_label_map.tsv, the
reader vocabulary kp2 is written in (as tx_bench --label-map does), and compared per position scored by both:
  equal    kp2 set == print set
  contains kp2 set strictly contains the print set (kp2 accepts reads the print truth calls wrong)
  misses   the print set has a member outside the kp2 set (kp2 calls a print-right read wrong)
Declared before running (this header committed first): "agrees" in the C1 gate = `equal`; `equal or contains` is reported
beside it, never alone. Gate: agree share >= 0.90 of positions scored by both -> PASS, else FAIL.
Writes per_position.tsv and the kp2 truth for f.128 (dint-f128-print.truth.kp2c.tsv here, never under benchmark-tx/ root,
never added to BENCHMARK-TX.tsv) plus bench_kp2c.tsv, a one-row bench file for tools/tx_bench.py. `--check` exits 1 if stale.
"""
import csv, os, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'benchmark-tx'))
import truth_variant as tv  # noqa: E402
import importlib.util  # noqa: E402
_s = importlib.util.spec_from_file_location('g89', os.path.join(ROOT, 'benchmark-tx/build_dint-f89-gloss.py'))
g89 = importlib.util.module_from_spec(_s); _s.loader.exec_module(g89)
F = os.path.join(ROOT, 'ciphers/fr3621-dinteville-1592/f128')
PT = os.path.join(ROOT, 'benchmark-tx/dint-f128-print.truth.tsv')


def rd(p):
    with open(p, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def build():
    al = defaultdict(list)
    for r in rd(os.path.join(F, 'print_align/align_print.tsv')):
        al[r['cipher_line']].append(r)
    trows, keys, cnt = [], [], Counter()
    for g in rd(os.path.join(F, 'gloss_pairs.tsv')):
        sg = g['signs'].split()
        if not sg:
            continue
        seg = al['%s.%s' % (g['line'], g['order'])]
        assert [r['sign'] for r in seg] == sg
        ln = 'f128_' + g['line']
        for r in seg:
            cnt[ln] += 1
            trows.append((ln, None, None, None, None, None, r['plain_chunk'], r['status']))
            keys.append((ln, cnt[ln], r['sign']))
    kp2 = tv.keyprint_rows(trows, keys, lambda c: False, g89.fold, 'kp2')
    lm = tv.reader_label_map()
    pt = {(r['line'], int(r['pos'])): r for r in rd(PT)}
    assert len(pt) == len(kp2)
    per, tally = [], Counter()
    for ln, pos, sign, truth, chunk, st, _, ast in kp2:
        p = pt[(ln, pos)]
        assert p['ref_sign'] == sign
        ps = {lm.get(x, x) for x in p['truth'].split('|') if x}
        ks = set(filter(None, truth.split('|')))
        if st == 'scored' and p['status'] == 'scored':
            cls = 'equal' if ks == ps else 'contains' if ks > ps else 'misses'
        else:
            cls = 'kp2-only' if st == 'scored' else 'print-only' if p['status'] == 'scored' else 'neither'
        tally[cls] += 1
        per.append((ln, pos, sign, chunk, ast, st, '|'.join(sorted(ks)), p['status'], '|'.join(sorted(ps)), cls))
    files = {}
    files['per_position.tsv'] = 'line\tpos\tref_sign\tprint_chunk\talign_status\tkp2_status\tkp2_set\tprint_status\tprint_set_mapped\tclass\n' + \
        ''.join('\t'.join(map(str, r)) + '\n' for r in per)
    sc = sum(1 for r in kp2 if r[5] == 'scored')
    files['dint-f128-print.truth.kp2c.tsv'] = (
        '# dint-f128-print kp2c: the kp2 recipe (truth_variant.keyprint_rows, variant kp2) on f.128r with the 1882 print letters as gloss; '
        'built by benchmark-tx/txeng2/kp2c/kp2c.py (PREREG-txeng2-4 C1); %d positions, %d scored; control only, not a bench item\n' % (len(kp2), sc)
        + 'line\tpos\tref_sign\ttruth\tplain\tstatus\tflag\talign_status\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in kp2))
    bench = open(os.path.join(ROOT, 'BENCHMARK-TX.tsv')).read().splitlines()
    hdr = bench[0]
    row = next(l for l in bench if l.startswith('dint-f128-print\t'))
    cols = hdr.split('\t')
    v = row.split('\t')
    v[cols.index('item')] = 'dint-f128-print-kp2c'
    v[cols.index('truth')] = 'dint-f128-print.truth.kp2c.tsv'
    files['bench_kp2c.tsv'] = hdr + '\n' + '\t'.join(v) + '\n'
    return files, tally


def main():
    files, tally = build()
    stale = []
    for rel, text in files.items():
        p = os.path.join(HERE, rel)
        if (open(p).read() if os.path.exists(p) else None) != text:
            stale.append(rel)
            if '--check' not in sys.argv:
                open(p, 'w').write(text)
    both = tally['equal'] + tally['contains'] + tally['misses']
    print('positions by class: %s' % dict(sorted(tally.items())))
    print('scored by both %d: equal %d (%.3f), contains %d, misses %d; equal-or-contains %.3f' % (
        both, tally['equal'], tally['equal'] / both, tally['contains'], tally['misses'],
        (tally['equal'] + tally['contains']) / both))
    print('gate (agree = equal, >= 0.90): %s' % ('PASS' if tally['equal'] / both >= 0.90 else 'FAIL'))
    print(('stale: ' + ', '.join(stale)) if stale and '--check' in sys.argv else 'written' if stale else 'up to date')
    return 1 if stale and '--check' in sys.argv else 0


if __name__ == '__main__':
    sys.exit(main())
