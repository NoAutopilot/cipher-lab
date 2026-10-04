# VER-GRACOS (account 3 verifier, 4 Oct 2026): per-sign joint null for the N8-COS C grades. Usage: python3 ciphers/costabili-modena-1491/align/ver_gracos_persign.py <scratch dir>
import sys,random,csv,collections,subprocess,json
sys.argv=['x',sys.argv[1]]
S=sys.argv[1]
exec(open('ciphers/costabili-modena-1491/align/run_align.py').read().split('res={}')[0])
def key(tag):
    d={}
    for r in csv.DictReader(open(f'{S}/{tag}_key.tsv'),delimiter='\t'): d[r['value']]=(r['meaning'],int(r['agree']))
    return d
C={'+':'a','T':'d','a':'i','b':'o','c':'p','d':'r','g':'l','o':'e','y':'n','z':'o','q':'c'}
P={'A':'ciphers/costabili-modena-1491/align/n8cos_passA_norm.tsv','B':'ciphers/costabili-modena-1491/align/n8cos_passB_norm.tsv'}
pr={t:rows(p) for t,p in P.items()}
N=100; hit=collections.Counter(); joint=collections.Counter()
for seed in range(N):
    ok={}
    for t in 'AB':
        random.seed(1000+seed); gl=[g for _,g,_ in pr[t]]; random.shuffle(gl)
        run([(c,g2,s) for (c,_,s),g2 in zip(pr[t],gl)],'ps'+t); k=key('ps'+t)
        ok[t]={s for s,v in C.items() if s in k and k[s][0]==v and k[s][1]>=2}
    for s in C:
        if s in ok['A'] and s in ok['B']: hit[s]+=1
print('per-sign joint null rate (both passes same claimed value, >=2 agree), N=%d'%N)
for s,v in C.items(): print(s,v,hit[s]/N)
