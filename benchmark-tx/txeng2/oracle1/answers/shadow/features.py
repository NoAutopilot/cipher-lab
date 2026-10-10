"""Shadow-box features (owner, 10 Oct 2026: "the super dark blocks on the page are shadows but are thought to be signs").
Per box: touches the crop's left/right edge, mean grey, share of near-black pixels, grey spread. Labels from the owner's
box-check answers (trashed = NOT-LETTER, kept = checked). Geometry and grey levels only; no value read."""
import csv, json, glob, os, sys
from PIL import Image
import numpy as np
R = 'benchmark-tx/txeng2/oracle1/sorter'
pages = json.load(open(f'{R}/pages.json'))
def ans(db):
    t = {os.path.basename(f)[:-5] for f in glob.glob(f'{db}/moves/*.json') if json.load(open(f)).get('to') == 'NOT-LETTER'}
    k = {os.path.basename(f)[:-5] for f in glob.glob(f'{db}/checked/*.json')}
    return t, k
SP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # answers/: birago/db, luzerne/db
out = []
for hand, db in [('birago', f'{SP}/birago/db'), ('luzerne', f'{SP}/luzerne/db'), ('vivonne', None)]:
    t, k = ans(db) if db else (set(), set())
    imgs = {}
    for r in csv.DictReader(open(f'{R}/{hand}/signs.tsv'), delimiter='\t'):
        p = r['page']
        if p not in imgs: imgs[p] = np.asarray(Image.open(pages[p]['image']).convert('L'), dtype=np.float32)
        a = imgs[p]; H, W = a.shape; x, y, w, h = (int(float(r[c])) for c in 'xywh')
        b = a[max(0, y):y + h, max(0, x):x + w]
        if b.size == 0: continue
        med = float(np.median(a))
        out.append(dict(hand=hand, sid=r['sid'], lab='trash' if r['sid'] in t else 'kept' if r['sid'] in k else '-',
                        edge=int(x <= 3 or x + w >= W - 3), mean=round(float(b.mean()) / med, 3), black=round(float((b < 0.35 * med).mean()), 3),
                        std=round(float(b.std()) / med, 3), w=w, h=h, H=H))
w = csv.DictWriter(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'features.tsv'), 'w'), fieldnames=list(out[0]), delimiter='\t'); w.writeheader(); w.writerows(out)
import statistics as st
for hand in ['birago', 'luzerne', 'vivonne']:
    for lab in ['trash', 'kept', '-']:
        rs = [r for r in out if r['hand'] == hand and r['lab'] == lab]
        if not rs: continue
        q = lambda f: (round(min(r[f] for r in rs), 2), round(st.median(r[f] for r in rs), 2), round(max(r[f] for r in rs), 2))
        print(f"{hand:8} {lab:5} n={len(rs):3} edge={sum(r['edge'] for r in rs):3} mean(min,med,max)={q('mean')} black={q('black')} std={q('std')} h/H={q('h')}")
