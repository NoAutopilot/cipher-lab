#!/usr/bin/env python3
"""EST-REG (14 Oct 2026): design diff of the Brasset key DECODE 9431 (keys_decode/9431_key.tsv) against the published
Clair 421 Brasset-Mazarin cipher of 1649 (clair421_published.tsv, Tomokiyo after Lasry). Counts only; says nothing about
whether either key reads the Clair 575 letter. Null: 421's syllable codes permuted among its syllables (seeded).
  python3 diff_421.py            print the report
  python3 diff_421.py --check    exit 1 if diff_421.txt is stale (rule 7)"""
import random, re, sys, unicodedata
from pathlib import Path
HERE = Path(__file__).resolve().parent
ORDER = {'plain': 0, 'bar': 1, 'dot': 2, 'caret': 3, 'prime': 0, 'overbar': 1, 'umlaut': 2, 'unread': 9}


def fold(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn').lower()
    return re.sub(r'[^a-z ]', '', s.replace('v', 'u').replace('j', 'i').replace('y', 'i')).strip()


def load(name):
    out = []
    for l in (HERE / name).read_text(encoding='utf-8').splitlines():
        if l.startswith('#') or l.startswith('code\t') or not l.strip():
            continue
        c = l.split('\t')
        if c[1] in ('sign', 'capital') or c[3] in ('blank', 'null', 'special', 'letter'):
            continue
        out.append((int(re.match(r'\d+', c[0]).group()), c[1], fold(c[2]), c[3]))
    return out


def monotone_share(rows):
    """share of adjacent pairs (series order, code) whose folded values are in alphabetical order"""
    s = sorted(rows, key=lambda r: (ORDER[r[1]], r[0]))
    pairs = [(a[2], b[2]) for a, b in zip(s, s[1:]) if a[1] == b[1]]
    return sum(a <= b for a, b in pairs) / len(pairs), len(pairs)


def report():
    k = load('9431_key.tsv')
    p = load('clair421_published.tsv')
    out = []
    ks = {v: (c, s) for c, s, v, kind in k if kind == 'syllable' or (len(v) == 2 and kind != 'nomenclator')}
    ps = {v: (c, s) for c, s, v, kind in p if kind == 'syllable' and len(v) == 2}
    shared = sorted(set(ks) & set(ps))
    same_num = [v for v in shared if ks[v][0] == ps[v][0]]
    out.append(f'syllables: 9431 {len(ks)}, Clair 421 {len(ps)}, shared {len(shared)}; same code number {len(same_num)} {same_num}')
    rng = random.Random(0)
    codes = [ps[v][0] for v in shared]
    null = []
    for _ in range(2000):
        rng.shuffle(codes)
        null.append(sum(ks[v][0] == c for v, c in zip(shared, codes)))
    null.sort()
    out.append(f'  null (421 syllable codes permuted, 2000 draws): mean {sum(null)/len(null):.2f}, p95 {null[int(.95*len(null))]}')
    # series pairing: for each 421 series, the 9431 series its shared syllables fall in
    for ser in ('prime', 'overbar', 'umlaut'):
        got = {}
        for v in shared:
            if ps[v][1] == ser:
                got[ks[v][1]] = got.get(ks[v][1], 0) + 1
        out.append(f'  421 {ser} syllables fall in 9431 series {dict(sorted(got.items()))}')
    kw = {v for c, s, v, kind in k if kind == 'nomenclator' or len(v) > 2}
    pw = {v for c, s, v, kind in p if kind == 'word'}
    sw = sorted(kw & pw)
    out.append(f'words: 9431 {len(kw)}, Clair 421 (legible subset) {len(pw)}, shared vocabulary {len(sw)} {sw}')
    kc = {v: c for c, s, v, kind in k}
    same = [v for v in sw if kc[v] == next(c for c, s, w, kd in p if w == v)]
    out.append(f'  shared words at the same code number: {len(same)} {same}')
    for name, rows in (('9431', k), ('Clair 421', [r for r in p if r[1] != 'unread'])):
        m, n = monotone_share(rows)
        out.append(f'alphabetical order within a series ({name}): {m:.3f} of {n} adjacent pairs')
    rng2 = random.Random(1)
    vals = [r[2] for r in k]
    nulls = []
    for _ in range(200):
        rng2.shuffle(vals)
        nulls.append(monotone_share([(r[0], r[1], v, r[3]) for r, v in zip(k, vals)])[0])
    nulls.sort()
    out.append(f'  null (9431 values shuffled, 200 draws): mean {sum(nulls)/len(nulls):.3f}, p95 {nulls[int(.95*len(nulls))]:.3f}')
    ranges = {}
    for name, rows in (('9431', k), ('Clair 421', p)):
        cs = [r[0] for r in rows]
        ranges[name] = (min(cs), max(cs))
    out.append(f'code ranges (non-sign rows): {ranges}')
    return '\n'.join(out) + '\n'


if __name__ == '__main__':
    text = report()
    f = HERE / 'diff_421.txt'
    if '--check' in sys.argv:
        ok = f.exists() and f.read_text() == text
        print('diff_421.txt current' if ok else 'diff_421.txt STALE')
        sys.exit(0 if ok else 1)
    f.write_text(text)
    sys.stdout.write(text)
