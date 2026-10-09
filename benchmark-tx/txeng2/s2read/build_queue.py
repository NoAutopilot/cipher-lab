"""TXE2-S2READ step 3: adjudication queue from reconcile_passes output (disagreements + uncertain), TXE-Q's format:
line, col (= ciphertext_draft position), kind, candidates, left_neighbours, right_neighbours (3 draft signs each side)."""
import csv
R = 'rec'
draft = {}
for r in csv.DictReader(open(f'{R}/ciphertext_draft.tsv'), delimiter='\t'):
    draft.setdefault(r['line'], {})[int(r['position'])] = r['sign']
q = []
for kind, fn in (('disagree', 'disagreements.tsv'), ('uncertain', 'uncertain.tsv')):
    for r in csv.DictReader(open(f'{R}/{fn}'), delimiter='\t'):
        c = int(r['col']); d = draft[r['line']]
        cands = [r['A'], r['B']] if kind == 'disagree' else [r['A']]
        cands = ' | '.join(x if x != '-' else '(no sign)' for x in cands)
        L = ' '.join(d[i] for i in range(c - 3, c) if i in d); Rr = ' '.join(d[i] for i in range(c + 1, c + 4) if i in d)
        q.append((r['line'], c, kind, cands, L, Rr))
q.sort(key=lambda x: (x[0], x[1]))
with open('adjud_queue.tsv', 'w') as f:
    f.write('line\tcol\tkind\tcandidates\tleft_neighbours\tright_neighbours\n')
    for x in q: f.write('\t'.join(map(str, x)) + '\n')
print(len(q), 'rows', sum(1 for x in q if x[2] == 'disagree'), 'disagree')
