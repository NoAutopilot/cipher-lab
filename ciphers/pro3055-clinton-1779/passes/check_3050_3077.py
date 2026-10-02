#!/usr/bin/env python3
"""Items 3050 (PRO 30/55/26/2; Clinton to Haldimand, New York, 2 Oct 1780) and 3077 (PRO 30/55/26/30; same, 18 Oct 1780):
their period decipherments on B.147 p.245 (H-1649 Image 889) and p.246 (Image 890) read, and the first cipher columns of
the cipher copies on p.242 (Image 886, columns 1-3) and p.247 (Image 891, columns 1-2) checked against them on the 1778
Army List title-page key (GAPS12-pro3055-clinton-1779, 2 Oct 2026; method as check_3868.py / check_2380.py).

Inputs: p245_246_reconciled.tsv (two blind Sonnet passes p245_246_passA.tsv / passB.tsv on 68 line crops of the 1600 px
frames, reconciled by the worker on one montage), p242_p247_cells.tsv (the five cipher columns, reconciled on a 3x montage;
"|" = the copyist's underline closing a cipher word), title1778_reading.txt (the key page), key_2894.tsv (cells from 2894).

Grades (rule 4): a decipherment word read the same by both passes or settled at reconciliation is H; [?] is M. A cipher
cell whose 1778-page letter equals the decipherment letter it stands for is C.

Alignment (fixed before any comparison, from the underlines and the clear words in the columns, never from the key's
output): cipher word k of a column segment <-> decipherment word k of the span named in SPANS. A cipher word is compared
letter by letter when its cell count equals the decipherment word's length (or its length with doubled letters written once);
otherwise it is listed as unequal and left out. Cells beyond the end of their title line (no letter there) are left out
and listed. Control on the statistic's own axis: the decipherments' letters shuffled (1000 seeds) and compared at the
same positions, so the control changes the plaintext side of every comparison and can fail where the target passes.

Outputs: p245_reading.txt, p246_reading.txt, check_3050_3077.json. --check re-derives them and exits 1 when stale (rule 7).
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
    return re.sub(r'[^a-z&]', '', s.lower())


def collapse(w):
    return re.sub(r'(.)\1+', r'\1', w)


def words(s):
    return [x for x in (re.sub(r'[^a-z0-9&]', '', w.lower()) for w in s.replace('[?]', '').split()) if x]


LETTERS = {
    '3050': {'page': 'p245', 'body': range(1, 21), 'endorse': range(24, 29),
             'head': ['# B.147 p.245 (H-1649 Image 889), BL Add MS 21807 fo.208: period decipherment ("Duplicate") of Clinton to',
                      '# Haldimand, New York, 2 Oct 1780 (item 3050, PRO 30/55/26/2; cipher copy on pp.242-244 = Images 886-888, duplicate',
                      '# p.239). Two blind Sonnet passes reconciled on the crops (passes/p245_246_reconciled.tsv); margin notes left out.',
                      '# Endorsement after the blank line.']},
    '3077': {'page': 'p246', 'body': range(1, 36), 'endorse': range(36, 37),
             'head': ['# B.147 p.246 (H-1649 Image 890), BL Add MS 21807 fo.209: period decipherment of Clinton to Haldimand, New York,',
                      '# 18 Oct 1780 (item 3077, PRO 30/55/26/30; cipher copy on p.247 = Image 891, opening in clear). Two blind Sonnet',
                      '# passes reconciled on the crops (passes/p245_246_reconciled.tsv); margin notes left out. Endorsement after the blank line.']},
}
# column segment -> (letter, decipherment words the cipher words of that segment stand for; None = no counterpart)
SPANS = [
    ('p242_col1', 0, '3050', ['general', 'arnold', 'discovered', None]),
    ('p242_col2', 0, '3050', ['an', 'intention', 'of', 'giving', 'up', 'the']),
    ('p242_col3', 0, '3050', ['forts']),
    ('p242_col3', 1, '3050', ['west', 'point', 'was', 'obliged']),
    ('p247_col1', 0, '3077', ['for']),
    ('p247_col1', 1, '3077', ['miscarriage', 'of', 'the', 'quebec', 'fleet']),
    ('p247_col1', 2, '3077', ['part']),
    ('p247_col2', 0, '3077', ['of', 'which', 'has', 'been', 'taken']),
]


def build():
    rec = {r['crop']: r for r in rows(P('p245_246_reconciled.tsv'))}
    agree_lines = sum(1 for r in rec.values() if words(r['passA']) == words(r['passB']))
    outputs, summary, bodies = {}, {}, {}
    for item, d in LETTERS.items():
        body = [rec[f"{d['page']}_L{i:02d}"]['reconciled'] for i in d['body']]
        body = [t for t in body if t != '(blank)']
        endorse = [rec[f"{d['page']}_L{i:02d}"]['reconciled'] for i in d['endorse']]
        g = {'H': 0, 'M': 0}
        for t in body:
            for w in t.split():
                if w in ('-', '/'):
                    continue
                g['M' if '[?]' in w else 'H'] += 1
        bodies[item] = ' '.join(body)
        outputs[P(f"{d['page']}_reading.txt")] = '\n'.join(d['head'] + body + [''] + endorse) + '\n'
        summary[item] = {'body_words': sum(g.values()), 'grades_words': g}

    title = [chars(l) for l in open(P('title1778_reading.txt'), encoding='utf-8') if not l.startswith('#') and l.strip()]
    segs = {}  # (column, segment index) -> list of cipher words, each a list of (line, pos); clear words split segments
    by_col = {}
    for c in rows(P('p242_p247_cells.tsv')):
        by_col.setdefault(c['col'], []).append(c['entry'].strip())
    for col, entries in by_col.items():
        si, cw, cur, line = 0, [], [], None
        for e in entries:
            if e.startswith('"'):
                if cur:
                    cw.append(cur); cur = []
                if cw:
                    segs[(col, si)] = cw; si += 1; cw = []
                continue
            a, b = e.rstrip('|').split('-')
            if a:
                line = int(a)
            cur.append((line, int(b)))
            if e.endswith('|'):
                cw.append(cur); cur = []
        if cur:
            cw.append(cur)
        if cw:
            segs[(col, si)] = cw
    compared, unequal, beyond, extra = [], [], [], []
    for col, si, item, plain in SPANS:
        cws = segs[(col, si)]
        assert len(cws) == len(plain), (col, si, len(cws), len(plain))
        for cells, w in zip(cws, plain):
            letters = ''.join(title[l - 1][p - 1] if p <= len(title[l - 1]) else '?' for l, p in cells)
            if w is None:
                extra.append({'column': col, 'cells': [f'{l}-{p}' for l, p in cells], 'page_letters': letters})
                continue
            if len(cells) == len(w):
                tgt = w
            elif len(cells) == len(collapse(w)):
                tgt = collapse(w)
            else:
                unequal.append({'decipherment_word': w, 'cells': [f'{l}-{p}' for l, p in cells], 'page_letters': letters})
                continue
            for (l, p), ch in zip(cells, tgt):
                if p > len(title[l - 1]):
                    beyond.append({'word': w, 'cell': f'{l}-{p}', 'stands_for': ch})
                    continue
                compared.append((item, l, p, ch, w))

    def stat(letters):
        return sum(1 for (_, l, p, _, _), ch in zip(compared, letters) if title[l - 1][p - 1] == ch)
    per = {it: sum(1 for (i, l, p, ch, _) in compared if i == it and title[l - 1][p - 1] == ch) for it in LETTERS}
    tot = {it: sum(1 for x in compared if x[0] == it) for it in LETTERS}
    match = stat([x[3] for x in compared])
    pool = list(chars(' '.join(bodies.values())))
    rng = random.Random(1780)
    null = []
    for _ in range(1000):
        rng.shuffle(pool)
        null.append(stat(pool[:len(compared)]))
    null.sort()
    k2894 = {(int(r['line']), int(r['pos'])): r['letter'] for r in rows(P('key_2894.tsv'))}
    distinct = {(l, p): title[l - 1][p - 1] for _, l, p, _, _ in compared}
    ov = [k for k in distinct if k in k2894]
    off = [{'word': w, 'cell': f'{l}-{p}', 'page': title[l - 1][p - 1], 'decipherment': ch}
           for _, l, p, ch, w in compared if title[l - 1][p - 1] != ch]
    # how far the reconciled cells rest on the blind passes alone (the reconciler knew the key and the decipherment)
    def pass_cols(path):
        cols, on = {}, False
        for line in open(path, encoding='utf-8'):
            if line.startswith('#COLUMNS'):
                on = True; continue
            q = line.rstrip('\n').split('\t')
            if on and len(q) >= 3 and q[0] != 'crop' and not q[2].startswith('"') and q[2] != '_':
                cols.setdefault(q[0].split('/')[-1].replace('.jpg', '').replace('_L01', ''), []).append(q[2])
        return cols
    pa, pb = pass_cols(P('p245_246_passA.tsv')), pass_cols(P('p245_246_passB.tsv'))
    both = total_cells = 0
    for col, entries in by_col.items():
        rc = [e.rstrip('|') for e in entries if not e.startswith('"')]
        total_cells += len(rc)
        ok = []
        for ps in (pa.get(col, []), pb.get(col, [])):
            sm = difflib.SequenceMatcher(None, rc, ps, autojunk=False)
            ok.append({i for t, i1, i2, j1, j2 in sm.get_opcodes() if t == 'equal' for i in range(i1, i2)})
        both += len(ok[0] & ok[1])
    out = {
        'cells_reconciled': total_cells,
        'cells_read_identically_by_both_blind_passes': both,
        'source': 'H-1649 Images 886 (p.242), 889 (p.245), 890 (p.246), 891 (p.247) at 1600 px; crops images/h1649/p245_lines/, p246_lines/, p242_cols/, p247_cols/',
        'line_crops': len(rec),
        'pass_agreement_lines': f'{agree_lines}/{len(rec)} line crops identical in words between the two blind passes (most differences are margin notes one pass read into the line)',
        'readings': summary,
        'key_check': {
            'compared_cells': len(compared), 'per_item': {it: f'{per[it]}/{tot[it]}' for it in LETTERS},
            'page_letter_equals_decipherment_letter': match,
            'shuffled_plaintext_control': {'seeds': 1000, 'mean': round(sum(null) / len(null), 3), 'p95': null[949], 'max': null[-1]},
            'off_cells': off,
            'unequal_words_left_out': unequal,
            'cells_beyond_title_line_left_out': beyond,
            'cipher_words_without_decipherment_counterpart': extra,
            'grade_C_cells': match,
        },
        'same_key_as_2894': {'distinct_cells': len(distinct), 'also_in_key_2894': len(ov),
                             'agree': sum(1 for k in ov if k2894[k] == distinct[k])},
    }
    outputs[P('check_3050_3077.json')] = json.dumps(out, indent=1) + '\n'
    return outputs, out


def main():
    outputs, out = build()
    if '--check' in sys.argv:
        bad = [p for p, t in outputs.items() if not os.path.exists(p) or open(p, encoding='utf-8').read() != t]
        for p in bad:
            print('STALE', os.path.basename(p))
        print('check_3050_3077: ' + ('FAIL' if bad else 'OK'))
        sys.exit(1 if bad else 0)
    for p, t in outputs.items():
        open(p, 'w', encoding='utf-8').write(t)
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
