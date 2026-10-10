"""FV-O9a (10 Oct 2026, account 1, for LANE LEDGER-N2): Google Books API phrase queries (key from GOOGLE_BOOKS_KEY, country=US; never printed). A miss is a search result (rule 10)."""
import json,os,sys,time,urllib.parse,urllib.request
K=os.environ['GOOGLE_BOOKS_KEY']
for q in sys.argv[1:]:
    u='https://www.googleapis.com/books/v1/volumes?q='+urllib.parse.quote(q)+'&country=US&maxResults=10&key='+K
    try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'cipher-lab research script (contact via repository)'}),timeout=60))
    except Exception as e: print('==',q,'ERR',type(e).__name__); time.sleep(2); continue
    print('==',q,'total',d.get('totalItems'))
    for it in d.get('items',[])[:10]:
        v=it['volumeInfo']; print('  ',v.get('title','')[:70],'|',v.get('publishedDate',''),'|',it.get('searchInfo',{}).get('textSnippet','')[:220].replace('\n',' '))
    time.sleep(2)
