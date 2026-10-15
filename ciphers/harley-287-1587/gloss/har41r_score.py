#!/usr/bin/env python3
"""HAR-41R: score Bourdeau's needham1587 pigpen key on the f.41r (R8480 P1) cipher block against the left-margin clear version.

Gate, normalisation and null are fixed in ../PREREG-HAR-41R.md (pushed before any read). Inputs (tx/):
  f41r_reads.tsv   run<TAB>part<TAB>tokens<TAB>note   one blind Opus reader call per run (R1..R4)
  f41r_ctrl.tsv    word<TAB>tokens                    the same call's read of f.39v line G words 1, 5, 8 (reader control)
  f41r_margin.tsv  line<TAB>text<TAB>note             one blind Opus read of the margin clear text
Key: github.com/dbourdeau/cyphersolver targets/needham1587/decode.py (commit 0445769, MIT), unchanged:
J U L / C O F / N 7 D = a-i; dot below ('.') k-s; dot inside (':') t u w x y z.
Output: gloss/har41r_score.tsv and a summary on stdout. --check exits 1 if the committed tsv is stale.

--block 2 (HAR-58, ../PREREG-HAR-58.md and its Amendment 1): runs R5-R9 from tx/f41r_reads_b2.tsv, control tx/f41r_ctrl_b2.tsv,
clear text tx/f41r_margin_b2.tsv (lines M1.. = the second margin note; G5/G6/G7 = the interlinear glosses over R5/R6/R7). The gate
(same S1/S2/null/outcome) is R8+R9 against the M lines; R5, R6, R7 against their own gloss are post hoc (S1 and its null only).
Output gloss/har58_score.tsv.

--second (HAR-2R, ../PREREG-HAR-2R.md): a second blind reader on R1-R9 (tx/f41r_reads_r2.tsv, control tx/f41r_ctrl_r2.tsv). Units
U1 = R1-R3 vs the first margin note, U5/U6/U7 = R5/R6/R7 vs their gloss, U89 = R8+R9 vs the second note (R4 has no blind-read
clear partner: reader agreement only). Per unit S1 and S3 (gap-free word statistic: share of clear words >= 3 letters found as a
substring of the gap-free decode) against the same 1000 value-shuffled keys. A sign is C only where both readers agree (shape and
mark, neither '?'), the unit passes, and the agreed letter matches its aligned clear letter beside at least one matching neighbour.
Disagreements go to tx/f41r_disagree_r1r2.tsv. Output gloss/har2r_score.tsv. --demo-s3 prints S3 for reader 1's reads (PREREG).
"""
import os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TX = os.path.join(HERE, '..', 'tx')
OUT = os.path.join(HERE, 'har41r_score.tsv')
BLOCK2 = '--block' in sys.argv and sys.argv[sys.argv.index('--block') + 1] == '2'
SFX = '_b2' if BLOCK2 else ''
if BLOCK2:
    OUT = os.path.join(HERE, 'har58_score.tsv')
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
    s = re.sub(r'\[\?([^\]]*)\]', r'\1', s)     # an uncertain word is kept as read
    s = re.sub(r'\[[^\]]*\]', ' ', s)
    s = s.replace('^', '')                        # superscripts read as written (y^t -> yt, w^th -> wth)
    for a, b in [(r'\byt\b', 'that'), (r'\bye\b', 'the'), (r'&', ' and '), (r'\blo\.', 'lord'), (r'\bl\.', 'lord')]:
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
    ctrl = load('f41r_ctrl%s.tsv' % SFX, 2)
    tot = miss = 0
    for w, toks in ctrl:
        ref = CTRL[w].split(); got = [t.rstrip('?') for t in toks.split()]
        e = lev(ref, got); tot += len(ref); miss += e
        out.append(['control', 'f39v_word' + w, ' '.join(ref), toks, '%d/%d' % (len(ref) - e, len(ref))])
    ctrl_ok = tot - miss >= 17
    out.append(['control', 'total', '', '', '%d/%d %s' % (tot - miss, tot, 'PASS' if ctrl_ok else 'FAIL')])

    rrows = load('f41r_reads%s.tsv' % SFX, 4)
    mrows = load('f41r_margin%s.tsv' % SFX, 3)
    if BLOCK2:
        posthoc = []
        for run in ('R5', 'R6', 'R7'):
            rd = [tokens_of(r[2]) for r in rrows if r[0] == run]
            gw = norm_text(' '.join(r[1] for r in mrows if r[0] == 'G' + run[1:]))
            a, _b, _w = stats(rd, gw, KEY)
            rng = random.Random(41); nn = []
            for _ in range(1000):
                L = LETTERS[:]; rng.shuffle(L)
                nn.append(stats(rd, gw, dict(zip(FORMS, L)))[0])
            posthoc.append(['posthoc', run + '_vs_G' + run[1:], '%.3f' % a, 'null p95 %.3f; frac>= %.3f' % (sorted(nn)[949], sum(1 for v in nn if v >= a) / 1000), ' '.join(gw)])
        rrows_all = rrows
        rrows = [r for r in rrows if r[0] in ('R8', 'R9')]
        mrows = [r for r in mrows if r[0].startswith('M')]
    reads = [tokens_of(r[2]) for r in rrows]
    nsign = sum(1 for t in sum(reads, []) if t != '|'); nq = sum(1 for t in sum(reads, []) if t.endswith('?'))
    mtext = ' '.join(r[1] for r in mrows)
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
    for r in (rrows_all if BLOCK2 else rrows):
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
    if BLOCK2:
        out += posthoc
    text = 'kind\titem\tread\tvalue\tnote\n' + ''.join('\t'.join(r) + '\n' for r in out)
    if '--check' in sys.argv:
        if not os.path.exists(OUT) or open(OUT, encoding='utf8').read() != text:
            print('STALE: gloss/%s differs from a fresh run' % os.path.basename(OUT)); sys.exit(1)
        print('OK'); return
    open(OUT, 'w', encoding='utf8').write(text)
    for r in out:
        if r[0] in ('control', 'stat', 'posthoc'):
            print('\t'.join(r))
    print('decoded words:', ' '.join(words))


def s3(reads, cwords, key):
    """gap-free word statistic: share of clear words (>= 3 letters, normalised) that occur inside the gap-free decode."""
    d = nl(''.join(sum((decode(t, key) for t in reads), [])))
    w = [x for x in cwords if len(x) >= 3]
    return sum(1 for x in w if x in d) / len(w) if w else 0.0


def unit_reads(rows, runs):
    return [tokens_of(r[2]) for r in rows if r[0] in runs]


UNITS = [('U1', ('R1', 'R2', 'R3'), 'margin1', None), ('U5', ('R5',), 'b2', 'G5'), ('U6', ('R6',), 'b2', 'G6'),
         ('U7', ('R7',), 'b2', 'G7'), ('U89', ('R8', 'R9'), 'b2', 'M')]


def clear_words(unit):
    if unit[2] == 'margin1':
        rows = load('f41r_margin.tsv', 3)
    else:
        rows = [r for r in load('f41r_margin_b2.tsv', 3) if r[0].startswith(unit[3])]
    return norm_text(' '.join(r[1] for r in rows))


def unit_stats(reads, cw):
    a = stats(reads, cw, KEY)[0]; b = s3(reads, cw, KEY)
    rng = random.Random(41); n1, n3 = [], []
    for _ in range(1000):
        L = LETTERS[:]; rng.shuffle(L); k = dict(zip(FORMS, L))
        n1.append(stats(reads, cw, k)[0]); n3.append(s3(reads, cw, k))
    return a, b, sorted(n1)[949], sorted(n3)[949], sum(1 for v in n1 if v >= a) / 1000, sum(1 for v in n3 if v >= b) / 1000


def tok_align(a, b):
    """Levenshtein alignment of two token lists; returns (i or None, j or None) pairs."""
    n, m = len(a), len(b)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + (a[i-1] != b[j-1]))
    out, i, j = [], n, m
    while i or j:
        if i and j and D[i][j] == D[i-1][j-1] + (a[i-1] != b[j-1]):
            out.append((i-1, j-1)); i -= 1; j -= 1
        elif i and D[i][j] == D[i-1][j] + 1:
            out.append((i-1, None)); i -= 1
        else:
            out.append((None, j-1)); j -= 1
    return out[::-1]


def ln(c):
    return {'j': 'i', 'v': 'u', 'y': 'i'}.get(c, c)


def sg_align(d, m):
    """semi-global alignment of d (all of it) to a substring of m; returns for each i in d the matched m char or None."""
    n, k = len(d), len(m)
    D = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): D[i][0] = i
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + (d[i-1] != m[j-1] or d[i-1] == '?'))
    j = min(range(k + 1), key=lambda x: (D[n][x], x)); i = n; res = [None] * n
    while i:
        if j and D[i][j] == D[i-1][j-1] + (d[i-1] != m[j-1] or d[i-1] == '?'):
            res[i-1] = m[j-1] if d[i-1] == m[j-1] and d[i-1] != '?' else None; i -= 1; j -= 1
        elif D[i][j] == D[i-1][j] + 1:
            i -= 1
        else:
            j -= 1
    return res


def second():
    r1 = load('f41r_reads.tsv', 4) + load('f41r_reads_b2.tsv', 4)
    if '--demo-s3' in sys.argv:
        for u in UNITS:
            a, b, p1, p3, f1, f3 = unit_stats(unit_reads(r1, u[1]), clear_words(u))
            print('reader1 %s S1 %.3f p95 %.3f | S3 %.3f p95 %.3f frac>= %.3f' % (u[0], a, p1, b, p3, f3))
        return
    r2 = load('f41r_reads_r2.tsv', 4)
    out, dis = [], []
    ctrl = load('f41r_ctrl_r2.tsv', 2); tot = miss = 0
    for w, toks in ctrl:
        ref = CTRL[w].split(); got = [t.rstrip('?') for t in toks.split()]
        e = lev(ref, got); tot += len(ref); miss += e
        out.append(['control', 'f39v_word' + w, ' '.join(ref), toks, '%d/%d' % (len(ref) - e, len(ref))])
    ctrl_ok = tot - miss >= 17
    out.append(['control', 'total', '', '', '%d/%d %s' % (tot - miss, tot, 'PASS' if ctrl_ok else 'FAIL')])
    # reader agreement per run part; consensus token = agreed token, else '?'
    cons, nag, ntot = {}, 0, 0
    for row in r2:
        key_ = (row[0], row[1]); m1 = [r for r in r1 if (r[0], r[1]) == key_]
        a = tokens_of(m1[0][2]) if m1 else []; b = tokens_of(row[2])
        al = tok_align([t for t in a if t != '|'], [t for t in b if t != '|'])
        a_ = [t for t in a if t != '|']; b_ = [t for t in b if t != '|']; c = []
        for i, j in al:
            x = a_[i] if i is not None else '-'; y = b_[j] if j is not None else '-'
            ok = x == y and not x.endswith('?') and x != '-'
            ntot += 1; nag += ok
            c.append((x, y, ok))
            if not ok:
                dis.append([row[0], row[1], str(len(c)), x, y])
        cons[key_] = c
    out.append(['agree', 'signs', '%d/%d' % (nag, ntot), 'aligned sign pairs, both readers equal in shape and mark, neither ?', ''])
    graded = {}
    for u in UNITS:
        cw = clear_words(u)
        reads = unit_reads(r2, u[1])
        if not reads:
            out.append(['unit', u[0], 'not read by reader 2', '', 'not passed']); continue
        a, b, p1, p3, f1, f3 = unit_stats(reads, cw)
        ok = ctrl_ok and a > p1 and b > p3 and a >= 0.60
        out.append(['unit', u[0], 'S1 %.3f (p95 %.3f, frac>= %.3f)' % (a, p1, f1), 'S3 %.3f (p95 %.3f, frac>= %.3f)' % (b, p3, f3),
                    'PASS' if ok else 'not passed'])
        # consensus decode for the unit, letter per aligned pair ('?' where not agreed)
        seq = []
        for k in sorted(cons):
            if k[0] in u[1]:
                for n, (x, y, agr) in enumerate(cons[k]):
                    seq.append((k, n, ln(KEY.get(x, '?')) if agr and x in KEY else '?'))
        d = ''.join(s[2] for s in seq)
        m = ''.join(ln(ch) for ch in ''.join(cw))
        res = sg_align(d, m)
        hit = [r is not None for r in res]
        for n, s in enumerate(seq):
            c = hit[n] and ((n > 0 and hit[n-1]) or (n + 1 < len(hit) and hit[n+1]))
            graded[(s[0], s[1])] = 'C' if (ok and c) else 'M'
        out.append(['unit', u[0] + '_consensus', d, m, '%d letters match beside a matching neighbour' % sum(
            1 for n in range(len(hit)) if hit[n] and ((n > 0 and hit[n-1]) or (n + 1 < len(hit) and hit[n+1])))])
    nC = sum(1 for k in sorted(cons) for n, (x, y, agr) in enumerate(cons[k]) if agr and graded.get((k, n)) == 'C')
    for k in sorted(cons):
        g = ''.join(graded.get((k, n), 'M') if agr else '-' for n, (x, y, agr) in enumerate(cons[k]))
        out.append(['grade', k[0] + '_p' + k[1], ' '.join(x if agr else '?' for x, y, agr in cons[k]), g, ''])
    out.append(['stat', 'C_signs', str(nC), 'of %d agreed, %d aligned pairs' % (nag, ntot), ''])
    text = 'kind\titem\tread\tvalue\tnote\n' + ''.join('\t'.join(r) + '\n' for r in out)
    dtext = '# HAR-2R: reader 1 (HAR-41R/HAR-58) vs reader 2 (HAR-2R) sign disagreements, per run part, Levenshtein-aligned; not settled by a third pass\nrun\tpart\tpos\treader1\treader2\n' + ''.join('\t'.join(r) + '\n' for r in dis)
    o = os.path.join(HERE, 'har2r_score.tsv'); od = os.path.join(TX, 'f41r_disagree_r1r2.tsv')
    if '--check' in sys.argv:
        for f, t in ((o, text), (od, dtext)):
            if not os.path.exists(f) or open(f, encoding='utf8').read() != t:
                print('STALE: %s differs from a fresh run' % os.path.basename(f)); sys.exit(1)
        print('OK'); return
    open(o, 'w', encoding='utf8').write(text); open(od, 'w', encoding='utf8').write(dtext)
    for r in out:
        if r[0] in ('control', 'agree', 'unit', 'stat'):
            print('\t'.join(r))


if __name__ == '__main__':
    second() if '--second' in sys.argv else main()
