#!/usr/bin/env python3
"""TXE3-7 RESCORE truth-free diagnostics (11 Oct 2026, account 3). Reads no truth file. Prints:

 1. owner_map.tsv (owner strip tile -> atlas box, the join behind TXE3-7's TRAINING labels): for the 438 registered boxes,
    does the tile's label equal the atlas classify top-k of its box (atlas/topk: fr3252-no77 = f117r, no73 = f144r,
    no85 = f168r/v) at the mapped box, or at the box one or two places left/right on the same atlas line? Done for the
    owner's final label (new_sign) and the machine start label (old_sign), overall and per strip line.
 2. The machine start labels along each strip (the A1 control's labels): where the owner changed a tile's label, does his
    label equal the START label of the neighbouring tile (-1 / +1)? A run of such equalities on one strip is a start-label
    join shifted by one tile, which the owner's move repairs.
 3. The target-side box -> token maps: for the registered arms' own kNN top-1 (runs/A1, A2; these labels steered neither
    map), the line read's sign at the mapped position, -1, +1, -2, +2; old vs corrected maps, no.87 and f152r.
Run from the repo root: python3 benchmark-tx/txeng3/7/rescore/diagnostics.py"""
import csv, collections
X = 'benchmark-tx/txeng3/7'; T = 'ciphers/nevers-birago-fr3251-1572'
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
fam = lambda s: s.split('-')[0]
om = {r['sid']: r for r in rd(f'{T}/sorter/no87/owner_map.tsv')}
lab = {r['sid']: r for r in rd(f'{T}/harvest/bir87align/settled_corrected.tsv')}
used = {r['box'] for r in rd(f'{X}/labels/owner.tsv')}
topk = {}
for f in ('fr3252-no77', 'no73', 'no85'):
    topk.update({r['box']: r for r in rd(f'{T}/atlas/topk/{f}.tsv')})
byline = collections.defaultdict(list)
for r in rd(f'{T}/atlas/signs.tsv'):
    byline[(r['page'], r['line'])].append(r)
order = {}
for k, v in byline.items():
    v.sort(key=lambda r: int(r['x']))
    for i, r in enumerate(v):
        order[r['sid']] = (k, i)
reg = [(sid, m['box'], lab[sid]) for sid, m in om.items() if m['box'] in used and m['dup'] == '0' and sid in lab
       and lab[sid]['status'] not in ('aside', 'bad-cut') and lab[sid]['new_sign'] and lab[sid]['old_sign']]
print(f'1. owner_map.tsv: {len(reg)} registered tile->box joins; tile centre inside its box for',
      sum(1 for sid, b, r in reg if float(om[sid]['dist_px']) == 0), '(the rest: nearest box centre within 0.6 x tile height)')
for which in ('new_sign', 'old_sign'):
    tot = collections.Counter(); per = collections.defaultdict(collections.Counter)
    for sid, box, r in reg:
        k, i = order[box]; line = byline[k]; strip = sid.rsplit('_', 1)[0]
        for off in (0, -1, 1, -2, 2):
            j = i + off
            if 0 <= j < len(line) and line[j]['sid'] in topk:
                t = topk[line[j]['sid']]
                if fam(r[which]) in {t['k1'], t['k2'], t['k3']}:
                    tot[off] += 1; per[strip][off] += 1
    bad = sorted(s for s, c in per.items() if max(c[-1], c[1]) > c[0])
    print(f'   {which} in box top-3 at offset 0 / -1 / +1 / -2 / +2: {tot[0]} / {tot[-1]} / {tot[1]} / {tot[-2]} / {tot[2]};'
          f' strip lines where -1 or +1 beats 0: {bad or "none"}')
    if which == 'old_sign':
        for s in bad:
            print(f'      {s}: 0 / -1 / +1 = {per[s][0]} / {per[s][-1]} / {per[s][1]}')

print('2. start labels (A1) vs the owner label of the next/previous tile on the same strip (changed tiles only):')
strips = collections.defaultdict(list)
for sid, r in lab.items():
    s, n = sid.rsplit('_', 1); strips[s].append((int(n), sid, r))
tot = collections.Counter(); rows = []
for s, v in sorted(strips.items()):
    v.sort(); c = collections.Counter()
    for k, (n, sid, r) in enumerate(v):
        if om.get(sid, {}).get('box') not in used or om[sid]['dup'] != '0': continue
        if r['status'] in ('aside', 'bad-cut') or not r['new_sign'] or not r['old_sign']: continue
        nw = fam(r['new_sign'])
        if fam(r['old_sign']) == nw: continue
        c['changed'] += 1
        for off in (-1, 1):
            j = k + off
            if 0 <= j < len(v) and v[j][2]['old_sign'] and fam(v[j][2]['old_sign']) == nw:
                c[off] += 1
                break
    tot.update(c)
    if c[-1] + c[1] >= 4:
        rows.append(f'      {s}: changed {c["changed"]}, owner label = start label of tile -1: {c[-1]}, of tile +1: {c[1]}')
print(f'   changed boxes {tot["changed"]}; owner label equals a neighbour tile\'s start label: -1 {tot[-1]}, +1 {tot[1]}'
      f' ({tot[-1] + tot[1]} of {tot["changed"]}); strips with 4 or more:')
print('\n'.join(rows))

print('3. target maps: kNN top-1 of the registered arms == line read at the mapped position (0 / -1 / +1 / -2 / +2)')
def check(mp, read, labels):
    c = collections.Counter(); per = collections.defaultdict(collections.Counter)
    for sid, (line, pos) in mp.items():
        if sid not in labels: continue
        c['n'] += 1
        for off in (0, -1, 1, -2, 2):
            if read.get((line, int(pos) + off)) == labels[sid]:
                c[off] += 1; per[line][off] += 1
    return c, sorted(l for l, v in per.items() if max(v[-1], v[1]) > v[0])
one = lambda p: {r['sid']: (r['line'], r['pos']) for r in rd(p) if r['op'] == '1:1'}
cases = [('no87', ['f178v', 'f179r'], 'benchmark-tx/outputs/birago1572-no87/passC.tsv',
          [('registered map atlas/no87_box_token.tsv', f'{T}/atlas/no87_box_token.tsv'),
           ('corrected map atlas/no87_box_token_labelaware.tsv', f'{T}/atlas/no87_box_token_labelaware.tsv')]),
         ('f152r', ['f152r'], 'benchmark-tx/outputs/birago1572-f152r/passZ_pipeline.tsv',
          [('registered map f152r_box_token.tsv', f'{X}/f152r_box_token.tsv'),
           ('label-aware twin rescore/f152r_box_token_labelaware.tsv', f'{X}/rescore/f152r_box_token_labelaware.tsv')])]
for item, pages, rp, maps in cases:
    read = {(r['line'], int(r['pos'])): r['sign'] for r in rd(rp)}
    for name, p in maps:
        for arm in ('A1', 'A2'):
            labels = {r['box']: r['code'] for pg in pages for r in rd(f'{X}/runs/{arm}_{pg}.tsv')}
            c, bad = check(one(p), read, labels)
            print(f'   {item} {name} {arm}: n {c["n"]}: {c[0]} / {c[-1]} / {c[1]} / {c[-2]} / {c[2]}; lines where -1 or +1 beats 0: {bad or "none"}')
