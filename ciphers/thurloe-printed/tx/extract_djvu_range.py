#!/usr/bin/env python3
"""Print a line range from a cached gzipped Thurloe djvu text, for citation. Not a reading --
a lookup helper so the exact excerpts quoted in NOTES.md 'LANE TX residue' can be regenerated
by anyone from the already-committed sources/ia-fulltext/thurloe-gz/ cache, no network fetch.

Usage: python3 extract_djvu_range.py <identifier> <start_line> <end_line>
  identifier: collectionofstat02thur | collectionofstat03thur | collectionofstat05thur
"""
import gzip
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
GZ_DIR = os.path.join(REPO_ROOT, 'sources', 'ia-fulltext', 'thurloe-gz')


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    ident, start, end = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    path = os.path.join(GZ_DIR, f'{ident}_djvu.txt.gz')
    with gzip.open(path, 'rt', errors='replace') as f:
        for i, line in enumerate(f, start=1):
            if start <= i <= end:
                print(f'{i}\t{line.rstrip(chr(10))}')
            if i > end:
                break


if __name__ == '__main__':
    main()
