import re,json,subprocess,time,sys
for inv in sys.argv[1:]:
    r=subprocess.run(['curl','-sS','-A','cipher-lab research script (contact via repository)','-o',f'item{inv}.html','-w','%{http_code}',f'https://www.nationaalarchief.nl/onderzoeken/archief/1.05.03/invnr/{inv}'],capture_output=True,text=True)
    print(inv,r.stdout,flush=True)
    t=open(f'item{inv}.html').read()
    m=re.search(r'<script[^>]*data-drupal-selector="drupal-settings-json"[^>]*>(.*?)</script>',t,re.S)
    v=json.loads(json.loads(m.group(1))['viewer']['response'])
    json.dump(v,open(f'viewer{inv}.json','w')); print(inv,v['availability'],len(v['scans']),flush=True)
    time.sleep(2)
