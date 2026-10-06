"""R7A-COL26 copy of A2-COL16's diagnostic (anchor_split_5456.py, key_f23_anchor_5456.tsv), written AFTER the gated run (post hoc, NOT gating): for each candidate code of siblings/anchor_split.py, the
   share of 2000 control-B draws in which that code reaches at least its real cross-unit agreement count. Appends diag_P to the note
   column of key_f23_anchor.tsv. Usage: python3 siblings/anchor_split_diag.py"""
import sys, runpy, random, collections
sys.argv=['x']
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    g = runpy.run_path(__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "anchor_split_5456.py"))
elig, real, cls, stat, U = g['elig'], g['real'], g['cls'], g['stat'], g['U']
realm = {c: max(len(v) for v in U[c].values()) for c in U}
cnt = collections.Counter(); rng = random.Random(7)
for _ in range(2000):
    tx = list(real)
    for v in cls.values():
        p=[real[i] for i in v]; rng.shuffle(p)
        for i,t in zip(v,p): tx[i]=t
    _,_,Uc = stat(tx)
    for c in realm:
        if realm[c]>=2 and max(len(v) for v in Uc[c].values())>=realm[c]: cnt[c]+=1
for c in sorted(realm,key=int):
    if realm[c]>=2: print(c, realm[c], round(cnt[c]/2000,3))
import csv, os
kf = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'key_f23_anchor_5456.tsv')
if os.path.exists(kf):
    rows = list(csv.DictReader(open(kf), delimiter='\t'))
    for r in rows:
        r['note'] = r['note'].split('; diag_P')[0] + f"; diag_P {cnt[r['code']]/2000:.3f} (post hoc, not gating)"
    with open(kf, 'w') as f:
        f.write('code\tvalue\tgrade\tsource\tnote\n')
        for r in rows: f.write('\t'.join(r[k] for k in ('code','value','grade','source','note')) + '\n')
