"""Pooled design analysis of the Nov 1571 Birago numerical system: fr.3251 f.119 (Bourdeau ct2) + fr.3252 f.100r.
BIRAGO-NUM, 2 Oct 2026.  python3 analyze.py f119_ct2_bourdeau.txt f100_recon.txt
Tests (each with its own control):
 1 digit unigrams, 6/7 share in plain vs marked digits
 2 even-parity segmentations (Bourdeau's design: letters null and dropped, the wavy sign a hard break, every marked
   digit inside one code group of 1..maxw digits, all else two-digit letter tokens); count per letter; control =
   random digits at the same item positions (same letters/marks/wavy), share of draws with >=1 segmentation
 3 cross-letter shared k-mers of the plain digit stream (k>=6); null = f.100 digits shuffled (unigram kept)
 4 overlapping digit-bigram profile correlation between the letters; null = shuffled; power = two synthetic
   Italian texts of the two lengths under ONE random homophonic two-digit key vs under TWO keys
"""
import sys, random, math, re
from collections import Counter
from functools import lru_cache
sys.path.insert(0, '.')
import parse

def seq(path):
    return parse.items(open(path).read())

def count_segs(its, maxw=3, cap=10**9, wavy='break'):
    xs = [x for x in its if x[0] != 'L' and not (wavy == 'ignore' and x[0] == 'W')]   # letters dropped
    n = len(xs)
    @lru_cache(None)
    def f(i):
        if i == n: return 1
        k, v = xs[i]
        if k == 'W': return f(i + 1)
        tot = 0
        # two plain digits
        if i + 1 < n and xs[i][0] == 'D' and xs[i + 1][0] == 'D':
            tot += f(i + 2)
        # code group of width w containing exactly one marked digit, starting at i
        for w in range(1, maxw + 1):
            span = xs[i:i + w]
            if len(span) < w or any(s[0] not in 'DM' for s in span): break
            if sum(s[0] == 'M' for s in span) == 1:
                tot += f(i + w)
        return min(tot, cap)
    sys.setrecursionlimit(100000)
    return f(0)

def control_segs(its, maxw, draws, rng, pool, wavy='break'):
    # control: the same number of marks placed at random digit positions (digit VALUES cannot change the count,
    # so a value-shuffle control would be identical by construction -- rule 3); letters dropped either way
    pos = [i for i, x in enumerate(its) if x[0] in 'DM']
    nm = sum(x[0] == 'M' for x in its)
    ok = 0; cnt = []
    for _ in range(draws):
        mk = set(rng.sample(pos, nm))
        r = [(('M' if i in mk else 'D') if x[0] in 'DM' else x[0], x[1]) for i, x in enumerate(its)]
        c = count_segs(r, maxw, wavy=wavy); cnt.append(c)
        if c > 0: ok += 1
    return ok / draws

def kmers(s, k):
    return Counter(s[i:i + k] for i in range(len(s) - k + 1))

def shared(a, b, k):
    A, B = kmers(a, k), kmers(b, k)
    return sorted(set(A) & set(B))

def bigram_vec(s):
    # residual digit-bigram profile: observed overlapping bigram count minus the count expected from the unigrams,
    # so a shared digit-frequency profile alone does not make two texts correlate
    c = Counter(s[i:i + 2] for i in range(len(s) - 1)); u = Counter(s); n = len(s)
    keys = [a + b for a in '0123456789' for b in '0123456789']
    return [c[k] - (n - 1) * u[k[0]] * u[k[1]] / n / n for k in keys]

def corr(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    sx = math.sqrt(sum((a - mx) ** 2 for a in x)); sy = math.sqrt(sum((b - my) ** 2 for b in y))
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (sx * sy)

if __name__ == '__main__':
    pa, pb = sys.argv[1], sys.argv[2]
    rng = random.Random(1)
    A, B = seq(pa), seq(pb)
    for name, its in (('f119', A), ('f100', B)):
        d = parse.digits(its); c = Counter(d)
        plain = parse.digits([x for x in its if x[0] == 'D'], False)
        marked = ''.join(v[0] for k, v in its if k == 'M')
        print(f'[1] {name}: digits {len(d)} (plain {len(plain)}, marked {len(marked)}), letters',
              Counter(v for k, v in its if k == 'L'), 'wavy', sum(k == 'W' for k, v in its))
        print('    unigrams', ' '.join(f'{x}:{c[x]}' for x in '0123456789'),
              '| 6/7 in plain', sum(plain.count(x) for x in '67'), 'in marked', sum(marked.count(x) for x in '67'),
              '| marked digits', marked)
    for name, its in (('f119', A), ('f100', B)):
        pool = list(parse.digits(its))
        for wv in ('ignore', 'break'):
            for mw in (2, 3):
                n = count_segs(its, mw, wavy=wv)
                cf = control_segs(its, mw, 200, rng, pool, wavy=wv)
                print(f'[2] {name} wavy={wv} maxw={mw}: segmentations {n}; random-mark-position control share with >=1: {cf:.3f} (200 draws)')
    a = parse.digits([x for x in A if x[0] in 'DM'])
    b = parse.digits([x for x in B if x[0] in 'DM'])
    for k in (6, 7, 8, 10):
        sh = shared(a, b, k)
        null = []
        for _ in range(200):
            bl = list(b); rng.shuffle(bl); null.append(len(shared(a, ''.join(bl), k)))
        null.sort()
        print(f'[3] shared {k}-mers f119/f100: {len(sh)} {sh[:12]}; null mean {sum(null)/200:.2f} p95 {null[189]} max {null[-1]}')
    r = corr(bigram_vec(a), bigram_vec(b))
    nl = []
    for _ in range(200):
        bl = list(b); rng.shuffle(bl); nl.append(corr(bigram_vec(a), bigram_vec(''.join(bl))))
    nl.sort()
    print(f'[4] bigram-profile r(f119,f100) = {r:.3f}; shuffled-f100 null mean {sum(nl)/200:.3f} p95 {nl[189]:.3f}')

# ---- matched synthetic power control for tests 3 and 4 ----
CELLS = [a + b for a in '01234589' for b in '01234589']   # 64 two-digit cells, no 6/7 (as f.119's letter tokens)
def italian(n_letters, rng, path='../../../tools/data/it16dip'):
    import glob, gzip
    global _CORPUS
    if '_CORPUS' not in globals():
        _CORPUS = ''.join(gzip.open(f, 'rt', errors='ignore').read() for f in sorted(glob.glob(path + '/*.txt.gz')))
    txt = _CORPUS
    if '_CLEAN' not in globals():
        globals()['_CLEAN'] = re.sub('[^a-z]', '', txt.lower().replace('j', 'i').replace('k', 'c').replace('w', 'u').replace('y', 'i').replace('x', 's'))
    txt = _CLEAN
    s = rng.randrange(0, len(txt) - n_letters)
    return txt[s:s + n_letters]
def random_key(rng, sample):
    letters = sorted(set(sample)); fr = Counter(sample)
    cells = CELLS[:]; rng.shuffle(cells)
    key = {l: [cells.pop()] for l in letters}
    # remaining cells to letters in proportion to frequency (vowel homophony), up to 62 used
    tot = sum(fr.values()); extra = 62 - len(letters)
    while extra > 0 and cells:
        l = max(letters, key=lambda l: fr[l] / tot / len(key[l]))
        key[l].append(cells.pop()); extra -= 1
    return key
def encipher(txt, key, rng):
    return ''.join(rng.choice(key[c]) for c in txt)
def power(len_a, len_b, trials, rng, k=6):
    same_sh, diff_sh, same_r, diff_r = [], [], [], []
    for _ in range(trials):
        ta, tb = italian(len_a, rng), italian(len_b, rng)
        k1 = random_key(rng, ta + tb); k2 = random_key(rng, ta + tb)
        a1 = encipher(ta, k1, rng); b1 = encipher(tb, k1, rng); b2 = encipher(tb, k2, rng)
        same_sh.append(len(shared(a1, b1, k))); diff_sh.append(len(shared(a1, b2, k)))
        same_r.append(corr(bigram_vec(a1), bigram_vec(b1))); diff_r.append(corr(bigram_vec(a1), bigram_vec(b2)))
    f = lambda v: f'mean {sum(v)/len(v):.3f} min {min(v):.3f} max {max(v):.3f}'
    print(f'[P] synthetic ({len_a}+{len_b} letters, 62-cell homophonic, {trials} trials) shared {k}-mers: same key {f(same_sh)}; two keys {f(diff_sh)}')
    print(f'[P] bigram r: same key {f(same_r)}; two keys {f(diff_r)}')
    return same_sh, diff_sh, same_r, diff_r
