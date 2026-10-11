#!/usr/bin/env python3
"""TXE3-7 RESCORE step 1 (11 Oct 2026, account 3; no truth read here). The registered TXE3-7 arms joined their no.87 kNN codes
to token positions through atlas/no87_box_token.tsv, the label-blind width DP that the TXE3-9 second check found shifts whole
stretches of a line by one token (f178v L06, L09, L11, L13, L21, f179r L03 ...). This re-builds every registered arm's
outputs with the corrected map and nothing else changed:

  * the classify outputs are the committed ../runs/*.tsv (the instrument does not touch the map; re-running all 69 classify
    calls at this commit reproduced every file byte for byte, RESCORE.md);
  * no.87 (target S): atlas/no87_box_token_labelaware.tsv, op == '1:1' rows only (as the registered run kept op == '1:1');
    f178r still has no map and keeps the line read in every arm;
  * f152r (target P): its registered map ../f152r_box_token.tsv is not the old no.87 file and is used unchanged for the
    registered figures (../out/); because it runs the same label-blind DP, a label-aware twin (map_f152r_la.py ->
    f152r_box_token_labelaware.tsv) is also applied, as a sensitivity row (outputs here, out/*_birago1572-f152r.tsv);
  * the same two output modes (atlas, override) and the same rules as ../run_arms.py.

POST HOC, reported separately (the second check's X_NEW-l -> T19 ruling, owner_review_2026-10-04.tsv q2): labels/
owner_xnewl_t19.tsv = ../labels/owner.tsv with the boxes of the owner's X_NEW-l pile coded T19 instead of X_NEW; classify
with the same settings into runs/A2x_<page>.tsv; outputs under the corrected maps (out/) and, to reproduce the second check's
figure, under the registered maps (out_oldmap/).

Writes out/, out_oldmap/, runs/, labels/, can_vary_la.json (boxes whose top-1 differs between arms, counted BEFORE scoring).
Run from the repo root: python3 benchmark-tx/txeng3/7/rescore/run_arms_la.py"""
import csv, json, os, subprocess, sys
A = 'ciphers/nevers-birago-fr3251-1572/atlas'; X = 'benchmark-tx/txeng3/7'; R = f'{X}/rescore'
B = 'ciphers/nevers-birago-fr3251-1572'
for d in ('out', 'out_oldmap', 'runs', 'labels'):
    os.makedirs(f'{R}/{d}', exist_ok=True)
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
PAGES = ['f152r', 'f178v', 'f179r']
TAGS = ['A0a', 'A1', 'A2'] + [f'A3s{s}' for s in range(1, 21)]

# post-hoc labels: X_NEW-l -> T19 (owner_review_2026-10-04.tsv q2), on the registered 438 boxes only
om = {r['sid']: r for r in rd(f'{B}/sorter/no87/owner_map.tsv')}
xl = {om[r['sid']]['box'] for r in rd(f'{B}/harvest/bir87align/settled_corrected.tsv')
      if r['new_sign'] == 'X_NEW-l' and r['status'] not in ('aside', 'bad-cut') and r['old_sign']
      and om.get(r['sid'], {}).get('box') and om[r['sid']]['dup'] == '0'}
own = rd(f'{X}/labels/owner.tsv')
assert all(r['code'] == 'X_NEW' for r in own if r['box'] in xl)
with open(f'{R}/labels/owner_xnewl_t19.tsv', 'w') as f:
    f.write('box\tcode\n' + ''.join(f"{r['box']}\t{'T19' if r['box'] in xl else r['code']}\n" for r in own))
print('post hoc: X_NEW-l boxes recoded T19:', len(xl), sorted(xl))

res = {}
for page in PAGES:
    for tag in TAGS:
        res[(tag, page)] = rd(f'{X}/runs/{tag}_{page}.tsv')
    tsv = f'{R}/runs/A2x_{page}.tsv'
    if not os.path.exists(tsv):
        subprocess.run([sys.executable, 'tools/glyph_atlas.py', 'classify', '--out', A, '--page', page, '--tsv', tsv, '--topk', '3',
                        '--labels', f'{A}/labels.json', '--train-labels', f'{R}/labels/owner_xnewl_t19.tsv', '--only-train-labels'],
                       check=True, capture_output=True, text=True)
    res[('A2x', page)] = rd(tsv)

one = lambda p: {r['sid']: (r['line'], r['pos']) for r in rd(p) if r['op'] == '1:1'}
MAPS = {'new': {'birago1572-no87': one(f'{A}/no87_box_token_labelaware.tsv'), 'birago1572-f152r': one(f'{R}/f152r_box_token_labelaware.tsv')},
        'old': {'birago1572-no87': one(f'{A}/no87_box_token.tsv'), 'birago1572-f152r': one(f'{X}/f152r_box_token.tsv')}}
reads = {'birago1572-f152r': rd('benchmark-tx/outputs/birago1572-f152r/passZ_pipeline.tsv'),
         'birago1572-no87': rd('benchmark-tx/outputs/birago1572-no87/passC.tsv')}
item_pages = {'birago1572-f152r': ['f152r'], 'birago1572-no87': ['f178v', 'f179r']}


def write(tag, item, mp, odir):
    code = {mp[r['box']]: (r['code'], float(r['share'])) for page in item_pages[item] for r in res[(tag, page)] if r['box'] in mp}
    for mode in ('atlas', 'override'):
        with open(f'{odir}/{tag}_{mode}_{item}.tsv', 'w') as f:
            f.write('line\tpos\tsign\n')
            for t in reads[item]:
                s = t['sign']; c = code.get((t['line'], t['pos']))
                if c and c[0] not in ('_', '_held') and (mode == 'atlas' or (c[1] >= 0.995 and c[0] != s)):
                    s = c[0]
                f.write(f"{t['line']}\t{t['pos']}\t{s}\n")


for item in item_pages:
    for tag in TAGS + ['A2x']:
        write(tag, item, MAPS['new'][item], f'{R}/out')
    write('A2x', item, MAPS['old'][item], f'{R}/out_oldmap')

# can-vary under the corrected maps (no truth); same counts as ../can_vary.json
can = {}
for item, pages in item_pages.items():
    mp = MAPS['new'][item]; base = {(t['line'], t['pos']): t['sign'] for t in reads[item]}
    codes = lambda tag: {mp[r['box']]: r['code'] for page in pages for r in res[(tag, page)] if r['box'] in mp}
    c1, c2, c0, cx = codes('A1'), codes('A2'), codes('A0a'), codes('A2x')
    keys = sorted(c1)
    nulls = [sum(1 for k in keys if codes(f'A3s{s}')[k] != c2[k]) for s in range(1, 21)]
    can[item] = dict(map='atlas/no87_box_token_labelaware.tsv' if item.endswith('no87') else 'rescore/f152r_box_token_labelaware.tsv',
                     mapped_tokens=len(keys), A1_ne_A2=sum(1 for k in keys if c1[k] != c2[k]),
                     A0a_ne_A2=sum(1 for k in keys if c0[k] != c2[k]),
                     A2_ne_null=dict(min=min(nulls), mean=sum(nulls) / 20, max=max(nulls)),
                     A1_ne_lineread=sum(1 for k in keys if c1[k] != base[k]), A2_ne_lineread=sum(1 for k in keys if c2[k] != base[k]),
                     posthoc_A2x_ne_A2=sum(1 for k in keys if cx[k] != c2[k]), posthoc_A2x_ne_A1=sum(1 for k in keys if cx[k] != c1[k]))
    # positions whose arm code changes between the registered and the corrected map (same classify output, different join)
    old = MAPS['old'][item]
    for tag in ('A1', 'A2'):
        co = {old[r['box']]: r['code'] for page in pages for r in res[(tag, page)] if r['box'] in old}
        cn = codes(tag)
        eff = lambda c, k: base[k] if c.get(k) in (None, '_', '_held') else c[k]
        can[item][f'{tag}_atlas_tokens_changed_by_map'] = sum(1 for k in set(co) | set(cn) if eff(co, k) != eff(cn, k))
json.dump(can, open(f'{R}/can_vary_la.json', 'w'), indent=1)
print(json.dumps(can, indent=1))
