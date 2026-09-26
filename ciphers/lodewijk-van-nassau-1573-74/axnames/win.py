import csv,sys,os
H=os.path.dirname(os.path.abspath(__file__)); T=os.path.dirname(H)
key={r['code']:r['value'] for r in csv.DictReader(open(os.path.join(T,'key.tsv')),delimiter='\t')}
def show(f,line,pos,w=10):
    rows=[r for r in csv.DictReader(open(os.path.join(T,f)),delimiter='\t') if (r.get('sign') or '').strip()]
    idx=[i for i,r in enumerate(rows) if r['line']==line and r['position']==pos][0]
    out=[]
    for r in rows[max(0,idx-w):idx+w+1]:
        s=r['sign']
        if s.isdigit() and int(s)<=120: out.append(key.get(s,'?'))
        elif s.startswith('='): out.append(s)
        else: out.append('<'+s+'>')
    print(f,line,pos,' '.join(out))
for a in sys.argv[2:]:
    l,p=a.split(':'); show(sys.argv[1],l,p)
