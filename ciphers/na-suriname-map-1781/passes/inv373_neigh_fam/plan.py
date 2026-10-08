"""FAM-SUR373 plan: every label in the neighbour ranges of the four glossed inv. 373 letters named by R13-SURSWP4 (0697-0701,
0703-0729, 0731-0745, 0747-0757), including scans earlier sweeps sampled (a full look, not an offset), skipping _deelopname02 halves.
Usage: plan.py VIEWER_JSON (viewer.response from the item page's drupal-settings-json, scratch); writes plan.tsv."""
import json,re,sys
v=json.load(open(sys.argv[1]))
want=set(range(697,702))|set(range(703,730))|set(range(731,746))|set(range(747,758))
seen=set(); plan=[]
for s in v['scans']:
    n=int(re.search(r'_373_(\d{4})',s['label']).group(1))
    if n in want and n not in seen and '_deelopname02' not in s['label']:
        seen.add(n); plan.append(s)
with open('plan.tsv','w') as f:
    f.write('order\tlabel\tiiif_base\n')
    for s in plan: f.write(f"{s['order']}\t{s['label']}\t{s['iiif']['url'].rsplit('/info.json',1)[0]}\n")
print(len(plan), sorted(want-seen))
