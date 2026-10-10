"""AUD2-LEDGER13-2 (10 Oct 2026): exact-phrase Google Books snippet queries restricted to Grant Papers by intitle (the route that found E516 and E531 in
vol. 13 for AUD2-LEDGER13-1), on the decoded phrases of E502 E507 E512 E520 E532; positive control first. Key GOOGLE_BOOKS_KEY, country=US, never
printed. Writes aud2_l13_2_gb2.out beside this file."""
import json, os, time, urllib.parse, urllib.request
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aud2_l13_2_gb2.out')
G = ' intitle:Grant'
Q = [('control', '"six vessels" Oriental' + G), ('control', '"enquiries made at both places"' + G),
 ('E502', '"which you have been and are now"' + G), ('E502', '"instructions received from General Ingalls"' + G), ('E502', '"to be loaded with the required"' + G),
 ('E502', '"ready to receive them"' + G + ' Morgan'), ('E502', '"what number of troops"' + G), ('E502', '"turn them over to Col"' + G), ('E502', 'Howell Webster coaling' + G),
 ('E507', '"had left here before"' + G), ('E507', '"in time for a flag"' + G), ('E507', '"steamer Russia"' + G), ('E507', '"Russia is disabled"' + G), ('E507', '"flag ship" Webster' + G),
 ('E512', '"hardly capable of going"' + G), ('E512', '"would be much better" Seneca' + G), ('E512', '"tug D. D. Porter"' + G), ('E512', '"bring down a tug"' + G),
 ('E512', '"the Winants"' + G), ('E512', '"Eliza Hancox"' + ' intitle:"Papers of Ulysses"'),
 ('E520', '"ordered to Baltimore"' + G), ('E520', '"except the Baltic"' + G), ('E520', '"heard from them since"' + G), ('E520', '"Victor and Illinois"' + G),
 ('E520', '"Ingalls" "Baltic" Webster' + G),
 ('E532', '"mule teams complete"' + G), ('E532', '"what time can this"' + G), ('E532', '"transportation for 4000"' + G), ('E532', '"transportation for four thousand"' + G),
 ('E532', 'Bradley Webster "mule teams"' + G), ('E532', '"Jan. 16" Bradley' + G)]
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
            f.write(f'    {it.get("id")} {v.get("title","")[:60]} {v.get("subtitle","")[:40]} {v.get("publishedDate","")} | {s[:320]}\n')
        time.sleep(1.6)
print(open(OUT).read())
