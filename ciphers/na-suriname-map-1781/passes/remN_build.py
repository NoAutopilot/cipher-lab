# GAPS16-na-suriname-map-1781 (account-4), 2 Oct 2026: rebuild the Remarque rows of ciphertext_2039_remarque.tsv from the
# native-resolution re-pass (passes/remN_merged.tsv from remN_merge.py, passes/remN_reconcile.tsv from one blind Opus
# reconciliation call). Title rows (2039_title1, 2039_title3) are kept as GAPS15 left them. Plain numbers -> w:<n>.
# Usage: python3 passes/remN_build.py [--check]   (--check exits 1 if the committed file differs from a fresh build)
import csv,sys
LINE={'remN_L01':'2039_rem_head','remN_L02':'2039_rem_L1','remN_L03':'2039_rem_L2','remN_L04':'2039_rem_L3',
      'remN_L05':'2039_rem_L4','remN_L06':'2039_rem_L5'}
M=list(csv.DictReader(open('passes/remN_merged.tsv'),delimiter='\t'))
R={}
for r in csv.DictReader((l for l in open('passes/remN_reconcile.tsv') if not l.startswith('#')),delimiter='\t'):
    if r['pos'].isdigit(): R[(r['crop'],int(r['pos']))]=r
by={}
for r in M: by.setdefault(r['crop'],[]).append(r)
CL=('remN_L05',45,52)  # the cluster the reconciliation decided as a whole sequence
rows=[]
for c,lst in by.items():
    out=[]
    for i,r in enumerate(lst):
        if c==CL[0] and CL[1]<=i<=CL[2]:
            if i==CL[1]:
                k=CL[1]
                while (c,k) in R:
                    d=R[(c,k)]
                    if d['decision']!='DROP': out.append((d['decision'],'M','reconciled cluster: '+d['note']))
                    k+=1
            continue
        if r['conf']=='M':
            d=R.get((c,i))
            if d is None: out.append((r['sign'],'M',r['note']+'; not reconciled'))
            elif d['decision']=='DROP': continue
            else: out.append((d['decision'],'H' if d['conf']=='H' else 'M',r['note']+'; reconciled '+d['conf']+': '+d['note']))
        else: out.append((r['sign'],'H',''))
    for j,(s,g,n) in enumerate(out):
        if s.startswith('<') and s.endswith('>'): s='w:'+s[1:-1]
        rows.append((LINE[c],j,s,g,n))
src=open('ciphertext_2039_remarque.tsv').read().splitlines()
head=[l for l in src if l.startswith('#')]
title=[l for l in src if l.startswith('2039_title')]
new=[h for h in head if 'GAPS16' not in h]
new.append('# GAPS16-na-suriname-map-1781 (account-4), 2 Oct 2026: the Remarque rows (2039_rem_*) are REPLACED by a native-resolution re-pass:')
new.append('# images/2039_remarque_native.jpg (IIIF region 1180,6760,2500,800 of 11267x8656), crops images/crops_2039_remN (tools/iiif_lines.py),')
new.append('# two blind Opus passes (passes/remN_passA.tsv, passB.tsv) aligned by passes/remN_merge.py, one blind reconciliation call')
new.append('# (passes/remN_reconcile.tsv); built by passes/remN_build.py. The GAPS15 notes above about the Remarque describe the superseded draft.')
new.append('line\tpos\tsign\tconf\tnote')
new+=title+['\t'.join(map(str,r)) for r in rows]
text='\n'.join(new)+'\n'
if '--check' in sys.argv:
    sys.exit(0 if open('ciphertext_2039_remarque.tsv').read()==text else 1)
open('ciphertext_2039_remarque.tsv','w').write(text)
print(len(rows),'remarque signs;',sum(1 for r in rows if r[3]=='H'),'H')
