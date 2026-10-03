# TX-ATLAS-B72 (3 Oct 2026): exemplar sheets of the clusters the clerk sheet could not name, for one model read per sheet.
# Row = cluster id, then up to 10 tiles cut from the grey page (crops/<page>.png) with a small margin, scaled to a 72 px
# row; tiles nearest the cluster centre first, then spread. Run from atlas/: python3 exemplar_sheets.py -> named/sheet_NN.png
import csv, os, collections
import numpy as np, cv2
rows = {r['sid']: r for r in csv.DictReader(open('signs.tsv'), delimiter='\t')}
cl = [r for r in csv.DictReader(open('clusters.tsv'), delimiter='\t') if r['kind'] == 'sign']
names = {r['cluster']: r for r in csv.DictReader(open('cluster_names.tsv'), delimiter='\t')}
todo = sorted((c for c, r in names.items() if r['source'] == 'unnamed'), key=int)
by = collections.defaultdict(list)
for r in cl: by[r['cluster']].append(r)
pages = {}
os.makedirs('named', exist_ok=True)
CELL, PER, RPS = 72, 10, 16
for s in range(0, len(todo), RPS):
    chunk = todo[s:s + RPS]
    img = np.full((len(chunk) * (CELL + 6), 70 + PER * (CELL + 8)), 255, np.uint8)
    for ri, c in enumerate(chunk):
        mem = sorted(by[c], key=lambda r: float(r['dist']))
        pick = mem[:PER // 2] + mem[PER // 2:][::max(1, len(mem[PER // 2:]) // (PER - PER // 2) or 1)][:PER - PER // 2]
        y = ri * (CELL + 6)
        cv2.putText(img, f'C{c}', (4, y + 44), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 0, 2)
        for ci, m in enumerate(pick):
            b = rows[m['id']]
            g = pages.setdefault(b['page'], cv2.imread(f"crops/{b['page']}.png", cv2.IMREAD_GRAYSCALE))
            x, yy, w, h = (int(b[k]) for k in 'xywh'); mg = 4
            t = g[max(0, yy - mg):yy + h + mg, max(0, x - mg):x + w + mg]
            sc = CELL / max(t.shape)
            t = cv2.resize(t, (max(1, int(t.shape[1] * sc)), max(1, int(t.shape[0] * sc))), interpolation=cv2.INTER_AREA)
            x0 = 70 + ci * (CELL + 8)
            img[y + 3:y + 3 + t.shape[0], x0:x0 + t.shape[1]] = t
        cv2.line(img, (0, y + CELL + 5), (img.shape[1], y + CELL + 5), 180, 1)
    cv2.imwrite(f'named/sheet_{s // RPS:02d}.png', img)
    print(f'named/sheet_{s // RPS:02d}.png', chunk)
