#!/bin/bash
# OBRED-945X (15 Oct 2026): re-derive NL-HaNA 1.01.02 inv. 9450 (4..70), 9451 (4..58), 9453 (4..46) at stride 3 (57 scans, 700 px; 3 item pages
# on www.nationaalarchief.nl + 57 IIIF requests on service.archief.nl) and the 7 contact sheets (SHEET_SCANS=9, seed 9450).
# Run from the target folder. Usage: bash screen_tools/regen_945x.sh OUTDIR  (images stay outside git)
set -e; O=${1:-scratch_945x}; I=images; mkdir -p $O/i945x
python3 - "$O/i945x" <<'PY'
import sys,re,json,time,os,urllib.request
UA="cipher-lab research script (contact via repository)"; O=sys.argv[1]; log=open(f"{O}/requests.log","a")
def get(u):
    r=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":UA}),timeout=60); b=r.read()
    log.write(f"{time.strftime('%H:%M:%S',time.gmtime())}\t{r.status}\t{u}\n"); log.flush(); time.sleep(3.2); return b
P={"9450":range(4,71,3),"9451":range(4,59,3),"9453":range(4,47,3)}
for inv,orders in P.items():
    x=get(f"https://www.nationaalarchief.nl/onderzoeken/archief/1.01.02/invnr/{inv}").decode("utf-8")
    m=re.search(r'data-drupal-selector="drupal-settings-json">(.*?)</script>',x,re.S)
    sc=json.loads(json.loads(m.group(1))["viewer"]["response"])["scans"]
    mp={s["order"]:s["iiif"]["url"].replace("/info.json","") for s in sc}
    print(inv,"scans on item page:",len(sc))
    for o in orders:
        fn=f"{O}/s{inv}{o:03d}_700.jpg"
        if os.path.exists(fn): continue
        b=get(f"{mp[o]}/full/700,/0/default.jpg")
        if b[:2]!=b"\xff\xd8": print("not jpeg",inv,o); sys.exit(1)
        open(fn,"wb").write(b)
PY
ORD=$(python3 -c "print(' '.join([f'9450{o:03d}' for o in range(4,71,3)]+[f'9451{o:03d}' for o in range(4,59,3)]+[f'9453{o:03d}' for o in range(4,47,3)]))")
SHEET_SCANS=9 python3 screen_tools/contact_sheets.py $O/i945x 700 $O/sh $O/key.json 9450 $I/na_301_14_2016_p0031.jpg $I/na_101_02_6016_p0261.jpg $I/na_101_02_6016_p0187_1200.jpg $ORD
[ -f $I/945x_screen_sheetkey.json ] && cmp $O/key.json $I/945x_screen_sheetkey.json && echo "sheet key reproduces"
true
