#!/usr/bin/env python3
"""AX2-5801 gate: share of value-1-120 numeral tokens that fall inside a French word (>=3 letters,
tools/data/fr16 word list -- ax4612tr/word_share_check.py's method, CLAUDE.md Usage 8 reuse), decoded
through key_5801.tsv, for a target ciphertext (5799 or 4612) and for 5801's own ciphertext (the control
side of the pre-registered gate). Also 20 value-shuffled copies of key_5801 applied to the target (rule 3:
this statistic CAN move under a shuffle -- report it, don't hide it).

    python3 word_share_check.py TARGET_CIPHERTEXT.tsv
"""
import csv, os, sys, random, unicodedata
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'tools'))
import french16_ngram as fr

HERE = os.path.dirname(os.path.abspath(__file__))
TOP = os.path.dirname(HERE)


def fold(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(ch for ch in s if unicodedata.category(ch) != 'Mn').upper()
    s = s.replace('J', 'I').replace('U', 'V').replace('W', 'VV')
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
    rows = list(csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'))
    runs, cur = [], []
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
        sub, cur = [], []
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


def main():
    target_path = sys.argv[1]
    m = fr.load()
    words = {w for w in m.words if len(w) >= 3}

    key5801 = load_key(os.path.join(TOP, 'key_5801.tsv'))

    runs_5801 = load_runs(os.path.join(TOP, 'ciphertext_5801.tsv'))
    c_5801, t_5801 = word_share(runs_5801, key5801, words)
    share_5801 = 100 * c_5801 / t_5801 if t_5801 else 0.0
    print(f'5801 (own text) under key_5801: {c_5801}/{t_5801} = {share_5801:.1f}% inside a French word (>=3 letters)')

    runs_t = load_runs(target_path)
    c_t, t_t = word_share(runs_t, key5801, words)
    share_t = 100 * c_t / t_t if t_t else 0.0
    print(f'{target_path} under key_5801: {c_t}/{t_t} = {share_t:.1f}% inside a French word (>=3 letters)')

    rng = random.Random(5801)
    codes = sorted(key5801)
    values = [key5801[c] for c in codes]
    shares = []
    for seed in range(20):
        vals = values[:]
        rng.shuffle(vals)
        shuffled_key = dict(zip(codes, vals))
        c_s, t_s = word_share(runs_t, shuffled_key, words)
        shares.append(100 * c_s / t_s if t_s else 0.0)
    shares.sort()
    print(f'{target_path} through 20 value-shuffled copies of key_5801: mean {sum(shares)/len(shares):.1f}%, '
          f'max {shares[-1]:.1f}%, range {shares[0]:.1f}-{shares[-1]:.1f}%')

    gate_shuffle = share_t > shares[-1]
    gate_5801 = share_t >= 0.85 * share_5801
    print(f'GATE: target {share_t:.1f}% > shuffle max {shares[-1]:.1f}%: {gate_shuffle}; '
          f'target >= 0.85 * 5801-own {0.85*share_5801:.1f}%: {gate_5801}; '
          f'READS: {gate_shuffle and gate_5801}')


if __name__ == '__main__':
    main()
