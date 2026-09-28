"""H40 pre-registered rule (fixed in CAMPAIGN.md H40 before these controls existed): accept a candidate key change iff
H35's wseg delta > 0 OR H37's design-violation count falls. Candidates per fresh control: true = wrong glyph -> majority
truth letter, decoys = least-cost es17c7 trigram moves of right glyphs matched on occurrence counts (h33/build.py's
recipe). Gate: true-accept >= 0.8 and decoy-reject >= 0.8 on glyphs with 2+ occurrences, pooled over seeds 11-13.
Target (h33/answers.json C: M2's corrections and its decoys) scored only if the gate is met."""
import json,csv,glob,gzip,sys,collections
sys.path.insert(0,'../../../tools'); import homophonic_anneal as H
ns={}; exec(open('h35/verify.py').read().split("CASES=")[0],ns); seg=ns['seg']
ns2={}; exec(open('h37/design.py').read().split("def run")[0],ns2); V=ns2['V']
M=H.Model([gzip.open(f,'rt',encoding='utf-8').read() for f in sorted(glob.glob('../../../tools/data/es17c7/*.txt.gz'))],3)
ALPHA='abcdefghilmnopqrstuxyz'
def cands(key,seq,truth):
    cnt=collections.Counter(seq); true=[(x,truth[x]) for x in cnt if key[x]!=truth[x]]; pool=[x for x in cnt if key[x]==truth[x]]
    dec=[]
    for x,_ in sorted(true,key=lambda z:-cnt[z[0]]):
        g=min((y for y in pool if y not in [d for d,_ in dec]),key=lambda y:(abs(cnt[y]-cnt[x]),y)); best=None
        for a in ALPHA:
            if a==key[g]: continue
            k2=dict(key); k2[g]=a; sc=H.score(M,''.join(k2[z] for z in seq),1.0)
            if best is None or sc>best[0]: best=(sc,a)
        dec.append((g,best[1]))
    return [(x,to,'true',cnt[x]) for x,to in true]+[(g,to,'decoy',cnt[g]) for g,to in dec]
def judge(key,seq,cs):
    cnt=collections.Counter(seq); glyphs=[g for g in cnt if cnt[g]>=2]; w0=seg(''.join(key[x] for x in seq))[0]; v0=V(key,glyphs); out=[]
    for x,to,kind,n in cs:
        k2=dict(key); k2[x]=to; dw=seg(''.join(k2[z] for z in seq))[0]-w0; dv=V(k2,glyphs)-v0
        out.append((x,key[x],to,kind,n,round(dw,2),dv,dw>0 or dv<0))
    return out
tally={'true':[0,0],'decoy':[0,0]}; rows=[]
for s in (11,12,13):
    d=json.load(open(f'h40/blind_seed{s}.json')); key=d['key']; seq=[r['sign'] for r in csv.DictReader(open(f'h40/ctl_seed{s}.tsv'),delimiter='\t')]
    plain=open(f'h40/ctl_seed{s}.tsv.plain').read().strip(); by=collections.defaultdict(collections.Counter)
    for x,q in zip(seq,plain): by[x][q]+=1
    truth={x:c.most_common(1)[0][0] for x,c in by.items()}
    print(f'seed {s}: blind letters {sum(a==b for a,b in zip(d["decoded"],plain))/len(plain):.3f}')
    for r in judge(key,seq,cands(key,seq,truth)):
        rows.append((s,)+r)
        if r[4]>=2: tally[r[3]][0]+=r[7]; tally[r[3]][1]+=1
ta=tally['true'][0]/max(1,tally['true'][1]); dr=1-tally['decoy'][0]/max(1,tally['decoy'][1])
print(f'FRESH CONTROLS (n>=2): true-accept {ta:.2f} ({tally["true"][0]}/{tally["true"][1]}), decoy-reject {dr:.2f} ({tally["decoy"][1]-tally["decoy"][0]}/{tally["decoy"][1]})')
gate=ta>=0.8 and dr>=0.8; print('GATE','MET' if gate else 'NOT MET')
if gate:
    d=json.load(open('target_marks_es17c7_seed2.json')); key=d['key']; seq=[r['sign'] for r in csv.DictReader(open('../cipher_codes.tsv'),delimiter='\t')]
    cs=[(x,to,kind,n) for kid,x,f,to,kind,n in json.load(open('h33/answers.json'))['C']]
    for r in judge(key,seq,cs): rows.append(('C',)+r); print('  target',r, 'ACCEPT' if r[7] else 'reject')
with open('h40/verdicts.tsv','w') as f:
    f.write('packet\tglyph\tfrom\tto\tkind\tn\td_wseg\td_V\taccept\n'); [f.write('\t'.join(map(str,r))+'\n') for r in rows]
