#!/usr/bin/env python3
"""BNF-Q7-ERR: align a blind digit pass to the reconciled transcription per line and count S/I/D.

usage: err_measure.py RECONCILED.tsv BLIND.tsv [--adj ADJ.tsv] [--out ops.tsv]

'?' marks (uncertain previous digit) are dropped before alignment; digits only. Alignment: Levenshtein
(unit costs, ties prefer substitution). d = (S+I+D)/len(reconciled); e_hi = Wilson 95% upper bound on d
(PREREG-Q7-T73-ADDENDUM.md rule 1). With --adj (line, rpos, verdict in {rec,blind,unread}) also reports the
adjudicated error of the reconciled text: ops judged 'blind' or 'unread' count against it, 'rec' does not.
Lines present only in BLIND are reported, not scored.
"""
import sys, math, argparse

def load(p):
    d = {}
    for ln in open(p):
        if ln.startswith('#') or ln.startswith('line\t') or not ln.strip(): continue
        a, b = ln.rstrip('\n').split('\t')[:2]
        d[a] = ''.join(c for c in b if c.isdigit())
    return d

def align(r, b):
    n, m = len(r), len(b)
    D = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): D[i][0] = i
    for j in range(m+1): D[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            D[i][j] = min(D[i-1][j-1] + (r[i-1] != b[j-1]), D[i-1][j] + 1, D[i][j-1] + 1)
    ops, i, j = [], n, m
    while i or j:
        if i and j and D[i][j] == D[i-1][j-1] + (r[i-1] != b[j-1]):
            ops.append(('M' if r[i-1] == b[j-1] else 'S', i-1, r[i-1], b[j-1])); i -= 1; j -= 1
        elif i and D[i][j] == D[i-1][j] + 1:
            ops.append(('D', i-1, r[i-1], '-')); i -= 1   # digit in reconciled, absent in blind
        else:
            ops.append(('I', i, '-', b[j-1])); j -= 1     # digit in blind, absent in reconciled (before rpos i)
    return ops[::-1]

def wilson_hi(k, n, z=1.96):
    p = k/n; den = 1 + z*z/n
    return (p + z*z/(2*n) + z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))) / den

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('rec'); ap.add_argument('blind'); ap.add_argument('--adj'); ap.add_argument('--out')
    a = ap.parse_args()
    R, B = load(a.rec), load(a.blind)
    adj = {}
    if a.adj:
        for ln in open(a.adj):
            if ln.startswith('#') or ln.startswith('line\t') or not ln.strip(): continue
            f = ln.rstrip('\n').split('\t'); adj[(f[0], int(f[1]), f[2])] = f[3]
    tot = dict(N=0, M=0, S=0, I=0, D=0); bad = 0; rows = []
    print('line\tN_rec\tN_blind\tM\tS\tI\tD\td')
    for L in sorted(R):
        if L not in B: print(f'{L}\tmissing in blind'); continue
        ops = align(R[L], B[L]); c = dict(M=0, S=0, I=0, D=0)
        for op in ops:
            c[op[0]] += 1
            if op[0] != 'M':
                rows.append((L,) + op)
                v = adj.get((L, op[1], op[0]))
                if v in ('blind', 'unread'): bad += 1
        n = len(R[L]); tot['N'] += n
        for k in c: tot[k] += c[k]
        print(f"{L}\t{n}\t{len(B[L])}\t{c['M']}\t{c['S']}\t{c['I']}\t{c['D']}\t{(c['S']+c['I']+c['D'])/n:.3f}")
    for L in sorted(set(B) - set(R)): print(f'{L}\t-\t{len(B[L])}\tnot in reconciled (not scored)')
    k = tot['S'] + tot['I'] + tot['D']; N = tot['N']
    print(f"TOTAL\tN={N}\tM={tot['M']}\tS={tot['S']}\tI={tot['I']}\tD={tot['D']}\td={k/N:.4f}\te_hi={wilson_hi(k, N):.4f}")
    if a.adj:
        miss = [r for r in rows if (r[0], r[2], r[1]) not in adj]
        print(f"ADJ\terrors_of_reconciled={bad}/{N}\te_adj={bad/N:.4f}\tWilson_hi={wilson_hi(bad, N):.4f}\tunadjudicated={len(miss)}")
    if a.out:
        with open(a.out, 'w') as f:
            f.write('line\top\trpos\trec\tblind\n')
            for r in rows: f.write('\t'.join(map(str, r)) + '\n')

if __name__ == '__main__':
    main()
