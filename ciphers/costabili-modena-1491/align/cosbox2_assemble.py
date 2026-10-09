# COS-BOX2, 9 Oct 2026: joins a reader's per-box lines (<slip>_L<nn>_b<k>.jpg) into per-line cipher entries (<slip>_L<nn>.jpg), boxes joined
# by ' | ' (a box edge is a break under PREREG-COS-SPAN), and splits the result into the two per-slip files cosspan_pairs.py reads.
# Usage: python3 cosbox2_assemble.py READ.txt OUTDIR TAG   -> OUTDIR/r1163_TAG.txt, OUTDIR/r1165_TAG.txt
import sys, re, collections
src, outdir, tag = sys.argv[1:4]
sec, boxes, clear = None, collections.defaultdict(list), []
for line in open(src):
    line = line.rstrip('\n')
    if line.strip() in ('CIPHER', 'CLEAR'): sec = line.strip(); continue
    if '\t' not in line or sec is None: continue
    name, txt = line.split('\t', 1); name = name.strip().split('/')[-1]
    if sec == 'CIPHER':
        m = re.match(r'(c6[35]_L\d\d)_b(\d+)', name)
        boxes[m.group(1)].append((int(m.group(2)), txt.strip()))
    else: clear.append((name, txt.strip()))
for slip, k in (('r1163', 'c63'), ('r1165', 'c65')):
    with open(f'{outdir}/{slip}_{tag}.txt', 'w') as f:
        f.write(f'# COS-BOX2 {tag}, assembled from box reads by cosbox2_assemble.py\nCIPHER\n')
        for line in sorted(x for x in boxes if x.startswith(k)):
            f.write(f'{line}.jpg\t' + ' | '.join(t for _, t in sorted(boxes[line]) if t) + '\n')
        f.write('CLEAR\n')
        for name, txt in sorted(clear):
            if name.startswith('k' + k[1:]): f.write(f'{name}\t{txt}\n')
