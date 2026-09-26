import csv,re,sys
key={r['code']:r['value'] for r in csv.DictReader(open('key_full.tsv'),delimiter='\t')}
rows=list(csv.DictReader(open('ciphertext_5801.tsv'),delimiter='\t'))
def dec(s):
    if s.startswith('='): return s[1:].upper()
    if re.fullmatch(r'\d+',s):
        v=key.get(s)
        if int(s)>120: return '[%s:%s]'%(s,v or '?')
        return v if v and v!='NULL' else ('' if v=='NULL' else '<%s>'%s)
    return '{%s}'%s
out=[]
for i,r in enumerate(rows):
    s=r['sign']
    if re.fullmatch(r'\d+',s) and int(s)>120 and key.get(s,'')!='NULL':
        a=' '.join(dec(x['sign']) for x in rows[max(0,i-14):i])
        b=' '.join(dec(x['sign']) for x in rows[i+1:i+15])
        c=' '.join(x['sign'] for x in rows[max(0,i-6):i+7])
        out.append((s,r['line'],r['position'],r['confidence'],c,a+'  ##'+dec(s)+'##  '+b))
for o in out: print('\t'.join(o))
