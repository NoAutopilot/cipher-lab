"""H33 verify mode: per packet, candidate key changes = true (controls: wrong glyph -> majority truth letter;
target: M2's key.tsv corrections) + the same number of decoys (a glyph whose blind letter is right -- for the target,
agrees with key.tsv -- moved to the alternative letter that costs the least es17c7 trigram score), decoys matched to the
true set's occurrence counts. Relabelled glyphs reuse h30/labelmaps.json; candidates shuffled; truth in h33/answers.json."""
import sys,json,csv,glob,gzip,random
from collections import Counter,defaultdict
sys.path.insert(0,'../../../tools'); import homophonic_anneal as H
texts=[gzip.open(f,'rt',encoding='utf-8').read() for f in sorted(glob.glob('../../../tools/data/es17c7/*.txt.gz'))]
M=H.Model(texts,3)
maps=json.load(open('h30/labelmaps.json'))
ref={r['code']:r['letter'] for r in csv.DictReader(open('../key.tsv'),delimiter='\t')}
CASES={'A':('h27/blind_seed1_n0.05.json','h27/ctl_seed1_n0.05.tsv','h21/vowelctl_cartas13_seed1.tsv.plain'),
       'B':('h27/blind_seed2_n0.1.json','h27/ctl_seed2_n0.1.tsv','h21/vowelctl_cartas13_seed2.tsv.plain'),
       'D':('h27/blind_seed3_n0.05.json','h27/ctl_seed3_n0.05.tsv','h21/vowelctl_cartas13_seed3.tsv.plain'),
       'C':('target_marks_es17c7_seed2.json','../cipher_codes.tsv',None)}
ALPHA='abcdefghilmnopqrstuxyz'
INSTR=open('h33/instructions.txt').read()
answers={}
for lab,(j,t,p) in CASES.items():
    d=json.load(open(j)); seq=[r['sign'] for r in csv.DictReader(open(t),delimiter='\t')]; key=d['key']; cnt=Counter(seq)
    if p:
        plain=open(p).read().strip(); by=defaultdict(Counter)
        for x,q in zip(seq,plain): by[x][q]+=1
        truth={x:c.most_common(1)[0][0] for x,c in by.items()}
        true=[(x,truth[x]) for x in by if key[x]!=truth[x]]; pool=[x for x in by if key[x]==truth[x]]
    else:
        true=[(x,ref[x]) for x in key if x in ref and ref[x] not in ('_',key[x])]; pool=[x for x in key if ref.get(x)==key[x]]
    base=H.score(M,''.join(key[x] for x in seq),1.0)
    decoys=[]
    for x,_ in sorted(true,key=lambda z:-cnt[z[0]]):
        g=min((y for y in pool if y not in [z for z,_ in decoys]),key=lambda y:(abs(cnt[y]-cnt[x]),y))
        best=None
        for a in ALPHA:
            if a==key[g]: continue
            k2=dict(key); k2[g]=a; sc=H.score(M,''.join(k2[z] for z in seq),1.0)
            if best is None or sc>best[0]: best=(sc,a)
        decoys.append((g,best[1]))
    cands=[(x,key[x],to,'true') for x,to in true]+[(g,key[g],to,'decoy') for g,to in decoys]
    random.Random(33+ord(lab)).shuffle(cands)
    m=maps[lab]; answers[lab]=[]
    lines=[INSTR,'',open(f'h30/packet_{lab}.txt').read().split('\n\n',1)[1],'CANDIDATE KEY CHANGES:']
    for i,(x,f,to,kind) in enumerate(cands,1):
        lines.append(f'K{i:02d}\t{m[x]}\t{f} -> {to}\t({cnt[x]} occurrences)'); answers[lab].append([f'K{i:02d}',x,f,to,kind,cnt[x]])
    open(f'h33/packet_{lab}.txt','w').write('\n'.join(lines)+'\n')
    print(lab,'true',len(true),'decoys',len(decoys))
json.dump(answers,open('h33/answers.json','w'),indent=0)
