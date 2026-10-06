import json,time,subprocess,sys
v=json.load(open('viewer.json')); sc={s['order']:s for s in v['scans']}
want=[1,2]+[23+21*k for k in range(47)]
log=open('fetch.log','a')
for n in want:
    s=sc[n]; base=s['iiif']['url'].rsplit('/info.json',1)[0]
    url=base+'/full/600,/0/default.jpg'
    r=subprocess.run(['curl','-sS','-A','cipher-lab research script (contact via repository)','-o',f'p{n:04d}.jpg','-w','%{http_code} %{content_type}',url],capture_output=True,text=True)
    log.write(f"{n}\t{s['label']}\t{r.stdout}\n"); log.flush()
    if not r.stdout.startswith('200'): print('stop',n,r.stdout); break
    time.sleep(1.9)
print(len(want),'done')
