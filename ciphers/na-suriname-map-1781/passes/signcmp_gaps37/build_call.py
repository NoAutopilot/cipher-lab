# GAPS37-na-suriname-map-1781 (account-4), 3 Oct 2026: build the value-blind masked query list for one same-hand g|l
# sorting call on 2077. Every 2077 token of reader code g (46, four of them C-known: L06:4 = g; L10:61, L12:26, L12:48 = l,
# exceptions_nieuw_image.tsv GAPS23/24) is masked as #k in its line's reader-code sequence; the reader is never told which
# four are known or what any sign means. Run from the target folder.
import csv
D = 'passes/signcmp_gaps37/'
KNOWN = {('2077_L06', 4): 'g', ('2077_L10', 61): 'l', ('2077_L12', 26): 'l', ('2077_L12', 48): 'l'}
lines = {}
for r in csv.reader((l for l in open('ciphertext_2077_legend.tsv') if not l.startswith('#')), delimiter='\t'):
    if r[0] == 'line': continue
    lines.setdefault(r[0], []).append((int(r[1]), r[2]))
q = []; seqs = {}; n = 0
for L in sorted(lines):
    out = []
    for pos, s in lines[L]:
        if s == 'g':
            n += 1; q.append((f'#{n}', L, pos, KNOWN.get((L, pos), ''))); out.append(f'#{n}')
        elif s.startswith('w:'): out.append('<plain:%s>' % s[2:])
        else: out.append(s)
    if any(o.startswith('#') for o in out): seqs[L] = ' '.join(out)
with open(D + 'queries_key.tsv', 'w') as f:
    f.write('query\tline\tpos\tknown_C\n')
    for row in q: f.write('\t'.join(map(str, row)) + '\n')
with open(D + 'query_sequences.txt', 'w') as f:
    for L, s in seqs.items(): f.write(f'{L.replace("2077_", "")}: {s}\n')
print(len(q), 'queries on', len(seqs), 'lines; known', sum(1 for r in q if r[3]))
