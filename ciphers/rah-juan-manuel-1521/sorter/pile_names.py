#!/usr/bin/env python3
"""RUN1-SEG: sorter labels for the Juan Manuel sheet. Every pile is a --cursive shape cluster; a pile is NAMED only where
pile_names_byeye.tsv names it after one of JM-ALPHA's six C signs (alphabet.tsv grade C, value from the clerk's f.197
decipherment) -- the pile-to-sign link is a by-eye look at the exemplar sheet, so the name is a proposal for the person's
sort, not a settled label. Everything else stays "pile NN". looks_like notes become the focus questions.

  python3 ciphers/rah-juan-manuel-1521/sorter/pile_names.py --atlas DIR --out DIR2 [--focus-per 3]
Writes DIR2/labels.tsv (sid, sign, family, cluster) and DIR2/focus.tsv (sid, question; no header, as sign_sorter --focus reads it).
(A positional transfer of the passes' labels onto boxes was tried first and dropped: only 2 lines had pass A, pass B and
box counts all equal, 24 boxes, and the widths showed even those were not aligned.)
"""
import argparse, csv, os

H = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(H)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--atlas', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--focus-per', type=int, default=3)
    a = ap.parse_args()
    C = {r['sign'] for r in csv.DictReader(open(f'{T}/alphabet.tsv'), delimiter='\t') if r['grade'] == 'C'}
    by = {r['cluster']: r for r in csv.DictReader(open(f'{H}/pile_names_byeye.tsv'), delimiter='\t')}
    for r in by.values():
        assert not r['name'] or r['name'].split('=')[0] in C, r
    cl = [r for r in csv.DictReader(open(f'{a.atlas}/clusters.tsv'), delimiter='\t') if r['kind'] == 'sign']
    os.makedirs(a.out, exist_ok=True)
    with open(f'{a.out}/labels.tsv', 'w') as f:
        f.write('sid\tsign\tfamily\tcluster\n')
        for r in cl:
            nm = by.get(r['cluster'], {}).get('name', '')
            f.write(f"{r['id']}\t{nm or 'pile ' + r['cluster'].zfill(2)}\t{'named (C, by eye)' if nm else 'unnamed'}\t{r['cluster']}\n")
    n = 0
    with open(f'{a.out}/focus.tsv', 'w') as f:
        for c, b in by.items():
            q = b['looks_like_note']
            if not q or b['name'] or 'code word' in q:
                continue
            mem = sorted((r for r in cl if r['cluster'] == c), key=lambda r: float(r['dist']))
            for r in mem[:a.focus_per]:
                f.write(f"{r['id']}\tpile {c.zfill(2)}: {q} -- which sign is this tile?\n"); n += 1
    print(f"labels {len(cl)}; named piles {sum(1 for b in by.values() if b['name'])}; focus tiles {n}")


if __name__ == '__main__':
    main()
