#!/usr/bin/env python3
"""extract_word_code.py: turn a Tomokiyo "word CODE" text-table region (html2text output, one pair per line,
tab or space separated, code last) into a house-style key TSV. U2 helper, CRYPT-KEYS-A, 27 Sept 2026 -- not a
tools/ shared script since the line shape (and its exceptions) differs per Cryptiana page; each call is
reviewed by hand against the source before the TSV is committed (this job's brief, U2).

Convention: sign = the CODE (what a ciphertext token would be), value = the WORD/meaning (matches the house
style already used by tools/keys/key60.tsv: 'sign\\tvalue\\tgrade\\tsource\\tnote'). A line wrapped in [...] is
Tomokiyo's own bracket (his marked-uncertain/inferred convention on the pages that use it); a trailing '?' on
either side of a line is his own uncertainty mark. Both make that row grade M with a note, on top of
base_grade -- base_grade itself is M throughout when the whole table is his cryptanalytic reconstruction
rather than a period key sheet he is transcribing (CLAUDE.md rule 4 grading is per-token: 'M uncertain'; this
job's brief simplifies the two-way choice to H "a period key table as he prints it" vs M "recovered ... rather
than read from a key sheet").
"""
import re

LINE_RE = re.compile(r'^(.+?)\s+([A-Za-z]{1,8}\??)$')


def parse_lines(lines, base_grade, base_note, code_first=False):
    """lines: raw text lines (already sliced to the table region). Returns a list of
    (sign, value, grade, note) rows; unmatched lines are returned separately for review."""
    rows, unmatched = [], []
    for raw in lines:
        s = raw.strip('\t ').strip()
        if not s:
            continue
        bracketed = s.startswith('[') and s.endswith(']')
        if bracketed:
            s = s[1:-1].strip()
        m = LINE_RE.match(s)
        if not m:
            unmatched.append(raw)
            continue
        a, b = m.group(1).strip(), m.group(2).strip()
        word, code = (b, a) if code_first else (a, b)
        uncertain = bracketed or word.endswith('?') or code.endswith('?')
        grade = 'M' if uncertain else base_grade
        notes = [base_note] if base_note else []
        if bracketed:
            notes.append('bracketed by Tomokiyo (inferred/uncertain, not directly attested)')
        if word.endswith('?') or code.endswith('?'):
            notes.append("Tomokiyo's own '?' uncertainty mark")
        rows.append((code.rstrip('?'), word.rstrip('?'), grade, '; '.join(notes)))
    return rows, unmatched


def write_tsv(path, header_comment_lines, rows, source):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        for l in header_comment_lines:
            f.write(l.rstrip('\n') + '\n')
        f.write('sign\tvalue\tgrade\tsource\tnote\n')
        for sign, value, grade, note in rows:
            f.write(f'{sign}\t{value}\t{grade}\t{source}\t{note}\n')
