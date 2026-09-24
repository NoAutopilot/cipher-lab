import csv, collections, random
rows=list(csv.DictReader(open('groen/groen_5549.tsv'),delimiter='\t'))
nums=[int(r['token']) for r in rows if r['kind']=='num' and r['token'].isdigit()]
print(len(nums), len(set(nums)))
c=collections.Counter(nums)
print(sorted(c.items(), key=lambda x:-x[1])[:40])
print('distinct <=120:', len([k for k in c if k<=120]), 'tokens<=120', sum(v for k,v in c.items() if k<=120))
print('missing 1..120:', [k for k in range(1,121) if k not in c])
def ic(seq):
    cc=collections.Counter(seq); n=len(seq)
    return sum(v*(v-1) for v in cc.values())/(n*(n-1))
low=[x for x in nums if x<=120]
for w in (3,4,5,6):
  for off in range(w):
    print(w,off, round(ic([(x-1+off)//w for x in low]),4))
# random baseline: shuffle code->block
for w in (5,):
  r=[]
  for t in range(200):
    p=list(range(1,121)); random.shuffle(p); m={i+1:p[i] for i in range(120)}
    r.append(ic([(m[x]-1)//w for x in low]))
  print('random5 mean',sum(r)/len(r), max(r))
