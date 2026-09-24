#!/usr/bin/env python3
"""Hard-EM alignment of the folio 86 cipher (ciphertext_f86.tsv) against the folio 87 decipherment
(dechiffre_f87.txt, paragraph 1), 24 Sept 2026.

The cipher is cut into segments at the clear words it carries ("M." for M.r, "mais aussy", "et c'est ce qui
donne lieu de"); each segment is aligned to the matching stretch of the f.87 text. Each cipher group takes
0-4 plaintext letters (0 = null). Viterbi segmentation under the current key, re-estimate, repeat.
"M.r"/"M.e" written in the decipherment where the cipher has no clear "M." is the symbol '#'.

  python3 align_f86.py                 align all segments, print the per-group alignment and write align_f86.tsv
  python3 align_f86.py --holdout S5    estimate the key without segment S5, then check how S5 decodes with it
"""
import csv, math, re, sys, unicodedata
from collections import Counter, defaultdict

MAXLEN = 4
SKIP = -4.0   # log-penalty per plaintext letter not carried by any group


def norm(s):
    s = s.replace('M.r', '#').replace('M.e', '#')
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn').lower()
    return re.sub(r'[^a-z#]', '', s.replace('[?]', ''))


def cipher_tokens():
    return [(r['line'], int(r['pos']), r['group']) for r in csv.DictReader(open('ciphertext_f86.tsv'), delimiter='\t')]


def f87_para1():
    lines = open('dechiffre_f87.txt').read().split('\n')[2:14]
    return ' '.join(lines)


def segments():
    toks = cipher_tokens()
    text = f87_para1()
    # split the cipher at clear material
    segs, cur = [], []
    for t in toks:
        g = t[2]
        if g == 'M.' or g.startswith('['):
            if cur:
                segs.append(cur); cur = []
            continue
        cur.append(t)
    segs.append(cur)
    # plaintext stretches, same cut points
    cuts = [r'M\.r\s*Dambrun', r'M\.r son fils', r'mais aussi', r'M\.r\s*Dambrun se', r'et cest ce qui donne à\s*lieu de']
    parts, rest = [], text
    for c in cuts:
        m = re.search(c, rest)
        parts.append(rest[:m.start()])
        # keep the name / following words that are enciphered after the clear "M."
        keep = {0: 'Dambrun', 1: 'son fils', 3: 'Dambrun se'}.get(len(parts) - 1, '')
        rest = keep + ' ' + rest[m.end():]
    parts.append(rest)
    names = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']
    return [(n, s, norm(p)) for n, s, p in zip(names, segs, parts)]


def viterbi(groups, text, score):
    n, m = len(groups), len(text)
    NEG = -1e18
    D = [[NEG] * (m + 1) for _ in range(n + 1)]
    B = [[0] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0.0
    for i in range(1, n + 1):
        g = groups[i - 1]
        for j in range(m + 1):
            best, arg = NEG, 0
            for L in range(0, min(MAXLEN, j) + 1):
                v = D[i - 1][j - L]
                if v <= NEG / 2:
                    continue
                v += score(g, text[j - L:j])
                if v > best:
                    best, arg = v, L
            D[i][j], B[i][j] = best, arg
        # plaintext letters the cipher leaves out (the decipherer's text is not a letter-for-letter copy)
        for j in range(1, m + 1):
            for L in (1, 2, 3):
                if j - L >= 0 and D[i][j - L] > NEG / 2 and D[i][j - L] + SKIP * L > D[i][j]:
                    D[i][j], B[i][j] = D[i][j - L] + SKIP * L, -L
    out, j, i = [], m, n
    skipped = []
    while i > 0:
        L = B[i][j]
        if L < 0:
            skipped.append(text[j + L:j]); j += L; continue
        out.append(text[j - L:j]); j -= L; i -= 1
    return out[::-1], D[n][m]


LENPRIOR = {0: math.log(0.05), 1: math.log(0.45), 2: math.log(0.35), 3: math.log(0.12), 4: math.log(0.03)}


def make_score(counts, tot, alpha=0.05):
    def score(g, chunk):
        c = counts[g][chunk]
        # a group seen with a different value is penalised; smoothing lets new values in early
        return math.log((c + alpha * math.exp(LENPRIOR[len(chunk)]) / 30) / (tot[g] + alpha)) + LENPRIOR[len(chunk)]
    return score


# Seeds: read by hand from repeats before any EM (24 Sept 2026): "_18 15 19" opens both "Soit" (L01) and
# "soit" (L08); "_3 7 21" recurs three times where "pour" recurs three times; "m 31 7 8 _7 24 18 19" recurs
# (L11, L16) where "a ceux qui ont" recurs.  Seeds only start the EM; every value is re-estimated.
SEEDS = {'_18': 's', '15': 'oi', '19': 't', '_3': 'p', '7': 'ou', '21': 'r', 'm': 'a', '31': 'ce',
         '8': 'x', '_7': 'q', '24': 'ui', '18': 'on',
         # second round, from the first unseeded-plus-seeded run: "tort a M.e de la" puts 115 on M.e
         '115': '#', '36': 'de', '20': 's', '35': 'da', '_0': 'pa', '6': 'qu', '_17': 'si', '61': 'le'}


def em(segs, iters=40, seeded=True):
    counts, tot = defaultdict(Counter), Counter()
    if seeded:
        for g, v in SEEDS.items():
            counts[g][v] += 2; tot[g] += 2
    for it in range(iters):
        score = make_score(counts, tot)
        newc, newt, res = defaultdict(Counter), Counter(), []
        for name, toks, text in segs:
            al, s = viterbi([t[2] for t in toks], text, score)
            res.append((name, toks, al))
            for t, a in zip(toks, al):
                newc[t[2]][a] += 1; newt[t[2]] += 1
        if newc == counts:
            break
        counts, tot = newc, newt
    return counts, res


def write_key(counts):
    """key_1659.tsv: modal value per group, grade C (known plaintext), evidence = occurrences aligned to that value."""
    def num(g):
        b = g.lstrip('_')
        return (int(b) if b.isdigit() else 999, g.startswith('_'), g)
    with open('key_1659.tsv', 'w') as f:
        f.write('code\tvalue\tgrade\tevidence\toccurrences\tother_values\tnote\n')
        for g in sorted(counts, key=num):
            c = counts[g]
            v, n = c.most_common(1)[0]
            tot = sum(c.values())
            other = ','.join(f'{k or "0"}:{m}' for k, m in c.most_common()[1:])
            note = 'conflict' if other and n / tot < 0.75 else ('minor conflict' if other else '')
            if n == 1 and tot == 1:
                note = 'single attestation'
            val = {'#': 'M.' , '': '0'}.get(v, v)
            f.write(f'{g}\t{val}\tC\t{n}\t{tot}\t{other}\t{note}\n')


def main():
    segs = segments()
    hold = sys.argv[sys.argv.index('--holdout') + 1] if '--holdout' in sys.argv else None
    train = [s for s in segs if s[0] != hold]
    counts, res = em(train)
    for name, toks, text in segs:
        print(name, len(toks), 'groups', len(text), 'letters')
    if hold:
        key = {g: c.most_common(1)[0][0] for g, c in counts.items()}
        for name, toks, text in segs:
            if name != hold:
                continue
            dec = [key.get(t[2], '?') for t in toks]
            print('held-out', name, 'truth :', text)
            print('held-out', name, 'decode:', '|'.join(dec))
            hit = sum(1 for t in toks if t[2] in key)
            print('groups keyed from the other segments:', hit, '/', len(toks))
            full, _ = em(segs)
            fk = {g: c.most_common(1)[0][0] for g, c in full.items()}
            al, _ = viterbi([t[2] for t in toks], text, make_score(full, Counter({g: sum(c.values()) for g, c in full.items()})))
            same = sum(1 for t, a, d in zip(toks, al, dec) if a == d)
            print('held-out groups whose value matches their position in the full alignment:', same, '/', len(toks))
        return
    write_key(counts)
    with open('align_f86.tsv', 'w') as f:
        f.write('seg\tline\tpos\tgroup\tplain\n')
        for name, toks, al in res:
            for t, a in zip(toks, al):
                f.write(f'{name}\t{t[0]}\t{t[1]}\t{t[2]}\t{a}\n')
            print(name, ' '.join(f'{t[2]}={a or "0"}' for t, a in zip(toks, al)))


if __name__ == '__main__':
    main()
