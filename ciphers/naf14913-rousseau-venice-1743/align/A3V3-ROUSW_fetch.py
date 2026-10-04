import json,time,urllib.request,hashlib,os
S='/tmp/claude-0/-home-user-cipher-lab/486a3e53-9e9e-53d2-b166-4722a3e8b2d8/scratchpad'
m=json.load(open('/home/user/cipher-lab/sources/gallica-manifests/btv1b525174513.json'));c=m['sequences'][0]['canvases']
out=open(S+'/fetch_manifest.tsv','a')
for n in range(595,801):
    fn=f'{S}/s300/c{n:03d}.jpg'
    if os.path.exists(fn): continue
    url=f'https://gallica.bnf.fr/iiif/ark:/12148/btv1b525174513/f{n}/full/300,/0/native.jpg'
    req=urllib.request.Request(url,headers={'User-Agent':'cipher-lab research script, contact via repository'})
    try:
        r=urllib.request.urlopen(req,timeout=60);b=r.read()
    except Exception as e:
        print('STOP',n,e,flush=True);break
    if not b.startswith(b'\xff\xd8'):
        print('STOP nonjpeg',n,flush=True);break
    open(fn,'wb').write(b)
    out.write(f'{n}\t{c[n-1]["label"]}\t{url}\t{len(b)}\t{hashlib.sha1(b).hexdigest()[:12]}\n');out.flush()
    time.sleep(1.5)
print('DONE',flush=True)
