#!/usr/bin/env python3
"""AX-4612TR2: content-level realignment of the two blind passes.

AX-4612TR's positional diff (agreement.py, passB p1 shifted -1 line for the header row) assumed a
single, uniform offset held the rest of p1's lines in step. Checking p1_r22 against the image while
settling (this worker, 26 Sept 2026) found that assumption false: passB_p1 r22 does NOT match
passA_p1 r22 (passB r23 does) -- a second, independent one-line drift opens somewhere before r22, on
top of the header offset already corrected for. A flat -1 shift is therefore not trustworthy for the
whole page, not just from p2_r10 on as AX-4612TR reported. Both pages are realigned here the same
way: flatten each pass's tokens into one per-page stream in reading order (p1's passB stream drops
its header row's 3 tokens first, since passA never numbered it), then align the two flat streams by
content with difflib.SequenceMatcher, not by line/position label. This finds a true agreement figure
and disagreement list for both pages that no longer depends on line-numbering staying in step.

Output: ax4612tr/p1_disagreements.tsv, ax4612tr/p2_disagreements.tsv (page, a_line, a_pos, b_line,
b_pos, a_tok, b_tok, kind) and prints both true agreement figures.
"""
import csv, difflib

BASE = 'ax4612tr/'

def load_flat(path):
    """Return list of (line, pos, token) in file order."""
    rows = []
    with open(path, encoding='utf-8') as f:
        r = csv.DictReader(f, delimiter='\t')
        for row in r:
            rows.append((row['line'], int(row['position']), row['token']))
    return rows

def norm(tok):
    return tok.strip().lower()

def kind(tok):
    t = tok.lstrip('=').strip()
    return 'numeral' if t[:1].isdigit() else 'clear'

def content_align(a2, b2, page):
    a_keys = [norm(t) for (_, _, t) in a2]
    b_keys = [norm(t) for (_, _, t) in b2]
    sm = difflib.SequenceMatcher(a=a_keys, b=b_keys, autojunk=False)
    total = 0
    agree = 0
    disagreements = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            total += i2 - i1
            agree += i2 - i1
        elif tag == 'replace':
            n = max(i2 - i1, j2 - j1)
            for k in range(n):
                total += 1
                ai = i1 + k if i1 + k < i2 else None
                bj = j1 + k if j1 + k < j2 else None
                a_line, a_pos, a_tok = a2[ai] if ai is not None else ('', '', '')
                b_line, b_pos, b_tok = b2[bj] if bj is not None else ('', '', '')
                disagreements.append({
                    'page': page, 'a_line': a_line, 'a_pos': a_pos, 'b_line': b_line, 'b_pos': b_pos,
                    'a_tok': a_tok, 'b_tok': b_tok, 'kind': kind(a_tok or b_tok or ''),
                })
        elif tag == 'delete':
            for k in range(i1, i2):
                total += 1
                a_line, a_pos, a_tok = a2[k]
                disagreements.append({
                    'page': page, 'a_line': a_line, 'a_pos': a_pos, 'b_line': '', 'b_pos': '',
                    'a_tok': a_tok, 'b_tok': '', 'kind': kind(a_tok),
                })
        elif tag == 'insert':
            for k in range(j1, j2):
                total += 1
                b_line, b_pos, b_tok = b2[k]
                disagreements.append({
                    'page': page, 'a_line': '', 'a_pos': '', 'b_line': b_line, 'b_pos': b_pos,
                    'a_tok': '', 'b_tok': b_tok, 'kind': kind(b_tok),
                })
    return total, agree, disagreements

def write_tsv(path, rows):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['page', 'a_line', 'a_pos', 'b_line', 'b_pos', 'a_tok', 'b_tok', 'kind'], delimiter='\t')
        w.writeheader()
        for row in rows:
            w.writerow(row)

if __name__ == '__main__':
    a1 = load_flat(BASE + 'passA_p1.tsv')
    b1_all = load_flat(BASE + 'passB_p1.tsv')
    b1 = [row for row in b1_all if row[0] != 'p1_r01']  # drop passB's header row, no counterpart in passA
    t1, a1n, d1 = content_align(a1, b1, 'p1')
    print(f'p1 (content-level realignment, supersedes AX-4612TR\'s 80.1% positional figure): {a1n}/{t1} = {100*a1n/t1:.1f}% true agreement, {len(d1)} disagreements')
    write_tsv(BASE + 'p1_disagreements.tsv', d1)

    a2 = load_flat(BASE + 'passA_p2.tsv')
    b2 = load_flat(BASE + 'passB_p2.tsv')
    t2, a2n, d2 = content_align(a2, b2, 'p2')
    print(f'p2 (content-level realignment): {a2n}/{t2} = {100*a2n/t2:.1f}% true agreement, {len(d2)} disagreements')
    write_tsv(BASE + 'p2_disagreements.tsv', d2)

    print(f'combined: {a1n+a2n}/{t1+t2} = {100*(a1n+a2n)/(t1+t2):.1f}%')

    num1 = sum(1 for d in d1 if d['kind'] == 'numeral')
    num2 = sum(1 for d in d2 if d['kind'] == 'numeral')
    print(f'numeral-only disagreements (these feed the two checks): p1 {num1}, p2 {num2}')
