import json,csv,sys,random
rec={k:[t for t in v if t] for k,v in json.load(open('recon.json')).items()}
# reconciliation by this worker from the crops: capital-N sign at the 'wir' positions = NW (c2 pos 17, c3 pos 1)
rec['c2'][16]='NW'; rec['c3'][0]='NW'
key={}
for r in csv.DictReader(open('../key_98.tsv'),delimiter='\t'):
    key[r['sign']]=r['value']
codes={};nxt=[1];wnxt=[100];unk=[50]
def code(t):
    if t=='?':
        unk[0]+=1; return str(unk[0])
    if t not in codes:
        v=key.get(t,'')
        if len(v)==1: codes[t]=str(nxt[0]); nxt[0]+=1
        else: codes[t]=str(wnxt[0]); wnxt[0]+=1
    return codes[t]
gl={'c1':"Jm Crass verwardacht auch wi sbrauch",
'c2':"Todts vnd grosse gefahr Leibs vnd vnser fraundlich lieb gemahl",
'c3':"Vnnd Vns alltzeit ersenget haben dann das die frawe Kostantin will"}
cip={k:[code(t) for t in v] for k,v in rec.items()}
json.dump({'codes':codes,'cip':cip,'rec':rec,'gl':gl},open('enc.json','w'))
with open('prior.tsv','w') as f:
    f.write('code\tmeaning\n')
    for s,c in codes.items():
        if int(c)<50: f.write('%s\t%s\n'%(c,key[s]))
print(codes); print(cip)
