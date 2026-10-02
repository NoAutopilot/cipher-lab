#!/usr/bin/env python3
"""Rebuild whole-line images of the f.198 cipher-bearing lines for the sign sorter (GAPS5, 2 Oct 2026).

Recto: the native region source was not kept, so each line is stitched from its two committed crops (s1 + the part of
s2 right of s1's end; both crops are native resolution, boxes in images/recto/manifest.json). Verso: cut from the
committed verso source image at the v2 crop boxes. Output: sorter/lines/r_Lnn.jpg and v_Lnn.jpg (grey, quality 85).
  python3 ciphers/fr3986-nevers-revol-1593/sorter/stitch_lines.py
"""
import json, os
from PIL import Image
T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(T, 'sorter', 'lines'); os.makedirs(OUT, exist_ok=True)
RECTO = ['L03', 'L04', 'L05', 'L09', 'L11', 'L12', 'L13', 'L14', 'L15', 'L16', 'L19']   # GAPS4 cipher-bearing lines
VERSO = ['L04', 'L05', 'L06', 'L07', 'L08', 'L09', 'L10', 'L13', 'L15', 'L16', 'L18', 'L19']  # lines with v2 signs


def boxes(d):
    m = json.load(open(os.path.join(T, 'images', d, 'manifest.json')))['iiif_lines']
    return {(f"L{e['band']:02d}", e['segment']): e for e in m}


rb = boxes('recto')
for L in RECTO:
    a, b = rb[(L, 1)], rb[(L, 2)]
    ia = Image.open(os.path.join(T, 'images/recto', a['crop'])).convert('L')
    ib = Image.open(os.path.join(T, 'images/recto', b['crop'])).convert('L')
    x0, x1 = a['box'][0], b['box'][2]
    im = Image.new('L', (x1 - x0, ia.height), 255)
    im.paste(ia, (0, 0)); im.paste(ib.crop((a['box'][2] - b['box'][0], 0, ib.width, ib.height)), (a['box'][2] - x0, 0))
    im.save(os.path.join(OUT, f'r_{L}.jpg'), quality=85)
vb = boxes('v2')
src = Image.open(os.path.join(T, 'images', vb[('L04', 1)]['source_file'])).convert('L')
for L in VERSO:
    a, b = vb[(L, 1)], vb[(L, 2)]
    src.crop((a['box'][0], a['box'][1], b['box'][2], a['box'][3])).save(os.path.join(OUT, f'v_{L}.jpg'), quality=85)
print(len(os.listdir(OUT)), 'line images ->', OUT)
