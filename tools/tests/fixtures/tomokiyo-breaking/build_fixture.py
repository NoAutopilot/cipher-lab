#!/usr/bin/env python3
"""Rebuild the cipher of Tomokiyo, "Breaking a Simple Cipher" (sources/cryptiana/web/breaking.htm, section before
"Further Steps") as a tools/decode_key.py target: ciphertext.tsv, key.tsv and decode.json in this folder.

The page prints the letter (an English 1781 naval despatch, numbers for letters, '-' as word break, '=' where a word runs
on to the next line) with 7, 22, 18, 15 already replaced by a, t, h, e; this script puts those four numbers back, so the
ciphertext is numeric again except for the clear words the page shows in clear. The key is the page's own identifications
(the "Breaking" and "Further Steps" sections: 7 a, 22 t, 18 h, 15 e, 26 f, 9 w, 14 d, 23 s, 8 c, 24 o, 29 p, 21 i, 6 u,
19 v, 5 n, 11 m, 4 g, 2 l, 12 b, 3 k, 25 r, 13 y; 1 q from "re 1 6 e s t", 17 x from "e 17 e r t i o n", 0 the numeral);
33 40 61 32 84 (the heading) stay unkeyed. Used by tools/tests/test_decode_key_consistency.py and the TT-CONS control
(tools/tests/PREREG-TT-CONS.md). Credit: Satoshi Tomokiyo, cryptiana.web.fc2.com, breaking.htm. Run from the repo root."""
import os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
txt = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'html2text.py'),
                      os.path.join(ROOT, 'sources', 'cryptiana', 'web', 'breaking.htm')],
                     capture_output=True, text=True, check=True).stdout.splitlines()
a = next(i for i, l in enumerate(txt) if l.startswith("Let's look at how far"))
b = next(i for i, l in enumerate(txt) if l.startswith('## Further Steps'))
BACK = {'a': '7', 't': '22', 'h': '18', 'e': '15'}
KEY = {v: k for k, v in BACK.items()}
KEY.update({'26': 'f', '9': 'w', '14': 'd', '23': 's', '8': 'c', '24': 'o', '29': 'p', '21': 'i', '6': 'u', '19': 'v',
            '5': 'n', '11': 'm', '4': 'g', '2': 'l', '12': 'b', '3': 'k', '25': 'r', '13': 'y', '1': 'q', '17': 'x',
            '0': '0'})
rows, n = [], 0
for l in txt[a + 1:b]:
    toks = l.split()
    if not toks:
        continue
    n += 1
    clear_line = not any(re.fullmatch(r'\d+', t) for t in toks)
    pos = 0
    for t in toks:
        if t == '=':
            continue  # the word runs on: no break
        if clear_line or (len(t) > 1 and not t.isdigit()):
            s = 'w:' + t
        else:
            s = BACK.get(t, t)
        rows.append(f'L{n:02d}\t{pos}\t{s}\t')
        pos += 1
open(os.path.join(HERE, 'ciphertext.tsv'), 'w').write('line\tpos\tsign\tconf\n' + '\n'.join(rows) + '\n')
open(os.path.join(HERE, 'key.tsv'), 'w').write('code\tvalue\tgrade\tsource\n' + ''.join(
    f'{k}\t{v}\tH\tbreaking.htm\n' for k, v in sorted(KEY.items(), key=lambda kv: int(kv[0]))))
open(os.path.join(HERE, 'decode.json'), 'w').write(
    '{"ciphertext": "ciphertext.tsv", "key": "key.tsv", "style": "concat", "word_sep": "-", "nonsign": ["-"],\n'
    ' "reading": "reading.txt", "tokens": "reading_tokens.tsv"}\n')
print(f'{n} lines, {sum(1 for r in rows if not r.split(chr(9))[2].startswith("w:"))} signs incl. separators')
