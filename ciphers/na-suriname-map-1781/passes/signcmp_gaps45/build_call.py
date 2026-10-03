# GAPS45-na-suriname-map-1781 (account-4), 3 Oct 2026: build the masked query list for one same-hand n|m sorting call on
# 2077. Every 2077 token of reader code [u-dots] (17, all decoded n at H by shape name, key_period_codes_nieuw.tsv) is
# masked as #k in its line's reader-code sequence. Same-hand references are single letters masked inside 2077's own
# plain-script words: lowercase m (4), lowercase n (6) and y-with-dots (5; the key's N-row sign is "ij / y with dots").
# The reader is told no value and no hypothesis; plain words are legible, so the references are not blind (prereg.md).
# Run from the target folder.
import csv
D = 'passes/signcmp_gaps45/'
# (line, pos) of the plain word -> list of (letter index in the word, ref class)
REFS = {('2077_L07', 12): [(1, 'm')],            # Ambagts
        ('2077_L08', 1): [(2, 'm')],             # Kamer
        ('2077_L08', 53): [(0, 'm')],            # legend label m
        ('2077_L13', 10): [(0, 'm')],            # materialien
        ('2077_L07', 6): [(2, 'n')],             # den
        ('2077_L07', 14): [(2, 'n')],            # van
        ('2077_L13', 7): [(5, 'n')],             # berging (first n)
        ('2077_L13', 15): [(0, 'n')],            # nog
        ('2077_L13', 16): [(2, 'n')],            # een
        ('2077_L13', 8): [(2, 'n')],             # van
        ('2077_L07', 4): [(2, 'y-dots')],        # huÿs
        ('2077_L09', 25): [(7, 'y-dots')],       # bootehuÿs
        ('2077_L09', 30): [(6, 'y-dots')],       # Vaartuÿgen
        ('2077_L13', 13): [(10, 'y-dots')],      # gevangenhuÿsen
        ('2077_L17', 3): [(7, 'y-dots')]}        # Smeederÿ
lines = {}
for r in csv.reader((l for l in open('ciphertext_2077_legend.tsv') if not l.startswith('#')), delimiter='\t'):
    if r[0] == 'line': continue
    lines.setdefault(r[0], []).append((int(r[1]), r[2]))
q = []; seqs = {}; n = 0
for L in sorted(lines):
    out = []
    for pos, s in lines[L]:
        if s == '[u-dots]':
            n += 1; q.append((f'#{n}', L, pos, '', 'cipher')); out.append(f'#{n}')
        elif s.startswith('w:'):
            w = s[2:]
            if (L, pos) in REFS:
                ch = list(w)
                for i, cls in REFS[(L, pos)]:
                    assert ch[i].lower() in {'m': 'm', 'n': 'n', 'y-dots': 'ÿ'}[cls], (L, pos, w, i)
                    n += 1; q.append((f'#{n}', L, pos, i, 'ref-' + cls)); ch[i] = f'#{n}'
                out.append('<plain:%s>' % ''.join(ch))
            else:
                out.append('<plain:%s>' % w)
        else: out.append(s)
    if any('#' in o for o in out): seqs[L] = ' '.join(out)
with open(D + 'queries_key.tsv', 'w') as f:
    f.write('query\tline\tpos\tletter_index\tclass\n')
    for row in q: f.write('\t'.join(map(str, row)) + '\n')
with open(D + 'query_sequences.txt', 'w') as f:
    for L, s in seqs.items(): f.write(f'{L.replace("2077_", "")}: {s}\n')
print(len(q), 'queries on', len(seqs), 'lines:', sorted(seqs))
