#!/usr/bin/env python3
"""B.148 p.124 (H-1649 Image 1206), the continuation of the p.123 cipher copy of Carleton to Haldimand, New York, 25 Sept 1782:
statistic B2 (D4-CLIN Addendum B, unchanged) on the 1778 title-page key against a page-permuted-key control (UNA-CLIN, 9 Oct 2026;
pre-registered in ../PREREG-UNA-CLIN.md, pushed 03444f53 before any p.124 read or score). No alignment (retired, CLIN-RG).

Input: p124_reconciled.tsv (col, idx, kind, entry, underline, gloss, grade, passA, passB, note), two blind Sonnet passes on the column
crops of cut_2380_p121_122.py (Image 1206), reconciled by the worker on the crops. kind from the page only: letter (x/+ L-P or -P),
word (a full pair without x/+, rule R0: always a word code, even inside an un-underlined letter run), clear (a plain word: ends a run).
B2: decode the letter cells on variant (b) of the key; runs split at underlines, word codes and clear words; runs of >= 3 cells all H;
hit = decoded string is a substring of the p.102 decipherment letters ('?' never matches). Control: title-page characters permuted
across the page (line lengths kept), 1000 seeds, seed 123. Prechecks: can-differ >= 0.99 and runs >= 10, else NON-TEST.
Gate: share >= 0.60 AND hits > control max. Reported, not gated: rule R1 (a full pair without x between two letter cells, no
underline before it = a letter cell on a new line), hit positions in p.102, word codes and glosses.
Output check_p124.json; --check exits 1 when stale (rule 7).
"""
import json, os, random, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)
chars = lambda s: re.sub(r'[^a-z&0-9]', '', s.lower())


def rows(path):
    out, hdr = [], None
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line or line.startswith('#'):
            continue
        parts = line.split('\t')
        if hdr is None:
            hdr = parts; continue
        out.append(dict(zip(hdr, parts + [''] * (len(hdr) - len(parts)))))
    return out


def page_letter(T, l, p):
    if l is None or l < 1 or l > len(T) or p < 1 or p > len(T[l - 1]):
        return '?'
    return T[l - 1][p - 1]


def runs_of(cells, rule):
    """Runs of letter cells (line, pos, grade, ref) per the class rule R0 or R1; a run never crosses a column."""
    runs = []
    for col in sorted({c['col'] for c in cells}, key=lambda s: int(re.sub(r'\D', '', s) or 0)):
        cc = [c for c in cells if c['col'] == col]
        kinds = [c['kind'] for c in cc]
        if rule == 'R1':
            for i, c in enumerate(cc):
                if (c['kind'] == 'word' and 0 < i < len(cc) - 1 and kinds[i - 1] == 'letter' and kinds[i + 1] == 'letter'
                        and cc[i - 1]['underline'] != 'y'):
                    kinds[i] = 'letter'
        cur, line = [], None
        for c, k in zip(cc, kinds):
            if k != 'letter':
                if cur: runs.append(cur); cur = []
                continue
            a, b = c['entry'].lstrip('x+').split('-')
            if a:
                line = int(a)
            cur.append((line, int(b), c['grade'], f"{c['col']}:{c['idx']}"))
            if c['underline'] == 'y':
                runs.append(cur); cur = []
        if cur:
            runs.append(cur)
    return [r for r in runs if len(r) >= 3 and all(g == 'H' for _, _, g, _ in r)]


def score(runs, title_b, letters, seed=123, seeds=1000):
    dec = lambda T, r: ''.join(page_letter(T, l, p) for l, p, *_ in r)
    hit = lambda s: '?' not in s and s in letters
    real = [dec(title_b, r) for r in runs]
    h = sum(hit(s) for s in real)
    lens = [len(t) for t in title_b]; flat = list(''.join(title_b)); rng = random.Random(seed); ctl, differ = [], 0
    for _ in range(seeds):
        rng.shuffle(flat); T, o = [], 0
        for n in lens:
            T.append(''.join(flat[o:o + n])); o += n
        ds = [dec(T, r) for r in runs]
        differ += any(a != b for a, b in zip(ds, real))
        ctl.append(sum(hit(s) for s in ds))
    ctl.sort()
    can_differ = differ / seeds
    if can_differ < 0.99 or len(runs) < 10:
        gate = 'NON-TEST'
    else:
        gate = 'PASS' if h / len(runs) >= 0.60 and h > ctl[-1] else 'FAIL'
    return {'runs_ge3': len(runs), 'hits': h, 'share': round(h / len(runs), 3) if runs else 0, 'can_differ': can_differ,
            'control_page_permuted': {'seeds': seeds, 'seed': seed, 'mean': round(sum(ctl) / seeds, 2),
                                      'p95': ctl[int(seeds * .95) - 1], 'max': ctl[-1]},
            'gate': gate,
            'decoded_runs': [{'start': r[0][3], 'cells': ' '.join(f'{l}-{p}' for l, p, *_ in r), 'decoded': s, 'hit': hit(s),
                              'at_letter': letters.find(s) if hit(s) else None} for r, s in zip(runs, real)]}


def build():
    body = [l.rstrip('\n') for l in open(P('p102_reading.txt'), encoding='utf-8') if not l.startswith('#')]
    text = ' '.join(body).replace('con. tributed', 'contributed').replace('Ver. plank', 'Verplank').replace('^', '')
    text = text.replace('(Signed)', '')
    letters = ''.join(c for c in chars(text) if c.isalpha() or c == '&')
    title = [chars(l) for l in open(P('title1778_reading.txt'), encoding='utf-8') if not l.startswith('#') and l.strip()]
    vb = list(title); vb[0] = chars('BY PERMISION of the RIGHT HONORABLE')
    cells = rows(P('p124_reconciled.tsv'))
    grades = {}
    for c in cells:
        if c['kind'] in ('letter', 'word'):
            grades[c['grade']] = grades.get(c['grade'], 0) + 1
    r0 = score(runs_of(cells, 'R0'), vb, letters)
    r1 = score(runs_of(cells, 'R1'), vb, letters)
    codes = [{'at': f"{c['col']}:{c['idx']}", 'code': c['entry'], 'gloss': c['gloss'], 'grade': c['grade']}
             for c in cells if c['kind'] == 'word']
    out = {'source': 'H-1649 Image 1206 (B.148 p.124) full/max, columns cut by cut_2380_p121_122.py (box 1206)',
           'key': 'title1778_reading.txt variant (b)', 'cells_letter_and_word': sum(grades.values()), 'cell_grades': grades,
           'B2_R0_GATED': r0, 'B2_R1_reported_not_gated': {k: r1[k] for k in r1 if k != 'decoded_runs'},
           'word_codes': codes, 'p102_letters': len(letters)}
    return json.dumps(out, indent=1) + '\n'


def main():
    js = build(); path = P('check_p124.json')
    if '--precheck' in sys.argv:  # PREREG pre-scoring checks only, printed before the hits are looked at
        d = json.loads(js)
        for k in ('B2_R0_GATED', 'B2_R1_reported_not_gated'):
            print(k, 'runs_ge3', d[k]['runs_ge3'], 'can_differ', d[k]['can_differ'])
        return
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path, encoding='utf-8').read() == js
        print('check_p124: ' + ('OK' if ok else 'FAIL (STALE check_p124.json)')); sys.exit(0 if ok else 1)
    if '--dry' not in sys.argv:
        open(path, 'w', encoding='utf-8').write(js)
    d = json.loads(js); B = d['B2_R0_GATED']
    print({k: d[k] for k in ('cells_letter_and_word', 'cell_grades')})
    print('R0', {k: B[k] for k in B if k != 'decoded_runs'})
    print('R1', d['B2_R1_reported_not_gated'])
    for r in B['decoded_runs']:
        print(r['start'], r['cells'], r['decoded'], r['hit'], r['at_letter'])


if __name__ == '__main__':
    main()
