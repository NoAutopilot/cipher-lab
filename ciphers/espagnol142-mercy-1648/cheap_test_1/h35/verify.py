"""H35: per-correction script verifier. For each candidate key change in h33/answers.json (controls A, B, D: true =
wrong glyph -> majority truth letter, decoy = least-cost wrong move of a right glyph; C = target: M2's key.tsv
corrections vs decoys), apply the change alone to the packet's blind key and measure
  (a) wseg: Viterbi word-segmentation log-likelihood of the whole decode under an es17c7 word-unigram model
      (words with >= 2 corpus occurrences; an unknown chunk costs -12 - 3*len),
  (b) lex4: letters covered by in-vocabulary words of 4+ letters in that segmentation (H14's measure, unsegmented form).
Pre-registered rule: accept iff the delta is > 0. Gate: controls pooled true-accept >= 0.8 and decoy-reject >= 0.8 on
either measure; the target is scored only then (this script prints C last, after the gate line)."""
import sys,json,csv,glob,gzip,re,math
from collections import Counter
sys.path.insert(0,'../../../tools'); import homophonic_anneal as H
wc=Counter()
for f in sorted(glob.glob('../../../tools/data/es17c7/*.txt.gz')):
    for w in re.findall(r"[^\W\d_]+",gzip.open(f,'rt',encoding='utf-8').read()):
        w=H.fold(w)
        if w: wc[w]+=1
V={w:c for w,c in wc.items() if c>=2 and len(w)<=20}; N=sum(V.values()); LP={w:math.log(c/N) for w,c in V.items()}
def seg(t):
    n=len(t); best=[0.0]+[-1e18]*n; back=[0]*(n+1)
    for j in range(1,n+1):
        for i in range(max(0,j-20),j):
            w=t[i:j]; s=best[i]+(LP[w] if w in LP else -12-3*len(w))
            if s>best[j]: best[j],back[j]=s,i
    ws=[]; j=n
    while j>0: ws.append(t[back[j]:j]); j=back[j]
    ws.reverse(); return best[n], sum(len(w) for w in ws if len(w)>=4 and w in LP)
CASES={'A':('h27/blind_seed1_n0.05.json','h27/ctl_seed1_n0.05.tsv'),'B':('h27/blind_seed2_n0.1.json','h27/ctl_seed2_n0.1.tsv'),
       'D':('h27/blind_seed3_n0.05.json','h27/ctl_seed3_n0.05.tsv'),'C':('target_marks_es17c7_seed2.json','../cipher_codes.tsv')}
ans=json.load(open('h33/answers.json')); out=[]; tally={m:{'true':[0,0],'decoy':[0,0]} for m in ('wseg','lex4')}
def run(lab):
    j,t=CASES[lab]; key=json.load(open(j))['key']; seq=[r['sign'] for r in csv.DictReader(open(t),delimiter='\t')]
    b0,l0=seg(''.join(key[x] for x in seq)); rows=[]
    for kid,x,f,to,kind,n in ans[lab]:
        k2=dict(key); k2[x]=to; b,l=seg(''.join(k2[z] for z in seq)); rows.append((kid,x,f,to,kind,n,b-b0,l-l0))
    return rows
for lab in 'ABD':
    for r in run(lab):
        out.append((lab,)+r)
        for m,d in (('wseg',r[6]),('lex4',r[7])): tally[m][r[4]][0]+=d>0; tally[m][r[4]][1]+=1
gate=False
for m in tally:
    ta=tally[m]['true'][0]/tally[m]['true'][1]; dr=1-tally[m]['decoy'][0]/tally[m]['decoy'][1]
    print(f'CONTROLS {m}: true-accept {ta:.2f} ({tally[m]["true"][0]}/{tally[m]["true"][1]}), decoy-reject {dr:.2f}')
    gate|= ta>=0.8 and dr>=0.8
print('GATE', 'MET' if gate else 'NOT MET')
if gate:
    for r in run('C'): out.append(('C',)+r)
with open('h35/deltas.tsv','w') as f:
    f.write('packet\tid\tglyph\tfrom\tto\tkind\tn\td_wseg\td_lex4\n')
    for r in out: f.write('\t'.join(str(round(v,2)) if isinstance(v,float) else str(v) for v in r)+'\n')
