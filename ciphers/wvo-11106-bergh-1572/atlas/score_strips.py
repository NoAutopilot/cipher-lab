#!/usr/bin/env python3
"""BERGH-STRIP: merge the two blind strip passes per box, score the PREREG-BERGH-STRIP.md gate, write atlas/box_sign.tsv.

  python3 atlas/score_strips.py atlas/strips/passA.tsv atlas/strips/passB.tsv [--check]

Gate rule (pre-registered): hit = A and B agree (after dropping a trailing '?') and the label is in the accepted list; a split is a
miss. FRAG:<x> and OTHERLINE both count as FRAG for the gate. --check exits 1 if atlas/box_sign.tsv differs from what it would write.
"""
import csv, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ACCEPT = {'L15_01_013': {'3'}, 'L11_01_020': {'FRAG'}, 'L12_01_044': {'r'}, 'L20_01_006': {'4'}, 'L02_01_038': {'FRAG'},
          'L06_01_020': {'FRAG'}, 'L06_01_004': {'y', 'yx'}, 'L20_01_036': {'b'}, 'L06_01_026': {'7'}, 'L07_01_009': {'FRAG'},
          'L18_01_018': {'r', 'yx'}, 'L22_01_007': {'B'}, 'L10_01_037': {'s', '5'}, 'L14_01_018': {'e'},
          'L18_01_007': {'FRAG'}, 'L15_01_031': {'3'}, 'L21_01_015': {'s', '5'}, 'L11_01_019': {'FRAG'}, 'L08_01_026': {'u', 'n'}}
GATE_STRIP = {sid: f'gate_{i:02d}' for i, sid in enumerate(ACCEPT, 1)}


def norm(l):
    l = l.strip().rstrip('?')
    return 'FRAG' if l.startswith('FRAG') or l == 'OTHERLINE' else l


def load(p):
    with open(p) as f:
        return {(r['strip'], r['num']): r for r in csv.DictReader(f, delimiter='\t')}


def main():
    a, b = load(sys.argv[1]), load(sys.argv[2]); check = '--check' in sys.argv
    with open(os.path.join(HERE, 'strips', 'key.tsv')) as f:
        key = list(csv.DictReader(f, delimiter='\t'))
    with open(os.path.join(HERE, 'boxmap.tsv')) as f:
        old = {r['sid']: r['label'] for r in csv.DictReader(f, delimiter='\t')}
    rows, agree, n, per = [], 0, 0, {}
    for k in key:
        ra, rb = a.get((k['strip'], k['num'])), b.get((k['strip'], k['num']))
        la, lb = (ra or {}).get('label', ''), (rb or {}).get('label', '')
        same = bool(la) and norm(la) == norm(lb) and (la.strip('?') == lb.strip('?') or norm(la) == 'FRAG')
        n += 1; agree += same
        lab = norm(la) if same else ''
        rows.append([k['sid'], k['strip'], k['num'], la, lb, lab, 'agreed' if same else 'split', old.get(k['sid'], '')])
        if GATE_STRIP.get(k['sid']) == k['strip']:
            per[k['sid']] = (la, lb, lab, lab in ACCEPT[k['sid']] if same else False)
    hits = sum(v[3] for v in per.values())
    out = 'sid\tstrip\tnum\tpassA\tpassB\tlabel\tstatus\told_mapped\n' + ''.join('\t'.join(r) + '\n' for r in rows)
    path = os.path.join(HERE, 'box_sign.tsv')
    if check:
        ok = os.path.exists(path) and open(path).read() == out
        print('box_sign.tsv', 'current' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(path, 'w').write(out)
    for sid in ACCEPT:
        la, lb, lab, hit = per.get(sid, ('', '', '', False))
        print(f'{sid}\tA={la}\tB={lb}\taccept={"/".join(sorted(ACCEPT[sid]))}\t{"HIT" if hit else "miss"}')
    print(f'gate: {hits}/19 (PASS needs >= 17); A/B agreement on all {n} numbered boxes: {agree}/{n} = {agree / n:.3f}')


if __name__ == '__main__':
    main()
