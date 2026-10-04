#!/usr/bin/env python3
"""TX-FABLE (4 Oct 2026): build the exact task prompt of each blind Fable call from the item's pass-A brief on disk, the
same crop list and grouping as pass A, and an output path under benchmark-tx/txfable/raw/. Run from the repo root."""
import os, glob
R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(R, 'benchmark-tx/txfable')
NB = 'ciphers/nevers-birago-fr3251-1572/harvest'
CE = 'ciphers/ceppo-nevers-fr3251-1570s/harvest'
B36 = 'ciphers/birago-fr3252-1571-72/harvest/f36'
DIN = 'ciphers/fr3621-dinteville-1592'


def crops(pat):
    return sorted(glob.glob(os.path.join(R, pat)))


def task(brief, sheet, crop_list, outs, extra=''):
    t = ('You are a blind reader in a transcription test. Follow the brief below exactly. Read ONLY the image files listed '
         'here (crops and sign sheet); do not open, list or search any other file or directory.\n\n'
         'Sign sheet: %s\n\nCrops (in order):\n%s\n\n%sOutput file(s): %s\n\n---- BRIEF ----\n\n%s'
         % (sheet, '\n'.join(crop_list), extra, outs, open(os.path.join(R, brief)).read()))
    return t


CALLS = []
b87 = NB + '/blind_pass_brief_1572.md'; s87 = os.path.join(R, NB, 'sign_sheet_blind_1572.png')
CALLS.append(('no87_c1', task(b87, s87, crops(NB + '/f178r/f178r_L??_s?.jpg') + crops(NB + '/f179r/f179r_L??_s?.jpg'),
    'two files: crops f178r_* -> %s/raw/passF_f178r.tsv ; crops f179r_* -> %s/raw/passF_f179r.tsv (passage ids L01..L03 within each leaf)' % (OUT, OUT))))
v = crops(NB + '/f178v/f178v_L??_s?.jpg')
CALLS.append(('no87_c2', task(b87, s87, [c for c in v if int(c.split('_L')[1][:2]) <= 10], '%s/raw/passF_f178v_L01-10.tsv' % OUT)))
CALLS.append(('no87_c3', task(b87, s87, [c for c in v if int(c.split('_L')[1][:2]) >= 11], '%s/raw/passF_f178v_L11-23.tsv' % OUT)))
# Dinteville f.128r: pass A = one call, 8 crops, pass_instructions.md (labels in the brief text; no separate sheet image)
CALLS.append(('dint', task(DIN + '/f128/pass_instructions.md', '(none: the sign labels are in the brief)',
    crops(DIN + '/images/f128_L0[2-5]_s?.jpg'), '%s/raw/passF_dint_f128.tsv' % OUT)))
# Ceppo f.21v: pass A = two calls (L01-06, L07-11), brief blind_pass_brief.md + the per-line layout (reconstructed, PREREG)
bce = CE + '/blind_pass_brief.md'; sce = os.path.join(R, CE, 'sign_sheet_blind.png')
LAY1 = ('Per-line layout (prose words between cipher runs):\n'
        'L01: cipher throughout. L02: cipher from line start up to the prose word "quello" (run L02.1); prose; cipher again '
        'after the prose word "essi" to line end (run L02.2). L03: cipher throughout. L04: prose up to "persone", then cipher '
        'to line end. L05: cipher throughout. L06: cipher from line start up to the prose word "Però" (L06.1); prose; cipher '
        'after "di" to line end (L06.2).\n\n')
LAY2 = ('Per-line layout (prose words between cipher runs):\n'
        'L07: cipher throughout. L08: cipher from line start up to the prose word "Et" (L08.1); prose; cipher after "si" to '
        'line end (L08.2). L09: cipher from line start up to the prose word "ch\'io", then prose. L10: prose up to "opra", '
        'then cipher to line end. L11: cipher from line start up to the prose word "Io", then prose.\n\n')
f21 = crops(CE + '/f21v/lines2x/f21v_L??_s?.png')
CALLS.append(('f21v_c1', task(bce, sce, [c for c in f21 if int(c.split('_L')[1][:2]) <= 6], '%s/raw/passF_f21v_L01-06.tsv' % OUT, LAY1)))
CALLS.append(('f21v_c2', task(bce, sce, [c for c in f21 if int(c.split('_L')[1][:2]) >= 7], '%s/raw/passF_f21v_L07-11.tsv' % OUT, LAY2)))
LAY87 = ('Per-line layout: L01: prose up to "... per alcuni suoi particolari", then cipher to line end. L02-L05: cipher '
         'throughout (the lines fall to the right; each crop is sheared to follow its line).\n\n')
CALLS.append(('f87', task(bce, sce, crops(CE + '/f87/lines2x/f87_L??_s?.png'), '%s/raw/passF_f87.tsv' % OUT, LAY87)))
# f.36v: pass A's prompt (prompt_A_v36.md) verbatim except the crop list (v36top_L01 only) and the output paths
p = open(os.path.join(R, B36, 'prompt_A_v36.md')).read()
head, rest = p.split('/home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f36/crops/r37_L01_s1.png', 1)
tail = rest[rest.index('## What to record'):]
p36 = (head + '\n'.join(crops(B36 + '/crops/v36top_L01_s?.png')) + '\n\n' + tail)
p36 = p36.replace(os.path.join(R, B36, 'passA_v36.tsv'), OUT + '/raw/passF_v36.tsv').replace(
    os.path.join(R, B36, 'passA_v36_gloss.txt'), OUT + '/raw/passF_v36_gloss.txt')
CALLS.append(('f36v', 'You are a blind reader in a transcription test. Follow the brief below exactly.\n\n' + p36))

os.makedirs(os.path.join(OUT, 'prompts'), exist_ok=True); os.makedirs(os.path.join(OUT, 'raw'), exist_ok=True)
for name, t in CALLS:
    open(os.path.join(OUT, 'prompts', name + '.md'), 'w').write(t)
    print(name, t.count('.png') + t.count('.jpg'), 'image refs')
