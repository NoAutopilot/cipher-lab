#!/usr/bin/env python3
"""Write votes.tsv and exceptions.tsv for tools/decode_key.py (NEXT2-PAG, 2 Oct 2026).

votes.tsv: one row per aligned code token, the period-gloss chunk the alignment (align/align_all.tsv) puts over that
token, located at its ciphertext.tsv page+position through align/pairs.tsv `positions`. decode_key.py grades a key
value C where the chunk equals it (known plaintext, rule 4) and M where it does not.
exceptions.tsv: image digit overrides (pairs.tsv `overrides`) and the cipher numerals that repeat the gloss's own
numeral (align_all kind 'clear', grade I). `--check` exits 1 if either committed file is stale.
"""
import csv, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rd = lambda f: list(csv.DictReader(open(os.path.join(D, f), encoding='utf-8'), delimiter='\t'))
pairs, al = rd('align/pairs.tsv'), rd('align/align_all.tsv')
key = {r['code']: r for r in rd('key.tsv')}
by = {}
for a in al:
    by.setdefault(a['cipher_line'], []).append(a)
votes, exc = ['line\tposition\tvalue\tcipher_line\tstatus'], ['line\tposition\tvalue\tgrade\treason']
for p in pairs:
    pos, toks = p['positions'].split(','), by[p['cipher_line']]
    ov = dict(o.split(':') for o in p['overrides'].split(';') if o)
    assert len(pos) == len(toks), p['cipher_line']
    for q, a in zip(pos, toks):
        if a['kind'] == 'num' and a['plain_chunk']:
            votes.append(f"{p['page']}\t{q}\t{a['plain_chunk']}\t{p['cipher_line']}\t{a['status']}")
        if q in ov:
            old, new = ov[q].split('->')
            k = key.get(new)
            v, g = (k['value'], 'M') if k else ('?', 'U')
            exc.append(f"{p['page']}\t{q}\t{v}\t{g}\timage reads {new}, ciphertext.tsv {old} (image override: NEXT-PAG, A2-PAG2)")
        elif a['kind'] == 'clear' and a['raw'].startswith('('):
            n = a['raw'].strip('()')
            exc.append(f"{p['page']}\t{q}\t{n}\tI\tcipher numeral repeating the gloss's own '{n}' ({p['cipher_line']})")
out = {'votes.tsv': '\n'.join(votes) + '\n', 'exceptions.tsv': '\n'.join(exc) + '\n'}
stale = 0
for f, s in out.items():
    path = os.path.join(D, f)
    if '--check' in sys.argv:
        if not os.path.exists(path) or open(path, encoding='utf-8').read() != s:
            print(f'STALE {f}'); stale = 1
    else:
        open(path, 'w', encoding='utf-8').write(s)
print(f'votes {len(votes) - 1}, exceptions {len(exc) - 1}')
sys.exit(stale)
