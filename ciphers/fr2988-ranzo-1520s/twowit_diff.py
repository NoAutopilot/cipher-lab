#!/usr/bin/env python3
"""Two-witness diff: fr.3019 no.27 (ff.73r-74r, our reconciled read) vs fr.2988 f.2r-v (Bourdeau's c006+c007).

  python3 twowit_diff.py [--bourdeau DIR] [--check]

Reads fr3019_no27_tokens.tsv (line, pos, token, conf, why) and Bourdeau's ranzo_c006.txt + ranzo_c007.txt
(github.com/dbourdeau/cyphersolver targets/vasto1527/n20/, MIT; default DIR = the copies in bourdeau/), aligns the two
token streams with difflib on whole tokens (bare '/' and '|' dropped, pre-registration item 1), and writes twowit_diff.tsv:
one row per disagreement (op, fr3019 line/pos/token, Bourdeau index/token) with the settle columns (class, note) carried
over from the existing file when the same (op, fr3019 positions, Bourdeau positions) row is already there. Prints the
agreement figure, and writes fr3019_no27_settled.tsv (the reconciled read with the R3019/R2 rows replaced
by the settled sign). --check exits 1 if the committed twowit_diff.tsv rows (ignoring settle columns) differ from a fresh run.
"""
import argparse, csv, difflib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKIP = {'/', '|', '/.', ''}


def bourdeau(d):
    toks = []
    for name in ('ranzo_c006.txt', 'ranzo_c007.txt'):
        for ln in open(os.path.join(d, name)):
            if ln.startswith('#'):
                continue
            toks += [t for t in ln.split() if t not in SKIP]
    return toks


def ours(path):
    rows = [r for r in csv.DictReader(open(path), delimiter='\t') if r['token'] not in SKIP]
    for r in rows:  # a trailing/inner '?' is our reader's uncertainty mark, not part of the sign (row class N)
        r['token'] = r['token'].replace('?', '') or '?'
    return rows


def diff(A, B):
    a = [r['token'] for r in A]
    sm = difflib.SequenceMatcher(None, a, B, autojunk=False)
    out, same = [], 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            same += i2 - i1
            continue
        n = max(i2 - i1, j2 - j1)
        for k in range(n):
            ia, jb = i1 + k, j1 + k
            ra = A[ia] if ia < i2 else None
            prev = A[i1 - 1] if i1 > 0 else None
            out.append(dict(after=f"{prev['line']}:{prev['pos']}" if (ra is None and prev) else '',
                            op=op if (ra is not None and jb < j2) else ('delete' if ra is not None else 'insert'),
                            line=ra['line'] if ra else '', pos=ra['pos'] if ra else '',
                            fr3019=ra['token'] if ra else '-', conf=ra.get('conf', '') if ra else '',
                            b_idx=str(jb) if jb < j2 else '', bourdeau=B[jb] if jb < j2 else '-'))
    return out, same


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--bourdeau', default=os.path.join(HERE, 'bourdeau'))
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    A, B = ours(os.path.join(HERE, 'fr3019_no27_tokens.tsv')), bourdeau(a.bourdeau)
    rows, same = diff(A, B)
    cols = ['op', 'line', 'pos', 'after', 'fr3019', 'conf', 'b_idx', 'bourdeau', 'class', 'note']
    path = os.path.join(HERE, 'twowit_diff.tsv')
    key = lambda r: (r['op'], r['line'], r['pos'], r['b_idx'])
    old = {}
    if os.path.exists(path):
        old = {key(r): r for r in csv.DictReader(open(path), delimiter='\t')}
    for r in rows:
        o = old.get(key(r), {})
        r['class'], r['note'] = o.get('class', ''), o.get('note', '')
    print(f'fr3019 tokens {len(A)}, Bourdeau tokens {len(B)}, equal {same}, disagreement rows {len(rows)}; '
          f'agreement {same}/{max(len(A), len(B))} = {same / max(len(A), len(B)):.3f}')
    if a.check:
        stale = [k for k in map(key, rows) if k not in old] or len(old) != len(rows)
        sys.exit(1 if stale else 0)
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, cols, delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)
    # settled fr.3019 read: our reconciled tokens with every R3019/R2 row replaced by the settled sign
    fix = {(r['line'], r['pos']): r['bourdeau'] for r in rows if r['class'] in ('R3019', 'R2') and r['line']}
    add = {}  # R3019 insert rows: a token our read missed, placed after the fr.3019 token named in 'after'
    for r in rows:
        if r['class'] in ('R3019', 'R2') and r['op'] == 'insert' and r['after']:
            add.setdefault(tuple(r['after'].split(':')), []).append(r['bourdeau'])
    with open(os.path.join(HERE, 'fr3019_no27_settled.tsv'), 'w') as f:
        f.write('line\tpos\ttoken\tsource\n')
        for r in A:
            k = (r['line'], r['pos'])
            f.write(f"{r['line']}\t{r['pos']}\t{fix.get(k, r['token'])}\t{'settled R3019' if k in fix else 'reconciled'}\n")
            for n, t in enumerate(add.get(k, []), 1):
                f.write(f"{r['line']}\t{r['pos']}+{n}\t{t}\tsettled R3019 (missed token; may belong to the next line)\n")


if __name__ == '__main__':
    main()
