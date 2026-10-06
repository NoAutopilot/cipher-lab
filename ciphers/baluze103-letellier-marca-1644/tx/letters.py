#!/usr/bin/env python3
"""Show a pass (raw tx format) as plaintext letters via key.tsv, for the reconciler's sense check. Ambiguous -> (a/b)."""
import sys, re
key={}
for r in open('key.tsv',encoding='utf-8'):
    if r.startswith('#') or not r.strip(): continue
    c=r.rstrip('\n').split('\t'); key.setdefault(c[0],[]).append(c[1])
def val(t):
    if t.startswith('w:'): return '['+t[2:]+']'
    alts=[a for a in t.split('|') if a]
    vs=[]
    for a in alts:
        for v in key.get(a,['?'+a]):
            if v not in vs: vs.append(v)
    return vs[0] if len(vs)==1 else '('+'/'.join(vs)+')'
sys.path.insert(0,'tx'); from prep_passes import toks
for r in open(sys.argv[1],encoding='utf-8'):
    if r.startswith('#') or '\t' not in r: continue
    cid,t=r.rstrip('\n').split('\t',1)
    print(cid.ljust(13),' '.join(val(x.replace('|>','')) for x in toks(t)))
