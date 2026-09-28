"""H71: false-positive rate of the H41 list crib on read stretches of this letter. Windows of 62 tokens (the length
of r16:2-r18:21), step 8, over the whole cipher stream; excluded: any window overlapping the unread stretch
r16:2-r18:21, the unread v04, or a token of a name the reading spells in cipher (brandenburg, cleues, cheureuse; found
in the key.tsv letter stream). Each window scored with tools/crib_list_fit.py's rank/verdict on the 883-name list
(h61/names_bd1to6.tsv), default wildcards (non-S tokens). Counted: windows whose best fit is >= 7 with 0 mismatches
(Burgsdorf's H41 fit), and windows meeting the full candidate rule."""
import sys,csv
sys.path.insert(0,'../../tools'); import crib_list_fit as clf
toks=clf.load_window('cipher_codes_522.tsv','key.tsv',None,None)
locs=[t[2] for t in toks]; letters=''.join(t[0] for t in toks)
def idx(loc): return locs.index(loc)
bad=set(range(idx('r16:2'),idx('r18:21')+1))|{i for i,l in enumerate(locs) if l.startswith('v04:')}
for nm in ('brandenbur','cleues','cheureus'):
    p=letters.find(nm)
    while p!=-1:
        bad|=set(range(p,p+len(nm))); p=letters.find(nm,p+1)
names=[l.split('\t')[0] for l in open('h61/names_bd1to6.tsv') if l.strip()]
W=62; n=0; hits7=0; cands=0; rows=[]
for st in range(0,len(toks)-W+1,8):
    if any(i in bad for i in range(st,st+W)): continue
    n+=1; res=clf.rank(names,toks[st:st+W]); v=clf.verdict(res)
    strong=v['score']>=7 and v['mismatch']==0
    hits7+=strong; cands+=v['candidate']
    rows.append(f"{locs[st]}\t{v['best']}\t{v['score']}\t{v['agree']}/{v['mismatch']}\t{v['P']:.3f}\t{v['candidate']}")
open('h71/windows.tsv','w').write('start\tbest\tscore\tagree/mismatch\tP\tcandidate\n'+'\n'.join(rows)+'\n')
print(f'{n} read windows of {W} tokens; best fit >= 7 with 0 mismatches: {hits7}; full candidate rule met: {cands}')
sc=sorted((int(r.split('\t')[2]) for r in rows),reverse=True); print('best scores per window, top 10:',sc[:10])
