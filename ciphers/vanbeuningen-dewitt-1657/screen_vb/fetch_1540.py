import re,sys,time,subprocess
t=open('1540/mets.xml').read()
uuid='442ce4c5-2316-4890-aed8-3759c5e3bae6'
p='/'.join(re.findall('..',uuid.replace('-','')))
divs={int(o):(s,l) for s,o,l in re.findall(r'<div ID="ID([0-9a-f-]+)" ORDER="(\d+)"[^>]*LABEL="([^"]+)"',t)}
for a in sys.argv[1:]:
    n,w=a.split(':'); s,l=divs[int(n)]
    fn=f'1540/{l}' if w=='400' else f'1540/w{w}_{l}'
    r=subprocess.run(['curl','-sS','-A','cipher-lab research script (contact via repository)','-o',fn,'-w','%{http_code} %{content_type}',f'https://service.archief.nl/iip/iipsrv?IIIF={p}/{s}.jp2/full/{w},/0/default.jpg'],capture_output=True,text=True)
    print(n,w,fn,r.stdout,flush=True); 
    if not r.stdout.startswith('200'): break
    time.sleep(1.8)
