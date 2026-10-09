import json,subprocess,time,os
os.makedirs('img',exist_ok=True)
log=open('fetch.log','a'); plan=open('plan.tsv','w'); plan.write('inv\torder\tlabel\tid\n')
K=22
for inv in ['370','371','372','378','379','380']:
    v=json.load(open(f'viewer{inv}.json')); sc=v['scans']; n=len(sc)
    step=(n-4)/K
    orders=sorted({int(5+step*k+step/2) for k in range(K)})
    for o in orders:
        s=sc[o-1]; assert s['order']==o
        plan.write(f"{inv}\t{o}\t{s['label']}\t{s['id']}\n"); plan.flush()
        base=s['iiif']['url'].rsplit('/info.json',1)[0]
        f=f"img/{inv}_{o:04d}.jpg"
        r=subprocess.run(['curl','-sS','-A','cipher-lab research script (contact via repository)','-o',f,'-w','%{http_code} %{content_type}',base+'/full/600,/0/default.jpg'],capture_output=True,text=True)
        log.write(f"{inv}\t{o}\t{s['label']}\t{r.stdout}\n"); log.flush()
        if not r.stdout.startswith('200 image'): print('stop',inv,o,r.stdout); raise SystemExit
        time.sleep(1.9)
print('done')
