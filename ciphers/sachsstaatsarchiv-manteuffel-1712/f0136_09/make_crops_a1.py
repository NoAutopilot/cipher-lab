#!/usr/bin/env python3
"""MANT-R07 (PREREG-MANT-0136-A1): tighter, higher-contrast r07/r08 strips from the committed crops f0136_L12.jpg + f0136_L13.jpg
(adjacent boxes of 0136.jpg, y 2532-2650 and 2650-2779). Stitch, autocontrast 1%, one strip per line (numerals + the gloss row
below), three overlapping thirds, 2.5x upscale -> crops_a1/*.png + manifest.json.
python3 ciphers/sachsstaatsarchiv-manteuffel-1712/f0136_09/make_crops_a1.py"""
import json, os
from PIL import Image, ImageOps
D = os.path.dirname(os.path.abspath(__file__)); O = f'{D}/crops_a1'; os.makedirs(O, exist_ok=True)
a = Image.open(f'{D}/crops/f0136_L12.jpg').convert('L'); b = Image.open(f'{D}/crops/f0136_L13.jpg').convert('L')
s = Image.new('L', (a.width, a.height + b.height), 255); s.paste(a, (0, 0)); s.paste(b, (0, a.height))
s = ImageOps.autocontrast(s, cutoff=1)
Y0 = 2532; STRIPS = {'r07': (56, 126), 'r08': (114, 196)}; W = s.width; thirds = [(0, 600), (480, 1080), (960, W)]
man = []
for ln, (y0, y1) in STRIPS.items():
    for k, (x0, x1) in enumerate(thirds, 1):
        c = s.crop((x0, y0, x1, y1)); c = c.resize((int(c.width * 2.5), int(c.height * 2.5)), Image.LANCZOS)
        name = f'a1_{ln}_{k}.png'; c.save(f'{O}/{name}')
        man.append({'crop': name, 'from': ['crops/f0136_L12.jpg', 'crops/f0136_L13.jpg'], 'box_in_0136': [600 + x0, Y0 + y0, 600 + x1, Y0 + y1],
                    'ops': 'stitch, autocontrast cutoff 1, LANCZOS 2.5x', 'date': '09 Oct 2026', 'job': 'MANT-R07'})
json.dump({'crops_a1': man}, open(f'{O}/manifest.json', 'w'), indent=1)
print(len(man), 'crops ->', O)
