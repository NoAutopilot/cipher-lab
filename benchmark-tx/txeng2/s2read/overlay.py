"""TXE2-S2READ step 1 overlay: each line's s1 and s2 stitched at the measured 150 px overlap (s2 drawn from s1's x=1450),
seam marked with dashed blue (0,114,178) lines; 10 lines per sheet. Read-free."""
from PIL import Image, ImageDraw
D = 'ciphers/fr16104-vivonne-spain-1572/images'; O = 150
for k, rng in enumerate([range(1, 11), range(11, 21), range(21, 31), range(31, 38)]):
    rows = []
    for i in rng:
        a = Image.open(f'{D}/c106_f103r_L{i:02d}_s1.jpg').convert('RGB'); b = Image.open(f'{D}/c106_f103r_L{i:02d}_s2.jpg').convert('RGB')
        h = max(a.height, b.height); W = a.width + b.width - O
        im = Image.new('RGB', (W, h + 18), 'white'); im.paste(a, (0, 18)); im.paste(b.crop((O, 0, b.width, b.height)), (a.width, 18))
        d = ImageDraw.Draw(im); d.text((4, 2), f'L{i:02d}', fill=(0, 0, 0))
        for x in (a.width - O, a.width):
            for y in range(18, h + 18, 8): d.line([(x, y), (x, y + 4)], fill=(0, 114, 178), width=2)
        rows.append(im)
    W = max(r.width for r in rows); H = sum(r.height + 6 for r in rows)
    sh = Image.new('RGB', (W, H), (230, 230, 230)); y = 0
    for r in rows: sh.paste(r, (0, y)); y += r.height + 6
    sh = sh.resize((sh.width // 2, sh.height // 2))
    sh.save(f'/tmp/claude-0/-home-user-cipher-lab/ce733730-fabb-57ea-ae1a-3fedb597e78b/scratchpad/ov{k}.jpg', quality=85)
