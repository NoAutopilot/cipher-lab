#!/usr/bin/env python3
"""TXE3-7 step 3: run every arm of PREREG-txeng3-7.md through tools/glyph_atlas.py classify and build the tx_bench outputs.
No truth is read here. Arms: A0a = cluster names only (labels.json 'signs', no overrides; no no.87 box votes on no.87, the
target page excluded on f152r); A1 = machine labels; A2 = owner labels; A3 = null seeds 1-20 (labels/*.tsv, --only-train-labels).
Pages: f152r (target P) and f178v, f179r (target S; f178r has no box map and keeps the line read in every arm).
Outputs: runs/<arm>_<page>.tsv (classify), out/<arm>_atlas_<item>.tsv and out/<arm>_override_<item>.tsv (line, pos, sign),
can_vary.json (boxes whose top-1 differs between arms, counted BEFORE scoring). Run from the repo root."""
import csv, json, os, subprocess, sys, collections
A = 'ciphers/nevers-birago-fr3251-1572/atlas'; W = 'benchmark-tx/txeng3/7'
R, O = f'{W}/runs', f'{W}/out'; os.makedirs(R, exist_ok=True); os.makedirs(O, exist_ok=True)
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
# cluster-names-only labels.json for A0a
L = json.load(open(f'{A}/labels.json')); L0 = dict(L); L0['override'] = {}
json.dump(L0, open(f'{W}/labels_clusters_only.json', 'w'))
PAGES = ['f152r', 'f178v', 'f179r']
arms = {'A1': f'{W}/labels/machine.tsv', 'A2': f'{W}/labels/owner.tsv'}
arms.update({f'A3s{s}': f'{W}/labels/null_{s}.tsv' for s in range(1, 21)})

def classify(tag, page, extra):
    tsv = f'{R}/{tag}_{page}.tsv'
    if os.path.exists(tsv): return rd(tsv)
    cmd = [sys.executable, 'tools/glyph_atlas.py', 'classify', '--out', A, '--page', page, '--tsv', tsv, '--topk', '3'] + extra
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    return rd(tsv)

res = {}
for page in PAGES:
    hold = ['--holdout', 'f178r_', '--holdout', 'f178v_', '--holdout', 'f179r_'] if page != 'f152r' else ['--exclude-page']
    res[('A0a', page)] = classify('A0a', page, ['--labels', f'{W}/labels_clusters_only.json'] + hold)
    for tag, tl in arms.items():
        res[(tag, page)] = classify(tag, page, ['--labels', f'{A}/labels.json', '--train-labels', tl, '--only-train-labels'])
        print(tag, page, 'done', flush=True)

# box -> token maps and line reads of record
maps = {'birago1572-f152r': {r['sid']: (r['line'], r['pos']) for r in rd(f'{W}/f152r_box_token.tsv')},
        'birago1572-no87': {r['sid']: (r['line'], r['pos']) for r in rd(f'{A}/no87_box_token.tsv') if r['op'] == '1:1'}}
reads = {'birago1572-f152r': rd('benchmark-tx/outputs/birago1572-f152r/passZ_pipeline.tsv'),
         'birago1572-no87': rd('benchmark-tx/outputs/birago1572-no87/passC.tsv')}
item_pages = {'birago1572-f152r': ['f152r'], 'birago1572-no87': ['f178v', 'f179r']}
tags = ['A0a'] + list(arms)
can = {}
for item, pages in item_pages.items():
    base = reads[item]
    for tag in tags:
        code = {}
        for page in pages:
            for r in res[(tag, page)]:
                if r['box'] in maps[item]:
                    code[maps[item][r['box']]] = (r['code'], float(r['share']))
        for mode in ('atlas', 'override'):
            with open(f'{O}/{tag}_{mode}_{item}.tsv', 'w') as f:
                f.write('line\tpos\tsign\n')
                for t in base:
                    s = t['sign']; c = code.get((t['line'], t['pos']))
                    if c and c[0] not in ('_', '_held') and (mode == 'atlas' or (c[1] >= 0.995 and c[0] != s)):
                        s = c[0]
                    f.write(f"{t['line']}\t{t['pos']}\t{s}\n")
    # can-vary: mapped boxes whose top-1 differs between arms (no truth involved)
    def codes(tag):
        return {maps[item][r['box']]: r['code'] for page in pages for r in res[(tag, page)] if r['box'] in maps[item]}
    c1, c2, c0 = codes('A1'), codes('A2'), codes('A0a')
    keys = sorted(c1)
    nulls = [sum(1 for k in keys if codes(f'A3s{s}')[k] != c2[k]) for s in range(1, 21)]
    can[item] = dict(mapped_tokens=len(keys), A1_ne_A2=sum(1 for k in keys if c1[k] != c2[k]),
                     A0a_ne_A2=sum(1 for k in keys if c0[k] != c2[k]), A2_ne_null=dict(min=min(nulls), mean=sum(nulls) / 20, max=max(nulls)),
                     A1_ne_lineread=sum(1 for k in keys if c1[k] != next(t['sign'] for t in base if (t['line'], t['pos']) == k)),
                     A2_ne_lineread=sum(1 for k in keys if c2[k] != next(t['sign'] for t in base if (t['line'], t['pos']) == k)),
                     A2_override_n=sum(1 for page in pages for r in res[('A2', page)] if r['box'] in maps[item] and float(r['share']) >= 0.995 and r['code'] not in ('_', '_held')),
                     A1_override_n=sum(1 for page in pages for r in res[('A1', page)] if r['box'] in maps[item] and float(r['share']) >= 0.995 and r['code'] not in ('_', '_held')))
json.dump(can, open(f'{W}/can_vary.json', 'w'), indent=1)
print(json.dumps(can, indent=1))
