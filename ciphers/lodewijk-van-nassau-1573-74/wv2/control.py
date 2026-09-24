#!/usr/bin/env python3
"""Matched control for wv2/table_test.py (rule 3): encipher N letters of period French (the fr16 corpus, not these
letters) with R18's table (five homophones per letter, n at 1-5) under origin k, add a transcription-error rate e
(random numeral 1-120), cut into runs like the letter, and ask whether table_test finds k and scores it French.
  python3 wv2/control.py N K E [seed]"""
import sys, random, os, tempfile
sys.path.insert(0, os.path.dirname(__file__))
import table_test as tt
from french16_ngram import load, corpus_words
N, K, E = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]); seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1
rnd = random.Random(seed); ws = list(corpus_words()); st = rnd.randrange(len(ws) - 5000)
txt = ''.join(ws[st:st + 5000]).replace('W', 'VV').replace('J', 'I').replace('U', 'V')
txt = ''.join(c for c in txt if c in tt.ALPHA)[:N]
inv = {}
for n in range(1, 121): inv.setdefault(tt.ALPHA[((n - 1 - K) % 120) // 5], []).append(n)
nums = [rnd.choice(inv[c]) if rnd.random() >= E else rnd.randint(1, 120) for c in txt]
f = tempfile.NamedTemporaryFile('w', suffix='.tsv', delete=False)
f.write('line\tpos\tsign\tconf\n'); [f.write(f'L\t{i}\t{x}\tH\n') for i, x in enumerate(nums)]; f.close()
m = load(); rs = tt.runs(f.name)
sc = sorted((tt.score(m, rs, k), k) for k in range(120))
ok, tot = tt.french_share(f.name, K)
print(f'control N={N} K={K} e={E}: best k={sc[0][1]} {sc[0][0]:.2f} b/c (next {sc[1][0]:.2f}); French share at true k {100*ok/tot:.1f}%')
os.unlink(f.name)
