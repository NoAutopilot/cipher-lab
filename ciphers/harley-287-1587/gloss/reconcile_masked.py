#!/usr/bin/env python3
"""RUN1-HAR (4 Oct 2026): mechanical reconciliation of the two gloss-masked blind passes of f.84r (PREREG_masked.md).
No arbitration by eye: per band the two token strings are aligned with difflib; agreed tokens are kept, the l/p naming
split goes to p (A2-HAR7's rule), every other split or one-sided token becomes '?'. A word divider '/' is kept where both
passes have one at the aligned position. Gloss column copied from gloss_pairs.tsv (f84r rows).
err_2reader = (token splits + one-sided tokens) / aligned token positions (word dividers excluded).
    python3 reconcile_masked.py [--check]   # writes gloss_pairs_masked.tsv; --check exits 1 if it is stale
"""
import csv, difflib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))

def read(p):
    rows = {}
    for line in open(os.path.join(HERE, p), encoding='utf-8'):
        f = line.rstrip('\n').split('\t')
        if len(f) >= 3 and f[0] == 'f84r':
            rows[f[1]] = f[2].split()
    return rows

def split_words(toks):
    """tokens -> list of (sign, word_end_after) dropping '/'"""
    out = []
    for t in toks:
        if t == '/':
            if out:
                out[-1] = (out[-1][0], True)
        else:
            out.append((t, False))
    return out

def main():
    A, B = read('passA_masked.tsv'), read('passB_masked.tsv')
    gloss = {r['band']: r for r in csv.DictReader(open(os.path.join(HERE, 'gloss_pairs.tsv'), encoding='utf-8'), delimiter='\t')
             if r['page'] == 'f84r'}
    out = ['page\tband\tpair\tgloss\tcipher\tnotes']
    pos = dis = lp = 0
    for band in sorted(gloss):
        a, b = split_words(A.get(band, [])), split_words(B.get(band, []))
        sa, sb = [x[0] for x in a], [x[0] for x in b]
        res = []
        agree = splits = ones = 0
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, sa, sb, autojunk=False).get_opcodes():
            if op == 'equal':
                for k in range(i2 - i1):
                    res.append((sa[i1 + k], a[i1 + k][1] and b[j1 + k][1])); agree += 1
            elif op == 'replace' and i2 - i1 == j2 - j1:
                for k in range(i2 - i1):
                    x, y = sa[i1 + k], sb[j1 + k]
                    if {x, y} == {'l', 'p'}:
                        res.append(('p', a[i1 + k][1] and b[j1 + k][1])); lp += 1; agree += 1
                    else:
                        res.append(('?', a[i1 + k][1] and b[j1 + k][1])); splits += 1
            else:
                n = max(i2 - i1, j2 - j1)
                for k in range(n):
                    res.append(('?', False))
                splits += min(i2 - i1, j2 - j1); ones += abs((i2 - i1) - (j2 - j1))
        n_pos = agree + splits + ones
        pos += n_pos; dis += splits + ones
        toks = []
        for s, end in res:
            toks.append(s)
            if end:
                toks.append('/')
        while toks and toks[-1] == '/':
            toks.pop()
        out.append('\t'.join(['f84r', band, '1', gloss[band]['gloss'], ' '.join(toks),
                              'masked: %d agreed (%d l/p->p), %d split, %d one-sided' % (agree, lp, splits, ones)]))
    text = '\n'.join(out) + '\n'
    summary = 'err_2reader (masked) = %d / %d = %.3f' % (dis, pos, dis / pos if pos else 0)
    path = os.path.join(HERE, 'gloss_pairs_masked.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path, encoding='utf-8').read() == text
        print('check ' + ('ok' if ok else 'STALE')); sys.exit(0 if ok else 1)
    open(path, 'w', encoding='utf-8').write(text)
    print(summary)

if __name__ == '__main__':
    main()
