#!/usr/bin/env python3
"""BOXMAP-RESCORE (others), 11 Oct 2026, account 3: TXE-D's read-free proxy (benchmark-tx/txeng/prep) re-joined through a box map.

tools/tx_prep.py proxy classified each setting's re-rendered f178v L01-12 boxes (committed: prep/proxy/<setting>_topk.tsv) and
joined box -> line-read position with tools/tx_compare.box_map (the old width DP) into <setting>_bench.tsv. The classification does
not depend on the map, so the join can be redone from the committed topk files: this writes <setting>_bench.tsv for every setting
with positions from MAP (a no87 map with sid line pos op: 1:1 -> the box; a 2:1 pair -> the wider box, as tx_prep does; a 1:2 box ->
both tokens; unsure / bad-cut -> the box at its position; an old-format map, which lists a 2:1 pair by its first box only, gets the
pair's second box as the next box in x order on that line, and a 1:2 box its second token, as the DP took them), rows in the same format as tx_prep's.
  python3 rebench.py MAP OUTDIR           (MAP = atlas/no87_box_token.tsv reproduces the committed bench files byte for byte)
"""
import csv, glob, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
P = os.path.join(ROOT, 'benchmark-tx/txeng/prep/proxy')
A = os.path.join(ROOT, 'ciphers/nevers-birago-fr3251-1572/atlas')
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))


def main(mapf, od):
    os.makedirs(od, exist_ok=True)
    sg = rd(os.path.join(A, 'signs.tsv'))
    w = {r['sid']: int(r['w']) for r in sg}
    nxt = {}                                  # the next box in x order on the same page line (an old-format 2:1 lists only its first box)
    lines = {}
    for r in sg:
        lines.setdefault((r['page'], r['line']), []).append(r)
    for v in lines.values():
        v.sort(key=lambda r: int(r['x']))
        for a_, b_ in zip(v, v[1:]):
            nxt[a_['sid']] = b_['sid']
    dev = {f'f178v_L{i:02d}' for i in range(1, 13)}
    L = [r for r in rd(os.path.join(ROOT, 'benchmark-tx/outputs/birago1572-no87/labels.tsv')) if r['line'] in dev]
    order = {(r['line'], r['pos']): i for i, r in enumerate(L)}
    by = {}
    for r in rd(mapf):
        if r['line'] not in dev or not r['sid']:
            continue
        by.setdefault((r['line'], r['pos']), []).append((r['sid'], r['op']))
        if r['op'] == '2:1' and 'labels' not in r and r['sid'] in nxt:      # old map: add the pair's second box
            by[(r['line'], r['pos'])].append((nxt[r['sid']], '2:1'))
        if r['op'] == '1:2' and 'labels' not in r:                            # old map: and a 1:2 box's second token
            by.setdefault((r['line'], str(int(r['pos']) + 1)), []).append((r['sid'], '1:2'))
    for tkf in sorted(glob.glob(os.path.join(P, '*_topk.tsv'))):
        name = os.path.basename(tkf)[:-len('_topk.tsv')]
        tk = {r['box']: r for r in rd(tkf)}
        out = []
        for k in sorted(by, key=lambda k: order.get(k, 1e9)):
            v = by[k]
            if k not in order:
                continue
            op = '2:1' if len(v) > 1 else ('1:1' if v[0][1] in ('unsure', 'bad-cut') else v[0][1])
            sid = max((s for s, _ in v), key=lambda s: w[s])
            t = tk.get(sid)
            if t is None:
                continue
            out.append((k[0], k[1], t['k1'], t.get('k2', ''), t.get('k3', ''), sid, op))
        with open(os.path.join(od, f'{name}_bench.tsv'), 'w') as f:
            f.write('line\tpos\tsign\tk2\tk3\tbox\top\n' + ''.join('\t'.join(x) + '\n' for x in out))
    print('->', od)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
