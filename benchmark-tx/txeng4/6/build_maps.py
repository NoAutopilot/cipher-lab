#!/usr/bin/env python3
"""TXE4-6 TIEBREAK unit 1 (12 Oct 2026, account 3): boxes and box-to-token maps for the three items, with no owner
evidence and every join through tools/box_token_align.py + tools/join_check.py (brief R4a; PREREG-txeng4-6 Deviation 1).

Per item: reconcile_passes.py A B --method nw -> rec_<item>/; the draft (every aligned column) is the read;
round 1 box_token_align --lam 0 (seed only); train labels = the round-1 1:1 boxes at agreed columns (A == B, lower
confidence not L); glyph_atlas classify --only-train-labels --topk 3 (the box itself never votes); round 2 with --topk,
--loo, check labels = that kNN's top-1 (steered -> leave-one-out positions), bounded by join_check.evaluate; on FAIL the
failing lines are dropped and the rest re-checked once. Tiles kept = 1:1 at the same (line, pos) in both rounds.
Reads no truth file. Usage: python3 benchmark-tx/txeng4/6/build_maps.py [no87 f152r gun]
"""
import csv, json, os, subprocess, sys
from collections import Counter, defaultdict
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
os.chdir(ROOT)
import box_token_align as BA
import join_check as JC
rd = BA.rd
OUT = 'benchmark-tx/txeng4/6'
A = 'ciphers/nevers-birago-fr3251-1572/atlas'
GUN = f'{OUT}/gun_atlas'
ITEMS = {
    'no87': dict(A='benchmark-tx/outputs/birago1572-no87/passA.tsv', B='benchmark-tx/outputs/birago1572-no87/passB.tsv',
                 atlas=A, pages=('f178r', 'f178v', 'f179r')),
    'f152r': dict(A='benchmark-tx/outputs/birago1572-f152r/passA.tsv', B='benchmark-tx/outputs/birago1572-f152r/passB.tsv',
                  atlas=A, pages=('f152r',)),
    'gun': dict(A='benchmark-tx/txeng3/3/passA_gun/passA_gun.tsv', B='benchmark-tx/txeng3/3/passB_gun/passB_gun.tsv',
                atlas=GUN, pages=tuple(f'g{i:02d}' for i in range(1, 18))),
}
XB = {'f152r_L01': lambda cx: cx > 2520, 'f152r_L04': lambda cx: cx < 2460}   # txeng3/7/rescore/map_f152r_la.py, unchanged


def gun_line(l):            # draft/base line L01 -> map line g01_L01 (one segmented page per crop)
    return f'g{int(l[1:]):02d}_L01' if l.startswith('L') and not l.startswith('g') else l


def wr(p, cols, rows):
    with open(p, 'w', encoding='utf-8') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(r.get(c, '')) for c in cols) + '\n')


def signs_for(item):
    S = rd(os.path.join(ITEMS[item]['atlas'], 'signs.tsv'))
    S = [s for s in S if s['page'] in ITEMS[item]['pages']]
    if item == 'f152r':             # atlas lines 2-5 are the letter's L01-L04; prose boxes dropped by the x bounds
        out = []
        for s in S:
            li = int(s['line'])
            if li < 2 or li > 5:
                continue
            s = dict(s); s['line'] = str(li - 1)
            cx = int(s['x']) + int(s['w']) / 2
            if XB.get(f'f152r_L{li - 1:02d}', lambda c: True)(cx):
                out.append(s)
        S = out
    return S


def segment_gun():
    if os.path.exists(f'{GUN}/signs.tsv'):
        return
    args = ['python3', 'tools/glyph_atlas.py', 'segment', '--out', GUN, '--median-h', 'pool']
    for i in range(1, 18):
        args += ['--page', f'g{i:02d}=benchmark-tx/txpool/gunther8246-p2/crops/p2_L{i:02d}.jpg']
    print(' '.join(args)); subprocess.run(args, check=True)
    json.dump({'signs': {}, 'marks': {}, 'override': {}, 'desc': {}}, open(f'{GUN}/labels.json', 'w'))
    with open(f'{GUN}/clusters.tsv', 'w') as f:
        f.write('id\tkind\tcluster\tdist\n')


def build(item):
    it = ITEMS[item]
    rec = f'{OUT}/rec_{item}'
    if not os.path.exists(f'{rec}/ciphertext_draft.tsv'):
        subprocess.run(['python3', 'tools/reconcile_passes.py', it['A'], it['B'], '--method', 'nw', '--out-dir', rec], check=True)
    if item == 'gun':
        segment_gun()
    draft = rd(f'{rec}/ciphertext_draft.tsv')
    ln = gun_line if item == 'gun' else (lambda l: l)
    read = [dict(line=ln(r['line']), pos=r['position'], sign=r['sign'].strip()) for r in draft if r['sign'].strip()]
    wr(f'{OUT}/read_{item}.tsv', ['line', 'pos', 'sign'], read)
    agreed = {(ln(r['line']), r['position']) for r in draft if r['why'] == 'agree' and r['confidence'] != 'L'}
    signs = signs_for(item)
    lines = sorted({r['line'] for r in read}, key=BA.split_line)
    # round 1: width only, a seed
    rows1, per1 = BA.build_map(signs, read, None, None, lines, 0.0, BA.NEUTRAL, False)
    wr(f'{OUT}/map1_{item}.tsv', BA.COLS, rows1)
    sign_at = {(r['line'], str(r['pos'])): r['sign'] for r in read}
    train = [dict(box=r['sid'], code=sign_at[(r['line'], str(r['pos']))]) for r in rows1
             if r['op'] == '1:1' and (r['line'], str(r['pos'])) in agreed]
    wr(f'{OUT}/train_{item}.tsv', ['box', 'code'], train)
    print(f'{item}: round 1 ops {dict(Counter(r["op"] for r in rows1))}; agreed columns {len(agreed)}; train tiles {len(train)}')
    topk = f'{OUT}/topk_{item}.tsv'
    subprocess.run(['python3', 'tools/glyph_atlas.py', 'classify', '--out', it['atlas'], '--labels',
                    os.path.join(it['atlas'], 'labels.json'), '--page', 'all', '--tsv', topk, '--train-labels',
                    f'{OUT}/train_{item}.tsv', '--only-train-labels', '--topk', '3', '--knn', '5'], check=True)
    want = {s['sid'] for s in signs}
    labels = BA.read_labels(topk)
    chk = {r['box']: r['k1'] for r in rd(topk) if r['box'] in want and r['k1'] and r['k1'] != '_'}
    wr(f'{OUT}/check_{item}.tsv', ['sid', 'label'], [dict(sid=s, label=l) for s, l in sorted(chk.items())])
    # round 2: label-aware, own-label leave-one-out
    rows2, per2 = BA.build_map(signs, read, labels, None, lines, BA.LAM, BA.NEUTRAL, True)
    rs = defaultdict(set)
    for r in read:
        rs[(r['line'], int(r['pos']))].add(r['sign'])
    mp = f'{OUT}/map_{item}.tsv'
    dropped = []
    for attempt in (1, 2):
        keep = [r for r in rows2 if r['line'] not in dropped]
        wr(mp, BA.COLS, keep)
        res = JC.evaluate(BA.positions(keep, loo=True), chk, rs)
        print(f'{item} join check (steered, leave-one-out) attempt {attempt}: {res["verdict"]} n={res["n"]} '
              f'overall {res["overall"]} share0={res["share0"]:.3f} (null p95 {res["p95_0"]:.3f}) '
              f'share+-1={res["sharepm1"]:.3f} (bound {res["b2_bound"]:.3f})')
        for l, d in sorted(res['lines'].items(), key=lambda t: BA.split_line(t[0])):
            print(f'  {l}: 0/-1/+1/+-2/none {d["counts"].get("0",0)}/{d["counts"].get("-1",0)}/{d["counts"].get("+1",0)}/'
                  f'{d["counts"].get("+-2",0)}/{d["counts"].get("none",0)} placed {d["placed"]} {d["verdict"]}')
        if res['verdict'] == 'FAIL' and attempt == 1:
            dropped = [l for l, d in res['lines'].items() if d['verdict'] == 'fail']
            if not dropped:        # FAIL on B2 only: nothing to drop line-wise
                break
            print(f'{item}: dropping failing lines {dropped} and re-checking once')
            continue
        break
    sc = JC.write_sidecar(mp, res, inputs=[os.path.join(it['atlas'], 'signs.tsv'), f'{OUT}/read_{item}.tsv', f'{OUT}/check_{item}.tsv'])
    p1 = {r['sid']: (r['line'], str(r['pos'])) for r in rows1 if r['op'] == '1:1'}
    tiles = [dict(sid=r['sid'], line=r['line'], pos=r['pos']) for r in keep
             if r['op'] == '1:1' and p1.get(r['sid']) == (r['line'], str(r['pos']))]
    wr(f'{OUT}/tiles_{item}.tsv', ['sid', 'line', 'pos'], tiles)
    dis = rd(f'{rec}/disagreements.tsv')
    reach = [(ln(r['line']), r['col']) for r in dis if r['A'] not in ('', '-') and r['B'] not in ('', '-')]
    tl = {(t['line'], str(t['pos'])) for t in tiles}
    cov = sum(1 for k in reach if k in tl)
    print(f'{item}: verdict {res["verdict"]}; dropped lines {dropped}; tiles kept (1:1 both rounds) {len(tiles)} of '
          f'{sum(1 for r in keep if r["op"] == "1:1")} 1:1; split rows {len(dis)}, reachable (both non-blank) {len(reach)}, '
          f'with a kept box {cov} ({cov / max(1, len(reach)):.2f}) -> {sc}')
    json.dump(dict(item=item, verdict=res['verdict'], dropped=dropped, tiles=len(tiles), split_rows=len(dis),
                   reachable=len(reach), reachable_boxed=cov), open(f'{OUT}/maps_{item}.json', 'w'), indent=1)


if __name__ == '__main__':
    for item in (sys.argv[1:] or ['no87', 'f152r', 'gun']):
        build(item)
