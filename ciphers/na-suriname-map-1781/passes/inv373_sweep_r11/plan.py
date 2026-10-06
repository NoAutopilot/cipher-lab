"""R11-SURSWP sample plan: inv. 373 labels 0800-1028 then 0001-0599, 1 in 4, skipping scans R10-SUR already sampled,
capped at 119 IIIF requests (120 minus the one item-page request). Reads viewer.json (from the item page's
drupal-settings-json, scratch), writes plan.tsv."""
import json,re,sys
v=json.load(open(sys.argv[1]))
prev={l.split('\t')[1] for l in open('../inv373_triage_r10/sampled_scans.tsv').read().split('\n')[1:] if l}
rows=[]
for s in v['scans']:
    m=re.search(r'_373_(\d{4})',s['label']); rows.append((int(m.group(1)),s))
def pick(lo,hi):
    out=[]
    for n,s in rows:
        if lo<=n<=hi and (n-lo)%4==0 and s['label'] not in prev and '_deelopname02' not in s['label']: out.append(s)
    return out
plan=pick(800,1028)+pick(1,599)
plan=plan[:119]
with open('plan.tsv','w') as f:
    f.write('order\tlabel\tiiif_base\n')
    for s in plan: f.write(f"{s['order']}\t{s['label']}\t{s['iiif']['url'].rsplit('/info.json',1)[0]}\n")
print(len(plan), plan[0]['label'], plan[-1]['label'])
