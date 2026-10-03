# A2-COS2, 3 Oct 2026: align the letter-level f.12r gloss/group pairs of each blind pass and run the gloss-shuffle control.
# Usage: python3 ciphers/decode-1168-modena-costabili-1492/align/run_align.py <dir>  (reads <dir>/f12r_passA.tsv, f12r_passB.tsv; writes real*/sh* TSVs to <dir>)
import csv,re,random,sys,subprocess,collections
S=sys.argv[1]
def rows(p):
    out=[]
    for r in csv.DictReader(open(p),delimiter='\t'):
        g=re.sub(r'[^a-z]','',(r['gloss_above'] or '').lower())
        sg=[t.rstrip('*') for t in r['signs'].split() if t not in ('-',':','.')]
        sg=[t for t in sg if not t.isdigit() or len(t)==1]  # drop clear numerals 13, 30, 85
        if g and sg and 0.8<=len(sg)/len(g)<=1.25: out.append((r['crop'],g,sg))
    return out
def write(pairs,path):
    w=csv.writer(open(path,'w'),delimiter='\t',lineterminator='\n'); w.writerow(['plain_line','plain_raw','cipher_line','cipher_raw'])
    for i,(c,g,sg) in enumerate(pairs): w.writerow([c,g,'%s_%d'%(c,i),' '.join('@'+t for t in sg)])
def run(pairs,tag):
    write(pairs,f'{S}/{tag}_pairs.tsv')
    o=subprocess.run(['python3','tools/interlinear_align.py','align',f'{S}/{tag}_pairs.tsv',f'{S}/{tag}_align.tsv',f'{S}/{tag}_key.tsv','--code-prefix','@','--keep-fs'],capture_output=True,text=True).stdout
    st=collections.Counter(r['status'].split(':')[0] for r in csv.DictReader(open(f'{S}/{tag}_align.tsv'),delimiter='\t'))
    tot=sum(st.values()); return st.get('agrees',0)/tot if tot else 0, o.strip()
for p in 'AB':
    pr=rows(f'{S}/f12r_pass{p}.tsv'); real,o=run(pr,'real'+p)
    print(p,'pairs',len(pr),[ (c,g,' '.join(s)) for c,g,s in pr]); print(' real agree %.3f'%real,o)
    sh=[]
    for seed in range(20):
        random.seed(seed); gl=[g for _,g,_ in pr]; random.shuffle(gl)
        # keep length band: shuffled gloss trimmed/padded? use as-is
        sh.append(run([(c,g2,s) for (c,_,s),g2 in zip(pr,gl)],'sh%s'%p)[0])
    sh.sort(); print(' shuffle mean %.3f p95 %.3f'%(sum(sh)/len(sh),sh[18]))
