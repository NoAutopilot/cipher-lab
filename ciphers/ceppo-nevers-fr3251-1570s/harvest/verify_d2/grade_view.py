"""Per passage: the D decode with, under each letter, D's src (A/B/AB/D) and conf, and whether solver's passC agrees on
the sign (VERIFY-CEPPO-D2-1, 29 Sept 2026). Usage: grade_view.py passD.tsv passC.tsv [X_THETA2=r ...]"""
import csv,json,sys,os
H=os.path.dirname(os.path.abspath(__file__))+'/../'
m={e['id']:e['value'] for e in json.load(open(H+'sign_id_map.json'))}
for x in sys.argv[3:]: k,v=x.split('=',1); m[k]=v
D=list(csv.DictReader(open(sys.argv[1]),delimiter='\t')); C={(r['passage'],r['pos']):r['sign_id'] for r in csv.DictReader(open(sys.argv[2]),delimiter='\t')}
P={}
for r in D: P.setdefault(r['passage'],[]).append(r)
for p,rs in P.items():
    l1=l2=l3='';
    for r in rs:
        v=m.get(r['sign_id']); t='_' if v is None else ('' if v=='null' else ('&' if v=='et' else v))
        if not t: continue
        g='S' if (r['conf']=='H' and r['src']=='AB') else ('m' if r['src'] in('AB','A','B') else 'd')
        c='=' if C.get((p,r['pos']))==r['sign_id'] else 'x'
        l1+=t; l2+=g*len(t); l3+=c*len(t)
    print(f'{p:6} {l1}\n{"":6} {l2}\n{"":6} {l3}')
