#!/usr/bin/env python3
"""THUR-BM2 seven-letter leave-one-letter-out gate (PREREG-THURBM2.md = PREREG-THURBM.md's rule on a seven-letter pool).

python3 bm_gate7.py [--check]
Reads bm/passes/<line>_B<k>.tsv for the seven glossed Blank-Marshall letters of Birch 1742 vol 6; a gloss word spanning several
groups is on the span's first group with '^' on the rest (l3370 is glossed by words). Writes bm/<line>_pairs_B<k>.tsv for the three
added letters (the four THUR-BM pairs files are rewritten identically by the same rule), trains per fold with
tools/interlinear_align.py align (default --floor 100), scores against the held-out letter's own per-group gloss, shuffled-key
control 200 draws (seeds 0..199). Writes bm/gate7.tsv and bm/key_blankmarshall_7.tsv; --check exits 1 if either is stale.
"""
import csv, os, random, subprocess, sys, tempfile, collections
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
LETTERS = ['l3370', 'l40469', 'l65889', 'l77385', 'l83274', 'l86815', 'l89881']
PASSES = ['B1', 'B2']

def norm(s):
    s = s.lower().replace('ſ', 's')
    s = ''.join(c for c in s if c.isalpha())
    return s.replace('j', 'i').replace('v', 'u')

def read_pass(L, k):
    rows = list(csv.DictReader(open(os.path.join(H, 'passes', f'{L}_{k}.tsv')), delimiter='\t'))
    for r in rows:
        r['token'] = (r.get('token') or '').strip().rstrip('|').rstrip('.')
        r['gloss'] = (r.get('gloss') or '').strip().rstrip('~')
        r['kind'] = (r.get('kind') or '').strip()
    return rows

def answers(rows):
    """Per-group known answer (PREREG-THURBM2): expand '^' spans; return (list of (row, answer or None), excluded count)."""
    N = [r for r in rows if r['kind'] == 'N' and r['token'].isdigit()]
    out, excl, i = [], 0, 0
    while i < len(N):
        r = N[i]; j = i + 1
        while j < len(N) and N[j]['gloss'] == '^':
            j += 1
        span = N[i:j]
        if r['gloss'] in ('', '^'):
            out += [(x, None) for x in span]
        elif len(span) == 1:
            out.append((r, r['gloss']))
        else:
            w = norm(r['gloss'])
            if len(w) == len(span) and all(int(x['token']) < 100 for x in span):
                out += [(x, c) for x, c in zip(span, w)]
            else:
                out += [(x, None) for x in span]; excl += len(span)
        i = j
    return out, excl

def write_pairs(L, k, rows):
    byrow = collections.OrderedDict()
    for r in rows:
        byrow.setdefault(r['row'], []).append(r)
    p = os.path.join(H, f'{L}_pairs_{k}.tsv')
    txt = 'plain_line\tplain_raw\tcipher_line\tcipher_raw\n'
    for rid, rs in byrow.items():
        if not any(r['kind'] == 'N' for r in rs):
            continue
        plain = '  '.join(r['gloss'] for r in rs if r['kind'] == 'N' and r['gloss'] and r['gloss'] != '^')
        ciph = '  '.join(r['token'] for r in rs if r['token'] and '?' not in r['token'] and r['token'] != '*')
        txt += f'{L}r{rid}g\t{plain}\t{L}r{rid}\t{ciph}\n'
    if not os.path.exists(p) or open(p).read() != txt:
        open(p, 'w').write(txt)
    return p

def train(pair_files, raw=False):
    with tempfile.TemporaryDirectory() as d:
        cat = os.path.join(d, 'pairs.tsv')
        with open(cat, 'w') as f:
            f.write('plain_line\tplain_raw\tcipher_line\tcipher_raw\n')
            for p in pair_files:
                f.writelines(open(p).readlines()[1:])
        al, ky = os.path.join(d, 'a.tsv'), os.path.join(d, 'k.tsv')
        subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'interlinear_align.py'), 'align', cat, al, ky],
                       check=True, capture_output=True)
        rows = list(csv.DictReader(open(ky), delimiter='\t'))
    if raw:
        return rows
    return {int(r['value']): norm(r['meaning']) for r in rows if r.get('value', '').isdigit() and r.get('meaning')}

def score(key, ans):
    tot = {'let': [0, 0], 'code': [0, 0]}; glossed = 0
    for r, a in ans:
        if a is None:
            continue
        glossed += 1
        v = int(r['token']); c = 'let' if v < 100 else 'code'
        if v in key:
            tot[c][1] += 1
            tot[c][0] += key[v] == norm(a)
    return tot, glossed

def agree(t):
    n = t['let'][1] + t['code'][1]
    return (t['let'][0] + t['code'][0]) / n if n else float('nan')

def main():
    out = ['pass\theld_out\tglossed\texcluded\tcovered\tcoverage\tagree_letters\tn_letters\tagree_codes\tn_codes\tagree_all\tshuffle_mean\tshuffle_p95\tabove_p95']
    fullkeys = {}
    for k in PASSES:
        R = {L: read_pass(L, k) for L in LETTERS}
        P = {L: write_pairs(L, k, R[L]) for L in LETTERS}
        pooled = [0, 0]; allabove = True
        for L in LETTERS:
            key = train([P[x] for x in LETTERS if x != L])
            ans, ex = answers(R[L])
            t, g = score(key, ans); a = agree(t)
            codes, vals = list(key), list(key.values()); sh = []
            for s in range(200):
                vv = vals[:]; random.Random(s).shuffle(vv)
                sh.append(agree(score(dict(zip(codes, vv)), ans)[0]))
            sh.sort(); p95 = sh[int(0.95 * len(sh))]
            cov = t['let'][1] + t['code'][1]
            pooled[0] += t['let'][0] + t['code'][0]; pooled[1] += cov
            ab = a > p95; allabove &= ab
            f = lambda x, y: f'{x/y:.3f}' if y else 'na'
            out.append(f"{k}\t{L}\t{g}\t{ex}\t{cov}\t{f(cov,g)}\t{f(*t['let'])}\t{t['let'][1]}\t{f(*t['code'])}\t{t['code'][1]}\t{a:.3f}\t{sum(sh)/len(sh):.3f}\t{p95:.3f}\t{ab}")
        pa = pooled[0] / pooled[1]
        out.append(f"{k}\tPOOLED\t\t\t{pooled[1]}\t\t\t\t\t\t{pa:.3f}\t\t\t{'PASS' if allabove and pa >= 0.70 else 'FAIL'}")
        fullkeys[k] = {int(r['value']): r for r in train([P[x] for x in LETTERS], raw=True) if r.get('value', '').isdigit() and r.get('meaning')}
    gate = '\n'.join(out) + '\n'
    kl = ['value\tmeaning\tgrade\tmeaning_B1\tcount_B1\tmeaning_B2\tcount_B2']
    cnt = lambda r: r.get('count', r.get('n', '')) if r else ''
    for v in sorted(set(fullkeys['B1']) | set(fullkeys['B2'])):
        a, b = fullkeys['B1'].get(v), fullkeys['B2'].get(v)
        ma, mb = (a or {}).get('meaning', ''), (b or {}).get('meaning', '')
        if a and b and norm(ma) == norm(mb):
            m, gr = ma, 'C'
        else:
            m, gr = f'{ma}|{mb}', 'M'
        kl.append(f'{v}\t{m}\t{gr}\t{ma}\t{cnt(a)}\t{mb}\t{cnt(b)}')
    key = '\n'.join(kl) + '\n'
    gp, kp = os.path.join(H, 'gate7.tsv'), os.path.join(H, 'key_blankmarshall_7.tsv')
    if '--check' in sys.argv:
        sys.exit(0 if open(gp).read() == gate and open(kp).read() == key else 1)
    open(gp, 'w').write(gate); open(kp, 'w').write(key); print(gate)
main()
