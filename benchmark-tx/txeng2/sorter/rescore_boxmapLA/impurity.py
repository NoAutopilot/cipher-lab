#!/usr/bin/env python3
"""BOXMAP-RESCORE: X6's "measured cluster impurity on no.87 (683 scored 1:1 tiles in 92 clusters): only 77.3% of tiles carry their
cluster's majority value, 31 of 92 clusters are value-pure" (RESULTS.md X6; computed in the X6 job without a committed script).
Rebuilt here: tiles = 1:1 boxes of MAP at scored truth positions of the two no.87 units (tools/tx_sorter_curve.oracle_rows on
labels.tsv, as measured), value = the truth row's `plain`, clusters from atlas/clusters.tsv; with the old map it reproduces 683 / 92
/ 0.773 / 31 exactly. Also splits the tiles into the 10 lines the label-aware map moved and the 16 it left alone (majority taken
over all tiles of the cluster). Reads the benchmark truth (it scores). From the repo root:
  python3 benchmark-tx/txeng2/sorter/rescore_boxmapLA/impurity.py [MAP ...]"""
import csv, collections, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import tx_bench, tx_sorter_curve as C  # noqa: E402
A = os.path.join(ROOT, 'ciphers/nevers-birago-fr3251-1572/atlas'); U = os.path.join(ROOT, 'benchmark-tx/txeng/units')


def tiles(mapf, mask='m'):
    truth = tx_bench.read_tsv(os.path.join(ROOT, 'benchmark-tx/birago1572-no87.truth.tsv'))
    if mask == 'x':
        truth = tx_bench.drop_flagged(truth)
    base = {}
    for u in ('dev_tune', 'eval_heldout'):
        for r in tx_bench.read_tsv(f'{U}/labels_{u}.tsv'):
            base.setdefault(r['line'], []).append((r['pos'], r['sign']))
    for ln in base:
        base[ln].sort(key=lambda x: float(x[0]))
    orc = C.oracle_rows(truth, base)
    cl = {r['id']: r['cluster'] for r in tx_bench.read_tsv(f'{A}/clusters.tsv') if r.get('kind', 'sign') == 'sign'}
    moved = {r['line'] for r in csv.DictReader(open(f'{A}/no87_box_token_labelaware_lines.tsv'), delimiter='\t') if r['moved'] not in ('0', '')}
    out = []
    for r in csv.DictReader(open(mapf), delimiter='\t'):
        k = (r['line'], r['pos'])
        if r['op'] != '1:1' or k not in orc or orc[k]['status'] != 'scored' or r['sid'] not in cl:
            continue
        out.append((cl[r['sid']], orc[k]['plain'], r['line'] in moved))
    return out


def report(mapf, mask='m'):
    t = tiles(mapf, mask)
    vals = collections.defaultdict(list)
    for c, v, _ in t:
        vals[c].append(v)
    maj = {c: collections.Counter(v).most_common(1)[0] for c, v in vals.items()}
    share = sum(n for _, n in maj.values()) / len(t)
    pure = sum(1 for v in vals.values() if len(set(v)) == 1)
    grp = {g: [x for x in t if x[2] == g] for g in (False, True)}
    gs = {('moved lines' if g else 'untouched lines'): (len(x), round(sum(maj[c][0] == v for c, v, _ in x) / len(x), 3)) for g, x in grp.items()}
    print(f'{os.path.relpath(mapf, ROOT)} [{mask}]: {len(t)} tiles in {len(vals)} clusters; majority-value share {share:.3f}; '
          f'value-pure clusters {pure}; by line group {gs}')


if __name__ == '__main__':
    for m in (sys.argv[1:] or [f'{A}/no87_box_token.tsv', f'{A}/no87_box_token_labelaware.tsv']):
        report(os.path.abspath(m))
