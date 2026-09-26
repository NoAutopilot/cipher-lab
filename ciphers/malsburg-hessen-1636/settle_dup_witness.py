#!/usr/bin/env python3
"""bMAL28B: settle f.28 L05-14 disagreements against f.30 using ALREADY-COLLECTED data, no new image reads.

dup_align.tsv (bMALDUP, whole-leaf NW alignment of f.28's raw group sequence against f.30's) turns out, once its
raw z/i spellings are normalized by the same rule bMALG's glyph_map.tsv applies (length<=3, digits+i/z only ->
i='1', z='2'), to reproduce recon_0030/ciphertext_draft.tsv's sign sequence exactly (0 mismatches over 464
tokens) at the positions where both sides are non-blank. So dup_align.tsv's idx order gives an exact, already-
graded f.30 reading for f.28's L05-14 tokens (positions confirmed against recon_0028_full/ciphertext_draft.tsv's
own L05-14 sequence: 0 mismatches after normalization over 497 tokens). This is a second, independent leaf's
own already-reconciled (two-blind-pass) reading, not a new observation -- exactly the "both leaves agree" bar
CLAUDE.md rule 3 and this job's brief set, at zero additional cost.

A disagreement row is promoted to H only when: f.30's OWN reconciled confidence at the aligned position is H
(both of f.30's blind passes agreed -- an uncertain f.30 reading is not corroboration), AND that value matches
one of f.28's two candidate readings (A or B) at the disagreement row, after normalization.

Usage: python3 settle_dup_witness.py [--apply]  (dry-run without --apply; writes the update with it)
"""
import argparse, csv, re, sys

def norm(t):
    if t and len(t) <= 3 and re.fullmatch(r'[0-9iz]+', t):
        return t.replace('i', '1').replace('z', '2')
    return t

def load_tsv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    a = ap.parse_args()

    dup = load_tsv('dup_align.tsv')
    f28rows = [r for r in load_tsv('recon_0028_full/ciphertext_draft.tsv') if int(r['line']) <= 14]
    r30 = load_tsv('recon_0030/ciphertext_draft.tsv')

    i28 = i30 = 0
    pair_map = {}
    for d in dup:
        f28row = f30row = None
        if d['f28_group'] != '':
            f28row = f28rows[i28]; i28 += 1
        if d['f30_group'] != '':
            f30row = r30[i30]; i30 += 1
        if f28row is not None and f30row is not None:
            pair_map[(f28row['line'], f28row['position'])] = f30row
    assert i28 == len(f28rows) and i30 == len(r30), (i28, len(f28rows), i30, len(r30))

    dis = load_tsv('recon_0028_full/disagreements.tsv')
    settled = {}
    for row in dis:
        if int(row['line']) > 14:
            continue
        f30row = pair_map.get((row['line'], row['col']))
        if f30row is None:
            continue
        f30val, f30conf = f30row['sign'], f30row['confidence']
        cands = {norm(v) for v in (row['A'], row['B']) if v != '-'}
        if f30conf == 'H' and f30val in cands:
            settled[(row['line'], row['col'])] = f30val

    print(f"settling {len(settled)} L05-14 rows to H via f.30 dup_align witness (H-graded, value-matched)")

    if not a.apply:
        print("dry run; pass --apply to write")
        return

    draft_path = 'recon_0028_full/ciphertext_draft.tsv'
    draft = load_tsv(draft_path)
    fieldnames = list(draft[0].keys())
    n_changed = 0
    for row in draft:
        key = (row['line'], row['position'])
        if key in settled:
            row['confidence'] = 'H'
            row['why'] = 'dup_witness'
            row['alt'] = f"f30={settled[key]}"
            n_changed += 1
    assert n_changed == len(settled)
    with open(draft_path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
        w.writeheader()
        w.writerows(draft)

    with open('recon_0028_full/dup_witness_settled.tsv', 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(['line', 'col', 'value', 'source'])
        for (line, col), val in sorted(settled.items(), key=lambda x: (int(x[0][0]), int(x[0][1]))):
            w.writerow([line, col, val, 'f30_dup_align_H'])

    print(f"wrote {n_changed} updated rows to {draft_path}; log at recon_0028_full/dup_witness_settled.tsv")

if __name__ == '__main__':
    sys.exit(main())
