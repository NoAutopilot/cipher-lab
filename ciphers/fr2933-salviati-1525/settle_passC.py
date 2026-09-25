#!/usr/bin/env python3
"""Majority vote passA/passB/passC on the 87 disagreement positions: 2 of 3 agree on base code -> that
call (marks taken from an agreeing pass, preferring one that also gives a mark); a three-way split (all
three codes differ) is settled from pass C's crop note at conf L, source noted as 3-way. Writes
recon_box_f55v/settled.tsv (line,pos,code,marks,source,reason) and prints the agreement recount
("rows where C agrees with A or B") and the three-way split count.
"""
import csv

def load(path):
    rows = {}
    for r in csv.DictReader(open(path), delimiter='\t'):
        rows[(r['line'].strip(), r['pos'].strip())] = r
    return rows

A = load('passA_f55v.tsv')
B = load('passB_f55v.tsv')
C = load('passC_f55v.tsv')

dis = list(csv.DictReader(open('recon_box_f55v/disagreements.tsv'), delimiter='\t'))

# Three-way splits (A, B and C all gave different base codes): C's own crop call (passC_f55v.tsv) is
# the blind read; this worker then re-examined the crop together with A's and B's own per-row notes
# (rule: pass C stays blind, but *settling* a genuine 3-way split is arbitration, not another blind
# pass) and picked the best-supported call, at conf L. code/marks empty-string means "keep C's own
# call" (C is the best-supported read); otherwise the tuple overrides to A's or B's call.
THREE_WAY_OVERRIDE = {
    ('3', '12'): ('_', '', 'B', "B's high-confidence note situates a plain '+'-shaped punctuation mark directly before the word 'Cosi'; more convincing than C's isolated '#' guess or A's S4"),
    ('8', '15'): ('v', '', 'C', "B's note places this inside an unbroken run of confirmed signs, ruling out A's plain read; C's independent 'v' (hook-then-loop) is kept over B's 'rz' as the closer atlas shape match"),
    ('9', '1'): ('_', '', 'B', "B reads a coherent plain-text stretch opening at this box (a Z-shaped plain letter); outweighs A's S7 and C's isolated Z-glyph match"),
    ('9', '2'): ('_', '', 'B', "same plain stretch as 9/1 and 9/3 (B: cursive 't'); C's isolated tee-shape match does not survive the word context"),
    ('9', '3'): ('_', '', 'B', "same plain stretch, B reads 's' with dot completing '...ts;'; C's isolated g match does not survive the word context"),
    ('10', '1'): (']', 'o', 'B', "B's '⊐ box open to the left plus a small o mark above' is a precise match to the ] (open bracket) atlas rather than C's closed-square 'sq'"),
    ('10', '4'): ('phi', '', 'B', "B's slashed-circle-on-stem description matches the same phi shape independently confirmed elsewhere on this leaf (line1 pos8); C's 'g' read a small edge mark in an otherwise blank crop"),
    ('10', '6'): ('lam', '3', 'B', "B identifies real ink (a lam stroke plus a numeral-3 mark, partly in a fold's shadow) that A's classifier missed as plain; consistent with C's own note of multiple numeral-like strokes here"),
    ('11', '8'): ('tee', '', 'B', "A (S7) and B (tee) both independently read a sign here, not plain; B's 'T-like vertical-with-crossbar' description is literally the tee atlas shape, so C's 'plain capital T' read is probably the same ink"),
    ('11', '16'): ('g', '', 'B', "genuinely marginal on all three passes (A 'uncertain', B share 0.63, C conf L); kept to B's atlas-anchored 'loop with crossing strokes, closer to g' as the least contrived of three weak reads"),
    ('13', '7'): ('nt', '', 'B', "B's high-confidence description (u/n hook joined to a crossed vertical, matching nt atlas exemplars) and cited precedent at line12 pos15 outweigh A's low-confidence Z and C's independent f guess"),
    ('16', '13'): ('dl', '', 'B', "three genuinely weak reads (nt/dl/phi); kept to B's dl, which explicitly weighs the low classifier share (0.62) against the loop+diagonal-flourish-tick shape"),
    ('16', '26'): ('w', '', 'B', "B's specific atlas comparison (flat hump-over-tail vs y's diagonal descender) is better reasoned than A's unexplained confirm or C's plain read of the same flourish"),
    ('17', '3'): ('S', '', 'B', "B's 'squiggle matching atlas S' beats C's eps guess (S/eps are a known confusable pair) and A's plain-with-marks read, which is internally inconsistent (plain boxes elsewhere on this leaf carry no marks)"),
    ('17', '5'): ('_', '', 'C', "B itself flags this as 'genuinely uncertain' and entertains a plain connecting ligature rather than a full sign; A's g call needs a loop B says isn't there; C's independent 'stray stroke, no codebook match' read is the most conservative and matches B's own doubt"),
    ('17', '9'): ('f', '', 'B', "B's stroke-order description (vertical, small loop near top, horizontal crossbar lower) matches the f atlas more precisely than C's p guess (f/p are a close confusable pair); overrides A's y"),
    ('18', '1'): ('_', '', 'B', "B's reading that this begins the word 'Parti' continuing into pos2-4 is corroborated by C's own independent plain reads of 18/2 ('pa') and 18/4 ('rtn') in this same pass, which together spell the same word"),
}

settled = []
n_c_agrees = 0
n_three_way = 0
for r in dis:
    key = (r['line'], r['pos'])
    ra, rb, rc = A.get(key), B.get(key), C.get(key)
    ca = ra['code'].strip() if ra else 'MISSING'
    cb = rb['code'].strip() if rb else 'MISSING'
    cc = rc['code'].strip()
    ma = ra['marks'].strip() if ra else ''
    mb = rb['marks'].strip() if rb else ''
    mc = rc['marks'].strip()

    if cc == ca or cc == cb:
        n_c_agrees += 1
    if len({ca, cb, cc}) == 3:
        n_three_way += 1
        ov_code, ov_marks, ov_kept, ov_reason = THREE_WAY_OVERRIDE[key]
        code, marks = ov_code, ov_marks
        source = f'3-way->{ov_kept}'
        reason = f'A={ca} B={cb} C={cc}, all differ; {ov_reason}'
    elif ca == cb:
        code, marks, source = ca, ma, 'AB'
        reason = f'A and B agree ({ca}); C read {cc} independently ({rc["note"]})' if cc != ca else f'A, B and C all agree ({ca})'
    elif cc == ca:
        code, marks, source = ca, ma, 'AC'
        reason = f'C agrees with A ({ca}) against B ({cb}): {rc["note"]}'
    elif cc == cb:
        code, marks, source = cb, mb, 'BC'
        reason = f'C agrees with B ({cb}) against A ({ca}): {rc["note"]}'
    else:
        raise AssertionError(key)
    settled.append((r['line'], r['pos'], code, marks, source, reason))

with open('recon_box_f55v/settled.tsv', 'w') as f:
    f.write('line\tpos\tcode\tmarks\tsource\treason\n')
    for row in settled:
        f.write('\t'.join(row) + '\n')

print(f'{len(dis)} disagreement rows settled')
print(f'C agrees with A or B: {n_c_agrees}/{len(dis)} = {100*n_c_agrees/len(dis):.1f}%')
print(f'three-way splits (A, B, C all differ): {n_three_way}')
from collections import Counter
print('source counts:', Counter(s[4] for s in settled))
