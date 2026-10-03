#!/usr/bin/env python3
"""GAPS2-matignon-mayenne-1586 (3 Oct 2026, account-4): score the per-leaf M-only beam's M choices against Bourdeau's
per-line decoder output, behind mu_leaf_agree_prereg.md (pushed before this ran, c26ff40d).

Agreement with another modern reading, not accuracy. Reference: sources/cyphersolver/2026-10-03/matignon1586/
(MIT, Bourdeau HEAD 4d32ec9). Run from the repository root:
  python3 ciphers/matignon-mayenne-1586/mu_leaf_agree.py [--check]
Writes ciphers/matignon-mayenne-1586/mu_leaf_agree.json; --check exits 1 if it is stale.
"""
import sys, json, random, re, unicodedata, collections
from pathlib import Path
from multiprocessing import Pool
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(ROOT / 'tools'))
import mu_beam as mb  # noqa: E402
import mu_leaf_beam as lb  # noqa: E402

REF = ROOT / 'sources/cyphersolver/2026-10-03/matignon1586'
LEAVES = {'f143r': 'reading_f143.txt', 'f143v': 'reading_f143v.txt', 'f154': 'reading_f154.txt',
          'f173': 'reading_f173.txt'}
SEEDS = (1, 2, 3)
NSHUF = 20


def norm(t):
    t = ''.join(c for c in unicodedata.normalize('NFD', t) if unicodedata.category(c) != 'Mn').lower()
    t = t.replace('v', 'u').replace('j', 'i').replace('w', 'u').replace('k', 'c')
    return re.sub(r'[^a-z]', '', t)


def ref_lines(leaf):
    out = {}
    for ln in (REF / LEAVES[leaf]).read_text().splitlines():
        m = re.match(r'^(\d+) (.*)$', ln)
        if m:
            out[int(m.group(1))] = norm(m.group(2))
    return [out.get(i + 1, '') for i in range(max(out))]


def pieces(L, ch):
    """per token: (pos, kind, normalised letters) in original order, U dropped."""
    out = []
    for pos, (k, s, c) in enumerate(L):
        if k == 'U':
            continue
        v = c[ch.get(pos, 0)] if k == 'M' else c[0]
        out.append((pos, k, norm(v) if v != mb.NULL else ''))
    return out


def align(a, b):
    """Levenshtein alignment; returns for each index of a the aligned index of b or None."""
    n, m = len(a), len(b)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + (a[i-1] != b[j-1]))
    i, j, amap = n, m, [None] * n
    while i > 0 and j > 0:
        if D[i][j] == D[i-1][j-1] + (a[i-1] != b[j-1]):
            amap[i-1] = j - 1; i -= 1; j -= 1
        elif D[i][j] == D[i-1][j] + 1:
            i -= 1
        else:
            j -= 1
    return amap


def agree(lines, mch, refs):
    ok = n = 0
    for L, ch, r in zip(lines, mch, refs):
        pc = pieces(L, ch)
        s = ''.join(p[2] for p in pc)
        amap = align(s, r)
        i = 0
        for pos, k, v in pc:
            if k == 'M':
                n += 1
                ok += bool(v) and all(amap[i + q] is not None and r[amap[i + q]] == v[q] for q in range(len(v)))
            i += len(v)
    return ok, n


def shuffled_choices(lm, lines, seed):
    rnd = random.Random(seed)
    perms = [rnd.sample(range(len(L)), len(L)) for L in lines]
    mch = lb.beam(lm, [[L[i] for i in p] for L, p in zip(lines, perms)])
    return [{p[q]: c for q, c in ch.items()} for ch, p in zip(mch, perms)]


def run_leaf(leaf):
    lm = mb.get_lm()
    target = lb.leaf_lines()[leaf]
    held = mb.words_of(f'{mb.D}/lettresdecatheri02cathuoft_djvu.txt.gz')
    ctl = []
    for seed in SEEDS:
        lines, tl, _ = mb.build_control(target, mb.load_key(), held, seed)
        acc = lambda mch: (sum(ch.get(p, 0) == T_[p] for L, T_, ch in zip(lines, tl, mch)
                               for p, t in enumerate(L) if t[0] == 'M') /
                           sum(1 for L in lines for t in L if t[0] == 'M'))
        b = acc(lb.beam(lm, lines))
        nulls = [acc(shuffled_choices(lm, lines, s)) for s in range(1, NSHUF + 1)]
        first = acc([{} for _ in lines])
        ctl.append(dict(seed=seed, beam=round(b, 4), first=round(first, 4), null_max=round(max(nulls), 4),
                        null_mean=round(sum(nulls) / NSHUF, 4), passed=b > max(nulls)))
    testable = sum(c['passed'] for c in ctl) >= 2 and max(c['first'] for c in ctl) < 0.95
    refs = ref_lines(leaf)
    assert len(refs) == len(target), (leaf, len(refs), len(target))
    bm = lb.beam(lm, target)
    ok_b, n = agree(target, bm, refs)
    ok_f, _ = agree(target, [{} for _ in target], refs)
    nulls, diffs = [], []
    for s in range(1, NSHUF + 1):
        nm = shuffled_choices(lm, target, s)
        nulls.append(agree(target, nm, refs)[0] / n)
        diffs.append(sum(1 for L, a, b in zip(target, bm, nm) for p, t in enumerate(L)
                         if t[0] == 'M' and a.get(p, 0) != b.get(p, 0)))
    A_b, A_f = ok_b / n, ok_f / n
    return dict(leaf=leaf, m_n=n, control=ctl, testable=testable,
                target=dict(A_beam=round(A_b, 4), A_first=round(A_f, 4), A_null_max=round(max(nulls), 4),
                            A_null_mean=round(sum(nulls) / NSHUF, 4),
                            null_choices_differ_min=min(diffs), null_choices_differ_mean=round(sum(diffs) / NSHUF, 1),
                            beam_vs_first_changed=sum(1 for L, a in zip(target, bm) for p, t in enumerate(L)
                                                      if t[0] == 'M' and a.get(p, 0) != 0),
                            passed=A_b > max(nulls) and A_b >= A_f + 0.02))


def main():
    with Pool(4) as p:
        rows = p.map(run_leaf, list(LEAVES))
    testable = [r for r in rows if r['testable']]
    passed = [r for r in testable if r['target']['passed']]
    if len(testable) < 3:
        verdict = 'NON-TEST AT THIS N (fewer than 3 of 4 leaves testable)'
    elif len(passed) >= 3:
        verdict = 'AGREEMENT SIGNAL'
    else:
        verdict = 'NO AGREEMENT SIGNAL'
    out = dict(job='GAPS2-matignon-mayenne-1586', prereg='mu_leaf_agree_prereg.md', reference='Bourdeau 4d32ec9',
               leaves=rows, testable=len(testable), passed=len(passed), verdict=verdict)
    js = json.dumps(out, indent=1, sort_keys=True)
    f = HERE / 'mu_leaf_agree.json'
    if '--check' in sys.argv:
        stale = not f.exists() or f.read_text() != js
        print('STALE' if stale else 'mu_leaf_agree.json current'); sys.exit(1 if stale else 0)
    f.write_text(js)
    for r in rows:
        print(r['leaf'], 'n', r['m_n'], 'ctl', [(c['beam'], c['null_max'], c['first']) for c in r['control']],
              'testable', r['testable'], '| T', r['target'])
    print(verdict, f'testable {len(testable)}/4 passed {len(passed)}')


if __name__ == '__main__':
    main()
