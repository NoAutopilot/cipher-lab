#!/usr/bin/env python3
"""Write key.tsv and ciphertext_key.tsv for tools/decode_key.py from the annealer's best key
(target_result.json, solve.py target --seeds 8 --iters 3000000) plus the hand corrections below, each
made from a crib in the solver's own reading (listed in NOTES.md "Reading"). Grade S for a letter value
seen >= 3 times (the matched control reads such values), M for rarer values. Codes (>100) and the printed
letter-signs (r rr nn ...) are left unkeyed (U).
    python3 make_key.py [--check]
"""
import csv, io, json, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
CORR = {  # value: (letter, crib)
    '62': ('u', "44 62 80 78 = kunne (x3), 20 26 47 26 32 ... 62 = eder numera"),
    '70': ('b', "70 51 26 27 44 26 = Bielke; 70 72 78 26 32 = Baner"),
    '50': ('c', "65 50 66 = och; retranchera"),
    '49': ('c', "retranchera eder"),
    '58': ('v', "57 26 27 24 72 58 73 80 48 26 32 73 = vele advancera"),
    "72°": ('a', "54 72° = på (på foten, påkomma); 72° 81 26 32 = åter (printed mark = å)"),
    "65''": ('o', "23 65'' 27 51 73 = följa; förste, tilförne (printed mark = ö)"),
    '38': ('x', "71 26 57 62 38 26 80 = bevuxen"),
    '35': ('o', "höglar, as 33 in the same word two lines up"),
    '99': ('a', "advancera 99 100 det närmeste = åt det närmeste"),
    '30': ('e', "17 54 72 32 30 = Sparre (name; e)"),
    '53': ('i', "her 53 72 68 73 78 70 72 78 26 32 = Johan Baner? (j=i)"),
}
LETTERS = {'u': 'u', 'v': 'u'}


def main():
    res = json.load(open(os.path.join(HERE, 'target_result.json')))
    key = dict(res['key'])
    rows = list(csv.DictReader(open(os.path.join(HERE, 'ciphertext_verified.tsv'), encoding='utf-8'), delimiter='\t'))
    def sign(r):
        return r['value'] + r['mark'].replace('"', "''")
    cnt = Counter(sign(r) for r in rows if r['class'] == 'NUM' and int(r['value']) <= 100)
    kb = io.StringIO(); w = csv.writer(kb, delimiter='\t', lineterminator='\n')
    w.writerow(['sign', 'value', 'grade', 'source', 'note'])
    for s in sorted(cnt, key=lambda x: (int(x.rstrip("°'")), x)):
        if s in CORR:
            v, note = CORR[s]; src = 'crib-correction'
        else:
            v, note, src = key[s], '', 'anneal'
        w.writerow([s, v, 'S' if cnt[s] >= 3 else 'M', src, f'n={cnt[s]}' + (f'; {note}' if note else '')])
    cb = io.StringIO(); w = csv.writer(cb, delimiter='\t', lineterminator='\n')
    w.writerow(['line', 'pos', 'token', 'conf'])
    for r in rows:
        if r['class'] == 'CLEAR':
            tok, conf = 'w:' + r['value'], ''
        elif r['class'] == 'NUM':
            tok, conf = sign(r), ''
        else:
            tok, conf = r['value'], ''
        w.writerow([r['page_line'], r['pos'], tok, conf])
    out = {'key.tsv': kb.getvalue(), 'ciphertext_key.tsv': cb.getvalue()}
    if '--check' in sys.argv:
        sys.exit(0 if all(open(os.path.join(HERE, f), encoding='utf-8').read() == t for f, t in out.items()) else 1)
    for f, t in out.items():
        open(os.path.join(HERE, f), 'w', encoding='utf-8').write(t)


if __name__ == '__main__':
    main()
