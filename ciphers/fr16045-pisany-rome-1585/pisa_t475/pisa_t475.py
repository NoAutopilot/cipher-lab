"""PISA-T475 (11 Oct 2026, pisa_t475/PREREG-PISA-T475.md): third blind reader on the 3 f.275r T45/T47/T57 tokens PISA-275R left
UNSETTLED, with the UNA-PISA instrument unchanged (22-cell sheet, known-answer tiles, prompt, parser).
  python3 ciphers/fr16045-pisany-rome-1585/pisa_t475/pisa_t475.py build        tiles + prompt (pisa_t475/tok/, blind/f275r/)
  python3 ciphers/fr16045-pisany-rome-1585/pisa_t475/pisa_t475.py score [--check]  blind/reply_f275r.txt -> pisa_t475/result.tsv
Run from the repository root."""
import sys, os, random, csv
from PIL import Image
sys.path.insert(0, 'ciphers/fr16045-pisany-rome-1585/una_pisa')
import una_pisa as UP, strips
D = UP.D; H = f'{D}/pisa_t475'; SEED = 20261011 + 75
TARGETS = [('L10', '12'), ('L11', '19'), ('L15', '27')]
VALUE = {'T45': 'o', 'T47': 'm', 'T31': 'm', 'T11': 'm', 'T57': 'la'}

def prior():
    """PISA-275R's read per token id: (best, second, conf)."""
    return {r['id']: (r['best_cell'], r['second_cell'], r['conf']) for r in csv.DictReader(open(f'{D}/una_pisa/result.tsv'), delimiter='\t')
            if r.get('stage') == 'f275r' and r.get('role') == 'test'}

def tiles_for():
    pos = {(r['line'], r['pos']): r for r in csv.DictReader(open(f'{D}/una_pisa/tokens_pos.tsv'), delimiter='\t') if r['page'] == 'f275r'}
    items = [(cid, crop, ans, 'control') for cid, crop, ans in UP.CONTROLS]
    for line, p in TARGETS:
        items.append((f'f275r_{line}_p{p}', f'{H}/tok/f275r_{line}_p{p}.png', pos[(line, p)]['label'], 'test'))
    rr = random.Random(SEED); rr.shuffle(items)
    return [(f'Q{i+1:02d}',) + it for i, it in enumerate(items)]

def build():
    os.makedirs(f'{H}/tok', exist_ok=True); os.makedirs(f'{H}/blind/f275r', exist_ok=True)
    pos = {(r['line'], r['pos']): r for r in csv.DictReader(open(f'{D}/una_pisa/tokens_pos.tsv'), delimiter='\t') if r['page'] == 'f275r'}
    for line, p in TARGETS:
        s = strips.strip('f275r', line); x = int(pos[(line, p)]['x_centre_strip'])
        s.crop((x - 60, 0, x + 60, s.size[1])).save(f'{H}/tok/f275r_{line}_p{p}.png')
    rows = tiles_for()
    with open(f'{H}/blind/f275r/tiles_map.tsv', 'w') as f:
        f.write('qid\tid\tcrop\tanswer_or_label\trole\n')
        for q, cid, crop, ans, role in rows:
            im = Image.open(crop).convert('L'); im = im.resize((im.size[0] * 2, im.size[1] * 2), Image.LANCZOS)
            im.save(f'{H}/blind/f275r/{q}.png'); f.write(f'{q}\t{cid}\t{crop}\t{ans}\t{role}\n')
    qs = ' '.join(r[0] for r in rows)
    prompt = f"""You are comparing handwritten cipher signs from a 16th-century letter against the cells of a printed cipher table.
Files: the table sheet {UP.U}/blind/cells_sheet.png shows 22 table cells, each under a letter A-V (cells were cut at low resolution;
some cells have a circle drawn round the sign). Token tiles: {', '.join(f'{H}/blind/f275r/{r[0]}.png' for r in rows)}.
Each token tile is cut from a line of the letter; the sign to identify is the one in the horizontal CENTRE of the tile (neighbouring
signs may show at the edges). Look at every image. For each tile, say which table cell's sign it is. Ignore any circle drawn round a
cell sign when matching shape, but note it.
Reply with exactly one line per tile, in this format and nothing else after the lines:
Qnn<TAB>best=<letter><TAB>second=<letter><TAB>confidence=<high|medium|low><TAB><short description of the centre sign>
Tiles: {qs}"""
    open(f'{H}/blind/f275r/prompt.md', 'w').write(prompt + '\n'); print(prompt)

def score():
    m = UP.cell_map(); pr = prior(); rows = []; k = []
    rep = UP.parse(f'{H}/blind/reply_f275r.txt')
    for r in csv.DictReader(open(f'{H}/blind/f275r/tiles_map.tsv'), delimiter='\t'):
        b, s, c = rep.get(r['qid'], ('', '', ''))
        bc, sc = m.get(b, '?'), m.get(s, '?')
        if r['role'] == 'control':
            v = 'HIT' if bc == r['answer_or_label'] else 'MISS'; k.append(v); p0 = ('', '', ''); two = ''
        else:
            p0 = pr[r['id']]; lab = r['answer_or_label']
            v = f'SETTLED-{bc}' if c in ('high', 'medium') else 'UNSETTLED'
            if v == 'UNSETTLED' or bc not in p0[:2]: two = 'UNSETTLED'
            elif bc == lab or (VALUE.get(bc) and VALUE.get(bc) == VALUE.get(lab)): two = f'SETTLED-BY-TWO-{bc} (no edit)'
            else: two = f'SETTLED-BY-TWO-{bc} (relabel candidate)'
        rows.append([r['qid'], r['id'], r['role'], r['answer_or_label'], bc, sc, c, v, p0[0], p0[1], p0[2], two])
    hit = k.count('HIT')
    out = ['qid\tid\trole\tanswer_or_label\tbest_cell\tsecond_cell\tconf\tverdict\tp275r_best\tp275r_second\tp275r_conf\tthird_reader_rule']
    out += ['\t'.join(x) for x in rows] + [f'# f275r: GK {hit}/{len(k)} {"PASS" if hit >= 4 else "FAIL (NON-TEST)"}']
    return '\n'.join(out) + '\n'

if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == 'build': build()
    elif a and a[0] == 'score':
        txt = score(); p = f'{H}/result.tsv'
        if '--check' in a:
            ok = os.path.exists(p) and open(p).read() == txt; print('up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
        open(p, 'w').write(txt); print(txt)
    else: print(__doc__); sys.exit(1)
