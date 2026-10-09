"""TXE2-S2READ step 1: per-line s1/s2 overlap of the committed c106_f103r crops by tools/overlap_audit.py's pixel match
(read-free, no truth), plus the manifest-box overlap and sign-width-based overlap sentence (tools/iiif_lines.overlap_sentence)."""
import sys, os, json, glob, re
sys.path.insert(0, 'tools')
import numpy as np
from PIL import Image
from overlap_audit import pixel_overlap, load_manifest, gray
import iiif_lines
D = 'ciphers/fr16104-vivonne-spain-1572/images'
segs = load_manifest(f'{D}/manifest.json', D)
rows = []
for ln in sorted(k for k in segs if k.startswith('c106_f103r_L')):
    s = segs[ln]
    if len(s) < 2:
        rows.append((ln, len(s), None, None, None, None, None)); continue
    w1 = Image.open(s[0]['path']).size; w2 = Image.open(s[1]['path']).size
    scale = w1[0] / (s[0]['x1'] - s[0]['x0'])
    box_ov = s[0]['x1'] - s[1]['x0']
    px, v = pixel_overlap(s[0]['path'], s[1]['path'])
    rows.append((ln, len(s), w1, w2, round(scale, 3), box_ov, (px, v)))
out = open('benchmark-tx/txeng2/s2read/overlap.tsv', 'w')
out.write('line\tnsegs\ts1_wh\ts2_wh\tscale\tbox_overlap_native\tpixel_overlap_img\tncc\tpixel_overlap_native\n')
for ln, n, w1, w2, sc, bo, pv in rows:
    if pv is None:
        out.write(f'{ln}\t{n}\t\t\t\t\t\t\t\n'); continue
    out.write(f'{ln}\t{n}\t{w1[0]}x{w1[1]}\t{w2[0]}x{w2[1]}\t{sc}\t{bo:.0f}\t{pv[0]}\t{pv[1]}\t{pv[0]/sc:.0f}\n')
out.close()
print(open('benchmark-tx/txeng2/s2read/overlap.tsv').read())

# sign width: tools/iiif_lines.ink_run_width on each crop's own core rows (crops are at native scale 1.0), median over L01-L37
ws = []
for ln in [f'c106_f103r_L{i:02d}' for i in range(1, 38)]:
    for s in segs[ln]:
        g = gray(s['path'])
        w = iiif_lines.ink_run_width(g, [(0, g.shape[0], None)], 0, g.shape[1], 170)
        if w: ws.append(w)
sw = float(np.median(ws))
lines = [f'c106_f103r_L{i:02d}' for i in range(1, 38)]
sent, o = iiif_lines.overlap_sentence([(segs[l][0]['x0'], segs[l][0]['x1']) for l in lines[:1]] +
                                      [(segs[lines[0]][1]['x0'], segs[lines[0]][1]['x1'])], sw, 'ink-run median over the 74 crops')
print('sign_w', sw)
print('SENTENCE:', sent)
open('benchmark-tx/txeng2/s2read/overlap_note.md', 'w').write(
    '# Crops note (tools/iiif_lines.overlap_sentence; overlap MEASURED per line by tools/overlap_audit.pixel_overlap: '
    '150 native px on all 37 lines L01-L37, ncc 0.998-0.999, equal to the manifest boxes)\n\n- c106_f103r: ' + sent + '\n')
