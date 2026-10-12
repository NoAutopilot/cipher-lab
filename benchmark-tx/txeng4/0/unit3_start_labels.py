#!/usr/bin/env python3
"""TXE4-0 REPAIR unit 3 (12 Oct 2026, account 3): re-attach the 3 Oct family-sorter start labels by geometry
instead of by index. Read-free, truth-free.

What exists. On 3 Oct the family sorter's start labels (sign_sorter_apply's old_sign; TXE3-7's A1 machine control)
were attached to strip tiles by index: `build_inputs.py` (both sorters) zips each passage's own line-read rows
(in position order, from harvest/f117/la/passD.tsv or harvest/lookalike/<run>_passD.tsv) against that passage's own
boxes (in x order) one-to-one -- so a tile's sid already encodes the ORIGINAL index/position it took
(f117_L09_07 is the 7th box of passage L09, which got the 7th line-read row). The sorter READMEs warn "f117 L09:
29 vs 30; f168 R03: 18 vs 19 ... the tile index may be one off" (ciphers/nevers-birago-fr3251-1572/harvest/
tx_decode/eye/open/sorter/README.md).

Geometric re-attachment: for each passage (treated as its own "line"), tools/box_token_align.py aligns that
passage's own boxes (signs.tsv x/w, in x order) against that passage's own line-read sequence (the old_sign values
of harvest/bir87align/settled_corrected.tsv, keyed back to their own position by the sid's own suffix -- this is
exactly the sequence passD.tsv gave, since old_sign is an unedited copy of it), steered by each box's OWN atlas
cluster label: sorter sid -> atlas box (sorter/no87/owner_map.tsv, the geometric centroid join TXE3-7's RESCORE
found sound) -> atlas box's classify top-3 (atlas/topk/{fr3252-no77,no73,no85}.tsv, by the owner_map's atlas_page).
A tile's re-attached start label is the read sign at its NEW (geometric) position, 1:1 boxes only.

Never reads a truth file, BENCHMARK-TX.tsv row or clerk sheet; the inputs are exactly those named above.

Usage: python3 benchmark-tx/txeng4/0/unit3_start_labels.py
"""
import csv
import os
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import box_token_align as BA  # noqa: E402
import join_check as JC  # noqa: E402

T = os.path.join(ROOT, 'ciphers/nevers-birago-fr3251-1572')
F117 = os.path.join(ROOT, 'ciphers/birago-fr3252-1571-72')
OUT = os.path.join(ROOT, 'ciphers/nevers-birago-fr3251-1572/harvest/bir87align')
rd = BA.rd
TOPK = {'f117r': os.path.join(T, 'atlas/topk/fr3252-no77.tsv'), 'f144r': os.path.join(T, 'atlas/topk/no73.tsv'),
        'f168r': os.path.join(T, 'atlas/topk/no85.tsv'), 'f168v': os.path.join(T, 'atlas/topk/no85.tsv')}


def split_sid(sid):
    run = sid.split('_', 1)[0]
    rest = sid[len(run) + 1:]
    psg, pos = rest.rsplit('_', 1)
    return run, psg, int(pos)


def load():
    settled = {r['sid']: r['old_sign'] for r in rd(os.path.join(OUT, 'settled_corrected.tsv'))}
    owner_map = {r['sid']: (r['atlas_page'], r['box']) for r in rd(os.path.join(T, 'sorter/no87/owner_map.tsv')) if r['box']}
    topk_cache = {}

    def atlas_topk(atlas_page, box):
        if atlas_page not in topk_cache:
            topk_cache[atlas_page] = {r['box']: r for r in rd(TOPK[atlas_page])}
        return topk_cache[atlas_page].get(box)

    signs = {}
    for sorter_dir in (F117, T):
        for r in rd(os.path.join(sorter_dir, 'sorter/signs.tsv')):
            signs[r['sid']] = r
    return settled, owner_map, atlas_topk, signs


def group_by_psg(settled):
    groups = defaultdict(list)
    for sid in settled:
        run, psg, pos = split_sid(sid)
        groups[(run, psg)].append((sid, pos))
    return groups


def weights_for(sid, owner_map, atlas_topk):
    om = owner_map.get(sid)
    if not om:
        return None
    page, box = om
    r = atlas_topk(page, box)
    if not r:
        return None
    w = {}
    for k, wt in (('k1', 1.0), ('k2', 0.5), ('k3', 0.5)):
        code = (r.get(k) or '').strip()
        if code and code != '_':
            w[code] = max(w.get(code, 0.0), wt)
    return w or None


def do_psg(run, psg, members, signs, owner_map, atlas_topk, settled):
    bx_sids = sorted((sid for sid, _ in members), key=lambda s: int(signs[s]['x']))
    n = len(bx_sids)
    pos_of_sid = {sid: pos for sid, pos in members}            # the sid's OWN encoded original position
    read_sign = {p: {settled[s] for s, p2 in members if p2 == p} for p in range(1, n + 1)}
    old_pos_of = {sid: ('PSG_L01', str(pos_of_sid[sid])) for sid in bx_sids}

    boxes = [dict(sid=sid, w=signs[sid]['w'], labels=weights_for(sid, owner_map, atlas_topk), status='') for sid in bx_sids]
    toks = [dict(pos=str(p), signs=read_sign[p]) for p in range(1, n + 1)]
    W = sorted(int(signs[s]['w']) for s in bx_sids)[n // 2]
    rows, _ = BA.align_line(boxes, toks, W, BA.LAM, BA.NEUTRAL, True)
    new_pos_of = {r['sid']: ('PSG_L01', str(r['pos'])) for r in rows if r['op'] == '1:1'}
    read_sign_lbl = {('PSG_L01', p): s for p, s in read_sign.items()}

    check_labels = {sid: next(iter(weights_for(sid, owner_map, atlas_topk) or {}), None) for sid in bx_sids}
    check_labels = {sid: lab for sid, lab in check_labels.items() if lab}
    r_old = JC.evaluate(old_pos_of, check_labels, read_sign_lbl)
    r_new = JC.evaluate(new_pos_of, check_labels, read_sign_lbl)

    out_rows = []
    for sid in bx_sids:
        index_pos = pos_of_sid[sid]
        index_start = settled[sid]
        if sid in new_pos_of:
            geom_pos = int(new_pos_of[sid][1])
            geom_start = next(iter(read_sign[geom_pos]))
            op = 'kept' if geom_pos == index_pos else 'moved'
        else:
            geom_pos, geom_start, op = '', '', 'unmapped'
        changed = int(geom_start != index_start) if geom_start else ''
        out_rows.append(dict(sid=sid, strip=f'{run}_{psg}', index_pos=index_pos, index_start=index_start,
                             geom_pos=geom_pos, geom_start=geom_start, op=op, changed=changed))
    return out_rows, r_old, r_new


def main():
    settled, owner_map, atlas_topk, signs = load()
    groups = group_by_psg(settled)
    all_rows = []
    print('shift check, old (index) join vs new (geometric) join, per strip passage:')
    for (run, psg), members in sorted(groups.items()):
        rows, r_old, r_new = do_psg(run, psg, members, signs, owner_map, atlas_topk, settled)
        all_rows += rows
        c_old, c_new = r_old['overall'], r_new['overall']
        print(f"  {run}_{psg} (n={len(members)}): old 0/-1/+1 {c_old.get('0', 0)}/{c_old.get('-1', 0)}/{c_old.get('+1', 0)} "
              f"({r_old['verdict']}) -> new 0/-1/+1 {c_new.get('0', 0)}/{c_new.get('-1', 0)}/{c_new.get('+1', 0)} ({r_new['verdict']})")

    with open(os.path.join(OUT, 'start_labels_geom.tsv'), 'w') as f:
        cols = ['sid', 'strip', 'index_pos', 'index_start', 'geom_pos', 'geom_start', 'op', 'changed']
        f.write('\t'.join(cols) + '\n')
        for r in all_rows:
            f.write('\t'.join(str(r.get(c, '')) for c in cols) + '\n')

    corrected = {r['sid']: r for r in rd(os.path.join(OUT, 'settled_corrected.tsv'))}
    geom = {r['sid']: r for r in all_rows}
    out2 = []
    for sid, r in corrected.items():
        g = geom.get(sid)
        new_old = g['geom_start'] if g and g['geom_start'] else r['old_sign']
        status = 'moved' if r['new_sign'] != new_old else 'kept'
        out2.append(dict(sid=sid, old_sign=new_old, new_sign=r['new_sign'], status=status,
                         corrected_from=r.get('corrected_from', '')))
    with open(os.path.join(OUT, 'settled_geom.tsv'), 'w') as f:
        cols = ['sid', 'old_sign', 'new_sign', 'status', 'corrected_from']
        f.write('\t'.join(cols) + '\n')
        for r in out2:
            f.write('\t'.join(str(r.get(c, '')) for c in cols) + '\n')

    changed = [r for r in all_rows if r['changed'] == 1]
    moved_old = sum(1 for r in out2 if r['status'] == 'moved')
    kept_old_total = sum(1 for r in corrected.values() if r['status'] == 'kept')
    moved_old_total = sum(1 for r in corrected.values() if r['status'] == 'moved')
    moved_new = moved_old
    kept_new = len(out2) - moved_new
    print(f'\nchanged start labels (old index_start != new geom_start): {len(changed)} of {len(all_rows)}')
    per_strip = defaultdict(int)
    for r in changed:
        per_strip[r['strip'].split('_')[0]] += 1
    print('  per run:', dict(per_strip))
    print(f'\nold (index-attached) kept/moved totals: kept {kept_old_total}, moved {moved_old_total}')
    print(f'new (geometry-attached) kept/moved totals: kept {kept_new}, moved {moved_new}')
    diff_count = sum(1 for sid in corrected if sid in geom and geom[sid]['geom_start'] and
                     geom[sid]['geom_start'] != corrected[sid]['old_sign'] and
                     corrected[sid]['new_sign'] == geom[sid]['geom_start'])
    print(f'of the boxes where A1 (old_sign) and A2 (new_sign) differ, now counted as kept '
          f'(owner label == re-attached start label): {diff_count} of '
          f"{sum(1 for sid, r in corrected.items() if r['old_sign'] != r['new_sign'])} "
          f"(TXE3-7 section 1 predicted 62 of 121)")


if __name__ == '__main__':
    main()
