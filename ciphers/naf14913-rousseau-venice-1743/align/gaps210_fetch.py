import json,time,urllib.request,hashlib,os,sys
S='/tmp/claude-0/-home-user-cipher-lab/dd6c29d6-6496-5bf8-b6e2-45c43428b1a8/scratchpad'
m=json.load(open('sources/gallica-manifests/btv1b525174513.json'));c=m['sequences'][0]['canvases']
todo=[424,425]+list(range(423,14,-1))
out=open(S+'/fetch_log.tsv','a')
for n in todo:
    fn=f'{S}/s300/c{n:03d}.jpg'
    if os.path.exists(fn): continue
    url=f'https://gallica.bnf.fr/iiif/ark:/12148/btv1b525174513/f{n}/full/300,/0/native.jpg'
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (cipher-lab research script, contact via repository)'})
    try:
        r=urllib.request.urlopen(req,timeout=60);b=r.read();ct=r.headers.get('Content-Type','')
    except Exception as e:
        print('STOP',n,e,flush=True);out.write(f'{n}\t{c[n-1]["label"]}\tERR {e}\n');break
    if not b.startswith(b'\xff\xd8'):
        print('STOP non-jpeg',n,ct,flush=True);out.write(f'{n}\t{c[n-1]["label"]}\tNONJPEG {ct}\n');break
    open(fn,'wb').write(b)
    out.write(f'{n}\t{c[n-1]["label"]}\t{url}\t{len(b)}\t{hashlib.sha1(b).hexdigest()[:12]}\n');out.flush()
    time.sleep(1.5)
print('DONE',flush=True)
