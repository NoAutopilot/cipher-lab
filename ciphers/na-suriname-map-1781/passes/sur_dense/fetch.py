import json,subprocess,time,os,csv
os.makedirs('img',exist_ok=True)
done={}
for r in csv.DictReader(open('/home/user/cipher-lab/sources/na-1.05.03/2026-10-09/screen_gov.tsv'),delimiter='\t'):
    done.setdefault(r['inv'],set()).add(int(r['viewer_order']))
log=open('fetch.log','a'); plan=open('plan.tsv','w'); plan.write('inv\torder\tlabel\tid\n')
K=26
for inv in ['370','371','378','379','380']:
    sc=json.load(open(f'viewer{inv}.json'))['scans']; n=len(sc); step=n/K
    for k in range(K):
        o=int(step*k+step*0.37)+1
        while o in done.get(inv,()): o+=1
        s=sc[o-1]; assert s['order']==o
        plan.write(f"{inv}\t{o}\t{s['label']}\t{s['id']}\n"); plan.flush()
        base=s['iiif']['url'].rsplit('/info.json',1)[0]
        r=subprocess.run(['curl','-sS','-A','cipher-lab research script (contact via repository)','-o',f'img/{inv}_{o:04d}.jpg','-w','%{http_code} %{content_type}',base+'/full/400,/0/default.jpg'],capture_output=True,text=True)
        log.write(f"{inv}\t{o}\t{s['label']}\t{r.stdout}\n"); log.flush()
        if not r.stdout.startswith('200 image'): print('stop',inv,o,r.stdout,flush=True); raise SystemExit
        time.sleep(1.95)
print('done')
