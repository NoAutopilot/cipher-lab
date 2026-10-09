import sys,re,time,subprocess,os,json
mets,inv,out=sys.argv[1],sys.argv[2],sys.argv[3]
t=open(mets).read()
uuid=re.search(r'<altRecordID TYPE="apeID">([0-9a-f-]+)<',t).group(1)
p='/'.join(re.findall('..',uuid.replace('-','')))
divs=re.findall(r'<div ID="ID([0-9a-f-]+)" ORDER="(\d+)"[^>]*LABEL="([^"]+)"',t)
os.makedirs(out,exist_ok=True); log=[]
for sid,order,label in divs:
    fn=os.path.join(out,label)
    if os.path.exists(fn): continue
    url=f"https://service.archief.nl/iip/iipsrv?IIIF={p}/{sid}.jp2/full/400,/0/default.jpg"
    r=subprocess.run(['curl','-sS','-A','cipher-lab research script (contact via repository)','-o',fn,'-w','%{http_code} %{content_type}',url],capture_output=True,text=True)
    log.append((label,r.stdout)); print(label,r.stdout,flush=True)
    if not r.stdout.startswith('200') or 'image' not in r.stdout:
        print('STOP non-200/non-image'); break
    time.sleep(1.6)
json.dump({'inv':inv,'mets_uuid':uuid,'iiif_prefix':p,'scans':[{'id':s,'order':int(o),'label':l} for s,o,l in divs]},open(os.path.join(out,'scanlist.json'),'w'),indent=0)
