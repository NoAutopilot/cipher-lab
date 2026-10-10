import json,subprocess,time,sys
for a in sys.argv[1:]:
    inv,o=a.split('_'); o=int(o)
    s=json.load(open(f'viewer{inv}.json'))['scans'][o-1]; assert s['order']==o
    base=s['iiif']['url'].rsplit('/info.json',1)[0]
    r=subprocess.run(['curl','-sS','-A','cipher-lab research script (contact via repository)','-o',f'img/look_{inv}_{o:04d}.jpg','-w','%{http_code} %{content_type}',base+'/full/1200,/0/default.jpg'],capture_output=True,text=True)
    open('fetch.log','a').write(f"{inv}\t{o}\t{s['label']}\t{r.stdout}\tlook1200\n"); print(a,r.stdout,flush=True); time.sleep(1.95)
