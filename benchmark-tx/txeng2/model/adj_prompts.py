#!/usr/bin/env python3
"""TXE2-MODEL: write the third-reader (Sonnet) adjudication task for one item/arm/line group: copies adjudicate_in rows of
those lines, the line crops and the blind sheet into a scratch folder; the same wording for both arms (the arm is never named).
    python3 adj_prompts.py ITEM ARM GROUP L01,L02,... SCRATCH"""
import os, shutil, sys
R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__))
item, arm, grp, lines, S = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4].split(','), sys.argv[5]
BIR = R + '/ciphers/nevers-birago-fr3251-1572/harvest'; CEP = R + '/ciphers/ceppo-nevers-fr3251-1570s/harvest'
DIN = R + '/ciphers/fr3621-dinteville-1592'
name = 'adj_%s_%s_%s' % (item.split('-')[0], arm, grp); d = os.path.join(S, name); os.makedirs(d, exist_ok=True)
src = open(os.path.join(HERE, 'work', item + '_' + arm, 'adjudicate_in.tsv')).read().splitlines()
keep = [src[0]] + [l for l in src[1:] if l.split('\t')[0] in lines]
open(d + '/adjudicate_in.tsv', 'w').write('\n'.join(keep) + '\n')
crops = []
if item == 'birago1572-no87':
    sheet = BIR + '/sign_sheet_blind_1572.png'
    for L in lines:
        crops += [BIR + '/f178v/f178v_%s_s%d.jpg' % (L, s) for s in (1, 2, 3)]
    layout = ('Crops: three overlapping segments s1, s2, s3 per line of f.178v (2x; about 100 px overlap, a sign at the right edge '
              'of s1 that reappears at the left edge of s2 is ONE sign). The page is cipher throughout.')
    vocab = 'Answer with a cell of the sheet (T10..T98) or one of X_K, X_A, X_EQ, X_S, X_NEW (describe it in the note).'
elif item == 'ceppo-f87-S':
    sheet = CEP + '/sign_sheet_blind.png'
    for L in lines:
        crops += sorted(CEP + '/f87/lines2x/' + f for f in os.listdir(CEP + '/f87/lines2x') if f.startswith('f87_%s_' % L))
    layout = ('Crops: segments s1, s2, s3 ... of each line (2x, tracked and sheared to follow the line; segments do NOT overlap). '
              'L01: prose up to "... per alcuni suoi particolari", then cipher to line end; L02-L05 cipher throughout.')
    vocab = 'Answer with a cell of the sheet (S10..S97) or one of X_THETA2, X_POUND, X_NEW (describe it in the note).'
else:
    sheet = None
    for L in lines:
        crops += [DIN + '/images/f128_%s_s%d.jpg' % (L, s) for s in (1, 2)]
    pi = open(DIN + '/f128/pass_instructions.md').read()
    layout = ('Crops: each line in two overlapping segments s1 (left) and s2 (right), about 150 px overlap (a sign seen at the end '
              'of s1 and the start of s2 is ONE sign); the cipher line is the middle row of each crop; ignore the small gloss '
              'writing above it and the next line at the bottom. The sign labels are listed below (from the readers\' instructions):\n\n'
              + pi[pi.index('Sign labels'):pi.index('Output:')].strip())
    vocab = 'Answer with one of the sign labels above, or NEW:<short description>.'
for f in crops + ([sheet] if sheet else []):
    shutil.copy(f, d)
P = ['You are a third, VALUE-BLIND reader settling the places where two earlier blind readers of a cipher transcription '
     'disagree. You match hand-drawn signs by SHAPE only; you do not know, and must not try to work out, what any sign means. '
     'Read ONLY the files listed here; do not open, list or search any other file or directory.', '']
if sheet:
    P += ['Sign sheet: %s/%s' % (d, os.path.basename(sheet)), '']
P += ['Crops (in order):'] + ['%s/%s' % (d, os.path.basename(c)) for c in crops] + ['', layout, '',
      'Disagreement sheet: %s/adjudicate_in.tsv' % d, '',
      'Each row of the sheet is one disputed position: passage (= line) and pos (position in the line counting the agreed signs), '
      'context_before / context_after (the agreed neighbouring signs, as labels, so you can find the place on the line crop by '
      'counting), candA / candB (what each earlier reader wrote there; "(none)" = that reader saw no sign there), their confidence '
      'and notes. For each row look at the crop and decide which reading the ink supports.', '',
      vocab + ' Write NONE if there is no separate sign at that position (one reader split one sign in two or saw a sign that is '
      'not there); write ? only if the ink cannot decide at all. You may give a cell neither reader wrote if the ink clearly shows it.', '',
      'Output: write exactly one TSV file %s/adjudicate_out.tsv with the header' % d,
      'passage\tpos\tsign_id\tconf\tnote',
      'and one row per sheet row (same passage and pos), conf H/M/L, note = a few words on the shape and which candidate you '
      'rejected. No other output file. Then report in two sentences: rows settled, how many to candA / candB / other / NONE / ?. '
      'Do not decode, do not guess meanings.']
open(os.path.join(HERE, 'prompts', name + '.md'), 'w').write('\n'.join(P) + '\n')
print(name, len(keep) - 1, 'rows', len(crops), 'crops')
