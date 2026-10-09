#!/usr/bin/env python3
"""GLY-11106 (8 Oct 2026): sign-sorter inputs for WVO 11106 p.2 from the glyph atlas (atlas/) and the reconciled
transcription. Writes sorter/labels.tsv (sid, sign, family, cluster), sorter/focus.tsv (box sid, question) and
sorter/cipher_lines.tsv. A box's pile is the reconciled label of the position atlas/map_tx.py matched it to; a box
carrying two joined signs goes to pile 'joined' (the person cuts or names it), an unmatched box to its shape cluster's
majority pile when that cluster's firm matches give one label >= 50% and >= 3 times (family 'shape-guess'), else to
'unmatched', a
fragment (dot, descender piece) to 'fragment'. Each tx/focus.tsv question (line:pos) points at the box matched to that
position; a position with no box of its own is listed in sorter/focus_unplaced.tsv. Run from anywhere.

--groups (BERGH-SORT, 9 Oct 2026): build from atlas/group_sign.tsv's whole-line group reads (jobs BERGH-ALL1 + BERGH-ALL2, one
row per atlas box, 875) instead of the alignment. An agreed group (same strip, same group in both passes, same labels) becomes ONE
tile: sorter/signs_grp.tsv carries the union box under a group sid (the member sids joined by '+', e.g. L01_01_001+002), and
sorter/marks_grp.tsv re-keys the members' marks to it. Pile = the agreed label ('FRAG' -> 'fragment'; a label of two or more signs,
e.g. "p g", -> pile "p+g", family 'multi'). Each split box stays its own tile in pile 'split' and is a "Check these first" question
quoting both passes; the NEW1 box (both passes: digit 1 with an overbar, not on tx/signlist.md) is a question too. The
alignment-mode tx/focus.tsv questions are not carried (their boxes came from the map BERGH-STRIP/GLY-11106 showed wrong)."""
import csv, sys
from pathlib import Path
here = Path(__file__).resolve().parent; root = here.parent
if '--groups' in sys.argv[1:]:
    from collections import defaultdict
    sg = {r['sid']: r for r in csv.DictReader(open(root / 'atlas/signs.tsv'), delimiter='\t')}
    cl = {r['id']: r['cluster'] for r in csv.DictReader(open(root / 'atlas/clusters.tsv'), delimiter='\t') if r['kind'] == 'sign'}
    rows = [r for r in csv.DictReader(open(root / 'atlas/group_sign.tsv'), delimiter='\t') if r['job'] in ('BERGH-ALL1', 'BERGH-ALL2')]
    assert len(rows) == len({r['sid'] for r in rows}) == len(sg), 'group_sign.tsv whole-line rows must cover every atlas box once'
    grp, tiles, foc = defaultdict(list), [], []
    for r in rows:
        if r['status'] == 'agreed': grp[(r['strip'], r['groupA'])].append(r)
        else: tiles.append(([r['sid']], 'split', 'split'))
    for (strip, g), mem in grp.items():
        lab = mem[0]['agreed_label']
        assert all(m['agreed_label'] == lab for m in mem) and len(mem) == len(g.split('+')), (strip, g)
        if lab == 'FRAG': pile, f = 'fragment', 'other'
        elif ' ' in lab: pile, f = lab.replace(' ', '+'), 'multi'
        else: pile, f = lab, ('digit' if lab[:1].isdigit() else 'letter' if lab[:1].isalpha() else 'other')
        tiles.append((sorted(m['sid'] for m in mem), pile, f))
    gsid = lambda ms: ms[0] + ''.join('+' + m.rsplit('_', 1)[1] for m in ms[1:])
    owner = {m: gsid(ms) for ms, _, _ in tiles for m in ms}
    out = []
    for ms, pile, f in tiles:
        b = [sg[m] for m in ms]; x0 = min(int(s['x']) for s in b); y0 = min(int(s['y']) for s in b)
        x1 = max(int(s['x']) + int(s['w']) for s in b); y1 = max(int(s['y']) + int(s['h']) for s in b)
        out.append((gsid(ms), b[0]['page'], b[0]['line'], x0, y0, x1 - x0, y1 - y0, pile, f, cl.get(ms[0], ''), len(ms)))
    out.sort(key=lambda t: (t[1], t[3]))
    with open(here / 'signs_grp.tsv', 'w') as o:
        o.write('sid\tpage\tline\tx\ty\tw\th\tboxes\n'); o.writelines(f'{t[0]}\t{t[1]}\t{t[2]}\t{t[3]}\t{t[4]}\t{t[5]}\t{t[6]}\t{t[10]}\n' for t in out)
    with open(here / 'labels.tsv', 'w') as o:
        o.write('sid\tsign\tfamily\tcluster\n'); o.writelines(f'{t[0]}\t{t[7]}\t{t[8]}\t{t[9]}\n' for t in out)
    mk = list(csv.DictReader(open(root / 'atlas/marks.tsv'), delimiter='\t'))
    with open(here / 'marks_grp.tsv', 'w') as o:
        o.write('mid\tpage\tline\tx\ty\tw\th\tsid\n')
        o.writelines(f"{m['mid']}\t{m['page']}\t{m['line']}\t{m['x']}\t{m['y']}\t{m['w']}\t{m['h']}\t{owner[m['sid']]}\n" for m in mk if m['sid'] in owner)
    for r in sorted(rows, key=lambda r: r['sid']):
        if r['status'] == 'split':
            ga = '' if r['groupA'] == r['num'] else f" (with boxes {r['groupA']})"; gb = '' if r['groupB'] == r['num'] else f" (with boxes {r['groupB']})"
            foc.append((r['sid'], f"{r['sid']} ({r['job']}, strip {r['strip']} box {r['num']}): A read {r['labelA']}{ga}, B read {r['labelB']}{gb}: which sign, and does it belong with its neighbours?"))
        elif r['agreed_label'] == 'NEW1':
            foc.append((owner[r['sid']], f"{r['sid']}: both passes NEW1, a digit 1 with an overbar (not on tx/signlist.md): which sign?"))
    with open(here / 'focus.tsv', 'w') as o:
        o.write('sid\tquestion\n'); o.writelines(f'{a}\t{b}\n' for a, b in foc)
    with open(here / 'focus_unplaced.tsv', 'w') as o:
        o.write('tx_sid\tquestion\n')
    with open(here / 'cipher_lines.tsv', 'w') as o:
        o.write('page\n'); o.writelines(f'L{i:02d}\n' for i in range(1, 23))
    n_ag = sum(1 for r in rows if r['status'] == 'agreed'); n_sp = len(rows) - n_ag
    print(f"{len(rows)} boxes: {n_ag} agreed in {len(grp)} group tiles, {n_sp} split boxes as single tiles; {len(out)} tiles, "
          f"{len({t[7] for t in out})} piles, {len(foc)} focus questions ({n_sp} split + NEW1)")
    sys.exit(0)
cl = {r['id']: r['cluster'] for r in csv.DictReader(open(root / 'atlas/clusters.tsv'), delimiter='\t') if r['kind'] == 'sign'}
bm = list(csv.DictReader(open(root / 'atlas/boxmap.tsv'), delimiter='\t'))
fam = lambda s: 'digit' if s[:1].isdigit() else ('letter' if s[:1].isalpha() else 'other')
from collections import Counter, defaultdict
maj = defaultdict(Counter)
for r in bm:
    if r['firm'] == '1' and r['kind'] == 'cipher': maj[cl.get(r['sid'])][r['label']] += 1
def guess(c):
    if not maj[c]: return None
    l, n = maj[c].most_common(1)[0]
    return l if n >= 3 and n / sum(maj[c].values()) >= 0.5 else None
lab, where = [], {}
for r in bm:
    if r['kind'] == 'fragment': s, f = 'fragment', 'other'
    elif not r['pos']:
        g = guess(cl.get(r['sid'])); s, f = (g, 'shape-guess') if g else ('unmatched', 'other')
    elif r['joined'] == '1': s, f = 'joined', 'other'
    elif r['kind'] == 'struck': s, f = r['label'], 'struck'
    else: s, f = r['label'], fam(r['label'])
    lab.append((r['sid'], s, f, cl.get(r['sid'], '')))
    for p in r['pos'].split('+'):
        if p: where.setdefault(f"{r['line']}:{p}", (r['sid'], r['joined'] == '1'))
with open(here / 'labels.tsv', 'w') as o:
    o.write('sid\tsign\tfamily\tcluster\n'); o.writelines('\t'.join(x) + '\n' for x in lab)
foc, unpl = [], []
for q in csv.DictReader(open(root / 'tx/focus.tsv'), delimiter='\t'):
    hit = where.get(q['sid']); text = q['question'].split(' (crop')[0]
    if hit: foc.append((hit[0], f"{q['sid']}: {text}" + (' (box holds two signs: cut it first)' if hit[1] else '')))
    else: unpl.append((q['sid'], text))
with open(here / 'focus.tsv', 'w') as o:
    o.write('sid\tquestion\n'); o.writelines(f'{a}\t{b}\n' for a, b in foc)
with open(here / 'focus_unplaced.tsv', 'w') as o:
    o.write('tx_sid\tquestion\n'); o.writelines(f'{a}\t{b}\n' for a, b in unpl)
with open(here / 'cipher_lines.tsv', 'w') as o:
    o.write('page\n'); o.writelines(f'L{i:02d}\n' for i in range(1, 23))
print(f'{len(lab)} tiles, {len(foc)} focus tiles, {len(unpl)} focus positions without a box of their own')
