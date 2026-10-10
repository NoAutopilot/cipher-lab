#!/usr/bin/env python3
"""THUR-BM leave-one-letter-out gate (PREREG-THURBM.md). Blank-Marshall letters, Birch 1742 vol 6.

python3 bm_gate.py [--check]
Reads bm/passes/<line>_B<k>.tsv (row pos kind token gloss; blind Sonnet passes, gloss never reconciled),
writes bm/<line>_pairs_B<k>.tsv (folder pairs format), trains a key per fold with tools/interlinear_align.py align
(default --floor 100) on the three training letters of pass k, scores the held-out letter of pass k against its own
gloss, with a shuffled-key control (200 draws, seeds 0..199). Writes bm/gate.tsv; --check exits 1 if stale.
"""
import csv, os, random, subprocess, sys, tempfile, collections
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
LETTERS = ['l40469', 'l65889', 'l77385', 'l89881']
PASSES = ['B1', 'B2']

def norm(s):
    s = s.lower().replace('ſ', 's')
    s = ''.join(c for c in s if c.isalpha())
    return s.replace('j', 'i').replace('v', 'u')

def read_pass(L, k):
    rows = list(csv.DictReader(open(os.path.join(H, 'passes', f'{L}_{k}.tsv')), delimiter='\t'))
    for r in rows:
        r['token'] = (r.get('token') or '').strip().rstrip('|')
        r['gloss'] = (r.get('gloss') or '').strip().rstrip('~')
    return rows

def write_pairs(L, k, rows):
    byrow = collections.OrderedDict()
    for r in rows:
        byrow.setdefault(r['row'], []).append(r)
    p = os.path.join(H, f'{L}_pairs_{k}.tsv')
    with open(p, 'w') as f:
        f.write('plain_line\tplain_raw\tcipher_line\tcipher_raw\n')
        for rid, rs in byrow.items():
            plain = '  '.join(r['gloss'] for r in rs if r['kind'] == 'N' and r['gloss'])
            ciph = '  '.join(r['token'] for r in rs if r['token'] and '?' not in r['token'])
            if not any(r['kind'] == 'N' for r in rs):
                continue
            f.write(f'{L}r{rid}g\t{plain}\t{L}r{rid}\t{ciph}\n')
    return p

def train(pair_files):
    with tempfile.TemporaryDirectory() as d:
        cat = os.path.join(d, 'pairs.tsv')
        with open(cat, 'w') as f:
            f.write('plain_line\tplain_raw\tcipher_line\tcipher_raw\n')
            for p in pair_files:
                f.writelines(open(p).readlines()[1:])
        al, ky = os.path.join(d, 'a.tsv'), os.path.join(d, 'k.tsv')
        subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'interlinear_align.py'), 'align', cat, al, ky],
                       check=True, capture_output=True)
        key = {}
        for r in csv.DictReader(open(ky), delimiter='\t'):
            v = r.get('value'); m = r.get('meaning')
            if v and m and v.isdigit():
                key[int(v)] = norm(m)
    return key

def score(key, rows):
    tot = {'let': [0, 0], 'code': [0, 0]}; glossed = 0
    for r in rows:
        if r['kind'] != 'N' or not r['token'].isdigit() or not r['gloss']:
            continue
        glossed += 1
        v = int(r['token']); c = 'let' if v < 100 else 'code'
        if v in key:
            tot[c][1] += 1
            tot[c][0] += key[v] == norm(r['gloss'])
    return tot, glossed

def agree(t):
    n = t['let'][1] + t['code'][1]
    return (t['let'][0] + t['code'][0]) / n if n else float('nan')

def main():
    out = ['pass\theld_out\tglossed\tcovered\tcoverage\tagree_letters\tn_letters\tagree_codes\tn_codes\tagree_all\tshuffle_mean\tshuffle_p95\tabove_p95']
    for k in PASSES:
        R = {L: read_pass(L, k) for L in LETTERS}
        P = {L: write_pairs(L, k, R[L]) for L in LETTERS}
        pooled = [0, 0]; allabove = True
        for L in LETTERS:
            key = train([P[x] for x in LETTERS if x != L])
            t, g = score(key, R[L]); a = agree(t)
            codes, vals = list(key), list(key.values()); sh = []
            for s in range(200):
                vv = vals[:]; random.Random(s).shuffle(vv)
                sh.append(agree(score(dict(zip(codes, vv)), R[L])[0]))
            sh.sort(); p95 = sh[int(0.95 * len(sh))]
            cov = t['let'][1] + t['code'][1]
            pooled[0] += t['let'][0] + t['code'][0]; pooled[1] += cov
            ab = a > p95; allabove &= ab
            f = lambda x, y: f'{x/y:.3f}' if y else 'na'
            out.append(f"{k}\t{L}\t{g}\t{cov}\t{f(cov,g)}\t{f(*t['let'])}\t{t['let'][1]}\t{f(*t['code'])}\t{t['code'][1]}\t{a:.3f}\t{sum(sh)/len(sh):.3f}\t{p95:.3f}\t{ab}")
        pa = pooled[0] / pooled[1]
        out.append(f"{k}\tPOOLED\t\t{pooled[1]}\t\t\t\t\t\t{pa:.3f}\t\t\t{'PASS' if allabove and pa >= 0.70 else 'FAIL'}")
    txt = '\n'.join(out) + '\n'
    p = os.path.join(H, 'gate.tsv')
    if '--check' in sys.argv:
        sys.exit(0 if open(p).read() == txt else 1)
    open(p, 'w').write(txt); print(txt)
main()
