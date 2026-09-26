#!/usr/bin/env python3
"""Diff ciphertext_ms.txt (this worker's independent manuscript re-transcription, pages 1-3 of the
20 Feb 1808 letter) against ciphertext.txt (Bourdeau's transcription) on the NUMERIC groups only,
ignoring shorthand marks (the two use different mark-counting conventions -- see ciphertext_ms.txt's
own header). Prints substitutions/insertions/deletions and the units-digit distribution of both,
restricted to the range ciphertext_ms.txt actually covers (its first 332 of ciphertext.txt's 369
groups -- frame 0033 was not fetched, see NOTES.md).

python3 tr/diff_ms_vs_ciphertext.py
"""
import re, difflib, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.dirname(HERE)


def nums_from(path):
    out = []
    with open(path) as f:
        for line in f:
            if line.startswith('#'):
                continue
            for tok in line.split():
                if re.fullmatch(r'\d+', tok):
                    out.append(tok)
                else:
                    m = re.fullmatch(r'(\d+)\?', tok)
                    if m:
                        out.append(m.group(1))
    return out


def units_dist(nums, min_value=0):
    c = Counter(int(n) % 10 for n in nums if int(n) >= min_value)
    return {d: c.get(d, 0) for d in range(10)}


def main():
    ms = nums_from(os.path.join(TARGET, 'ciphertext_ms.txt'))
    ct = nums_from(os.path.join(TARGET, 'ciphertext.txt'))
    covered_ct = ct[:len(ms) + 20]  # ms should align within the first ~332 of 369; slack for indels

    sm = difflib.SequenceMatcher(None, ms, ct, autojunk=False)
    last_a = last_b = 0
    subs = ins = dele = 0
    diffs = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            last_a, last_b = i2, j2
            continue
        if tag == 'replace':
            n = max(i2 - i1, j2 - j1)
            subs += n
            for k in range(n):
                av = ms[i1 + k] if i1 + k < i2 else None
                bv = ct[j1 + k] if j1 + k < j2 else None
                diffs.append(('replace', av, bv))
        elif tag == 'insert':
            ins += j2 - j1
            for k in range(j1, j2):
                diffs.append(('in_ciphertext_not_ms', None, ct[k]))
        elif tag == 'delete':
            dele += i2 - i1
            for k in range(i1, i2):
                diffs.append(('in_ms_not_ciphertext', ms[k], None))

    print(f"ms numeric tokens: {len(ms)}  ciphertext.txt numeric tokens: {len(ct)}")
    print(f"ms's own reading covers ciphertext.txt positions 1-{last_b} "
          f"({len(ct) - last_b} groups at the end are NOT covered by the fetched frames)")
    print(f"within covered range: substitutions={subs} in_ciphertext_not_ms={ins} "
          f"in_ms_not_ciphertext={dele}  match_ratio={sm.ratio():.4f}")
    print()
    for d in diffs:
        print(d)
    print()
    print("units-digit distribution, ms (all values):        ", units_dist(ms))
    print("units-digit distribution, ms (values >=100):       ", units_dist(ms, 100))
    print("units-digit distribution, ciphertext.txt (full 369):", units_dist(ct))
    print("units-digit distribution, ciphertext.txt (>=100):   ", units_dist(ct, 100))
    print("units-digit distribution, ciphertext.txt (first", last_b, "= ms's own coverage):",
          units_dist(covered_ct[:last_b]))


if __name__ == '__main__':
    main()
