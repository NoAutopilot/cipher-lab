#!/usr/bin/env python3
"""BOXMAP-RESCORE (others), 11 Oct 2026, account 3: label-free sensitivity map for rescoring consumers that score ATLAS labels.

The label-aware map (atlas/no87_box_token_labelaware.tsv) is steered partly by the atlas classify top-3 (every no.87 page held
out). A consumer that scores atlas labels at the mapped position is then partly scored at positions its own family of labels
helped choose (each box's own label is guarded by leave-one-out, its neighbours' are not). This writes the one map that uses
no label at all -- the same width DP (lam 0) plus only the owner's sorter statuses (not-letter skipped, bad-cut never 1:1) --
so a rescore can be bracketed: old map (width only) / status-only (this) / label-aware (committed). A second variant,
sorter-only, is steered by the statuses and the sorter pile labels alone (seed pile family, or the owner's pile where he moved
the tile; no atlas top-k), as no87_map.py --label-aware builds them, with lam, neutral and leave-one-out as committed.
Status-only moves L06 alone (statuses exist only for sorter tiles); sorter-only reaches the lines where sorter tiles sit.

  python3 ciphers/nevers-birago-fr3251-1572/atlas/rescore_boxmapLA/variants.py OUT_DIR
  -> OUT_DIR/statusonly_map.tsv, OUT_DIR/sorteronly_map.tsv (new-map columns) and OUT_DIR/compat_{statusonly,sorteronly}.tsv
     (old columns with truth, via no87_map.compat: they read align_real.tsv, keep them outside the repository)
Reads no truth file. No image, no network.
"""
import os, sys, collections
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, A)
import no87_map as N


def main(od):
    sys.path.insert(0, os.path.join(N.ROOT, 'tools'))
    import box_token_align as BA
    os.makedirs(od, exist_ok=True)
    L = [r for r in BA.rd(os.path.join(N.ROOT, 'benchmark-tx/outputs/birago1572-no87/labels.tsv')) if r['line'] in N.LINES]
    alt, idx, csign = [], {}, {}
    for fol in ('f178v', 'f179r'):
        for k, t in enumerate(BA.rd(os.path.join(N.H, f'ciphertext_{fol}.tsv'))):
            alt.append(t); idx[(t['line'], t['pos'])] = k; csign[(t['line'], t['pos'])] = t['sign']
    settled = BA.rd(os.path.join(N.SORT, 'owner-sort-2026-10-04', 'settled_no87.tsv'))
    status = {r['sid']: BA.norm_status(r['status']) for r in settled}
    seed = {r['sid']: r for r in BA.rd(os.path.join(N.SORT, 'seed.tsv'))}
    lab = collections.defaultdict(dict)
    for r in settled:
        f1 = N.fam(r['new_sign']) if r['status'] == 'moved' else N.fam(seed.get(r['sid'], {}).get('seed'))
        if f1:
            lab[r['sid']][f1] = 1.0
    old = BA.read_old(os.path.join(A, 'no87_box_token.tsv'))
    for name, labels, lam, loo in (('statusonly', {}, 0.0, False), ('sorteronly', lab, BA.LAM, True)):
        rows, per = BA.build_map(N.S, L, labels, status, N.LINES, lam, BA.NEUTRAL, loo, alt)
        write(od, name, rows, per, old, idx, csign, BA)


def write(od, name, rows, per, old, idx, csign, BA):
    for r in rows:
        k = (r['line'], str(r['pos']))
        r.update(fol=r['page'], idx=idx.get(k, ''), sign=csign.get(k, ''), split='tune' if r['line'] in N.TUNE else 'heldout',
                 old_pos=old[r['sid']][1] if r['sid'] in old else '')
    p = os.path.join(od, f'{name}_map.tsv')
    with open(p, 'w') as f:
        f.write('\t'.join(N.NEW_COLS) + '\n')
        for r in rows: f.write('\t'.join(str(r.get(c, '')) for c in N.NEW_COLS) + '\n')
    lines = BA.line_summary(rows, per, old)
    N.compat(os.path.join(od, f'compat_{name}.tsv'), src=p)
    print(name, 'map ->', p, dict(collections.Counter(r['op'] for r in rows)),
          '| tiles moved vs old', sum(x['moved'] for x in lines), '| lines moved',
          [x['line'] for x in lines if x['moved']])
    return p


if __name__ == '__main__':
    main(sys.argv[1])
