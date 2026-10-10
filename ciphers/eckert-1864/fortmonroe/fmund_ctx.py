import gzip, os, re, sys
D = '../../../sources/ia-fulltext/print-check'
def ctx(vol, phrase, w=700):
    raw = gzip.open(f'{D}/{vol}_djvu.txt.gz','rt',errors='ignore').read()
    # build letters-only index map
    idx=[i for i,c in enumerate(raw) if c.isalpha()]; s=''.join(raw[i].lower() for i in idx)
    k=re.sub(r'[^a-z]','',phrase.lower()); j=s.find(k)
    if j<0: return 'NOHIT'
    a=idx[j]; return raw[max(0,a-w//2):a+w].replace('\n',' ')
for vol, ph in [(a.split('::')[0], a.split('::')[1]) for a in sys.argv[1:]]:
    print('=====',vol,'|',ph); print(ctx(vol,ph)); print()
