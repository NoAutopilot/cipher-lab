"""TXE2-VIV102-BASE step 1: per-line s1/s2 overlap of the committed c105_f102r crops by tools/overlap_audit.pixel_overlap
(read-free, no truth) and the brief's overlap sentence by tools/iiif_lines.overlap_sentence (never typed).
Copy of ../s2read/overlap_measure.py with the leaf (c105_f102r) and output dir changed."""
import sys
sys.path.insert(0, 'tools')
import numpy as np
from PIL import Image
from overlap_audit import pixel_overlap, load_manifest, gray
import iiif_lines
D = 'ciphers/fr16104-vivonne-spain-1572/images'
O = 'benchmark-tx/txeng2/viv102base'
segs = load_manifest(f'{D}/manifest.json', D)
lines = sorted(k for k in segs if k.startswith('c105_f102r_L'))
out = open(f'{O}/overlap.tsv', 'w')
out.write('line\tnsegs\ts1_wh\ts2_wh\tscale\tbox_overlap_native\tpixel_overlap_img\tncc\tpixel_overlap_native\n')
pxs, nccs, boxes = [], [], []
for ln in lines:
    s = segs[ln]
    if len(s) < 2:
        out.write(f'{ln}\t{len(s)}\t\t\t\t\t\t\t\n'); continue
    w1 = Image.open(s[0]['path']).size; w2 = Image.open(s[1]['path']).size
    sc = w1[0] / (s[0]['x1'] - s[0]['x0']); bo = s[0]['x1'] - s[1]['x0']
    px, v = pixel_overlap(s[0]['path'], s[1]['path'])
    pxs.append(round(px / sc)); nccs.append(v); boxes.append(round(bo))
    out.write(f'{ln}\t{len(s)}\t{w1[0]}x{w1[1]}\t{w2[0]}x{w2[1]}\t{sc:.3f}\t{bo:.0f}\t{px}\t{v}\t{px/sc:.0f}\n')
out.close()
ws = []
for ln in lines:
    for s in segs[ln]:
        g = gray(s['path'])
        w = iiif_lines.ink_run_width(g, [(0, g.shape[0], None)], 0, g.shape[1], 170)
        if w: ws.append(w)
sw = float(np.median(ws))
sent, o = iiif_lines.overlap_sentence([(segs[lines[0]][0]['x0'], segs[lines[0]][0]['x1']),
                                       (segs[lines[0]][1]['x0'], segs[lines[0]][1]['x1'])], sw,
                                      f'ink-run median over the {len(ws)} crops')
summ = (f'{len(lines)} lines; pixel overlap native min {min(pxs)} max {max(pxs)}; manifest boxes min {min(boxes)} max {max(boxes)}; '
        f'ncc {min(nccs):.3f}-{max(nccs):.3f}; sign width {sw:.0f} px')
print(summ); print('SENTENCE:', sent)
open(f'{O}/overlap_note.md', 'w').write(
    '# Crops note (tools/iiif_lines.overlap_sentence; overlap MEASURED per line by tools/overlap_audit.pixel_overlap: '
    + summ + ')\n\n- c105_f102r: ' + sent + '\n')
