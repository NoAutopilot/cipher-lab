"""R12-SURSWP2 sample plan: inv. 373 labels 0270-0599, 1 in 4 from 0270, skipping scans R10-SUR already sampled and the
_deelopname02 halves (as R11-SURSWP's plan.py), capped at 89 IIIF requests (90 minus the one item-page request).
Usage: plan.py VIEWER_JSON (viewer.response from the item page's drupal-settings-json, scratch); writes plan.tsv."""
import json,re,sys
v=json.load(open(sys.argv[1]))
prev={l.split('\t')[1] for l in open('../inv373_triage_r10/sampled_scans.tsv').read().split('\n')[1:] if l}
rows=[]
for s in v['scans']:
    m=re.search(r'_373_(\d{4})',s['label']); rows.append((int(m.group(1)),s))
plan=[s for n,s in rows if 270<=n<=599 and (n-270)%4==0 and s['label'] not in prev and '_deelopname02' not in s['label']][:89]
with open('plan.tsv','w') as f:
    f.write('order\tlabel\tiiif_base\n')
    for s in plan: f.write(f"{s['order']}\t{s['label']}\t{s['iiif']['url'].rsplit('/info.json',1)[0]}\n")
print(len(plan), plan[0]['label'], plan[-1]['label'])
