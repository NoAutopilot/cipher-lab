#!/usr/bin/env python3
"""Item 2380 (PRO 30/55/19/98; recipient copy BL Add MS 21807 = Brymner B.147): Clinton to Haldimand, New York,
22 Oct 1779. The period decipherment on B.147 pp.134-135 (H-1649 Images 772-773) read, and the first two cipher
columns of the cipher copy on p.120 (Image 758) checked against it on the 1778 Army List title-page key
(GAPS9-pro3055-clinton-1779, 2 Oct 2026).

Inputs: p134_reconciled.tsv (two blind Sonnet passes p134_passA.tsv / p134_passB.tsv over the line crops of
images/h1649/p134_lines/ and p135_lines/, reconciled by the worker on a montage of the disputed crops; row per crop:
crop, passA, passB, reconciled, note), p120_cells.tsv (cipher columns 1-2 from images/h1649/p120_cols/, both passes and
the settled entry; "|" = the cell is underlined, i.e. ends a word; "-N" repeats the previous line figure),
title1778_reading.txt (the key page), key_2894.tsv (cells recovered from item 2894, July 1780).

Grades (rule 4): a decipherment word read the same by both passes or settled at reconciliation is H (a period
decipherment in the manuscript); a word carrying [?] is M. A cipher cell whose 1778-page letter equals the letter of
the decipherment word it stands for is C.

Alignment: the cipher's underlines split the cells into words; cipher word k is set against decipherment word k
(the clear "19th July" is an anchor). A pair is compared letter by letter only when the cell count equals the length of
the decipherment word with doubled letters written once (the encipherers drop a doubled letter: "leters", "matros",
"artilery", as in 2894); a pair with any other length is listed, not compared. Cells naming a position beyond the
line's length (2-99, 6-77) are M and not compared.

Statistics, each with its control on the same axis (rule 3): exact = the page letter at the cell's position equals the
decipherment letter; near = the decipherment letter sits within +-2 positions of the cell on the same line (Tomokiyo's
extract of this letter notes -1 and -2 errors). Control: the decipherment body's letters shuffled (1000 seeds) and
compared at the same cells, same rule -- it changes exactly the plaintext side, so it can fail where the target passes.
Line-1 shift test: on line 1 every off cell is checked against the variant "BY PERMISION OF THE RIGHT HONORABLE"
(one s, no u), which is what the cells of this letter fit.

Outputs: p134_reading.txt, check_2380.json. --check re-derives both and exits 1 when a committed output differs (rule 7).
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
    return re.sub(r'[^a-z&]', '', s.lower())


def collapse(w):
    return re.sub(r'(.)\1+', r'\1', w)


BODY_CROPS = [f'p134_L{i:02d}' for i in range(1, 37)] + [f'p135_L{i:02d}' for i in range(1, 10)]
LINE1_VARIANT = chars('BY PERMISION of the RIGHT HONORABLE')


def build():
    rec = rows(P('p134_reconciled.tsv'))
    grades = {'H': 0, 'M': 0}
    body, endorse = [], []
    for r in rec:
        t = r['reconciled']
        if r['crop'] == 'p135_L09':
            body.append(t.split('||')[0].strip())
            endorse.append(' '.join(x.strip() for x in t.split('||')[1:]))
        elif r['crop'] in BODY_CROPS:
            body.append(t)
        else:
            endorse.append(t)
    for t in body:
        for w in t.split():
            if w in ('-', '/'):
                continue
            grades['M' if '[?]' in w else 'H'] += 1
    agree = sum(1 for r in rec if r['passA'] == r['passB'])
    reading = ['# B.147 pp.134-135 (H-1649 Images 772-773), BL Add MS 21807 fo.113-114v: period decipherment of Clinton to',
               '# Haldimand, New York, 22 Oct 1779 (item 2380; cipher copy on p.120 = Image 758). Two blind Sonnet passes reconciled',
               '# on the crops (passes/p134_reconciled.tsv). Spelling as written; [?] = M. Endorsement after the blank line.']
    reading += body + [''] + endorse

    dwords = [w for w in (chars(x) for x in ' '.join(body).replace('19th July', ' JULYMARK ').split()) if w]
    title = [chars(l) for l in open(P('title1778_reading.txt'), encoding='utf-8') if not l.startswith('#') and l.strip()]
    cells = rows(P('p120_cells.tsv'))
    cwords, cur, line = [], [], None
    for c in cells:
        e = c['entry'].strip()
        end = e.endswith('|')
        e = e.rstrip('|')
        if 'July' in e:
            cwords.append('JULY')
            continue
        a, b = e.split('-')
        if a:
            line = int(a)
        cur.append((line, int(b), c['col'] + ':' + c['idx']))
        if end:
            cwords.append(cur)
            cur = []
    if cur:
        cwords.append(cur)
    # align: word k <-> decipherment word k, with "19th July" (one cipher word) as anchor
    dw = [w for w in dwords]
    ji = dw.index('julymark')
    pre = cwords[:cwords.index('JULY')]
    post = cwords[cwords.index('JULY') + 1:]
    pairs = list(zip(pre, dw[:ji][-len(pre):])) + list(zip(post, dw[ji + 1:]))
    compared, unequal, excluded = [], [], []
    for cw, w in pairs:
        cw_ok = [(l, p, i) for l, p, i in cw if p <= len(title[l - 1])]
        excluded += [i for l, p, i in cw if p > len(title[l - 1])]
        if len(cw) != len(collapse(w)):
            unequal.append({'decipherment_word': w, 'cells': [f'{l}-{p}' for l, p, _ in cw],
                            'page_letters': ''.join(title[l - 1][p - 1] if p <= len(title[l - 1]) else '?' for l, p, _ in cw)})
            continue
        for (l, p, i), ch in zip(cw, collapse(w)):
            if p <= len(title[l - 1]):
                compared.append((l, p, ch, w))

    def stat(letters):
        ex = sum(1 for (l, p, _, _), ch in zip(compared, letters) if title[l - 1][p - 1] == ch)
        nr = sum(1 for (l, p, _, _), ch in zip(compared, letters) if ch in title[l - 1][max(0, p - 3):p + 2])
        return ex, nr
    ex, nr = stat([c for _, _, c, _ in compared])
    pool = list(chars(' '.join(body)))
    rng = random.Random(1779)
    nex, nnr = [], []
    for _ in range(1000):
        rng.shuffle(pool)
        a, b = stat(pool[:len(compared)])
        nex.append(a); nnr.append(b)
    nex.sort(); nnr.sort()
    offs = {}
    for l, p, ch, w in compared:
        L = title[l - 1]
        if L[p - 1] == ch:
            continue
        d = [k for k in (-2, -1, 1, 2) if 0 <= p - 1 + k < len(L) and L[p - 1 + k] == ch]
        offs.setdefault(l, []).append({'cell': f'{l}-{p}', 'want': ch, 'page': L[p - 1], 'found_at_offset': d, 'word': w})
    l1 = [(p, ch) for l, p, ch, _ in compared if l == 1]
    l1_var = sum(1 for p, ch in l1 if p <= len(LINE1_VARIANT) and LINE1_VARIANT[p - 1] == ch)
    l1_page = sum(1 for p, ch in l1 if title[0][p - 1] == ch)
    k2894 = {(int(r['line']), int(r['pos'])): r['letter'] for r in rows(P('key_2894.tsv'))}
    mine = {}
    for l, p, ch, _ in compared:
        mine.setdefault((l, p), set()).add(ch)
    ov = {k: v for k, v in mine.items() if k in k2894}
    out = {
        'source': 'H-1649 Images 772 (p.134) and 773 (p.135) full/max, crops images/h1649/p134_lines/, p135_lines/; cipher Image 758 (p.120), images/h1649/p120_cols/ (columns 1-2 of 7)',
        'p134_conflict': 'settled on the images: p.134 is the decipherment of this letter (22 Oct 1779), opening "I was honored with your Letters of the 19th July", margin "See a cypher copy transcd. on p.120 supra"; p.120 margin "See a decoded copy transcd. on p.134 infra"; endorsement p.135 "Lettre en Chiffre 1779 du Genl Clinton recue a Quebec par Halifax le 18. Jan[?] 1780". Tomokiyo\'s placement holds; Brymner\'s reading of p.134 as an abstract of the 9 Sept 1779 letter does not fit the page.',
        'lines': len(rec),
        'pass_agreement_lines': f'{agree}/{len(rec)} crops identical between the two blind passes; the rest differ by margin fragments the crops caught, a superscript, Chesipeak/Chesapeak and recue/reçue',
        'grades_words_body': grades,
        'key_check': {
            'cells_read': sum(len(c) for c in cwords if c != 'JULY'),
            'cell_pass_agreement': '95 of 97 entries identical in value (c1 row 1 cut by the crop edge in A, c2 row 5 6-77 with ? in B); 1 underline differs (c2 2-4, kept B on the column preview)',
            'cipher_words': len(cwords), 'word_pairs': len(pairs),
            'pairs_not_compared_length_differs': unequal,
            'cells_out_of_range_M': excluded,
            'compared_cells': len(compared),
            'exact': ex, 'exact_control': {'seeds': 1000, 'mean': round(sum(nex) / 1000, 3), 'p95': nex[949], 'max': nex[-1]},
            'within_2': nr, 'within_2_control': {'seeds': 1000, 'mean': round(sum(nnr) / 1000, 3), 'p95': nnr[949], 'max': nnr[-1]},
            'off_cells_by_line': {str(k): v for k, v in sorted(offs.items())},
            'line1_cells': len(l1), 'line1_match_1778_page': l1_page, 'line1_match_variant_PERMISION_HONORABLE': l1_var,
            'grade_C_cells': ex,
        },
        'vs_key_2894': {'distinct_cells': len(mine), 'also_in_key_2894': len(ov),
                        'agree': sum(1 for k, v in ov.items() if k2894[k] in v),
                        'disagree': {f'{k[0]}-{k[1]}': [k2894[k], sorted(v)] for k, v in ov.items() if k2894[k] not in v}},
    }
    return '\n'.join(reading) + '\n', json.dumps(out, indent=1) + '\n'


def main():
    reading, js = build()
    targets = [(P('p134_reading.txt'), reading), (P('check_2380.json'), js)]
    if '--check' in sys.argv:
        bad = [p for p, t in targets if not os.path.exists(p) or open(p, encoding='utf-8').read() != t]
        for p in bad:
            print('STALE', os.path.basename(p))
        print('check_2380: ' + ('FAIL' if bad else 'OK'))
        sys.exit(1 if bad else 0)
    for p, t in targets:
        open(p, 'w', encoding='utf-8').write(t)
    print(js)


if __name__ == '__main__':
    main()
