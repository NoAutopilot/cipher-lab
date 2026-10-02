#!/usr/bin/env python3
"""Item 3868 (PRO 30/55/33/65; recipient copy BL Add MS 21807 = Brymner B.147): Clinton to Haldimand, New York,
12 Nov 1781. The period decipherment on B.147 pp.385-386 (H-1649 Images 1033-1034) read, and the first two cipher
columns of the cipher copy on p.382 (Image 1030) checked against it on the 1778 Army List title-page key
(GAPS8-pro3055-clinton-1779, 2 Oct 2026).

Inputs: p385_reconciled.tsv (two blind Sonnet passes p385_passA.tsv / p385_passB.tsv, reconciled by the worker on a
montage of the disputed crops and the 1600 px region overlay; row per line crop: crop, passA, passB, reconciled, note),
p382_cells.tsv (the two cipher columns, both passes; glosses in quotes), title1778_reading.txt (the key book page),
key_2894.tsv (the key cells recovered from item 2894), vhs2_3868_print.txt (the letter as printed in Collections of
the Vermont Historical Society vol. II, 1871, pp.198-199, archive.org OCR).

Grades (rule 4): a word of the decipherment read the same by both passes, or settled at reconciliation, is H (a period
decipherment in the manuscript is a key-source reading); a word carrying [?] is M. A cipher cell whose 1778-page letter
equals the decipherment letter it stands for is C (known plaintext).

Key check: each cell (line, pos) is looked up on the 1778 title page (letters and & counted, as title_1778_check.py)
and compared with the letter of the decipherment word it enciphers. The alignment is by the copyist's own glosses:
the cells between two glosses spell the decipherment words between them ("of your proclamation" | and | "of the
letter" | marked | "a" ; to the | "minister" | not | "having time to" | prepare | "copies"). "proclamation" is reported
apart (9 cells for a 12-letter word; the decipherment itself writes "proclama^n" with a marginal *Sic). Control on the
statistic's own axis: the decipherment body's letters shuffled (1000 seeds) and compared at the same 44 positions,
so the control changes exactly the plaintext side of each comparison and can fail where the target passes.

Print comparison (rule 10, a search result only): word-level difflib between the reading (body, without the P.S.) and
the printed body; counts of equal words and the differing spans.

Outputs: p385_reading.txt, check_3868.json. --check re-derives both and exits 1 when a committed output differs (rule 7).
"""
import difflib, json, os, random, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)


def rows(path):
    out, hdr = [], None
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line or line.startswith('#'):
            continue
        parts = line.split('\t')
        if hdr is None:
            hdr = parts
            continue
        out.append(dict(zip(hdr, parts + [''] * (len(hdr) - len(parts)))))
    return out


def chars(s):
    return [c.lower() for c in s if c.isalpha() or c == '&']


def words(s):
    return [x for x in (re.sub(r'[^a-z0-9&]', '', w.lower()) for w in s.replace('[?]', '').split()) if x]


SEGMENTS = [  # (column, cells between glosses, decipherment words they spell)
    ('p382_col1', 'of your', 'proclamation'),
    ('p382_col1', 'of the letter', None),
    ('p382_col1', 'a', None),
    ('p382_col2', 'minister', None),
    ('p382_col2', 'having time to', None),
    ('p382_col2', 'copies', None),
]


def build():
    rec = rows(P('p385_reconciled.tsv'))
    grades = {'H': 0, 'M': 0}
    body_lines, ps_lines = [], []
    for r in rec:
        t = r['reconciled']
        for w in re.sub(r'[{}]', ' ', t).split():
            if w in ('-',):
                continue
            grades['M' if '[?]' in w else 'H'] += 1
        (ps_lines if r['crop'] in ('p386_L06', 'p386_L07', 'p386_L08', 'p386_L09') else body_lines).append(t)
    agree = sum(1 for r in rec if words(r['passA']) == words(r['passB']))
    wd = sum(max(i2 - i1, j2 - j1) for r in rec for t, i1, i2, j1, j2 in
             difflib.SequenceMatcher(None, words(r['passA']), words(r['passB'])).get_opcodes() if t != 'equal')
    wt = sum(len(words(r['passA'])) for r in rec)
    reading = ['# B.147 pp.385-386 (H-1649 Images 1033-1034), BL Add MS 21807: period decipherment of Clinton to Haldimand,',
               '# New York, 12 Nov 1781 (item 3868; cipher on p.382 = Image 1030). Two blind Sonnet passes reconciled on the crops',
               '# (passes/p385_reconciled.tsv). Spelling as written; {..} = interlinear; [?] = M-graded word. P.S. after the blank line.']
    reading += body_lines + [''] + ps_lines

    # key check
    title = [l.rstrip('\n') for l in open(P('title1778_reading.txt'), encoding='utf-8')
             if not l.startswith('#') and l.strip()]
    cells = rows(P('p382_cells.tsv'))
    segs, cur, col = [], [], None
    for c in cells:
        if c['col'] != col:
            if cur:
                segs.append((col, cur))
            col, cur = c['col'], []
        e = c['entry']
        if e.startswith('"'):
            if cur:
                segs.append((col, cur))
            cur = []
            continue
        cur.append(e)
    if cur:
        segs.append((col, cur))
    assert len(segs) == len(SEGMENTS), (len(segs), segs)
    look = []  # (segment index, pair, page letter)
    for si, (col, entries) in enumerate(segs):
        line = None
        for e in entries:
            a, b = e.split('-')
            if a:
                line = int(a)
            pos = int(b)
            cl = chars(title[line - 1])
            look.append((si, f'{line}-{pos}', cl[pos - 1] if pos <= len(cl) else None))
    compared, procl = [], []
    for si, (col, plain, extra) in enumerate(SEGMENTS):
        page = [x for x in look if x[0] == si]
        target = ''.join(plain.split())
        if extra:
            n = len(target)
            compared += [(p, pl) for p, pl in zip(page[:n], target)]
            procl = page[n:]
        else:
            assert len(page) == len(target), (plain, len(page))
            compared += [(p, pl) for p, pl in zip(page, target)]
    match = sum(1 for (_, _, a), b in compared if a == b)
    body_letters = chars(' '.join(body_lines))
    rng = random.Random(1781)
    null = []
    for _ in range(1000):
        sh = body_letters[:]
        rng.shuffle(sh)
        null.append(sum(1 for ((_, _, a), _), b in zip(compared, sh) if a == b))
    null.sort()
    k2894 = {(int(r['line']), int(r['pos'])): r['letter'] for r in rows(P('key_2894.tsv'))}
    distinct = {tuple(map(int, pr.split('-'))): a for _, pr, a in look}
    ov = {k: v for k, v in distinct.items() if k in k2894}
    ov_agree = sum(1 for k, v in ov.items() if k2894[k] == v)

    # print comparison
    pr = [l for l in open(P('vhs2_3868_print.txt'), encoding='utf-8') if not l.startswith('#')]
    ptxt = ' '.join(pr)
    i0 = ptxt.index('I  received')
    i1 = ptxt.index('mitted.')
    ptxt = re.sub(r'\^  Note.*?Same,  290\.', ' ', ptxt[i0:i1 + 7], flags=re.S)
    ptxt = re.sub(r'G-overnor  Chittenden  to  General  Washington\.  199', ' ', ptxt)
    ptxt = re.sub(r'(\w)-\s+(\w)', r'\1\2', ptxt)  # OCR line-end hyphens
    pw = words(ptxt)
    rw = words(re.sub(r'\{[^}]*\}', ' ', ' '.join(body_lines)))
    sm = difflib.SequenceMatcher(None, rw, pw, autojunk=False)
    eq = sum(i2 - i1 for t, i1, i2, j1, j2 in sm.get_opcodes() if t == 'equal')
    diffs = [f"{' '.join(rw[i1:i2]) or '-'} | {' '.join(pw[j1:j2]) or '-'}"
             for t, i1, i2, j1, j2 in sm.get_opcodes() if t != 'equal']
    out = {
        'source': 'H-1649 Images 1033 (p.385) and 1034 (p.386) full/max 5440x4056, crops images/h1649/p385_lines/, p386_lines/; cipher Image 1030 (p.382), images/h1649/p382_cols/',
        'lines': len(rec),
        'pass_agreement': f'{agree}/{len(rec)} lines and {wt - wd}/{wt} words identical between the two blind passes; most differences are words at the left edge the crops cut (settled on the 1600 px overlay)',
        'grades_words': grades,
        'key_check': {
            'cells_read': len(look),
            'cell_pass_agreement': '56/57 entries (one col1 repeat "-4" read once by pass B)',
            'compared_cells': len(compared),
            'page_letter_equals_decipherment_letter': match,
            'shuffled_plaintext_control': {'seeds': 1000, 'mean': round(sum(null) / len(null), 3),
                                           'p95': null[949], 'max': null[-1]},
            'proclamation_cells': {'pairs': [p for _, p, _ in procl], 'page_letters': ''.join(a or '?' for _, _, a in procl),
                                   'note': 'the cells after "of your" spell "proclatio" against the decipherment "proclama^n" (*Sic): 6 of 9 agree with p-r-o-c-l-a, the encipherer skipped "ma" and the n, or wrote 18-4 t for 18-7 m'},
            'grade_C_cells': match,
        },
        'same_key_as_2894': {'distinct_cells': len(distinct), 'also_in_key_2894': len(ov), 'agree': ov_agree},
        'print_comparison': {
            'printed_in': 'Collections of the Vermont Historical Society vol. II (1871) pp.198-199 (archive.org collectionsofver02vermuoft); same phrase also in Walton, Records of the Governor and Council of Vermont vol. II, and Wilbur, Ira Allen (1928), per one be-api fts query',
            'reading_body_words': len(rw), 'printed_body_words': len(pw), 'equal_words_in_order': eq,
            'differing_spans_reading_vs_print': diffs,
        },
    }
    return '\n'.join(reading) + '\n', json.dumps(out, indent=1) + '\n'


def main():
    reading, js = build()
    targets = [(P('p385_reading.txt'), reading), (P('check_3868.json'), js)]
    if '--check' in sys.argv:
        bad = [p for p, t in targets if not os.path.exists(p) or open(p, encoding='utf-8').read() != t]
        for p in bad:
            print('STALE', os.path.basename(p))
        print('check_3868: ' + ('FAIL' if bad else 'OK'))
        sys.exit(1 if bad else 0)
    for p, t in targets:
        open(p, 'w', encoding='utf-8').write(t)
    print(js)


if __name__ == '__main__':
    main()
