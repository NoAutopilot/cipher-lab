#!/usr/bin/env python3
"""bMAL28B: apply manual_witness_settled.tsv (rows settled by directly reading the aligned f.30 line crop and
checking which of f.28's two blind-pass candidates it confirms) to recon_0028_all/ciphertext_draft.tsv.

f.30's line numbering runs ahead of f.28's own line breaks by a growing lag (confirmed: f.30 L16's crop covers
f.28 L15's tail plus L16; f.30 L17's crop covers the rest of f.28 L16), so each row here names which f.30 crop was
read, not "same line number" -- there is no fixed offset, each match was confirmed by exact agreement on a run of
several neighbouring already-H tokens before trusting the crop for a disagreement row.
"""
import csv, sys

def load_tsv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def main():
    settled = {}
    for fn in ('manual_witness_settled.tsv', 'manual_witness_settled2.tsv', 'manual_witness_settled3.tsv',
               'manual_witness_settled4.tsv', 'manual_witness_settled5.tsv', 'manual_witness_settled6.tsv'):
        for row in load_tsv(fn):
            settled[(row['line'], row['col'])] = row

    draft_path = 'recon_0028_all/ciphertext_draft.tsv'
    draft = load_tsv(draft_path)
    fieldnames = list(draft[0].keys())
    n = 0
    for row in draft:
        key = (row['line'], row['position'])
        if key in settled:
            s = settled[key]
            row['confidence'] = 'H'
            row['why'] = 'f30_read'
            row['alt'] = s['source']
            n += 1
    print(f"applied {n} of {len(settled)} rows")
    with open(draft_path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
        w.writeheader()
        w.writerows(draft)

if __name__ == '__main__':
    sys.exit(main())
