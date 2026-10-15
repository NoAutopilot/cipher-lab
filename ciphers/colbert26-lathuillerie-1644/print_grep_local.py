# COL26-PRINT2 (15 Oct 2026): normalised full-phrase and 4-word-window grep of cached IA djvu texts. usage: print_grep_local.py phrases.txt phrases_c50.txt DIR_OF_TXT
import sys,re,glob,unicodedata
def norm(s):
    s=unicodedata.normalize('NFKD',s.lower()); s=''.join(c for c in s if not unicodedata.combining(c))
    s=s.replace('ſ','s').replace('j','i').replace('v','u')
    return re.sub(r'[^a-z0-9]+',' ',s).strip()
ph=[l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]
ph+=[l.strip() for l in open(sys.argv[2]) if l.strip() and not l.startswith('#')]
for f in sorted(glob.glob(sys.argv[3]+'/*.txt')):
    t=norm(open(f,errors='ignore').read())
    hits=[]
    for p in ph:
        n=norm(p); w=n.split()
        if n in t: hits.append(('FULL',p))
        else:
            # any 4-word window
            for i in range(max(1,len(w)-3)):
                g=' '.join(w[i:i+4])
                if len(w)>=4 and g in t: hits.append(('4gram',p+' :: '+g)); break
    print(f.split('/')[-1],len(ph),'phrases; hits:',hits)
