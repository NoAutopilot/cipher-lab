"""PISA-244 (12 Oct 2026, PREREG-PISA-244.md): blind per-token crop compare of the f.244r key86 T45/T47/T57 tokens with the UNA-PISA
instrument unchanged (22-cell sheet, 5 known-answer tiles, prompt, parser, settle rule). Centres: pisa_244/locate.tsv (eye-located).
  python3 ciphers/fr16045-pisany-rome-1585/pisa_244/pisa_244.py build          tiles + prompt (pisa_244/tok/, blind/f244r/)
  python3 ciphers/fr16045-pisany-rome-1585/pisa_244/pisa_244.py score [--check]  blind/reply_f244r.txt -> pisa_244/result.tsv
Run from the repository root."""
import sys, os, random, csv
from collections import Counter
from PIL import Image
sys.path.insert(0, 'ciphers/fr16045-pisany-rome-1585/una_pisa')
import una_pisa as UP, strips
strips.PAGES['f244r'] = ('f244r', 1360, 'tx86/ciphertext_f244r_preRS244.tsv' if os.path.exists(f'{UP.D}/tx86/ciphertext_f244r_preRS244.tsv') else 'tx86/ciphertext_f244r.tsv')  # PISA-RS244 pre-edit labels  # R9-PIS2's f.244r stitch (s2 box x 1360)
D = UP.D; H = f'{D}/pisa_244'; SEED = 20261012 + 244

def located():
    return [r for r in csv.DictReader(open(f'{H}/locate.tsv'), delimiter='\t') if r['x_centre_strip'] != '-']

def values():
    return {r['sign']: r['value'] for r in csv.DictReader(open(f'{D}/key86.tsv'), delimiter='\t')}

def tiles_for():
    items = [(cid, crop, ans, 'control') for cid, crop, ans in UP.CONTROLS]
    for r in located():
        tid = f"f244r_{r['line']}_p{r['pos']}"
        items.append((tid, f'{H}/tok/{tid}.png', r['label'], 'test'))
    rr = random.Random(SEED); rr.shuffle(items)
    return [(f'Q{i+1:02d}',) + it for i, it in enumerate(items)]

def build():
    os.makedirs(f'{H}/tok', exist_ok=True); os.makedirs(f'{H}/blind/f244r', exist_ok=True)
    for r in located():
        s = strips.strip('f244r', r['line']); x = int(r['x_centre_strip'])
        s.crop((x - 60, 0, x + 60, s.size[1])).save(f"{H}/tok/f244r_{r['line']}_p{r['pos']}.png")
    rows = tiles_for()
    with open(f'{H}/blind/f244r/tiles_map.tsv', 'w') as f:
        f.write('qid\tid\tcrop\tanswer_or_label\trole\n')
        for q, cid, crop, ans, role in rows:
            im = Image.open(crop).convert('L'); im = im.resize((im.size[0] * 2, im.size[1] * 2), Image.LANCZOS)
            im.save(f'{H}/blind/f244r/{q}.png'); f.write(f'{q}\t{cid}\t{crop}\t{ans}\t{role}\n')
    qs = ' '.join(r[0] for r in rows)
    prompt = f"""You are comparing handwritten cipher signs from a 16th-century letter against the cells of a printed cipher table.
Files: the table sheet {UP.U}/blind/cells_sheet.png shows 22 table cells, each under a letter A-V (cells were cut at low resolution;
some cells have a circle drawn round the sign). Token tiles: {', '.join(f'{H}/blind/f244r/{r[0]}.png' for r in rows)}.
Each token tile is cut from a line of the letter; the sign to identify is the one in the horizontal CENTRE of the tile (neighbouring
signs may show at the edges). Look at every image. For each tile, say which table cell's sign it is. Ignore any circle drawn round a
cell sign when matching shape, but note it.
Reply with exactly one line per tile, in this format and nothing else after the lines:
Qnn<TAB>best=<letter><TAB>second=<letter><TAB>confidence=<high|medium|low><TAB><short description of the centre sign>
Tiles: {qs}"""
    open(f'{H}/blind/f244r/prompt.md', 'w').write(prompt + '\n'); print(prompt)

def score():
    m = UP.cell_map(); val = values(); rows = []; k = []; settled = Counter(); own = Counter()
    rep = UP.parse(f'{H}/blind/reply_f244r.txt')
    for r in csv.DictReader(open(f'{H}/blind/f244r/tiles_map.tsv'), delimiter='\t'):
        b, s, c = rep.get(r['qid'], ('', '', ''))
        bc, sc = m.get(b, '?'), m.get(s, '?'); lab = r['answer_or_label']
        if r['role'] == 'control':
            v = 'HIT' if bc == lab else 'MISS'; k.append(v); note = ''
        else:
            v = f'SETTLED-{bc}' if c in ('high', 'medium') else 'UNSETTLED'
            if v == 'UNSETTLED': note = ''
            elif bc == lab: note = 'own cell'; own[lab] += 1
            elif val.get(bc) == val.get(lab): note = f'same value ({val.get(bc)}), no edit'
            else: note = f'label-slip candidate ({val.get(lab)} -> {val.get(bc)})'; settled[(lab, bc)] += 1
        rows.append([r['qid'], r['id'], r['role'], lab, bc, sc, c, v, note])
    hit = k.count('HIT'); gk = hit >= 4
    out = ['qid\tid\trole\tanswer_or_label\tbest_cell\tsecond_cell\tconf\tverdict\tnote']
    out += ['\t'.join(x) for x in rows] + [f'# f244r: GK {hit}/{len(k)} {"PASS" if gk else "FAIL (NON-TEST)"}']
    if gk:
        for (lab, bc), n in sorted(settled.items()):
            kc = n >= 3 and own[lab] == 0
            out.append(f'# {lab} -> {bc} ({val.get(lab)} -> {val.get(bc)}): {n} settled; {own[lab]} settled on {lab}; '
                       f'key-cell rule {"MET (candidate for a separate PREREG)" if kc else "not met"}; relabel candidates {n} (not applied)')
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
