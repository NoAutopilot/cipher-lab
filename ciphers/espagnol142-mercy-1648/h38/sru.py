"""H38: Gallica SRU sibling sweep. One request at a time, 2 s apart, browser UA (CLAUDE.md host table). Writes sru_hits.tsv."""
import urllib.request,urllib.parse,time,re,sys,html
Q=[('Galarreta','gallica all "Galarreta"'),('Galarreta2','gallica all "Galaretta"'),
   ('Leopold-chiffre','(gallica all "Leopold Guillaume" or gallica all "Léopold-Guillaume") and gallica all "chiffr"'),
   ('Leopoldo-cifra','gallica all "Leopoldo Guillermo" and (gallica all "cifra" or gallica all "chiffr")'),
   ('Mercy-chiffre','gallica all "Mercy" and gallica all "chiffr" and dc.type all "manuscrit"'),
   ('espagnol-chiffre-1648','dc.source all "Espagnol" and gallica all "chiffr" and gallica all "1648"'),
   ('espagnol-cifra','dc.source all "Espagnol" and (gallica all "cifra" or gallica all "cifrada")'),
   ('peñaranda-chiffre','gallica all "Peñaranda" and gallica all "chiffr"')]
out=open('sru_hits.tsv','w'); out.write('query\ttotal\tark\ttitle\tdate\tsource\n'); n=0
for lab,q in Q:
    url='https://gallica.bnf.fr/SRU?'+urllib.parse.urlencode({'operation':'searchRetrieve','version':'1.2','query':q,'maximumRecords':'50'})
    try:
        x=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read().decode('utf-8','replace')
    except Exception as e:
        print(lab,'ERROR',e); time.sleep(2); continue
    n+=1; tot=re.search(r'<srw:numberOfRecords>(\d+)',x); tot=tot.group(1) if tot else '?'
    recs=x.split('<srw:record>')[1:]
    print(lab,tot,len(recs))
    for r in recs:
        g=lambda t: ' | '.join(html.unescape(v).strip().replace('\n',' ') for v in re.findall(rf'<dc:{t}[^>]*>(.*?)</dc:{t}>',r,re.S))
        ark=re.search(r'ark:/12148/\w+',r); out.write('\t'.join([lab,tot,ark.group(0) if ark else '',g('title')[:250],g('date'),g('source')[:120]])+'\n')
    time.sleep(2)
print('requests',n)
