"""UNA-PISA (9 Oct 2026): per-token crop compare of key86 tokens against the 688 px table cells, PREREG-UNA-PISA.md.
  python3 una_pisa/una_pisa.py build STAGE      cells sheet + shuffled tiles + prompt for stage 1 (controls) or a page
  python3 una_pisa/una_pisa.py score [--check]  parse blind/reply_*.txt -> result.tsv (gate GK, per-token settle rule)
Run from the repository root. UNA_IMG=<dir> (PISA-275R, 9 Oct 2026): token crops <dir>/tok/ and tiles <dir>/blind/<stage>/
for pages whose crops are not committed (f275r; images stay out of the public repository)."""
import sys, os, random, re, csv
from PIL import Image, ImageDraw
D = 'ciphers/fr16045-pisany-rome-1585'; U = f'{D}/una_pisa'
IMG = os.environ.get('UNA_IMG', U)
CELLS = 'T45 T47 T57 T13 T33 T11 T31 T19 T38 T46 T51 T06 T27 T42 T12 T32 T48 T36 T17 T49 T16 T35'.split()
SEED = 20261009
CONTROLS = [  # id, crop, answer cell
    ('K-T36a', f'{D}/pis2/tok/f275r_L09_i3.jpg', 'T36'), ('K-T36b', f'{D}/pis2/tok/f275r_L14_i28.jpg', 'T36'),
    ('K-T17', f'{D}/pissd/tok/f302v_L02_i16.jpg', 'T17'), ('K-T16', f'{D}/pissd/tok/f302v_L02_i15.jpg', 'T16'),
    ('K-T46', f'{D}/pissd/tok/f302v_L03_i6.jpg', 'T46')]
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUV'

def cell_map():
    r = random.Random(SEED); cells = CELLS[:]; r.shuffle(cells)
    return dict(zip(LETTERS, cells))

def build_sheet():
    m = cell_map(); S = 4; w, h = 32 * S, 26 * S
    sheet = Image.new('L', (6 * (w + 20) + 20, 4 * (h + 40) + 20), 255); d = ImageDraw.Draw(sheet)
    for k, (L, T) in enumerate(m.items()):
        c = Image.open(f'{U}/cells/k_{T}_L01.jpg').convert('L').resize((w, h), Image.LANCZOS)
        x, y = 20 + (k % 6) * (w + 20), 20 + (k // 6) * (h + 40)
        sheet.paste(c, (x, y + 22)); d.text((x + w // 2 - 4, y + 4), L, fill=0)
    sheet.save(f'{U}/blind/cells_sheet.png')
    with open(f'{U}/cells_map.tsv', 'w') as f:
        f.write('letter\tcell\n' + ''.join(f'{L}\t{T}\n' for L, T in m.items()))

def tiles_for(stage):
    items = [(cid, crop, ans, 'control') for cid, crop, ans in CONTROLS]
    if stage != 'controls':
        for row in csv.DictReader(open(f'{U}/tokens_pos.tsv'), delimiter='\t'):
            if row['page'] == stage and row['located'] != 'not-located':
                items.append((f"{row['page']}_{row['line']}_p{row['pos']}", f"{IMG if stage == 'f275r' else U}/tok/{row['page']}_{row['line']}_p{row['pos']}.jpg", row['label'], 'test'))
    idx = {'controls': 0, 'f275r': 1, 'f301v': 2, 'f302v': 3}[stage]
    r = random.Random(SEED + idx); r.shuffle(items)
    return [(f'Q{i+1:02d}',) + it for i, it in enumerate(items)]

def build(stage):
    T = IMG if stage == 'f275r' else U
    os.makedirs(f'{U}/blind/{stage}', exist_ok=True); os.makedirs(f'{T}/blind/{stage}', exist_ok=True); build_sheet()
    rows = tiles_for(stage)
    with open(f'{U}/blind/{stage}/tiles_map.tsv', 'w') as f:
        f.write('qid\tid\tcrop\tanswer_or_label\trole\n')
        for q, cid, crop, ans, role in rows:
            im = Image.open(crop).convert('L'); im = im.resize((im.size[0] * 2, im.size[1] * 2), Image.LANCZOS)
            im.save(f'{T}/blind/{stage}/{q}.png'); f.write(f'{q}\t{cid}\t{crop}\t{ans}\t{role}\n')
    qs = ' '.join(r[0] for r in rows)
    prompt = f"""You are comparing handwritten cipher signs from a 16th-century letter against the cells of a printed cipher table.
Files: the table sheet {U}/blind/cells_sheet.png shows 22 table cells, each under a letter A-V (cells were cut at low resolution;
some cells have a circle drawn round the sign). Token tiles: {', '.join(f'{T}/blind/{stage}/{r[0]}.png' for r in rows)}.
Each token tile is cut from a line of the letter; the sign to identify is the one in the horizontal CENTRE of the tile (neighbouring
signs may show at the edges). Look at every image. For each tile, say which table cell's sign it is. Ignore any circle drawn round a
cell sign when matching shape, but note it.
Reply with exactly one line per tile, in this format and nothing else after the lines:
Qnn<TAB>best=<letter><TAB>second=<letter><TAB>confidence=<high|medium|low><TAB><short description of the centre sign>
Tiles: {qs}"""
    open(f'{U}/blind/{stage}/prompt.md', 'w').write(prompt + '\n')
    print(prompt)

def parse(path):
    out = {}
    for line in open(path):
        m = re.match(r'\s*(Q\d\d)\s+best=([A-V])\s+second=([A-V-]?)\s+confidence=(high|medium|low)', line.replace('\t', ' '))
        if m: out[m.group(1)] = m.groups()[1:]
    return out

def score():
    m = cell_map(); rows = []
    for stage in ['controls', 'f275r', 'f301v', 'f302v']:
        rp = f'{U}/blind/reply_{stage}.txt'
        if not os.path.exists(rp): continue
        rep = parse(rp)
        for r in csv.DictReader(open(f'{U}/blind/{stage}/tiles_map.tsv'), delimiter='\t'):
            b, s, c = rep.get(r['qid'], ('', '', ''))
            bc, sc = m.get(b, '?'), m.get(s, '?')
            if r['role'] == 'control': verdict = 'HIT' if bc == r['answer_or_label'] else 'MISS'
            else: verdict = f'SETTLED-{bc}' if c in ('high', 'medium') else 'UNSETTLED'
            rows.append([stage, r['qid'], r['id'], r['role'], r['answer_or_label'], bc, sc, c, verdict])
    lines = ['stage\tqid\tid\trole\tanswer_or_label\tbest_cell\tsecond_cell\tconf\tverdict']
    lines += ['\t'.join(x) for x in rows]
    for stage in sorted({x[0] for x in rows}):
        k = [x for x in rows if x[0] == stage and x[3] == 'control']; hit = sum(x[8] == 'HIT' for x in k)
        lines.append(f'# {stage}: GK {hit}/{len(k)} {"PASS" if hit >= 4 else "FAIL"}')
    return '\n'.join(lines) + '\n'

if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == 'build': build(a[1])
    elif a and a[0] == 'score':
        txt = score(); p = f'{U}/result.tsv'
        if '--check' in a:
            ok = os.path.exists(p) and open(p).read() == txt; print('up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
        open(p, 'w').write(txt); print(txt)
    else: print(__doc__); sys.exit(1)
