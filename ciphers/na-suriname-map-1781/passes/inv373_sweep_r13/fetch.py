"""(copied from inv373_sweep_r12b, unchanged; originally inv373_sweep_r12) Fetch plan.tsv thumbnails (IIIF full/600,/) one at a time, >= 1.8 s apart, stop on first non-200/non-JPEG.
Usage: python3 fetch.py OUTDIR  (images stay in scratch; fetch.log is written here)."""
import subprocess,sys,time,os
out=sys.argv[1]; os.makedirs(out,exist_ok=True)
rows=[l.split('\t') for l in open('plan.tsv').read().split('\n')[1:] if l]
log=open('fetch.log','w'); log.write('order\tlabel\tresult\n')
for order,label,base in rows:
    n=label.split('_')[-1][:4]
    r=subprocess.run(['curl','-sS','-A','cipher-lab research script (contact via repository)','-o',f'{out}/s{n}.jpg',
        '-w','%{http_code} %{content_type}',base+'/full/600,/0/default.jpg'],capture_output=True,text=True)
    log.write(f'{order}\t{label}\t{r.stdout}\n'); log.flush()
    if not r.stdout.startswith('200 image'): print('stop',label,r.stdout); break
    time.sleep(1.9)
print('done')
