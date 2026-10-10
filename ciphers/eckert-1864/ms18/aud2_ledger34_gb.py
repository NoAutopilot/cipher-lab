#!/usr/bin/env python3
"""AUD2-LEDGER-34 (10 Oct 2026): Google Books API (key from GOOGLE_BOOKS_KEY, never printed; country=US). stdin: one query per line. Appends to argv[1]. 1.6 s apart."""
import json,os,sys,time,urllib.parse,urllib.request
K=os.environ['GOOGLE_BOOKS_KEY']; out=open(sys.argv[1],'a')
for q in sys.stdin:
    q=q.strip()
    if not q: continue
    url='https://www.googleapis.com/books/v1/volumes?q='+urllib.parse.quote(q)+'&maxResults=10&country=US&key='+K
    try:
        d=json.load(urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60))
        it=d.get('items',[]) ; r=f"{q}\t{d.get('totalItems')}\t"+' ; '.join(f"{i['volumeInfo'].get('title','')[:50]} ({i['volumeInfo'].get('publishedDate','')}) {i.get('searchInfo',{}).get('textSnippet','')[:170]!r}" for i in it[:8])
    except Exception as e:
        r=f"{q}\tERR {str(e)[:80]}\t"
    print(r[:1500]); out.write(r+'\n'); time.sleep(1.6)
