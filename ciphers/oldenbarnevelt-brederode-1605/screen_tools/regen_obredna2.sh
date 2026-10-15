#!/bin/bash
# OBRED-NA2 (15 Oct 2026): re-derive the NL-HaNA 1.01.02 inv. 9450-9460 scans listed (OBRED-NA2 rows) in na_obredna_scans.tsv
# (38 requests incl. the 11 item pages). Images stay outside git. Run from this folder. Usage: bash screen_tools/regen_obredna2.sh OUTDIR
set -e; O=${1:-scratch_obredna2}; mkdir -p $O
python3 - "$O" <<'PY'
import sys,re,json,time,urllib.request
UA="cipher-lab research script (contact via repository)"; O=sys.argv[1]
def get(u):
    b=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":UA}),timeout=60).read(); time.sleep(3.2); return b
P={"9450":[1],"9451":[1,15,30,45],"9452":[1,6],"9453":[1,12,24,36],"9454":[1],"9455":[1,4],"9456":[1],"9457":[1],
   "9458":[1,5],"9459":[2,4,6,8,10,12,14,16],"9460":[1]}
for inv,orders in P.items():
    x=get(f"https://www.nationaalarchief.nl/onderzoeken/archief/1.01.02/invnr/{inv}").decode("utf-8")
    m=re.search(r'data-drupal-selector="drupal-settings-json">(.*?)</script>',x,re.S)
    sc=json.loads(json.loads(m.group(1))["viewer"]["response"])["scans"]
    mp={s["order"]:s["iiif"]["url"].replace("/info.json","") for s in sc}
    for o in orders: open(f"{O}/{inv}_s{o:04d}_900.jpg","wb").write(get(f"{mp[o]}/full/900,/0/default.jpg"))
PY
sha1sum $O/*.jpg
