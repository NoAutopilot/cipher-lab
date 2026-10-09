import json,subprocess,time,os
os.makedirs('img',exist_ok=True)
log=open('fetch.log','a'); plan=open('plan.tsv','w'); plan.write('inv\torder\tlabel\tid\n')
K=24
for inv in ['266','267','268','269','270']:
    sc=json.load(open(f'viewer{inv}.json'))['scans']; n=len(sc); step=(n-4)/K
    for o in sorted({int(5+step*k+step/2) for k in range(K)}):
        s=sc[o-1]; assert s['order']==o
        plan.write(f"{inv}\t{o}\t{s['label']}\t{s['id']}\n"); plan.flush()
        base=s['iiif']['url'].rsplit('/info.json',1)[0]
        r=subprocess.run(['curl','-sS','-A','cipher-lab research script (contact via repository)','-o',f'img/{inv}_{o:04d}.jpg','-w','%{http_code} %{content_type}',base+'/full/400,/0/default.jpg'],capture_output=True,text=True)
        log.write(f"{inv}\t{o}\t{s['label']}\t{r.stdout}\n"); log.flush()
        if not r.stdout.startswith('200 image'): print('stop',inv,o,r.stdout); raise SystemExit
        time.sleep(1.95)
print('done')
