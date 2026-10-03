#!/usr/bin/env python3
"""GAPS194 (3 Oct 2026): ad 2 group-structure screen against period codebooks (PREREG-GAPS194.md).

S0 = number of ad 2's 36 groups with 1 <= value <= R_B (book B's highest code number).
Positive control: 36-word English windows encoded through B's word->number list (plain, and with an
additive key wrapping mod R_B). Null: same digit-length profile, uniform in class. Seed 194.
Writes codebook_screen.tsv. --check exits 1 if the committed TSV differs.
"""
import re, random, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '../../..'))
AD2 = "56 717 9362 81720 19736 14 618 9 77314 390 400 272 20 211 59 91 881 460 80 401 70 447 415 91 437 801 10031 874 92 871 2391 941 72050 67321 438921 150".split()
assert len(AD2) == 36
FIX = str.maketrans('OoIlS', '00115')

def slater():
    lines = [l.strip() for l in open(os.path.join(HERE, 'codebooks/telegraphiccodet00slatuoft.txt'), errors='replace')]
    lines = [l for l in lines if l]
    pairs, word = {}, None
    for l in lines:
        m = re.fullmatch(r'(?:[.\s]*)([0-9OoIlS]{5})', l)
        if m and word:
            n = int(m.group(1).translate(FIX)) if m.group(1).translate(FIX).isdigit() else None
            if n: pairs.setdefault(n, word)
            word = None; continue
        w = re.match(r'([A-Za-z][a-z]+)\b', l)
        word = w.group(1).lower() if w else None
    # keep numbers consistent with alphabetical order (drop OCR misreads): word order must be monotone
    ns = sorted(pairs)
    good = {}
    for i, n in enumerate(ns):
        lo = pairs[ns[i-1]] if i else ''
        hi = pairs[ns[i+1]] if i+1 < len(ns) else '~'
        if lo <= pairs[n] <= hi: good[n] = pairs[n]
    R = max(n for n in good if n <= 30000 and (n-1 in good or n-2 in good))  # highest number in a consecutive run
    return good, R

def smith_R():
    # naked numbers = phrases (preface); phrase list follows the vocabulary's last word 'Zygodactylous'
    lines = open(os.path.join(HERE, 'codebooks/secretcorrespon00smitgoog.txt'), errors='replace').read().splitlines()
    start = max(i for i, l in enumerate(lines) if l.startswith('Zygodactyl'))
    body = [l for l in lines[start:] if len(l.strip()) > 12]
    return len(body)  # one phrase per long line (upper bound: wrapped phrases count twice)

def s0(vals, R): return sum(1 <= v <= R for v in vals)

def main():
    rng = random.Random(194)
    words = re.findall(r"[a-z]+", open(os.path.join(ROOT, 'tools/data/pg1661_holmes.txt'), errors='replace').read().lower())
    book, R_sl = slater()
    R_sm = smith_R()
    w2n = {}
    for n, w in book.items(): w2n.setdefault(w, n)
    tv = [int(x) for x in AD2]
    tv2 = tv[:7] + [977314] + tv[9:]
    rows = [('book', 'R_B', 'entries_parsed', 'S0_target', 'S0_target_977314', 'pos_plain_power', 'pos_key_power', 'null_mean', 'null_p95', 'gate', 'verdict')]
    for name, R, enc in (('slater1888', R_sl, w2n), ('smith1845_phrases', R_sm, None)):
        pp = pk = 0; null = []
        for _ in range(2000):
            if enc:
                i = rng.randrange(len(words) - 400); codes = []
                while len(codes) < 36:
                    if words[i] in enc: codes.append(enc[words[i]])
                    i += 1
            else:
                codes = [rng.randint(1, R) for _ in range(36)]  # phrase book: any phrase sequence
            pp += s0(codes, R) >= 34
            k = rng.randint(1, R)
            pk += s0([(c + k - 1) % R + 1 for c in codes], R) >= 34
            null.append(s0([rng.randint(10**(len(x)-1), 10**len(x)-1) for x in AD2], R))
        null.sort()
        t, t2 = s0(tv, R), s0(tv2, R)
        pw = min(pp, pk) / 2000
        verdict = 'non-test' if pw < 0.8 else ('PASS' if t >= 34 else 'FAIL')
        rows.append((name, R, len(enc) if enc else 'n/a', t, t2, pp/2000, pk/2000, round(sum(null)/2000, 2), null[int(0.95*2000)], '>=34 & power>=0.8', verdict))
    out = '\n'.join('\t'.join(map(str, r)) for r in rows) + '\n'
    path = os.path.join(HERE, 'codebook_screen.tsv')
    if '--check' in sys.argv:
        sys.exit(0 if open(path).read() == out else 1)
    open(path, 'w').write(out); print(out, end='')
    print('over-range ad2 groups (slater):', [v for v in tv if v > R_sl])

if __name__ == '__main__': main()
