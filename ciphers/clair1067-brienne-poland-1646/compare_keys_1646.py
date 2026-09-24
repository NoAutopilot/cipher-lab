#!/usr/bin/env python3
"""Compare key_1646.tsv with Tomokiyo's Brienne tables (1647, 1651), with fr5160's recovered key_1659.tsv and with the
signs of the fr5160 fol.1 (1653) inventory (24 Sept 2026). Writes compare_keys_1646.tsv, prints the counts.

  python3 compare_keys_1646.py
"""
import csv
from collections import Counter

F = '../fr5160-letellier-1653/'


def table(path, code='code', val=None):
    rows = list(csv.DictReader(open(path), delimiter='\t'))
    val = val or [k for k in rows[0] if k != code][0]
    d = {}
    for r in rows:
        d.setdefault(r[code], []).append(r[val].lower())
    return d


def plain(v):
    return v.lower().replace('v', 'u').replace('j', 'i')


k46 = {r['code']: r for r in csv.DictReader(open('key_1646.tsv'), delimiter='\t')}
others = {'1647': table('key_brienne_1647.tsv'), '1651': table('key_brienne_1651.tsv'),
          '1659': table(F + 'key_1659.tsv')}
inv53 = Counter(r['token'] for r in csv.DictReader(open(F + 'ciphertext_f1.tsv'), delimiter='\t')
                if not r['token'].startswith('[PLAIN'))
out = []
tally = {k: Counter() for k in others}
for code, r in k46.items():
    v = plain(r['value'])
    row = [code, r['value'], r['evidence'], r['occurrences']]
    for name, t in others.items():
        tv = t.get(code) or t.get(code.strip('_'))
        if tv is None:
            row.append(''); tally[name]['sign absent'] += 1
        else:
            same = any(plain(x) == v for x in tv)
            row.append(('SAME ' if same else 'diff ') + '|'.join(tv))
            tally[name]['same value' if same else 'different value'] += 1
    row.append(str(inv53.get(code, 0)))
    out.append(row)
with open('compare_keys_1646.tsv', 'w') as f:
    f.write('code\tvalue_1646\tevidence\toccurrences\ttomokiyo_1647\ttomokiyo_1651\tfr5160_key_1659\tfr5160_f1_1653_tokens\n')
    for row in out:
        f.write('\t'.join(row) + '\n')
for name, c in tally.items():
    print(name, dict(c))
print('signs of key_1646 present in the fr5160 fol.1 (1653) inventory:', sum(1 for r in out if r[-1] != '0'), '/', len(out))
