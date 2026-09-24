#!/usr/bin/env python3
"""WV2 table test (LANE R2 W1, 24 Sept 2026): does a letter's numeral run read as French under R18's table
(n 1-5, o 6-10 ... m 116-120) or under the same table with a shifted origin?  Scripts read, models judge.
  python3 wv2/table_test.py CIPHERTEXT.tsv [...]   prints, per file, the best offsets k (number n reads as
  ALPHA[((n-1-k) mod 120)//5]) by French 5-gram bits/char over runs of numerals <=120, with k=0 (R18's table) first.
Control: the same score for ciphertext_sib.tsv (siblings, known to read at k=0) and for a shuffle of the file.
"""
import sys, os, csv, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'tools'))
from french16_ngram import load
ALPHA = 'NOPQRSTVVXYZABCDEFGHIKLM'.replace('VV', 'UV')  # n o p q r s t u v x y z a b c d e f g h i k l m
ALPHA = 'NOPQRSTVVXYZABCDEFGHIKLM'  # u and v fold to V in the model
def runs(path):
    rs, cur, last = [], [], None
    for r in csv.DictReader(open(path), delimiter='\t'):
        s = (r.get('sign') or r.get('token') or '').rstrip('?').strip("'")
        ln = r.get('line')
        if ln != last and False: pass
        last = ln
        if s.isdigit() and 1 <= int(s) <= 120:
            cur.append(int(s))
        elif s.isdigit():   # >120: name/null, keep the run going
            continue
        else:
            if len(cur) >= 4: rs.append(cur)
            cur = []
    if len(cur) >= 4: rs.append(cur)
    return rs
def score(m, rs, k):
    bits = n = 0
    for r in rs:
        t = ''.join(ALPHA[((x - 1 - k) % 120) // 5] for x in r)
        bits -= m.logp(t); n += len(t)
    return bits / max(n, 1)
def main():
    m = load()
    for p in sys.argv[1:]:
        rs = runs(p); N = sum(map(len, rs))
        sc = sorted((score(m, rs, k), k) for k in range(120))
        k0 = score(m, rs, 0)
        flat = [x for r in rs for x in r]; random.seed(1); random.shuffle(flat)
        sh = score(m, [flat], 0)
        print(f'{p}: {N} numerals in {len(rs)} runs; k=0 {k0:.2f} b/c; shuffled {sh:.2f}; best ' +
              ', '.join(f'k={k} {b:.2f}' for b, k in sc[:5]))
        if len(sys.argv) > 2 or True:
            b, k = sc[0]
            print('  sample at best k:', ' '.join(''.join(ALPHA[((x-1-k) % 120)//5] for x in r) for r in rs[:6])[:300])
            print('  sample at k=0   :', ' '.join(''.join(ALPHA[((x-1) % 120)//5] for x in r) for r in rs[:6])[:300])
def french_share(path, k=0, win=12, thr=4.0):
    """Share of numerals (<=120) lying in at least one window of `win` consecutive numerals that scores under `thr`
    bits/char under offset k: the per-letter 'reads as French' figure reported in NOTES.md 'W1'."""
    m = load(); rs = runs(path); ok = tot = 0
    for r in rs:
        t = ''.join(ALPHA[((x - 1 - k) % 120) // 5] for x in r); good = [False] * len(t)
        for i in range(0, max(1, len(t) - win + 1)):
            if -m.logp(t[i:i + win]) / len(t[i:i + win]) < thr:
                for j in range(i, min(len(t), i + win)): good[j] = True
        ok += sum(good); tot += len(t)
    return ok, tot

if __name__ == "__main__" and "--share" not in sys.argv: main()
if "--share" in sys.argv:
    for p in sys.argv[1:]:
        if p != "--share": ok, tot = french_share(p); print(f"{p}: {ok}/{tot} numerals in French-scoring windows ({100*ok/max(tot,1):.1f}%)")
