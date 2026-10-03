"""GAPS205 (3 Oct 2026, account-4): line-pairing permutation test on a CONTENT axis, pre-registered in PREREG-GAPS205.md.

T = sum over the 24 letter lines of pairs.tsv of the best order-preserving merge of the 8 May half with its 20 May half,
scored by an English letter-bigram model (tools/data/en Huck Finn + Gatsby). Null: random re-pairing of the 20 May
halves. Controls: pairs.py's synth() with true pairs (coin, half dealers; power) and unpaired halves (false positives).
Credit: Ernst's 2018 line division; Bourdeau's length test (pairs.py reproduces it); this file adds only T.

T' (PREREG Addendum A) subtracts E[len a][len b], the mean merge score of independent halves of those lengths.

Usage: python3 gaps205_content.py [--check]    (writes / checks content_test.json)
"""
import csv, json, math, os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pairs  # noqa: E402  (synth, corpus_letters)

AZ = 'abcdefghijklmnopqrstuvwxyz'


def model(letters):
    uc, bc = Counter(letters), Counter(zip(letters, letters[1:]))
    n = len(letters)
    uni = {c: math.log10((uc[c] + 0.5) / (n + 13)) for c in AZ}
    big = {}
    for a in AZ:
        tot = sum(bc[(a, b)] for b in AZ) + 13
        for b in AZ:
            big[(a, b)] = math.log10((bc[(a, b)] + 0.5) / tot)
    return uni, big


def merge(a, b, uni, big):
    """Best order-preserving interleave of a and b; DP over (i, j, last-from)."""
    NEG = -1e18
    n, m = len(a), len(b)
    # D[i][j] = (best ending with a[i-1], best ending with b[j-1])
    D = [[[NEG, NEG] for _ in range(m + 1)] for _ in range(n + 1)]
    if n: D[1][0][0] = uni[a[0]]
    if m: D[0][1][1] = uni[b[0]]
    for i in range(n + 1):
        for j in range(m + 1):
            for k in (0, 1):
                v = D[i][j][k]
                if v == NEG: continue
                last = a[i - 1] if k == 0 else b[j - 1]
                if i < n:
                    w = v + big[(last, a[i])]
                    if w > D[i + 1][j][0]: D[i + 1][j][0] = w
                if j < m:
                    w = v + big[(last, b[j])]
                    if w > D[i][j + 1][1]: D[i][j + 1][1] = w
    return max(D[n][m])


def subsample(n, letters, rng):
    start = rng.randrange(len(letters) - 2 * n - 1); src = letters[start:start + 2 * n]
    return ''.join(src[i] for i in sorted(rng.sample(range(2 * n), n)))


class Expect:
    """E[n][m]: mean merge score of two independent order-preserving corpus subsamples (Addendum A, seed 2050)."""
    def __init__(self, letters, uni, big):
        self.l, self.u, self.b, self.c = letters, uni, big, {}

    def __call__(self, n, m):
        if (n, m) not in self.c:
            r = random.Random(2050 * 1000 + 100 * n + m)
            self.c[(n, m)] = sum(merge(subsample(n, self.l, r), subsample(m, self.l, r), self.u, self.b)
                                 for _ in range(40)) / 40
        return self.c[(n, m)]


def ptest(A, B, uni, big, perms, rng, E=None):
    M = [[merge(a, b, uni, big) - (E(len(a), len(b)) if E else 0) for b in B] for a in A]
    k = len(A); t = sum(M[i][i] for i in range(k)); idx = list(range(k)); hit = 0
    for _ in range(perms):
        rng.shuffle(idx)
        if sum(M[i][idx[i]] for i in range(k)) >= t: hit += 1
    return t, (hit + 1) / (perms + 1)


def run(variant):
    rows = [r for r in csv.DictReader(open(os.path.join(HERE, 'pairs.tsv')), delimiter='\t') if r['letter_line'] == 'y']
    A = [r['ad_8may'] for r in rows]; B = [r['ad_20may'] for r in rows]
    letters = pairs.corpus_letters(); uni, big = model(letters)
    E = Expect(letters, uni, big) if variant == "T'" else None
    t, p = ptest(A, B, uni, big, 20000, random.Random(205), E)
    tl = [len(a) + len(b) for a, b in zip(A, B)]
    arms = {}
    for arm in ('P-coin', 'P-half', 'U-half'):
        ps = []
        for c in range(20):
            cr = random.Random(205000 + 1000 * len(arms) + c)
            if arm == 'U-half':
                cA, _ = pairs.synth(tl, letters, cr, 'half'); _, cB = pairs.synth(tl, letters, cr, 'half')
            else:
                cA, cB = pairs.synth(tl, letters, cr, arm[2:])
            ps.append(ptest(cA, cB, uni, big, 2000, cr, E)[1])
        ps.sort()
        arms[arm] = {'texts': 20, 'perms_each': 2000, 'p_median': round(ps[10], 5),
                     'share_p_lt_0.001': sum(x < 0.001 for x in ps) / 20, 'share_p_lt_0.05': sum(x < 0.05 for x in ps) / 20}
    power = max(arms['P-coin']['share_p_lt_0.001'], arms['P-half']['share_p_lt_0.001'])
    fpr = arms['U-half']['share_p_lt_0.05']
    valid = power >= 0.5 and fpr <= 0.15
    verdict = ('non-test' if not valid else 'supported' if p < 0.001 else 'not detected' if p >= 0.05 else 'inconclusive')
    return {'statistic': variant, 'n_letter_lines': len(A), 'T_obs': round(t, 3), 'perms': 20000, 'seed': 205, 'p': round(p, 6),
            'controls': arms, 'power': power, 'fpr_U_half': fpr, 'valid': valid, 'verdict': verdict}


if __name__ == '__main__':
    out = json.dumps([run('T'), run("T'")], indent=1) + '\n'; path = os.path.join(HERE, 'content_test.json')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path).read() == out
        print('ok: content_test.json current' if ok else 'stale: content_test.json'); sys.exit(0 if ok else 1)
    open(path, 'w').write(out); print(out)
