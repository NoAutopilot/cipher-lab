"""H31: does a stretch read better as letters around word codes? Remove the nomenclature-range tokens (48/52/65/72),
score the remaining key.tsv letters with the es17c7 trigram (tools/homophonic_anneal.py score, uni_w 0: local n-gram
only), and compare the gain with 1,000 draws removing the same number of random non-nomenclature positions."""
import sys,csv,glob,gzip,random
sys.path.insert(0,'../../tools'); import homophonic_anneal as H
M=H.Model([gzip.open(f,'rt',encoding='utf-8').read() for f in sorted(glob.glob('../../tools/data/es17c7/*.txt.gz'))],3)
key={r['code']:r['letter'] for r in csv.DictReader(open('key.tsv'),delimiter='\t')}
rows=list(csv.DictReader(open('cipher_codes_522.tsv'),delimiter='\t'))
NOM={'48','52','65','72'}
def sc(t): return H.score(M,t,0.0)/max(1,len(t)-2)   # per-trigram mean, so removal length does not bias
for lines in (['r16','r17'],['r20'],['r24']):
    toks=[r['sign'] for r in rows if r['line'] in lines]
    let=[key.get(x,'_') for x in toks]
    nom=[i for i,x in enumerate(toks) if x in NOM]; rest=[i for i in range(len(toks)) if i not in nom]
    base=sc(''.join(let)); drop=lambda S:''.join(l for i,l in enumerate(let) if i not in S)
    obs=sc(drop(set(nom)))-base
    rng=random.Random(31); null=sorted(sc(drop(set(rng.sample(rest,len(nom)))))-base for _ in range(1000))
    p=sum(v>=obs for v in null)/1000
    print(f'{"+".join(lines)}: n={len(toks)} nomen at {[i+1 for i in nom]} ({[toks[i]+"="+let[i] for i in nom]}); text {"".join(let)}')
    print(f'   gain per trigram {obs:+.3f}; random-removal median {null[500]:+.3f}, p95 {null[949]:+.3f}; P(null>=obs) {p:.3f}')
    print(f'   without: {drop(set(nom))}')
