import json,subprocess,time
log=open('fetch.log','a')
jobs=[('372',o,600) for o in [184,185,186,187,188,190,191,192,193,194]]+[('379',28,1100),('380',319,1100)]
for inv,o,w in jobs:
    s=json.load(open(f'viewer{inv}.json'))['scans'][o-1]; assert s['order']==o
    base=s['iiif']['url'].rsplit('/info.json',1)[0]
    f=f'img/nb_{inv}_{o:04d}_{w}.jpg'
    r=subprocess.run(['curl','-sS','-A','cipher-lab research script (contact via repository)','-o',f,'-w','%{http_code} %{content_type}',base+f'/full/{w},/0/default.jpg'],capture_output=True,text=True)
    log.write(f"{inv}\t{o}\t{s['label']}\t{r.stdout}\tnb\n"); log.flush()
    if not r.stdout.startswith('200 image'): print('stop',inv,o,r.stdout); break
    time.sleep(1.9)
print('done')
