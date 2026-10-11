"""PISA-T475 (11 Oct 2026) locating aid (not evidence): predicted strip x for every f.244r T45/T47/T57 token (una_pisa/windows.py's
predict, f.244r strips stitched at s2 x=1360 as R9-PIS2, anchors = R9-PIS2's eye-located f.244r T31 tokens pis2/tokens_pos.tsv),
and a montage of 300 px windows with the predicted centre marked, for the worker's eye re-centring.
  python3 ciphers/fr16045-pisany-rome-1585/pisa_t475/locate.py OUT_MONTAGE.png   (prints page line pos ord label x)
Run from the repository root."""
import sys, csv
from PIL import Image, ImageDraw
sys.path.insert(0, 'ciphers/fr16045-pisany-rome-1585/una_pisa')
import strips, windows
strips.PAGES['f244r'] = ('f244r', 1360, 'tx86/ciphertext_f244r.tsv')
_anch = windows.anchors
def anchors(page, line):
    if page != 'f244r': return _anch(page, line)
    return {int(r['tok_index']): int(r['x_centre_strip']) for r in csv.DictReader(open(f'{strips.D}/pis2/tokens_pos.tsv'), delimiter='\t')
            if r['leaf'] == page and r['line'] == line and r['x_centre_strip'] not in ('-', '')}
windows.anchors = anchors
TGT = {'T45', 'T47', 'T57'}
def main(out):
    tiles = []
    lines = sorted({r.split('\t')[0] for r in open(f'{strips.D}/reading_f244r_tokens.tsv')} - {'line'})
    for line in lines:
        toks = strips.tokens('f244r', line)
        if not any(s in TGT for _, s in toks): continue
        s, toks, xs = windows.predict('f244r', line)
        for k, (pos, sg) in enumerate(toks):
            if sg not in TGT: continue
            c = int(xs[k]); w0 = max(0, c - 150); win = s.crop((w0, 0, w0 + 300, s.size[1])).convert('RGB')
            im = Image.new('RGB', (300, s.size[1] + 18), 'white'); im.paste(win, (0, 18)); d = ImageDraw.Draw(im)
            d.line([(c - w0, 18), (c - w0, 26)], fill='red', width=2); d.text((2, 2), f'{line} p{pos} x{c}', fill='red')
            tiles.append(im); print(f'f244r\t{line}\t{pos}\t{k+1}\t{sg}\t{c}')
    cols = 4; W = 300; H = max(t.size[1] for t in tiles); rows = (len(tiles) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * W, rows * H), 'white')
    for i, t in enumerate(tiles): sheet.paste(t, ((i % cols) * W, (i // cols) * H))
    sheet.save(out)
if __name__ == '__main__':
    main(sys.argv[1])
