#!/usr/bin/env python3
"""R8-HEL (6 Oct 2026): list every R1953 token in 801-1796 (image-check "all" stream) with a 0<->8 twin keyed in R4369 with a
different value. Run from ciphers/hellen-frederick-1752: python3 zero_eight/candidates.py > zero_eight/candidates.tsv"""
import csv,itertools
key={r['code']:(r['value'],r['grade']) for r in csv.DictReader(open('key_r4369/key_decode.tsv'),delimiter='\t')}
toks=[r for r in csv.DictReader(open('image_check_r1953/reading_R1953_all_tokens.tsv'),delimiter='\t')]
def twins(c):
    idx=[i for i,ch in enumerate(c) if ch in '08']
    out=set()
    for n in range(1,len(idx)+1):
        for sub in itertools.combinations(idx,n):
            s=list(c)
            for i in sub: s[i]='8' if s[i]=='0' else '0'
            out.add(''.join(s))
    return out
n=0
for t in toks:
    c=t['sign'].strip('_=?')
    if not c.isdigit(): continue
    v=int(c)
    if not (801<=v<=1796): continue
    tw=[w for w in twins(c) if 801<=int(w)<=1796 and w in key and key[w][0]!=key.get(c,('?',))[0]]
    if tw:
        n+=1
        print(t['line'],t['pos'],t['sign'],t['value'],t['grade'],' | '.join(f"{w}={key[w][0]}/{key[w][1]}" for w in tw),sep='\t')
print(n)
