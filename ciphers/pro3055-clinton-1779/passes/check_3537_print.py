#!/usr/bin/env python3
"""Item 3537 (PRO 30/55/30/26, Clinton to Haldimand, New York, 31 May 1781): the cipher specimen VHS Collections II (1871) prints
on pp.339-341 decoded on the 1778 Army List title-page key and compared with the volume's own printed translation (pp.341-342).
R15-CLIN3537, 6 Oct 2026; rules fixed in ../PREREG_R15-CLIN3537.md before scoring.

Input: vhs2_3537_print.txt (the djvu OCR lines as served, unrepaired), title1778_reading.txt (key page), key_2894.tsv (cells
seen in 2894). Output: check_3537_print.json. --check re-derives and exits 1 when stale (rule 7).
"""
import json, os, random, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)
DASH = '[—–~\\-]+'
FULL = re.compile(r'^\D{0,2}(\d{1,2})\s*' + DASH + r'\s*(\d{1,2})\D{0,2}$')
CONT = re.compile(r'^\s*' + DASH + r'\s*(\d{1,2})\s*$')
FURN = re.compile(r'^(The\s+Haldimand\s+Papers\.?|34[012])$')

def chars(s):
    return re.sub(r'[^a-z&]', '', s.lower())

def lcs(a, b):
    prev = [0] * (len(b) + 1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b):
            cur.append(prev[j] + 1 if x == y else max(prev[j + 1], cur[j]))
        prev = cur
    return prev[-1]

def lcs_unmatched(a, b):
    n, k = len(a), len(b)
    T = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(k - 1, -1, -1):
            T[i][j] = T[i+1][j+1] + 1 if a[i] == b[j] else max(T[i+1][j], T[i][j+1])
    i = j = 0; un = []
    while i < n and j < k:
        if a[i] == b[j]: i += 1; j += 1
        elif T[i+1][j] >= T[i][j+1]: un.append(i); i += 1
        else: j += 1
    return un + list(range(i, n))

def nw(a, b, m=2, x=-1, g=-1):
    n, k = len(a), len(b)
    S = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): S[i][0] = i * g
    for j in range(1, k + 1): S[0][j] = 0          # free leading gaps in the translation (clear words)
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            S[i][j] = max(S[i-1][j-1] + (m if a[i-1] == b[j-1] else x), S[i-1][j] + g, S[i][j-1] + g)
    j = max(range(k + 1), key=lambda jj: S[n][jj]); i = n; pairs = []
    while i > 0 and j > 0:
        if S[i][j] == S[i-1][j-1] + (m if a[i-1] == b[j-1] else x):
            pairs.append((i-1, j-1)); i -= 1; j -= 1
        elif S[i][j] == S[i-1][j] + g:
            pairs.append((i-1, None)); i -= 1
        else:
            j -= 1
    while i > 0:
        pairs.append((i-1, None)); i -= 1
    return pairs[::-1]

def runs(dec, tr, n=5):
    c, i = 0, 0
    while i + n <= len(dec):
        if '?' not in dec[i:i+n] and dec[i:i+n] in tr:
            j = i + n
            while j < len(dec) and dec[i:j+1] in tr: j += 1
            c += 1; i = j
        else:
            i += 1
    return c

def main():
    check = '--check' in sys.argv
    lines = [l.rstrip('\n') for l in open(P('vhs2_3537_print.txt'), encoding='utf-8') if not l.startswith('#')]
    s = next(i for i, l in enumerate(lines) if re.search(r'May\s+31,\s*1781', l)) + 1
    e = next(i for i, l in enumerate(lines) if 'FOREGOING' in l.upper() or 'FOKEGOING' in l.upper()) - 1
    t0 = next(i for i, l in enumerate(lines) if l.strip().startswith('Sir') and 'Your' in l)
    title = [chars(l) for l in open(P('title1778_reading.txt'), encoding='utf-8') if not l.startswith('#') and l.strip()]
    cells, unparsed, clear, last = [], [], 0, None
    for l in lines[s:e]:
        t = l.strip()
        if not t or FURN.match(t):
            continue
        m, c = FULL.match(t), CONT.match(t)
        if m:
            last = int(m.group(1)); cells.append((last, int(m.group(2))))
        elif c and last is not None:
            cells.append((last, int(c.group(1))))
        elif re.search(r'\d', t):
            unparsed.append(t)
        else:
            clear += 1
    def letter(L, Q):
        return title[L-1][Q-1] if 1 <= L <= len(title) and 1 <= Q <= len(title[L-1]) else '?'
    dec = ''.join(letter(L, Q) for L, Q in cells)
    tr_text = ' '.join(lines[t0:])
    tr_text = tr_text[tr_text.index('Your'):re.search(r'H\.\s+C\.', tr_text).start()]
    tr_text = re.sub(r'\d{3}\s+The\s+Haldimand\s+Papers\.', ' ', tr_text)
    tr = chars(tr_text)
    S_t = lcs(dec, tr) / len(dec)
    rng = random.Random(3537); ctl, ctl_runs = [], []
    for _ in range(1000):
        sh = list(tr); rng.shuffle(sh); sh = ''.join(sh)
        ctl.append(lcs(dec, sh) / len(dec)); ctl_runs.append(runs(dec, sh))
    ctl_sorted = sorted(ctl)
    key = {}
    for line in open(P('key_2894.tsv'), encoding='utf-8'):
        p = line.rstrip('\n').split('\t')
        if p[0].isdigit(): key[(int(p[0]), int(p[1]))] = p[2]
    distinct = sorted(set(cells)); in2894 = [c for c in distinct if c in key]
    agree2894 = sum(1 for c in in2894 if key[c] == letter(*c))
    diffs = []
    for i, j in nw(dec, tr):
        if j is not None and dec[i] != tr[j]:
            L, Q = cells[i]
            diffs.append({'idx': i, 'cell': f'{L}-{Q}', 'key1778': dec[i], 'print': tr[j], 'key_2894': key.get((L, Q), '')})
    out = {'parsed_cells': len(cells), 'unparsed_digit_lines': len(unparsed), 'clear_lines': clear,
           'cells_off_title': dec.count('?'), 'translation_letters': len(tr), 'decoded': dec,
           'S_target': round(S_t, 4), 'control_mean': round(sum(ctl) / len(ctl), 4),
           'control_p95': round(ctl_sorted[949], 4), 'control_max': round(ctl_sorted[-1], 4),
           'runs5_target': runs(dec, tr), 'runs5_control_mean': round(sum(ctl_runs) / len(ctl_runs), 2),
           'gate': 'PASS' if S_t >= 0.80 and S_t > ctl_sorted[-1] else 'FAIL',
           'lcs_unmatched': [{'idx': i, 'cell': f'{cells[i][0]}-{cells[i][1]}', 'key1778': dec[i], 'context': dec[max(0,i-8):i+9]} for i in lcs_unmatched(dec, tr)],
           'distinct_cells': len(distinct), 'distinct_cells_in_key_2894': len(in2894), 'agree_key_2894': agree2894,
           'cells_not_in_key_2894': [f'{L}-{Q}={letter(L, Q)}' for L, Q in distinct if (L, Q) not in key],
           'nw_mismatches': len(diffs), 'mismatches': diffs, 'unparsed': unparsed}
    js = json.dumps(out, indent=1, ensure_ascii=False) + '\n'
    path = P('check_3537_print.json')
    if check:
        ok = os.path.exists(path) and open(path, encoding='utf-8').read() == js
        print('check_3537_print: OK' if ok else 'check_3537_print: STALE'); sys.exit(0 if ok else 1)
    open(path, 'w', encoding='utf-8').write(js)
    print({k: v for k, v in out.items() if k not in ('mismatches', 'unparsed', 'decoded')})

if __name__ == '__main__':
    main()
