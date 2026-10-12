#!/usr/bin/env python3
"""TXE4-8 BOX-ANCHOR: build one reader's scratch directory (task.txt, sheet.png, crops) for a pass.
    python3 build_tasks.py PASS SCRATCH_DIR      PASS one of N1 N2 O1 O2 R1
N: the SHEET-VIV task text (benchmark-tx/txeng2/sheetviv/reader_task.txt) with its placeholders filled and the repository
paths replaced by the scratch copies'. O and R: the same text plus the numbered-box paragraph and the per-box output
format; R's text is identical to O's. The task text is also written to tasks/<PASS>.txt beside this script (committed).
No truth, no key, no other pass, no repository path reaches the reader."""
import os, re, shutil, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
HERE = os.path.dirname(os.path.abspath(__file__))
LINES = ['L02', 'L04', 'L08', 'L10', 'L16', 'L18', 'L20', 'L24', 'L28', 'L30', 'L32', 'L34', 'L36']
IMG = os.path.join(ROOT, 'ciphers/fr16104-vivonne-spain-1572/images')
SHEET = os.path.join(ROOT, 'ciphers/fr16104-vivonne-spain-1572/glyphs/sheet_tomokiyo_v1.png')
TASK = os.path.join(ROOT, 'benchmark-tx/txeng2/sheetviv/reader_task.txt')

BOX_PARA = """
NUMBERED BOXES (read this before the crops). For every line you get FOUR images, in this order: s1 as it is, s1 with numbered
boxes drawn on it (file name ending _boxes.jpg), s2 as it is, s2 with numbered boxes. The boxed copy is the same picture with a
dashed blue or orange rectangle around each sign unit and its number printed in the light band below the picture (a thin tick
joins each box to its number; the numbers run left to right along the line, continuing from s1 into s2; the overlap between s1
and s2 is numbered ONCE, so a box number appears on only one of the two segments). Use the unmarked copy to see the ink
clearly and the boxed copy to know which box you are answering. Read ONLY the numbered boxes, one row per box, in box order:
- signs = the sheet token of the sign inside the box; if the box holds SEVERAL signs, write their tokens left to right
  separated by single spaces (e.g. "o o" or "m e"); if the box holds NO cipher sign (plain words, a blot, a flourish, empty
  paper, part of a neighbouring line), write "-".
- Never add a row for ink outside the numbered boxes, never skip a box number, never merge two boxes into one row.
- alt = your second choice for the FIRST sign in the box if unsure (one token), else empty. conf = H/M/L for the whole box.
Write a TSV to OUTPUT_PATH with header: line<TAB>box<TAB>signs<TAB>alt<TAB>conf
line = f102r_L02 style ids; box = the printed box number (1, 2, 3 ... per line, every number present exactly once).
Reply with only the number of rows per line.
"""


def main(p, scratch):
    arm = p[0]
    os.makedirs(scratch, exist_ok=True)
    sheet = os.path.join(scratch, 'sign_sheet.png'); shutil.copy(SHEET, sheet)
    crops = os.path.join(scratch, 'crops'); os.makedirs(crops, exist_ok=True)
    files = []
    for ln in LINES:
        for seg in ('s1', 's2'):
            f = f'c105_f102r_{ln}_{seg}.jpg'; shutil.copy(os.path.join(IMG, f), os.path.join(crops, f)); files.append(f)
            if arm in 'OR':
                g = f'c105_f102r_{ln}_{seg}_boxes.jpg'
                shutil.copy(os.path.join(HERE, 'overlays', arm, g), os.path.join(crops, g)); files.append(g)
    txt = open(TASK, encoding='utf-8').read()
    txt = txt.replace(os.path.join(ROOT, 'ciphers/fr16104-vivonne-spain-1572/glyphs/sheet_tomokiyo_v1.png'), sheet)
    txt = txt.replace('/home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/glyphs/sheet_tomokiyo_v1.png', sheet)
    txt = txt.replace('/home/user/cipher-lab/ciphers/fr16104-vivonne-spain-1572/images/', crops + '/')
    txt = txt.replace('LINES_HERE', ', '.join(LINES)).replace('FILECOUNT', str(len(files)))
    out_path = os.path.join(scratch, 'read.tsv')
    if arm in 'OR':
        txt = txt.replace('the two files c105_f102r_<line>_s1.jpg then c105_f102r_<line>_s2.jpg (view every one; %d files)' % len(files),
                          'the four files c105_f102r_<line>_s1.jpg, c105_f102r_<line>_s1_boxes.jpg, c105_f102r_<line>_s2.jpg, '
                          'c105_f102r_<line>_s2_boxes.jpg (view every one; %d files)' % len(files))
        # the per-box output replaces the free-read output block
        i = txt.index('Write a TSV to OUTPUT_PATH')
        txt = txt[:i] + BOX_PARA.lstrip('\n')
        txt = txt.replace('- One row per sign, using the token', '- Name each sign by the token')
    txt = txt.replace('OUTPUT_PATH', out_path)
    assert '/home/user/cipher-lab/ciphers' not in txt and 'benchmark-tx' not in txt, 'repository path left in the task text'
    open(os.path.join(scratch, 'task.txt'), 'w', encoding='utf-8').write(txt)
    open(os.path.join(HERE, 'tasks', f'{p}.txt'), 'w', encoding='utf-8').write(txt.replace(scratch, '<SCRATCH>'))
    print(p, scratch, len(files), 'images; task', len(txt), 'chars')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
