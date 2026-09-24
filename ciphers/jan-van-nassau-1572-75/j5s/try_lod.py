import csv,sys,collections
key={}
for r in csv.DictReader(open(__import__('os').path.join(__import__('os').path.dirname(__file__),'../../lodewijk-van-nassau-1573-74/key.tsv')),delimiter='\t'): key[r['code']]=r['value']
f=sys.argv[1]; col=sys.argv[2] if len(sys.argv)>2 else 'token'
runs=collections.OrderedDict()
for r in csv.DictReader(open(f),delimiter='\t'):
    runs.setdefault(r['run'],[]).append(r)
for k,rs in runs.items():
    out=[]; gl=[]
    for r in rs:
        t=r[col]
        if t.isdigit():
            v=key.get(t,'?'); out.append('_' if v=='NULL' else ('<'+v+'>' if len(v)>1 else v))
        else: out.append('('+t+')')
        if r.get('gloss') not in (None,'','^'): gl.append(r['gloss'])
    print(k, ''.join(out), '|', ' '.join(gl))
