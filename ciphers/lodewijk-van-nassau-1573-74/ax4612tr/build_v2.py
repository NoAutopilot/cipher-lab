#!/usr/bin/env python3
"""AX-4612TR2: build ciphertext_4612_v2.tsv from the content-aligned passes plus this session's
settlements against images_wv2/crops_4612/src_04612_p{1,2}.png (see NOTES.md AX-4612TR2, settle.tsv).

Convention (matches the committed ciphertext_4612.tsv / ciphertext_4610.tsv):
  confidence H why=agree       -- both raw passes agree, neither flagged an alt
  confidence M why=agree-flagged -- both raw passes agree on the primary token, but one flagged an alt
  confidence S why=settled-image(AX-4612TR2) -- disagreement settled against the image this session
  sign '?' confidence M why=unsettled-diff -- disagreement NOT settled; alt carries both raw readings
Line/position follow passA's own numbering (the convention the old ciphertext_4612.tsv also used,
i.e. passA's line labels minus the header offset already present in passA); a token passB alone
inserted is appended to the end of the passA line it falls inside, at a new synthetic position.
"""
import csv, difflib

BASE = 'ax4612tr/'

def load_flat(path):
    rows = []
    with open(path, encoding='utf-8') as f:
        r = csv.DictReader(f, delimiter='\t')
        for row in r:
            rows.append({'line': row['line'], 'pos': int(row['position']), 'tok': row['token'], 'alt': row.get('alt') or ''})
    return rows

def norm(tok):
    return tok.strip().lower()

def norm_loose(tok):
    """Case/trailing-punctuation-insensitive form, for auto-settling clear-word spelling variants
    (vre./vre, lre./lre) that are not really disagreements needing an image check."""
    return tok.strip().lower().rstrip('.,;:')

# (page, a_line, a_pos) -> (settled_value, why)
SETTLEMENTS = {
    ('p1', 'p1_r04', 26): ('68', 'settled-image(AX-4612TR2): passB 68 confirmed, passA misread 67'),
    ('p1', 'p1_r06', 6): ('84', 'settled-image(AX-4612TR2): passB 84 confirmed, passA garbled "8A"'),
    ('p1', 'p1_r06', 12): ('118', 'settled-image(AX-4612TR2): passB 118 confirmed, passA misread 113'),
    ('p1', 'p1_r07', 7): ('83', 'settled-image(AX-4612TR2): passB 83 confirmed, passA misread 53'),
    ('p1', 'p1_r07', 8): ('97', 'settled-image(AX-4612TR2): passB 97 confirmed, passA misread 74'),
    ('p1', 'p1_r09', 11): ('13', 'settled-image(AX-4612TR2): passB 13 confirmed (compact glyph), passA misread 113'),
    ('p1', 'p1_r11', 15): ('150', 'settled-image(AX-4612TR2): passB 150 confirmed, passA misread 130'),
    ('p1', 'p1_r14', 23): ('135', 'settled-image(AX-4612TR2): passB 135 confirmed, passA misread 133'),
    ('p1', 'p1_r15', 2): ('34', 'settled-image(AX-4612TR2): passB 34 confirmed, passA misread 74'),
    ('p1', 'p1_r15', 16): ('73', 'settled-image(AX-4612TR2): passB 73, moderate confidence, passA misread 77'),
    ('p1', 'p1_r17', 9): ('87', 'settled-image(AX-4612TR2): passA 87 confirmed, passB misread 37'),
    ('p2', 'p2_r07', 12): ('83', 'settled-image(AX-4612TR2): passB 83 confirmed, passA misread 33'),
    ('p2', 'p2_r08', 3): ('83', 'settled-image(AX-4612TR2): passB 83 confirmed, passA misread 33'),
    ('p2', 'p2_r08', 13): ('120', 'settled-image(AX-4612TR2): passB 120 confirmed, passA misread 12'),
    ('p2', 'p2_r09', 15): ('25', 'settled-image(AX-4612TR2): passB 25 confirmed, passA misread 15'),
    ('p2', 'p2_r21', 6): ('=1574', 'settled-image(AX-4612TR2): clear-text date, both passes read the same value'),
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
                settled = SETTLEMENTS.get(key) if key else None
                a_tok = ra['tok'] if ra is not None else '(none)'
                b_tok = rb['tok'] if rb is not None else '(none)'
                if settled:
                    value, why = settled
                    emit(line, pos, value, 'S', f'A:{a_tok}|B:{b_tok}', why)
                elif ra is not None and rb is not None and norm_loose(a_tok) == norm_loose(b_tok) and a_tok.startswith('='):
                    # a clear-word spelling/case/punctuation variant, not a real disagreement
                    value = a_tok if len(a_tok) >= len(b_tok) else b_tok
                    emit(line, pos, value, 'H', f'A:{a_tok}|B:{b_tok}', 'settled-case-only')
                else:
                    emit(line, pos, '?', 'M', f'A:{a_tok}|B:{b_tok}', 'unsettled-diff')
        elif tag == 'delete':
            for k in range(i1, i2):
                ra = a[k]
                key = (page, ra['line'], ra['pos'])
                settled = SETTLEMENTS.get(key)
                if settled:
                    value, why = settled
                    emit(ra['line'], ra['pos'], value, 'S', f'A:{ra["tok"]}|B:(none)', why)
                else:
                    emit(ra['line'], ra['pos'], '?', 'M', f'A:{ra["tok"]}|B:(none)', 'unsettled-diff')
        elif tag == 'insert':
            for k in range(j1, j2):
                rb = b[j1 + (k - j1)]
                # append to the end of the preceding passA line, synthetic position
                prev_line = out[-1]['line'] if out else rb['line']
                synth_counter[prev_line] = synth_counter.get(prev_line, 0) + 1
                pos = 1000 + synth_counter[prev_line]
                emit(prev_line, pos, '?', 'M', f'A:(none)|B:{rb["tok"]}', 'unsettled-diff-insert-only-in-B')
    return out

rows_p1 = build_page('p1', BASE + 'passA_p1.tsv', BASE + 'passB_p1.tsv', drop_b_header='p1_r01')
rows_p2 = build_page('p2', BASE + 'passA_p2.tsv', BASE + 'passB_p2.tsv')

with open('ciphertext_4612_v2.tsv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerow(['line', 'position', 'sign', 'confidence', 'alt', 'why'])
    for row in rows_p1 + rows_p2:
        w.writerow([row['line'], row['position'], row['sign'], row['confidence'], row['alt'], row['why']])

n = len(rows_p1) + len(rows_p2)
unsettled = sum(1 for r in rows_p1 + rows_p2 if r['sign'] == '?')
print(f'ciphertext_4612_v2.tsv: {n} tokens, {unsettled} unsettled (?)')
