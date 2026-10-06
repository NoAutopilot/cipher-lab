"""R13-SURSWP4 sample plan: the inv. 373 offset sweep's remainder named in the Verdict (R12-SURSWP3): labels n = 2 mod 4 in
0614-0798, then n = 0 mod 4 in 0270-0598 (R12-SURSWP2 already took n = 2 mod 4 there), skipping every scan already sampled
(R10-SUR triage, R10-SUR693's every-7th 0600-0796 sweep and its 0690-0696, R11-SURSWP, R12-SURSWP2, R12-SURSWP3) and the
_deelopname02 halves, capped at 129 IIIF requests.
Usage: plan.py VIEWER_JSON (viewer.response from the item page's drupal-settings-json, scratch); writes plan.tsv."""
import json,re,sys
v=json.load(open(sys.argv[1]))
def labs(p): return {l.split('\t')[1] for l in open(p).read().split('\n')[1:] if l}
prev=(labs('../inv373_triage_r10/sampled_scans.tsv')|labs('../inv373_sweep_r11/plan.tsv')|labs('../inv373_sweep_r12/plan.tsv')
      |labs('../inv373_sweep_r12b/plan.tsv'))
prevn={int(re.search(r'_373_(\d{4})',l).group(1)) for l in prev}|{600+7*k for k in range(29)}|set(range(690,697))
rows=[(int(re.search(r'_373_(\d{4})',s['label']).group(1)),s) for s in v['scans']]
def pick(a,b,r):
    seen=set(); out=[]
    for n,s in rows:
        if a<=n<=b and n%4==r and n not in prevn and n not in seen and '_deelopname02' not in s['label']:
            seen.add(n); out.append(s)
    return out
plan=(pick(614,798,2)+pick(270,598,0))[:129]
with open('plan.tsv','w') as f:
    f.write('order\tlabel\tiiif_base\n')
    for s in plan: f.write(f"{s['order']}\t{s['label']}\t{s['iiif']['url'].rsplit('/info.json',1)[0]}\n")
print(len(plan), plan[0]['label'], plan[-1]['label'], len(pick(614,798,2)),len(pick(270,598,0)))
