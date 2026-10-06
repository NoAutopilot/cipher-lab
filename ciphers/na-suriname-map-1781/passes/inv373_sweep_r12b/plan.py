"""R12-SURSWP3 sample plan: inv. 373 labels n = 2 mod 4 (the offset between the earlier 1-in-4 samples), in the order
0006-0266, 0802-1022, then 0602-0798, skipping every scan already sampled (R10-SUR triage, R10-SUR693's 0600-0796 sweep is
every 7th from 0600 -- read from its NOTES section, not a file --, R11-SURSWP, R12-SURSWP2) and the _deelopname02 halves,
capped at 119 IIIF requests (120 minus the one item-page request).
Usage: plan.py VIEWER_JSON (viewer.response from the item page's drupal-settings-json, scratch); writes plan.tsv."""
import json,re,sys
v=json.load(open(sys.argv[1]))
def labs(p): return {l.split('\t')[1] for l in open(p).read().split('\n')[1:] if l}
prev=labs('../inv373_triage_r10/sampled_scans.tsv')|labs('../inv373_sweep_r11/plan.tsv')|labs('../inv373_sweep_r12/plan.tsv')
prevn={int(re.search(r'_373_(\d{4})',l).group(1)) for l in prev}|{600+7*k for k in range(29)}
rows=[(int(re.search(r'_373_(\d{4})',s['label']).group(1)),s) for s in v['scans']]
def pick(a,b): return [s for n,s in rows if a<=n<=b and n%4==2 and n not in prevn and '_deelopname02' not in s['label']]
plan=(pick(6,266)+pick(802,1022)+pick(602,798))[:119]
with open('plan.tsv','w') as f:
    f.write('order\tlabel\tiiif_base\n')
    for s in plan: f.write(f"{s['order']}\t{s['label']}\t{s['iiif']['url'].rsplit('/info.json',1)[0]}\n")
print(len(plan), plan[0]['label'], plan[-1]['label'], len(pick(6,266)),len(pick(802,1022)),len(pick(602,798)))
