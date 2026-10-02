#!/usr/bin/env python3
"""NEXT-LVN (2 Oct 2026): word_share_check_v3.py's measure for 4612 v3 under key_1572
(../jan-van-nassau-1572-75/key_1572.tsv, KEY-OFFICES.tsv row 34), with 20 value shuffles of key_1572 and
5200 (read under key_1572) cut to 4612 v3's N of value-1-120 numerals as the matched control.
Adaptation (same for target, shuffles, control): NULL-valued codes are dropped inside a run, not run breaks;
codes with no key_1572 row break a run. Gate: see NOTES.md "NEXT-LVN". Run from the target folder."""
import csv, os, sys, random, glob
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
sys.path.insert(0, HERE)
import french16_ngram as fr
from word_share_check_v3 import fold, word_share

JAN = os.path.join(HERE, '..', '..', 'jan-van-nassau-1572-75')

def load_key_1572():
    key = {}
    for r in csv.DictReader(open(os.path.join(JAN, 'key_1572.tsv'), encoding='utf-8'), delimiter='\t'):
        v = r['value'].strip()
        if v == 'NULL':
            key[int(r['code'])] = 'NULL'
        elif len(v) == 1 and v.isalpha():
            key[int(r['code'])] = fold(v)
        # '?' (code 63) left unkeyed
    return key

def load_signs(paths):
    out = []
    for p in paths:
        out += [r['sign'].strip() for r in csv.DictReader(open(p, encoding='utf-8'), delimiter='\t')]
    return out

def runs_of(signs, key, max_numerals=None):
    """Runs of value-1-120 numerals; NULL codes dropped in place, unkeyed codes kept (word_share breaks on them)."""
    runs, cur, count = [], [], 0
    for s in signs:
        if s.isdigit() and 1 <= int(s) <= 120:
            c = int(s)
            count += 1
            if key.get(c) != 'NULL':
                cur.append(c)
            if max_numerals is not None and count >= max_numerals:
                break
        else:
            if cur:
                runs.append(cur)
            cur = []
    if cur:
        runs.append(cur)
    return runs, count

def share(signs, key, words, cut=None):
    lkey = {c: v for c, v in key.items() if v != 'NULL'}
    runs, n = runs_of(signs, key, cut)
    c, t = word_share(runs, lkey, words)
    return 100 * c / t if t else 0.0, c, t, n

if __name__ == '__main__':
    words = {w for w in fr.load().words if len(w) >= 3}
    key = load_key_1572()
    t_signs = load_signs(['ciphertext_4612_v3.tsv'])
    c_signs = load_signs(sorted(glob.glob(os.path.join(JAN, 'reading_5200_p*_tokens.tsv'))))
    tp, tc, tt, tn = share(t_signs, key, words)
    print(f'4612 v3 under key_1572: {tc}/{tt} = {tp:.1f}% inside a French word; N={tn} value-1-120 numerals')
    cp, cc, ct, cn = share(c_signs, key, words, cut=tn)
    print(f'5200 cut to N={cn} under key_1572: {cc}/{ct} = {cp:.1f}%')
    codes = sorted(key); vals = [key[c] for c in codes]
    rng = random.Random(46121)
    ts, cs = [], []
    for _ in range(20):
        v = vals[:]; rng.shuffle(v); k = dict(zip(codes, v))
        ts.append(share(t_signs, k, words)[0]); cs.append(share(c_signs, k, words, cut=tn)[0])
    ts.sort(); cs.sort()
    print(f'4612 v3, 20 value shuffles of key_1572: mean {sum(ts)/20:.1f}%, range {ts[0]:.1f}-{ts[-1]:.1f}%')
    print(f'5200 cut, same 20 shuffles (headroom): mean {sum(cs)/20:.1f}%, range {cs[0]:.1f}-{cs[-1]:.1f}%')
    mod3 = lambda sg, cut: sum(1 for s in [x for x in sg if x.isdigit() and 1 <= int(x) <= 120][:cut] if int(s) % 3 == 0)
    print(f'share of numerals on a multiple of 3 (table letter slots 3-72 and unkeyed 75-120): 4612 {mod3(t_signs, None)}/{tn}, 5200 cut {mod3(c_signs, tn)}/{cn}')
    a, b = tp > ts[-1], tp >= 0.85 * cp
    print(f'\nGATE: 4612 {tp:.1f}% > shuffle max {ts[-1]:.1f}%? {a}. 4612 {tp:.1f}% >= 0.85 x 5200 {cp:.1f}% = {0.85*cp:.1f}%? {b}.')
    print('GATE VERDICT:', 'READS under key_1572 (both conditions met)' if a and b else 'does not read under key_1572 (gate not met)')
