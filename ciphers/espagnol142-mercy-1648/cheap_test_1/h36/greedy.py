"""H36 selection control: M2's corrections were chosen by a reader to make words, so a large word-model gain could be
selection, not truth. Greedy hill-climb on H35's wseg: 12 single-glyph re-letterings (the size of M2's set), each the
best available move, from each blind key. On controls: the gain reached and how many of the moves are right (truth
key). On the target: the gain reached and how many moves agree with key.tsv. If greedy wseg gains on controls exceed
the true-set gains with mostly wrong moves, the target's M2 gain is not evidence by itself."""
import json,csv,collections
src=open('h35/verify.py').read().split("CASES=")[0]; ns={}; exec(src,ns); seg=ns['seg']
ALPHA='abcdefghilmnopqrstuxyz'
ref={r['code']:r['letter'] for r in csv.DictReader(open('../key.tsv'),delimiter='\t')}
CASES={'A':('h27/blind_seed1_n0.05.json','h27/ctl_seed1_n0.05.tsv','h21/vowelctl_cartas13_seed1.tsv.plain'),
       'B':('h27/blind_seed2_n0.1.json','h27/ctl_seed2_n0.1.tsv','h21/vowelctl_cartas13_seed2.tsv.plain'),
       'D':('h27/blind_seed3_n0.05.json','h27/ctl_seed3_n0.05.tsv','h21/vowelctl_cartas13_seed3.tsv.plain'),
       'C':('target_marks_es17c7_seed2.json','../cipher_codes.tsv',None)}
for lab,(j,t,p) in CASES.items():
    key=json.load(open(j))['key']; seq=[r['sign'] for r in csv.DictReader(open(t),delimiter='\t')]
    if p:
        by=collections.defaultdict(collections.Counter)
        for x,q in zip(seq,open(p).read().strip()): by[x][q]+=1
        truth={x:c.most_common(1)[0][0] for x,c in by.items()}
    else: truth={x:(ref[x] if ref.get(x,'_')!='_' else key[x]) for x in key}
    pl=lambda k: seg(''.join(k[x] for x in seq))[0]/len(seq)
    k=dict(key); b=pl(k); cur=b; moves=[]
    for step in range(12):
        best=None
        for g in set(seq):
            for a in ALPHA:
                if a==k[g]: continue
                k2=dict(k); k2[g]=a; s=pl(k2)
                if best is None or s>best[0]: best=(s,g,a)
        if best[0]<=cur: break
        cur=best[0]; k[best[1]]=best[2]; moves.append((best[1],key[best[1]],best[2],truth[best[1]]==best[2]))
    tr=pl(truth)
    print(f'{lab}: blind {b:.3f} greedy-12 {cur:.3f} (gain {cur-b:+.3f}); {"truth" if p else "key.tsv"} {tr:.3f} (gain {tr-b:+.3f}); moves right/agreeing {sum(m[3] for m in moves)}/{len(moves)}: {moves}',flush=True)
