"""LIN-COUNT (9 Oct 2026): score blind row labels under PREREG-LINCOUNT.md. Labels: hocr/lincount_labels/<leaf>_c<col>_<pass>.tsv
(R##<TAB>LABEL<TAB>word/note, verbatim from the subagent). Calibration: --calibrate prints hit/MISS/undecided per column and
pass and the gate; exit 0 PASS, 1 FAIL. --rank KEY RANK prints the FLUSH word at that rank per pass (targets)."""
import sys, glob, os, unicodedata, re
D=os.path.join(os.path.dirname(__file__),'lincount_labels')
CAL=[('0236_c1','Guerra',2),('0236_c3','Habil',1),('0146_c1','D',1),('0276_c2','Memoria',3),('0261_c2','Lhe',6),('0265_c2','Lugar',17),('0255_c2','Junto',20)]
def norm(w):
    w=unicodedata.normalize('NFKD',w.replace('ſ','s')); w=''.join(c for c in w if not unicodedata.combining(c))
    return re.sub(r'[^a-z]','',w.lower())
def load(k,p):
    rows=[]
    for line in open(os.path.join(D,f'{k}_{p}.tsv'),encoding='utf-8'):
        f=line.rstrip('\n').split('\t')
        if len(f)>=2 and f[0].startswith('R'): rows.append((f[0],f[1].strip().upper(),f[2].strip() if len(f)>2 else ''))
    return rows
def flush(rows): return [(r,w) for r,l,w in rows if l=='FLUSH']
def bad_above(rows,stop_row):
    for r,l,w in rows:
        if r==stop_row: break
        if l=='OTHER' and re.search(r'fragment|merged|two',w,re.I): return True
    return False
def score(k,hw,rank,p):
    rows=load(k,p); fl=flush(rows)
    if len(fl)>=rank and norm(fl[rank-1][1]).startswith(norm(hw)):
        return ('undecided' if bad_above(rows,fl[rank-1][0]) else 'hit'),0
    m=[i+1 for i,(r,w) in enumerate(fl) if norm(w).startswith(norm(hw))]
    if not m: return 'undecided',None
    k_=min(m,key=lambda i:abs(i-rank)); return 'MISS',k_-rank
if __name__=='__main__':
    if sys.argv[1]=='--calibrate':
        ok=True
        for p in ('A','B'):
            res=[(k,hw,rank)+score(k,hw,rank,p) for k,hw,rank in CAL]
            hits=sum(r[3]=='hit' for r in res); non=[r for r in res if r[3]!='hit']
            pas=hits>=6 and len(non)<=1 and all(r[3]=='undecided' or abs(r[4])<=1 for r in non)
            ok&=pas
            for r in res: print(p,*r,sep='\t')
            print(f'pass {p}: hit {hits}/7, non-hit {len(non)} -> {"PASS" if pas else "FAIL"}')
        print('GATE',('PASS' if ok else 'FAIL')); sys.exit(0 if ok else 1)
    if sys.argv[1]=='--rank':
        k,rank=sys.argv[2],int(sys.argv[3])
        for p in ('A','B'):
            rows=load(k,p); fl=flush(rows)
            w=fl[rank-1] if len(fl)>=rank else None
            print(p,k,'FLUSH rows',len(fl),'rank',rank,'->',w,'| ranks around:',fl[max(0,rank-3):rank+2], '| OTHER fragment/merged above:',bad_above(rows,w[0]) if w else None)
