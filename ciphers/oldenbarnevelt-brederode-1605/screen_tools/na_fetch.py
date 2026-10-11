"""Fetch NA METS once and IIIF images for listed scan orders. usage: fetch.py METS_UUID OUTDIR WIDTH ORDERS..."""
import sys, time, re, json, os, urllib.request
UA = "cipher-lab research script (contact via repository)"
mets_id, out, width = sys.argv[1], sys.argv[2], sys.argv[3]
orders = [int(x) for x in sys.argv[4:]]
os.makedirs(out, exist_ok=True)
log = open(os.path.join(out, "requests.log"), "a")
def get(url):
    r = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60)
    b = r.read(); log.write(f"{time.strftime('%H:%M:%S', time.gmtime())}\t{r.status}\t{url}\n"); log.flush(); return b
mp = os.path.join(out, f"mets_{mets_id}.xml")
if not os.path.exists(mp):
    open(mp, "wb").write(get(f"https://service.archief.nl/gaf/api/mets/v1/{mets_id}")); time.sleep(2.1)
x = open(mp, encoding="utf-8").read()
# map order -> file uuid
om = {}
for m in re.finditer(r'<(?:mets:)?div[^>]*ORDER="(\d+)"[^>]*>(.*?)</(?:mets:)?div>', x, re.S):
    f = re.search(r'FILEID="ID([0-9a-f-]+)DEF"', m.group(2))
    if f: om[int(m.group(1))] = f.group(1)
p = "/".join(re.findall("..", mets_id.replace("-", "")))
json.dump({"mets": mets_id, "n": len(om)}, open(os.path.join(out, "mets_info.json"), "w"))
print("scans in METS:", len(om))
for o in orders:
    fn = os.path.join(out, f"s{o:04d}_{width}.jpg")
    if os.path.exists(fn): continue
    url = f"https://service.archief.nl/iip/iipsrv?IIIF={p}/{om[o]}.jp2/full/{width},/0/default.jpg"
    b = get(url)
    if b[:2] != b"\xff\xd8": print("not jpeg", o); break
    open(fn, "wb").write(b); time.sleep(2.1)
print("done")
