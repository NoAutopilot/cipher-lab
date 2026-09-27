#!/usr/bin/env python3
"""Campaign step H7 (27 Sept 2026): value-range screen of the 1803 Livingston compact key
(James Monroe Papers, Series 1, reel 3 frame 127; images/monroe/mss33217-003-0127.jpg) against the
366 numeric groups of Armstrong to Madison, 20 Feb 1808 (ciphertext.txt, Bourdeau's transcription).

Question: could the target's groups have been produced by this key at all?  The key's rules (read
from the leaf, grade M, one reader): letter alphabets 1-9 with a distinguishing mark per alphabet;
short words 15-97 and 232-286; a vocabulary column 334-897; explicit nulls 100..900 and 1000..9000;
zeroes may be appended on the right without changing the meaning.  So a group G is *producible* iff
strip_trailing_zeros(G) lies in the key's value set or G is a null.

Statistic: producible fraction over the numeric groups.  Controls (rule 3):
  positive  -- en18 period prose encoded with this key (words where the key has them, else letters),
               with the key's own nulls and trailing-zero variants sprinkled in: must read ~1.0, and its
               own digit-permuted null must sit well below it, or the statistic has no power;
  null A    -- the target's digits permuted within each group (200 draws): same digit multiset, same
               lengths, values changed -- the shuffled-VALUE control CAMPAIGN.md H7 names;
  null B    -- each group replaced by a uniform random value of the same digit count (200 draws).
No plaintext is read; no reading is claimed.  Output: screen.tsv beside this script.
"""
import gzip, random, re, sys, pathlib, statistics
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]

# --- key value set (grade M, this runner's single downscaled look + the PR 50 fixture; H11's blind
# passes settle the words; only the VALUES matter here) -------------------------------------------
LETTERS = set(range(1, 10))
WORDS = {15, 17, 19, 23, 24, 26, 28, 32, 34, 36, 38, 42, 43, 46, 48, 51, 57, 59, 62, 63, 64, 68, 71, 75,
         79, 82, 83, 84, 86, 91, 97, 232, 234, 236, 238, 243, 246, 248, 262, 263, 264, 268, 282, 283,
         284, 286}
WORDS |= {240, 241, 242, 244, 245}            # the smudged 'on' entry: 24x, exact digit unread
VOCAB = {334, 335, 336, 337, 338, 421, 422, 423, 424, 425, 426, 427, 428, 429, 442, 443, 446, 463, 465,
         642, 645, 647, 648, 682, 683, 684, 685, 686, 687, 689, 823, 824, 825, 826, 827, 842, 846, 864,
         869, 892, 893, 896, 897}
VOCAB_RANGES = [(330, 339), (420, 429), (440, 449), (460, 469), (640, 649), (680, 689), (820, 829),
                (840, 849), (860, 869), (890, 899)]   # generous: any entry in a column band counts
NULLS = {n * 100 for n in range(1, 10)} | {n * 1000 for n in range(1, 10)}
STRICT = LETTERS | WORDS | VOCAB
def in_generous(v):
    return v in STRICT or any(a <= v <= b for a, b in VOCAB_RANGES)

def strip0(n):
    while n > 0 and n % 10 == 0:
        n //= 10
    return n

def producible(g, generous=True):
    if g in NULLS:
        return True
    v = strip0(g)
    return in_generous(v) if generous else v in STRICT

def coverage(groups, generous=True):
    return sum(producible(g, generous) for g in groups) / len(groups)

def permute_digits(groups, rng):
    out = []
    for g in groups:
        d = list(str(g)); rng.shuffle(d)
        out.append(int(''.join(d)))   # a leading zero shortens the group: kept, it is what the permutation gives
    return out

def uniform_same_length(groups, rng):
    return [rng.randint(10 ** (len(str(g)) - 1) if len(str(g)) > 1 else 1, 10 ** len(str(g)) - 1) for g in groups]

# --- positive control: encode en18 prose with the key ------------------------------------------
WORDMAP = {'this': 15, 'the': 17, 'very': 19, 'a': 23, 'and': 24, 'an': 26, 'as': 28, 'all': 32, 'any': 34,
           'but': 36, 'by': 38, 'because': 42, 'can': 43, 'could': 46, 'do': 48, 'us': 51, 'with': 57,
           'was': 59, 'for': 62, 'give': 63, 'got': 64, 'have': 68, 'will': 71, 'would': 75, 'which': 79,
           'had': 82, 'how': 83, 'he': 84, 'in': 86, 'when': 91, 'you': 97, 'is': 232, 'i': 234, 'it': 236,
           'know': 238, 'on': 240, 'of': 243, 'out': 246, 'over': 248, 'so': 262, 'should': 263,
           'soon': 264, 'some': 268, 'to': 282, 'take': 283, 'that': 284, 'they': 286,
           'congress': 338, 'canada': 421, 'france': 429, 'french': 442, 'king': 642, 'louisiana': 645,
           'money': 647, 'spain': 842, 'spy': 864, 'trade': 869, 'union': 893}
ALPHA = {}
for i, c in enumerate('abcdefghi', 1): ALPHA[c] = i
for c, d in zip('klmnopqrs', [2, 4, 1, 6, 7, 5, 8, 9, 3]): ALPHA[c] = d
for c, d in zip('tuvwxyz', [2, 4, 6, 8, 7, 5, 9]): ALPHA[c] = d
ALPHA['j'] = ALPHA['i']

def encode(text, n_groups, rng, null_rate=0.03, zero_rate=0.10):
    words = re.findall(r"[a-z]+", text.lower())
    out = []
    for w in words:
        if len(out) >= n_groups: break
        codes = [WORDMAP[w]] if w in WORDMAP else [ALPHA[c] for c in w]
        for c in codes:
            if rng.random() < zero_rate: c *= 10 ** rng.randint(1, 2)
            out.append(c)
            if rng.random() < null_rate: out.append(rng.choice(sorted(NULLS)))
    return out[:n_groups]

def en18_texts(n, length, rng):
    files = sorted((ROOT / 'tools/data/en18').glob('*.txt.gz'))
    texts = []
    for f in files[:n]:
        t = gzip.open(f, 'rt', errors='ignore').read()
        start = rng.randint(len(t) // 4, len(t) // 2)
        texts.append(t[start:start + length])
    return texts

def main():
    rng = random.Random(20260927)
    body = [l for l in (ROOT / 'ciphers/armstrong-madison-1808/ciphertext.txt').read_text().splitlines()
            if l.strip() and not l.startswith('#')]
    groups = [int(t) for t in ' '.join(body).split() if t.isdigit()]
    n = len(groups)
    rows = []
    def rec(label, gs, note=''):
        rows.append((label, len(gs), f'{coverage(gs, True):.3f}', f'{coverage(gs, False):.3f}', note))
    rec('target', groups, 'ciphertext.txt numeric groups')
    over899 = sum(strip0(g) > 899 and g not in NULLS for g in groups)
    four_nonround = sum(g >= 1000 and g % 10 != 0 for g in groups)
    rows.append(('target: stripped value > 899 (impossible under this key, not a null)', over899, f'{over899/n:.3f}', '', ''))
    rows.append(('target: four-digit groups with a nonzero last digit', four_nonround, f'{four_nonround/n:.3f}', '', ''))
    for label, fn in [('nullA: target digits permuted within each group', permute_digits),
                      ('nullB: uniform random value, same digit count per group', uniform_same_length)]:
        cs = [coverage(fn(groups, rng), True) for _ in range(200)]
        cs_s = [coverage(fn(groups, rng), False) for _ in range(200)]
        rows.append((label, 200, f'mean {statistics.mean(cs):.3f} min {min(cs):.3f} p95 {sorted(cs)[189]:.3f} max {max(cs):.3f}',
                     f'mean {statistics.mean(cs_s):.3f} max {max(cs_s):.3f}', ''))
        tgt = coverage(groups, True)
        rows.append((label + ' -> target percentile', '', f'{sum(c < tgt for c in cs)/200:.3f}', '', 'share of draws below the target'))
    for i, t in enumerate(en18_texts(6, 6000, rng)):
        enc = encode(t, n, rng)
        rec(f'positive control {i+1}: en18 text encoded with this key', enc)
        cs = [coverage(permute_digits(enc, rng), True) for _ in range(200)]
        rows.append((f'positive control {i+1}: its own digit-permuted null', 200,
                     f'mean {statistics.mean(cs):.3f} max {max(cs):.3f}', '', ''))
    out = HERE / 'screen.tsv'
    with open(out, 'w') as f:
        f.write('row\tn\tproducible_generous\tproducible_strict\tnote\n')
        for r in rows: f.write('\t'.join(str(x) for x in r) + '\n')
    print(open(out).read())

if __name__ == '__main__':
    main()
