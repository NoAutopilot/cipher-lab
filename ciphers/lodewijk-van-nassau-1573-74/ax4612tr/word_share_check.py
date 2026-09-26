#!/usr/bin/env python3
"""AX-4612TR2 check (a): share of value-1-120 numeral tokens that fall inside a French word (>=3
letters, from tools/data/fr16's own word list -- CLAUDE.md Usage 8, 'shared scripts before new
ones'), decoded through the repo's key.tsv, old ciphertext_4612.tsv vs the settled v2. Also runs the
same statistic on 20 value-shuffled copies of key.tsv (rule 3: this statistic CAN move under a value
shuffle -- report it, don't hide it).

A numeral 'run' is a maximal stretch of value-1-120 tokens between clear (=word) tokens, NULL/name
codes (>120) or unsettled '?' tokens; runs are decoded and scanned separately so a match never spans
a clear-word break the transcription itself marks.
"""
import csv, os, sys, random, unicodedata
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'tools'))
import french16_ngram as fr

def fold(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(ch for ch in s if unicodedata.category(ch) != 'Mn').upper()
    s = s.replace('J', 'I').replace('U', 'V').replace('W', 'VV').replace('OE', 'OE').replace('AE', 'AE')
    return s

def load_key(path):
    rows = list(csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'))
    key = {}
    for r in rows:
        try:
            code = int(r['code'])
        except ValueError:
            continue
        if 1 <= code <= 120 and len(r['value']) == 1 and r['value'].isalpha():
            key[code] = fold(r['value'])
    return key

def load_runs(path):
    """Return list of lists of int codes (value 1-120 numeral runs, as transcribed)."""
    rows = list(csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'))
    runs = []
    cur = []
    for r in rows:
        sign = r['sign'].strip()
        if sign.isdigit() and 1 <= int(sign) <= 120:
            cur.append(int(sign))
        else:
            if cur:
                runs.append(cur)
            cur = []
    if cur:
        runs.append(cur)
    return runs

def word_share(runs, key, words):
    covered = 0
    total = 0
    for run in runs:
        letters = [key.get(c) for c in run]
        total += sum(1 for l in letters if l is not None)
        # positions with an unknown code break coverage scanning into sub-runs too
        sub = []
        cur = []
        for l in letters:
            if l is None:
                if cur:
                    sub.append(cur)
                cur = []
            else:
                cur.append(l)
        if cur:
            sub.append(cur)
        for s in sub:
            n = len(s)
            hit = [False] * n
            for i in range(n):
                for j in range(i + 3, n + 1):
                    if ''.join(s[i:j]) in words:
                        for k in range(i, j):
                            hit[k] = True
            covered += sum(hit)
    return covered, total

if __name__ == '__main__':
    m = fr.load()
    words = {w for w in m.words if len(w) >= 3}

    key_old = load_key('key.tsv')
    runs_old = load_runs('ciphertext_4612.tsv')
    c_old, t_old = word_share(runs_old, key_old, words)

    runs_v2 = load_runs('ciphertext_4612_v2.tsv')
    c_v2, t_v2 = word_share(runs_v2, key_old, words)

    print(f'old ciphertext_4612.tsv: {c_old}/{t_old} = {100*c_old/t_old:.1f}% inside a French word (>=3 letters)')
    print(f'v2  ciphertext_4612_v2.tsv: {c_v2}/{t_v2} = {100*c_v2/t_v2:.1f}% inside a French word (>=3 letters)')

    rng = random.Random(4612)
    codes = sorted(key_old)
    values = [key_old[c] for c in codes]
    shares = []
    for seed in range(20):
        vals = values[:]
        rng.shuffle(vals)
        shuffled_key = dict(zip(codes, vals))
        c_s, t_s = word_share(runs_v2, shuffled_key, words)
        shares.append(100 * c_s / t_s)
    shares.sort()
    print(f'v2 through 20 value-shuffled copies of key.tsv: mean {sum(shares)/len(shares):.1f}%, '
          f'range {shares[0]:.1f}-{shares[-1]:.1f}% (this statistic CAN move under a shuffle, rule 3)')
