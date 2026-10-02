#!/usr/bin/env python3
# Promoted to tools/lookalike_pass.py (LOOKALIKE-TOOL, 2 Oct 2026): use the shared tool for any new run; this copy stays
# because its outputs are cited in NOTES.md (NEVBIR-LOOKALIKE).
"""NEVBIR-LOOKALIKE step 2 packet (2 Oct 2026): list the f.144r and f.168 tiles to re-read and cut a value-blind
candidate sheet. A tile is listed if its two readers split (any non-agree status that survived into passC) or if its
passC label sits in one of the top-10 confusion pairs of confusion_1572.tsv. Candidates per tile: reader A's and B's
labels, the passC label, and the label's top-2 confusion partners. lookalike/<run>_tiles.tsv and
lookalike/<run>_candidates.png (only the candidate cells of sign_sheet_blind_1572.png, ids only, no values).
"""
import csv, json, collections
from pathlib import Path
from PIL import Image
H = Path(__file__).resolve().parent
conf = [l.split('\t') for l in open(H / 'confusion_1572.tsv').read().splitlines()[1:]]
top = conf[:10]; toplabs = {x for p in top for x in p[:2]}
partners = collections.defaultdict(list)
for a, b, n, *_ in conf:
    partners[a].append(b); partners[b].append(a)
cells = json.load(open(H / 'sign_id_map_1572.json'))
order = [c['id'] for c in cells]
sheet = Image.open(H / 'sign_sheet_blind_1572.png')
for run in ('f144r', 'f168'):
    al = list(csv.DictReader(open(H / run / 'passC_agreement.tsv'), delimiter='\t'))
    pc = list(csv.DictReader(open(H / run / 'passC.tsv'), delimiter='\t'))
    i = 0; tiles = []; used = set()
    for r in al:
        if r['merged'] in ('', 'NONE'):
            continue
        c = pc[i]; i += 1
        assert c['passage'] == r['passage'] and c['sign_id'] == r['merged'], (run, c, r)
        split = r['status'] != 'agree'
        lab = c['sign_id']
        if not split and lab not in toplabs:
            continue
        cand = [x for x in dict.fromkeys([r['idA'], r['idB'], lab] + partners[lab][:2]) if x]
        used.update(x for x in cand if x.startswith('T'))
        ctx = ' '.join(p['sign_id'] for p in pc[max(0, i - 4):i - 1] if p['passage'] == c['passage'])
        ctx2 = ' '.join(p['sign_id'] for p in pc[i:i + 3] if p['passage'] == c['passage'])
        tiles.append(dict(run=run, passage=c['passage'], pos=c['pos'], passC=lab, A=r['idA'], B=r['idB'],
                          status=r['status'], why='split' if split else 'top-pair', candidates=','.join(cand),
                          before=ctx, after=ctx2, noteA=r.get('noteA', ''), noteB=r.get('noteB', '')))
    assert i == len(pc)
    with open(H / 'lookalike' / f'{run}_tiles.tsv', 'w') as o:
        w = csv.DictWriter(o, fieldnames=list(tiles[0]), delimiter='\t'); w.writeheader(); w.writerows(tiles)
    ids = sorted(used); NC = 8
    out = Image.new('RGB', (NC * 110, ((len(ids) + NC - 1) // NC) * 110), 'white')
    for n, t in enumerate(ids):
        k = order.index(t); gx, gy = (k % 9) * 110, (k // 9) * 110
        out.paste(sheet.crop((gx, gy, gx + 110, gy + 110)), ((n % NC) * 110, (n // NC) * 110))
    out.save(H / 'lookalike' / f'{run}_candidates.png')
    print(run, len(pc), 'tiles', len(tiles), 'split', sum(t['why'] == 'split' for t in tiles), 'cands', len(ids))
