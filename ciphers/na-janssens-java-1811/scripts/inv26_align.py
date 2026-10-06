#!/usr/bin/env python3
"""Align the invnr 26 copy of dispatch No.1 (scans 10-11, inv26_reconciled.tsv) against leaf 188 (ciphertext.tsv).

PREREG-R11-JANS26TX.md: Needleman-Wunsch (match +1, mismatch -1, gap -1, whole codes), A = matches / len(leaf 188),
control = 1000 shuffles of leaf 188's order (seeds 0-999). Writes inv26_vs_188.tsv (every aligned position) and
prints the gate numbers. --check exits 1 if inv26_vs_188.tsv is stale.
"""
import csv, random, sys, os
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(fn, col):
    with open(os.path.join(HERE, fn)) as f:
        return [(int(r['line']), int(r['pos']), r[col]) for r in csv.DictReader(f, delimiter='\t')]

def nw(a, b):
    n, m = len(a), len(b)
    S = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): S[i][0] = -i
    for j in range(m + 1): S[0][j] = -j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            S[i][j] = max(S[i-1][j-1] + (1 if a[i-1] == b[j-1] else -1), S[i-1][j] - 1, S[i][j-1] - 1)
    i, j, out = n, m, []
    while i or j:
        if i and j and S[i][j] == S[i-1][j-1] + (1 if a[i-1] == b[j-1] else -1):
            out.append((i-1, j-1)); i -= 1; j -= 1
        elif i and S[i][j] == S[i-1][j] - 1:
            out.append((i-1, None)); i -= 1
        else:
            out.append((None, j-1)); j -= 1
    return out[::-1]

def matches(a, b):
    return sum(1 for i, j in nw(a, b) if i is not None and j is not None and a[i] == b[j])

def main():
    inv = load('inv26_reconciled.tsv', 'digits')
    l188 = load('ciphertext.tsv', 'sign')
    a = [t[2] for t in inv]; b = [t[2] for t in l188]
    rows = []
    for i, j in nw(a, b):
        ia = inv[i] if i is not None else (None, None, '')
        jb = l188[j] if j is not None else (None, None, '')
        kind = 'gap188' if j is None else 'gapinv' if i is None else ('agree' if ia[2] == jb[2] else 'differ')
        rows.append([kind, ia[0] or '', ia[1] or '', ia[2], jb[0] or '', jb[1] or '', jb[2]])
    text = 'kind\tinv_line\tinv_pos\tinv26\tl188_line\tl188_pos\tleaf188\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in rows)
    out = os.path.join(HERE, 'inv26_vs_188.tsv')
    if '--check' in sys.argv:
        ok = open(out).read() == text
        print('inv26_vs_188.tsv', 'ok' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(out, 'w').write(text)
    real = sum(1 for r in rows if r[0] == 'agree')
    ctrl = []
    for s in range(1000):
        bb = b[:]; random.Random(s).shuffle(bb); ctrl.append(matches(a, bb))
    n = len(b)
    print(f'inv26 codes {len(a)}, leaf188 codes {n}; agree {real}, differ {sum(r[0]=="differ" for r in rows)}, '
          f'only-inv26 {sum(r[0]=="gap188" for r in rows)}, only-188 {sum(r[0]=="gapinv" for r in rows)}')
    print(f'A = {real}/{n} = {real/n:.3f}; control mean {sum(ctrl)/len(ctrl)/n:.3f}, max {max(ctrl)/n:.3f}, '
          f'shuffles >= real {sum(c >= real for c in ctrl)}/1000')
    print('GATE', 'PASS' if real / n >= 0.80 and real > max(ctrl) else 'FAIL')

if __name__ == '__main__':
    main()
