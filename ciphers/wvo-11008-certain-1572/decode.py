#!/usr/bin/env python3
"""Decode WVO 11008 (12 Aug 1572) numeral runs with the 1572 Orange-Nassau table and run the shuffled-key control.

  python3 decode.py            write reading.txt and control.tsv
  python3 decode.py --check    exit 1 if the committed reading.txt / control.tsv are stale (rule 7)

Key: ../jan-van-nassau-1572-75/key_1572.tsv (the printed 1572 table: letters = multiples of 3, other numbers null;
same table as ../orange-nassau-1572/key_nepveu.tsv). Codes outside the key print as [n].
Control (rule 3): the 23 letter values are permuted among the 23 letter codes (nulls fixed), 1000 seeded shuffles; the
statistic is letters covered by French words of 4+ letters from tools/data/fr16 (Catherine de Medicis, Marguerite de
Valois letters) plus a fixed 16th-century Low-Countries place list -- a statistic a shuffled key can change.
A third figure is the mean log10 4-gram probability per letter under the fr16 corpus (no word list).
The place list was written after the decode was seen (post hoc), so a second figure scores fr16 words only.
"""
import csv, gzip, glob, os, random, re, sys
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, '..', '..')
key = {}
for r in csv.DictReader(open(os.path.join(H, '..', 'jan-van-nassau-1572-75', 'key_1572.tsv')), delimiter='\t'):
    key[int(r['code'])] = r['value']
runs = {}
for r in csv.DictReader(open(os.path.join(H, 'ciphertext.tsv')), delimiter='\t'):
    runs.setdefault(int(r['run']), []).append(int(r['code']))
def dec(k, codes):
    out = []
    for c in codes:
        v = k.get(c)
        if v is None: out.append(f'[{c}]')
        elif v == 'NULL': continue
        elif v == '?': out.append('?')
        else: out.append(v)
    return ''.join(out)
vocab = set()
for f in sorted(glob.glob(os.path.join(R, 'tools', 'data', 'fr16', '*.gz'))):
    for w in re.findall(r'[a-zàâçéèêëîïôûùü]+', gzip.open(f, 'rt', errors='replace').read().lower()):
        w = w.translate(str.maketrans('àâçéèêëîïôûùüjvw', 'aaceeeeiiouuuiuu'))
        if len(w) >= 4: vocab.add(w)
PLACES = {'holstein', 'vlissinghen', 'flessingue', 'armuyden', 'ermuyden', 'arnemuyden', 'middelbourg', 'zelande',
          'anvers', 'bruxelles', 'malines', 'mons', 'tournay', 'cologne', 'brielle', 'enchuyse', 'hollande'}
VOCAB_FR = set(vocab)
import math
from collections import Counter
_txt = ''
for f in sorted(glob.glob(os.path.join(R, 'tools', 'data', 'fr16', '*.gz'))):
    _txt += gzip.open(f, 'rt', errors='replace').read().lower()
_txt = re.sub(r'[^a-z]', '', _txt.translate(str.maketrans('àâçéèêëîïôûùüjvwy', 'aaceeeeiiouuuiuui')))
Q4 = Counter(_txt[i:i + 4] for i in range(len(_txt) - 3)); Q3 = Counter(_txt[i:i + 3] for i in range(len(_txt) - 2))
def q4(s):
    s = re.sub(r'[^a-z]', '', s.translate(str.maketrans('jvwy', 'iuui'))); n = 0; t = 0.0
    for i in range(len(s) - 3):
        t += math.log10((Q4[s[i:i + 4]] + 0.1) / (Q3[s[i:i + 3]] + 2.6)); n += 1
    return t, n
vocab |= PLACES
def norm(s): return re.sub(r'[^a-z]', '', s.replace('j', 'i').replace('v', 'u').replace('w', 'u'))
VOC = {norm(w) for w in vocab}
VOC_FR = {norm(w) for w in VOCAB_FR}
def cover(s, V=None):
    V = VOC if V is None else V
    s = norm(s); hit = [0] * len(s)
    for i in range(len(s)):
        for j in range(i + 4, min(len(s), i + 14) + 1):
            if s[i:j] in V:
                for t in range(i, j): hit[t] = 1
    return sum(hit)
def qscore(k):
    t = n = 0
    for c in runs.values():
        a, b = q4(re.sub(r'\[\d+\]|\?', '', dec(k, c))); t += a; n += b
    return t / max(n, 1)
def score(k, V=None): return sum(cover(re.sub(r'\[\d+\]|\?', '', dec(k, c)), V) for c in runs.values())
lines = [f'run {n}: {dec(key, c)}' for n, c in sorted(runs.items())]
real = score(key)
letter_codes = [c for c, v in key.items() if v not in ('NULL', '?')]
vals = [key[c] for c in letter_codes]
sh = []; sh2 = []; sh3 = []; real2 = score(key, VOC_FR); real3 = qscore(key)
for seed in range(1000):
    rnd = random.Random(seed); v = vals[:]; rnd.shuffle(v)
    k2 = dict(key); k2.update(zip(letter_codes, v)); sh.append(score(k2)); sh2.append(score(k2, VOC_FR)); sh3.append(qscore(k2))
sh.sort(); mean = sum(sh) / len(sh); p95 = sh[int(0.95 * len(sh))]; ge = sum(1 for x in sh if x >= real)
sh3.sort(); ge3 = sum(1 for x in sh3 if x >= real3)
sh2.sort(); ge2 = sum(1 for x in sh2 if x >= real2)
letters = sum(len(norm(re.sub(r'\[\d+\]|\?', '', dec(key, c)))) for c in runs.values())
reading = '\n'.join(lines) + '\n'
control = ('stat\tvalue\nletters_decoded\t%d\nreal_word_cover\t%d\nshuffle_n\t1000\nshuffle_mean\t%.2f\nshuffle_p95\t%d\n'
           'shuffle_max\t%d\nshuffles_ge_real\t%d\n'
           'fr16_only_real\t%d\nfr16_only_shuffle_mean\t%.2f\nfr16_only_shuffle_p95\t%d\nfr16_only_ge_real\t%d\n'
           'q4_real\t%.3f\nq4_shuffle_mean\t%.3f\nq4_shuffle_p95\t%.3f\nq4_ge_real\t%d\n'
           % (letters, real, mean, p95, sh[-1], ge, real2, sum(sh2) / len(sh2), sh2[int(0.95 * len(sh2))], ge2,
              real3, sum(sh3) / len(sh3), sh3[int(0.95 * len(sh3))], ge3))
if '--check' in sys.argv:
    ok = all(os.path.exists(os.path.join(H, f)) and open(os.path.join(H, f)).read() == t
             for f, t in (('reading.txt', reading), ('control.tsv', control)))
    print('OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(os.path.join(H, 'reading.txt'), 'w').write(reading); open(os.path.join(H, 'control.tsv'), 'w').write(control)
print(reading + control)
