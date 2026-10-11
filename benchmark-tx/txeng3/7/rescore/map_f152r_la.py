#!/usr/bin/env python3
"""TXE3-7 RESCORE (11 Oct 2026, account 3): a label-aware box -> token map for birago1572-f152r, the f152r twin of
atlas/no87_map.py --label-aware (BOXMAP-LA). TXE3-7's registered f152r map (../map_f152r.py -> ../f152r_box_token.tsv) is
NOT the old no.87 file, but it runs the same label-blind width-only DP, so it can carry the same defect: one box that is
not a letter, mapped 1:1, pushes the rest of a line one token late.

Everything of ../map_f152r.py is kept (atlas page f152r lines 2-5 = letter L01-L04; the same x bounds that drop the prose
boxes; the per-line median box width as W; the line read of record passZ_pipeline.tsv as the token sequence). Added, from
tools/box_token_align.py with its defaults (lam 1.5, neutral 0.5, own-label leave-one-out on): truth-blind box labels =
the cluster-name classifier with the f152r page excluded and labels.json's per-tile overrides removed (../runs/A0a_f152r.tsv,
k1 weight 1.0, k2/k3 0.5) -- the f152r analogue of no.87's topk_no87_allheld.tsv. No sorter statuses exist for f152r.
Guard: with lam 0 the tool must reproduce ../f152r_box_token.tsv row for row (asserted on every run).

Writes rescore/f152r_box_token_labelaware.tsv (sid, line, pos, op, labels, loo_pos, old_pos). --check exits 1 when the
committed file differs from a fresh run (CLAUDE.md rule 7). Reads no truth file. Run from the repo root."""
import csv, os, sys, collections
sys.path.insert(0, 'tools')
import box_token_align as BA
X = 'benchmark-tx/txeng3/7'; A = 'ciphers/nevers-birago-fr3251-1572/atlas'
OUT = f'{X}/rescore/f152r_box_token_labelaware.tsv'
rd = BA.rd
S = [r for r in rd(f'{A}/signs.tsv') if r['page'] == 'f152r']
toks = collections.defaultdict(list)
for r in rd('benchmark-tx/outputs/birago1572-f152r/passZ_pipeline.tsv'):
    toks[r['line']].append(r)
XB = {'f152r_L01': lambda cx: cx > 2520, 'f152r_L04': lambda cx: cx < 2460}   # ../map_f152r.py, unchanged
labels = BA.read_labels(f'{X}/runs/A0a_f152r.tsv')
old = {r['sid']: (r['line'], r['pos']) for r in rd(f'{X}/f152r_box_token.tsv') if r['op'] == '1:1'}


def build(lam):
    out = []
    for li, L in ((2, 'f152r_L01'), (3, 'f152r_L02'), (4, 'f152r_L03'), (5, 'f152r_L04')):
        bx = sorted((r for r in S if int(r['line']) == li), key=lambda r: int(r['x']))
        bx = [r for r in bx if XB.get(L, lambda cx: True)(int(r['x']) + int(r['w']) / 2)]
        Wmed = sorted(int(r['w']) for r in bx)[len(bx) // 2]
        boxes = [dict(sid=r['sid'], w=r['w'], labels=labels.get(r['sid']) if lam else None, status='') for r in bx]
        tk = [dict(pos=t['pos'], signs={t['sign']}) for t in toks[L]]
        rows, skipped = BA.align_line(boxes, tk, Wmed, lam, BA.NEUTRAL, True)
        for r in rows:
            r['line'] = L; r['old_pos'] = old[r['sid']][1] if r['sid'] in old else ''
        out += rows
    return out


blind = {(r['sid'], r['line'], str(r['pos'])) for r in build(0.0) if r['op'] == '1:1'}
assert blind == {(s, l, p) for s, (l, p) in old.items()}, 'lam 0 does not reproduce ../f152r_box_token.tsv'
rows = build(BA.LAM)
cols = ['sid', 'line', 'pos', 'op', 'labels', 'loo_pos', 'old_pos']
text = '\t'.join(cols) + '\n' + ''.join('\t'.join(str(r.get(c, '')) for c in cols) + '\n' for r in rows)
moved = [(r['sid'], r['old_pos'], r['pos']) for r in rows if r['op'] in ('1:1', 'unsure') and r['old_pos'] and str(r['old_pos']) != str(r['pos'])]
lost = sorted(s for s in old if s not in {r['sid'] for r in rows if r['op'] in ('1:1', 'unsure')})
print('lam 0 reproduces the registered f152r map:', len(blind), 'of', len(old), '1:1 rows')
print('ops', dict(collections.Counter(r['op'] for r in rows)), '| one-token boxes moved', moved, '| old 1:1 no longer one-token', lost)
if '--check' in sys.argv:
    ok = os.path.exists(OUT) and open(OUT).read() == text
    print('map_f152r_la --check:', 'current' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(OUT, 'w').write(text); print('->', OUT)
