import os, re, sys
# V-SUR0744 verifier re-run of SUR-BLIND run 1 (gated [ij] -> A3) with a chosen seed; prints the A3 line. Not a gate of its own.
P=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
src=open(os.path.join(P,'inv373_alias_r15','alias_run.py'),encoding='utf-8').read().split('\nout = []; allp = []')[0]
ns={'__file__':os.path.join(P,'inv373_alias_r15','alias_run.py')}; exec(src,ns)
ns['ALIASES'].clear(); ns['ALIASES']['A3']=(('0744',),lambda s:s.replace('[ij]','‹ij›'),'[ij]')
tabs=['inv373_0693_r10','inv373_0702_r13','inv373_0730_r13']
p, seed = sys.argv[1], int(sys.argv[2]); out=[]
ns['run']('0744',os.path.join('inv373_0744_blind_sb',p),tabs,seed,out)
print(p, seed, ' || '.join(l for l in out if 'A3' in l or 'after' in l))
