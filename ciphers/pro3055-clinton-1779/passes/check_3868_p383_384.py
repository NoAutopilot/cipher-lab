#!/usr/bin/env python3
"""Item 3868: B.147 pp.383-384 cipher cells (H-1649 Images 1031-1032) checked against the period decipherment on
pp.385-386, on the 1778 Army List title-page key (R10-CLIN3868B, 6 Oct 2026; pre-registered in
../PREREG_R10-CLIN3868B.md, continuing check_3868_c36.py for p.382).

Inputs: p383_passA.tsv / p384_passA.tsv (one blind Sonnet pass per page on PIL column crops), p383_reconciled.tsv /
p384_reconciled.tsv (the worker's re-read of cells the pass misread, per-cell note), title1778_reading.txt (key page),
p385_reading.txt (decipherment).

Alignment (pre-registered): SEGMENTS lists, per page and in order, the decipherment text each run of cells between two
of the copyist's glosses spells (a gloss is None in the list; its wording is checked against the pass). A run whose cell
count equals its letter count is compared cell by cell; otherwise it is split at the copyist's rules into words and
matched word by word, words of equal count compared, the rest reported apart. Gate per page and pooled: share >= 0.80 and
count > shuffled-plaintext control max (1000 seeds, seed 1782, decipherment body letters at the same positions).

Outputs: check_3868_p383_384.json. --check re-derives it and exits 1 when the committed file differs (rule 7).
"""
import json, os, random, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)

# per page, in order: the decipherment words each run of cells between two glosses spells ('' = no cells between two
# glosses). Gloss positions were located from the gloss wording only ("General", "Confidence", "and I hope ...").
SEGMENTS = {
    'p383': ['your measures with the leaders of vermont than a', 'declaration of my', 'in your endeavours to separate',
             'district from', 'revolt and my wish for its success the extent', 'expectations', 'people',
             'your promise to meet them will', '', '', 'it necessary for the crown',
             'resort to parliament for the truth is that the powers',
             'present commissioners extend only to granting pardons', 'restoring provinces', 'districts', 'kings peace',
             ''],
    'p384': ['alone is the reason of my sending', 'secretary of state these transactions', '', '', '', '', '', '',
             'in preventing our enemies', 'practising upon the jealousies of the inhabitants of vermont before the result',
             'public deliberations can be transmitted', '', 'general arnold', '', '', 'calvert pere flo', 'uet',
             'hay cord freeman', 'watts', 'friends', 'rebels'],
}
GLOSSES = {'p383': ['General', 'Confidence', 'that', 'the', 'of the', 'of the', 'and of', 'I', 'apprehend', 'make', 'to',
                    'of the', 'and', 'of', 'to the', 'and this'],
           'p384': ['to the', 'and I', 'hope', 'you', 'will', 'find', 'no', 'difficulty', 'from', 'of the', 'H.C.',
                    'P.S.', 'says', 'Monst-', 'du', 'q', 'Mess', 'and', 'were', 'to the']}
# the blind pass as delivered: on p.383 it read the gloss "I" as a cell (-3) and took the next column's "and" into
# column 6; on p.384 it read the in-clear q as "a" and "Mess" as "Next" (glosses unquoted, recognised as non-figures)
PASS_A = {'p383': (['General', 'Confidence', 'that', 'the', 'of the', 'of the', 'and of', 'apprehend', 'make', 'to',
                    'of the', 'and', 'and', 'of', 'to the', 'and this'],
                   SEGMENTS['p383'][:7] + ['your promise to meet them will i', ''] + SEGMENTS['p383'][10:12] +
                   ['present commissioners extend only to granting', 'pardons'] + SEGMENTS['p383'][13:]),
          'p384': (GLOSSES['p384'][:15] + ['a', 'Next'] + GLOSSES['p384'][17:], SEGMENTS['p384'])}


def chars(s):
    return [c.lower() for c in s if c.isalpha() or c == '&']


def rows(path):
    r = [l.rstrip('\n').split('\t') for l in open(path, encoding='utf-8') if l.strip() and not l.startswith('#')]
    return [dict(zip(r[0], x + [''] * (len(r[0]) - len(x)))) for x in r[1:]]


def runs(path, title):
    out, cur, glosses, line, ncells = [], [], [], None, 0
    for r in rows(path):
        e = r['entry'].replace('[?]', '')
        bar = e.endswith(' |')
        e = e.replace(' |', '')
        if not re.fullmatch(r'\d*-\d+', e):
            out.append(cur)
            glosses.append(e.strip('"'))
            cur = []
            continue
        a, b = e.split('-')
        line = int(a) if a else line
        cl = chars(title[line - 1])
        p = int(b)
        cur.append((line, p, cl[p - 1] if p <= len(cl) else '?', bar, r['col'] + '.' + r['idx']))
        ncells += 1
    out.append(cur)
    return out, glosses, ncells


def align(run, text):
    """whole run when the counts agree; else split at the copyist's rules and match words in order (a stray rule
    inside a word is merged when the merged count equals the word); unequal words are reported apart"""
    letters = [c for c in text if c.isalpha()]
    if len(run) == len(letters):
        return list(zip(run, letters)), []
    groups, g = [], []
    for c in run:
        g.append(c)
        if c[3]:
            groups.append(g)
            g = []
    if g:
        groups.append(g)
    comp, apart, words, i = [], [], text.split(), 0
    for w in words:
        if i >= len(groups):
            apart.append({'word': w, 'cells': '', 'apart': 'no cells left'})
            continue
        g = groups[i]
        if len(g) < len(w) and i + 1 < len(groups) and len(g) + len(groups[i + 1]) == len(w):
            g = g + groups[i + 1]
            i += 1
        i += 1
        if len(g) == len(w):
            comp += list(zip(g, w))
        else:
            apart.append({'word': w, 'cells': ' '.join(f'{a}-{b}' for a, b, *_ in g),
                          'page_letters': ''.join(c[2] for c in g), 'apart': f'{len(g)} cells for {len(w)} letters'})
    return comp, apart


def score_page(page, path, title, body, glosses, segments):
    rs, gl, ncells = runs(path, title)
    assert gl == glosses, (page, gl)
    assert len(rs) == len(segments), (page, len(rs))
    comp, apart = [], []
    for run, text in zip(rs, segments):
        c, a = align(run, text)
        comp += c
        apart += a
    return ncells, comp, apart


def stats(comp, body):
    strict = sum(1 for c, x in comp if c[2] == x)
    ij = sum(1 for c, x in comp if c[2] == x or (x == 'j' and c[2] == 'i'))
    rng = random.Random(1782)
    null = []
    for _ in range(1000):
        sh = body[:]
        rng.shuffle(sh)
        null.append(sum(1 for (c, _), y in zip(comp, sh) if c[2] == y))
    null.sort()
    return {'compared_cells': len(comp), 'match_strict': strict, 'match_i_eq_j': ij,
            'share_i_eq_j': round(ij / len(comp), 3),
            'control_shuffled_plaintext': {'seeds': 1000, 'mean': round(sum(null) / 1000, 3), 'p95': null[949],
                                           'max': null[-1]},
            'gate_pass': ij / len(comp) >= 0.80 and ij > null[-1]}


def build():
    title = [l.rstrip('\n') for l in open(P('title1778_reading.txt'), encoding='utf-8')
             if not l.startswith('#') and l.strip()]
    txt = ' '.join(l for l in open(P('p385_reading.txt'), encoding='utf-8') if not l.startswith('#'))
    body = chars(txt.split('General Arnold')[0])
    flat = re.sub(r'[^a-z ]', '', re.sub(r'\{[^}]*\}', ' ', txt).lower())
    for page in SEGMENTS:  # every run's words occur in the decipherment (Darby/Digby aside, none here)
        for seg in SEGMENTS[page]:
            for w in seg.split():
                assert w in flat or w in ('flo', 'uet', 'kings', 'jealousies', 'i'), w
    res = {}
    for tag, suf in (('pass_A', 'passA'), ('reconciled', 'reconciled')):
        allc = []
        res[tag] = {}
        for page in ('p383', 'p384'):
            gs = PASS_A[page] if tag == 'pass_A' else (GLOSSES[page], SEGMENTS[page])
            ncells, comp, apart = score_page(page, P(f'{page}_{suf}.tsv'), title, body, *gs)
            allc += comp
            d = {'cells_read': ncells, **stats(comp, body)}
            if tag == 'reconciled':
                d['apart'] = apart
                d['mismatches'] = [f"{c[4]} {c[0]}-{c[1]} page {c[2]} / decipherment {x}" for c, x in comp
                                   if not (c[2] == x or (x == 'j' and c[2] == 'i'))]
            res[tag][page] = d
        res[tag]['pooled'] = stats(allc, body)
        if tag == 'reconciled':
            k2894 = {(int(r['line']), int(r['pos'])): r['letter'] for r in rows(P('key_2894.tsv'))}
            distinct = {(c[0], c[1]): c[2] for c, _ in allc}
            ov = {k: v for k, v in distinct.items() if k in k2894}
            res['same_key_as_2894'] = {'distinct_cells': len(distinct), 'also_in_key_2894': len(ov),
                                       'agree': sum(1 for k, v in ov.items() if k2894[k] == v)}
    res['reconciled_changes'] = [f"{p} {r['col']}.{r['idx']} {r['entry']} ({r['note']})" for p in ('p383', 'p384')
                                 for r in rows(P(f'{p}_reconciled.tsv')) if r['note']]
    return json.dumps(res, indent=1) + '\n'


def main():
    js = build()
    p = P('check_3868_p383_384.json')
    if '--check' in sys.argv:
        ok = os.path.exists(p) and open(p, encoding='utf-8').read() == js
        print('check_3868_p383_384: ' + ('OK' if ok else 'FAIL (STALE check_3868_p383_384.json)'))
        sys.exit(0 if ok else 1)
    open(p, 'w', encoding='utf-8').write(js)
    print(js)


if __name__ == '__main__':
    main()
