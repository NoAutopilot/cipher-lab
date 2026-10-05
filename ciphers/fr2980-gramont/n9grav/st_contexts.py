#!/usr/bin/env python3
"""N9-GRAV (5 Oct 2026): aligned print letter at every ST and every reader-split "?" on the fr.3040 no.6 rows carrying an ST
read by either pass, with key.tsv minus ST (so ST cannot steer the alignment). Run from the target folder:
  python3 n9grav/st_contexts.py > n9grav/st_contexts.txt"""
import sys
sys.path.insert(0,'n8gra2'); sys.path.insert(0,'n8gra3')
import score as S, score3 as S3
from pathlib import Path
key=S.load_key(); key.pop('ST',None)  # pre-N8-GRA3 key: ST unkeyed (wildcard)
rows={'n8gra2/recon.tsv':['f18r_L01'],'n8gra3/recon.tsv':['f18vA_L01','f18vA_L03','f18vB_L01','f18vB_L03','f18vB_L04','f18vC_L16','f19r_L02']}
# build blocks with row labels
for rf,want in rows.items():
    lines=[l.split('\t') for l in Path(rf).read_text().splitlines()[1:]]
    if 'n8gra2' in rf:
        bl={'S1':[(r,t) for r,c in lines if r in S.ROWS for t in c.split()]}; segs={'S1':S.load_print()}
    else:
        bl={}
        for r,c in lines:
            bl.setdefault(S3.BLOCK[r.split('_')[0]],[]).extend((r,t) for t in c.split())
        segs=S3.SEGS
    for s,rt in bl.items():
        rt=[(r,t) for r,t in rt if t not in ('/','.') and t]
        dec=S.decode([t for r,t in rt],key)
        # decode drops NULLs; rebuild row mapping
        keep=[(r,t) for r,t in rt if not (t in key and key[t]=='NULL')]
        assert len(keep)==len(dec)
        _,_,al=S.align_agree(dec,segs[s])
        for i,((r,t),(t2,v),a) in enumerate(zip(keep,dec,al)):
            if r in want and t in ('ST','?'):
                lo,hi=max(0,i-6),i+7
                ctx=' '.join(f"{dec[j][0]}={dec[j][1] or '*'}:{al[j]}" for j in range(lo,min(hi,len(dec))))
                print(f"{r} #{i} {t} -> {a}\n   {ctx}")
