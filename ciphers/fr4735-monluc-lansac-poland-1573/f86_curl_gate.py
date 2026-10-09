#!/usr/bin/env python3
# MONLUC-CURL (9 Oct 2026): pre-registered gate on the binary curl-present blind sort of the f.86 K07 tiles.
# Usage: python3 -I f86_curl_gate.py ANSWERS.tsv   (ANSWERS: line, pos, curl in Y/N/U; joined to f86_k07_sort.tsv gloss_faced)
# Gate: >=3 K07 tiles in Y and >=3 in N; statistic = t-faced K07 tiles answered Y among the 14 faced; null = 10,000 shuffles of the
# 14 faced letters over the same tiles (fixed X = Y, binary, no max-group re-pick); PASS if p < 0.05. U counts as not-Y.
import csv,random,sys
T='ciphers/fr4735-monluc-lansac-poland-1573/'
faced={}
for r in csv.reader(open(T+'f86_k07_sort.tsv'),delimiter='\t'):
    if not r or r[0].startswith('#') or r[0]=='tile': continue
    faced[(r[1],r[2])]=(r[3],r[4],r[7])
ans={(r['line'],r['pos']):r['curl'] for r in csv.DictReader(open(sys.argv[1]),delimiter='\t')}
k07=[k for k in faced if faced[k][0]=='K07']
ny=sum(ans[k]=='Y' for k in k07); nn=sum(ans[k]=='N' for k in k07); nu=len(k07)-ny-nn
print(f'K07 tiles: Y {ny} N {nn} U {nu}; K38 tile answered', [ans[k] for k in faced if faced[k][0]=='K38'])
split=ny>=3 and nn>=3
fk=[k for k in k07 if faced[k][1]]
y=[ans[k]=='Y' for k in fk]; v=[faced[k][1] for k in fk]
obs=sum(1 for a,b in zip(y,v) if a and b=='t')
print(f'faced Y: t {obs} of {sum(y)} ({",".join(sorted(b for a,b in zip(y,v) if a))}); faced not-Y: t {sum(1 for a,b in zip(y,v) if not a and b=="t")} of {len(y)-sum(y)}')
R=random.Random(1186); ge=0; dist=[]
for _ in range(10000):
    R.shuffle(v); s=sum(1 for a,b in zip(y,v) if a and b=='t'); dist.append(s); ge+=s>=obs
dist.sort(); p=ge/10000
print(f'split {"yes" if split else "no"}; obs {obs}, null p95 {dist[9499]}, p {p:.4f} ->', 'PASS' if split and p<0.05 else 'FAIL')
agree=sum(1 for k in k07 if (ans[k]=='Y')==(faced[k][2]=='1')); print(f'secondary: agreement with curl_reader (non-blind) {agree}/{len(k07)}')
