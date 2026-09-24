#!/usr/bin/env python3
"""Extract QUEUE.md row W1 (Gustav II Adolf to Axel Oxenstierna, Nurnberg 23 July 1632,
Rikskansleren Axel Oxenstiernas skrifter och brefvexling, letter no. 602, pp. 821-822) into
printed_ocr.txt, ciphertext.txt and tokens.tsv.

Extraction only -- no decoding, no repair, no key applied (CLAUDE.md layout rule, and this
worker's brief). Reads the cached djvu text at sources/ia-fulltext/rikskanslerenax00styfgoog_djvu.txt
(gitignored; re-fetch with:
    curl -sS -L -A "cipher-lab research script (contact via repository)" \
        https://archive.org/download/rikskanslerenax00styfgoog/rikskanslerenax00styfgoog_djvu.txt \
        -o sources/ia-fulltext/rikskanslerenax00styfgoog_djvu.txt
), djvu-text line numbers 39871-39947 for the letter body (the page-break marker "822" at line
39896 and the footnote definition at lines 39890-39893 are printed apparatus, extracted
separately, not letter-body tokens).

A token is classified CIPHER only if it is already, before any substitution, a 1-4 digit run
with optional trailing punctuation (tools/thurloe_extract.py's convention: NUM = ^\\d{1,4}[.,;:]?$
tested on the RAW token); the OCR digit-lookalike substitution (l/i -> 1, o -> 0) is then applied
only to already-numeric-looking tokens, per ciphers/orange-nassau-1572/decode.py's convention. A
short isolated letter-run (<=2 chars, no vowel, not a standalone Swedish/German word: r, rr, nn,
mm, W, ee, ...) interspersed among numeral groups is kept as a CLEAR token verbatim (never
reclassified as cipher by inference) but flagged with a doubt note -- it reads as part of the
cipher's own symbol set on the page, not as a transcription artifact, but that is for a solver to
confirm against the image, not decided here.

    python3 ciphers/oxenstierna-gustav-adolf-1632/extract.py

Reproducible: re-running against the same cached djvu text regenerates byte-identical output.
"""
import re

DJVU = "sources/ia-fulltext/rikskanslerenax00styfgoog_djvu.txt"
OUT_DIR = "ciphers/oxenstierna-gustav-adolf-1632"

LETTER_START = 39871  # "602*).  Nurnberg  den  23  JuU  1682."
LETTER_END = 39947    # "gen.     Aff  lagret  vidh  Niirenberg  den  23  Julij,  Ahr  1632."
FOOTNOTE_LINES = range(39890, 39894)  # editor's footnote (quoted in NOTES.md), not letter body
PAGE_BREAK_LINES = {39896}           # bare printed page number "822"
# The letter-number/place/date heading and the closing dateline formula are printed apparatus in
# clear (the editor's numbering "602", the day-of-month and year), not cipher: excluded from the
# CIPHER/CLEAR token stream entirely and reported as their own [HEADING]/[DATELINE] lines so their
# digits are never counted as cipher tokens.
HEADING_LINE = 39871
DATELINE_TEXT = "Aff  lägret  vidh  Niirenberg  den  23  Julij,  Åhr  1632."
BODY_TAIL_ON_DATELINE_LINE = "gen."  # continuation of "nådeligen" from the previous line

NUM = re.compile(r'^\d{1,4}["′°*]?[.,;:]?$')
MERGED_NUM = re.compile(r'^\d{1,4}\.\d{1,4}\.?$')
DIGIT_SUBST = str.maketrans({'i': '1', 'I': '1', 'l': '1', 'L': '1', 'o': '0', 'O': '0'})
# Short letter-runs seen interspersed with the numeral groups in this letter: not reclassified
# as cipher (that would be inference), only flagged for a solver to check against the image.
SUSPECT_LETTER_RUN = re.compile(r'^(r|rr|nn|mm|w|ee|t)\.?$', re.IGNORECASE)


def clean_num_token(tok):
    core = tok.rstrip('.,;:"′°*')
    trail = tok[len(core):]
    normalized = core.translate(DIGIT_SUBST)
    doubt = ''
    if not normalized.isdigit() or not (1 <= len(normalized) <= 4):
        doubt = '[?]'
    if trail:
        doubt = doubt or ('[?]' if trail not in ('.', ',', ';', ':') else '')
    return normalized, doubt


def load_lines():
    with open(DJVU, encoding='utf-8', errors='replace') as fh:
        return fh.readlines()


def main():
    raw_lines = load_lines()
    ocr_out = []
    ct_out = []
    tokens = []
    pos = 0

    ocr_out.append(f"# Printed OCR excerpt, {DJVU}, lines {LETTER_START}-{LETTER_END}")
    ocr_out.append("# (letter body only; footnote and page-break lines shown separately below)")
    ocr_out.append("")

    footnote_text = ' '.join(
        raw_lines[i - 1].strip() for i in FOOTNOTE_LINES if 1 <= i <= len(raw_lines)
    )
    ocr_out.append(f"# [FOOTNOTE, L{FOOTNOTE_LINES.start}-L{FOOTNOTE_LINES.stop - 1}]: {footnote_text}")
    ocr_out.append("")

    ct_out.append('# Rikskansleren Axel Oxenstiernas skrifter och brefvexling (Styffe ed.),')
    ct_out.append('# letter no. 602, printed pp. 821-822')
    ct_out.append('# Sender: Gustav II Adolf (Gustavus Adolphus)')
    ct_out.append('# Recipient: Axel Oxenstierna ("her Cantzler")')
    ct_out.append('# Date: Nurnberg, 23 July 1632 ("Nurnberg den 23 JuU 1682" / "23 Julij, Ahr 1632" -- OCR digit slip 1682->1632)')
    ct_out.append('# Cipher system: unidentified nomenclator, 733 cipher tokens (91 distinct values, range 4-5152)')
    ct_out.append('# Prior work: none found (check-solved sweep, 24 Sept 2026, NOTES.md)')
    ct_out.append('#')
    ct_out.append('# As transcribed (OCR), never silently repaired. Source: Internet Archive')
    ct_out.append(f'# identifier rikskanslerenax00styfgoog, cached djvu text {DJVU}')
    ct_out.append(f'# (gitignored; re-fetch per extract.py docstring), djvu-text lines {LETTER_START}-{LETTER_END}.')
    ct_out.append('# Regenerate this file with: python3 ciphers/oxenstierna-gustav-adolf-1632/extract.py')
    ct_out.append('#')
    ct_out.append('# Format: one row per token, in reading order. CIPHER rows give RAW (OCR verbatim)')
    ct_out.append('# and CLEANED (l/i->1, o->0 OCR-digit-misread normalisation only, thurloe_extract.py\'s')
    ct_out.append('# convention); a token still not a clean 1-4 digit run after that gets a trailing')
    ct_out.append('# [?] -- doubtful, not fixed. CLEAR rows are clear-text tokens kept verbatim, OCR')
    ct_out.append('# errors and all (e.g. "8om" for "som", "tUl" for "till" -- not repaired here).')
    ct_out.append('# [?]SYM rows are short letter-runs (r, rr, nn, mm, W, ee) interspersed among the')
    ct_out.append('# numeral groups: kept as CLEAR (never reclassified as cipher by inference) but')
    ct_out.append('# flagged -- they read as part of the cipher\'s own symbol set on the page, to be')
    ct_out.append('# checked against the image by a solver, not decided in extraction.')
    ct_out.append('# [?]MERGED rows are two digit groups run together with no space (e.g. "26.24"):')
    ct_out.append('# kept as one CLEAR token verbatim, not split, since which split is right is not')
    ct_out.append('# decided here. [?]OCR rows are alphabetic tokens with a stray embedded digit')
    ct_out.append('# (e.g. "8om" for "som"): kept verbatim, not repaired, only flagged.')
    ct_out.append('#')
    ct_out.append('# ==========================================================================')

    n_cipher = 0
    n_clear = 0
    n_flagged = 0

    for lineno in range(LETTER_START, LETTER_END + 1):
        raw_line = raw_lines[lineno - 1].rstrip('\n')
        stripped = raw_line.strip()
        if not stripped:
            continue
        if lineno in PAGE_BREAK_LINES:
            ocr_out.append(f"L{lineno}\t[PAGE-BREAK: \"{stripped}\"]")
            continue
        if lineno in FOOTNOTE_LINES:
            ocr_out.append(f"L{lineno}\t[FOOTNOTE-TEXT: \"{stripped}\"]")
            continue
        if lineno == HEADING_LINE:
            ocr_out.append(f"L{lineno}\t[HEADING: \"{stripped}\"]")
            ct_out.append(f"# ---- L{lineno} ----")
            ct_out.append(f"L{lineno}\t[HEADING, not tokenised: \"{stripped}\"]")
            continue

        line_body = stripped
        dateline_note = None
        if lineno == LETTER_END:
            # split the body-continuation ("gen.") from the closing dateline formula
            line_body = BODY_TAIL_ON_DATELINE_LINE
            dateline_note = DATELINE_TEXT

        ocr_out.append(f"L{lineno}\tRAW: {stripped}")
        ct_out.append(f"# ---- L{lineno} ----")

        for tok in line_body.split():
            pos += 1
            core_test = tok.rstrip('.,;:"′°*')
            is_num = bool(NUM.match(tok))
            if is_num:
                cleaned, doubt = clean_num_token(tok)
                ct_out.append(f"L{lineno}\tCIPHER\tpos={pos}\tRAW={tok}\tCLEANED={cleaned}{doubt}")
                tokens.append((pos, lineno, 'CIPHER', tok, cleaned, doubt))
                n_cipher += 1
                if doubt:
                    n_flagged += 1
            else:
                doubt = ''
                if MERGED_NUM.match(tok):
                    # two cipher groups run together with no space, e.g. "26.24": neither
                    # split nor merged here -- flagged, not decided, per CLAUDE.md layout rule.
                    doubt = '[?]MERGED'
                elif SUSPECT_LETTER_RUN.match(core_test):
                    doubt = '[?]SYM'
                elif re.search(r'\d', tok) and re.search(r'[A-Za-zÀ-ÿ]', tok):
                    # a digit mixed into an otherwise alphabetic token: likely an OCR
                    # misread of a clear word (e.g. "8om" for "som") -- kept verbatim, flagged.
                    doubt = '[?]OCR'
                if doubt:
                    n_flagged += 1
                ct_out.append(f"L{lineno}\tCLEAR\tpos={pos}\t{tok}{doubt}")
                tokens.append((pos, lineno, 'CLEAR', tok, tok, doubt))
                n_clear += 1

        if dateline_note:
            ct_out.append(f"L{lineno}\t[DATELINE, not tokenised: \"{dateline_note}\"]")

    ct_header_note = (
        f"# {n_cipher} cipher-classified tokens, {n_clear} clear tokens, "
        f"{n_flagged} flagged [?] (doubtful digit run or suspect letter-run), "
        f"in this window.\n#"
    )
    ct_out.insert(21, ct_header_note)

    with open(f"{OUT_DIR}/printed_ocr.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(ocr_out) + "\n")

    with open(f"{OUT_DIR}/ciphertext.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(ct_out) + "\n")

    with open(f"{OUT_DIR}/tokens.tsv", "w", encoding="utf-8") as fh:
        fh.write("position\tline\tclass\traw\tnormalized\tdoubt\n")
        for p, ln, cls, raw, norm, doubt in tokens:
            fh.write(f"{p}\t{ln}\t{cls}\t{raw}\t{norm}\t{doubt}\n")

    print(f"tokens: {len(tokens)} ({n_cipher} cipher, {n_clear} clear, {n_flagged} flagged)")
    print(f"wrote {OUT_DIR}/printed_ocr.txt, {OUT_DIR}/ciphertext.txt, {OUT_DIR}/tokens.tsv")


if __name__ == "__main__":
    main()
