# GAPS18-na-suriname-map-1781 (account-4), 3 Oct 2026: align the two blind passes of the 4.VEL 2046 legend block
# (adapted from remN_merge.py). Plain tokens <...> other than punctuation are KEPT (labels No.1., a., numbers) so entries
# stay separable; punctuation <,> <.> and word separators are dropped (decode style concat).
import csv,difflib,sys
NORM={}   # reader-name unification, filled after reading both passes (each pairing listed in NOTES.md)
def toks_of(g):
    out=[]
    for t in g.replace('/',' ').split():
        if t in ('<,>','<.>','.',','): continue
        out.append(NORM.get(t,t))
    return out
def load(f):
    return {r['crop']:toks_of(r['glyphs']) for r in csv.DictReader(open(f),delimiter='\t')}
A=load('passes/leg2046_passA.tsv');B=load('passes/leg2046_passB.tsv')
out=[];tot=agree=0
for c in A:
    a,b=A[c],B.get(c,[]); sm=difflib.SequenceMatcher(None,a,b,autojunk=False); pos=0
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal':
            for t in a[i1:i2]: out.append((c,pos,t,'H','')); pos+=1; agree+=1; tot+=1
        else:
            for k in range(max(i2-i1,j2-j1)):
                ta=a[i1+k] if i1+k<i2 else '-'; tb=b[j1+k] if j1+k<j2 else '-'
                out.append((c,pos,ta if ta!='-' else tb,'M',f'A:{ta} B:{tb}')); pos+=1; tot+=1
    print(c,len(a),len(b),round(sm.ratio(),3))
print('agree',agree,'of',tot)
with open('passes/leg2046_merged.tsv','w') as f:
    f.write('crop\tpos\tsign\tconf\tnote\n')
    for r in out: f.write('\t'.join(map(str,r))+'\n')
