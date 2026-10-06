#!/usr/bin/env python3
"""Item 3868: B.147 p.382 cipher columns 3-6 (H-1649 Image 1030) checked against the period decipherment on pp.385-386,
on the 1778 Army List title-page key (R10-CLIN3868, 6 Oct 2026; pre-registered in ../PREREG_R10-CLIN3868.md).

Inputs: p382_c36_passA.tsv (one blind Sonnet pass on PIL column crops), p382_c36_reconciled.tsv (the worker's re-read of
the cells the pass misread, per-cell note), title1778_reading.txt (key page; letters and & counted, as check_3868.py),
p385_reading.txt (decipherment), key_2894.tsv (cells recovered from item 2894).

Alignment: WORDS below gives, in order, the decipherment word each group of cells spells (a group ends at a gloss or at
a rule the copyist drew; "respecting" spans three rules). The words follow "copies" in p385_reading.txt; the script
asserts they occur there in this order, except "darby" which the decipherment writes (the cipher cells spell "digby").
Groups whose cell count differs from the word's letter count (admiral 5/7, commissioner 11/12) are reported apart and
not counted in the gate. Gate (pre-registered): share >= 0.80 and count > shuffled-plaintext control max (1000 seeds,
seed 1782, decipherment body letters at the same positions). j is compared both strictly and as i (the key page's
'j' cell 22-41 is never used here; period usage writes i for j).

Outputs: check_3868_c36.json. --check re-derives it and exits 1 when the committed file differs (rule 7).
"""
import json, os, random, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)
WORDS = ['of', 'the', 'whole', 'but', None, 'be', 'sent', 'by', 'the', 'next', 'opportunity', None, 'laid', 'before',
         'admiral', 'darby', 'who', 'is', 'a', 'joint', 'commissioner', None, 'me', 'as', 'soon', 'as', 'he', 'arrives',
         'in', 'town', None, 'respecting']  # None = a gloss in the copyist's hand


def chars(s):
    return [c.lower() for c in s if c.isalpha() or c == '&']


def rows(path):
    r = [l.rstrip('\n').split('\t') for l in open(path, encoding='utf-8') if l.strip() and not l.startswith('#')]
    return [dict(zip(r[0], x + [''] * (len(r[0]) - len(x)))) for x in r[1:]]


def groups(path, title):
    gs, cur, line, cells = [], [], None, 0
    for r in rows(path):
        e = r['entry'].replace('[?]', '')
        bar = e.endswith(' |')
        e = e.replace(' |', '')
        if e.startswith('"'):
            if cur:
                gs.append(cur)
            gs.append(e)
            cur = []
            continue
        a, b = e.split('-')
        line = int(a) if a else line
        cl = chars(title[line - 1])
        p = int(b)
        cur.append((line, p, cl[p - 1] if p <= len(cl) else '?'))
        cells += 1
        if bar:
            gs.append(cur)
            cur = []
    if cur:
        gs.append(cur)
    return gs, cells


def merge(gs):
    """join cell groups so that they line up with WORDS (respecting spans three rules)"""
    out = []
    for g in gs:  # consecutive glosses ("and" / "also") are one gloss
        if isinstance(g, str) and out and isinstance(out[-1], str):
            out[-1] = out[-1] + ' ' + g
        else:
            out.append(g)
    # the last three cell groups (after the gloss) are one word
    if len(out) >= 3 and all(isinstance(x, list) for x in out[-3:]):
        out = out[:-3] + [out[-3] + out[-2] + out[-1]]
    return out


def score(path, title, body):
    gs, ncells = groups(path, title)
    gs = merge(gs)
    assert len(gs) == len(WORDS), (len(gs), len(WORDS))
    comp, apart, detail = [], [], []
    for g, w in zip(gs, WORDS):
        if w is None:
            assert isinstance(g, str), g
            detail.append({'gloss': g.replace('"', '')})
            continue
        page = ''.join(c[2] for c in g)
        d = {'word': w, 'cells': ' '.join(f'{a}-{b}' for a, b, _ in g), 'page_letters': page}
        if len(g) == len(w):
            comp += [(c, x) for c, x in zip(g, w)]
            d['match'] = sum(1 for c, x in zip(g, w) if c[2] == x)
        else:
            apart.append(d)
            d['apart'] = f'{len(g)} cells for {len(w)} letters'
        detail.append(d)
    strict = sum(1 for c, x in comp if c[2] == x)
    ij = sum(1 for c, x in comp if c[2] == x or (x == 'j' and c[2] == 'i'))
    rng = random.Random(1782)
    null = []
    for _ in range(1000):
        sh = body[:]
        rng.shuffle(sh)
        null.append(sum(1 for (c, _), y in zip(comp, sh) if c[2] == y))
    null.sort()
    return ncells, comp, strict, ij, null, detail, apart, gs


def build():
    title = [l.rstrip('\n') for l in open(P('title1778_reading.txt'), encoding='utf-8')
             if not l.startswith('#') and l.strip()]
    rd = [l for l in open(P('p385_reading.txt'), encoding='utf-8') if not l.startswith('#')]
    txt = ' '.join(rd)
    body = chars(txt.split('General Arnold')[0])
    dw = [re.sub(r'[^a-z]', '', w.lower()) for w in re.sub(r'\{[^}]*\}', ' ', txt).split()]
    dw = [w for w in dw if w]
    i = dw.index('copies') + 1
    for w in [x for x in WORDS if x]:  # order check against the decipherment
        j = dw.index(w, i)
        assert j - i < 12, (w, dw[i:i + 12])
        i = j + 1
    res = {}
    for tag, f in (('pass_A', 'p382_c36_passA.tsv'), ('reconciled', 'p382_c36_reconciled.tsv')):
        ncells, comp, strict, ij, null, detail, apart, gs = score(P(f), title, body)
        res[tag] = {'cells_read': ncells, 'compared_cells': len(comp), 'match_strict': strict, 'match_i_eq_j': ij,
                    'share_i_eq_j': round(ij / len(comp), 3),
                    'control_shuffled_plaintext': {'seeds': 1000, 'mean': round(sum(null) / 1000, 3),
                                                   'p95': null[949], 'max': null[-1]},
                    'gate_pass': ij / len(comp) >= 0.80 and ij > null[-1]}
        if tag == 'reconciled':
            res['words'] = detail
            k2894 = {(int(r['line']), int(r['pos'])): r['letter'] for r in rows(P('key_2894.tsv'))}
            distinct = {(a, b): c for g in gs if isinstance(g, list) for a, b, c in g}
            ov = {k: v for k, v in distinct.items() if k in k2894}
            res['same_key_as_2894'] = {'distinct_cells': len(distinct), 'also_in_key_2894': len(ov),
                                       'agree': sum(1 for k, v in ov.items() if k2894[k] == v)}
            res['mismatches_reconciled'] = [f"{d['word']}: {d['cells']} -> {d['page_letters']}" for d in detail
                                            if 'match' in d and d['match'] != len(d['word'])]
    res['reconciled_changes'] = [f"{r['col']}.{r['idx']} {r['entry']} ({r['note']})"
                                 for r in rows(P('p382_c36_reconciled.tsv')) if r['note']]
    return json.dumps(res, indent=1) + '\n'


def main():
    js = build()
    p = P('check_3868_c36.json')
    if '--check' in sys.argv:
        ok = os.path.exists(p) and open(p, encoding='utf-8').read() == js
        print('check_3868_c36: ' + ('OK' if ok else 'FAIL (STALE check_3868_c36.json)'))
        sys.exit(0 if ok else 1)
    open(p, 'w', encoding='utf-8').write(js)
    print(js)


if __name__ == '__main__':
    main()
