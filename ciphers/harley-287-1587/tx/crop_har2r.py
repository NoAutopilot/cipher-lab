import sys, os, csv, random
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
img_dir, runs_tsv, out = sys.argv[1:4]
P1 = Image.open(os.path.join(img_dir, 'IMG_R8480_I39160_P1.jpg')).convert('RGB')
frames = {}
def frame(reg):
    if reg not in frames:
        x, y, w, h = reg
        frames[reg] = P1.crop((x, y, x + w, y + h)).rotate(-2.25, Image.BICUBIC, fillcolor=(230, 230, 230))
    return frames[reg]
A, B = (2650, 6200, 4030, 800), (2650, 6200, 4400, 2000)
for line in open(runs_tsv):
    f = line.rstrip('\n').split('\t')
    if line.startswith('#') or f[0] == 'run' or f[0].startswith('G'): continue
    run, part, x0, x1, y0, y1 = f[0], f[1], *map(int, f[2:6])
    fr = frame(A if run in ('R1', 'R2', 'R3', 'R4') else B)
    c = fr.crop((x0, y0, x1, y1)); c = c.resize((int(c.width * 1.15), int(c.height * 1.15)), Image.BICUBIC)
    c.save(os.path.join(out, '%s_p%s.png' % (run, part))); print(run, part, c.size)
P4 = Image.open(os.path.join(img_dir, 'IMG_R8479_I39159_P4.jpg')).convert('RGB')
boxes = [(3030, 3150, 3570, 3340), (4730, 3110, 5110, 3300), (5700, 3020, 6290, 3210)]
cs = [P4.crop(b) for b in boxes]; H = max(c.height for c in cs); W = sum(c.width for c in cs) + 60 * 2
ctl = Image.new('RGB', (W, H), (230, 230, 230)); x = 0
for c in cs: ctl.paste(c, (x, 0)); x += c.width + 60
ctl.save(os.path.join(out, 'control.png')); print('control', ctl.size)
print('order (A,B) for call 1:', random.Random(2).sample(['R1', 'control'], 2))
