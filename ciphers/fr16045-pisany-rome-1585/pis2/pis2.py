"""R9-PIS2: apply PREREG_pis2.md's settlement rule to the blind reads. --check fails if t31_tokens.tsv is stale."""
import csv,sys,os
D=os.path.dirname(os.path.abspath(__file__))
cell={r['label']:r['cell'] for r in csv.DictReader(open(D+'/blind/cell_labels.tsv'),delimiter='\t')}
tok={r['label']:r for r in csv.DictReader(open(D+'/blind/token_labels.tsv'),delimiter='\t')}
LOOP={'T45','T36'};XO={'T36'};BARE={'T31','T47'}
adm={}
for l,i in [('L03','5'),('L03','25'),('L03','35'),('L06','15'),('L06','44'),('L07','28'),('L07','45'),('L09','20'),('L09','30')]: adm[('f244r',l,i)]=LOOP
adm[('f244r','L07','33')]=set()
for l,i in [('L04','7'),('L04','39'),('L05','0'),('L09','3'),('L12','5'),('L14','28'),('L15','9')]: adm[('f275r',l,i)]=XO
for l,i in [('L03','31'),('L07','11'),('L10','13'),('L15','33'),('L13','11')]: adm[('f275r',l,i)]=BARE
adm[('f275r','L08','0')]=set()
out=['leaf\tline\ttok_index\tblind_id\treader_top\treader_second\tconf\teye_admissible\tverdict']
for f in ('reader_f244r.txt','reader_f275r.txt'):
    for line in open(D+'/blind/'+f):
        b,t,s,c,_=line.rstrip('\n').split('\t');r=tok[b];k=(r['leaf'],r['line'],r['tok_index'])
        top=cell.get(t,'none');sec=cell.get(s,'none');a=adm[k];ok=c in('medium','high')
        if a: v='SETTLED-'+top if ok and top in a else 'UNSETTLED'
        else: v='NOT-T31-SHAPE' if ok and top!='T31' else 'UNSETTLED'
        out.append('\t'.join([*k,b,top,sec,c,','.join(sorted(a)) or '-',v]))
out.append('f244r\tL09\t26\t-\t-\t-\t-\t-\tNOT-LOCATED')
txt='\n'.join(sorted(out[1:],key=lambda x:(x.split('\t')[0],int(x.split('\t')[1][1:]),int(x.split('\t')[2]))))
txt=out[0]+'\n'+txt+'\n';p=D+'/t31_tokens.tsv'
if '--check' in sys.argv:
    if open(p).read()!=txt: print('STALE');sys.exit(1)
    print('up to date');sys.exit(0)
open(p,'w').write(txt);print(txt)
