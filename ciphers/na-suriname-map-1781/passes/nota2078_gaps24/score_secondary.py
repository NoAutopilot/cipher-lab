#!/usr/bin/env python3
"""GAPS24: secondary pairs of the 2077 legend vs the plain 4.VEL 2078 Nota (prereg.md in this folder).

  python3 score_secondary.py  -> result.tsv, regrade.tsv (APPLY rows only in supported pairs)
Reuses passes/nota2078_gaps23/score.py (entry extraction, normalisation, NW alignment, statistic A) unchanged.
"""
import csv, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'nota2078_gaps23'))
import score as g23  # noqa: E402

PAIRS = [('a', 'B'), ('e', 'h'), ('k', 's'), ('l', 't')]
SEED, DRAWS = 20261003, 2000


def main():
    e77 = g23.entries_2077()
    e78 = {}
    with open(os.path.join(HERE, '..', 'nota2078_gaps23', 'nota2078.tsv')) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            e78[r['entry'].strip()] = g23.norm(r['text'])
    rng = random.Random(SEED)
    keys78 = sorted(e78)
    lines = ['pair\tH_match\tH\tA\tN1_p99\tN1_mean\tN2_p99\tN2_mean\tsupported']
    M = H = 0
    supported, cand = [], []
    for a, b in PAIRS:
        m, h, al = g23.stat(e77[a], e78[b]); M += m; H += h
        n1 = [g23.stat(e77[a], e78[rng.choice([k for k in keys78 if k != b])])[0] / h for _ in range(DRAWS)]
        n2 = [g23.stat(g23.permuted(e77[a], rng), e78[b])[0] / h for _ in range(DRAWS)]
        A = m / h
        ok = A > g23.p99(n1) and A > g23.p99(n2)
        lines.append(f'77{a}-78{b}\t{m}\t{h}\t{A:.3f}\t{g23.p99(n1):.3f}\t{sum(n1)/DRAWS:.3f}\t'
                     f'{g23.p99(n2):.3f}\t{sum(n2)/DRAWS:.3f}\t{"yes" if ok else "no"}')
        toks, text = e77[a], e78[b]
        hidx = [i for i, t in enumerate(toks) if t[3] == 'H']
        for i, (t, x) in enumerate(zip(toks, al)):
            if t[3] not in ('M', 'U') or x is None:
                continue
            got = text[x]
            ctx = [k for k in hidx if k < i][-3:] + [k for k in hidx if k > i][:3]
            ok_ctx = len(ctx) >= 2 and all(al[k] is not None and text[al[k]] in toks[k][2] for k in ctx)
            ok_val = (t[3] == 'U') or (got in t[2])
            act = 'APPLY' if (ok and ok_ctx and ok_val) else ('keep-unsupported-pair' if not ok else 'keep')
            cand.append((f'77{a}-78{b}', t[0], t[1], t[4], t[3], got, 'yes' if ok_ctx else 'no', 'yes' if ok_val else 'no', act))
    lines.append(f'POOLED(descriptive)\t{M}\t{H}\t{M/H:.3f}')
    open(os.path.join(HERE, 'result.tsv'), 'w').write('\n'.join(lines) + '\n')
    print('\n'.join(lines))
    with open(os.path.join(HERE, 'regrade.tsv'), 'w') as f:
        f.write('pair\tline\tpos\tvalue\tgrade\taligned_2078\tctx_ok\tvalue_ok\taction\n')
        for c in cand:
            f.write('\t'.join(map(str, c)) + '\n')
    print(f'regrade: {sum(c[-1]=="APPLY" for c in cand)} APPLY of {len(cand)} M/U aligned')
    return 0


if __name__ == '__main__':
    sys.exit(main())
