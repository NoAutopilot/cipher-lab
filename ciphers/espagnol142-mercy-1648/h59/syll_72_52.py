"""H59 (from h45/syll.py; codes 72 and 52; also prints the rank of the crib values). H45: if nomenclature codes stand for syllables (H41-H42's reading of 72 and 52), which one- or two-letter value of
48 and 65 reads best? Decode = key.tsv letters over cipher_codes_522.tsv (boxed 101 left as its blind letter a), scored
with H35's word-segmentation log-likelihood (es17c7 word unigram). For a code, try every value v in the 22 letters and
the 484 two-letter strings, substituted at all its occurrences; gain = best score - score with key.tsv's letter.
Control: 200 draws of k random S-graded token positions (k = the code's occurrence count), the same search for one
shared value at those positions; gain measured the same way. Pre-registered (CAMPAIGN.md H45): a value is a candidate
only if it improves each occurrence (per-occurrence deltas all > 0) and its gain beats the control's 95th percentile."""
import csv,random,sys
ns={}; exec(open('../cheap_test_1/h35/verify.py').read().split("CASES=")[0].replace("'../../../tools","'../../../tools"),ns)
seg=ns['seg']
key={r['code']:(r['letter'],r['grade']) for r in csv.DictReader(open('../key.tsv'),delimiter='\t')}
rows=list(csv.DictReader(open('../cipher_codes_522.tsv'),delimiter='\t')); seq=[r['sign'] for r in rows]
base=[key[x][0] if key.get(x,('_',''))[0]!='_' else 'a' for x in seq]
A='abcdefghilmnopqrstuxyz'; VALS=list(A)+[a+b for a in A for b in A]
def score(parts): return seg(''.join(parts))[0]
S0=score(base)
ALL={}
def best(pos,record=False):
    cur=[base[i] for i in pos]; out=None
    for v in VALS:
        p=list(base)
        for i in pos: p[i]=v
        sc=score(p)
        if record: ALL[v]=sc-S0
        if out is None or sc>out[0]: out=(sc,v)
    per=[]
    for i in pos:
        p=list(base); p[i]=out[1]; per.append(score(p)-S0)
    return out[0]-S0,out[1],per
rng=random.Random(45)
Spos=[i for i,x in enumerate(seq) if key.get(x,('','M'))[1]=='S']
for code in ('72','52'):
    pos=[i for i,x in enumerate(seq) if x==code]
    ALL.clear(); g,v,per=best(pos,True); order=sorted(ALL,key=lambda x:-ALL[x]); crib={'72':'do','52':'ro'}[code]; print(f'  {code}: crib value {crib} rank {order.index(crib)+1} of {len(order)}, gain {ALL[crib]:+.2f}; top 8 {[(x,round(ALL[x],2)) for x in order[:8]]}',flush=True)
    null=sorted(best(rng.sample(Spos,len(pos)))[0] for _ in range(int(sys.argv[1]) if len(sys.argv)>1 else 200))
    p95=null[int(0.95*len(null))-1]
    ctx=['%s:%s'%(rows[i]['line'],rows[i]['position']) for i in pos]
    ranks=None
    print(f'code {code} at {ctx} (key.tsv {key[code][0]}): best value "{v}" gain {g:+.2f}, per-occurrence {[round(x,2) for x in per]}; control gain median {null[len(null)//2]:+.2f} p95 {p95:+.2f}; candidate: {g>p95 and all(x>0 for x in per)}',flush=True)
