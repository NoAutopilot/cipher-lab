# NO87-FOLLOW (3 Oct 2026): value-blind shuffled panels of the nos.71/86/90 T50/T46 tiles in followup_71_86_90.tsv, same
# protocol as mk.py (ids only, candidate-only sheet candidates.png reused), seed 1004. Window +-5 signs (lines here are not
# all evenly spaced, so the arrow is approximate; the neighbour ids locate the target). Tiles whose crops are not on disk
# (f185r2, gitignored, REGEN.sh needs a Gallica fetch) are listed as skipped. Run from harvest/:
#   python3 lookalike_87/no87_labels/mk_follow.py   -> follow_blind_*.jpg, follow_key.tsv, follow_neighbours.tsv
import csv,glob,random
from PIL import Image, ImageDraw
D='lookalike_87/no87_labels'
rows=list(csv.DictReader(open(f'{D}/followup_71_86_90.tsv'),delimiter='\t'))
cnt={}; seq={}
for f in ['ciphertext_f139v.tsv','ciphertext_no86.tsv','ciphertext_no90.tsv']:
    for r in csv.DictReader(open(f),delimiter='\t'):
        cnt[r['line']]=max(cnt.get(r['line'],0),int(r['pos'])); seq[(r['line'],int(r['pos']))]=r['sign']
def crop_prefix(line):
    p=line.split('_')
    if p[0]=='f139v': return f'f139v/{line}'
    fol,L=p[1],p[2]
    if fol=='f174r': return f'f174r/f174r_{L}'
    if fol=='f174v':
        n=int(L[1:]); return f'f174v/f174v_{L}' if n<=11 else f'f174vB/f174vB_L{n-11:02d}'
    if fol=='f175v': return f'f175v/f175v_L{L[1:]}'
    if fol=='f184r': return f'f184r/f184r_{L}'
    if fol=='f184v': return f'f184v/f184v_{L}'
    if fol=='f185r' and L in [f'L0{i}' for i in range(1,9)]: return f'f185r/f185r_{L}'
    return None
ok=[];skip=[]
for r in rows:
    pre=crop_prefix(r['line']); fs=sorted(glob.glob(pre+'_s*.jpg')) if pre else []
    (ok if fs else skip).append((r,fs))
random.seed(1004); random.shuffle(ok)
key=open(f'{D}/follow_key.tsv','w'); key.write('panel\tletter\tline\tpos\tlabel\tcrop\n')
nb=open(f'{D}/follow_neighbours.tsv','w'); nb.write('panel\tneighbours (target = [?])\n'); panels=[]
for i,(t,fs) in enumerate(ok):
    segs=[Image.open(f).convert('RGB') for f in fs]
    W=sum(s.size[0] for s in segs); H=max(s.size[1] for s in segs)
    line=Image.new('RGB',(W,H),'white'); x=0
    for s in segs: line.paste(s,(x,0)); x+=s.size[0]
    n=cnt[t['line']]; p=int(t['pos']); cx=int((p-0.5)/n*W); half=min(int(W/n*5.5),450)
    x0=max(0,cx-half); win=line.crop((x0,0,min(W,cx+half),H))
    sc=140/win.size[1] if win.size[1]<140 else 1.0
    win=win.resize((int(win.size[0]*sc),int(win.size[1]*sc)))
    lab=Image.new('RGB',(win.size[0],win.size[1]+34),'white'); lab.paste(win,(0,20)); d=ImageDraw.Draw(lab)
    pid=f'Q{i+1:02d}'; d.text((2,2),pid,fill='red')
    mx=int((cx-x0)*sc); d.polygon([(mx,lab.size[1]-2),(mx-6,lab.size[1]-12),(mx+6,lab.size[1]-12)],fill='red')
    c=[('[?]' if q==p else seq.get((t['line'],q),'')) for q in range(p-4,p+5)]; c=[x for x in c if x]; nb.write(pid+'\t'+' '.join(c)+'\n')
    panels.append(lab); key.write('\t'.join([pid,t['letter'],t['line'],t['pos'],t['label'],fs[0].rsplit('_s',1)[0]])+'\n')
for k in range((len(panels)+9)//10):
    ps=panels[k*10:(k+1)*10]; w=max(p.size[0] for p in ps); h=max(p.size[1] for p in ps)
    m=Image.new('RGB',(w,len(ps)*(h+8)),'white')
    for j,p in enumerate(ps): m.paste(p,(0,j*(h+8)))
    m.save(f'{D}/follow_blind_{k+1}.jpg',quality=90)
with open(f'{D}/follow_skipped.tsv','w') as f:
    f.write('line\tpos\tlabel\twhy\n')
    for t,_ in skip: f.write(f"{t['line']}\t{t['pos']}\t{t['label']}\tcrop not on disk (f185r2 crops gitignored; f185r2/REGEN.sh re-fetches, 1 Gallica request)\n")
print('panels',len(panels),'skipped',len(skip))
