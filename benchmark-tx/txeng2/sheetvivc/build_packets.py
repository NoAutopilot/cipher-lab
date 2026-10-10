"""TXE2-SHEETVIVC (copy of ../viv102base/build_packets.py, unchanged; S2-ADJ shape, copy of ../s2adj/build_packets.py + the task fill): split the DISAGREE rows of
adjud_queue.tsv into packets of <= 16 rows in queue order (a line may span two packets; each packet's task names every crop,
s1 and s2, of each of its lines). The agreed-uncertain rows are not sent (PREREG-txeng2-14 "DV1b re-priced").
Writes packets/P<k>_queue.tsv and packets/P<k>_task.txt from adjud_task_template.txt."""
import csv
D = '/home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/images'
rows = [r for r in csv.DictReader(open('adjud_queue.tsv'), delimiter='\t') if r['kind'] == 'disagree']
packets = [rows[i:i + 16] for i in range(0, len(rows), 16)]
cols = ['line', 'col', 'kind', 'candidates', 'left_neighbours', 'right_neighbours']
tmpl = open('adjud_task_template.txt').read()
for i, p in enumerate(packets, 1):
    P = f'P{i:02d}'
    with open(f'packets/{P}_queue.tsv', 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in p: f.write('\t'.join(r[c] for c in cols) + '\n')
    lines = sorted({r['line'] for r in p})
    crops = ', '.join(f'{D}/c105_{ln}_s{k}.jpg' for ln in lines for k in (1, 2))
    open(f'packets/{P}_task.txt', 'w').write(tmpl.replace('{LINES}', ', '.join(lines)).replace('{CROPS}', crops)
                                             .replace('{N}', str(len(p))).replace('{P}', P))
    print(P, len(p), ' '.join(l[-3:] for l in lines))
print('rows', sum(map(len, packets)), 'packets', len(packets))
