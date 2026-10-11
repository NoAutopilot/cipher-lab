#!/usr/bin/env python3
"""BOXMAP-RESCORE (others), 11 Oct 2026, account 3: BIR87-ALIGN's `disagreements.tsv` (committed 4 Oct without its script) rebuilt
by a script, for the old and the label-aware box map.

Rows: every sorter tile with status kept or moved whose box maps 1:1 to a no.87 token (the map MAP) and whose owner pile
(settled_no87.tsv new_sign) differs, as a string, from the committed sign at that token (harvest/ciphertext_<fol>.tsv).
committed_value = the committed sign's value (atlas/name_clusters.value_map: keys/key_1572_clerk.tsv, else the printed sheet;
'?' when unvalued); owner_pile_value = the pile's value under the same map, else the pile's clerk-aligned value from PILES
(the run's piles.tsv, cipher_owner rows); clerk_chunk = the run's own clerk alignment of that sequence (align_cipher_owner.tsv,
plain_chunk at the token); clerk_sides_with
= committed / owner / both / neither by string equality with clerk_chunk. With the old map and the committed piles.tsv this
reproduces the committed disagreements.tsv row for row (checked 11 Oct 2026).

  python3 disagreements.py MAP RUNDIR OUT.tsv      (RUNDIR holds the run's piles.tsv and align_cipher_owner.tsv)
"""
import csv, sys, collections
from pathlib import Path
F = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(F / 'atlas'))
from name_clusters import value_map  # noqa: E402
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))


def main(mapf, rundir, out):
    piles, align = Path(rundir) / 'piles.tsv', Path(rundir) / 'align_cipher_owner.tsv'
    V = value_map()
    bt = {}
    for r in rd(mapf):
        bt.setdefault(r['sid'], r)
    pv = {r['pile']: r['value'] for r in rd(piles) if r['seq'] == 'cipher_owner'}
    seed = {r['sid']: r['seed'] for r in rd(F / 'sorter/no87/seed.tsv')}
    tok, idx = {}, {}
    for fol in ('f178r', 'f178v', 'f179r'):
        for k, t in enumerate(rd(F / f'harvest/ciphertext_{fol}.tsv')):
            tok[(t['line'], t['pos'])] = t['sign']; idx[(t['line'], t['pos'])] = (fol, k)
    al = {(r['cipher_line'], int(r['idx'])): r['plain_chunk'] for r in rd(align)}
    rows = []
    for r in rd(F / 'sorter/no87/owner-sort-2026-10-04/settled_no87.tsv'):
        b = bt.get(r['sid'])
        if not b or b['op'] != '1:1' or r['status'] not in ('kept', 'moved'):
            continue
        k = (b['line'], b['pos']); cs = tok[k]
        if r['new_sign'] == cs:
            continue
        cv = V.get(cs, '?'); ov = V.get(r['new_sign'], pv.get(r['new_sign'], '?'))
        ch = al.get(idx[k], '')
        side = {(True, True): 'both', (True, False): 'committed', (False, True): 'owner', (False, False): 'neither'}[(cv == ch, ov == ch)]
        rows.append(dict(sid=r['sid'], status=r['status'], committed_sign=cs, seed_pile=seed.get(r['sid'], ''), owner_pile=r['new_sign'],
                         committed_value=cv, owner_pile_value=ov, clerk_chunk=ch, clerk_sides_with=side, line=b['line'], pos=b['pos']))
    cols = ['sid', 'status', 'committed_sign', 'seed_pile', 'owner_pile', 'committed_value', 'owner_pile_value', 'clerk_chunk', 'clerk_sides_with']
    with open(out, 'w') as f:
        f.write('\t'.join(cols) + '\n' + ''.join('\t'.join(r[c] for c in cols) + '\n' for r in rows))
    for st in ('kept', 'moved'):
        c = collections.Counter(r['clerk_sides_with'] for r in rows if r['status'] == st)
        print(f"{st}: {sum(c.values())} tokens; clerk sides with committed {c['committed']}, owner pile {c['owner']}, both {c['both']}, neither {c['neither']}")
    return rows


if __name__ == '__main__':
    main(*sys.argv[1:4])
