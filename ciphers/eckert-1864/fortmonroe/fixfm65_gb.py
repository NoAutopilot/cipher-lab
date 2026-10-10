#!/usr/bin/env python3
"""FIX-FM65 (10 Oct 2026, account 1, for LANE LEDGER-13): Google Books API (keyed, country=US) snippet sweep of Grant Papers vols. 13-14 for the
unaudited 1865 Fort Monroe entries. Controls first (E531, E530). A hit = a snippet from a Grant Papers vol. 13/14 volume id whose bolded words cover
>= 3 of the query's content words. >= 1.6 s apart; never prints the key. Output: fixfm65_gb.out (tsv-ish)."""
import json, os, re, sys, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
V13 = {'mnRjmhe3QLoC', 'ij8fAQAAMAAJ'}; V14 = {'DVLPEPsH1_oC', '1D8fAQAAMAAJ'}
P = [('CTRL-E531', ['"six vessels" Oriental', '"Suwo Nada" "half an hour"']),
     ('CTRL-E530', ['"sailed in perfect order"', '"sailed in perfect order" Fort Fisher'])]
P += [(e, q) for e, q in [
 ('E500', ['"Baltic" anchor chain expedition Newport', '"anchor and chain" steamer Baltic']),
 ('E505', ['steamers "coaled and loaded" rations Howell', 'Webster Howell steamers capacity coaled']),
 ('E506', ['Rawlins steamers "Jamestown" started', 'Beckwith Sheldon Rawlins Jamestown steamers']),
 ('E508', ['"C. C. Leary" City Point ten days coal', 'Leary Montauk Howell']),
 ('E509', ['"C. C. Leary" Bendford Montauk Metropolis', 'Bendford Alliance Metropolis hospital boat']),
 ('E511', ['"Eliza Hancox" Winants light-draft', 'Winants "Eliza Hancox"']),
 ('E513', ['Binney paymaster Brice Butler second expedition', '"not mustered" 31 December Binney']),
 ('E514', ['Blackstone Leary 350 troops no transportation', 'Beckwith Sheldon 350 troops river steamer Blackstone']),
 ('E515', ['Ariel Victor Illinois "Sedgwick" Baltic Newport', '"Gen. Sedgwick" Baltic Ariel Victor Illinois']),
 ('E517', ['Baltic countermanded Monroe embark troops Newport', 'Baltic "ordered to Monroe"']),
 ('E518', ['"Elias Smith" Tribune correspondent expedition', 'Elias Smith Tribune Ingalls Monroe']),
 ('E521', ['Beckwith "has left Monroe" Butler "don\'t mention"', 'Rawlins enquired Butler left Monroe bound']),
 ('E525', ['Baltic left for Monroe countermanded Newport coal Annapolis', 'Baltic "return her to Annapolis"']),
 ('E526', ['Emerick Ingalls forage vessels Abbott James', 'General Abbott no troops arrived Monroe forage']),
 ('E527', ['Carney "negro affairs" Eastville Butler relieved resign', 'Whiting Eastville Carney Norfolk resign']),
 ('E528', ['Ariel "General Sedgwick" arrived Baltimore troops Ingalls forage', 'Ingalls "no forage vessels" James']),
 ('E529', ['Ericsson Puritan shaft blockade runner Niagara Beaufort', 'Puritan shaft Ericsson Department approbation']),
 ('E536', ['Fort Fisher "New Inlet" Terry Tribune Dana Sheldon', 'Dana Eckert Tribune correspondent Fort Fisher surrendered Terry']),
 ('E537', ['Mulford flag-of-truce Varina Blair Ord', '"Varina" Blair Mulford flag of truce Ord']),
 ('E539', ['Lynch "St. Lawrence" Phlox torpedoes 900 pounds', 'Parker torpedoes insulating wire Phlox']),
 ('E541', ['Nevada Monroe recruits City Point Webster steamer', 'steamer Nevada recruits Webster Monroe']),
 ('E542', ['Saugus Washington Grant needs her at once Berrien', 'Saugus half way turn her back Secretary of the Navy']),
 ('E543', ['Ord "return to your headquarters in the field" contingency', 'Ord absent several days charge army operations']),
 ('E544', ['Palmer Newbern "6000 men" report', '"not less than 6000 men" Newbern Palmer']),
 ('E545', ['Schofield one battery each division Boyd Willards', 'Schofield "one battery with each division"']),
 ('E546', ['Foster Willards ship ordered Portsmouth New Hampshire detached Parker', 'Portsmouth New Hampshire detached executive officer Parker ship']),
 ('E548', ['President Annapolis Point Lookout boat leaving cipher Bates Eckert', '"Point Lookout" President Annapolis boat passes Bates']),
 ('E549', ['Stager cipher operator Schofield construction corps North Carolina', 'Schofield "cipher operator" Stager construction corps']),
 ('E550', ['Blodget Annapolis Schofield despatches Sherman Anderson', 'Jay F. Anderson Schofield Annapolis Sherman despatches']),
 ('E551', ['Rhode Island patrol Cape Henry Cape Fear River vessels Fort Fisher', '"Cape Henry" "Cape Fear" patrol Rhode Island Roads']),
 ('E552', ['Dumbarton Cambridge ready James River vessel Navy', 'Dumbarton "up the James River" Cambridge Tuesday']),
 ('E553', ['Vogdes Eastern District Commission command Emerick Ord', 'Vogdes "Eastern District" investigation Ord']),
 ('E554', ['Gordon "take the command for the present" Vogdes', 'Gordon Vogdes investigation Ord command district']),
 ('E555', ['Rucker battery 440 horses Schofield Meagher division', 'Rucker Meagher 23rd Corps 10,000 men horses']),
 ('E557', ['torpedoes Wise Bureau of Ordnance James River not received', 'Wise ordnance submarine torpedoes immediate use James']),
 ('E558', ['Ord office Yorktown operators Quartermaster Monroe', 'Yorktown telegraph office Ord operators Eckert']),
 ('E560', ['Yorktown telegraph station battery operator Chief Quartermaster Monroe', 'Yorktown station "without delay" battery operator']),
 ('E562', ['Washburne Johnson "state\'s evidence" Committee of Commerce', 'Johnson rascal Washburne under guard Monroe']),
 ('E564', ['"out of pilots" monitors James River James', 'pilots monitors up James River Bradley Chief Quartermaster']),
 ('E565', ['scout Roberts 139th New York Bowers', 'Roberts "139th New York" scout Bowers']),
 ('E566', ['Sumner "Mounted Rifles" Turner Army of the James', 'E. V. Sumner First Mounted Rifles Turner']),
 ('E567', ['Schofield engines flat cars Wright Newbern', 'Wright engines flat cars Schofield Newbern']),
 ('E568', ['Schofield line Fort Fisher Wilmington double line Goldsboro Eckert', 'double line Goldsboro Wilmington Schofield telegraph']),
 ('E569', ['moving office Mrs. Ord Sheldon Eckert', 'Monroe telegraph office Mrs. Ord move']),
 ('E571', ['Glisson gunboat convoy Roberts Babcock', 'Glisson convoy Rawlins Beckwith gunboat']),
 ('E572', ['Champion Wilmington Sherman Fayetteville', 'steamship Champion Fayetteville Sherman Wilmington']),
 ('E573', ['Hurlbut Charleston James River Montauk Kinston Glisson', 'Kinston Hurlbut Montauk Glisson']),
 ('E574', ['Stanton left 1 P.M. City Point Fortress Monroe 11 P.M. Dealy', 'Eckert Sheldon Dealy Secretary of War arrive Fortress Monroe']),
 ('E575', ['Gordon gunboats Suffolk Nansemond cavalry land', 'Nansemond cavalry gunboats Suffolk Gordon Beckwith']),
 ('E576', ['Gordon guide Boyle Blackwater bridging Ord', 'Blackwater crossed Boyle guide Gordon']),
 ('E577', ['Abbot Gordon command district East Virginia Stanton', 'Gordon continue command district Abbot order Emerick'])]]
STOP = {'the','and','for','are','was','with','from','not','his','has','all','her'}
out = open('fixfm65_gb.out', 'w'); n = 0
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
