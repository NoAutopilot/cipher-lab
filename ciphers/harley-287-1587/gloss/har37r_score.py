#!/usr/bin/env python3
"""HAR-37R: score Bourdeau's needham1587 pigpen key against the f.37r (R8478) interlinear glosses.

Gate and normalisation are fixed in ../PREREG-HAR-37R.md (pushed before any read). Inputs (tx/):
  f37r_P1.tsv, f37r_P2.tsv  two blind Sonnet cipher passes   (run<TAB>tokens<TAB>note)
  f37r_R.tsv                blind reconcile of P1/P2          (same format)
  f37r_G.tsv                blind gloss pass                  (run<TAB>gloss<TAB>note; NONE = no gloss)
Key: github.com/dbourdeau/cyphersolver targets/needham1587/decode.py (commit 0445769, MIT), restated here
unchanged: shapes J U L / C O F / N 7 D; plain a-i, dot below k-s, dot inside t u w x y z.
Output: gloss/har37r_score.tsv (per run) and a summary on stdout. --check exits 1 if the committed tsv is stale.
"""
import random, re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
TX = os.path.join(HERE, '..', 'tx')
SHAPES = 'J U L C O F N 7 D'.split()
KEY = {}
for i, s in enumerate(SHAPES):
    KEY[s] = 'abcdefghi'[i]
    KEY[s + '.'] = 'klmnopqrs'[i]
    if i < 6:
        KEY[s + ':'] = 'tuwxyz'[i]

ABBR = [(r'\blo\.', 'lord'), (r'\bl\.', 'lord'), (r'\bmr\b', 'master'), (r'\bsr\b', 'sir'),
        (r'&', 'and'), (r'\byt\b', 'that'), (r'\bye\b', 'the')]


def norm(s):
    s = s.lower()
    s = re.sub(r'\[[^\]]*\]', '', s)          # illegible markers dropped
    for a, b in ABBR:
        s = re.sub(a, b, s)
    s = re.sub(r'[^a-z]', '', s)
    s = s.replace('j', 'i').replace('v', 'u').replace('y', 'i')
    return re.sub(r'(.)\1+', r'\1', s)


def decode(tokens):
    out = []
    for t in tokens.split():
        if t == '|':
            continue
        t = t.rstrip('?')
        out.append(KEY.get(t, '?'))
    return ''.join(out)


def nsigns(tokens):
    return sum(1 for t in tokens.split() if t != '|')


def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def sim(a, b):
    a = a.replace('?', '')
    if not a or not b:
        return 0.0
    return 1 - lev(a, b) / max(len(a), len(b))


def load(name):
    d = {}
    p = os.path.join(TX, name)
    for line in open(p, encoding='utf8'):
        if not line.strip() or line.startswith('#') or line.startswith('run\t'):
            continue
        f = line.rstrip('\n').split('\t')
        d[f[0]] = f[1] if len(f) > 1 else ''
    return d


def score(cipher, gloss, runs):
    D = [norm(decode(cipher[r])) for r in runs]
    G = [norm(gloss[r]) for r in runs]
    real = [sim(d, g) for d, g in zip(D, G)]
    S = sum(real) / len(real)
    rng = random.Random(37)
    null = []
    for _ in range(1000):
        Gp = G[:]
        rng.shuffle(Gp)
        null.append(sum(sim(d, g) for d, g in zip(D, Gp)) / len(D))
    null.sort()
    p95 = null[949]
    frac = sum(1 for x in null if x >= S) / len(null)
    return S, p95, frac, real, D, G


def main():
    P1, P2, G = (load(f) for f in ('f37r_P1.tsv', 'f37r_P2.tsv', 'f37r_G.tsv'))
    # HAR-37R: the reconcile unit was not run (P1/P2 agreement far below any usable level, cap rule);
    # R is absent, so only the pre-registered per-pass checks are computed and K1 is not computable.
    R = load('f37r_R.tsv') if os.path.exists(os.path.join(TX, 'f37r_R.tsv')) else None
    base = R if R is not None else P1
    runs = [r for r in sorted(base) if r in G and G[r].strip().upper() != 'NONE'
            and nsigns(base[r]) >= 3 and len(norm(G[r])) >= 3]
    rows, lines = [], []
    res = {}
    sets = (('R', R), ('P1', P1), ('P2', P2)) if R is not None else (('P1', P1), ('P2', P2))
    for lab, c in sets:
        rr = [r for r in runs if r in c]
        res[lab] = score(c, G, rr) + (rr,)
    first = sets[0][0]
    S, p95, frac, real, D, Gn, rr = res[first]
    R = R if R is not None else P1
    # reader agreement: share of signs with the same shape+mark (marks of '?' stripped), position by position
    tot = same = 0
    for r in sorted(P1):
        a = [t.rstrip('?') for t in P1[r].split() if t != '|']
        b = [t.rstrip('?') for t in P2.get(r, '').split() if t != '|']
        tot += max(len(a), len(b))
        same += sum(1 for x, y in zip(a, b) if x == y)
        lines.append('agree %s: P1 %d signs, P2 %d signs, same-position equal %d' % (r, len(a), len(b), sum(1 for x, y in zip(a, b) if x == y)))
    lines.append('reader agreement P1 vs P2 (positional, all runs): %d/%d = %.3f' % (same, tot, same / tot if tot else 0))
    for r, s, d, g in zip(rr, real, D, Gn):
        agreed = P1.get(r, '').split() == P2.get(r, '').split()
        cls = 'agree' if s >= 0.75 else ('conflict' if s < 0.50 and agreed else 'unsettled')
        rows.append('\t'.join([r, decode(R[r]), d, G[r], g, '%.3f' % s, 'P1=P2' if agreed else 'P1!=P2', cls]))
    out = 'run\tdecode_raw\tdecode_norm\tgloss\tgloss_norm\tsim\treaders\tclass\n' + '\n'.join(rows) + '\n'
    for lab in [l for l, _ in sets]:
        S_, p_, f_ = res[lab][:3]
        lines.append('%s: S=%.3f null p95=%.3f frac(null>=S)=%.3f n=%d' % (lab, S_, p_, f_, len(res[lab][6])))
    if 'R' in res:
        k1 = res['R'][0] >= 0.80 and res['R'][0] > res['R'][1] and all(res[l][0] > res[l][1] for l in ('P1', 'P2'))
        lines.append('K1 %s' % ('PASS' if k1 else 'FAIL'))
    else:
        lines.append('K1 not computable (no reconcile; per-pass rows below use P1 as the decode column)')
    target = os.path.join(HERE, 'har37r_score.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(target) and open(target, encoding='utf8').read() == out
        print('\n'.join(lines))
        print('check: ' + ('OK' if ok else 'STALE'))
        sys.exit(0 if ok else 1)
    open(target, 'w', encoding='utf8').write(out)
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
