#!/usr/bin/env python3
"""Build benchmark item dint-f128-print for BENCHMARK-TX.tsv (TXB2, 3 Oct 2026; rules in benchmark-tx/PREREG-dint128.md).

Reference = the reconciled sign read of BnF fr.3621 f.128r (ciphers/fr3621-dinteville-1592/f128/gloss_pairs.tsv), per
physical line (f128_L02..L05), segments joined in order. Truth = the 1882 Revue de Champagne print chunk aligned to each
sign (DIN-PRINT, f128/print_align/align_print.tsv) forced through key_print.tsv: scored only where the alignment status is
'agrees' and the reference sign's key row has agree == n >= 2; truth set = every such sign with the same meaning.
Also writes the blind passes A and B in tx_bench format (outputs/dint-f128-print/passA.tsv, passB.tsv): per physical line,
every non-CLEAR row's signs in order, nothing else edited. The reconciled read is not written (it scores 0 by construction).
Run from the repo root: python3 benchmark-tx/build_dint128.py [--check]
"""
import csv, os, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = os.path.join(ROOT, 'ciphers/fr3621-dinteville-1592/f128')
OUT = os.path.join(ROOT, 'benchmark-tx')
ITEM = 'dint-f128-print'


def rd(p):
    with open(p, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def build():
    key = {r['sign']: r for r in rd(os.path.join(F, 'print_align/key_print.tsv'))}
    good = {s: r['meaning'] for s, r in key.items() if int(r['agree']) == int(r['n']) >= 2}
    by_mean = defaultdict(set)
    for s, m in good.items():
        by_mean[m].add(s)
    al = defaultdict(list)
    for r in rd(os.path.join(F, 'print_align/align_print.tsv')):
        al[r['cipher_line']].append(r)
    files = {}
    rows = ['# dint-f128-print: fr.3621 f.128r reconciled read vs the 1882 Revue de Champagne print through key_print '
            '(agree==n>=2); built by benchmark-tx/build_dint128.py, rules benchmark-tx/PREREG-dint128.md',
            'line\tpos\tref_sign\ttruth\tplain\tstatus']
    nsc = nex = 0
    for g in rd(os.path.join(F, 'gloss_pairs.tsv')):
        sg = g['signs'].split()
        if not sg:
            continue
        seg = al['%s.%s' % (g['line'], g['order'])]
        assert [r['sign'] for r in seg] == sg, (g['line'], g['order'])
        ln = 'f128_' + g['line']
        for r in seg:
            pos = sum(1 for x in rows[2:] if x.startswith(ln + '\t')) + 1
            s, p = r['sign'], r['plain_chunk']
            if r['status'] == 'agrees' and s in good and good[s] == p:
                rows.append('%s\t%d\t%s\t%s\t%s\tscored' % (ln, pos, s, '|'.join(sorted(by_mean[p])), p)); nsc += 1
            else:
                why = r['status'] if r['status'] != 'agrees' else ('key-row-n<2-or-conflicted' if s not in good else 'key-mismatch')
                rows.append('%s\t%d\t%s\t\t%s\texcluded:%s' % (ln, pos, s, p, why)); nex += 1
    files['%s.truth.tsv' % ITEM] = '\n'.join(rows) + '\n'
    for P in ('A', 'B'):
        lines = defaultdict(list)
        for r in rd(os.path.join(F, 'pass%s.tsv' % P)):
            if r['gloss'].startswith('CLEAR:'):
                continue
            lines[r['line']] += [x for x in r['signs'].split() if x != '-']
        out = ['# blind pass %s of fr.3621 f.128r (A2-DIN, Sonnet, crops only, no key), from f128/pass%s.tsv, rows joined per line' % (P, P),
               'line\tpos\tsign']
        for ln in sorted(lines):
            out += ['f128_%s\t%d\t%s' % (ln, i + 1, s) for i, s in enumerate(lines[ln])]
        files['outputs/%s/pass%s.tsv' % (ITEM, P)] = '\n'.join(out) + '\n'
    return files, nsc, nex


def main():
    files, nsc, nex = build()
    stale = []
    for rel, text in files.items():
        p = os.path.join(OUT, rel)
        old = open(p).read() if os.path.exists(p) else None
        if old != text:
            stale.append(rel)
            if '--check' not in sys.argv:
                os.makedirs(os.path.dirname(p), exist_ok=True)
                open(p, 'w').write(text)
    print('%s: positions %d, scored %d, excluded %d; %s' % (ITEM, nsc + nex, nsc, nex,
          ('stale: ' + ', '.join(stale)) if stale and '--check' in sys.argv else 'written' if stale else 'up to date'))
    return 1 if stale and '--check' in sys.argv else 0


if __name__ == '__main__':
    sys.exit(main())
