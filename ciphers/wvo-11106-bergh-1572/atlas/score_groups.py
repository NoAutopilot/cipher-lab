#!/usr/bin/env python3
"""BERGH-GRP: score two blind sign-GROUP passes on the 19 gate windows against PREREG-BERGH-GRP.md; write atlas/group_sign.tsv.

  python3 atlas/score_groups.py atlas/strips_grp/passA.tsv atlas/strips_grp/passB.tsv [--check]

Pass rows: strip, boxes ('3+4'), labels ('y' | 'd 4' | 'FRAG' | 'OTHERLINE'), note. Gate rule (pre-registered): a sign-truth gate box is
a hit iff both passes give its group exactly one sign, the same after dropping '?', in the accepted set; a fragment-truth box is a hit
iff both give FRAG/OTHERLINE, or both put it in a group of >= 2 boxes labelled with one accepted parent sign. Missing = miss.
atlas/group_sign.tsv (one row per numbered box: the group and label of each pass, agreed or split) is written only on PASS, or with
--force for inspection; --check exits 1 if it is stale.
"""
import csv, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SIGN = {'L15_01_013': {'3'}, 'L12_01_044': {'r'}, 'L20_01_006': {'4'}, 'L06_01_004': {'y', 'yx'}, 'L20_01_036': {'b'},
        'L06_01_026': {'7'}, 'L18_01_018': {'r', 'yx'}, 'L22_01_007': {'B'}, 'L10_01_037': {'s', '5'}, 'L14_01_018': {'e'},
        'L15_01_031': {'3'}, 'L21_01_015': {'s', '5'}, 'L08_01_026': {'u', 'n'}}
FRAG = {'L11_01_020': {'m'}, 'L02_01_038': set(), 'L06_01_020': {'m'}, 'L07_01_009': set(), 'L18_01_007': {'u', 'n'},
        'L11_01_019': {'m', 'f', 'b'}}
ORDER = ['L15_01_013', 'L11_01_020', 'L12_01_044', 'L20_01_006', 'L02_01_038', 'L06_01_020', 'L06_01_004', 'L20_01_036',
         'L06_01_026', 'L07_01_009', 'L18_01_018', 'L22_01_007', 'L10_01_037', 'L14_01_018', 'L18_01_007', 'L15_01_031',
         'L21_01_015', 'L11_01_019', 'L08_01_026']


def norm(lab):
    t = [x.rstrip('?') for x in lab.split()]
    return tuple('FRAG' if x in ('FRAG', 'OTHERLINE') or x.startswith('FRAG') else x for x in t if x)


def load(p):
    """(strip, num) -> (frozenset of nums in its group, normalized labels, raw label)."""
    m = {}
    with open(p) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            nums = frozenset(x.strip() for x in r['boxes'].split('+') if x.strip())
            for n in nums:
                m[(r['strip'], n)] = (nums, norm(r['labels']), r['labels'].strip())
    return m


def hit(sid, g):
    if g is None:
        return False
    nums, lab = g[0], g[1]
    if sid in SIGN:
        return len(lab) == 1 and lab[0] in SIGN[sid]
    if lab and all(x == 'FRAG' for x in lab):
        return True
    return len(nums) >= 2 and len(lab) == 1 and lab[0] in FRAG[sid]


def main():
    args = [x for x in sys.argv[1:] if not x.startswith('--')]
    A, B = load(args[0]), load(args[1])
    with open(os.path.join(HERE, 'strips_grp', 'key.tsv')) as f:
        key = list(csv.DictReader(f, delimiter='\t'))
    gate = {f'gate_{i:02d}': sid for i, sid in enumerate(ORDER, 1)}
    rows, agree, multi, nag = [], 0, 0, 0
    res = {}
    for k in key:
        s, n, sid = k['strip'], k['num'], k['sid']
        a, b = A.get((s, n)), B.get((s, n))
        same = a is not None and b is not None and a[0] == b[0] and a[1] == b[1]
        agree += same
        if same:
            multi += len(a[0]) >= 2
        fa = '+'.join(sorted(a[0], key=int)) if a else ''
        fb = '+'.join(sorted(b[0], key=int)) if b else ''
        rows.append([sid, s, n, fa, a[2] if a else '', fb, b[2] if b else '', ' '.join(a[1]) if same else '',
                     'agreed' if same else 'split'])
        if gate.get(s) == sid:
            ha, hb = hit(sid, a), hit(sid, b)
            lab_same = a is not None and b is not None and a[1] == b[1]
            res[sid] = (s, n, fa, a[2] if a else '-', fb, b[2] if b else '-', ha and hb and lab_same, a is not None and b is not None and a[0] == b[0])
    nk = len(key)
    out = 'sid\tstrip\tnum\tgroupA\tlabelA\tgroupB\tlabelB\tagreed_label\tstatus\n' + ''.join('\t'.join(r) + '\n' for r in rows)
    path = os.path.join(HERE, 'group_sign.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path).read() == out
        print('group_sign.tsv', 'current' if ok else 'STALE'); sys.exit(0 if ok else 1)
    hits = sum(v[6] for v in res.values())
    for sid in ORDER:
        s, n, fa, la, fb, lb, h, gm = res.get(sid, ('', '', '', '-', '', '-', False, False))
        print(f'{s}/{n}\t{sid}\tA={fa}:{la}\tB={fb}:{lb}\tgroups {"same" if gm else "differ"}\t{"HIT" if h else "miss"}')
    print(f'gate: {hits}/19 (PASS needs >= 17); A/B agreement (same group and labels) on all {nk} numbered boxes: {agree}/{nk} = '
          f'{agree / nk:.3f}; agreed boxes in groups of >= 2: {multi}/{agree}')
    if hits >= 17 or '--force' in sys.argv:
        open(path, 'w').write(out); print('wrote', path)


if __name__ == '__main__':
    main()
