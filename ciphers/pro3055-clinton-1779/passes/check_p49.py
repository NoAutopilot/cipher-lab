#!/usr/bin/env python3
"""B.148 f.49 (H-1649 Image 1125), Carleton to Haldimand, 22 July 1782, a cipher page with no period decipherment recorded here:
CLIN-SIB's statistic B2 (check_p49.py copied; names and input changed) on the 1778 title-page key as printed (variant a, GATED;
variant b reported) against the page-permuted-key control (CLIN-F49, 16 Oct 2026; pre-registered in ../PREREG-CLIN-F49.md, pushed
before the image was fetched). NO known answer: the hit test is the era lexicon (a decoded run is a word occurring >= 3 times in
tools/data/en18, or exactly two such words of >= 3 letters each). Also reported, NOT gated: rule R1 runs (added after the PREREG) and
agreement with Tomokiyo's printed extract (sources/cryptiana/web/haldimand.htm). Input p49_reconciled.tsv; output check_p49.json;
--precheck prints the PREREG prechecks; --check exits 1 when stale (rule 7)."""
import gzip, glob
import json, os, random, re, sys

SOURCE = 'H-1649 Image 1125 (B.148 f.49) at full/max 4744x4056, columns cut by tools/iiif_lines.py (images/h1649/p49_cols)'

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


def split_of(s, L):
    if s in L:
        return s
    for i in range(3, len(s) - 2):
        if s[:i] in L and s[i:] in L:
            return s[:i] + ' ' + s[i:]
    return None


is_words = lambda s, L: split_of(s, L) is not None


def lexicon():
    from collections import Counter
    c = Counter()
    for f in sorted(glob.glob(os.path.join(ROOT, '..', '..', '..', 'tools', 'data', 'en18', '*.txt.gz'))):
        c.update(re.findall(r'[a-z]+', gzip.open(f, 'rt', encoding='utf-8', errors='replace').read().lower()))
    return {w for w, n in c.items() if n >= 3}


def score(runs, title_b, letters, seed=123, seeds=1000):
    dec = lambda T, r: ''.join(page_letter(T, l, p) for l, p, *_ in r)
    hit = lambda s: '?' not in s and is_words(s, letters)
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
                              'split': split_of(s, letters) if hit(s) else None} for r, s in zip(runs, real)]}


def build():
    letters = lexicon()
    title = [chars(l) for l in open(P('title1778_reading.txt'), encoding='utf-8') if not l.startswith('#') and l.strip()]
    vb = list(title); vb[0] = chars('BY PERMISION of the RIGHT HONORABLE')
    cells = rows(P('p49_reconciled.tsv'))
    grades = {}
    for c in cells:
        if c['kind'] in ('letter', 'word'):
            grades[c['grade']] = grades.get(c['grade'], 0) + 1
    r0 = score(runs_of(cells, 'R0'), title, letters)
    r1 = score(runs_of(cells, 'R0'), vb, letters)
    rr1 = score(runs_of(cells, 'R1'), title, letters)
    codes = [{'at': f"{c['col']}:{c['idx']}", 'code': c['entry'], 'gloss': c['gloss'], 'grade': c['grade']}
             for c in cells if c['kind'] == 'word']
    out = {'source': SOURCE,
           'key': 'title1778_reading.txt as printed (variant a) GATED; variant (b) reported', 'cells_letter_and_word': sum(grades.values()), 'cell_grades': grades,
           'B2_variant_a_GATED': r0, 'B2_variant_b_reported_not_gated': {k: r1[k] for k in r1 if k != 'decoded_runs'},
           'B2_rule_R1_reported_not_gated_post_prereg': rr1, 'tomokiyo_agreement': tomokiyo(cells, title),
           'word_codes': codes, 'clear_words': [c['entry'] for c in cells if c['kind'] == 'clear'], 'lexicon_words': len(letters)}
    return json.dumps(out, indent=1) + '\n'


def tomokiyo(cells, T):
    """Tomokiyo's printed extract: each 'xL-P c' / '-P c' letter group with his letter; compare with our decode of the same cell."""
    import html
    t = open(os.path.join(ROOT, '..', '..', '..', 'sources', 'cryptiana', 'web', 'haldimand.htm'), encoding='utf-8', errors='replace').read()
    t = html.unescape(re.sub(r'<[^>]+>', ' ', t))
    seg = t[t.index('f.49 (Image 1125)'):t.index('f.65A (Image 1142)')]
    seg = seg[seg.index('extract'):]
    groups = re.findall(r'(x?\d*-\d+)\s+(\S+)', seg)
    ours, L, col = [], None, None
    for c in cells:  # write each dash-only cell with the line it inherits in its column, as Tomokiyo prints it
        if c['col'] != col:
            col, L = c['col'], None
        a, b = c['entry'].lstrip('x+').split('-')
        L = a or L
        ours.append((f'{L}-{b}', c['kind']))
    n = agree = 0; line = None; diffs = []; j = 0; used = set(); missing = []
    for e, g in groups:
        k = next((i for i in list(range(j, len(ours))) + list(range(0, j)) if i not in used and ours[i][0].lstrip('x+') == e.lstrip('x')), None)
        if k is None:  # Tomokiyo's group not on our page (a transcription difference on one side)
            missing.append(e); continue
        used.add(k); j = k + 1
        if e.startswith('x') or (len(g) == 1 and not e.split('-')[0]):
            a, b = e.lstrip('x').split('-'); line = int(a) if a else line
            mine = page_letter(T, line, int(b)); n += 1
            if mine == g.strip('[]').lower():
                agree += 1
            else:
                diffs.append(f'{e}: T {g} / ours {mine}')
    return {'tomokiyo_groups': len(groups), 'not_found_on_our_page': missing, 'tomokiyo_letter_groups_matched': n, 'same_letter': agree, 'diffs': diffs}


def main():
    js = build(); path = P('check_p49.json')
    if '--precheck' in sys.argv:  # PREREG pre-scoring checks only, printed before the hits are looked at
        d = json.loads(js)
        for k in ('B2_variant_a_GATED', 'B2_variant_b_reported_not_gated'):
            print(k, 'runs_ge3', d[k]['runs_ge3'], 'can_differ', d[k]['can_differ'])
        return
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path, encoding='utf-8').read() == js
        print('check_p49: ' + ('OK' if ok else 'FAIL (STALE check_p49.json)')); sys.exit(0 if ok else 1)
    if '--dry' not in sys.argv:
        open(path, 'w', encoding='utf-8').write(js)
    d = json.loads(js); B = d['B2_variant_a_GATED']
    print({k: d[k] for k in ('cells_letter_and_word', 'cell_grades')})
    print('R0', {k: B[k] for k in B if k != 'decoded_runs'})
    print('variant b', d['B2_variant_b_reported_not_gated'])
    R = d['B2_rule_R1_reported_not_gated_post_prereg']; print('rule R1 (not gated)', {k: R[k] for k in R if k != 'decoded_runs'})
    print('tomokiyo', d['tomokiyo_agreement'])
    for r in B['decoded_runs']:
        print(r['start'], r['cells'], r['decoded'], r['hit'], r['split'])


if __name__ == '__main__':
    main()
