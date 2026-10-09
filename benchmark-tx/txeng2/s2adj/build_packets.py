"""TXE2-S2ADJ: split the 208 disagree rows of ../s2read/adjud_queue.tsv into packets of <= 16 rows, in queue order
(13 packets: 12 x 16 + 1 x 16 = 208; a line may span two packets, each packet gets every crop of its lines). The 167 uncertain rows are not sent."""
import csv
rows = [r for r in csv.DictReader(open('../s2read/adjud_queue.tsv'), delimiter='\t') if r['kind'] == 'disagree']
packets = [rows[i:i + 16] for i in range(0, len(rows), 16)]
cols = ['line', 'col', 'kind', 'candidates', 'left_neighbours', 'right_neighbours']
for i, p in enumerate(packets, 1):
    with open(f'packets/P{i:02d}_queue.tsv', 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in p: f.write('\t'.join(r[c] for c in cols) + '\n')
    print(f'P{i:02d}', len(p), ' '.join(sorted({r["line"][-3:] for r in p})))
print('rows', sum(map(len, packets)), 'packets', len(packets))
