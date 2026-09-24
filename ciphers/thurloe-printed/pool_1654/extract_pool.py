#!/usr/bin/env python3
"""Extraction for the 1654 inline-numeral pool (LANE T worker C, 24 Sept 2026).

Re-reads the heading-to-signature span of each letter in the pool, verified by
hand against the cached djvu text (not the old padded thurloe_extract.py windows,
which cut two of the three letters short and misattributed all three senders --
see NOTES.md section 12). Produces:

  tokens.tsv -- one row per numeral token, cipher lines AND inline numerals found
                inside otherwise-plain lines (the brief's point 1: PLAIN-tagged
                lines carry cipher numerals here and must count).
  cribs.tsv  -- cipher runs (numeral tokens merged if within RUN_GAP lines of each
                other) with surrounding plain-text context. For P5_P6 and P7,
                Birch prints a full decipherment paragraph immediately after the
                cipher paragraph ("The fame letter decypherd") -- that text is
                pulled in as the run's "expected_content" and marked FOUND
                (Birch's own print), not CANDIDATE. P4 has no such companion, so
                its expected_content is this pass's own reading of the plain
                context, graded CANDIDATE only, per the brief.

Reproducible: python3 pool_1654/extract_pool.py from ciphers/thurloe-printed/,
against sources/ia-fulltext/collectionofstat03thur_djvu.txt (gitignored, restore
with: zcat sources/ia-fulltext/thurloe-gz/collectionofstat03thur_djvu.txt.gz >
sources/ia-fulltext/collectionofstat03thur_djvu.txt). Deterministic, no randomness.
"""
import csv
import filecmp
import os
import re
import shutil
import sys
import tempfile

DJVU = '../../../sources/ia-fulltext/collectionofstat03thur_djvu.txt'
OUT_DIR = '.'
RUN_GAP = 3  # lines of pure-plain gap allowed before a new cipher "run" starts

TOKEN = re.compile(r'\b[0-9OoIiLl]{1,4}[.,;:]?')
DIGIT_SUBST = str.maketrans({'i': '1', 'I': '1', 'l': '1', 'L': '1', 'o': '0', 'O': '0'})
NUM_LINE = re.compile(r'^\d{1,4}[.,;:]?$')


def clean_token(tok):
    core = tok.rstrip('.,;:')
    trail = tok[len(core):]
    normalized = core.translate(DIGIT_SUBST)
    if normalized.isdigit() and 1 <= len(normalized) <= 4:
        return normalized, trail, False
    return normalized, trail, True  # doubtful


MARGIN_WORDS = {'vol', 'p', 'p-', 'pag', 'a.d', 'ad', 'iii', 'xxiv',
                 'state', 'papers', 'john', 'thurloe', 'esq', 'esq^'}


def is_marginal_noise(core, words, pos):
    """Filter Birch's running-head marginalia (volume/page/year stamps) that
    OCR merges inline with body text on plain lines -- e.g. 'A.D. 1654.' or
    'Vol. xxiv. p. 76.'. Real cipher values in this system run 2-43 with a
    few 3-digit outliers (130/143/81, per the brief); a bare 4-digit 16xx
    token, or one sitting next to a volume/page marker word, is a running
    head, not a cipher group."""
    if len(core) == 4 and core.isdigit() and core.startswith('16'):
        return True
    prev_w = words[pos - 1].lower().rstrip('.,;:-') if pos > 0 else ''
    next_w = words[pos + 1].lower().rstrip('.,;:-') if pos + 1 < len(words) else ''
    if prev_w in MARGIN_WORDS or next_w in MARGIN_WORDS:
        return True
    return False


def is_cipher_line(line):
    tk = line.split()
    if len(tk) < 4:
        return False
    return sum(1 for t in tk if NUM_LINE.match(t)) / len(tk) >= 0.7


# Verified letter boundaries (heading line .. signature/postscript-end line),
# hand-checked against the djvu text this pass (section 12 of NOTES.md has the
# line-by-line evidence). 1-indexed, inclusive.
LETTERS = {
    'P4': dict(
        label='W.S. (Calais) to [Thurloe?], 13 March 1654 N.S.',
        heading_line=15467, heading_text='A letter of W. S. from Calais.',
        start=15467, end=15648,
        printed_page='76 (Vol. xxiv)',
        decipherment=None,
    ),
    'P5_P6': dict(
        label='W. Stamford (Calais) to [Thurloe?], 30 March 1654 N.S. -- one letter, was split P5/P6',
        heading_line=22884, heading_text='A letter of intelligence.',
        start=22884, end=23063,
        printed_page='319 (Vol. xxiv), cipher para; decipherment marginal p.324',
        decipherment=(23065, 23144),
    ),
    'P7': dict(
        label='"S." (Calais, same hand) to [Thurloe?], 20 March 1654',
        heading_line=23230, heading_text='A letter of intelligence, [March 20, 1654.]',
        start=23230, end=23348,
        printed_page='340 (Vol. xxiv), cipher para; decipherment marginal p.337',
        decipherment=(23349, 23422),
    ),
}


def load_lines():
    with open(DJVU, encoding='utf-8', errors='ignore') as f:
        return f.read().split('\n')


def word_context(lines, idx0, tok_start, tok_end, line_tokens_pos):
    """prev/next clear word on the same line, else from adjacent non-blank lines."""
    line = lines[idx0]
    words = line.split()
    # crude: find position of this token among split() tokens
    pos = line_tokens_pos
    prev_word = words[pos - 1] if pos > 0 else None
    next_word = words[pos + 1] if pos + 1 < len(words) else None
    return prev_word, next_word


def extract_tokens(letter_id, lines, start, end):
    rows = []
    for lineno in range(start, end + 1):
        idx0 = lineno - 1
        if idx0 < 0 or idx0 >= len(lines):
            continue
        raw_line = lines[idx0].strip()
        if not raw_line:
            continue
        cipher_line = is_cipher_line(raw_line)
        words = raw_line.split()
        for pos, w in enumerate(words):
            m = re.match(r'^[0-9OoIiLl]{1,4}[.,;:]?$', w)
            if not m:
                continue
            core = w.rstrip('.,;:')
            has_real_digit = any(c.isdigit() for c in core)
            # On a PLAIN (non-cipher) line, only count tokens with an actual
            # digit character -- a lone letter-only token (I, O, l, Il, ...)
            # on a plain line is almost always the word "I"/"O", not a cipher
            # group; that ambiguity only resolves in the cipher line's own
            # favour (thurloe_extract.py's CLEANED convention).
            if not cipher_line and not has_real_digit:
                continue
            if not cipher_line and is_marginal_noise(core, words, pos):
                continue
            cleaned, trail, doubtful = clean_token(w)
            prev_word = words[pos - 1] if pos > 0 else ''
            next_word = words[pos + 1] if pos + 1 < len(words) else ''
            rows.append(dict(
                letter=letter_id, djvu_line=lineno, raw=w,
                cleaned=cleaned + trail, doubtful='yes' if doubtful else 'no',
                prev_word=prev_word, next_word=next_word,
                line_is_cipher='yes' if is_cipher_line(raw_line) else 'no',
            ))
    return rows


def build_runs(token_rows, gap):
    """Cluster tokens by djvu_line into runs allowing `gap` lines of no-token lines."""
    lines_with_tokens = sorted(set(r['djvu_line'] for r in token_rows))
    runs = []
    cur = None
    for ln in lines_with_tokens:
        if cur is None:
            cur = [ln, ln]
        elif ln - cur[1] <= gap:
            cur[1] = ln
        else:
            runs.append(tuple(cur))
            cur = [ln, ln]
    if cur is not None:
        runs.append(tuple(cur))
    return runs


def plain_context(lines, lo, hi, n=2):
    before = []
    i = lo - 2
    while i >= 0 and len(before) < n:
        s = lines[i].strip()
        if s:
            before.append(s)
        i -= 1
    before.reverse()
    after = []
    i = hi
    while i < len(lines) and len(after) < n:
        s = lines[i].strip()
        if s:
            after.append(s)
        i += 1
    return ' / '.join(before), ' / '.join(after)


def decipherment_text(lines, span):
    if span is None:
        return None
    lo, hi = span
    out = []
    for i in range(lo - 1, hi):
        s = lines[i].strip()
        if s:
            out.append(s)
    return ' '.join(out)


def main():
    check = '--check' in sys.argv
    global OUT_DIR
    if check:
        real_out = OUT_DIR
        OUT_DIR = tempfile.mkdtemp()
    lines = load_lines()
    all_tokens = []
    crib_rows = []
    for letter_id, meta in LETTERS.items():
        toks = extract_tokens(letter_id, lines, meta['start'], meta['end'])
        all_tokens.extend(toks)
        runs = build_runs(toks, RUN_GAP)
        deciph = decipherment_text(lines, meta['decipherment']) if meta['decipherment'] else None
        for lo, hi in runs:
            before, after = plain_context(lines, lo, hi)
            n_tok = sum(1 for t in toks if lo <= t['djvu_line'] <= hi)
            if deciph is not None:
                expected = deciph
                grade = 'FOUND (Birch prints "The fame letter decypherd" for this whole letter; ' \
                        'not a per-run alignment, the full paragraph is given once per letter)'
            else:
                expected = before + ' [[RUN]] ' + after
                grade = 'CANDIDATE (this pass\'s own reading of surrounding plain text, not verified)'
            crib_rows.append(dict(
                letter=letter_id, run_lines='%d-%d' % (lo, hi), n_tokens=n_tok,
                context_before=before, context_after=after,
                expected_content=expected if deciph is None else '(see decipherment_P5_P6.txt / decipherment_P7.txt)',
                grade=grade,
            ))
    tok_path = os.path.join(OUT_DIR, 'tokens.tsv')
    with open(tok_path, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['letter', 'djvu_line', 'raw', 'cleaned', 'doubtful',
                                           'prev_word', 'next_word', 'line_is_cipher'], delimiter='\t')
        w.writeheader()
        for r in all_tokens:
            w.writerow(r)

    crib_path = os.path.join(OUT_DIR, 'cribs.tsv')
    with open(crib_path, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['letter', 'run_lines', 'n_tokens', 'context_before',
                                           'context_after', 'expected_content', 'grade'], delimiter='\t')
        w.writeheader()
        for r in crib_rows:
            w.writerow(r)

    # Full decipherment texts, saved verbatim for the two found-solved letters.
    for letter_id in ('P5_P6', 'P7'):
        span = LETTERS[letter_id]['decipherment']
        if span is None:
            continue
        text = decipherment_text(lines, span)
        with open(os.path.join(OUT_DIR, 'decipherment_%s.txt' % letter_id), 'w', encoding='utf-8') as f:
            f.write('# Birch 1742, "The fame letter decypherd" (OCR verbatim, djvu lines %d-%d)\n' % span)
            f.write(text + '\n')

    if check:
        stale = False
        for fname in ['tokens.tsv', 'cribs.tsv', 'decipherment_P5_P6.txt', 'decipherment_P7.txt']:
            a, b = os.path.join(OUT_DIR, fname), os.path.join(real_out, fname)
            if not os.path.exists(b) or not filecmp.cmp(a, b, shallow=False):
                print('STALE: %s differs from regenerated output' % fname)
                stale = True
        shutil.rmtree(OUT_DIR)
        if stale:
            sys.exit(1)
        print('OK: tokens.tsv, cribs.tsv, decipherment_*.txt match regeneration')
        return

    print('tokens: %d rows -> %s' % (len(all_tokens), tok_path))
    print('cribs: %d runs -> %s' % (len(crib_rows), crib_path))
    for letter_id in LETTERS:
        n = sum(1 for t in all_tokens if t['letter'] == letter_id)
        print('  %s: %d tokens' % (letter_id, n))


if __name__ == '__main__':
    main()
