#!/usr/bin/env python3
"""Held-out check, 24 Sept 2026: the key is estimated from f.86 only (align_f86.em); the f.88 cipher (which f.87
paragraph 2 deciphers, up to "celle la" where f.88's cipher breaks off) is aligned to that paragraph under the f.86
counts, and each f.88 group's f.86 key value is compared with the letters the alignment gives it."""
import csv
from collections import Counter
import align_f86 as A

counts, _ = A.em(A.segments())
key = {g: c.most_common(1)[0][0] for g, c in counts.items()}
toks = [r for r in csv.DictReader(open('ciphertext_f88.tsv'), delimiter='\t') if not r['group'].startswith('[') and r['group'] != 'M.r']
cut = [i for i, r in enumerate(toks) if r['group'] == '[mais]']
lines = open('dechiffre_f87.txt').read().split('\n')[14:]
p2 = ' '.join(lines)
p2 = p2[p2.index('de Savoye'):p2.index('celle la, et') + len('celle la')]
before, after = p2.split('mais', 1)
segs = []
allt = [r for r in csv.DictReader(open('ciphertext_f88.tsv'), delimiter='\t') if r['line'] <= 'L08']   # f.88 proper; L09+ is the canvas 173 tail
cur, parts = [], []
for r in allt:
    if r['group'] == '[mais]':
        parts.append(cur); cur = []
    elif not r['group'].startswith('[') and r['group'] != 'M.r':
        cur.append(r['group'])
parts.append(cur)
tot = Counter({g: sum(c.values()) for g, c in counts.items()})
score = A.make_score(counts, tot)
same = keyed = n = 0
rows = []
for gs, text in zip(parts, (A.norm(before), A.norm(after))):
    al, _ = A.viterbi(gs, text, score)
    for g, a in zip(gs, al):
        n += 1
        if g in key:
            keyed += 1
            same += key[g] == a
        rows.append((g, key.get(g, '?'), a))
print('f.88 groups', n, 'keyed from f.86', keyed, 'key value = aligned letters', same)
with open('holdout_f88.tsv', 'w') as f:
    f.write('group\tf86_key_value\taligned_to_f87_para2\n')
    for r in rows:
        f.write('\t'.join(r) + '\n')

# Control: the same f.88 groups aligned, under the same f.86 counts, to paragraph 2 with its letters shuffled (seeds 0-4)
import random
for seed in range(5):
    r = random.Random(seed); s2 = 0
    for gs, text in zip(parts, (A.norm(before), A.norm(after))):
        t = ''.join(r.sample(text, len(text)))
        al, _ = A.viterbi(gs, t, score)
        s2 += sum(1 for g, a in zip(gs, al) if g in key and key[g] == a)
    print('control seed', seed, 'key value = aligned letters', s2, '/', keyed)
