"""Fetch NA IIIF scans from an order->iiif-base map (from the item page). usage: fetch_map.py MAP.json OUTDIR WIDTH ORDERS..."""
import sys, json, time, os, urllib.request
UA = "cipher-lab research script (contact via repository)"
mp, out, w = json.load(open(sys.argv[1])), sys.argv[2], sys.argv[3]
os.makedirs(out, exist_ok=True); log = open(os.path.join(out, "requests.log"), "a")
for o in sys.argv[4:]:
    fn = os.path.join(out, f"s{int(o):04d}_{w}.jpg")
    if os.path.exists(fn): continue
    url = f"{mp[str(int(o))]}/full/{w},/0/default.jpg"
    r = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60); b = r.read()
    log.write(f"{time.strftime('%H:%M:%S', time.gmtime())}\t{r.status}\t{url}\n"); log.flush()
    if b[:2] != b"\xff\xd8": print("not jpeg", o); break
    open(fn, "wb").write(b); time.sleep(2.1)
print("done")
