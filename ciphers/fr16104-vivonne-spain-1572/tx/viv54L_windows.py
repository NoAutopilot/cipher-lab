#!/usr/bin/env python3
"""N7-VIV54L: the second look-alike instrument for ink 54 -- per-tile window montages, reusing tx/viv53L_windows.py (N7-VIV53L's
window/strip/boxes/DESC, imported, not copied) on images/ (f.173r-v crops, images/manifest.json).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv54L_windows.py PAGE     # f173r | f173v

Why: the first instrument (lookalike_pass.py packet prompt: id-only sheet + whole line crops, passC sequence shown) gave three echo
re-reads on ink 54 (VOID, NOTES N7-VIV54L), as it did four times on ink 53. Here every SPLIT tile of the packet (status split; one-pass
gaps are not re-read and stay UNSETTLED/M, PREREG-N7VIV54L addendum) gets a window, 6 per montage, candidates alphabetical, the
committed label never singled out. Writes tx/lookalike54/<PAGE>_win/*.png, viv54L_<PAGE>_splits_tiles.tsv, viv54L_<PAGE>_win_prompt.md.
"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv53L_windows as w53  # noqa: E402
w53.IMG = os.path.join(T, 'images')
LA = os.path.join(HERE, 'lookalike54')


def main():
    page = sys.argv[1]
    tiles = list(csv.DictReader(open(os.path.join(LA, f'viv54L_{page}_tiles.tsv')), delimiter='\t'))
    splits = [t for t in tiles if t['status'] == 'split']
    nline = {}
    for r in csv.DictReader(open(os.path.join(LA, 'align', page, 'passC.tsv')), delimiter='\t'):
        nline[f"{page}_{r['passage']}"] = nline.get(f"{page}_{r['passage']}", 0) + 1
    bx = {page: w53.boxes(page)}
    strips, wins = {}, []
    for t in splits:
        wins.append((f"{t['passage']}.{t['pos']}", w53.window(strips, bx, nline, f"{page}_{t['passage']}", int(t['pos']))))
    d = os.path.join(LA, f'{page}_win'); os.makedirs(d, exist_ok=True)
    pngs = w53.montage(wins, d, f'{page}_win')
    with open(os.path.join(LA, f'viv54L_{page}_splits_tiles.tsv'), 'w') as o:
        wr = csv.DictWriter(o, fieldnames=list(tiles[0]), delimiter='\t', lineterminator='\n'); wr.writeheader(); wr.writerows(splits)
    lines = []
    for t in splits:
        cand = sorted({x for x in t['candidates'].split(',') if x})
        cd = '; '.join(f"{c} = {w53.DESC.get(c, c.strip('{}') + ' (free description)')}" for c in cand)
        lines.append(f"{t['passage']}\t{t['pos']}\tbefore: {t['before']} | after: {t['after']}\tcandidates: {cd}")
    prompt = f"""# Look-alike re-read by window, 54L {page} (value-blind, second instrument)

{len(splits)} tiles. Each tile has its own window image: open the montages below IN ORDER (6 windows each, captioned in blue with
the tile id passage.pos). In each window the red ticks top and bottom mark the ESTIMATED position of the tile's sign (the estimate
can be off by 1-3 signs). Find the sign using the labels of the 3 signs before and after it (keyboard look-alike ids, described in
SIGNS.md), then decide which candidate's SHAPE it is. The candidate list is alphabetical; nothing tells you which is "right".

Montages: {', '.join(pngs)}

Answer one TSV row per tile, header: passage<TAB>pos<TAB>label<TAB>conf<TAB>second<TAB>note
  label = one candidate id, X_NEW if none fits, SPLIT:a|b if you cannot choose; conf H clear / M probable / L guess (use L whenever
  you could not find the sign in its window); second = runner-up or empty; note = the shape feature you SAW (e.g. "flat top bar").

Tiles (passage, pos, context, candidates):
""" + '\n'.join(lines) + '\n'
    open(os.path.join(LA, f'viv54L_{page}_win_prompt.md'), 'w').write(prompt)
    print(page, len(splits), 'split tiles,', len(pngs), 'montages')


if __name__ == '__main__':
    main()
