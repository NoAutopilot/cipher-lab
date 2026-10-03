import re,glob,sys
pats={'futurus status':r'futur\w*\s+stat\w*','dubitatur':r'dub[il1]tatur','qualis sit eius':r'qual[il1]s\s+s[il1]t\s+e[il1]us','magnas admodum':r'magnas\s+admodum','expensas':r'expens[ae]s','factum magnas':r'factum\s+magn','mittatur nobis':r'm[il1]ttatur\s+nob','responsum mittatur':r'mittatur\s+\w*\s*respons','sed tamen ut res':r'sed\s+tamen\s+ut\s+res'}
for f in sorted(glob.glob(sys.argv[1] if len(sys.argv)>1 else '*goog.txt')):
    t=re.sub(r'-\s*\n\s*','',open(f,errors='replace').read()); t=re.sub(r'\s+',' ',t)
    for k,p in pats.items():
        hits=[m.start() for m in re.finditer(p,t,re.I)]
        print(f,k,len(hits))
        if k in ('futurus status','qualis sit eius','magnas admodum','mittatur nobis','sed tamen ut res','factum magnas','dubitatur'):
            for h in hits[:4]: print('   ',t[max(0,h-120):h+120])
