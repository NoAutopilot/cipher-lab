#!/usr/bin/env python3
"""Offline test for tools/homophonic_anneal.py: a matched control (German 1562 plaintext from
ciphers/august-van-saksen-1561-64/align_74.txt, N=282, K=20, w as uu) must be read at >= 90 percent."""
import os, re, subprocess, sys, tempfile, json
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(R, 'ciphers', 'august-van-saksen-1561-64')
words = []
for l in open(os.path.join(D, 'align_74.txt'), encoding='utf-8'):
    if l.startswith('#') or ':' not in l:
        continue
    for w in l.split(':', 1)[1].split(';;'):
        if '|' in w:
            words.append(w.split('|')[1].replace(' ', ''))
with tempfile.TemporaryDirectory() as t:
    p = os.path.join(t, 'ctl.txt'); open(p, 'w').write(' '.join(words))
    o = os.path.join(t, 'o.json')
    subprocess.run([sys.executable, os.path.join(R, 'tools', 'homophonic_anneal.py'), '--control', p, '--signs', '20',
                    '--length', '282', '--corpus', os.path.join(R, 'tools', 'data', 'de16', 'composed_enhg.txt'),
                    '--corpus', os.path.join(D, 'plaintext_98.txt'), '--restarts', '3', '--iters', '200000',
                    '--w-as-uu', '--out', o], check=True, stdout=subprocess.DEVNULL)
    share = json.load(open(o))['share']
    assert share >= 0.9, share
    print('ok', share)

# allowed= restricts a sign's letters (vowel-indicator marks): the restricted sign never leaves its set
sys.path.insert(0, os.path.join(R, 'tools'))
import random, homophonic_anneal as ha
m = ha.Model([open(os.path.join(R, 'tools', 'data', 'de16', 'composed_enhg.txt'), encoding='utf-8').read()[:20000]])
_, k = ha.anneal(list('abcabcxyzxyz'), m, 2000, random.Random(1), 1.0, allowed={'x': 'aeiou', 'y': 'e'})
assert k['x'] in 'aeiou' and k['y'] == 'e', k
print('ok allowed')

# --noise (anneal_noisy, LANE R6 CM2, 25 Sept 2026): on a K=20, N=400 German control with 10 percent of the signs
# replaced by random signs, the error-tolerant solve returns a free set within its cap, letters from ALPHA, and reads
# the corrected text at >= 75 percent; the plain solve's reading of the same noisy input is printed beside it.
seq, p, truth = ha.make_control(open(os.path.join(D, 'plaintext_98.txt'), encoding='utf-8').read(), 20, 400, m, 3)
nr = random.Random(3); types = sorted(set(seq))
seqn = [nr.choice(types) if nr.random() < 0.1 else s for s in seq]
acc = lambda d: sum(a == b for a, b in zip(d, p)) / len(p)
sc, key, free = ha.solve(seqn, m, 3, 100000, 1, 1.0, noise=0.1)[0]
import math
assert len(free) <= math.ceil(1.5 * 0.1 * len(seqn)), len(free)
assert all(l in ha.ALPHA for l in free.values()) and all(0 <= i < len(seqn) for i in free)
dec = ''.join(free.get(i, key[x]) for i, x in enumerate(seqn))
plain_key = ha.solve(seqn, m, 3, 100000, 1, 1.0)[0][1]
plain_dec = ''.join(plain_key[x] for x in seqn)
print(f'ok noise: corrected {acc(dec):.1%} (key-only {acc("".join(key[x] for x in seqn)):.1%}, free {len(free)}), plain solver {acc(plain_dec):.1%}')
assert acc(dec) >= 0.75, acc(dec)
