#!/usr/bin/env python3
"""HAR-41R: score Bourdeau's needham1587 pigpen key on the f.41r (R8480 P1) cipher block against the left-margin clear version.

Gate, normalisation and null are fixed in ../PREREG-HAR-41R.md (pushed before any read). Inputs (tx/):
  f41r_reads.tsv   run<TAB>part<TAB>tokens<TAB>note   one blind Opus reader call per run (R1..R4)
  f41r_ctrl.tsv    word<TAB>tokens                    the same call's read of f.39v line G words 1, 5, 8 (reader control)
  f41r_margin.tsv  line<TAB>text<TAB>note             one blind Opus read of the margin clear text
Key: github.com/dbourdeau/cyphersolver targets/needham1587/decode.py (commit 0445769, MIT), unchanged:
J U L / C O F / N 7 D = a-i; dot below ('.') k-s; dot inside (':') t u w x y z.
Output: gloss/har41r_score.tsv and a summary on stdout. --check exits 1 if the committed tsv is stale.
"""
import os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TX = os.path.join(HERE, '..', 'tx')
OUT = os.path.join(HERE, 'har41r_score.tsv')
SHAPES = 'J U L C O F N 7 D'.split()
FORMS, LETTERS = [], []
for i, s in enumerate(SHAPES):
    FORMS.append(s); LETTERS.append('abcdefghi'[i])
for i, s in enumerate(SHAPES):
    FORMS.append(s + '.'); LETTERS.append('klmnopqrs'[i])
for i, s in enumerate(SHAPES[:6]):
    FORMS.append(s + ':'); LETTERS.append('tuwxyz'[i])
KEY = dict(zip(FORMS, LETTERS))
CTRL = {'1': 'L 7 J C. O U.', '5': '7 O. O: O D.', '8': 'F J D. J: O C. O C'}   # HAR-39V tx/f39v_lineG_har39v.tsv


def nl(s):
    """PREREG normalisation for letters (u/v, i/j/y, doubled letters)."""
    s = s.replace('j', 'i').replace('v', 'u').replace('y', 'i')
    return re.sub(r'(.)\1+', r'\1', s)


def norm_text(s):
    s = s.lower()
    s = re.sub(r'\[[^\]]*\]', ' ', s)
    for a, b in [(r'\by[tᵗ]\b', 'that'), (r'\bye\b', 'the'), (r'&', ' and '), (r'\blo\.', 'lord'), (r'\bl\.', 'lord')]:
        s = re.sub(a, b, s)
    words = [nl(re.sub(r'[^a-z]', '', w)) for w in s.split()]
    return [w for w in words if w]


def tokens_of(s):
    toks = []
    for t in s.split():
        if t.startswith('{'):
            toks.append('|'); continue
        toks.append(t)
    return toks


def decode(toks, key):
    """Return the list of decoded words (word gaps at '|'); unsure/unknown signs -> '?'."""
    words, cur = [], []
    for t in toks:
        if t == '|':
            if cur: words.append(''.join(cur)); cur = []
            continue
        cur.append(key.get(t.rstrip('?'), '?'))
    if cur: words.append(''.join(cur))
    return words


def semiglobal(d, m):
    """edit distance of d aligned in full against the best substring of m ('?' in d costs 1)."""
    prev = [0] * (len(m) + 1)
    for i, cd in enumerate(d, 1):
        cur = [i] + [0] * len(m)
        for j, cm in enumerate(m, 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (0 if cd == cm else 1))
        prev = cur
    return min(prev)


def stats(reads, mwords, key):
    words = []
    for toks in reads:
        words += decode(toks, key)
    d = nl(''.join(words))
    m = ''.join(mwords)
    s1 = 1 - semiglobal(d, m) / len(d) if d else 0.0
    long = [nl(w) for w in words if len(w.replace('?', '')) >= 3]
    mset = set(mwords)
    s2 = sum(1 for w in long if w in mset) / len(long) if long else 0.0
    return s1, s2, words


def load(name, ncol):
    rows = []
    for line in open(os.path.join(TX, name), encoding='utf8'):
        if not line.strip() or line.startswith('#') or line.split('\t')[0] in ('run', 'word', 'line'):
            continue
        f = line.rstrip('\n').split('\t')
        rows.append(f + [''] * (ncol - len(f)))
    return rows


def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def main():
    out = []
    ctrl = load('f41r_ctrl.tsv', 2)
    tot = miss = 0
    for w, toks in ctrl:
        ref = CTRL[w].split(); got = [t.rstrip('?') for t in toks.split()]
        e = lev(ref, got); tot += len(ref); miss += e
        out.append(['control', 'f39v_word' + w, ' '.join(ref), toks, '%d/%d' % (len(ref) - e, len(ref))])
    ctrl_ok = tot - miss >= 17
    out.append(['control', 'total', '', '', '%d/%d %s' % (tot - miss, tot, 'PASS' if ctrl_ok else 'FAIL')])

    reads = [tokens_of(r[2]) for r in load('f41r_reads.tsv', 4)]
    nsign = sum(1 for t in sum(reads, []) if t != '|'); nq = sum(1 for t in sum(reads, []) if t.endswith('?'))
    mtext = ' '.join(r[1] for r in load('f41r_margin.tsv', 3))
    mwords = norm_text(mtext)
    s1, s2, words = stats(reads, mwords, KEY)
    rng = random.Random(41)
    n1, n2 = [], []
    for _ in range(1000):
        L = LETTERS[:]; rng.shuffle(L)
        a, b, _w = stats(reads, mwords, dict(zip(FORMS, L)))
        n1.append(a); n2.append(b)
    p95 = lambda v: sorted(v)[949]
    f1 = sum(1 for v in n1 if v >= s1) / 1000; f2 = sum(1 for v in n2 if v >= s2) / 1000
    for r in load('f41r_reads.tsv', 4):
        out.append(['decode', r[0] + '_p' + r[1], r[2], ' '.join(decode(tokens_of(r[2]), KEY)), ''])
    out.append(['margin', 'normalised', '', ' '.join(mwords), '%d letters' % len(''.join(mwords))])
    nonte = len(''.join(mwords)) < 40
    if not ctrl_ok or nonte:
        outcome = 'non-test (%s)' % ('control FAIL' if not ctrl_ok else 'margin < 40 letters')
    elif s1 > p95(n1) and s2 > p95(n2):
        outcome = 'A' if s1 >= 0.60 else 'B'
    else:
        outcome = 'C'
    out.append(['stat', 'S1', '%.3f' % s1, 'null p95 %.3f; frac>= %.3f' % (p95(n1), f1), ''])
    out.append(['stat', 'S2', '%.3f' % s2, 'null p95 %.3f; frac>= %.3f' % (p95(n2), f2), ''])
    out.append(['stat', 'signs', str(nsign), 'unsure %d' % nq, ''])
    out.append(['stat', 'outcome', outcome, '', ''])
    text = 'kind\titem\tread\tvalue\tnote\n' + ''.join('\t'.join(r) + '\n' for r in out)
    if '--check' in sys.argv:
        if not os.path.exists(OUT) or open(OUT, encoding='utf8').read() != text:
            print('STALE: gloss/har41r_score.tsv differs from a fresh run'); sys.exit(1)
        print('OK'); return
    open(OUT, 'w', encoding='utf8').write(text)
    for r in out:
        if r[0] in ('control', 'stat'):
            print('\t'.join(r))
    print('decoded words:', ' '.join(words))


if __name__ == '__main__':
    main()
