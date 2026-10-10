#!/usr/bin/env python3
"""FM-S65B (10 Oct 2026, account 1, for LANE LEDGER-17): Google Books API (keyed, country=US) snippet sweep of Grant Papers vols. 13-14 for the
unaudited 1865 Fort Monroe entries. Controls first (E531, E530). A hit = a snippet from a Grant Papers vol. 13/14 volume id whose bolded words cover
>= 3 of the query's content words. >= 1.6 s apart; never prints the key. Output: fm_s65b_gb.out (tsv-ish)."""
import json, os, re, sys, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
V13 = {'mnRjmhe3QLoC', 'ij8fAQAAMAAJ'}; V14 = {'DVLPEPsH1_oC', '1D8fAQAAMAAJ'}
P = [
 ('5892/1', ['Monohansett leave Monroe Eckert wishes meet arrival', 'steamer Monohansett Beckwith Sheldon']),
 ('5896/0', ['"staff officer" letter "retained no copy" Seward', 'Grant Seward letter staff officer Fort Monroe February 1865']),
 ('5896/1', ['Anderson despatches Sherman Annapolis Friday Schofield']),
 ('5908/0', ['Radford New Ironsides torpedoes Lynch Bureau of Ordnance', 'Radford Lynch twenty torpedoes forward immediately']),
 ('5910/1', ['Cammann gold sell Cooper naval officer', 'Camman Company gold Eckert approval']),
 ('5914/2', ['Gordon commission adjourned cashier National Bank Norfolk', 'Meredith Gordon commission cashier call before it']),
 ('5936/2', ['ponchos not on hand Canby Sheridan Ingalls', 'ponchos Canby Ingalls Beckwith']),
 ('5941/2', ['Sherman John Sherman "City Point" Goldsboro Newbern Wednesday', 'Sherman brother Fort Monroe "going to see" Grant Goldsboro'])]
STOP = {'the','and','for','are','was','with','from','not','his','has','all','her'}
out = open('fm_s65b_gb_run2.out', 'w'); n = 0
only = sys.argv[1:]
for e, qs in P:
    if only and e not in only: continue
    for q in qs:
        words = [w.lower() for w in re.findall(r"[A-Za-z0-9']+", q) if len(w) > 2 and w.lower() not in STOP]
        url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q + ' intitle:Grant', 'country': 'US', 'maxResults': 15, 'key': K})
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60)); n += 1
            hits = []
            for it in d.get('items', []):
                vid = it.get('id')
                if vid not in V13 | V14: continue
                s = (it.get('searchInfo') or {}).get('textSnippet', '')
                bold = {b.lower() for b in re.findall(r'<b>([^<]+)</b>', s)}
                cov = sum(1 for w in set(words) if any(w in b for b in bold))
                hits.append((('v13' if vid in V13 else 'v14'), vid, cov, s))
            if not hits: out.write(f'{e}\t{q}\tNO HIT (total {d.get("totalItems")})\n')
            for v, vid, cov, s in hits:
                out.write(f'{e}\t{q}\t{v} {vid}\tcov {cov}/{len(set(words))}\t{re.sub(chr(10)," ",s)[:400]}\n')
        except Exception as ex:
            out.write(f'{e}\t{q}\tERR {str(ex)[:60]}\n')
        out.flush(); time.sleep(1.6)
out.write(f'# requests {n}\n'); out.close()
