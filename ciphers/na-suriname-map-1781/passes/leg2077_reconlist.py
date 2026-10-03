# GAPS19 (account-4), 3 Oct 2026: list the disagreements of passes/leg2077_merged.tsv for the one blind reconciliation call,
# with 4 glyphs of context on each side ({?} = the disputed position). Usage: python3 passes/leg2077_reconlist.py
import csv
M=list(csv.DictReader(open('passes/leg2077_merged.tsv'),delimiter='\t'))
by={}
for r in M: by.setdefault(r['crop'],[]).append(r)
with open('passes/leg2077_recon_list.tsv','w') as f:
    f.write('crop\tpos\tcontext\toptionA\toptionB\n'); n=0
    for c,l in by.items():
        for i,r in enumerate(l):
            if r['conf']!='M': continue
            A,B=r['note'][2:].split(' B:')
            ctx=' '.join([x['sign'] for x in l[max(0,i-4):i]]+['{?}']+[x['sign'] for x in l[i+1:i+5]])
            f.write(f'{c}\t{i}\t{ctx}\t{A}\t{B}\n'); n+=1
print(n,'rows')
