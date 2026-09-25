#!/usr/bin/env python3
"""PX-BRODEC step 2 control: decode m0179-r1/m0180-r1 (body, letters 80/81) with key.tsv and compare, letter
by letter, against plaintext_appendix.tsv's own Carta 80/81 Deciffrada text (the manuscript's contemporary
plaintext for the same two letters, already on file independently of this decode).

Uses difflib.SequenceMatcher over the two letter sequences, the same alignment convention as
tools/reconcile_passes.py and this target's own scripts/07_reconcile.py ('equal' opcodes = agreement,
'replace'/'insert'/'delete' = disagreement, over the longer of the two sequences) rather than assuming the
two token runs are the same length and line up position-for-position -- body_ciphertext.tsv's own run has
2 extra tokens for m0179-r1 that ciphertext_appendix.tsv's Carta 80 does not (PX-BROBODY, NOTES.md), so a
naive 1:1 index comparison would misattribute a length difference as many mismatches.

Run: python3 scripts/10_body_control.py   (from the target folder; reads reading_body_tokens.tsv,
key.tsv and plaintext_appendix.tsv; prints a report, writes nothing)
"""
import csv
import difflib
import os
import re

HERE = os.path.dirname(__file__)
TARGET = os.path.join(HERE, '..')

CONTROLS = [
    ('m0179-r1', 'Carta 80'),
    ('m0180-r1', 'Carta 81'),
]


def fold(s):
    s = s.lower()
    s = (s.replace('ã', 'a').replace('á', 'a').replace('à', 'a').replace('â', 'a')
          .replace('é', 'e').replace('ê', 'e').replace('í', 'i').replace('ó', 'o')
          .replace('ô', 'o').replace('õ', 'o').replace('ú', 'u').replace('ç', 'c'))
    return re.sub(r'[^a-z]', '', s)


def load_body_decode(run_id):
    letters = []
    with open(os.path.join(TARGET, 'reading_body_tokens.tsv'), encoding='utf-8', newline='') as f:
        r = csv.DictReader(f, delimiter='\t')
        for row in r:
            if row['line'] == run_id:
                letters.append((row['value'], row['grade']))
    return letters


def load_appendix_plain(entry_label):
    with open(os.path.join(TARGET, 'plaintext_appendix.tsv'), encoding='utf-8', newline='') as f:
        r = csv.DictReader(f, delimiter='\t')
        for row in r:
            if row['entry_label'] == entry_label:
                line = row['deciffrada_line']
                line = re.sub(r'\s*V\.?(Sa|mce)?\.?\s*$', '', line, flags=re.IGNORECASE)
                return line
    return None


def main():
    for run_id, entry_label in CONTROLS:
        body = load_body_decode(run_id)
        body_str = ''.join(v if v not in ('?', '') else '_' for v, g in body)
        plain_line = load_appendix_plain(entry_label)
        plain_str = fold(plain_line)
        sm = difflib.SequenceMatcher(a=body_str, b=plain_str, autojunk=False)
        agree = sum(b.size for b in sm.get_matching_blocks())
        total = max(len(body_str), len(plain_str))
        print(f'== {run_id} vs {entry_label} ==')
        print(f'  body decode ({len(body_str)} tokens): {body_str}')
        print(f'  appendix plaintext, stripped ({len(plain_str)} letters, from "{plain_line}"): {plain_str}')
        print(f'  agreement (SequenceMatcher matching blocks / longer sequence): {agree}/{total} = {agree/total:.1%}')
        opcodes = sm.get_opcodes()
        print(f'  opcodes: ' + '; '.join(f'{tag} body[{i1}:{i2}]={body_str[i1:i2]!r} plain[{j1}:{j2}]={plain_str[j1:j2]!r}'
                                          for tag, i1, i2, j1, j2 in opcodes if tag != 'equal'))
        print()


if __name__ == '__main__':
    main()
