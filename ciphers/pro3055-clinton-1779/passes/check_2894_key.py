#!/usr/bin/env python3
"""Known-plaintext key check of PRO 30/55/24/76 (item 2894, Clinton to Haldimand, 6 July 1780) against its own
period decipherment (H-1649 page 186, passes/p186_reading.txt): GAPS2-pro3055-clinton-1779, 2 Oct 2026.

Inputs (all on disk, no network):
  passes/cipher_reconciled.tsv   the cipher as transcribed from H-1649 pages 184-185 (two blind passes + reconciliation);
                                 columns crop,row,first,second,clear,rule_below,conf,note; first is EMPTY where the
                                 writer omitted a repeated first figure
  passes/p186_reading.txt        the period decipherment, lines 1-20 = the body (grade H, GAPS 2 Oct 2026)
  passes/tomokiyo_key_pairs.tsv  the title-page cells S. Tomokiyo reads from OTHER letters of the same correspondence
                                 (an independent witness to the key, not derived from this letter)

Method (no cryptanalysis: every letter comes from the period decipherment):
  1. expand omitted first figures; segment the cipher into words at the rule lines and at clear-text entries;
  2. dynamic-programming word alignment of the cipher word sequence to the decipherment's word sequence
     (a pair-word costs |pairs - letters|, less a half when the plaintext word has a doubled letter that the
     key's own N.B. says to drop; a clear entry costs 0 when it equals the plaintext words it covers; a skip costs 3);
  3. letters within an aligned word map 1:1 (lengths equal), or by a doubled-letter drop, else by a sub-alignment
     whose tokens are graded M;
  4. key cells (line, position) -> letter are tallied; statistics: internal consistency (fraction of occurrences,
     over cells seen twice or more, that carry the cell's majority letter) and agreement with Tomokiyo's cells,
     exact and with the -1/-2 counting tolerance his notes describe for Clinton's letters;
  5. controls, 20 seeds each: (a) shuffled key -- Tomokiyo's letters permuted over his cells, same agreement
     statistic; (b) shuffled plaintext -- the decipherment's letters permuted within the body, same alignment
     structure, both statistics. Each control can vary on the statistic's own axis (rule 3).
Outputs: key_2894.tsv (cells), tokens_2894.tsv (every pair graded), check_2894.json (numbers); --check re-derives
and exits 1 when any committed output differs (rule 7).

Why not tools/interlinear_align.py: that tool aligns numeral groups (one letter below a code floor, chunks above) to
a printed plain line; here every group is a two-figure cell that takes exactly one letter, and the manuscript's own
rule lines give the word boundaries, so the alignment is at word level, with a trivial 1:1 inside words. A
`--pair-groups` option on the shared tool would be the right home for this if a second target needs it.
"""
import argparse, json, os, random, re, sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)

def read_tsv(path):
    rows = []
    with open(path, encoding='utf-8') as f:
        hdr = None
        for line in f:
            line = line.rstrip('\n')
            if not line or line.startswith('#'):
                continue
            parts = line.split('\t')
            if hdr is None:
                hdr = parts
                continue
            parts += [''] * (len(hdr) - len(parts))
            rows.append(dict(zip(hdr, parts)))
    return rows

def norm(w):
    return re.sub(r'[^a-z0-9&]', '', w.lower())

def load_cipher(path):
    """-> list of units: ('pairs', [(L,P,rowref), ...]) or ('clear', text, rowref)."""
    rows = read_tsv(path)
    units, cur, last_first = [], [], None
    for r in rows:
        if r.get('note', '').startswith('margin') or r.get('skip') == '1':
            continue
        clear = r.get('clear', '').strip()
        first, second = r.get('first', '').strip(), r.get('second', '').strip()
        ref = f"{r['crop']}:{r['row']}"
        if clear and not second:
            if cur:
                units.append(('pairs', cur)); cur = []
            units.append(('clear', clear, ref))
            continue
        if not second:
            continue
        if first:
            last_first = first
        L = last_first
        cur.append((L, second, ref, r.get('conf', ''), first != ''))
        if r.get('rule_below', '').strip() == '1':
            units.append(('pairs', cur)); cur = []
    if cur:
        units.append(('pairs', cur))
    return units

def load_plain(path, nlines=20):
    words = []
    with open(path, encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= nlines:
                break
            for w in line.split():
                w = w.replace('[M]', '')
                if norm(w):
                    words.append(w)
    return words

def has_double(w):
    s = norm(w)
    return any(s[i] == s[i + 1] for i in range(len(s) - 1))

PRIOR = {}   # (L,P) -> letter, majority cells seen twice or more in the previous iteration (hard-EM, see docstring)

def unit_cost(unit, pw):
    """cost of matching one cipher unit to the plaintext words pw (list)."""
    if unit[0] == 'pairs':
        if len(pw) != 1:
            return None
        n, s = len(unit[1]), norm(pw[0])
        d = abs(n - len(s))
        if d == 1 and n == len(s) - 1 and has_double(pw[0]):
            d = 0.5
        if PRIOR:
            mp, _ = sub_align(unit[1], s)
            got = {a: b for a, b in mp}
            for a, (L, Pp, *_rest) in enumerate(unit[1]):
                pl = PRIOR.get((L, Pp))
                if pl and a in got and pl != s[got[a]]:
                    d += 1.0
        return d
    text = norm(unit[1])
    target = ''.join(norm(w) for w in pw)
    if text == target:
        return 0
    # partial credit: same first letter and similar length
    return 1.5 + abs(len(text) - len(target)) * 0.5 + (0 if text[:1] == target[:1] else 1)

SKIP = 3.0

def align(units, plain):
    n, m = len(units), len(plain)
    INF = float('inf')
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if D[i][j] == INF:
                continue
            if i < n:
                c = D[i][j] + SKIP
                if c < D[i + 1][j]:
                    D[i + 1][j], B[i + 1][j] = c, (i, j, 'skip_c')
            if j < m:
                c = D[i][j] + SKIP
                if c < D[i][j + 1]:
                    D[i][j + 1], B[i][j + 1] = c, (i, j, 'skip_p')
            if i < n:
                maxk = 1 if units[i][0] == 'pairs' else 4
                for k in range(1, maxk + 1):
                    if j + k > m:
                        break
                    uc = unit_cost(units[i], plain[j:j + k])
                    if uc is None:
                        continue
                    c = D[i][j] + uc
                    if c < D[i + 1][j + k]:
                        D[i + 1][j + k], B[i + 1][j + k] = c, (i, j, f'match{k}')
    i, j, path = n, m, []
    while (i, j) != (0, 0):
        pi, pj, op = B[i][j]
        path.append((pi, pj, op, i, j))
        i, j = pi, pj
    path.reverse()
    return D[n][m], path

def sub_align(pairs, letters):
    """1:1 letters to pairs; drop one of a doubled letter if pairs == letters-1; else edit-distance alignment."""
    n, m = len(pairs), len(letters)
    if n == m:
        return list(zip(range(n), range(m))), 'exact'
    if n == m - 1:
        for i in range(m - 1):
            if letters[i] == letters[i + 1]:
                idx = list(range(i + 1)) + list(range(i + 2, m))
                return list(zip(range(n), idx)), 'double-drop'
    # generic: align by DP minimising indels, letters taken in order
    INF = float('inf')
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if D[i][j] == INF:
                continue
            if i < n and D[i][j] + 1 < D[i + 1][j]:
                D[i + 1][j], B[i + 1][j] = D[i][j] + 1, (i, j)
            if j < m and D[i][j] + 1 < D[i][j + 1]:
                D[i][j + 1], B[i][j + 1] = D[i][j] + 1, (i, j)
            if i < n and j < m and D[i][j] < D[i + 1][j + 1]:
                D[i + 1][j + 1], B[i + 1][j + 1] = D[i][j], (i, j)
    i, j, out = n, m, []
    while (i, j) != (0, 0):
        pi, pj = B[i][j]
        if pi == i - 1 and pj == j - 1:
            out.append((pi, pj))
        i, j = pi, pj
    out.reverse()
    return out, 'indel'

def shifted(tomo_map, L, Pp, k):
    return tomo_map.get((L, str(int(Pp) + k))) if str(Pp).isdigit() else None

def run(units, plain, tomo, verbose=True, iterations=3):
    global PRIOR
    PRIOR = {}
    cost, path = align(units, plain)
    for _ in range(iterations - 1):
        cells0 = defaultdict(Counter)
        for pi, pj, op, i, j in path:
            if op.startswith('match') and units[pi][0] == 'pairs':
                letters = norm(plain[pj])
                mp, how = sub_align(units[pi][1], letters)
                if how in ('exact', 'double-drop'):
                    for a, b in mp:
                        cells0[(units[pi][1][a][0], units[pi][1][a][1])][letters[b]] += 1
        PRIOR = {c: cnt.most_common(1)[0][0] for c, cnt in cells0.items() if sum(cnt.values()) >= 2}
        cost2, path2 = align(units, plain)
        if path2 == path:
            break
        cost, path = cost2, path2
    PRIOR = {}
    tokens = []       # one per cipher pair
    aligned_words = []
    for pi, pj, op, i, j in path:
        if op.startswith('match'):
            unit = units[pi]
            pw = plain[pj:j]
            if unit[0] == 'clear':
                aligned_words.append(('clear', unit[1], ' '.join(pw), unit_cost(unit, pw)))
                continue
            letters = norm(pw[0])
            pairs = unit[1]
            mp, how = sub_align(pairs, letters)
            aligned_words.append(('pairs', len(pairs), pw[0], how))
            got = {a: b for a, b in mp}
            for a, (L, Pp, ref, conf, explicit) in enumerate(pairs):
                letter = letters[got[a]] if a in got else ''
                tokens.append(dict(L=L, P=Pp, ref=ref, conf=conf, explicit=explicit, word=pw[0],
                                   letter=letter, how=how))
        elif op == 'skip_c':
            unit = units[pi]
            if unit[0] == 'pairs':
                aligned_words.append(('pairs-unmatched', len(unit[1]), '', 'skip'))
                for (L, Pp, ref, conf, explicit) in unit[1]:
                    tokens.append(dict(L=L, P=Pp, ref=ref, conf=conf, explicit=explicit, word='', letter='', how='skip'))
            else:
                aligned_words.append(('clear-unmatched', unit[1], '', 'skip'))
        else:
            aligned_words.append(('plain-unmatched', '', plain[pj], 'skip'))
    # key cells
    cells = defaultdict(Counter)
    for t in tokens:
        if t['letter'] and t['how'] in ('exact', 'double-drop'):
            cells[(t['L'], t['P'])][t['letter']] += 1
    # consistency
    occ = agree = 0
    for c, cnt in cells.items():
        tot = sum(cnt.values())
        if tot >= 2:
            occ += tot; agree += cnt.most_common(1)[0][1]
    # tomokiyo agreement (cells with a majority letter)
    maj = {c: cnt.most_common(1)[0][0] for c, cnt in cells.items()}
    def tomo_stats(tomo_map):
        ex = tol = n = 0
        for (L, Pp), letter in maj.items():
            cands = [tomo_map.get((L, Pp))]
            if cands[0] is None:
                continue
            n += 1
            if letter == cands[0]:
                ex += 1; tol += 1
            elif letter in (shifted(tomo_map, L, Pp, 1), shifted(tomo_map, L, Pp, 2)):
                tol += 1
        return n, ex, tol
    n_t, ex_t, tol_t = tomo_stats(tomo)
    # skipped groups (no counterpart in the decipherment): read with the cells fixed elsewhere, graded by cell source
    own = {c: cnt.most_common(1)[0][0] for c, cnt in cells.items()}
    skipped_words = []
    cur = []
    for t in tokens + [None]:
        if t is not None and t['how'] == 'skip':
            c = (t['L'], t['P'])
            if c in own:
                t['letter'], t['src'] = own[c], 'C'
            elif c in tomo:
                t['letter'], t['src'] = tomo[c], 'H'
            else:
                t['letter'], t['src'] = '', 'M'
            cur.append(t)
        elif cur:
            skipped_words.append((cur[0]['ref'], ''.join(x['letter'] or '.' for x in cur), ''.join(x['src'] for x in cur)))
            cur = []
    # grades
    for t in tokens:
        if t['how'] == 'skip':
            t['grade'] = t['src']
        elif not t['letter']:
            t['grade'] = 'M'
        elif t['how'] in ('exact', 'double-drop') and t['conf'] in ('H', 'M', '') and '?' not in t['P'] and '?' not in str(t['L']):
            cnt = cells[(t['L'], t['P'])]
            t['grade'] = 'H' if cnt.most_common(1)[0][0] == t['letter'] else 'M'
        else:
            t['grade'] = 'M'
        tv = tomo.get((t['L'], t['P']))
        t['tomokiyo'] = tv or ''
        t['tomo_match'] = ('exact' if tv == t['letter'] else
                           'tol' if t['letter'] and t['letter'] in (shifted(tomo, t['L'], t['P'], 1), shifted(tomo, t['L'], t['P'], 2)) else
                           'no' if tv else '')
    stats = dict(align_cost=cost, n_units=len(units), n_plain_words=len(plain), n_tokens=len(tokens),
                 n_cells=len(cells), consistency_occ=occ, consistency_agree=agree,
                 consistency=(agree / occ if occ else None),
                 tomo_cells_compared=n_t, tomo_exact=ex_t, tomo_tolerant=tol_t,
                 grades=dict(Counter(t['grade'] for t in tokens)),
                 groups_without_counterpart=skipped_words)
    return stats, tokens, cells, aligned_words, path

def shuffled_tomo(tomo, seed):
    keys = list(tomo.keys()); vals = [tomo[k] for k in keys]
    random.Random(seed).shuffle(vals)
    return dict(zip(keys, vals))

def shuffled_plain(plain, seed):
    letters = [ch for w in plain for ch in norm(w)]
    random.Random(seed).shuffle(letters)
    out, k = [], 0
    for w in plain:
        n = len(norm(w)); out.append(''.join(letters[k:k + n])); k += n
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cipher', default=P('cipher_reconciled.tsv'))
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--seeds', type=int, default=20)
    a = ap.parse_args()
    units = load_cipher(a.cipher)
    plain = load_plain(P('p186_reading.txt'))
    tomo_rows = read_tsv(P('tomokiyo_key_pairs.tsv'))
    tomo = {}
    for r in tomo_rows:
        if r['flag'] == 'counting-error':
            continue           # cells Tomokiyo marks as miscounts are not key cells
        tomo.setdefault((r['line'], r['pos']), r['letter'])
    stats, tokens, cells, words, path = run(units, plain, tomo)
    # controls
    ctl_key = [run(units, plain, shuffled_tomo(tomo, s), verbose=False)[0] for s in range(a.seeds)]
    ctl_plain = [run(units, shuffled_plain(plain, s), tomo, verbose=False)[0] for s in range(a.seeds)]
    def summ(xs, k):
        v = [x[k] for x in xs if x[k] is not None]
        return dict(mean=sum(v) / len(v), max=max(v), min=min(v)) if v else None
    out = dict(target=stats,
               control_shuffled_key=dict(seeds=a.seeds,
                                         tomo_exact=summ(ctl_key, 'tomo_exact'), tomo_tolerant=summ(ctl_key, 'tomo_tolerant'),
                                         tomo_cells_compared=summ(ctl_key, 'tomo_cells_compared')),
               control_shuffled_plain=dict(seeds=a.seeds, consistency=summ(ctl_plain, 'consistency'),
                                           tomo_exact=summ(ctl_plain, 'tomo_exact'), tomo_tolerant=summ(ctl_plain, 'tomo_tolerant'),
                                           tomo_cells_compared=summ(ctl_plain, 'tomo_cells_compared')))
    # text outputs
    key_lines = ['line\tpos\tletter\tcount\tother\ttomokiyo\tmatch']
    for (L, Pp), cnt in sorted(cells.items(), key=lambda x: (int(x[0][0]) if x[0][0].isdigit() else 99, int(x[0][1]) if x[0][1].isdigit() else 99)):
        letter, c = cnt.most_common(1)[0]
        other = ';'.join(f'{k}:{v}' for k, v in cnt.items() if k != letter)
        tv = tomo.get((L, Pp), '')
        match = '' if not tv else ('exact' if tv == letter else
                                   'tol' if letter in (shifted(tomo, L, Pp, 1), shifted(tomo, L, Pp, 2)) else 'no')
        key_lines.append(f'{L}\t{Pp}\t{letter}\t{c}\t{other}\t{tv}\t{match}')
    tok_lines = ['n\tref\tline\tpos\texplicit_first\tletter\tword\thow\tgrade\ttomokiyo\ttomo_match']
    for n, t in enumerate(tokens, 1):
        tok_lines.append(f"{n}\t{t['ref']}\t{t['L']}\t{t['P']}\t{int(t['explicit'])}\t{t['letter']}\t{t['word']}\t{t['how']}\t{t['grade']}\t{t['tomokiyo']}\t{t['tomo_match']}")
    # reconstructed title-page lines
    lines = defaultdict(dict)
    for (L, Pp), cnt in cells.items():
        if L.isdigit() and Pp.isdigit():
            lines[int(L)][int(Pp)] = cnt.most_common(1)[0][0]
    recon = []
    for L in sorted(lines):
        w = max(lines[L]); s = ''.join(lines[L].get(p, '.') for p in range(1, w + 1))
        recon.append(f'{L:>2}: {s}')
    out['title_page_lines_from_2894'] = recon
    out['aligned_words'] = [list(map(str, w)) for w in words]
    new = {'key_2894.tsv': '\n'.join(key_lines) + '\n', 'tokens_2894.tsv': '\n'.join(tok_lines) + '\n',
           'check_2894.json': json.dumps(out, indent=1) + '\n'}
    if a.check:
        bad = [k for k, v in new.items() if not os.path.exists(P(k)) or open(P(k)).read() != v]
        print('STALE: ' + ', '.join(bad) if bad else 'check ok: key_2894.tsv, tokens_2894.tsv, check_2894.json regenerate identically')
        sys.exit(1 if bad else 0)
    for k, v in new.items():
        open(P(k), 'w').write(v)
    print(json.dumps({k: v for k, v in out.items() if k not in ('aligned_words',)}, indent=1))
    print('\nalignment:')
    for w in words:
        print('  ', w)

if __name__ == '__main__':
    main()
