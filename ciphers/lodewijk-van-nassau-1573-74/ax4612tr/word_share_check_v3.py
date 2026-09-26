#!/usr/bin/env python3
"""AX2-4612 (26 Sept 2026): word_share_check.py's method (French-word share of value-1-120 numeral
runs, tools/data/fr16's own word list), re-run for the settled v3 transcription under key_full.tsv
(not key.tsv -- the brief's gate is against key_full), plus:
  - 20 value-shuffled copies of key_full (same statistic, rule 3's required control)
  - 5811's own ciphertext (a letter key_full reads correctly), cut to 4612 v3's N of value-1-120
    numeral tokens, as the positive-control comparison the brief's gate names.

Gate (written to NOTES.md AX2-4612 before these numbers were computed, verbatim):
"4612 v3 reads under key_full if its French-word share (word_share_check.py method, fr16) is above
the max of 20 value-shuffles of key_full AND at least 0.85 of the share the same statistic gives
5811's own ciphertext (known reading) cut to 4612's N."
"""
import csv, os, sys, random, unicodedata
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'tools'))
import french16_ngram as fr

def fold(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(ch for ch in s if unicodedata.category(ch) != 'Mn').upper()
    s = s.replace('J', 'I').replace('U', 'V').replace('W', 'VV').replace('OE', 'OE').replace('AE', 'AE')
    return s

def load_key_full(path):
    """key_full.tsv: code, value, grade, source, note. Same 1-120 single-letter filter as
    word_share_check.py's load_key, but reading key_full's own columns."""
    rows = list(csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'))
    key = {}
    for r in rows:
        try:
            code = int(r['code'])
        except (ValueError, KeyError):
            continue
        v = r.get('value', '')
        if 1 <= code <= 120 and len(v) == 1 and v.isalpha():
            key[code] = fold(v)
    return key

def load_runs(path, max_numerals=None):
    """Return list of lists of int codes (value 1-120 numeral runs). If max_numerals is set, stop
    once that many 1-120 numerals have been collected (cutting 5811 to 4612 v3's N), truncating the
    final run in progress rather than starting a new one."""
    rows = list(csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'))
    runs = []
    cur = []
    count = 0
    for r in rows:
        sign = r['sign'].strip()
        if sign.isdigit() and 1 <= int(sign) <= 120:
            cur.append(int(sign))
            count += 1
            if max_numerals is not None and count >= max_numerals:
                runs.append(cur)
                return runs
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

    key_full = load_key_full('key_full.tsv')

    runs_v3 = load_runs('ciphertext_4612_v3.tsv')
    c_v3, t_v3 = word_share(runs_v3, key_full, words)
    n_v3_numerals = sum(len(r) for r in runs_v3)
    print(f'v3 ciphertext_4612_v3.tsv under key_full: {c_v3}/{t_v3} = {100*c_v3/t_v3:.1f}% inside a French word (>=3 letters); N={n_v3_numerals} value-1-120 numerals')

    rng = random.Random(46120)
    codes = sorted(key_full)
    values = [key_full[c] for c in codes]
    shares = []
    for seed in range(20):
        vals = values[:]
        rng.shuffle(vals)
        shuffled_key = dict(zip(codes, vals))
        c_s, t_s = word_share(runs_v3, shuffled_key, words)
        shares.append(100 * c_s / t_s)
    shares.sort()
    print(f'v3 through 20 value-shuffled copies of key_full: mean {sum(shares)/len(shares):.1f}%, '
          f'range {shares[0]:.1f}-{shares[-1]:.1f}%, max {shares[-1]:.1f}%')

    runs_5811_cut = load_runs('ciphertext_5811.tsv', max_numerals=n_v3_numerals)
    c_5811, t_5811 = word_share(runs_5811_cut, key_full, words)
    n_5811_numerals = sum(len(r) for r in runs_5811_cut)
    print(f'5811 (known reading) cut to N={n_5811_numerals} under key_full: {c_5811}/{t_5811} = {100*c_5811/t_5811:.1f}% inside a French word (>=3 letters)')

    v3_pct = 100 * c_v3 / t_v3
    shuf_max = shares[-1]
    ctrl_pct = 100 * c_5811 / t_5811
    threshold = 0.85 * ctrl_pct
    passes_shuffle = v3_pct > shuf_max
    passes_control = v3_pct >= threshold
    print()
    print(f'GATE: v3 {v3_pct:.1f}% > shuffle max {shuf_max:.1f}%? {passes_shuffle}. '
          f'v3 {v3_pct:.1f}% >= 0.85 * 5811-control {ctrl_pct:.1f}% = {threshold:.1f}%? {passes_control}.')
    print(f'GATE VERDICT: {"READS under key_full (both conditions met)" if passes_shuffle and passes_control else "does not read under key_full (gate not met)"}')
