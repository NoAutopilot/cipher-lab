#!/usr/bin/env python3
"""B.148 p.102 (H-1649 Image 1183): the period decipherment of Carleton to Haldimand, New York, 25 Sept 1782, and the
key check of the p.123 cipher copy against it (GAPS7-pro3055-clinton-1779, 2 Oct 2026).

Inputs: p102_reconciled.tsv (two blind Sonnet passes, p102_passA.tsv / p102_passB.tsv, reconciled by the worker on the
crops; one row per crop: crop, passA, passB, reconciled, grade, note), p123_cells.tsv (the p.123 cipher cells on disk:
S. Tomokiyo's f.123 extract and the GAPS6 first-column read), title1778_reading.txt (the 1778 title page, the key book),
key_2894.tsv (the key cells recovered from item 2894).

Grades (rule 4): every word of the decipherment body read the same by both passes, or settled on the crop at
reconciliation, is H (a period decipherment in the manuscript is a key-source reading); a word still open is M. Key cells
of p.123 matched to the decipherment's own letters are C (known plaintext).

Key check: each p.123 letter cell (line, pos) is looked up on the 1778 title page (letters and & counted, as
title_1778_check.py) and compared with the decipherment letter it enciphers (alignment: "Congress" 8 letters, the two
word-code elements "and" "the", then "Pensylvania" 11 letters -- the order of Tomokiyo's extract). Control on the
statistic's own axis: the decipherment's body letters shuffled (1000 seeds) and the same 19 positions compared, so the
control changes exactly the plaintext side of each comparison. Overlap with key_2894.tsv is reported as agreement on the
cells both carry.

Outputs: p102_reading.txt, check_p102.json. --check re-derives both and exits 1 when a committed output differs (rule 7).
"""
import json, os, random, re, sys

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


def build():
    rec = rows(P('p102_reconciled.tsv'))
    body = [r for r in rec if r['crop'].startswith('p102_text_')]
    grades = {'H': 0, 'M': 0}
    lines = []
    for r in body:
        text = r['reconciled']
        for w in text.split():
            g = 'M' if '[?]' in w else 'H'
            grades[g] += 1
        lines.append(text)
    other = [r for r in rec if not r['crop'].startswith('p102_text_')]
    other_tokens = {'H': 0, 'M': 0}
    for r in other:
        for w in r['reconciled'].replace(' / ', ' ').split():
            other_tokens['M' if '[?]' in w else 'H'] += 1
    norm = lambda t: [x for x in (re.sub(r'[^a-z0-9&]', '', w.lower().replace('[?]', ''))
                                  for w in t.replace('^', '').split()) if x]
    agree = sum(1 for r in body if norm(r['passA']) == norm(r['passB']))
    import difflib
    wdiff = sum(max(i2 - i1, j2 - j1) for r in body for t, i1, i2, j1, j2 in
                difflib.SequenceMatcher(None, norm(r['passA']), norm(r['passB'])).get_opcodes() if t != 'equal')
    wtot = sum(len(norm(r['passA'])) for r in body)
    reading = ['# B.148 p.102 (H-1649 Image 1183), BL Add MS 21808: period decipherment of Carleton to Haldimand,',
               '# New York, 25 Sept 1782 (Tomokiyo: "decoded on f.102"). Two blind Sonnet passes reconciled on the crops',
               '# (passes/p102_reconciled.tsv). Spelling as written; ^ = raised letters; [?] = M-graded word.']
    reading += lines

    # key check
    title = [l.rstrip('\n') for l in open(P('title1778_reading.txt'), encoding='utf-8')
             if not l.startswith('#') and l.strip()]
    cells = rows(P('p123_cells.tsv'))
    text = ' '.join(lines)
    m = re.search(r'Congress and the Pensylvania', text)
    assert m, 'decipherment opening not found'
    plain_letters = list('congress') + list('pensylvania')
    word_plain = ['and', 'the']
    letter_cells = [c for c in cells if c['kind'] == 'letter']
    word_cells = [c for c in cells if c['kind'] == 'word']
    assert len(letter_cells) == len(plain_letters)
    page = []
    for c in letter_cells:
        ln, pos = int(c['line']), int(c['pos'])
        cl = chars(title[ln - 1])
        page.append(cl[pos - 1] if pos <= len(cl) else None)
    match = sum(1 for a, b in zip(page, plain_letters) if a == b)
    tom = sum(1 for c, b in zip(letter_cells, plain_letters) if c['tomokiyo'] == b)
    words_ok = sum(1 for c, w in zip(word_cells, word_plain) if c['tomokiyo'] == w)
    body_letters = [c for c in chars(text)]
    rng = random.Random(1782)
    null = []
    for _ in range(1000):
        sh = body_letters[:]
        rng.shuffle(sh)
        null.append(sum(1 for a, b in zip(page, sh[:len(page)]) if a == b))
    null.sort()
    k2894 = {}
    for r in rows(P('key_2894.tsv')):
        k2894[(int(r['line']), int(r['pos']))] = r['letter']
    distinct = {}
    for c, a in zip(letter_cells, page):
        distinct[(int(c['line']), int(c['pos']))] = a
    overlap = {k: v for k, v in distinct.items() if k in k2894}
    ov_agree = sum(1 for k, v in overlap.items() if k2894[k] == v)
    out = {
        'source': 'H-1649 Image 1183 (B.148 p.102), full/max 5536x4056, crops images/h1649/p102_lines/',
        'body_lines': len(lines),
        'pass_agreement': f'{agree}/{len(body)} body lines and {wtot - wdiff}/{wtot} words identical between the two blind passes (raised-letter marks and punctuation set aside); the 3 differing words settled at reconciliation',
        'grades_body_words': grades,
        'grades_margin_header_tokens': other_tokens,
        'key_check': {
            'letter_cells': len(page),
            'page_letter_equals_decipherment_letter': match,
            'shuffled_plaintext_control': {'seeds': 1000, 'mean': round(sum(null) / len(null), 3),
                                           'p95': null[949], 'max': null[-1]},
            'tomokiyo_letters_equal_decipherment': tom,
            'word_code_elements_equal_decipherment_words': f'{words_ok}/{len(word_cells)}',
            'head_pair_3-4': 'no letter value (line 3 has 1 character); Tomokiyo d-?; the decipherment starts at Congress',
            'grade_C_cells': match + words_ok,
        },
        'same_key_as_2894': {'distinct_letter_cells': len(distinct), 'also_in_key_2894': len(overlap),
                             'agree': ov_agree},
    }
    return '\n'.join(reading) + '\n', json.dumps(out, indent=1) + '\n'


def main():
    reading, js = build()
    targets = [(P('p102_reading.txt'), reading), (P('check_p102.json'), js)]
    if '--check' in sys.argv:
        bad = [p for p, t in targets if not os.path.exists(p) or open(p, encoding='utf-8').read() != t]
        for p in bad:
            print('STALE', os.path.basename(p))
        print('check_p102: ' + ('FAIL' if bad else 'OK'))
        sys.exit(1 if bad else 0)
    for p, t in targets:
        open(p, 'w', encoding='utf-8').write(t)
    print(js)


if __name__ == '__main__':
    main()
