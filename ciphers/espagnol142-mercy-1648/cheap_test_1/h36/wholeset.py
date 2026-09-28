"""H36: the whole correction set at once. Word-segmentation log-likelihood per letter (H35's wseg, es17c7 word unigram)
for: blind decode; blind + all true corrections (controls: truth key; target: key.tsv, '_' codes left at the blind
letter); blind + all decoys at once (h33/answers.json); and 20 shuffled keys (the corrected key's letters permuted
among glyphs). The question: is the target's gain from M2's set inside the controls' true-set gains and above their
decoy-set gains?"""
import sys,json,csv,random
sys.path.insert(0,'h35'); sys.argv=[sys.argv[0]]
import importlib.util
spec=importlib.util.spec_from_file_location('v','h35/verify.py')
src=open('h35/verify.py').read().split("CASES=")[0]; ns={}; exec(src,ns); seg=ns['seg']
ans=json.load(open('h33/answers.json'))
CASES={'A':('h27/blind_seed1_n0.05.json','h27/ctl_seed1_n0.05.tsv'),'B':('h27/blind_seed2_n0.1.json','h27/ctl_seed2_n0.1.tsv'),
       'D':('h27/blind_seed3_n0.05.json','h27/ctl_seed3_n0.05.tsv'),'C':('target_marks_es17c7_seed2.json','../cipher_codes.tsv')}
for lab in 'ABDC':
    j,t=CASES[lab]; key=json.load(open(j))['key']; seq=[r['sign'] for r in csv.DictReader(open(t),delimiter='\t')]
    pl=lambda k: seg(''.join(k[x] for x in seq))[0]/len(seq)
    tru=dict(key); dec=dict(key)
    for kid,x,f,to,kind,n in ans[lab]:
        (tru if kind=='true' else dec)[x]=to
    b,tt,dd=pl(key),pl(tru),pl(dec)
    rng=random.Random(36); sh=[]
    for _ in range(20):
        g=list(tru); v=[tru[x] for x in g]; rng.shuffle(v); sh.append(pl(dict(zip(g,v))))
    print(f'{lab}: blind {b:.3f}  +true set {tt:.3f} (gain {tt-b:+.3f})  +decoy set {dd:.3f} (gain {dd-b:+.3f})  shuffled keys {min(sh):.3f}..{max(sh):.3f}')
