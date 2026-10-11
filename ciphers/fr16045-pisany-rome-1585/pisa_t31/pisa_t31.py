"""PISA-T31 (11 Oct 2026, PREREG-PISA-T31.md): third blind reader on the 14 key86 T31 tokens R9-PIS2 left UNSETTLED, with the
UNA-PISA instrument unchanged (22-cell sheet, known-answer tiles, prompt, parser).
  python3 pisa_t31/pisa_t31.py build LEAF      tiles + prompt for f244r or f275r (writes pisa_t31/blind/LEAF/)
  python3 pisa_t31/pisa_t31.py score [--check] blind/reply_*.txt -> pisa_t31/result.tsv (GK, settle, third-reader rule)
Run from the repository root."""
import sys, os, random, csv
from PIL import Image
sys.path.insert(0, 'ciphers/fr16045-pisany-rome-1585/una_pisa')
import una_pisa as UP
D = UP.D; H = f'{D}/pisa_t31'; SEED = 20261011
LEAVES = {'f244r': 1, 'f275r': 2}

def targets():
    return [r for r in csv.DictReader(open(f'{D}/pis2/t31_tokens.tsv'), delimiter='\t') if r['verdict'] == 'UNSETTLED']

def tiles_for(leaf):
    items = [(cid, crop, ans, 'control', '', '') for cid, crop, ans in UP.CONTROLS]
    for r in targets():
        if r['leaf'] == leaf:
            items.append((f"{leaf}_{r['line']}_i{r['tok_index']}", f"{D}/pis2/tok/{leaf}_{r['line']}_i{r['tok_index']}.jpg", 'T31',
                          'test', r['reader_top'], r['reader_second']))
    rr = random.Random(SEED + LEAVES[leaf]); rr.shuffle(items)
    return [(f'Q{i+1:02d}',) + it for i, it in enumerate(items)]

def build(leaf):
    os.makedirs(f'{H}/blind/{leaf}', exist_ok=True); rows = tiles_for(leaf)
    with open(f'{H}/blind/{leaf}/tiles_map.tsv', 'w') as f:
        f.write('qid\tid\tcrop\tanswer_or_label\trole\tr9_top\tr9_second\n')
        for q, cid, crop, ans, role, t, s in rows:
            im = Image.open(crop).convert('L'); im = im.resize((im.size[0] * 2, im.size[1] * 2), Image.LANCZOS)
            im.save(f'{H}/blind/{leaf}/{q}.png'); f.write(f'{q}\t{cid}\t{crop}\t{ans}\t{role}\t{t}\t{s}\n')
    qs = ' '.join(r[0] for r in rows)
    prompt = f"""You are comparing handwritten cipher signs from a 16th-century letter against the cells of a printed cipher table.
Files: the table sheet {UP.U}/blind/cells_sheet.png shows 22 table cells, each under a letter A-V (cells were cut at low resolution;
some cells have a circle drawn round the sign). Token tiles: {', '.join(f'{H}/blind/{leaf}/{r[0]}.png' for r in rows)}.
Each token tile is cut from a line of the letter; the sign to identify is the one in the horizontal CENTRE of the tile (neighbouring
signs may show at the edges). Look at every image. For each tile, say which table cell's sign it is. Ignore any circle drawn round a
cell sign when matching shape, but note it.
Reply with exactly one line per tile, in this format and nothing else after the lines:
Qnn<TAB>best=<letter><TAB>second=<letter><TAB>confidence=<high|medium|low><TAB><short description of the centre sign>
Tiles: {qs}"""
    open(f'{H}/blind/{leaf}/prompt.md', 'w').write(prompt + '\n'); print(prompt)

VALUE_M = {'T31', 'T47', 'T11'}

def score():
    m = UP.cell_map(); rows = []; summ = []
    for leaf in LEAVES:
        rp = f'{H}/blind/reply_{leaf}.txt'
        if not os.path.exists(rp): continue
        rep = UP.parse(rp); k = []
        for r in csv.DictReader(open(f'{H}/blind/{leaf}/tiles_map.tsv'), delimiter='\t'):
            b, s, c = rep.get(r['qid'], ('', '', ''))
            bc, sc = m.get(b, '?'), m.get(s, '?')
            if r['role'] == 'control':
                v = 'HIT' if bc == r['answer_or_label'] else 'MISS'; two = ''; k.append(v)
            else:
                v = f'SETTLED-{bc}' if c in ('high', 'medium') else 'UNSETTLED'
                if v == 'UNSETTLED' or bc not in (r['r9_top'], r['r9_second']): two = 'UNSETTLED'
                elif bc == 'T31': two = 'SETTLED-BY-TWO-T31'
                elif bc in VALUE_M: two = f'SETTLED-BY-TWO-{bc} (value-neutral)'
                else: two = f'SETTLED-BY-TWO-{bc} (relabel candidate)'
            rows.append([leaf, r['qid'], r['id'], r['role'], r['answer_or_label'], bc, sc, c, v, r['r9_top'], r['r9_second'], two])
        hit = k.count('HIT'); summ.append(f'# {leaf}: GK {hit}/{len(k)} {"PASS" if hit >= 4 else "FAIL (NON-TEST for this leaf)"}')
    lines = ['leaf\tqid\tid\trole\tanswer_or_label\tbest_cell\tsecond_cell\tconf\tverdict\tr9_top\tr9_second\tthird_reader_rule']
    return '\n'.join(lines + ['\t'.join(x) for x in rows] + summ) + '\n'

if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == 'build': build(a[1])
    elif a and a[0] == 'score':
        txt = score(); p = f'{H}/result.tsv'
        if '--check' in a:
            ok = os.path.exists(p) and open(p).read() == txt; print('up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
        open(p, 'w').write(txt); print(txt)
    else: print(__doc__); sys.exit(1)
