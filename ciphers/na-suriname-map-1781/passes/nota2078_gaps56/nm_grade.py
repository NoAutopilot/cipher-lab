#!/usr/bin/env python3
"""GAPS56: apply GAPS23's context clause (ii) to the three [u-dots] tokens the gating alignment places on a 2078 m.

  python3 nm_grade.py   -> nm_grade.tsv (one row per [u-dots] token in a gating pair; APPLY only for aligned m + ctx ok)
Reuses score.py (byte-identical copy of passes/nota2078_gaps45/score.py) for the entries, the alignment and the context
test. Run BEFORE the exceptions are written: it reads the current reading, where these tokens are H n.
GAPS23's registered clause (i) covers M/U tokens only; these are H on the sign (key's N, GAPS25/45). The step licensed
here (GAPS55 Verdict, account-4 parent 3 Oct 2026) grades the plain letter C where the 2078 Nota gives it, with the
sign identity (N) kept in the reason: Wollant's own use of the N sign for m (GAPS45: 16 of 17 by context).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import score as S

TARGETS = {('2077_L11', 10), ('2077_L11', 23), ('2077_L12', 37)}


def main():
    e77 = S.entries_2077()
    import csv
    e78 = {}
    with open(os.path.join(S.HERE, 'nota2078.tsv')) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            e78[r['entry'].strip()] = S.norm(r['text'])
    rows = []
    for a, b in S.GATING:
        toks, text = e77[a], e78[b]
        _, _, al = S.stat(toks, text)
        hidx = [i for i, t in enumerate(toks) if t[3] == 'H']
        for i, (t, x) in enumerate(zip(toks, al)):
            if (t[0], t[1]) not in TARGETS:
                continue
            got = text[x] if x is not None else '-'
            ctx = [k for k in hidx if k < i][-3:] + [k for k in hidx if k > i][:3]
            ok_ctx = len(ctx) >= 2 and all(al[k] is not None and text[al[k]] in toks[k][2] for k in ctx)
            lo, hi = max(0, (x or 0) - 6), (x or 0) + 7
            rows.append((f'77{a}-78{b}', t[0], t[1], t[4], t[3], got, len(ctx), 'yes' if ok_ctx else 'no',
                         text[lo:hi], 'APPLY' if (ok_ctx and got == 'm') else 'keep'))
    with open(os.path.join(S.HERE, 'nm_grade.tsv'), 'w') as f:
        f.write('pair\tline\tpos\tvalue\tgrade\taligned_2078\tn_ctx\tctx_ok\t2078_window\taction\n')
        for r in rows:
            f.write('\t'.join(map(str, r)) + '\n')
    for r in rows:
        print('\t'.join(map(str, r)))
    found = {(r[1], r[2]) for r in rows}
    print(f'{len(rows)} of {len(TARGETS)} targets found in gating pairs; missing: {sorted(TARGETS - found)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
