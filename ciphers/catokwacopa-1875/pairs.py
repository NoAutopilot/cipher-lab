"""Catokwacopa 1875: segment the two W. ads into Ernst's [1]-[28]+[10a] line pairs and re-run the
line-pairing permutation test (specs/catokwacopa-1875.json cheap test 1), with a matched synthetic control.

Input : ciphertext.txt (AD 3 / AD 4 lines, copied from ciphers/pollaky-1865-1875/ciphertext.txt).
Output: pairs.tsv (29 pairs, Ernst's labels and Bourdeau's line numbers side by side),
        pairtest.json (target statistic, null, controls).
Check : the segmentation is compared pair by pair with Bourdeau's PAIRS (his ads.py, Ernst's 2018 division,
        snapshot sources/cyphersolver/2026-10-02/catokwacopa/ads.py, MIT); read, not copied.

Test  : over the letter-only lines (both halves alphabetic, Bourdeau's LETTER_LINES rule: numerals and the
        mixed line 13 = Ernst [12] set aside, plus the identical 'Ap. 138' line), S = sum |len(a_i)-len(b_i)|.
        Null: the 20 May halves randomly re-paired with the 8 May halves (N permutations, fixed seed);
        p = share of re-pairings with S_perm <= S_obs.
Control (rule 3, matched design, length and line count): for each control text, every target letter line i
        gets an English phrase from tools/data/en (Huck Finn, Gatsby) of len(a_i)+len(b_i)+o letters, o in 0..3
        letters dropped at random, the rest dealt to two order-preserving streams; the same test is run on
        each synthetic pair-set. Two dealers bracket W.'s unknown splitting habit: 'coin' (each letter to
        either half with p=0.5, the least balanced) and 'half' (a random subset of floor(n/2) or ceil(n/2)
        letters, the most balanced). Power = share of control texts with p < 0.001.

Usage: python3 pairs.py [--check] [--perms 100000] [--controls 40]
"""
import argparse, json, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
BOURDEAU = os.path.join(ROOT, 'sources/cyphersolver/2026-10-02/catokwacopa/ads.py')
CORPUS = [os.path.join(ROOT, 'tools/data/en', f) for f in ('pg76_huckfinn.txt', 'pg64317_gatsby.txt')]
NUM = re.compile(r'^\d+$')


def ads():
    lines = [l.strip() for l in open(os.path.join(HERE, 'ciphertext.txt')) if l.startswith('W.')]
    assert len(lines) == 2, lines
    return lines[0], lines[1].split('--This will')[0]


def units(ad):
    """Printed tokens -> line units: runs of numerals join ('54. 3' -> '54.3'), 'Ap. 138' / 'A.P. 138' -> 'ap138'."""
    toks = [t for t in re.split(r'[\s.,\-–:]+', ad[2:]) if t]
    out = []
    i = 0
    while i < len(toks):
        t = toks[i]
        if t.lower() in ('ap', 'a') and i + 1 < len(toks):
            j = i + (2 if t.lower() == 'a' and toks[i + 1].lower() == 'p' else 1)
            if j < len(toks) and NUM.match(toks[j]):
                out.append('ap' + toks[j]); i = j + 1; continue
        if NUM.match(t):
            run = [t]; i += 1
            while i < len(toks) and NUM.match(toks[i]): run.append(toks[i]); i += 1
            out.append('.'.join(run)); continue
        out.append(t.lower()); i += 1
    return out


def ernst_label(k):          # Bourdeau line k (1-29) -> Ernst's 2018 comment-#2 label
    return '[%d]' % k if k <= 10 else ('[10a]' if k == 11 else '[%d]' % (k - 1))


def bourdeau_pairs():
    src = open(BOURDEAU).read()
    body = src[src.index('PAIRS = ['):src.index(']', src.index('PAIRS = [') + 10) + 1]
    return re.findall(r"\('([^']*)', '([^']*)'\)", body)


def stat(A, B):
    return sum(abs(len(a) - len(b)) for a, b in zip(A, B))


def ptest(A, B, n, rng):
    s = stat(A, B); lb = [len(b) for b in B]; la = [len(a) for a in A]; hit = 0
    for _ in range(n):
        rng.shuffle(lb)
        if sum(abs(x - y) for x, y in zip(la, lb)) <= s: hit += 1
    return s, hit


def corpus_letters():
    txt = ''
    for f in CORPUS:
        t = open(f, encoding='utf-8', errors='ignore').read()
        a, b = t.find('*** START'), t.find('*** END')
        txt += t[t.find('\n', a) if a >= 0 else 0: b if b > 0 else None]
    return re.sub('[^a-z]', '', txt.lower())


def synth(total_lens, letters, rng, dealer):
    A, B = [], []
    for n in total_lens:
        o = rng.randint(0, 3); start = rng.randrange(len(letters) - n - o)
        p = list(letters[start:start + n + o])
        for _ in range(o): p.pop(rng.randrange(len(p)))
        if dealer == 'coin':
            side = [rng.random() < 0.5 for _ in p]
        else:
            k = n // 2 + (rng.random() < 0.5 and n % 2); idx = set(rng.sample(range(n), k))
            side = [i in idx for i in range(n)]
        A.append(''.join(c for c, s in zip(p, side) if s)); B.append(''.join(c for c, s in zip(p, side) if not s))
    return A, B


def run(perms, controls):
    u3, u4 = units(ads()[0]), units(ads()[1])
    assert len(u3) == len(u4) == 29, (len(u3), len(u4))
    bp = bourdeau_pairs()
    mism = [(k + 1, (a, b), bp[k]) for k, (a, b) in enumerate(zip(u3, u4)) if (a, b) != tuple(bp[k])]
    rows = ['bourdeau_line\ternst\tad_8may\tad_20may\tlen_8may\tlen_20may\tletter_line']
    letter = []
    for k, (a, b) in enumerate(zip(u3, u4), 1):
        isl = a.isalpha() and b.isalpha() and a != b
        if isl: letter.append(k)
        rows.append('%d\t%s\t%s\t%s\t%d\t%d\t%s' % (k, ernst_label(k), a, b, len(a), len(b), 'y' if isl else 'n'))
    A = [u3[k - 1] for k in letter]; B = [u4[k - 1] for k in letter]
    rng = random.Random(1875)
    s, hit = ptest(A, B, perms, rng)
    letters = corpus_letters(); tl = [len(a) + len(b) for a, b in zip(A, B)]
    ctl = {}
    for dealer in ('coin', 'half'):
        ps = []
        for c in range(controls):
            cr = random.Random(10000 * (dealer == 'half') + c)
            cA, cB = synth(tl, letters, cr, dealer)
            cs, ch = ptest(cA, cB, perms // 10, cr)
            ps.append((cs, (ch + 1) / (perms // 10 + 1)))
        ctl[dealer] = {'controls': controls, 'perms_each': perms // 10,
                       'S_mean': round(sum(x for x, _ in ps) / controls, 1),
                       'S_range': [min(x for x, _ in ps), max(x for x, _ in ps)],
                       'power_p_lt_0.001': round(sum(p < 0.001 for _, p in ps) / controls, 3),
                       'p_median': sorted(p for _, p in ps)[controls // 2]}
    res = {'pairs': 29, 'mismatches_vs_bourdeau_ads_py': [str(m) for m in mism],
           'letter_lines': letter, 'n_letter_lines': len(letter),
           'letters_8may': sum(map(len, A)), 'letters_20may': sum(map(len, B)),
           'S_obs': s, 'perms': perms, 'perms_le_S_obs': hit, 'p': (hit + 1) / (perms + 1),
           'seed': 1875, 'control': ctl}
    return '\n'.join(rows) + '\n', json.dumps(res, indent=1) + '\n'


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true', help='fail if pairs.tsv / pairtest.json are stale')
    ap.add_argument('--perms', type=int, default=100000)
    ap.add_argument('--controls', type=int, default=40)
    a = ap.parse_args()
    tsv, js = run(a.perms, a.controls)
    paths = [(os.path.join(HERE, 'pairs.tsv'), tsv), (os.path.join(HERE, 'pairtest.json'), js)]
    if a.check:
        stale = [p for p, c in paths if not os.path.exists(p) or open(p).read() != c]
        print('stale: %s' % stale if stale else 'ok: pairs.tsv and pairtest.json current'); sys.exit(1 if stale else 0)
    for p, c in paths: open(p, 'w').write(c)
    print(js)
