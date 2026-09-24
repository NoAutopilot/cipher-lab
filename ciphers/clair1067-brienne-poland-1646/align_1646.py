#!/usr/bin/env python3
"""Hard-EM alignment of ciphertext.txt against the interlinear decipherment dechiffre.tsv (24 Sept 2026).

Pattern of ciphers/fr5160-letellier-1653/align_f86.py, but line by line: each physical cipher line is aligned to
the words written above it. Each cipher group takes 0-MAXLEN plaintext letters (0 = null); a plaintext letter
no group carries costs SKIP. Viterbi segmentation under the current key, re-estimate, repeat. No seeds.
"Mr" is the symbol '#', "Mate" the symbol '&' (both abbreviations may be single codes).

  python3 align_1646.py              align runs of lines (BLOCKS), write align_1646.tsv and key_1646.tsv, print the per-line alignment
  python3 align_1646.py --control N  compare the true line-by-line pairing with N shuffled pairings (same EM, same scoring)
"""
import csv, math, random, re, sys, unicodedata
from collections import Counter, defaultdict

MAXLEN = 7
SKIP = -6.0
LENPRIOR = {0: 0.08, 1: 0.30, 2: 0.30, 3: 0.17, 4: 0.08, 5: 0.04, 6: 0.02, 7: 0.01}
LENPRIOR = {k: math.log(v) for k, v in LENPRIOR.items()}


def norm(s):
    s = re.sub(r'\[del:[^\]]*\]', '', s)
    s = s.replace('Mr', '#').replace('Mate', '&')
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn').lower().replace('v', 'u').replace('j', 'i')
    return re.sub(r'[^a-z#&]', '', s)


def load():
    toks = defaultdict(list)
    for r in csv.DictReader(open('ciphertext.txt'), delimiter='\t'):
        toks[r['line']].append((int(r['pos']), r['token']))
    gl = {r['line']: r['words'] for r in csv.DictReader(open('dechiffre.tsv'), delimiter='\t')}
    return [(ln, [t for _, t in sorted(toks[ln])], norm(gl[ln])) for ln in toks]


# Runs of cipher lines with no clear text between them; the decipherer's words flow across line ends inside a run
# (e.g. "renouue" stands over the end of f226v_C05, "lleroient" over f226v_C06).  Read from the images.
BLOCKS = [['f226r_C1', 'f226r_C2'], ['f226v_C01', 'f226v_C02'],
          ['f226v_C03', 'f226v_C04', 'f226v_C05', 'f226v_C06', 'f226v_C07'],
          ['f226v_C%02d' % i for i in range(8, 15)], ['f227r_C01'],
          ['f227r_C%02d' % i for i in range(2, 13)], ['f227r_C13', 'f227r_C14']]


def blocks(segs):
    d = {s[0]: s for s in segs}
    out = []
    for b in BLOCKS:
        toks = [(ln, i + 1, g) for ln in b for i, g in enumerate(d[ln][1])]
        out.append(('+'.join(b), toks, ''.join(d[ln][2] for ln in b)))
    return out


def viterbi(groups, text, score):
    n, m = len(groups), len(text)
    NEG = -1e18
    D = [[NEG] * (m + 1) for _ in range(n + 1)]
    B = [[0] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0.0
    for j in range(1, m + 1):
        D[0][j], B[0][j] = SKIP * j, -1
    for i in range(1, n + 1):
        g = groups[i - 1]
        for j in range(m + 1):
            best, arg = NEG, 0
            for L in range(0, min(MAXLEN, j) + 1):
                v = D[i - 1][j - L]
                if v > NEG / 2:
                    v += score(g, text[j - L:j])
                    if v > best:
                        best, arg = v, L
            if j and D[i][j - 1] > NEG / 2 and D[i][j - 1] + SKIP > best:
                best, arg = D[i][j - 1] + SKIP, -1
            D[i][j], B[i][j] = best, arg
    out, i, j = [], n, m
    while i > 0 or j > 0:
        L = B[i][j]
        if L < 0 or i == 0:
            j -= 1
            continue
        out.append(text[j - L:j]); j -= L; i -= 1
    return out[::-1], D[n][m]


def make_score(counts, tot, alpha=0.05):
    def score(g, chunk):
        c = counts[g][chunk]
        return math.log((c + alpha * math.exp(LENPRIOR[len(chunk)]) / 30 ** max(len(chunk), 1) * 30)
                        / (tot[g] + alpha)) + LENPRIOR[len(chunk)]
    return score


def sample(groups, text, score, T, rng):
    """Forward filtering, backward sampling of one segmentation at temperature T (annealed hard EM)."""
    n, m = len(groups), len(text)
    NEG = -1e18
    F = [[NEG] * (m + 1) for _ in range(n + 1)]
    F[0][0] = 0.0
    for j in range(1, m + 1):
        F[0][j] = SKIP * j / T
    def lse(xs):
        mx = max(xs)
        return mx + math.log(sum(math.exp(x - mx) for x in xs)) if mx > NEG / 2 else NEG
    for i in range(1, n + 1):
        g = groups[i - 1]
        for j in range(m + 1):
            xs = [F[i - 1][j - L] + score(g, text[j - L:j]) / T for L in range(0, min(MAXLEN, j) + 1) if F[i - 1][j - L] > NEG / 2]
            if j and F[i][j - 1] > NEG / 2:
                xs.append(F[i][j - 1] + SKIP / T)
            F[i][j] = lse(xs) if xs else NEG
    out, i, j = [], n, m
    while i > 0:
        opts = [(F[i - 1][j - L] + score(groups[i - 1], text[j - L:j]) / T, L) for L in range(0, min(MAXLEN, j) + 1) if F[i - 1][j - L] > NEG / 2]
        if j and F[i][j - 1] > NEG / 2:
            opts.append((F[i][j - 1] + SKIP / T, -1))
        mx = max(o[0] for o in opts)
        r = rng.random() * sum(math.exp(o[0] - mx) for o in opts)
        for w, L in opts:
            r -= math.exp(w - mx)
            if r <= 0:
                break
        if L < 0:
            j -= 1; continue
        out.append(text[j - L:j]); j -= L; i -= 1
    return out[::-1]


def em(segs, iters=60, restarts=6, seed=1646):
    """Annealed stochastic EM (restarts x 150 sampled sweeps, T 3 -> 1), then hard EM to convergence; best loglik kept."""
    best = None
    rng = random.Random(seed)
    for r in range(restarts):
        counts, tot = defaultdict(Counter), Counter()
        cur = {}
        for it in range(150):
            T = max(1.0, 3.0 - it / 50)
            for k, (ln, groups, text) in enumerate(segs):
                if k in cur:
                    for g, a in zip(groups, cur[k]):
                        counts[g][a] -= 1; tot[g] -= 1
                al = sample(groups, text, make_score(counts, tot), T, rng)
                cur[k] = al
                for g, a in zip(groups, al):
                    counts[g][a] += 1; tot[g] += 1
        c, res, ll = hard_em(segs, counts, tot, iters)
        if best is None or ll > best[2]:
            best = (c, res, ll)
    return best


def hard_em(segs, counts, tot, iters):
    ll = 0.0
    for _ in range(iters):
        score = make_score(counts, tot)
        newc, newt, res, ll = defaultdict(Counter), Counter(), [], 0.0
        for ln, groups, text in segs:
            al, s = viterbi(groups, text, score)
            res.append((ln, groups, al)); ll += s
            for g, a in zip(groups, al):
                newc[g][a] += 1; newt[g] += 1
        if newc == counts:
            break
        counts, tot = newc, newt
    return newc, res, ll


def consistency(counts):
    """Share of occurrences of repeated groups (>=2 tokens) that carry their group's modal value."""
    rep = [c for c in counts.values() if sum(c.values()) >= 2]
    return sum(c.most_common(1)[0][1] for c in rep) / sum(sum(c.values()) for c in rep)


def control(n):
    segs = load()
    c, _, ll = em(segs)
    print(f'true pairing      consistency {consistency(c):.3f}  loglik {ll:.1f}')
    rng = random.Random(1646)
    vals = []
    for k in range(n):
        texts = [s[2] for s in segs]
        while True:
            rng.shuffle(texts)
            if all(t != s[2] for t, s in zip(texts, segs)):
                break
        sh = [(s[0], s[1], t) for s, t in zip(segs, texts)]
        cc, _, l2 = em(sh)
        vals.append((consistency(cc), l2))
        print(f'shuffled pairing {k + 1:2d} consistency {vals[-1][0]:.3f}  loglik {l2:.1f}')
    print(f'shuffled: consistency max {max(v[0] for v in vals):.3f} mean {sum(v[0] for v in vals) / n:.3f}; '
          f'loglik max {max(v[1] for v in vals):.1f}')


VAL = {'#': 'Mr', '&': 'Mate', '': '0'}   # printed forms of the abbreviation symbols and of a null


def write_key(counts):
    def num(g):
        b = g.strip('_')
        return (0 if b.isdigit() else 1, int(b) if b.isdigit() else 0, g)
    with open('key_1646.tsv', 'w') as f:
        f.write('code\tvalue\tgrade\tevidence\toccurrences\tother_values\tnote\n')
        for g in sorted(counts, key=num):
            c = counts[g]
            v, n = c.most_common(1)[0]
            tot = sum(c.values())
            other = ','.join(f'{k or "0"}:{m}' for k, m in c.most_common()[1:])
            note = 'single attestation' if tot == 1 else ('conflict' if n / tot < 0.75 else ('minor conflict' if other else ''))
            val = VAL.get(v, v)
            f.write(f'{g}\t{val}\tC\t{n}\t{tot}\t{other}\t{note}\n')


def main():
    if '--control' in sys.argv:
        return control(int(sys.argv[sys.argv.index('--control') + 1]))
    blk = blocks(load())
    counts, res, ll = em([(b, [t[2] for t in toks], text) for b, toks, text in blk])
    write_key(counts)
    with open('align_1646.tsv', 'w') as f:
        f.write('line\tpos\tgroup\tplain\n')
        for (b, toks, text), (_, groups, al) in zip(blk, res):
            for t, a in zip(toks, al):
                f.write(f'{t[0]}\t{t[1]}\t{t[2]}\t{VAL.get(a, a)}\n')
            print(b, ' '.join(f'{g}={a or "0"}' for g, a in zip(groups, al)))
    print(f'consistency {consistency(counts):.3f}  groups {len(counts)}')


if __name__ == '__main__':
    main()
