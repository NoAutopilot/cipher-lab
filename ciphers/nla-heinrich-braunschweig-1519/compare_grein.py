#!/usr/bin/env python3
"""Diff the decode of the numeral groups (reading_tokens_548/562.tsv, from tools/decode_key.py with Grein's key
sheets) against Grein's own deciphered word lists (grein_words.tsv, transcribed from aufn_0002 of each file).

  python3 compare_grein.py           write grein_diff.tsv and print the counts
  python3 compare_grein.py --check   exit 1 if grein_diff.tsv is stale (rule 7)

Words are compared after lower-casing and folding u/v (both sheets key one number to 'u (v)' / 'u.v.').
One cipher word = one '/'-terminated group in ciphertext_<n>.tsv (group column)."""
import csv, os, sys
D = os.path.dirname(os.path.abspath(__file__))
def norm(w): return w.lower().replace('v', 'u')
def words(n):
    ct = list(csv.DictReader(open(os.path.join(D, f'ciphertext_{n}.tsv')), delimiter='\t'))
    tok = {r['pos']: r for r in csv.DictReader(open(os.path.join(D, f'reading_tokens_{n}.tsv')), delimiter='\t')}
    out = {}
    for r in ct:
        if r['sign'] == '/': continue
        t = tok[r['pos']]
        w = out.setdefault(int(r['group']), {'signs': [], 'value': '', 'M': 0})
        w['signs'].append(r['sign']); w['value'] += t['value']; w['M'] += t['grade'] == 'M'
    return out
rows = ['letter\tidx\tsigns\tdecode\tgrein_word\tM_tokens\tverdict']
cnt = {}
for r in csv.DictReader(open(os.path.join(D, 'grein_words.tsv')), delimiter='\t'):
    w = words(r['letter']).get(int(r['idx']))
    dec = w['value'] if w else ''
    v = 'agree' if w and norm(dec) == norm(r['grein_word']) else 'differ'
    cnt[(r['letter'], v)] = cnt.get((r['letter'], v), 0) + 1
    rows.append('\t'.join([r['letter'], r['idx'], '.'.join(w['signs']) if w else '', dec, r['grein_word'],
                           str(w['M'] if w else ''), v]))
for n in ('548', '562'):
    extra = set(words(n)) - {int(r['idx']) for r in csv.DictReader(open(os.path.join(D, 'grein_words.tsv')), delimiter='\t') if r['letter'] == n}
    for g in sorted(extra): rows.append(f'{n}\t{g}\t\t{words(n)[g]["value"]}\t\t\tnot in Grein list')
text = '\n'.join(rows) + '\n'
p = os.path.join(D, 'grein_diff.tsv')
if '--check' in sys.argv:
    ok = os.path.exists(p) and open(p).read() == text
    print('grein_diff.tsv up to date' if ok else 'grein_diff.tsv STALE'); sys.exit(0 if ok else 1)
open(p, 'w').write(text)
print(' '.join(f'{k[0]} {k[1]} {v}' for k, v in sorted(cnt.items())))
