#!/usr/bin/env python3
"""AX2-4612 (26 Sept 2026): build ciphertext_4612_v3.tsv from v2 plus this session's settlement of the
16 remaining numeral disagreements in ax4612tr/settle.tsv, checked against images_wv2/crops_4612/
src_04612_p{1,2}.png directly (see NOTES.md AX2-4612). Reuses build_v2.py's logic and its 16 prior
settlements unchanged; adds this session's 16 (SETTLEMENTS_V3) and one insert-only case (row p1_r04
pos27, a token present only in passB with no passA counterpart at all -- passA missed a numeral tucked
at the very right margin; INSERT_SETTLEMENTS, keyed by (page, b_line, b_pos) since an insert-only token
has no a_line/a_pos).

Same column convention as v2 (line, position, sign, confidence, alt, why); confidence S for every
settled numeral (checked directly against the image this session), M unchanged for anything still open
(none remain among the 16 named in the brief)."""
import csv, difflib

BASE = 'ax4612tr/'

from build_v2 import SETTLEMENTS as SETTLEMENTS_V2, load_flat, norm, norm_loose

# This session's 16 settlements (AX2-4612, 26 Sept 2026), each checked directly against
# images_wv2/crops_4612/src_04612_p1.png at 3-6x zoom (see NOTES.md AX2-4612 for the crop coordinates
# and the specific glyph comparison for each). All 16 of settle.tsv's '?' rows are resolved here.
SETTLEMENTS_V3 = dict(SETTLEMENTS_V2)
SETTLEMENTS_V3.update({
    ('p1', 'p1_r04', 12): ('81', 'settled-image(AX2-4612): own zoom confirms passB 81 (loop-8 shape matches the "81" at r04 pos17, distinct from the "31" shapes beside it); passA misread the digit-shape (8/5-like confusion)'),
    ('p1', 'p1_r05', 21): ('13', 'settled-image(AX2-4612): own zoom confirms passB 13; passA misread'),
    ('p1', 'p1_r06', 18): ('34', 'settled-image(AX2-4612): own zoom confirms passB 34; passA misread 74'),
    ('p1', 'p1_r09', 5): ('22', 'settled-image(AX2-4612): own zoom confirms passB 22; passA misread 28'),
    ('p1', 'p1_r10', 3): ('10', 'settled-image(AX2-4612): own zoom confirms passA 10 (straight "1" stroke, not the curved "2"); passB misread 20'),
    ('p1', 'p1_r10', 4): ('38', 'settled-image(AX2-4612): own zoom confirms passA 38 (looped "3", not the straight-diagonal "7"); passB misread 78'),
    ('p1', 'p1_r10', 25): ('38', 'settled-image(AX2-4612): own zoom confirms passA 38 (last token of the line, before the paragraph-end dash); passB misread 88'),
    ('p1', 'p1_r22', 20): ('34', 'settled-image(AX2-4612): own zoom confirms passA 34; passB misread 84'),
    ('p1', 'p1_r22', 22): ('23', 'settled-image(AX2-4612): own zoom confirms passA 23; passB misread 28'),
    ('p1', 'p1_r23', 7): ('150', 'settled-image(AX2-4612): own zoom confirms passB 150 (rounded "5" loop, matches "150" elsewhere on the page, distinct from the "3" in the neighbouring "138"); passA misread 130'),
    ('p1', 'p1_r26', 7): ('51', 'settled-image(AX2-4612): own zoom confirms passA 51 (open "5" hook, distinct from the "8" double-loop at the next position); passB misread 81'),
    ('p1', 'p1_r26', 8): ('84', 'settled-image(AX2-4612): own zoom confirms passB 84; passA misread 34'),
    ('p1', 'p1_r33', 22): ('=Wesel', 'settled-image(AX2-4612): own zoom shows a genuine cursive word here (a tall looping ascender, not a numeral shape), consistent with passB\'s clear-word reading "Wesel" (a Rhine town, plausible in this military context); passA misread the word as the numeral 109'),
    ('p1', 'p1_r35', 22): ('33', 'settled-image(AX2-4612): own zoom confirms passA 33 (two looped "3"s, both matching the "33" shape elsewhere on the page); passB misread 37'),
    ('p1', 'p1_r36', 4): ('51', 'settled-image(AX2-4612): own zoom confirms passA 51 (open "5" hook, distinct from "8"); passB misread 81'),
})

# The one insert-only disagreement (p1_disagreements.tsv line 23): passB's own r04 pos27 = "9", with
# no passA counterpart anywhere in the content alignment (passA's corresponding physical line, its own
# r03, ends at "...6, 25" -- 16 numerals -- while passB's r04 reads "...6, 25, 9", 17). Own zoom
# (row3_rightedge2.png) confirms a small "9" really is written at the extreme right margin, after the
# comma following "25", cut off in passA's crop.
INSERT_SETTLEMENTS = {
    ('p1', 'p1_r04', 27): ('9', 'settled-image(AX2-4612): own zoom confirms a small "9" at the right margin after "25,", present in the manuscript but missed by passA (not on a page-edge fold visible in the image; passA\'s own read simply stops one token short)'),
}


def build_page(page, a_path, b_path, drop_b_header=None):
    a = load_flat(a_path)
    b_all = load_flat(b_path)
    b = [row for row in b_all if row['line'] != drop_b_header] if drop_b_header else b_all
    a_keys = [norm(r['tok']) for r in a]
    b_keys = [norm(r['tok']) for r in b]
    sm = difflib.SequenceMatcher(a=a_keys, b=b_keys, autojunk=False)

    out = []
    synth_counter = {}

    def emit(line, pos, sign, confidence, alt, why):
        out.append({'line': line, 'position': pos, 'sign': sign, 'confidence': confidence, 'alt': alt, 'why': why})

    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            for k in range(i2 - i1):
                ra, rb = a[i1 + k], b[j1 + k]
                flagged = bool(ra['alt'].strip()) or bool(rb['alt'].strip())
                conf = 'M' if flagged else 'H'
                why = 'agree-flagged' if flagged else 'agree'
                emit(ra['line'], ra['pos'], ra['tok'], conf, '', why)
        elif tag == 'replace':
            n = max(i2 - i1, j2 - j1)
            for k in range(n):
                ai = i1 + k if i1 + k < i2 else None
                bj = j1 + k if j1 + k < j2 else None
                ra = a[ai] if ai is not None else None
                rb = b[bj] if bj is not None else None
                if ra is not None:
                    line, pos = ra['line'], ra['pos']
                else:
                    line, pos = rb['line'], rb['pos']
                key = (page, ra['line'], ra['pos']) if ra is not None else None
                settled = SETTLEMENTS_V3.get(key) if key else None
                a_tok = ra['tok'] if ra is not None else '(none)'
                b_tok = rb['tok'] if rb is not None else '(none)'
                if settled:
                    value, why = settled
                    emit(line, pos, value, 'S', f'A:{a_tok}|B:{b_tok}', why)
                elif ra is not None and rb is not None and norm_loose(a_tok) == norm_loose(b_tok) and a_tok.startswith('='):
                    value = a_tok if len(a_tok) >= len(b_tok) else b_tok
                    emit(line, pos, value, 'H', f'A:{a_tok}|B:{b_tok}', 'settled-case-only')
                else:
                    emit(line, pos, '?', 'M', f'A:{a_tok}|B:{b_tok}', 'unsettled-diff')
        elif tag == 'delete':
            for k in range(i1, i2):
                ra = a[k]
                key = (page, ra['line'], ra['pos'])
                settled = SETTLEMENTS_V3.get(key)
                if settled:
                    value, why = settled
                    emit(ra['line'], ra['pos'], value, 'S', f'A:{ra["tok"]}|B:(none)', why)
                else:
                    emit(ra['line'], ra['pos'], '?', 'M', f'A:{ra["tok"]}|B:(none)', 'unsettled-diff')
        elif tag == 'insert':
            for k in range(j1, j2):
                rb = b[j1 + (k - j1)]
                prev_line = out[-1]['line'] if out else rb['line']
                synth_counter[prev_line] = synth_counter.get(prev_line, 0) + 1
                pos = 1000 + synth_counter[prev_line]
                ins_key = (page, rb['line'], rb['pos'])
                settled = INSERT_SETTLEMENTS.get(ins_key)
                if settled:
                    value, why = settled
                    emit(prev_line, pos, value, 'S', f'A:(none)|B:{rb["tok"]}', why)
                else:
                    emit(prev_line, pos, '?', 'M', f'A:(none)|B:{rb["tok"]}', 'unsettled-diff-insert-only-in-B')
    return out


rows_p1 = build_page('p1', BASE + 'passA_p1.tsv', BASE + 'passB_p1.tsv', drop_b_header='p1_r01')
rows_p2 = build_page('p2', BASE + 'passA_p2.tsv', BASE + 'passB_p2.tsv')

with open('ciphertext_4612_v3.tsv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerow(['line', 'position', 'sign', 'confidence', 'alt', 'why'])
    for row in rows_p1 + rows_p2:
        w.writerow([row['line'], row['position'], row['sign'], row['confidence'], row['alt'], row['why']])

n = len(rows_p1) + len(rows_p2)
unsettled = sum(1 for r in rows_p1 + rows_p2 if r['sign'] == '?')
settled_this_session = sum(1 for r in rows_p1 + rows_p2 if 'AX2-4612' in r['why'])
print(f'ciphertext_4612_v3.tsv: {n} tokens, {unsettled} unsettled (?), {settled_this_session} settled this session (of 16 named in settle.tsv)')
