#!/bin/bash
# OBRED-NA (15 Oct 2026): re-derive the NL-HaNA 1.01.02 inv. 9459 and inv. 4562 scans listed in na_obredna_scans.tsv (16 requests incl. the
# two item pages). Images stay outside git. Run from this folder. Usage: bash screen_tools/regen_obredna.sh OUTDIR
set -e; O=${1:-scratch_obredna}; mkdir -p $O
python3 - "$O" <<'PY'
import sys,re,json,time,urllib.request
UA="cipher-lab research script (contact via repository)"; O=sys.argv[1]
def get(u):
    b=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":UA}),timeout=60).read(); time.sleep(3.2); return b
for inv,w,orders in (("9459",900,[1,3,5,7,9,11,13,15,17]),("4562",1000,[32,35,36,37,50])):
    x=get(f"https://www.nationaalarchief.nl/onderzoeken/archief/1.01.02/invnr/{inv}").decode("utf-8")
    m=re.search(r'data-drupal-selector="drupal-settings-json">(.*?)</script>',x,re.S)
    sc=json.loads(json.loads(m.group(1))["viewer"]["response"])["scans"]
    mp={s["order"]:s["iiif"]["url"].replace("/info.json","") for s in sc}
    for o in orders: open(f"{O}/{inv}_s{o:04d}_{w}.jpg","wb").write(get(f"{mp[o]}/full/{w},/0/default.jpg"))
PY
sha1sum $O/*.jpg
