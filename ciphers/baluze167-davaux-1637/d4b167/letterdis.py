"""D4-B167: disagreement columns from reconcile_passes.py that remain after mapping sign shapes to their exemplar letter (d1bal167)."""
import csv,sys
SH={'gam':'u','h':'n','w':'e','S':'s','c':'x','p':'s','ll':'l','hook':'s','y+':'r','v':'s','wave':'s','u4':'t/n','4u':'a/d','loop':'u/i/d','m4':'m','r':'g','k':'o','t':'e','y':'b','u':'u'}
def L(t):
    t=t.rstrip('?')
    if t.startswith('s:'): s=t[2:].split('|')[0]; return 'L'+SH.get(s,'?'+s)
    return t
for r in csv.DictReader(open(sys.argv[1]),delimiter='\t'):
    a,b=r['A'],r['B']
    if L(a)!=L(b): print(r['line'][-3:],r['col'],a,b,sep='\t')
