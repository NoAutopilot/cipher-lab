#!/usr/bin/env python3
"""MAT-154 (15 Oct 2026), per o154/PREREG-MAT-154.md.

  agree               reads o154/answers_r1.tsv + answers_r2.tsv (47 f.154 `o` tokens), prints raw agreement and Cohen's kappa
                      (A/B on tokens both called A or B -- gating, >= 0.6 and >= 24 such tokens; A/B/X over all 47 -- reported),
                      writes o154/answers_cons.tsv (both A -> A, both B -> B, else X) and o154/agree.tsv; exit 0 gate pass, 3 fail.
  build OUTDIR        a decode_key.py-ready copy of the 28 f154 lines of ciphertext.txt, consensus `o` -> oA / oB (unkeyed), X stays o;
                      key.tsv + decode.json copied unchanged.
Usage: python3 o154/make154.py agree | build OUTDIR"""
import collections, csv, os, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)

def load(f):
    return {r['id']: (r['shape'].strip().upper() or 'X') for r in csv.DictReader(open(os.path.join(HERE, f)), delimiter='\t')}

def kappa(pairs, cats):
    n = len(pairs)
    if not n: return float('nan')
    po = sum(a == b for a, b in pairs) / n
    pe = sum((sum(a == c for a, _ in pairs) / n) * (sum(b == c for _, b in pairs) / n) for c in cats)
    return (po - pe) / (1 - pe) if pe < 1 else float('nan')

def tokens():
    return list(csv.DictReader(open(os.path.join(HERE, 'tokens154.tsv')), delimiter='\t'))

if __name__ == '__main__':
    if sys.argv[1:2] == ['agree']:
        r1, r2 = load('answers_r1.tsv'), load('answers_r2.tsv'); ids = [t['id'] for t in tokens()]
        a = [r1.get(i, 'X') if r1.get(i, 'X') in 'AB' else 'X' for i in ids]
        b = [r2.get(i, 'X') if r2.get(i, 'X') in 'AB' else 'X' for i in ids]
        both = [(x, y) for x, y in zip(a, b) if x in 'AB' and y in 'AB']
        kab, kall = kappa(both, 'AB'), kappa(list(zip(a, b)), 'ABX')
        cons = [x if x == y and x in 'AB' else 'X' for x, y in zip(a, b)]
        gate = kab >= 0.6 and len(both) >= 24
        with open(os.path.join(HERE, 'answers_cons.tsv'), 'w') as f:
            f.write('id\tshape\tr1\tr2\n')
            for i, c, x, y in zip(ids, cons, a, b): f.write(f'{i}\t{c}\t{x}\t{y}\n')
        lines = [f"r1 A/B/X {collections.Counter(a)}", f"r2 A/B/X {collections.Counter(b)}",
                 f"both A/B: n {len(both)}, agree {sum(x == y for x, y in both)}, kappa {kab:.3f}",
                 f"all 47 A/B/X: agree {sum(x == y for x, y in zip(a, b))}, kappa {kall:.3f}",
                 f"consensus: {collections.Counter(cons)}", f"gate K (kappa A/B >= 0.6 and n >= 24): {'PASS' if gate else 'FAIL'}"]
        open(os.path.join(HERE, 'agree.tsv'), 'w').write('\n'.join(lines) + '\n'); print('\n'.join(lines))
        sys.exit(0 if gate else 3)
    elif sys.argv[1:2] == ['build']:
        out = sys.argv[2]; os.makedirs(out, exist_ok=True)
        cons = {r['id']: r['shape'] for r in csv.DictReader(open(os.path.join(HERE, 'answers_cons.tsv')), delimiter='\t')}
        lab = {(t['line'], int(t['position'])): cons.get(t['id'], 'X') for t in tokens()}
        for f in ('decode.json', 'key.tsv'): shutil.copy(os.path.join(T, f), os.path.join(out, f))
        c = collections.Counter()
        with open(os.path.join(out, 'ciphertext.txt'), 'w') as fh:
            for l in open(os.path.join(T, 'ciphertext.txt')):
                p = l.rstrip('\n').split('\t')
                if not p[0].startswith('f154-'): continue
                v = p[1].split()
                for i, s in enumerate(v, 1):
                    if s == 'o' and lab.get((p[0], i), 'X') in 'AB': v[i - 1] = 'o' + lab[(p[0], i)]
                c.update(v)
                fh.write(f"{p[0]}\t{' '.join(v)}\t\n")
        print('built', out, 'tokens', sum(c.values()), 'o', c['o'], 'oA', c['oA'], 'oB', c['oB'], 'n', c['n'], 'c', c['c'], 's', c['s'], 'e', c['e'])
    else:
        print(__doc__); sys.exit(2)
