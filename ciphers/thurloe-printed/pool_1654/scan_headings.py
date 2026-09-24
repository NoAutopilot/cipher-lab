#!/usr/bin/env python3
"""One-off scan: find OCR lines that look like cipher-group runs (same detector
as tools/thurloe_extract.py) across vols 2 and 3, cluster into runs, and report
the nearest preceding heading line ("X to secretary Thurloe." etc.) for each
cluster. Used to check whether other letters in vols 2-3 share the P4/P5/P6/P7
inline-numeral style beyond the 23 rows already in index.tsv. Read-only report,
writes nothing; output was pasted into NOTES.md section 12 by hand.
"""
import re
import sys

NUM = re.compile(r'^\d{1,4}[.,;:]?$')
HEADING = re.compile(
    r'^([A-Z][a-zA-Z.]*\s+)?[A-Z][a-zA-Z.\'’]*(\s+[A-Za-z.\'’]+){1,6}\s+to\s+'
    r'(fecretary|fecrefary|the\s+protedtor|the\s+proteSior)\b', re.IGNORECASE)


def is_cipher_line(line):
    tk = line.split()
    if len(tk) < 4:
        return False
    return sum(1 for t in tk if NUM.match(t)) / len(tk) >= 0.7


def scan(path, label):
    with open(path, encoding='utf-8', errors='ignore') as f:
        lines = f.read().split('\n')
    headings = []
    for i, l in enumerate(lines):
        if HEADING.search(l.strip()):
            headings.append((i + 1, l.strip()))
    runs = []
    cur = None
    for i, l in enumerate(lines):
        if is_cipher_line(l.strip()):
            if cur is None:
                cur = [i + 1, i + 1]
            else:
                cur[1] = i + 1
        else:
            if cur is not None:
                runs.append(tuple(cur))
                cur = None
    if cur is not None:
        runs.append(tuple(cur))
    # merge runs within 30 lines of each other (allow for interleaved plain lines)
    merged = []
    for r in runs:
        if merged and r[0] - merged[-1][1] <= 30:
            merged[-1] = (merged[-1][0], r[1])
        else:
            merged.append(r)
    print(f'=== {label}: {len(merged)} cipher-line clusters (merged within 30 lines) ===')
    for lo, hi in merged:
        # nearest heading at or before lo
        h = None
        for hl, htext in headings:
            if hl <= lo:
                h = (hl, htext)
            else:
                break
        n_lines = sum(1 for i in range(lo - 1, hi) if is_cipher_line(lines[i].strip()))
        print(f'{label}\t{lo}-{hi}\tcipher_lines={n_lines}\theading_at={h[0] if h else "?"}\t{h[1] if h else "?"}')


if __name__ == '__main__':
    for path, label in [
        ('sources/ia-fulltext/collectionofstat02thur_djvu.txt', 'vol2'),
        ('sources/ia-fulltext/collectionofstat03thur_djvu.txt', 'vol3'),
    ]:
        scan(path, label)
