#!/usr/bin/env python3
"""Align a printed interlinear decipherment to the cipher groups printed beneath it.

Birch's 1742 Thurloe State Papers print many numeral-cipher letters with the
contemporary decipherment set above each cipher line, letter by letter or word by
word. In the djvu OCR the two lines survive as a pair: a "plain" line (spaced
letters and words, long-s read as f, l often read as 1) followed by a "cipher" line
(numerals, with the usual OCR digit confusions). This tool

  pairs  extracts every (plain line, cipher line) pair from a djvu line range into a
         TSV, verbatim, so the alignment can be regenerated without the gitignored
         djvu cache;
  align  aligns each pair by dynamic programming (each cipher group takes a chunk of
         the plain line's letters: one letter for a group below --code-floor, one or
         more for a code group at or above it, none for a null or a parenthesised
         clear numeral), iterating so that a group's chunk agrees with what the same
         group reads elsewhere in the letter, and writes a per-token alignment TSV
         and a value -> meaning key TSV with counts and agreement.

No cryptanalysis: every meaning comes from the printed decipherment. OCR-doubtful
tokens are resolved only when one of their digit-confusion candidates is a value
whose meaning (from the rest of the letter) matches the chunk aligned to it; the
alignment TSV records that as a repair.

    python3 tools/interlinear_align.py pairs DJVU FIRST LAST OUT_PAIRS.tsv
    python3 tools/interlinear_align.py align PAIRS.tsv OUT_ALIGN.tsv OUT_KEY.tsv [--floor N] [--clear-consumes]
            [--prior KEY.tsv]

--floor N: groups below N take at most one letter (default 100, Thurloe; 121 for the
Nassau 1573-74 tables, where 1-120 are letters). --clear-consumes (26 Sept 2026, AX-COMP):
a clear word written among the cipher groups takes its own span of the plain text, for a
separate clear decipherment of a letter that mixes clear words with cipher (the Nassau
letters), rather than Thurloe's interlinear lines, where the clear word is not repeated above.
--prior KEY.tsv: seed the first iteration with the single-letter values below --floor from a
known table (2 counts each), so long spans between clear anchors do not drift; the codes at or
above --floor (names, words, nulls) are never seeded and take their meaning from the plain text
alone. Counts for the seeded codes are then not independent evidence for that table.
"""
import csv
import itertools
import re
import sys
from collections import Counter, defaultdict

CLEAN = str.maketrans({'i': '1', 'I': '1', 'l': '1', 'L': '1', 'o': '0', 'O': '0', '°': '0'})
# wider OCR digit confusions, used only to propose repairs for doubtful tokens
CONFUSE = {
    'l': '1', 'I': '1', 'i': '1', 'L': '1', 'J': '1', 'j': '1', '!': '1', '|': '1', '*': '1',
    'o': '0', 'O': '0', '°': '0', 'Q': '0', 'D': '0',
    'S': '5', 's': '5', '$': '58', 'Z': '2', 'z': '2', 'g': '9', 'q': '9', 'y': '7',
    'B': '8', 'G': '6', 'b': '6', '^': '4', '%': '7', 'n': '11', 'u': '11', 'c': '9',
}
MAXCHUNK = 14


def fold(chunk):
    """The print's long s is read by OCR as f, and u/v are one letter in 1656:
    compare chunks with f == s and v == u."""
    return chunk.replace('f', 's').replace('v', 'u')


def digitish(tok):
    t = tok.strip('.,;:()\'"-')
    if not t:
        return False
    d = sum(c.isdigit() or c == '°' for c in t)
    return d * 2 >= len(t)


def is_cipher_line(line):
    tk = line.split()
    return len(tk) >= 3 and sum(digitish(t) for t in tk) / len(tk) >= 0.6


def cmd_pairs(djvu, first, last, out):
    lines = open(djvu, encoding='utf-8').read().split('\n')
    rows = []
    prev = None  # (lineno, text) of last non-blank non-cipher line
    for n in range(first, last + 1):
        s = lines[n - 1].strip()
        if not s:
            continue
        if is_cipher_line(s):
            if prev is not None:
                rows.append((prev[0], prev[1], n, s))
            prev = None
        else:
            prev = (n, s)
    with open(out, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw'])
        w.writerows(rows)
    print('%d pairs' % len(rows))


def classify_token(tok):
    """-> (kind, value): kind num (value int), clear (parenthesised numeral or a
    word in clear), doubtful (value None)."""
    core = tok.strip('.,;:\'"')
    if core.startswith('(') or core.endswith(')'):
        inner = core.strip('()').strip('.,;:')
        if inner.translate(CLEAN).isdigit():
            return 'clear', None
    c = core.strip('()').translate(CLEAN)
    if c.isdigit() and 1 <= len(c) <= 3:
        return 'num', int(c)
    if not digitish(tok):
        return 'clear', None
    return 'doubtful', None


def candidates(tok):
    core = tok.strip('.,;:()\'"-')
    opts = []
    for ch in core:
        if ch.isdigit():
            opts.append([ch])
        elif ch in CONFUSE:
            opts.append(list(CONFUSE[ch]) + [''])
        else:
            opts.append([''])
    out = set()
    for combo in itertools.islice(itertools.product(*opts), 4096):
        s = ''.join(combo)
        if s.isdigit() and 1 <= len(s) <= 4:
            out.add(int(s))
    return sorted(out)


def plain_letters(raw):
    """letters of the plain line (lowercase, 1 -> l) with a flag per letter for
    'starts an OCR segment' and 'ends an OCR segment'."""
    letters, starts, ends = [], [], []
    for seg in raw.split():
        seg = seg.lower().replace('1', 'l').replace('&', 'ct')
        seg = re.sub(r'[^a-z]', '', seg)
        for k, ch in enumerate(seg):
            letters.append(ch)
            starts.append(k == 0)
            ends.append(k == len(seg) - 1)
    return ''.join(letters), starts, ends


def align_pair(toks, letters, starts, ends, floor, prior, clear_words=None):
    """DP; returns list of chunks (one per token) or None for tokens left unaligned.
    clear_words (--clear-consumes): per token, the letters of a clear word written in the
    cipher line, which then takes its own span of the plain line instead of none."""
    N, L = len(toks), len(letters)
    NEG = -1e9
    best = [[NEG] * (L + 1) for _ in range(N + 1)]
    back = [[None] * (L + 1) for _ in range(N + 1)]
    best[0][0] = 0.0
    for j in range(1, L + 1):  # leading plain text not over a group
        best[0][j] = -0.3 * j
        back[0][j] = ('skip', 0, j - 1)
    for i in range(N + 1):
        for j in range(L + 1):
            cur = best[i][j]
            if cur <= NEG / 2:
                continue
            if j < L and i > 0:  # interior / trailing plain letter with no group
                pen = -0.3 if i == N else -2.5
                if cur + pen > best[i][j + 1]:
                    best[i][j + 1] = cur + pen
                    back[i][j + 1] = ('skip', i, j)
            if i == N:
                continue
            kind, val = toks[i]
            cw = clear_words[i] if clear_words else ''
            if kind == 'clear' and cw:
                lens = sorted({0, max(1, len(cw) - 1), len(cw), len(cw) + 1})
            elif kind == 'clear':
                lens = [0]
            elif kind == 'num' and val < floor:
                lens = [0, 1]
            else:
                lens = range(0, MAXCHUNK + 1)
            for ln in lens:
                if j + ln > L:
                    break
                sc = -0.5
                if ln == 0:
                    sc = (-1.0 - len(cw) if cw else 0.0) if kind == 'clear' else -3.0
                elif kind == 'clear':
                    ch = fold(letters[j:j + ln])
                    same = sum(a == b for a, b in zip(ch, fold(cw)))
                    sc = 1.0 * same - 1.0 * (max(ln, len(cw)) - same)
                else:
                    ch = letters[j:j + ln]
                    sc += 1.0 if starts[j] else 0.0
                    sc += 1.0 if ends[j + ln - 1] else 0.0
                    if kind == 'num' and prior.get(val):
                        cnt = prior[val]
                        tot = sum(cnt.values())
                        hit = cnt.get(fold(ch), 0)
                        sc += 4.0 * hit / tot - (1.5 if hit == 0 else 0)
                    if kind == 'doubtful':
                        sc -= 1.0
                nv = cur + sc
                if nv > best[i + 1][j + ln]:
                    best[i + 1][j + ln] = nv
                    back[i + 1][j + ln] = ('tok', i, j)
    # recover
    chunks = [None] * N
    i, j = N, L
    while (i, j) != (0, 0):
        b = back[i][j]
        if b[0] == 'skip':
            i, j = b[1], b[2]
        else:
            pi, pj = b[1], b[2]
            chunks[pi] = (pj, j)
            i, j = pi, pj
    return chunks


def load_pairs(path):
    with open(path, encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def load_prior(path, floor):
    """--prior KEY.tsv: seed counts (2 each) from a value->meaning key (columns code|value, value|meaning),
    for codes below floor only; letter values only, so a name code is never seeded."""
    prior = defaultdict(Counter)
    with open(path, encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            code = r.get('code') or r.get('value')
            mean = r.get('meaning') if 'meaning' in r else r.get('value')
            if code and code.isdigit() and int(code) < floor and mean and mean.isalpha() and len(mean) == 1:
                prior[int(code)][fold(mean.lower())] += 2
    return prior


def run_align(pairs, floor=100, iters=6, clear_consumes=False, prior=None):
    prepared = []
    for p in pairs:
        raw = p['cipher_raw'].split()
        toks = [classify_token(t) for t in raw]
        letters, starts, ends = plain_letters(p['plain_raw'])
        cws = None
        if clear_consumes:
            cws = [plain_letters(t)[0] if k == 'clear' else '' for t, (k, _) in zip(raw, toks)]
        prepared.append((p, raw, toks, letters, starts, ends, cws))
    prior = prior or {}
    for _ in range(iters):
        counts = defaultdict(Counter)
        shown = defaultdict(Counter)
        results = []
        for p, raw, toks, letters, starts, ends, cws in prepared:
            chunks = align_pair(toks, letters, starts, ends, floor, prior, cws)
            results.append(chunks)
            for (kind, val), c in zip(toks, chunks):
                if kind == 'num' and c and c[1] > c[0]:
                    counts[val][fold(letters[c[0]:c[1]])] += 1
                    shown[(val, fold(letters[c[0]:c[1]]))][letters[c[0]:c[1]]] += 1
        prior = counts
    return prepared, results, counts, shown


def display(shown, val, folded):
    """most common printed spelling of a folded chunk (ties: alphabetical)."""
    c = shown.get((val, folded))
    if not c:
        return folded
    return sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]


def top_of(cnt):
    return sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[0] if cnt else ('', 0)


def token_rows(prepared, results, counts, shown):
    rows = []
    for (p, raw, toks, letters, starts, ends, _cws), chunks in zip(prepared, results):
        for k, ((kind, val), c) in enumerate(zip(toks, chunks)):
            chunk = letters[c[0]:c[1]] if c else ''
            fchunk = fold(chunk)
            bstart = bool(c and c[1] > c[0] and starts[c[0]])
            bend = bool(c and c[1] > c[0] and ends[c[1] - 1])
            value, repair, status = '', '', ''
            if kind == 'num':
                value = str(val)
                cnt = counts.get(val, Counter())
                top, topn = top_of(cnt)
                if not chunk:
                    status = 'null-or-unaligned'
                elif fchunk == top and topn >= 2:
                    status = 'agrees'
                elif fchunk == top and bstart and bend:
                    status = 'single-segment'
                elif fchunk == top:
                    status = 'single'
                else:
                    status = 'conflict:%s' % display(shown, val, top)
            elif kind == 'doubtful':
                cands = candidates(raw[k])
                hits = [v for v in cands if chunk and counts.get(v) and top_of(counts[v])[0] == fchunk]
                if len(hits) == 1:
                    repair = str(hits[0])
                    status = 'repaired'
                else:
                    status = 'doubtful'
            else:
                status = 'clear'
            rows.append([p['cipher_line'], k, raw[k], kind, value, repair, chunk, status])
    return rows


def cmd_align(pairs_path, out_align, out_key, floor=100, clear_consumes=False, prior_path=None):
    prior = load_prior(prior_path, floor) if prior_path else None
    prepared, results, counts, shown = run_align(load_pairs(pairs_path), floor, clear_consumes=clear_consumes,
                                                 prior=prior)
    rows = token_rows(prepared, results, counts, shown)
    with open(out_align, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['cipher_line', 'idx', 'raw', 'kind', 'value', 'repair', 'plain_chunk', 'status'])
        w.writerows(rows)
    with open(out_key, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['value', 'meaning', 'n', 'agree', 'others'])
        for v in sorted(counts):
            cnt = counts[v]
            top, topn = top_of(cnt)
            rest = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[1:]
            others = ','.join('%s:%d' % (display(shown, v, m), c) for m, c in rest)
            w.writerow([v, display(shown, v, top), sum(cnt.values()), topn, others])
    st = Counter(r[7].split(':')[0] for r in rows)
    print('tokens %d; values %d; %s' % (len(rows), len(counts), dict(st)))


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == 'pairs':
        cmd_pairs(a[1], int(a[2]), int(a[3]), a[4])
    elif a and a[0] == 'align':
        floor = 100
        if '--floor' in a:
            k = a.index('--floor')
            floor = int(a[k + 1])
            del a[k:k + 2]
        prior_path = None
        if '--prior' in a:
            k = a.index('--prior')
            prior_path = a[k + 1]
            del a[k:k + 2]
        cc = '--clear-consumes' in a
        a = [x for x in a if x != '--clear-consumes']
        cmd_align(a[1], a[2], a[3], floor, cc, prior_path)
    else:
        sys.exit(__doc__)
