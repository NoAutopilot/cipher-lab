#!/usr/bin/env python3
"""SIG-B228: cut line strips (cipher part only, < 2500 px wide) for the numeral-mark re-check; writes b167228/sig_num/S??.png and
targets.tsv (strip, numeral index, code, role: target = one of the 27 unmarked numerals, control = transcribed with a mark).
Usage: python3 b167228/sig_num.py (from the target folder)"""
from PIL import Image
C = 'images/crops/src_ark_12148_btv1b90015040_'
RA, RC, RB = C + 'f239_4250_2150_3450_560.jpg', C + 'f239_4250_2700_3450_330.jpg', C + 'f239_4200_4150_3500_500.jpg'
VA, VB = C + 'f240_850_1250_3200_480.jpg', C + 'f240_850_3560_3200_1340.jpg'
STRIPS = [('S01', 'r_a_L02', RA, (850, 150, 2350, 410), '73 45 70 77 98 16 73'),
          ('S02', 'r_c_L01', RC, (600, 0, 1300, 250), '86 9'),
          ('S03', 'r_b_L01', RB, (2550, 110, 3300, 300), '16 41 29 16'),
          ('S04', 'r_b_L02', RB, (950, 210, 3250, 450), '40 46 46 73 76 33 81 98 40 51'),
          ('S05', 'v_a_L01', VA, (150, 20, 2400, 240), '55 71 22 62 71 66 16 44'),
          ('S06', 'v_a_L02', VA, (150, 170, 750, 340), '26 12 41'),
          ('S07', 'v_b_L02', VB, (150, 130, 2450, 370), '65 81 96 10 19 16 44 51 6 40 13 48'),
          ('S08', 'v_b_L03', VB, (150, 290, 2450, 530), '16 86 10 95 51 47 9 96 73 73 95'),
          ('S09', 'v_b_L04', VB, (150, 460, 2450, 700), '90 65 16 71 66 77 66 30 14 16'),
          ('S10', 'v_b_L07', VB, (150, 950, 1300, 1190), '10 19 16 44 51 6')]
TARGET = {'S01': [6, 7], 'S02': [1], 'S03': [1, 3], 'S04': [2, 5, 7, 8, 9, 10], 'S05': [1, 3, 4, 6, 7], 'S06': [2], 'S07': [3, 6],
          'S08': [1, 8], 'S09': [3, 5, 7, 9, 10], 'S10': [3]}
CONTROL = {('S05', 2): "'", ('S09', 1): "'", ('S04', 1): "'", ('S07', 7): "'"}   # pre-registered 4 (prereg_sig.md item 6)
if __name__ == '__main__':
    rows = ['strip\tline\tidx\tcode\trole\ttranscribed']
    for sid, line, src, box, seq in STRIPS:
        Image.open(src).crop(box).save(f'b167228/sig_num/{sid}.png')
        for i, c in enumerate(seq.split(), 1):
            role = 'target' if i in TARGET[sid] else ('control' if (sid, i) in CONTROL else 'other')
            rows.append(f'{sid}\t{line}\t{i}\t{c}\t{role}\t' + (CONTROL.get((sid, i), 'none') if role != 'other' else ''))
    open('b167228/sig_num/targets.tsv', 'w').write('\n'.join(rows) + '\n')
    print(sum(r.endswith('\tnone') for r in rows), 'targets;', len(CONTROL), 'controls')
