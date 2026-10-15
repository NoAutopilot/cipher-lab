#!/usr/bin/env python3
"""NOAI-CH (PREREG-NOAICH.md): c231's clear opening vs Charriere III p.207 n.1, with a whole-volume window control
and a shuffled-order control; G2 length band. Reads the disk copy only.
  python3 ciphers/fr16142-noailles-constantinople-1571/scripts/noaich_g1.py"""
import gzip, re, random, unicodedata, statistics, sys
SRC = 'sources/ia-fulltext/print-check/ngociationsdel03charuoft_djvu.txt.gz'
C231 = "Le gain de ceste grande bataille advenue en saison incommode".split()
def norm(w):
    w = unicodedata.normalize('NFD', w.lower()); w = ''.join(c for c in w if not unicodedata.combining(c))
    w = w.replace('v', 'u').replace('j', 'i').replace('y', 'i')
    return re.sub(r'[^a-z]', '', w)
def ed(a, b):
    p = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        c = [i]
        for j, cb in enumerate(b, 1): c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (ca != cb)))
        p = c
    return p[-1]
def score(x, y): return sum(1 for a, b in zip(x, y) if ed(a, b) <= 1)
raw = gzip.open(SRC, 'rt', encoding='utf-8', errors='replace').read().split('\n')
text = '\n'.join(raw)
text = re.sub(r'-\s*\n\s*', '', text)                      # rejoin line-end hyphenation
words = [norm(w) for w in re.split(r"[\s'’]+", text)]
words = [w for w in words if w]
c = [norm(w) for w in C231]
# target: footnote quote start, located from raw lines 15718-15745 (NOAI-C262), quote opens at "a  Le  gain"
fn = re.sub(r'-\s*\n\s*', '', '\n'.join(raw[15700:15760]))
q = fn[re.search(r'Le\s+gain', fn).start():]; q = q[:q.index('marché') + len('marché')]
qw = [norm(w) for w in re.split(r"[\s'’]+", q) if norm(w)]
tgt = score(c, qw[:9])
# locate target window index in volume to exclude it
starts = [i for i in range(len(words) - 8) if words[i:i + 3] == qw[:3]]
ctrl = [score(c, words[i:i + 9]) for i in range(len(words) - 8) if not any(abs(i - s) < 9 for s in starts)]
rnd = random.Random(1); sh = []
for _ in range(1000):
    t = qw[:9][:]; rnd.shuffle(t); sh.append(score(c, t))
sh.sort(); p95 = sh[int(0.95 * len(sh)) - 1]
mx = max(ctrl)
print(f"target words: {' '.join(qw[:9])}")
print(f"G1 target {tgt}/9; control(a) windows {len(ctrl)} max {mx}/9 mean {statistics.mean(ctrl):.3f} (n>=5: {sum(s>=5 for s in ctrl)}); control(b) p95 {p95}/9 max {max(sh)}/9")
g1 = tgt >= 8 and mx <= 4 and p95 <= 4
print('G1', 'PASS' if g1 else 'FAIL')
letters = len(re.sub(r'[^a-z]', '', ''.join(qw)))
print(f"footnote quote: {len(qw)} words, {letters} letters")
r = [letters / e for e in (1500, 3000)]
band = 'WHOLE' if all(0.8 <= x <= 1.25 for x in r) else 'PART' if all(x < 0.8 for x in r) else 'UNDECIDED'
print(f"G2 R = {r[0]:.3f} (est 1500), {r[1]:.3f} (est 3000): {band}")
