import json,subprocess,time
log=open('fetch.log','a')
for inv,o in [('266',937),('267',217),('269',152)]:
    s=json.load(open(f'viewer{inv}.json'))['scans'][o-1]; assert s['order']==o
    base=s['iiif']['url'].rsplit('/info.json',1)[0]
    r=subprocess.run(['curl','-sS','-A','cipher-lab research script (contact via repository)','-o',f'img/nb_{inv}_{o:04d}_1200.jpg','-w','%{http_code} %{content_type}',base+'/full/1200,/0/default.jpg'],capture_output=True,text=True)
    log.write(f"{inv}\t{o}\t{s['label']}\t{r.stdout}\tnb\n"); log.flush(); print(inv,o,r.stdout)
    time.sleep(2)
