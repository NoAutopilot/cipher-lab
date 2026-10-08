#!/usr/bin/env python3
"""SIG-GRA30 (8 Oct 2026): per-line fr16 score for f.30, the scorer of test_f30r_top.py's linescore()
(infer_unkeyed.seg_score: tools/french16_ngram.py 5-gram, '?' filled greedily, bits/char = C - score/known).

  python3 sig30/linescore.py --rank          rank f.30 lines by (M+U) and bits/char, write sig30/rank.tsv
  python3 sig30/linescore.py --tokens FILE   print per-line bits/char for a tokens TSV (reading_f30_extended_tokens.tsv shape)

Values come from the extended tokens file (sign -> value is a function there; checked). Higher bits/char = worse.
"""
import os, sys, csv, collections, importlib.util
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location('iu', os.path.join(H, 'infer_unkeyed.py'))
iu = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(iu)
EXCL = {'f30r_L01', 'f30r_L02', 'f30r_L11', 'f30r_L12'}

def load(fn=os.path.join(H, 'reading_f30_extended_tokens.tsv')):
    return list(csv.DictReader(open(fn), delimiter='\t'))

def signval(rows):
    return {r['sign']: r['value'] for r in rows}

def lstring(vals):
    return ''.join('?' if v == '?' else '' if v == 'NULL' else v for v in vals)

def bpc(vals):
    s = lstring(vals); known = sum(c != '?' for c in s)
    return (iu.C - iu.seg_score(s) / known) if known else float('nan')

def bylines(rows):
    out = collections.OrderedDict()
    for r in rows: out.setdefault(f"{r['folio']}_{r['line']}", []).append(r)
    return out

if __name__ == '__main__':
    if '--help' in sys.argv or len(sys.argv) < 2: print(__doc__); sys.exit(0)
    if '--tokens' in sys.argv:
        for L, rr in bylines(load(sys.argv[sys.argv.index('--tokens') + 1])).items():
            print(f"{L}\t{bpc([r['value'] for r in rr]):.3f}")
        sys.exit(0)
    lines = bylines(load())
    stats = []
    for L, rr in lines.items():
        mu = sum(r['grade'] in ('M', 'U') for r in rr)
        stats.append((L, len(rr), mu, bpc([r['value'] for r in rr])))
    elig = [s for s in stats if s[0] not in EXCL]
    rk_mu = {s[0]: i for i, s in enumerate(sorted(elig, key=lambda s: -s[2]))}
    rk_b = {s[0]: i for i, s in enumerate(sorted(elig, key=lambda s: -s[3]))}
    # combined rank: sum of the two ranks; ties broken by M+U then bits/char
    order = sorted(elig, key=lambda s: (rk_mu[s[0]] + rk_b[s[0]], -s[2], -s[3]))
    out = ['line\ttokens\tM_plus_U\tbits_per_char\trank_MU\trank_bpc\trank_sum\tchosen']
    for i, s in enumerate(order):
        out.append(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]:.3f}\t{rk_mu[s[0]]+1}\t{rk_b[s[0]]+1}\t{rk_mu[s[0]]+rk_b[s[0]]+2}\t{int(i < 8)}")
    open(os.path.join(H, 'sig30', 'rank.tsv'), 'w').write('\n'.join(out) + '\n')
    print('\n'.join(out[:14]))
