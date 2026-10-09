#!/usr/bin/env python3
"""X20 (TXE2-SORT, LANE TX-ENGINEER-2, 9 Oct 2026; PREREG benchmark-tx/PREREG-txeng2-1.md): the owner's 4 Oct 2026
sorter decisions applied on top of L (benchmark-tx/outputs/birago1572-no87/labels.tsv) for every no.87 line.

    python3 benchmark-tx/txeng2/sorter/x20_owner.py [--check]

Two sources of owner decisions, both from 4 Oct 2026, kept apart so each can be scored on its own:
  A family sort (sorter/owner-sort-2026-10-04: labels_as_published.tsv -> settled_labels.tsv, then corrections.tsv on top;
    488 tiles of f.117 / f.144r / f.168, none on no.87). tools/sign_sorter_apply.py --atlas-labels writes a cluster
    decision only from a sorter `clusters` collection, which this save does not have (summary.json: no cluster docs),
    and per-tile overrides only for the owner's own tiles, so through the tool alone no no.87 tile changes. The
    cluster-level reuse TRANSCRIPTION.md asks for is made here explicitly: owner tiles are placed in atlas clusters
    through sorter/no87/owner_map.tsv (one-to-one boxes only, dup 0); for an atlas cluster c and a starting pile family
    F, when >= 2 of the owner's tiles of c started in F and >= 2/3 of them ended in one other family C, the decision is
    "c: F -> C", and every no.87 1:1 tile of cluster c whose L sign is F becomes C. Aside, bad-cut and UNPLACED tiles
    carry no decision.
  B no.87 sort (sorter/no87/owner-sort-2026-10-04/settled_no87.tsv): tile-level, only `moved` rows are owner decisions
    (`kept` rows keep a computer seed); the tile's L sign becomes the final pile's family when that is an atlas T code.
A pile's family is its name without the owner's split suffix (T60-e -> T60, T24-b -> T24): the benchmark scores atlas
codes, and a split pile is a sub-variant the key has not valued. Piles outside the T codes (X_NEW-l, NOT-LETTER) move
nothing. Writes benchmark-tx/outputs/birago1572-no87/passX20_owner.tsv (A then B; B wins where both touch a tile),
passX20a_family.tsv, passX20b_no87sort.tsv and benchmark-tx/txeng2/sorter/x20_changes.tsv. --check exits 1 if a
committed file differs from what this run would write (CLAUDE.md rule 7). The truth file is never read here.
"""
import csv, os, re, sys
from collections import Counter, defaultdict

R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
F = os.path.join(R, 'ciphers/nevers-birago-fr3251-1572')
OUT = os.path.join(R, 'benchmark-tx/outputs/birago1572-no87')


def tsv(p):
    with open(p, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def fam(p):
    p = (p or '').strip()
    m = re.match(r'^(T\d+)(-[a-z])?$', p)
    return m.group(1) if m else None


def main():
    check = '--check' in sys.argv
    L = tsv(os.path.join(OUT, 'labels.tsv'))
    cl = {r['id']: r['cluster'] for r in tsv(os.path.join(F, 'atlas/clusters.tsv')) if r['kind'] == 'sign'}
    box = {}
    for r in tsv(os.path.join(F, 'atlas/no87_box_token.tsv')):
        if r['op'] == '1:1':
            box[r['sid']] = (r['line'], r['pos'])
    pos_cluster = {v: cl[s] for s, v in box.items() if s in cl}
    lsign = {(r['line'], r['pos']): r['sign'] for r in L}

    # A: family sort -> cluster decisions
    S = os.path.join(F, 'sorter/owner-sort-2026-10-04')
    start = {r['sid']: r['sign'] for r in tsv(os.path.join(S, 'labels_as_published.tsv'))}
    final = {r['sid']: (r['new_sign'], r['status']) for r in tsv(os.path.join(S, 'settled_labels.tsv'))}
    for r in tsv(os.path.join(S, 'corrections.tsv')):
        final[r['owner_sid']] = (r['to_pile'], 'corrected')
    omap = {r['sid']: r['box'] for r in tsv(os.path.join(F, 'sorter/no87/owner_map.tsv')) if r['box'] and r['dup'] == '0'}
    per = defaultdict(list)
    n_mapped = 0
    for sid, (to, st) in final.items():
        if st in ('aside', 'bad-cut') or to in ('UNPLACED', '') or sid not in omap or omap[sid] not in cl:
            continue
        n_mapped += 1
        per[(cl[omap[sid]], fam(start.get(sid)))].append(fam(to))
    dec = {}
    for (c, f0), tos in per.items():
        if f0 is None or len(tos) < 2:
            continue
        top, n = Counter(tos).most_common(1)[0]
        if top and top != f0 and n * 3 >= 2 * len(tos):
            dec[(c, f0)] = (top, n, len(tos))
    A = {}
    for k, c in pos_cluster.items():
        d = dec.get((c, lsign.get(k)))
        if d:
            A[k] = d[0]
    # B: no.87 sort, moved rows
    B = {}
    for r in tsv(os.path.join(F, 'sorter/no87/owner-sort-2026-10-04/settled_no87.tsv')):
        if r['status'] != 'moved' or r['sid'] not in box:
            continue
        f1 = fam(r['new_sign'])
        k = box[r['sid']]
        if f1 and lsign.get(k) and f1 != lsign[k]:
            B[k] = f1

    def write(name, ch):
        p = os.path.join(OUT, name)
        txt = '# X20 %s (benchmark-tx/txeng2/sorter/x20_owner.py): L with the owner 4 Oct 2026 decisions applied; %d positions changed\n' % (name, len(ch))
        txt += 'line\tpos\tsign\n' + ''.join('%s\t%s\t%s\n' % (r['line'], r['pos'], ch.get((r['line'], r['pos']), r['sign'])) for r in L)
        if check:
            return open(p).read() == txt
        open(p, 'w').write(txt)
        return True
    allc = dict(A); allc.update(B)
    ok = all([write('passX20a_family.tsv', A), write('passX20b_no87sort.tsv', B), write('passX20_owner.tsv', allc)])
    rows = ['source\tline\tpos\tL\tnew\tdecision']
    for k, v in sorted(A.items()):
        c = pos_cluster[k]; t, n, m = dec[(c, lsign[k])]
        rows.append('A\t%s\t%s\t%s\t%s\tcluster %s: %s->%s (%d of %d owner tiles)' % (k[0], k[1], lsign[k], v, c, lsign[k], t, n, m))
    for k, v in sorted(B.items()):
        rows.append('B\t%s\t%s\t%s\t%s\tno.87 sort moved' % (k[0], k[1], lsign[k], v))
    ctxt = '\n'.join(rows) + '\n'
    cp = os.path.join(R, 'benchmark-tx/txeng2/sorter/x20_changes.tsv')
    if check:
        ok = ok and open(cp).read() == ctxt
        print('x20_owner --check:', 'current' if ok else 'STALE')
        return 0 if ok else 1
    open(cp, 'w').write(ctxt)
    print('owner family tiles mapped to atlas clusters: %d; cluster decisions: %d %s' % (n_mapped, len(dec), sorted(dec.items())))
    print('no.87 positions changed: A family %d, B no.87 sort %d, combined %d' % (len(A), len(B), len(allc)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
