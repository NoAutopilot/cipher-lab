"""AUD2-LEDGER13-2 (10 Oct 2026): Google Books API queries restricted to The Papers of Ulysses S. Grant vol. 13 by its
ISBN (isbn:0809311976, volume mnRjmhe3QLoC), positive controls first, then the decoded words of E502 E507 E512 E520 E532;
plus unrestricted phrase variants the first audit (FV-FM65b) did not run. Key from GOOGLE_BOOKS_KEY, country=US; never printed.
Writes aud2_l13_2_gb.out beside this file."""
import json, os, time, urllib.parse, urllib.request
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aud2_l13_2_gb.out')
I = 'isbn:0809311976 '
Q = [
 ('control', I + 'Ariel Sedgwick'), ('control', I + '"perfect order"'), ('control', I + 'Ashland'),
 ('E502', I + 'Howell'), ('E502', I + 'Howell Webster'), ('E502', I + '"Colonel Morgan" steamers'), ('E502', I + 'coaling watering'),
 ('E502', I + '"Rawlins wishes"'), ('E502', I + '"chief commissary" steamers rations'),
 ('E507', I + 'Russia'), ('E507', I + '"flag ship"'), ('E507', I + '"flag-ship"'), ('E507', I + 'Webster Dodge'),
 ('E512', I + 'Winants'), ('E512', I + 'Hancox'), ('E512', I + 'Seneca'), ('E512', I + '"Porter" tug'),
 ('E520', I + 'Baltic'), ('E520', I + 'Illinois Victor'), ('E520', I + 'Ingalls Webster Baltimore'),
 ('E532', I + 'Bradley'), ('E532', I + '"mule teams"'), ('E532', I + '"4,000 men"'), ('E532', I + 'Webster transportation'),
 ('E502u', '"turn them over to Col. Morgan"'), ('E502u', '"what number of troops each steamer"'),
 ('E507u', '"send her here in time for a flag"'), ('E507u', '"Russia" "flag ship" 1865 Butler Monroe'),
 ('E512u', '"Seneca at Bermuda"'), ('E512u', '"Winants" "Hancox" 1865'),
 ('E520u', '"Baltic" "Ariel" "Illinois" "Sedgwick" "Victor" 1865'),
 ('E532u', '"transportation for four thousand men"'), ('E532u', '"what time can this transportation"'),
]
key = os.environ.get('GOOGLE_BOOKS_KEY', '')
with open(OUT, 'w') as f:
    for tag, q in Q:
        url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 10, 'key': key})
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=60))
        except Exception as e:
            f.write(f'{tag}\t{q}\tERROR {type(e).__name__}\n'); time.sleep(2); continue
        f.write(f'{tag}\t{q}\ttotal {d.get("totalItems", 0)}\n')
        for it in d.get('items', [])[:10]:
            v = it.get('volumeInfo', {}); s = it.get('searchInfo', {}).get('textSnippet', '')
            f.write(f'    {it.get("id")} {v.get("title","")[:70]} {v.get("publishedDate","")} | {s[:300]}\n')
        time.sleep(1.6)
print(open(OUT).read())
