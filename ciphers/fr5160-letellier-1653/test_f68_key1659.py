#!/usr/bin/env python3
"""Second-letter test of key_1659 on the f.67 cipher against its f.68r clear text (8 Oct 2026, worker D1A-F68).

Pre-registered in PREREG-D1A-F68.md (pushed before this was run).  key_1659.tsv is used as committed (modal value only); no
f.67 evidence enters the key.  Each of f.67's three cipher stretches is decoded token by token, the decoded letters are
aligned (Needleman-Wunsch, +2/-1/-1) to the matching f.68r stretch, and a token agrees when all its letters align to identical
clear letters.  Control: f.68r words shuffled within each (stretch, manuscript line), 1000 shuffles, seed 20261008.

  python3 test_f68_key1659.py           write f68_key1659_test.tsv (summary) and f68_key1659_codes.tsv (per code)
  python3 test_f68_key1659.py --check   exit 1 if either committed output differs
"""
import csv, io, os, random, re, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
import align_f86 as A

NONSIGN = {',', ';', '.', ':', '—', 'X'}
CUTS = ['parceque sil pouvoit estre', 'que ce qui se dit', 'Cest ce que vous']
SEED, NSHUF = 20261008, 1000


def norm(s):
    return A.norm(s.replace('Madame', 'M.e'))


def f68_words():
    """[(line_no, word)] of f.68r, struck words dropped, interlined kept, with a stretch id 0/1/2 (None = cut words)."""
    words = []
    n = 0
    for line in open('dechiffre_f68.txt', encoding='utf-8'):
        if line.startswith('#'):
            continue
        n += 1
        line = re.sub(r'\[del: [^\]]*\]', ' ', line)
        line = re.sub(r'\[ins: ([^\]]*)\]', r' \1 ', line).replace('[?]', '')
        words += [(n, w) for w in line.split()]
    flat = [w for _, w in words]

    def find(phrase):
        p = phrase.split()
        for i in range(len(flat)):
            if flat[i:i + len(p)] == p:
                return i, i + len(p)
        raise SystemExit(f'cut not found: {phrase}')
    (a0, a1), (b0, _), (c0, _) = find(CUTS[0]), find(CUTS[1]), find(CUTS[2])
    out = []
    for i, (ln, w) in enumerate(words):
        seg = 0 if i < a0 else (None if i < a1 else (1 if i < b0 else (2 if i < c0 else None)))
        out.append((seg, ln, w))
    return out


def stretches(words, rng=None):
    groups = defaultdict(list)
    for seg, ln, w in words:
        if seg is not None:
            groups[(seg, ln)].append(w)
    texts = ['', '', '']
    for (seg, ln) in sorted(groups):
        ws = list(groups[(seg, ln)])
        if rng:
            rng.shuffle(ws)
        texts[seg] += norm(' '.join(ws))
    return texts


def cipher_segments():
    segs, cur = [], []
    for r in csv.DictReader(open('ciphertext_f67.tsv', encoding='utf-8'), delimiter='\t'):
        g = r['group']
        if g.startswith('[PLAIN'):
            if cur:
                segs.append(cur); cur = []
            continue
        if g in NONSIGN:
            continue
        cur.append(g)
    segs.append(cur)
    assert len(segs) == 3
    return segs


def load_key():
    key = {}
    for r in csv.DictReader(open('key_1659.tsv', encoding='utf-8'), delimiter='\t'):
        v = r['value']
        key[r['code']] = '#' if v == 'M.' else ('' if v == '0' else norm(v) or v)
    return key


def nw(a, b):
    """Global alignment; returns for each index of a the aligned char of b (or None)."""
    n, m = len(a), len(b)
    S = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        S[i][0] = -i
    for j in range(1, m + 1):
        S[0][j] = -j
    for i in range(1, n + 1):
        ai, Si, Sp = a[i - 1], S[i], S[i - 1]
        for j in range(1, m + 1):
            d = Sp[j - 1] + (2 if ai == b[j - 1] else -1)
            u = Sp[j] - 1
            l = Si[j - 1] - 1
            Si[j] = d if d >= u and d >= l else (u if u >= l else l)
    out = [None] * n
    i, j = n, m
    while i > 0 and j > 0:
        if S[i][j] == S[i - 1][j - 1] + (2 if a[i - 1] == b[j - 1] else -1):
            out[i - 1] = b[j - 1]; i -= 1; j -= 1
        elif S[i][j] == S[i - 1][j] - 1:
            i -= 1
        else:
            j -= 1
    return out


def score(segs, key, texts, percode=None):
    agree = tot = 0
    for toks, text in zip(segs, texts):
        dec, owner = '', []
        for k, g in enumerate(toks):
            v = key.get(g, '')
            dec += v
            owner += [k] * len(v)
        al = nw(dec, text)
        ok = defaultdict(lambda: True)
        for idx, (ch, k) in enumerate(zip(dec, owner)):
            if al[idx] != ch:
                ok[k] = False
        for k, g in enumerate(toks):
            if key.get(g, ''):
                tot += 1
                agree += ok[k]
                if percode is not None:
                    percode[g][0] += ok[k]; percode[g][1] += 1
    return agree, tot


def build():
    key, segs, words = load_key(), cipher_segments(), f68_words()
    percode = defaultdict(lambda: [0, 0])
    a, t = score(segs, key, stretches(words), percode)
    S = a / t
    rng = random.Random(SEED)
    null = sorted(score(segs, key, stretches(words, rng))[0] / t for _ in range(NSHUF))
    p99 = null[int(0.99 * NSHUF) - 1]
    ge = sum(x >= S for x in null)
    unscored = sum(1 for s in segs for g in s if not key.get(g, ''))
    summ = [('measure', 'value'), ('cipher_groups', sum(map(len, segs))), ('scored_tokens', t), ('unscored_tokens', unscored),
            ('agree', a), ('S_target', f'{S:.4f}'), ('null_mean', f'{sum(null) / NSHUF:.4f}'),
            ('null_p95', f'{null[int(0.95 * NSHUF) - 1]:.4f}'), ('null_p99', f'{p99:.4f}'), ('null_max', f'{null[-1]:.4f}'),
            ('null_ge_target', f'{ge}/{NSHUF}'), ('gate', 'PASS' if S > p99 else 'FAIL')]
    f1 = io.StringIO(); csv.writer(f1, delimiter='\t', lineterminator='\n').writerows(summ)
    rows = [('code', 'key_1659', 'agree', 'scored')]
    for g in sorted(percode, key=lambda g: (int(g.lstrip('_')) if g.lstrip('_').isdigit() else 999, g)):
        rows.append((g, key[g] or '0', percode[g][0], percode[g][1]))
    f2 = io.StringIO(); csv.writer(f2, delimiter='\t', lineterminator='\n').writerows(rows)
    return {'f68_key1659_test.tsv': f1.getvalue(), 'f68_key1659_codes.tsv': f2.getvalue()}


if __name__ == '__main__':
    out = build()
    if '--check' in sys.argv:
        bad = [f for f, s in out.items() if not os.path.exists(f) or open(f, encoding='utf-8').read() != s]
        print('stale: ' + ' '.join(bad) if bad else 'ok')
        sys.exit(1 if bad else 0)
    for f, s in out.items():
        open(f, 'w', encoding='utf-8').write(s)
    print(out['f68_key1659_test.tsv'])
