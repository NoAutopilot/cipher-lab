#!/usr/bin/env python3
"""MANT-0309: stack one kind of strip (c = code, g = gloss) into one labelled sheet, in run order or reverse.
python3 sheet.py c|g fwd|rev OUT.jpg"""
import sys, csv, os
from PIL import Image, ImageDraw
D = os.path.dirname(os.path.abspath(__file__))
kind, order, out = sys.argv[1], sys.argv[2], sys.argv[3]
runs = [r['run'] for r in csv.DictReader(open(f'{D}/runs.tsv'), delimiter='\t')]
if order == 'rev': runs = runs[::-1]
ims = [(r, Image.open(f'{D}/crops/{kind}0309{r}_L01.jpg').convert('L')) for r in runs]
sc = 1.5; W = int(max(i.width for _, i in ims) * sc) + 110; H = sum(int(i.height * sc) + 14 for _, i in ims)
S = Image.new('L', (W, H), 255); d = ImageDraw.Draw(S); y = 0
for r, i in ims:
    i = i.resize((int(i.width * sc), int(i.height * sc))); d.text((4, y + i.height // 2 - 5), r, fill=0)
    S.paste(i, (100, y)); y += i.height + 14; d.line((0, y - 7, W, y - 7), fill=160)
S.save(out, quality=92); print(out, S.size)
