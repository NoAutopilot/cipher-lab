#!/usr/bin/env python3
"""GAPS64 (account-4, 3 Oct 2026; copy of FT4k decide_l1121.py): decide the L10:66 [sigma] U -> e knock-on candidate under GAPS23's registered rule
(passes/nota2078_gaps23/prereg.md, "Regrade rule"). Run on the reading as committed after GAPS56, BEFORE any exception.

Prints, for L10:66 in pair 77q-78b: the 2078 letter its alignment lands on, clause (i) (value set), and clause (ii)
(nearest three H tokens each side, each aligned to an identical 2078 letter) -- (A) as stated (H tokens only, current
reading), (B) robustness: GAPS56's two C m tokens counted in the context with their C value, (C) the gaps45 state
(L11:10/L11:23 back to H n) to show what made the context fail before. Uses score.py (byte-identical to gaps45/gaps56).
  python3 decide_l1066.py   -> decide_l1066.tsv
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import score as S

T = ('2077_L10', 66)
REVERT = {('2077_L11', 10), ('2077_L11', 23)}


def ctx(toks, al, text, i, grades):
    hidx = [k for k, t in enumerate(toks) if t[3] in grades]
    left = [k for k in hidx if k < i][-3:]; right = [k for k in hidx if k > i][:3]
    out = []
    for k in left + right:
        got = text[al[k]] if al[k] is not None else '-'
        out.append((toks[k][0], toks[k][1], toks[k][4], toks[k][3], got, got in toks[k][2]))
    return out


def main():
    e77 = S.entries_2077()
    e78 = {}
    with open(os.path.join(S.HERE, 'nota2078.tsv')) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            e78[r['entry'].strip()] = S.norm(r['text'])
    toks, text = e77['q'], e78['b']
    variants = {'A_as_stated': (toks, ('H',)), 'B_C_counted': (toks, ('H', 'C'))}
    gt = [(t[0], t[1], frozenset('n'), 'H', 'n') if (t[0], t[1]) in REVERT else t for t in toks]
    # variant C of decide_l1121.py (L11:10/:23 reverted) kept: it does not touch L10:66's context
    variants['C_gaps45_state'] = (gt, ('H',))
    rows = []
    for name, (tk, grades) in variants.items():
        _, _, al = S.stat(tk, text)
        i = next(k for k, t in enumerate(tk) if (t[0], t[1]) == T)
        got = text[al[i]] if al[i] is not None else '-'
        c = ctx(tk, al, text, i, grades)
        ok_ctx = len(c) >= 2 and all(x[5] for x in c)
        ok_val = tk[i][3] == 'U' or got in tk[i][2]   # clause (i) binds M only (prereg text; score.py line 161)
        cs = ' '.join(f'{l[5:]}:{p}={v}({g})->{a}{"" if m else "X"}' for l, p, v, g, a, m in c)
        rows.append((name, tk[i][4], tk[i][3], got, 'yes' if ok_val else 'no', 'yes' if ok_ctx else 'no',
                     'APPLY' if ok_val and ok_ctx else 'keep', cs))
    with open(os.path.join(S.HERE, 'decide_l1066.tsv'), 'w') as f:
        f.write('variant\tvalue\tgrade\taligned_2078\tclause_i\tclause_ii\taction\tcontext\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
            print('\t'.join(r))


if __name__ == '__main__':
    main()
