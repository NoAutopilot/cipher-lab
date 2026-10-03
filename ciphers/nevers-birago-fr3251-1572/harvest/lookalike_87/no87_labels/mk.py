# NO87-LABELS (3 Oct 2026): value-blind shuffled montage of every no.87 tile labelled T50/T46/T98/T52 (42, tiles.tsv), panels
# P01-P42 only (no line, pos, label or sheet value), seed 1003; plus a candidate-only sheet (cells cut from
# sign_sheet_blind_1572.png, ids only, values never shown). Run from harvest/: python3 lookalike_87/no87_labels/mk.py
# Writes lookalike_87/no87_labels/{blind_1..3.jpg, candidates.png, key.tsv}. PIL only.
import csv,glob,random
from PIL import Image, ImageDraw
D='lookalike_87/no87_labels'
tiles=list(csv.DictReader(open('lookalike_87/tiles.tsv'),delimiter='\t'))
cnt={}; seq={}
for fol in ['f178r','f178v','f179r']:
    for r in csv.DictReader(open(f'ciphertext_{fol}.tsv'),delimiter='\t'):
        cnt[r['line']]=max(cnt.get(r['line'],0),int(r['pos'])); seq[(r['line'],int(r['pos']))]=r['sign']
random.seed(1003); random.shuffle(tiles)
key=open(f'{D}/key.tsv','w'); key.write('panel\tfolio\tline\tpos\tsign\tchunk\n'); nb=open(f'{D}/neighbours.tsv','w'); nb.write('panel\tneighbours (target = [?])\n'); panels=[]
for i,t in enumerate(tiles):
    fol=t['folio']; L=t['line'].split('_')[1]
    segs=[Image.open(f).convert('RGB') for f in sorted(glob.glob(f'{fol}/{fol}_{L}_s*.jpg'))]
    W=sum(s.size[0] for s in segs); H=max(s.size[1] for s in segs)
    line=Image.new('RGB',(W,H),'white'); x=0
    for s in segs: line.paste(s,(x,0)); x+=s.size[0]
    n=cnt[t['line']]; p=int(t['pos']); cx=int((p-0.5)/n*W); half=int(W/n*3.5)
    x0=max(0,cx-half); win=line.crop((x0,0,min(W,cx+half),H))
    sc=140/win.size[1] if win.size[1]<140 else 1.0
    win=win.resize((int(win.size[0]*sc),int(win.size[1]*sc)))
    lab=Image.new('RGB',(win.size[0],win.size[1]+34),'white'); lab.paste(win,(0,20)); d=ImageDraw.Draw(lab)
    pid=f'P{i+1:02d}'; d.text((2,2),pid,fill='red')
    mx=int((cx-x0)*sc); d.polygon([(mx,lab.size[1]-2),(mx-6,lab.size[1]-12),(mx+6,lab.size[1]-12)],fill='red')
    c=[('[?]' if q==p else seq.get((t['line'],q),'')) for q in range(p-3,p+4)]; c=[x for x in c if x]; nb.write(pid+'\t'+' '.join(c)+'\n')
    panels.append(lab); key.write('\t'.join([pid,fol,t['line'],t['pos'],t['sign'],t['chunk']])+'\n')
for k in range(3):
    ps=panels[k*14:(k+1)*14]; cols=2
    w=max(p.size[0] for p in ps); h=max(p.size[1] for p in ps)
    m=Image.new('RGB',(cols*w+20,((len(ps)+1)//2)*(h+8)),'white')
    for j,p in enumerate(ps): m.paste(p,((j%cols)*(w+20),(j//cols)*(h+8)))
    m.save(f'{D}/blind_{k+1}.jpg',quality=90)
sheet=Image.open('sign_sheet_blind_1572.png').convert('RGB')
ids=['T10','T11','T13','T15','T17','T18','T19','T24','T25','T26','T27','T29','T33','T36','T37','T38','T42','T45','T46','T49','T50','T51','T52','T53','T54','T55','T56','T57','T58','T60','T63','T64','T65','T66','T70','T76','T78','T80','T81','T83','T84','T85','T86','T88','T89','T90','T92','T95','T96','T97','T98']
cand=['T50','T92','T96','T46','T11','T15','T98','T18','T36','T45','T52','T13','T64','T38']
c=Image.new('RGB',(7*110,2*110),'white')
for j,cid in enumerate(cand):
    k=ids.index(cid); cell=sheet.crop(((k%9)*110,(k//9)*110,(k%9)*110+110,(k//9)*110+110)); c.paste(cell,((j%7)*110,(j//7)*110))
c.save(f'{D}/candidates.png'); print('ok',len(panels))
