"""Build the owner's "which shorthand?" page (SHORTHAND-PAGE, 5 Oct 2026, account 3). Disk only, no network.

Rows: Armstrong's mark types R1-R7 (images/shorthand/INVENTORY_reconciled.tsv), three padded one-mark tiles each
(exemplars.tsv, cut by tiles.py from the sorter boxes). Columns: five period alphabets under BLIND labels A-E, cut
into per-letter cells by cells.py. The owner picks the sign that looks like each mark, or "nothing similar", then gives
a family verdict per system. Answers go to the page db: collection `picks` (doc `R1-A`: type, system, pick (cell
index or -1 for nothing similar), letter, updated) and `verdicts` (doc `A`: verdict, note, updated).
Usage (repo root): python3 ciphers/armstrong-madison-1808/sorter/family/build_family_page.py OUT.html
"""
import base64, csv, io, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cells import cut_cells, ROOT
from tiles import tiles

def uri(im, h=None, q=80):
    im = im.convert('L')
    if h and im.height > h:
        im = im.resize((round(im.width * h / im.height), h))
    b = io.BytesIO(); im.save(b, 'JPEG', quality=q, optimize=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

def main(out):
    inv = {r['id']: r for r in csv.DictReader(open(ROOT + 'images/shorthand/INVENTORY_reconciled.tsv'), delimiter='\t')}
    plain = {'R1': 'Low wave on the line', 'R2': 'Loop with a tail, like a 3', 'R3': 'Back-curving hook, like a 5',
             'R4': 'Small hook, like a little 2', 'R5': 'Short bar', 'R6': 'Single dot',
             'R7': 'Long slash (usually with a dot beside it)'}
    types = []
    for t, sid, im in tiles():
        if not types or types[-1]['id'] != t:
            types.append({'id': t, 'name': plain[t], 'count': int(inv[t]['count']),
                          'share': inv[t]['share_pct'], 'tiles': []})
        types[-1]['tiles'].append({'sid': sid, 'src': uri(im, 150)})
    systems = []
    for k in 'ABCDE':
        systems.append({'id': k, 'cells': [{'letter': l, 'src': uri(c, 84)} for l, c in cut_cells(k)]})
    tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'family_template.html')).read()
    html = tpl.replace('/*TYPES*/[]', json.dumps(types)).replace('/*SYSTEMS*/[]', json.dumps(systems))
    open(out, 'w').write(html)
    print(out, len(html) // 1024, 'KB;', len(types), 'mark types,', sum(len(s['cells']) for s in systems), 'cells')

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'which_shorthand.html')
