#!/usr/bin/env python3
"""Score the partial key decode of 4.VEL 2039's legend entries against 4.VEL 2038's plain legend (crib_2038_legend.tsv),
with shuffled-crib controls (CLAUDE.md rule 3). GAPS5-na-suriname-map-1781, 2 Oct 2026.

Statistic per 2039 entry: the decoded letters at keyed positions (reading_2039_legend_tokens.tsv, grade M, value known) are
slid over every crib entry's letter string at every offset; the score is the best fraction of keyed positions whose letter
equals the crib letter under it. Two aggregates: SAME-LABEL (the crib entry with the same letter label, best offset) and
FREE (best over all crib entries). Control: the letters inside each crib entry are shuffled (lengths and letter stock kept),
20 seeds, same procedure -- the control can vary on the statistic's own axis (which letters sit where), so it is a test.
Exit 0 always; the numbers are what counts. Usage: python3 align_2039_legend.py [--seeds 20] [--crib crib_2038_legend.tsv]
--shuffle-target N (GAPS6): a second control on the other axis -- the real crib, but the decoded letters of each 2039 entry
  shuffled among that entry's positions (keyed count and letter stock kept), N seeds; it asks whether the ORDER of the
  transferred key's letters is what the free statistic rewards.
--verbose (GAPS6): per 2039 entry, the best-matching crib entry, offset and matched letters, so a pass can be read for words.
--crib (GAPS6, 2 Oct 2026): any legend crib TSV with entry/text columns; a row whose entry cell is empty is a continuation
of the previous lowercase entry (crib_2042_legend.tsv's h and i), so the two cribs score the same way.
"""
import csv, random, sys, os, re, statistics
here=os.path.dirname(os.path.abspath(__file__))
seeds=int(sys.argv[sys.argv.index('--seeds')+1]) if '--seeds' in sys.argv else 20
cribfile=sys.argv[sys.argv.index('--crib')+1] if '--crib' in sys.argv else 'crib_2038_legend.tsv'
print(f"crib: {cribfile}")
toks={}
for r in csv.DictReader((l for l in open(os.path.join(here,'reading_2039_legend_tokens.tsv')) if not l.startswith('#')),delimiter='\t'):
    lab=r['line'].replace('2039_leg_',''); toks.setdefault(lab,[]).append((int(r['pos']),r['value'] if r['grade']!='U' else None))
crib={}
last=None
for r in csv.DictReader((l for l in open(os.path.join(here,cribfile)) if not l.startswith('#')),delimiter='\t'):
    if len(r['entry'])==1 and r['entry'].islower():
        crib[r['entry']]=re.sub(r'[^a-z]','',r['text'].lower().replace('ij','ij')); last=r['entry']
    elif r['entry']=='' and last:
        crib[last]+=re.sub(r'[^a-z]','',r['text'].lower())
    else:
        last=None
def best(entry_vals, text, detail=False):
    n=len(entry_vals); m=len(text); bestf=0.0; bestoff=0
    keyed=[(i,v) for i,v in entry_vals if v]
    if not keyed: return None
    for off in range(-n+1, m):
        hit=sum(1 for i,v in keyed if 0<=i+off<m and text[i+off]==v)
        if hit/len(keyed)>bestf: bestf, bestoff = hit/len(keyed), off
    if detail:
        row=''.join((v if (0<=i+bestoff<m and text[i+bestoff]==v) else (v.upper() if v else '.')) for i,v in sorted(entry_vals))
        return bestf, bestoff, row
    return bestf
def run(cr):
    same=[]; free=[]
    for lab,tv in toks.items():
        if lab=='head': continue
        vals=sorted(tv)
        if lab in cr:
            b=best(vals, cr[lab]); 
            if b is not None: same.append(b)
        bs=[best(vals,t) for t in cr.values()]; bs=[b for b in bs if b is not None]
        if bs: free.append(max(bs))
    return statistics.mean(same), statistics.mean(free), len(same), len(free)
rs,rf,ns,nf=run(crib)
if '--verbose' in sys.argv:
    print("per entry (free): 2039 entry -> best crib entry @offset score | decode row: lowercase = matches the crib letter under it, UPPER = keyed but no match, . = unkeyed")
    for lab,tv in toks.items():
        if lab=='head': continue
        vals=sorted(tv); cand=[(best(vals,t,True),k) for k,t in crib.items()]
        cand=[(c,k) for c,k in cand if c]
        if not cand: continue
        (f,off,row),k=max(cand,key=lambda x:x[0][0])
        print(f"  {lab}: -> {k} @{off:+d} {f:.3f} | {row} | crib {crib[k]}")
cs=[];cf=[]
for seed in range(seeds):
    rnd=random.Random(seed); sh={}
    for k,t in crib.items():
        l=list(t); rnd.shuffle(l); sh[k]=''.join(l)
    s,f,_,_=run(sh); cs.append(s); cf.append(f)
def rep(name, real, ctrl):
    mu=statistics.mean(ctrl); sd=statistics.pstdev(ctrl) or 1e-9; p95=sorted(ctrl)[int(0.95*len(ctrl))-1]
    rank=sum(1 for c in ctrl if c>=real)
    print(f"{name}: real {real:.3f} | shuffled-crib controls (n={len(ctrl)}) mean {mu:.3f} sd {sd:.3f} p95 {p95:.3f} max {max(ctrl):.3f} | z {(real-mu)/sd:+.2f} | controls >= real: {rank}/{len(ctrl)}")
print(f"entries scored: same-label {ns}, free {nf}; keyed positions per entry from reading_2039_legend_tokens.tsv")
rep('SAME-LABEL', rs, cs); rep('FREE      ', rf, cf)
if '--shuffle-target' in sys.argv:
    nt=int(sys.argv[sys.argv.index('--shuffle-target')+1]); ts=[]; tf=[]
    saved={k:list(v) for k,v in toks.items()}
    for seed in range(nt):
        rnd=random.Random(1000+seed)
        for k,v in saved.items():
            vals=[x[1] for x in sorted(v)]; rnd.shuffle(vals); toks[k]=[(i,vals[i]) for i in range(len(vals))]
        s_,f_,_,_=run(crib); ts.append(s_); tf.append(f_)
    toks.update(saved)
    rep('SAME-LABEL vs shuffled-target', rs, ts); rep('FREE       vs shuffled-target', rf, tf)
