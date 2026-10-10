import gzip,re,sys,unicodedata
P='sources/ia-fulltext/print-check/'
eds=['labibliothquen02gachuoft','lepredemadamede00dargoog','archivesoucorre03housgoog','archivesoucorre04housgoog','lettresdecatheri04cathuoft','leshuguenotsetle03kerv','correspondancede02phil']
def norm(s):
    s=unicodedata.normalize('NFD',s.lower())
    s=''.join(c for c in s if c.isascii() and c.isalpha())
    return s.translate(str.maketrans('vjyk','uiic'))
phr=[l.split('|') for l in open(sys.argv[1]).read().split('\n') if l.strip()]
for e in eds:
    raw=gzip.open(P+e+'_djvu.txt.gz','rt',errors='ignore').read()
    n=norm(raw)
    for p in phr:
        lab=p[0]; pats=[norm(x) for x in p[1:]]
        hits=[m.start() for m in re.finditer(pats[0],n)]
        if len(pats)>1: # proximity: all within 400 letters
            hits=[h for h in hits if all(re.search(q,n[max(0,h-400):h+400]) for q in pats[1:])]
        if hits: print(e,lab,len(hits),'|',' '.join(n[max(0,h-60):h+90] for h in hits[:3]))
        else: print(e,lab,0)
