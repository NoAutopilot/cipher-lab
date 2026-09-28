#!/usr/bin/env python3
"""Campaign step H3 (28 Sept 2026): anneal with the 29 S-graded key.tsv codes held, on the regenerated 522-token stream
(cipher_codes_522.tsv: ciphertext.tsv minus [PLAIN] tokens, current exceptions.tsv applied), vs M2's -1199.1 on the
521-token m2/cipher_codes_eyefix.tsv; a permuted-held-key control (same 29 codes held at a permutation of their
letters, at most 2 in place); a free anneal on the 522 stream. Prints scores and the free codes' values per run.
  python3 ciphers/espagnol142-mercy-1648/cheap_test_1/h3/analyse.py
"""
import json, glob, os, collections
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(H, '..', '..')
key = {r[0]: (r[1], r[2]) for r in [l.rstrip('\n').split('\t') for l in open(f'{T}/key.tsv')][1:]}
free_codes = [c for c, (v, g) in key.items() if g != 'S']
groups = [('held-29, 522 tokens, es17', 'held29_522_es17_seed?.json'), ('held-29, 522 tokens, es17c7', 'held29_522_es17c7_seed?.json'),
          ('held-29, M2 eyefix 521 tokens, es17 (reproduction of -1199.1)', 'held29_eyefix521_es17_seed1.json'),
          ('CONTROL permuted-held-29, 522, es17', 'permheld29_522_es17_seed?.json'), ('free anneal, 522, es17 (Y8 gave -1154.3 on 521)', 'free_522_es17_seed?.json')]
for name, pat in groups:
    print('==', name)
    for f in sorted(glob.glob(f'{H}/{pat}')):
        o = json.load(open(f)); k = o['key']
        vals = ' '.join(f'{c}={k.get(c, "?")}' for c in free_codes)
        print(f'  {os.path.basename(f)}: score {o["score"]:.1f} restarts {o["restart_scores"][:4]} | free codes: {vals}')
print('key.tsv M values:', ' '.join(f'{c}={key[c][0]}' for c in free_codes))
