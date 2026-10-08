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
    python3 tools/interlinear_align.py stream SYMBOLS.txt TEXT.txt OUT_KEY.tsv [--band N] [--step N] [--iters N]
            (a whole letter against its whole separate clear copy: tools/stream_align.py, RUN2-NXALN 4 Oct 2026)
    python3 tools/interlinear_align.py align PAIRS.tsv OUT_ALIGN.tsv OUT_KEY.tsv [--floor N] [--clear-consumes]
            [--prior KEY.tsv] [--code-prefix PFX] [--null-cost X] [--wildcard C]
            [--max-chunk N] [--seg-bonus B] [--len-prior X]

--floor N: groups below N take at most one letter (default 100, Thurloe; 121 for the
Nassau 1573-74 tables, where 1-120 are letters). --clear-consumes (26 Sept 2026, AX-COMP):
a clear word written among the cipher groups takes its own span of the plain text, for a
separate clear decipherment of a letter that mixes clear words with cipher (the Nassau
letters), rather than Thurloe's interlinear lines, where the clear word is not repeated above.
--prior KEY.tsv: seed the first iteration with the single-letter values below --floor from a
known table (2 counts each), so long spans between clear anchors do not drift; the codes at or
above --floor (names, words, nulls) are never seeded and take their meaning from the plain text
alone. Counts for the seeded codes are then not independent evidence for that table.

--code-prefix PFX (26 Sept 2026, AX2-BRO4): a codebook whose codes are not numerals-with-a-floor
but an arbitrary symbol set (digits and single letters mixed, e.g. Brochado's homophonic cipher,
one code = one plaintext letter always, no word/name codes at all). Mark every CODE token in
cipher_raw with the prefix (e.g. "@2", "@x", "@16") when building PAIRS.tsv; a token without the
prefix is a literal clear word already printed in the cipher line (Portuguese abbreviations,
--clear-consumes applies to these same as Thurloe's). Every prefixed code is always floor (0 or 1
plain letters, like a below-floor Thurloe numeral) regardless of its value -- there is no
above-floor word-code class in this mode. --prior with --code-prefix seeds every code (not only
digit-named ones) whose meaning is a single letter, ignoring --floor entirely (moot in this mode).

--null-cost X and --wildcard C (27 Sept 2026, campaign fr4715-f61-mayenne-1592 step H11): for an interlinear
markup over a cipher whose sign classes are largely nulls (Mayenne's polyphonic table: about 40% of f.61's signs
are dashed by Tomokiyo). The Thurloe default charges -3.0 for a code that takes no plain letter, which pushes
letters onto null codes when the plain line is shorter than the cipher line; --null-cost sets that charge
(0 = free). --wildcard C keeps the character C of the plain line as an explicit "sign here, unread" position:
a code may take it as its one-character chunk at score 0 (no prior bonus, no prior miss), it is never counted
as evidence for the code's meaning, and it never joins a longer chunk. Without --wildcard every non-letter is
stripped from the plain line as before.

--max-chunk N, --seg-bonus B and --len-prior X (2 Oct 2026, NEXT-PAG, clairambault1225-paget-1714): for a syllabic
code (Paget 1714: one code = a syllable or a short word, about two letters, chunks not on word boundaries). The
Thurloe defaults let an at-or-above-floor code take up to 14 letters and add B=1.0 for a chunk that starts and 1.0
for one that ends an OCR word, so from a flat start one code soaks up a whole gloss word and hard-EM locks it in.
--max-chunk caps the chunk length, --seg-bonus sets the word-boundary bonus (0 = none), and --len-prior X charges
X per letter of distance between a chunk's length and the pair's own letters-per-code ratio, so the first
iteration splits each gloss roughly evenly and consistency across pairs does the rest. Defaults reproduce the
Thurloe behaviour exactly.

--digits N and --word-prior (2 Oct 2026, GAPS8-na-janssens-java-1811): for a word/syllable nomenclator with codes up
to four digits (Janssens 1811: 1-1197) checked against a separate plain copy rather than an interlinear line. --digits N
lets a numeral of up to N digits count as a code (default 3, Thurloe; a 4-digit group was 'doubtful' before). With
--prior KEY.tsv, --word-prior seeds EVERY code in the key (any length, any floor) with its meaning's letters (accents
folded, 2 counts), not only single-letter values below --floor: the use is testing a period gloss against an
independent plain copy, where each code occurs once or twice and a flat start has nothing to agree with (GAPS8: 2/209
positions from a flat start). The seeded counts are then the hypothesis under test, not independent evidence: report
agreement against the same run on the codes in shuffled order. Without either flag nothing changes.

--keep-fs (2 Oct 2026, NEVBIR-87ALIGN, nevers-birago-fr3251-1572): the f == s fold exists for OCR of a printed
long s; a clear sheet read by eye from a manuscript has no long-s confusion, and a cipher with distinct f and s
signs needs the two kept apart in the counts. Default unchanged.

--code-chunk N (4 Oct 2026, JM-ALPHA, rah-juan-manuel-1521): with --code-prefix, let a prefixed code take up to N
plain letters instead of 0-1, for a letter alphabet that may also carry syllable signs (Juan Manuel 1522: symbols
among word codes; the word codes are written into the pairs as their decoded clear words with --clear-consumes).
Default 1 reproduces the --code-prefix behaviour exactly. --word-code-prefix P (same job): with --code-prefix, a token
marked P (e.g. "%kig", a code group missing from the published table) is a word code taking 0..--max-chunk letters,
learned from the plain text like an above-floor numeral; its value keeps the prefix in the key.

--shuffle N [--seed S] [--min-share X] [--shuffle-out FILE.json] (6 Oct 2026, R9-WVOALIGN, wvo-hessen-1564 f.23):
after the real run, re-run the same alignment N times with the plain lines dealt to the wrong cipher lines (a random
derangement of plain_raw across the pairs, seed S, default 1564) and report the rule-3 statistic for the real run and the
draws: CONSISTENT = number of code values whose top chunk is non-empty, occurs >= 2 times, on >= 2 different cipher lines,
and is >= X (default 0.6) of that value's aligned (non-empty) occurrences. Shuffling which gloss sits over which cipher
line can move this number (a gloss over the wrong line gives letters that disagree across lines), so the control is able
to fail differently from the target. Prints real, control mean, p95, max and the empirical p; FILE.json keeps every draw.
Without --shuffle nothing changes.

--fix KEY.tsv (6 Oct 2026, R9-MANTPOOL, sachsstaatsarchiv-manteuffel-1712): hold every code in KEY.tsv (columns code|value,
any length, '|' separating alternative values, accents folded, non-letters dropped; a row with an empty value is a null and
is held to no letters) at its key value through EVERY iteration, 10 counts per alternative, instead of seeding it once
(--prior/--word-prior): the fixed codes act as anchors and only the codes absent from KEY.tsv are re-estimated. The fixed
codes' own chunks still appear in the alignment TSV but are not evidence; report only the free codes. Use with a pooled
PAIRS.tsv of many glossed multi-code runs, where a free code's chunk is learned from its agreement across runs.

--cipher-pair A B --out DIR [--iters N] [--gap-open X] [--gap-ext Y] [--min-n N] [--min-lift L]
(8 Oct 2026, TT-PAIR, LANE TOOLS-TOMO; Tomokiyo practice 7, servien.htm "Identifying Symbols by Aligning Two
Ciphertexts", Servien to Sabran, Baluze 155 f.123/f.127, 1632): two token files of ONE text in two encipherments (a
letter and its duplicata, or the same despatch to two ambassadors). Whitespace-separated cipher tokens; a clear word is
written in braces, {francois}, and is split into clear letters; '|' and line breaks are ignored. No plaintext is needed.
Affine-gap Needleman-Wunsch (Gotoh) over the two streams, iterated align -> symbol-equivalence update -> realign
(Tomokiyo: "the identified symbols reveal letters; revealed letters allow aligning more portions ... and the alignment
reveals identification of more homophones"; leave-one-out, so a column never votes for itself): a clear letter against the same clear letter is an anchor (+4; words in
clear in BOTH copies are plaintext, not nulls); a cipher token against a clear letter in the other copy is a crib (its
letter is counted for that symbol); a cipher pair scores by the lift of its co-alignment count over chance in the last
alignment, plus a bonus or charge when both symbols carry a crib letter. A contradiction is resolved by the gap model,
i.e. a one-place shift ("cete" against "ceste"). Writes DIR/alignment.tsv (column, A token, B token, kind, score,
confidence = share of the A symbol's alignments that go to this B symbol), DIR/equivalences.tsv (A symbol, B symbol,
n, lift, group), DIR/groups.tsv (homophone groups: connected components of the accepted equivalences, so two A symbols
that both map to one B symbol fall in one group; crib letter by vote) and DIR/cribs.tsv (each cipher run in one copy set
against a clear word in the other). Meant to catch: homophones of one letter in two independent encipherments of the
same text, with insertions and wording differences between the copies. Must NOT flag: two DIFFERENT texts of the same
length (the null control) -- equivalences there fall to chance precision. Grade from a known two-copy case only.
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


def fold_accents(s):
    import unicodedata
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def fold(chunk):
    """The print's long s is read by OCR as f, and u/v are one letter in 1656:
    compare chunks with f == s and v == u. --keep-fs keeps f and s apart (a manuscript clear sheet, not OCR)."""
    if not FOLD_FS:
        return chunk.replace('v', 'u')
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


MAX_DIGITS = 3      # --digits
WORD_PRIOR = False  # --word-prior
FOLD_FS = True      # --keep-fs turns this off
CODE_CHUNK = 1      # --code-chunk N: a --code-prefix code may take up to N plain letters (default 1)
FIXED = {}          # --fix KEY.tsv: code -> Counter held constant every iteration
SHUFFLE = 0         # --shuffle N: row-shuffled control draws (R9-WVOALIGN)
SEED = 1564         # --seed
MIN_SHARE = 0.6     # --min-share
SHUFFLE_OUT = None  # --shuffle-out FILE.json
WORD_PFX = None     # --word-code-prefix P: with --code-prefix, a token marked P is a word code (0..--max-chunk letters)


def classify_token(tok, code_prefix=None):
    """-> (kind, value): kind num (value int), code (value str, --code-prefix mode: a
    non-numeral codebook symbol, always floor -- see run_align), clear (parenthesised
    numeral, a word in clear, or any token not marked as a code in --code-prefix mode),
    doubtful (value None)."""
    if code_prefix is not None:
        if WORD_PFX and tok.startswith(WORD_PFX):
            return 'num', WORD_PFX + tok[len(WORD_PFX):]
        if tok.startswith(code_prefix):
            return 'code', tok[len(code_prefix):]
        return 'clear', None
    core = tok.strip('.,;:\'"')
    if core.startswith('(') or core.endswith(')'):
        inner = core.strip('()').strip('.,;:')
        if inner.translate(CLEAN).isdigit():
            return 'clear', None
    c = core.strip('()').translate(CLEAN)
    if c.isdigit() and 1 <= len(c) <= MAX_DIGITS:
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


def plain_letters(raw, wildcard=None):
    """letters of the plain line (lowercase, 1 -> l) with a flag per letter for
    'starts an OCR segment' and 'ends an OCR segment'. --wildcard C keeps C as a position."""
    letters, starts, ends = [], [], []
    for seg in raw.split():
        seg = seg.lower().replace('1', 'l').replace('&', 'ct')
        seg = re.sub(r'[^a-z' + (re.escape(wildcard) if wildcard else '') + r']', '', seg)
        for k, ch in enumerate(seg):
            letters.append(ch)
            starts.append(k == 0)
            ends.append(k == len(seg) - 1)
    return ''.join(letters), starts, ends


def align_pair(toks, letters, starts, ends, floor, prior, clear_words=None, null_cost=-3.0, wildcard=None,
               max_chunk=MAXCHUNK, seg_bonus=1.0, len_prior=0.0):
    """DP; returns list of chunks (one per token) or None for tokens left unaligned.
    clear_words (--clear-consumes): per token, the letters of a clear word written in the
    cipher line, which then takes its own span of the plain line instead of none."""
    N, L = len(toks), len(letters)
    NEG = -1e9
    best = [[NEG] * (L + 1) for _ in range(N + 1)]
    back = [[None] * (L + 1) for _ in range(N + 1)]
    best[0][0] = 0.0
    ncode = sum(k in ('num', 'code', 'doubtful') for k, _ in toks)
    ratio = L / ncode if ncode else 1.0
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
            elif kind == 'code':
                lens = range(0, CODE_CHUNK + 1)  # floor by default (0-1); --code-chunk N for a syllable sign
            elif kind == 'num' and not isinstance(val, str) and val < floor:
                lens = [0, 1]
            else:
                lens = range(0, max_chunk + 1)
            for ln in lens:
                if j + ln > L:
                    break
                sc = -0.5
                if ln == 0:
                    sc = (-1.0 - len(cw) if cw else 0.0) if kind == 'clear' else null_cost
                elif wildcard and wildcard in letters[j:j + ln]:
                    if ln > 1 or kind == 'clear':
                        continue                      # a wildcard never joins a longer chunk
                    sc = 0.0                          # an unread position: no evidence either way
                elif kind == 'clear':
                    ch = fold(letters[j:j + ln])
                    same = sum(a == b for a, b in zip(ch, fold(cw)))
                    sc = 1.0 * same - 1.0 * (max(ln, len(cw)) - same)
                else:
                    ch = letters[j:j + ln]
                    sc += seg_bonus if starts[j] else 0.0
                    sc += seg_bonus if ends[j + ln - 1] else 0.0
                    if len_prior:
                        sc -= len_prior * abs(ln - ratio)
                    if kind in ('num', 'code') and val in FIXED and '' in FIXED[val]:
                        continue                      # --fix: a null code takes no letters
                    if kind in ('num', 'code') and prior.get(val):
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


def load_prior(path, floor, code_mode=False):
    """--prior KEY.tsv: seed counts (2 each) from a value->meaning key (columns code|value, value|meaning),
    for codes below floor only; letter values only, so a name code is never seeded.
    code_mode (--code-prefix): every code is floor by construction (align_pair's kind=='code' branch),
    so seed any code (digit or not) with a single-letter meaning, ignoring the floor comparison."""
    prior = defaultdict(Counter)
    with open(path, encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            code = r.get('code') or r.get('value')
            mean = r.get('meaning') if 'meaning' in r else r.get('value')
            if WORD_PRIOR:
                letters = re.sub(r'[^a-z]', '', fold_accents(mean or '').lower())
                if code and code.strip().isdigit() and letters:
                    prior[int(code)][fold(letters)] += 2
                continue
            if not (code and mean and mean.isalpha() and len(mean) == 1):
                continue
            if code_mode:
                prior[code.rstrip('±')][fold(mean.lower())] += 2
            elif code.isdigit() and int(code) < floor:
                prior[int(code)][fold(mean.lower())] += 2
    return prior


def load_fixed(path):
    """--fix KEY.tsv -> {int code: Counter(folded alternative -> 10)}; '' marks a null."""
    out = {}
    with open(path, encoding='utf-8') as f:
        for r in csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'):
            code = (r.get('code') or '').strip()
            if not code.isdigit():
                continue
            alts = (r.get('value') or '').split('|')
            c = Counter()
            for a in alts:
                c[fold(re.sub(r'[^a-z]', '', fold_accents(a).lower()))] += 10
            out[int(code)] = c
    return out


def run_align(pairs, floor=100, iters=6, clear_consumes=False, prior=None, code_prefix=None,
              null_cost=-3.0, wildcard=None, max_chunk=MAXCHUNK, seg_bonus=1.0, len_prior=0.0):
    prepared = []
    for p in pairs:
        raw = p['cipher_raw'].split()
        toks = [classify_token(t, code_prefix) for t in raw]
        letters, starts, ends = plain_letters(p['plain_raw'], wildcard)
        cws = None
        if clear_consumes:
            cws = [plain_letters(t)[0] if k == 'clear' else '' for t, (k, _) in zip(raw, toks)]
        prepared.append((p, raw, toks, letters, starts, ends, cws))
    prior = prior or {}
    if FIXED:
        prior = defaultdict(Counter, {k: Counter(v) for k, v in prior.items()})
        for v, c in FIXED.items():
            prior[v] = Counter(c)
    for _ in range(iters):
        counts = defaultdict(Counter)
        shown = defaultdict(Counter)
        results = []
        for p, raw, toks, letters, starts, ends, cws in prepared:
            chunks = align_pair(toks, letters, starts, ends, floor, prior, cws, null_cost, wildcard,
                                max_chunk, seg_bonus, len_prior)
            results.append(chunks)
            for (kind, val), c in zip(toks, chunks):
                if kind in ('num', 'code') and c and c[1] > c[0] and not (wildcard and wildcard in letters[c[0]:c[1]]):
                    counts[val][fold(letters[c[0]:c[1]])] += 1
                    shown[(val, fold(letters[c[0]:c[1]]))][letters[c[0]:c[1]]] += 1
        prior = counts
        if FIXED:  # the key output keeps the observed chunks; only the next iteration's prior is held
            prior = defaultdict(Counter, counts)
            for v, c in FIXED.items():
                prior[v] = Counter(c)
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
            if kind in ('num', 'code'):
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


def consistent_count(prepared, results, min_share=0.6):
    """--shuffle statistic: code values whose top non-empty chunk occurs >= 2 times on >= 2 cipher lines and is
    >= min_share of the value's non-empty chunks."""
    per = defaultdict(Counter)
    lines = defaultdict(lambda: defaultdict(set))
    for (p, raw, toks, letters, starts, ends, _cws), chunks in zip(prepared, results):
        for (kind, val), c in zip(toks, chunks):
            if kind in ('num', 'code') and c and c[1] > c[0]:
                ch = fold(letters[c[0]:c[1]])
                per[val][ch] += 1
                lines[val][ch].add(p['cipher_line'])
    n = 0
    for val, cnt in per.items():
        top, topn = top_of(cnt)
        if topn >= 2 and len(lines[val][top]) >= 2 and topn >= min_share * sum(cnt.values()):
            n += 1
    return n


def shuffle_control(pairs, run_kwargs, real):
    import json
    import random
    rng = random.Random(SEED)
    draws = []
    idx = list(range(len(pairs)))
    for _ in range(SHUFFLE):
        while True:
            perm = idx[:]
            rng.shuffle(perm)
            if all(a != b for a, b in zip(idx, perm)):
                break
        sp = [dict(p, plain_raw=pairs[k]['plain_raw']) for p, k in zip(pairs, perm)]
        prep, res, _c, _s = run_align(sp, **run_kwargs)
        draws.append(consistent_count(prep, res, MIN_SHARE))
    srt = sorted(draws)
    p95 = srt[min(len(srt) - 1, int(0.95 * len(srt)))]
    mean = sum(draws) / len(draws)
    pval = (1 + sum(d >= real for d in draws)) / (1 + len(draws))
    print('shuffle control: real %d; control mean %.2f, p95 %d, max %d, n %d; p = %.4f; real > p95: %s'
          % (real, mean, p95, srt[-1], len(draws), pval, real > p95))
    if SHUFFLE_OUT:
        with open(SHUFFLE_OUT, 'w') as f:
            json.dump({'real': real, 'mean': mean, 'p95': p95, 'max': srt[-1], 'p': pval, 'seed': SEED,
                       'min_share': MIN_SHARE, 'draws': draws}, f)


def cmd_align(pairs_path, out_align, out_key, floor=100, clear_consumes=False, prior_path=None, code_prefix=None,
              null_cost=-3.0, wildcard=None, max_chunk=MAXCHUNK, seg_bonus=1.0, len_prior=0.0):
    prior = load_prior(prior_path, floor, code_mode=code_prefix is not None) if prior_path else None
    pairs = load_pairs(pairs_path)
    kw = dict(floor=floor, clear_consumes=clear_consumes, prior=prior, code_prefix=code_prefix, null_cost=null_cost,
              wildcard=wildcard, max_chunk=max_chunk, seg_bonus=seg_bonus, len_prior=len_prior)
    prepared, results, counts, shown = run_align(pairs, **kw)
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
    if SHUFFLE:
        real = consistent_count(prepared, results, MIN_SHARE)
        shuffle_control(pairs, kw, real)


# ---------------------------------------------------------------------------------------------------------------
# --cipher-pair (TT-PAIR, 8 Oct 2026; Tomokiyo practice 7, servien.htm). See the module docstring.

def cp_read(path):
    """Token file -> list of (kind, value): ('c', symbol) for a cipher token, ('p', letter) for a clear letter."""
    out = []
    txt = open(path, encoding='utf-8').read().replace('|', ' ')
    for m in re.finditer(r'\{([^}]*)\}|(\S+)', txt):
        if m.group(1) is not None:
            for ch in fold(fold_accents(m.group(1).lower())):
                if ch.isalpha():
                    out.append(('p', ch))
        else:
            out.append(('c', m.group(2)))
    return out


def cp_align(A, B, score, gap_open=-3.0, gap_ext=-0.4):
    """Gotoh affine-gap global alignment; returns a list of (i or None, j or None)."""
    import math
    n, m = len(A), len(B)
    NEG = -math.inf
    M = [[NEG] * (m + 1) for _ in range(n + 1)]
    X = [[NEG] * (m + 1) for _ in range(n + 1)]   # gap in B (A token unmatched)
    Y = [[NEG] * (m + 1) for _ in range(n + 1)]   # gap in A (B token unmatched)
    M[0][0] = 0.0
    for i in range(1, n + 1):
        X[i][0] = gap_open + (i - 1) * gap_ext
    for j in range(1, m + 1):
        Y[0][j] = gap_open + (j - 1) * gap_ext
    for i in range(1, n + 1):
        Mi, Xi, Yi, Mp, Xp, Yp = M[i], X[i], Y[i], M[i - 1], X[i - 1], Y[i - 1]
        a = A[i - 1]
        for j in range(1, m + 1):
            best = Mp[j - 1]
            if Xp[j - 1] > best:
                best = Xp[j - 1]
            if Yp[j - 1] > best:
                best = Yp[j - 1]
            Mi[j] = best + score(a, B[j - 1], i - 1, j - 1)
            o = max(Mp[j], Yp[j]) + gap_open
            e = Xp[j] + gap_ext
            Xi[j] = o if o > e else e
            o = max(Mi[j - 1], Xi[j - 1]) + gap_open
            e = Yi[j - 1] + gap_ext
            Yi[j] = o if o > e else e
    i, j = n, m
    st = max((M[i][j], 0), (X[i][j], 1), (Y[i][j], 2))[1]
    path = []
    while i > 0 or j > 0:
        if st == 0:
            path.append((i - 1, j - 1))
            pm, px, py = M[i - 1][j - 1], X[i - 1][j - 1], Y[i - 1][j - 1]
            st = 0 if pm >= px and pm >= py else (1 if px >= py else 2)
            i, j = i - 1, j - 1
        elif st == 1:
            path.append((i - 1, None))
            st = 1 if (i > 1 and X[i - 1][j] + gap_ext >= max(M[i - 1][j], Y[i - 1][j]) + gap_open) else \
                (0 if M[i - 1][j] >= Y[i - 1][j] else 2)
            if i - 1 == 0 and j == 0:
                st = 0
            i -= 1
        else:
            path.append((None, j - 1))
            st = 2 if (j > 1 and Y[i][j - 1] + gap_ext >= max(M[i][j - 1], X[i][j - 1]) + gap_open) else \
                (0 if M[i][j - 1] >= X[i][j - 1] else 1)
            if i == 0 and j - 1 == 0:
                st = 0
            j -= 1
    path.reverse()
    return path


def cp_counts(A, B, path):
    pair, ca, cb = Counter(), Counter(), Counter()
    la, lb = defaultdict(Counter), defaultdict(Counter)
    for i, j in path:
        if i is None or j is None:
            continue
        (ka, va), (kb, vb) = A[i], B[j]
        if ka == 'c' and kb == 'c':
            pair[(va, vb)] += 1
            ca[va] += 1
            cb[vb] += 1
        elif ka == 'c' and kb == 'p':
            la[va][vb] += 1
        elif ka == 'p' and kb == 'c':
            lb[vb][va] += 1
    return pair, ca, cb, la, lb


def cp_label(cnt, min_n=2, share=0.6):
    if not cnt:
        return None
    x, k = max(cnt.items(), key=lambda kv: (kv[1], kv[0]))
    tot = sum(cnt.values())
    return x if k >= min_n and k >= share * tot else None


def cp_lift(pair, ca, cb, a, b):
    import math
    tot = sum(ca.values()) or 1
    exp = ca[a] * cb[b] / tot
    return math.log((pair[(a, b)] + 0.2) / (exp + 0.2))


def cp_run(A, B, iters=8, gap_open=-3.0, gap_ext=-0.4):
    """Iterate align -> equivalence counts -> realign until the alignment stops changing. Returns (path, counts)."""
    import math
    state = {'pair': Counter(), 'ca': Counter(), 'cb': Counter(), 'labA': {}, 'labB': {}, 'it': 0, 'cols': set()}

    def score(x, y, i, j):
        (kx, vx), (ky, vy) = x, y
        if kx == 'p' and ky == 'p':
            return 4.0 if vx == vy else -4.0
        if kx == 'c' and ky == 'c':
            if state['it'] == 0:
                return 1.0
            # leave-one-out: a column does not vote for itself, so the last alignment cannot simply lock itself in
            own = 1 if (i, j) in state['cols'] else 0
            pair, ca, cb = state['pair'], state['ca'], state['cb']
            tot = (sum(ca.values()) or 1)
            exp = (ca[vx] - own) * (cb[vy] - own) / tot
            s = math.log((pair[(vx, vy)] - own + 0.2) / (max(exp, 0.0) + 0.2))
            s = max(-3.0, min(3.0, s))
            lx, ly = state['labA'].get(vx), state['labB'].get(vy)
            if lx and ly:
                s += 2.0 if lx == ly else -2.0
            return s
        sym, let, lab = (vx, vy, state['labA']) if kx == 'c' else (vy, vx, state['labB'])
        l = lab.get(sym)
        if l is None:
            return 0.5
        return 3.0 if l == let else -2.0

    path, prev = None, None
    for it in range(iters):
        state['it'] = it
        path = cp_align(A, B, score, gap_open, gap_ext)
        pair, ca, cb, la, lb = cp_counts(A, B, path)
        # crib letters, propagated one hop through the cipher-cipher equivalences
        labA, labB = {}, {}
        for s_, c in la.items():
            if cp_label(c):
                labA[s_] = cp_label(c)
        for s_, c in lb.items():
            if cp_label(c):
                labB[s_] = cp_label(c)
        votesA, votesB = defaultdict(Counter), defaultdict(Counter)
        for (a, b), k in pair.items():
            if b in labB:
                votesA[a][labB[b]] += k
            if a in labA:
                votesB[b][labA[a]] += k
        for a, v in votesA.items():
            v.update(la.get(a, {}))
            if cp_label(v, 2, 0.6):
                labA.setdefault(a, cp_label(v, 2, 0.6))
        for b, v in votesB.items():
            v.update(lb.get(b, {}))
            if cp_label(v, 2, 0.6):
                labB.setdefault(b, cp_label(v, 2, 0.6))
        state.update(pair=pair, ca=ca, cb=cb, labA=labA, labB=labB,
                     cols={(i, j) for i, j in path if i is not None and j is not None})
        if path == prev:
            break
        prev = path
    return path, state


def cp_groups(state, min_n=2, min_lift=1.0):
    """Accepted equivalences and their connected components (homophone groups)."""
    pair, ca, cb = state['pair'], state['ca'], state['cb']
    acc = [(a, b, k, cp_lift(pair, ca, cb, a, b)) for (a, b), k in pair.items()
           if k >= min_n and cp_lift(pair, ca, cb, a, b) >= min_lift]
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, b, _k, _l in acc:
        parent[find(('A', a))] = find(('B', b))
    comp = defaultdict(list)
    for x in list(parent):
        comp[find(x)].append(x)
    gid = {}
    groups = []
    for n, root in enumerate(sorted(comp, key=lambda r: (-len(comp[r]), str(r)))):
        g = 'g%d' % (n + 1)
        mem = comp[root]
        for x in mem:
            gid[x] = g
        letters = Counter()
        for side, s_ in mem:
            l = (state['labA'] if side == 'A' else state['labB']).get(s_)
            if l:
                letters[l] += 1
        groups.append((g, sorted(s_ for side, s_ in mem if side == 'A'), sorted(s_ for side, s_ in mem if side == 'B'),
                       letters.most_common(1)[0][0] if letters else ''))
    return acc, gid, groups


def cp_cribs(A, B, path):
    """Each maximal run of cipher tokens in one copy aligned against clear letters in the other."""
    out = []
    for side, mine, other in (('A', 0, 1), ('B', 1, 0)):
        S, O = (A, B) if side == 'A' else (B, A)
        run_c, run_p, start = [], [], None
        for col, ij in enumerate(path + [(None, None)]):
            x, y = ij[mine], ij[other]
            if x is not None and y is not None and S[x][0] == 'c' and O[y][0] == 'p':
                if start is None:
                    start = col
                run_c.append(S[x][1])
                run_p.append(O[y][1])
            else:
                if len(run_c) >= 2:
                    out.append((side, start, ' '.join(run_c), ''.join(run_p)))
                run_c, run_p, start = [], [], None
    return out


def cmd_cipher_pair(a_path, b_path, out_dir, iters=8, gap_open=-3.0, gap_ext=-0.4, min_n=2, min_lift=1.0):
    import os
    A, B = cp_read(a_path), cp_read(b_path)
    path, state = cp_run(A, B, iters, gap_open, gap_ext)
    acc, gid, groups = cp_groups(state, min_n, min_lift)
    os.makedirs(out_dir, exist_ok=True)
    pair, ca = state['pair'], state['ca']

    def w(name, header, rows):
        with open(os.path.join(out_dir, name), 'w', encoding='utf-8', newline='') as f:
            wr = csv.writer(f, delimiter='\t', lineterminator='\n')
            wr.writerow(header)
            wr.writerows(rows)
    rows = []
    for col, (i, j) in enumerate(path):
        ta = A[i] if i is not None else None
        tb = B[j] if j is not None else None
        kind = 'gap'
        conf = ''
        sc = ''
        if ta and tb:
            kind = {'cc': 'cipher', 'pp': 'anchor', 'cp': 'crib', 'pc': 'crib'}[ta[0] + tb[0]]
            if kind == 'anchor' and ta[1] != tb[1]:
                kind = 'clash'
            if kind == 'cipher':
                conf = '%.2f' % (pair[(ta[1], tb[1])] / ca[ta[1]])
                sc = '%.2f' % cp_lift(pair, ca, state['cb'], ta[1], tb[1])
        show = lambda t: '' if t is None else (t[1] if t[0] == 'c' else '{%s}' % t[1])
        rows.append([col, show(ta), show(tb), kind, sc, conf])
    w('alignment.tsv', ['col', 'a', 'b', 'kind', 'lift', 'confidence'], rows)
    w('equivalences.tsv', ['a', 'b', 'n', 'lift', 'group'],
      [[a, b, k, '%.2f' % l, gid.get(('A', a), '')] for a, b, k, l in sorted(acc, key=lambda r: (-r[2], r[0], r[1]))])
    w('groups.tsv', ['group', 'a_symbols', 'b_symbols', 'crib_letter'],
      [[g, ' '.join(sa), ' '.join(sb), l] for g, sa, sb, l in groups])
    cribs = cp_cribs(A, B, path)
    w('cribs.tsv', ['cipher_copy', 'col', 'cipher_run', 'clear_in_other'], cribs)
    kinds = Counter(r[3] for r in rows)
    print('cipher-pair: A %d tokens, B %d; columns %s; equivalences %d; groups %d (%d with a crib letter); cribs %d'
          % (len(A), len(B), dict(kinds), len(acc), len(groups), sum(1 for g in groups if g[3]), len(cribs)))
    return path, state, acc, groups


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == '--cipher-pair':
        opts = {'--iters': 8, '--gap-open': -3.0, '--gap-ext': -0.4, '--min-n': 2, '--min-lift': 1.0, '--out': None}
        for flag in list(opts):
            if flag in a:
                k = a.index(flag)
                opts[flag] = a[k + 1] if flag == '--out' else type(opts[flag])(float(a[k + 1]))
                del a[k:k + 2]
        if len(a) != 3 or not opts['--out']:
            sys.exit('usage: interlinear_align.py --cipher-pair A.txt B.txt --out DIR [--iters N] [--gap-open X] '
                     '[--gap-ext Y] [--min-n N] [--min-lift L]')
        cmd_cipher_pair(a[1], a[2], opts['--out'], int(opts['--iters']), opts['--gap-open'], opts['--gap-ext'],
                        int(opts['--min-n']), opts['--min-lift'])
        sys.exit(0)
    if a and a[0] == 'stream':
        import stream_align
        stream_align.main(a[1:])
    elif a and a[0] == 'pairs':
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
        code_prefix = None
        if '--code-prefix' in a:
            k = a.index('--code-prefix')
            code_prefix = a[k + 1]
            del a[k:k + 2]
        null_cost, wildcard = -3.0, None
        if '--null-cost' in a:
            k = a.index('--null-cost')
            null_cost = float(a[k + 1])
            del a[k:k + 2]
        if '--wildcard' in a:
            k = a.index('--wildcard')
            wildcard = a[k + 1]
            del a[k:k + 2]
        max_chunk, seg_bonus, len_prior = MAXCHUNK, 1.0, 0.0
        if '--digits' in a:
            k = a.index('--digits')
            MAX_DIGITS = int(a[k + 1])
            del a[k:k + 2]
        if '--word-prior' in a:
            WORD_PRIOR = True
            a = [x for x in a if x != '--word-prior']
        if '--word-code-prefix' in a:
            k = a.index('--word-code-prefix')
            WORD_PFX = a[k + 1]
            del a[k:k + 2]
        if '--code-chunk' in a:
            k = a.index('--code-chunk')
            CODE_CHUNK = int(a[k + 1])
            del a[k:k + 2]
        if '--keep-fs' in a:
            FOLD_FS = False
            a = [x for x in a if x != '--keep-fs']
        for flag in ('--shuffle', '--seed', '--min-share', '--shuffle-out'):
            if flag in a:
                k = a.index(flag)
                v = a[k + 1]
                del a[k:k + 2]
                if flag == '--shuffle':
                    SHUFFLE = int(v)
                elif flag == '--seed':
                    SEED = int(v)
                elif flag == '--min-share':
                    MIN_SHARE = float(v)
                else:
                    SHUFFLE_OUT = v
        if '--fix' in a:
            k = a.index('--fix')
            FIXED.update(load_fixed(a[k + 1]))
            a = a[:k] + a[k + 2:]
        for flag in ('--max-chunk', '--seg-bonus', '--len-prior'):
            if flag in a:
                k = a.index(flag)
                v = a[k + 1]
                del a[k:k + 2]
                if flag == '--max-chunk':
                    max_chunk = int(v)
                elif flag == '--seg-bonus':
                    seg_bonus = float(v)
                else:
                    len_prior = float(v)
        cmd_align(a[1], a[2], a[3], floor, cc, prior_path, code_prefix, null_cost, wildcard,
                  max_chunk, seg_bonus, len_prior)
    else:
        sys.exit(__doc__)
