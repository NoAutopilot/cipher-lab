#!/usr/bin/env python3
"""Reproducible renumbering screens and shuffled-order baselines. See REPORT.md."""
import subprocess,random,json,csv,re
from pathlib import Path
D=Path(__file__).resolve().parent
exe=D/'renumber'
subprocess.run(['g++','-O3','-std=c++17',str(D/'renumber.cpp'),'-o',str(exe)],check=True)
base=list(map(int,(D/'control_original.seq').read_text().split()))[:366]
rng=random.Random(71);p=list(range(10));rng.shuffle(p);pos=[2,0,3,1]
def enc(n):return int(''.join(str(p[int(f'{n:04d}'[j])]) for j in pos))
def transform(n,key):
 if key.startswith('positions='):
  pos,ds=re.findall(r'=(\d+)',key);return int(''.join(ds[int(f'{n:04d}'[int(j)])] for j in pos))
 nums=list(map(int,re.findall(r'=(\d+)',key)))
 if key.startswith('mod='):
  N,a,b=nums;return (a*(n-1)+b)%N+1
 N,c,rev,off=nums;x=(n-1+off)%N;rr,cc=divmod(x,c)
 if rev&1:rr=N//c-1-rr
 if rev&2:cc=c-1-cc
 return cc*(N//c)+rr+1
controls={'digits':[enc(n) for n in base], 'affine':[(71*(n-1)+391)%2000+1 for n in base]}
inv={transform(n,'grid=2000 cols=50 rev=1 offset=173'):n for n in range(1,2001)}
controls['grid']=[inv[n] for n in base]
for mode,seq in controls.items():(D/f'control_{mode}.seq').write_text(' '.join(map(str,seq)))
res=[]
def run(table,mode,name,seq):
 seqfile=D/'run_input.seq';seqfile.write_text(' '.join(map(str,seq)))
 proc=subprocess.run([str(exe),table,seqfile.name,mode,'run_output.tsv'],capture_output=True,text=True,cwd=D,check=True)
 rr=list(csv.DictReader(open(D/'run_output.tsv'),delimiter='\t'))
 result={'table':table,'mode':mode,'sequence':name,'search':proc.stderr.strip(),'best':rr[0] if rr else None}
 if name=='control' and rr:result['exact_token_recovery']=sum(transform(n,rr[0]['transform'])==old for n,old in zip(seq,base))/len(base)
 if name in ('control','target_clean'):(D/f'{name}_{table}_{mode}.tsv').write_text((D/'run_output.tsv').read_text())
 res.append(result)
target=list(map(int,(D/'target_clean.seq').read_text().split()))
for table in ['THE972_bourdeau','WE028']:
 for mode in ['digits','affine','grid']:
  run(table,mode,'target_clean',target)
  if table=='THE972_bourdeau':run(table,mode,'control',controls[mode])
  for seed in range(20):
   nums=[v for v in target if v>=0];random.Random(seed).shuffle(nums);it=iter(nums);ss=[next(it) if v>=0 else -1 for v in target]
   run(table,mode,f'null_{seed}',ss)
  (D/'clean_screen_results.json').write_text(json.dumps(res,indent=2)+'\n')
  print(table,mode,'done',flush=True)
