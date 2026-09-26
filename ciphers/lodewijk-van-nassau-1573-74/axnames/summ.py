import csv,sys,collections,glob,os
H=os.path.dirname(os.path.abspath(__file__))
d=collections.defaultdict(list)
for f in sorted(glob.glob(os.path.join(H,'occ_*.tsv'))):
    for r in csv.DictReader(open(f),delimiter='\t'):
        d[int(r['code'])].append(r)
for c in sorted(d):
    occ=d[c]; cnt=collections.Counter(r['absorbed'] for r in occ)
    print(c, len(occ), dict(cnt.most_common(6)))
