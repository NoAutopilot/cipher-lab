# N9-COSV verifier, 5 Oct 2026: per-group support for the 10 N8-COS C values from the committed pass/alignment files.
# Usage (repo root): python3 ciphers/costabili-modena-1491/align/n9cosv_pergroup.py ciphers/costabili-modena-1491/align/n9cosv_pergroup.tsv
import csv,collections,sys
D='ciphers/costabili-modena-1491/align/'
C={'+':'a','T':'d','a':'i','b':'o','c':'p','d':'r','g':'l','o':'e','y':'n','z':'o'}
norm={}
for p in 'AB':
    for r in csv.DictReader(open(D+f'n8cos_pass{p}_norm.tsv'),delimiter='\t'): norm.setdefault(r['crop'],{})[p]=(r['gloss_above'],r['signs'])
al={}
for p in 'AB':
    for r in csv.DictReader(open(D+f'n8cos_align_pass{p}.tsv'),delimiter='\t'):
        crop=r['cipher_line'].rsplit('_',1)[0]
        al.setdefault((p,crop),[]).append((r['value'],r['plain_chunk'],r['status'].split(':')[0]))
out=csv.writer(open(sys.argv[1],'w'),delimiter='\t',lineterminator='\n')
out.writerow(['sign','value','crop','gloss_A','signs_A','chunks_A','gloss_B','signs_B','chunks_B','A_agree','B_agree','both'])
summ=[]
for s,v in C.items():
    groupsA=set();groupsB=set()
    for crop in sorted(norm):
        ca=[(pc,st) for (val,pc,st) in al.get(('A',crop),[]) if val==s]
        cb=[(pc,st) for (val,pc,st) in al.get(('B',crop),[]) if val==s]
        if not ca and not cb: continue
        aA=sum(1 for pc,st in ca if pc==v); aB=sum(1 for pc,st in cb if pc==v)
        if aA: groupsA.add(crop)
        if aB: groupsB.add(crop)
        gA,sA=norm[crop].get('A',('',''));gB,sB=norm[crop].get('B',('',''))
        out.writerow([s,v,crop,gA,sA,' '.join(pc for pc,_ in ca),gB,sB,' '.join(pc for pc,_ in cb),aA,aB,'Y' if aA and aB else ''])
    both=groupsA&groupsB
    summ.append((s,v,len(groupsA),len(groupsB),len(both),sorted(both)))
for x in summ: print(*x,sep='\t')
