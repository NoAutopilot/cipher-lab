# RUN3-COSK, 4 Oct 2026: align R1166 P1 gloss/group pairs of each blind pass and run the gloss-shuffle control
# (same filter, statistic and control as ciphers/decode-1168-modena-costabili-1492/align/run_align.py; PREREG-RUN3-COSK.md).
# Usage: python3 ciphers/costabili-modena-1491/align/run_align.py <dir> [passA.tsv passB.tsv]  (writes real*/sh* TSVs to <dir>)
import csv,re,random,sys,subprocess,collections,json
S=sys.argv[1]; P=sys.argv[2:] or [f'{S}/r1166p1_passA.tsv',f'{S}/r1166p1_passB.tsv']
def rows(p):
    out=[]
    for r in csv.DictReader(open(p),delimiter='\t'):
        g=re.sub(r'[^a-z]','',(r['gloss_above'] or '').lower())
        sg=[re.sub(r'\*$','',t) for t in (r['signs'] or '').split() if t not in ('-',':','.')]
        sg=[t for t in sg if not t.isdigit() or len(t)==1]
        if g and sg and 0.8<=len(sg)/len(g)<=1.25: out.append((r['crop'],g,sg))
    return out
def write(pairs,path):
    w=csv.writer(open(path,'w'),delimiter='\t',lineterminator='\n'); w.writerow(['plain_line','plain_raw','cipher_line','cipher_raw'])
    for i,(c,g,sg) in enumerate(pairs): w.writerow([c,g,'%s_%d'%(c,i),' '.join('@'+t for t in sg)])
def run(pairs,tag):
    write(pairs,f'{S}/{tag}_pairs.tsv')
    subprocess.run(['python3','tools/interlinear_align.py','align',f'{S}/{tag}_pairs.tsv',f'{S}/{tag}_align.tsv',f'{S}/{tag}_key.tsv','--code-prefix','@','--keep-fs'],capture_output=True,text=True)
    st=collections.Counter(r['status'].split(':')[0] for r in csv.DictReader(open(f'{S}/{tag}_align.tsv'),delimiter='\t'))
    tot=sum(st.values()); return st.get('agrees',0)/tot if tot else 0
res={}
for tag,p in zip('AB',P):
    pr=rows(p); real=run(pr,'real'+tag); sh=[]
    for seed in range(20):
        random.seed(seed); gl=[g for _,g,_ in pr]; random.shuffle(gl)
        sh.append(run([(c,g2,s) for (c,_,s),g2 in zip(pr,gl)],'sh'+tag))
    sh.sort(); res[tag]=dict(pairs=len(pr),real=round(real,3),sh_mean=round(sum(sh)/len(sh),3),sh_p95=round(sh[18],3),gate=real>=sh[18]+0.20)
    run(pr,'real'+tag)  # leave the real key/alignment on disk
print(json.dumps(res))
