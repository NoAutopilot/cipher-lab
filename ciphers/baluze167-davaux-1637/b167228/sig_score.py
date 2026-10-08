#!/usr/bin/env python3
"""SIG-B228: score the two blind shape reads (b167228/sig_tiles/read{A,B}.tsv) against key_private.tsv under prereg_sig.md items 3-4.
A tile's agreed exemplar = a letter both reads name on the same channel (A = f.229 tiles, B = Tomokiyo block). Writes sig_score.tsv,
prints the decoy gate (overall and per channel) and the adopted shape map. Usage: python3 b167228/sig_score.py (from the target folder)"""
import collections, csv
D = 'b167228/sig_tiles/'
rd = lambda f: {r['tile']: r for r in csv.DictReader(open(D + f), delimiter='\t')}
A, B, K = rd('readA.tsv'), rd('readB.tsv'), rd('key_private.tsv')
def agreed(t, ch):
    a, b = A[t][ch], B[t][ch]
    return a if a == b and a != 'NONE' else None
rows, dec, byshape = ['tile\tshape\twhere\tch_A_f229\tch_B_tomokiyo'], {}, collections.defaultdict(list)
for t in sorted(K):
    s = K[t]['shape']; fa, fb = agreed(t, 'A'), agreed(t, 'B')
    rows.append(f"{t}\t{s}\t{K[t]['where']}\t{fa or '-'}\t{fb or '-'}")
    if s.startswith('DECOY:'):
        right = s.split('=')[1]; dec[t] = (s, fa == right, fb == right)
    else:
        byshape[s].append({fa, fb} - {None})
open('b167228/sig_score.tsv', 'w').write('\n'.join(rows) + '\n')
any_ok = sum(a or b for _, a, b in dec.values()); ok_a = sum(a for _, a, _ in dec.values()); ok_b = sum(b for _, _, b in dec.values())
for t, (s, a, b) in sorted(dec.items()):
    print('decoy', t, s, 'f229-channel', a, 'tomokiyo-channel', b)
print(f'decoy gate (prereg item 4, >=2 of 3 by both reads, any exemplar): {any_ok}/3 ->', 'PASS' if any_ok >= 2 else 'FAIL')
print(f'  per channel: f229 tiles {ok_a}/3, Tomokiyo block {ok_b}/3')
for s, sets in sorted(byshape.items()):
    c = collections.Counter(v for st in sets for v in st)
    top = c.most_common(1)
    val = top[0][0] if top and top[0][1] * 2 > len(sets) and len(c) == 1 else None
    if top and top[0][1] * 2 > len(sets) and len(c) > 1:
        val = None  # conflicting agreed values across channels/tiles: stays U
    print(f'shape {s}: {len(sets)} tile(s), agreed values {dict(c)} ->', val or 'U', '' if any_ok >= 2 else '(not adopted: decoy gate FAIL)')
