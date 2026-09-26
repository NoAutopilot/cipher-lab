#!/usr/bin/env python3
"""AX-COMP (26 Sept 2026): cut a Nassau cipher letter and its separate period decipherment into
(plain span, cipher run) pairs for tools/interlinear_align.py.

The cipher letter mixes clear French words with numeral groups; the decipherment is a continuous
clear text. Runs of clear words in the cipher of >= MINANCHOR letters are located in the
decipherment (semi-global edit distance, inside a window sized from the numerals since the last
anchor) and used as cut points; between two anchors the numerals (and any short clear words) form
one pair with the decipherment text between them. No key is used: the cuts come from clear words
only, so every meaning the aligner later assigns comes from the period decipherment (grade H).

    python3 axcomp/build_pairs.py N        (reads ciphertext_N.tsv, decipherment_N.txt;
                                            writes axcomp/pairs_N.tsv, axcomp/anchors_N.tsv)
Roman numerals in the cipher (i, ii, iii) are kept distinct as 901, 902, 903.
"""
import csv, re, sys, os

MINANCHOR = 9
ROMAN = {'i': '901', 'ii': '902', 'iii': '903'}
HERE = os.path.dirname(os.path.abspath(__file__))
TOP = os.path.dirname(HERE)


def letters(s):
    return re.sub(r'[^a-z]', '', s.lower().replace('&', 'et'))


def load_plain(n):
    txt = []
    for line in open(os.path.join(TOP, 'decipherment_%s.txt' % n), encoding='utf-8'):
        if line.startswith('#'):
            continue
        txt.append(line)
    t = ' '.join(txt).replace('//', ' ').replace('[?]', '')
    t = re.sub(r'\([^)]*\)', ' ', t)
    words = [w for w in t.split() if letters(w)]
    # letter stream with the index of the word each letter belongs to
    L, widx = [], []
    for k, w in enumerate(words):
        for ch in letters(w):
            L.append(ch)
            widx.append(k)
    return words, ''.join(L), widx


def load_cipher(n):
    toks = []
    with open(os.path.join(TOP, 'ciphertext_%s.tsv' % n), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            s = r['sign'].strip()
            if s.startswith('='):
                toks.append(('clear', s[1:], r['line']))
            elif s.lower() in ROMAN:
                toks.append(('num', ROMAN[s.lower()], r['line']))
            elif s.rstrip('?').isdigit():
                toks.append(('num', s.rstrip('?'), r['line']))
    return toks


def semiglobal(a, text):
    """best (dist, start, end) of pattern a inside text, free ends in text."""
    n, m = len(a), len(text)
    prev = [0] * (m + 1)
    start = list(range(m + 1))
    for i in range(1, n + 1):
        cur = [i] + [0] * m
        cst = [0] * (m + 1)
        for j in range(1, m + 1):
            best, bs = prev[j - 1] + (a[i - 1] != text[j - 1]), start[j - 1]
            if prev[j] + 1 < best:
                best, bs = prev[j] + 1, start[j]
            if cur[j - 1] + 1 < best:
                best, bs = cur[j - 1] + 1, cst[j - 1]
            cur[j], cst[j] = best, bs
        prev, start = cur, cst
    j = min(range(m + 1), key=lambda j: prev[j])
    return prev[j], start[j], j


def main(n):
    words, L, widx = load_plain(n)
    toks = load_cipher(n)
    # group clear runs
    runs, k = [], 0
    while k < len(toks):
        if toks[k][0] == 'clear':
            e = k
            while e < len(toks) and toks[e][0] == 'clear':
                e += 1
            runs.append((k, e))
            k = e
        else:
            k += 1
    ptr, last_tok = 0, 0
    cuts = []  # (tok_start, tok_end, let_start, let_end, dist)
    for s, e in runs:
        a = letters(''.join(t[1] for t in toks[s:e]))
        if len(a) < MINANCHOR:
            continue
        nnum = sum(1 for t in toks[last_tok:s] if t[0] == 'num')
        nclr = len(letters(''.join(t[1] for t in toks[last_tok:s] if t[0] == 'clear')))
        lo = ptr + max(0, int(0.5 * nnum) + nclr - 20)
        hi = min(len(L), ptr + int(3.0 * nnum) + nclr + 60 + len(a))
        d, st, en = semiglobal(a, L[lo:hi])
        if d <= 0.35 * len(a):
            cuts.append((s, e, lo + st, lo + en, d, a))
            ptr, last_tok = lo + en, e
    anchors = os.path.join(HERE, 'anchors_%s.tsv' % n)
    with open(anchors, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['cipher_line', 'anchor', 'plain_found', 'dist'])
        for s, e, ls, le, d, a in cuts:
            w.writerow([toks[s][2], a, L[ls:le], d])
    # pairs between anchors
    rows = []
    bounds = [(0, 0)] + [(c[1], c[3]) for c in cuts]
    ends = [(c[0], c[2]) for c in cuts] + [(len(toks), len(L))]
    for (ts, ls), (te, le) in zip(bounds, ends):
        seg = toks[ts:te]
        if not any(t[0] == 'num' for t in seg):
            continue
        plain = ''
        if le > ls:
            # rebuild the span with word boundaries
            out, cur = [], widx[ls]
            word = ''
            for p in range(ls, le):
                if widx[p] != cur:
                    out.append(word); word = ''; cur = widx[p]
                word += L[p]
            out.append(word)
            plain = ' '.join(out)
        rows.append([seg[0][2], plain, seg[-1][2], ' '.join(t[1] for t in seg)])
    with open(os.path.join(HERE, 'pairs_%s.tsv' % n), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw'])
        w.writerows(rows)
    nn = sum(1 for t in toks if t[0] == 'num')
    print('%s: %d tokens (%d numerals), %d clear runs, %d anchors, %d pairs, plain letters %d'
          % (n, len(toks), nn, len(runs), len(cuts), len(rows), len(L)))


if __name__ == '__main__':
    main(sys.argv[1])
