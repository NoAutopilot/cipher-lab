#!/usr/bin/env python3
"""Inputs for `sign_sorter.py --oddness-audit` on the Birago no.87 known answer (MQS-SORTER, 9 Oct 2026; rule in
tools/tests/PREREG-MQS-SORTER.md section A). Read-only on ciphers/. Writes signs.tsv + labels.tsv into OUT_DIR:
a tile is clean when its box<->token op is 1:1 and the printed 1572 key value of its line-read sign equals the clerk-sheet letter.

  python3 tools/tests/oddness_no87_inputs.py OUT_DIR
"""
import csv, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
B = os.path.join(ROOT, 'ciphers', 'nevers-birago-fr3251-1572')
rd = lambda p: list(csv.DictReader(open(p, newline=''), delimiter='\t'))


def main(out):
    key = {r['sign']: r['value'].strip().lower() for r in rd(os.path.join(B, 'harvest', 'key_1572_sheet.tsv'))}
    box = {r['sid']: r for r in rd(os.path.join(B, 'atlas', 'signs.tsv'))}
    # --map FILE (BOXMAP-RESCORE, 11 Oct 2026): a map with the old map's truth column (atlas/no87_map.py --compat OUT); default the old map
    mp = sys.argv[sys.argv.index('--map') + 1] if '--map' in sys.argv else os.path.join(B, 'atlas', 'no87_box_token.tsv')
    clean = [r for r in rd(mp)
             if r['op'] == '1:1' and r['sid'] in box and key.get(r['sign']) == r['truth'].strip().lower()]
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, 'signs.tsv'), 'w') as f:
        f.write('sid\tpage\tx\ty\tw\th\n' + ''.join(f"{r['sid']}\t{box[r['sid']]['page']}\t{box[r['sid']]['x']}\t{box[r['sid']]['y']}\t{box[r['sid']]['w']}\t{box[r['sid']]['h']}\n" for r in clean))
    with open(os.path.join(out, 'labels.tsv'), 'w') as f:
        f.write('sid\tsign\tfamily\n' + ''.join(f"{r['sid']}\t{r['sign']}\t{r['sign']}\n" for r in clean))
    print(f'{len(clean)} clean tiles, {len({r["sign"] for r in clean})} piles -> {out}')


if __name__ == '__main__':
    pos = [x for i, x in enumerate(sys.argv[1:], 1) if x != '--map' and sys.argv[i - 1] != '--map']
    main(pos[0] if pos else '.')
