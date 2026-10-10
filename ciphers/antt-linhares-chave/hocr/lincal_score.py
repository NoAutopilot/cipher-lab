"""LIN-CAL (FAM-LINCAL, 10 Oct 2026): score blind row labels under PREREG-LINCAL.md. Labels: hocr/lincal_labels/<leaf>_c<col>.tsv
(R##<TAB>LABEL<TAB>word/note, verbatim from the subagent, one pass per column). The undecided clause is positional: any OTHER row
strictly between the first FLUSH row and the rank row makes the column undecided (OTHER rows above the first FLUSH are ignored).
--calibrate prints hit/MISS/undecided per held-out column and the gate (4/4 hits); exit 0 PASS, 1 FAIL.
--rank KEY RANK prints the FLUSH word at that rank for a target column and whether the column is undecided."""
import sys, os, unicodedata, re
D=os.path.join(os.path.dirname(__file__),'lincal_labels')
CAL=[('0306_c2','Parecer',19),('0248_c1','Inevitavel',24),('0362_c3','Rustico',25),('0225_c1','Franco',8)]
def norm(w):
    w=unicodedata.normalize('NFKD',w.replace('ſ','s')); w=''.join(c for c in w if not unicodedata.combining(c))
    return re.sub(r'[^a-z]','',w.lower())
def load(k):
    rows=[]
    for line in open(os.path.join(D,f'{k}.tsv'),encoding='utf-8'):
        f=line.rstrip('\n').split('\t')
        if len(f)>=2 and f[0].startswith('R'): rows.append((f[0],f[1].strip().upper(),f[2].strip() if len(f)>2 else ''))
    return rows
def flush(rows): return [(r,w) for r,l,w in rows if l=='FLUSH']
def other_inside(rows,stop_row):
    """True iff an OTHER row lies after the first FLUSH row and before stop_row."""
    seen=False
    for r,l,w in rows:
        if r==stop_row: return False
        if l=='FLUSH': seen=True
        elif l=='OTHER' and seen: return True
    return False
def score(k,hw,rank):
    rows=load(k); fl=flush(rows)
    if len(fl)>=rank and norm(fl[rank-1][1]).startswith(norm(hw)):
        return ('undecided' if other_inside(rows,fl[rank-1][0]) else 'hit'),0
    m=[i+1 for i,(r,w) in enumerate(fl) if norm(w).startswith(norm(hw))]
    if not m: return 'undecided',None
    k_=min(m,key=lambda i:abs(i-rank)); return 'MISS',k_-rank
if __name__=='__main__':
    if sys.argv[1]=='--calibrate':
        res=[(k,hw,rank)+score(k,hw,rank) for k,hw,rank in CAL]
        for r in res: print(*r,sep='\t')
        hits=sum(r[3]=='hit' for r in res); ok=hits==len(CAL)
        print(f'hit {hits}/{len(CAL)} -> GATE {"PASS" if ok else "FAIL"}'); sys.exit(0 if ok else 1)
    if sys.argv[1]=='--rank':
        k,rank=sys.argv[2],int(sys.argv[3]); rows=load(k); fl=flush(rows)
        w=fl[rank-1] if len(fl)>=rank else None
        print(k,'FLUSH rows',len(fl),'rank',rank,'->',w,'| ranks around:',fl[max(0,rank-3):rank+2],
              '| OTHER inside span:',other_inside(rows,w[0]) if w else None)
