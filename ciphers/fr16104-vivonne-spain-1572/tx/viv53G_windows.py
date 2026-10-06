#!/usr/bin/env python3
"""R7A-VIV53 (6 Oct 2026): window montages for the ink 53 one-reader GAP tiles plus agreed-sign decoys, PREREG-R7VIV53G.md (i).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv53G_windows.py PAGE

Gap tiles = rows of tx/lookalike53L/<PAGE>/53L_<PAGE>_tiles.tsv with status 'gap' (deduplicated on passage, pos). Decoys = 12 'agree'
rows of that page's agreement.tsv drawn with random.Random("R7VIV53G-decoy" + PAGE); candidates = agreed label + its two top partners
in tx/lookalike53L/confusion.tsv. Every item gets NONE as a candidate. Items are shuffled together (random.Random("R7VIV53G-order" +
PAGE)) and captioned "item N"; the answer key (kind gap|decoy, passage, pos, label) goes to tx/lookalike53G/<PAGE>/items.tsv, which
the re-reader is never shown. Windows are cut with tx/viv53L_windows.py's window()/montage() unchanged (the N7-VIV53L instrument).
Writes tx/lookalike53G/<PAGE>/win/*.png (not committed), items.tsv and 53G_<PAGE>_prompt.md.
"""
import csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import viv53L_windows as vw  # noqa: E402

L53 = os.path.join(HERE, 'lookalike53L')
NONE_DESC = 'NONE = no separate sign at this point (the ticks fall on part of a neighbouring sign, a flourish, or blank space)'


def partners():
    p = {}
    for r in csv.DictReader(open(os.path.join(L53, 'confusion.tsv')), delimiter='\t'):
        for a, b in ((r['label_a'], r['label_b']), (r['label_b'], r['label_a'])):
            p.setdefault(a, []).append((int(r['n']), b))
    return {a: [b for _, b in sorted(v, key=lambda x: -x[0])[:2]] for a, v in p.items()}


def items(page):
    d = os.path.join(L53, page)
    tiles = list(csv.DictReader(open(os.path.join(d, f'53L_{page}_tiles.tsv')), delimiter='\t'))
    pc = list(csv.DictReader(open(os.path.join(d, 'passD.tsv')), delimiter='\t'))
    seq = {}
    for r in pc:
        seq.setdefault(r['passage'], []).append(r['sign_id'])
    seen, out = set(), []
    for t in tiles:
        if t['status'] != 'gap' or (t['passage'], t['pos']) in seen:
            continue
        seen.add((t['passage'], t['pos']))
        out.append(dict(kind='gap', passage=t['passage'], pos=t['pos'], label=t['passC'],
                        cands=sorted({x for x in t['candidates'].split(',') if x} | {'NONE'})))
    P = partners()
    ag = [r for r in csv.DictReader(open(os.path.join(d, 'agreement.tsv')), delimiter='\t') if r['status'] == 'agree'
          and r['merged'] and int(r['posA']) <= len(seq.get(r['passage'], []))
          and seq[r['passage']][int(r['posA']) - 1] == r['merged']]
    ag = sorted({(r['passage'], r['posA']): r for r in ag}.values(), key=lambda r: (r['passage'], int(r['posA'])))
    for r in random.Random('R7VIV53G-decoy' + page).sample(ag, 12):
        out.append(dict(kind='decoy', passage=r['passage'], pos=r['posA'], label=r['merged'],
                        cands=sorted({r['merged'], *P.get(r['merged'], []), 'NONE'})))
    random.Random('R7VIV53G-order' + page).shuffle(out)
    for i, it in enumerate(out, 1):
        it['item'] = i
    return out, seq


def main():
    page = sys.argv[1]
    its, seq = items(page)
    d = os.path.join(HERE, 'lookalike53G', page)
    os.makedirs(os.path.join(d, 'win'), exist_ok=True)
    nline = {k: len(v) for k, v in seq.items()}
    bx = {page: vw.boxes(page)}
    strips, wins, lines = {}, [], []
    for it in its:
        wins.append((f"item {it['item']}", vw.window(strips, bx, nline, it['passage'], int(it['pos']))))
        s, p = seq[it['passage']], int(it['pos'])
        cd = '; '.join(NONE_DESC if c == 'NONE' else f"{c} = {vw.DESC.get(c, c.strip('{}') + ' (free description)')}"
                       for c in it['cands'])
        lines.append(f"{it['item']}\tbefore: {' '.join(s[max(0, p - 4):p - 1])} | after: {' '.join(s[p:p + 3])}\tcandidates: {cd}")
    pngs = vw.montage(wins, os.path.join(d, 'win'), f'{page}_g')
    with open(os.path.join(d, 'items.tsv'), 'w') as o:
        o.write('item\tkind\tpassage\tpos\tlabel\tcandidates\n')
        for it in its:
            o.write(f"{it['item']}\t{it['kind']}\t{it['passage']}\t{it['pos']}\t{it['label']}\t{','.join(it['cands'])}\n")
    prompt = f"""# Window re-read, 53G {page} (value-blind)

{len(its)} items. Open the montages below IN ORDER (6 windows each, captioned in blue "item N"). In each window the red ticks top and
bottom mark the ESTIMATED position of the item's sign (can be off by 1-3 signs). Find the sign using the labels of the 3 signs
before and after it (keyboard look-alike ids), then decide which candidate's SHAPE it is -- or NONE if there is no separate sign
there (e.g. the "sign" is really a stroke of a neighbour, a flourish, or blank). Candidates are alphabetical; nothing tells you
which is right. Some items are checks with a known answer.

Montages: {', '.join(pngs)}

Answer one TSV row per item, header: item<TAB>label<TAB>conf<TAB>second<TAB>note
  label = one candidate id (or NONE), X_NEW if a sign is there but no candidate fits, SPLIT:a|b if you cannot choose;
  conf H clear / M probable / L guess (L whenever you could not find the place); second = runner-up or empty;
  note = the shape feature you SAW (a few words).

Items (item, context, candidates):
""" + '\n'.join(lines) + '\n'
    open(os.path.join(d, f'53G_{page}_prompt.md'), 'w').write(prompt)
    print(page, sum(i['kind'] == 'gap' for i in its), 'gap +', sum(i['kind'] == 'decoy' for i in its), 'decoys,', len(pngs), 'montages')


if __name__ == '__main__':
    main()
