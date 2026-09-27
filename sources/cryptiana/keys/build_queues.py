#!/usr/bin/env python3
"""build_queues.py: triage every sources/cryptiana/web/*.htm page for a text key table versus an image key
table, per LANE CRYPT job brief U1b (2026-09-27, CRYPT-KEYS-A).

CRYPTO-INDEX.tsv's key_row_lines column is a weak signal on its own (the parent's 00:1x UTC check: spanish.htm,
which prints Puebla's Roman-numeral code as plain text, does not reach its own top 20 by that column, while most
of Tomokiyo's key tables are IMAGES -- about 1,650 <img> references across the 278 pages, 90 on henryiii.htm,
86 on nevers.htm). This script re-scores every page from four script-only signals -- tab-separated code/value
lines, <table> blocks, <pre> blocks, Roman-numeral tokens -- and separately lists every <img> tag with its own
heading/caption context, scored (never by a model) for whether it looks like a key table.

Usage: python3 sources/cryptiana/keys/build_queues.py

Writes:
  sources/cryptiana/keys/TEXT-QUEUE.tsv   page, score, tables, pre_blocks, tsv_lines, roman_lines
                                          sorted by score descending (the U2 reading order: NOT key_row_lines)
  sources/cryptiana/keys/IMAGE-QUEUE.tsv  page, image_src, alt, heading, caption, looks_like_key, office_match
                                          (CRYPT-KEYS-B's queue -- this job does not read images)

Scoring (script only, thresholds stated, not learned):
  TEXT-QUEUE score = 5*tsv_lines + 3*tables + 2*pre_blocks + 1*roman_lines
    tsv_lines:   lines matching CLAUDE.md's own regex, ^\\s*[A-Za-z0-9IVXLCDMivxlcdm\\[\\]]{1,10}\\t+\\S
                 (run against the page's own decoded text, not the html2text conversion -- a code table's
                 tabs are almost always inside a <pre> block, which both preserve verbatim)
    tables/pre_blocks: raw counts of <table and <pre opening tags
    roman_lines: lines containing a standalone token that parses as a Roman numeral (2+ characters, so a
                 lone "I" in running prose is not counted)
  IMAGE-QUEUE looks_like_key: yes if the image's alt text, nearest preceding heading (h1-h4) or the text
    line immediately after it contains any of: key, table, cipher, chiffre, cifra, code, nomenclat, alphabet,
    homophon, syllab (case-insensitive substring)
  IMAGE-QUEUE office_match: the ciphers/<folder> name(s) whose NOTES.md or KEY-OFFICES.tsv mentions one of
    this page's own CRYPTO-INDEX.tsv shelfmark tokens (";"-split, len>=3), by plain grep -- never a model.
"""
import csv
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent
WEB = ROOT / 'sources' / 'cryptiana' / 'web'
CIPHERS = ROOT / 'ciphers'
INDEX = ROOT / 'sources' / 'cryptiana' / 'CRYPTO-INDEX.tsv'
OUT_DIR = Path(__file__).resolve().parent
TOOLS = ROOT / 'tools'
sys.path.insert(0, str(TOOLS))
import html2text as h2t  # noqa: E402

TSV_LINE_RE = re.compile(r'^\s*[A-Za-z0-9IVXLCDMivxlcdm\[\]]{1,10}\t+\S')
ROMAN_TOKEN_RE = re.compile(
    r'\b(?=[IVXLCDMivxlcdm]{2,10}\b)M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\b', re.I)
KEY_WORDS = ('key', 'table', 'cipher', 'chiffre', 'cifra', 'code', 'nomenclat', 'alphabet', 'homophon', 'syllab')


def roman_line_count(text):
    n = 0
    for line in text.splitlines():
        for tok in line.split():
            tok = tok.strip('.,;:()[]"\'')
            if len(tok) >= 2 and ROMAN_TOKEN_RE.fullmatch(tok):
                n += 1
                break
    return n


class ImageScanner(HTMLParser):
    """Every <img> tag with its src/alt, the nearest preceding h1-h4 heading text, and the caption text
    (the first non-blank run of text data after the tag)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.heading = ''
        self._heading_buf = None
        self.images = []
        self._pending = None
        self._cap_parts = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('h1', 'h2', 'h3', 'h4'):
            self._heading_buf = []
        if tag == 'img':
            rec = {'src': a.get('src', ''), 'alt': a.get('alt', ''), 'heading': self.heading, 'caption': ''}
            self.images.append(rec)
            self._pending = rec
            self._cap_parts = []

    def handle_endtag(self, tag):
        if tag in ('h1', 'h2', 'h3', 'h4') and self._heading_buf is not None:
            self.heading = re.sub(r'\s+', ' ', ' '.join(self._heading_buf)).strip()
            self._heading_buf = None

    def handle_data(self, data):
        if self._heading_buf is not None:
            self._heading_buf.append(data)
        if self._pending is not None:
            t = re.sub(r'\s+', ' ', data).strip()
            if t:
                self._cap_parts.append(t)
                joined = ' '.join(self._cap_parts)
                self._pending['caption'] = joined[:200]
                if len(joined) > 60:
                    self._pending = None


def looks_like_key(rec):
    blob = f"{rec['alt']} {rec['heading']} {rec['caption']}".lower()
    return 'yes' if any(w in blob for w in KEY_WORDS) else 'no'


def load_index():
    rows = {}
    if INDEX.exists():
        with open(INDEX, encoding='utf-8') as f:
            for row in csv.DictReader(f, delimiter='\t'):
                rows[row['page']] = row
    return rows


def notes_and_offices_blob():
    """One lowercase blob per ciphers/<folder>: its NOTES.md text plus any KEY-OFFICES.tsv row naming it,
    for a plain substring office_match (script only, never a model)."""
    blobs = {}
    for notes in CIPHERS.glob('*/NOTES.md'):
        folder = notes.parent.name
        try:
            blobs[folder] = notes.read_text(encoding='utf-8', errors='replace').lower()
        except Exception:
            blobs[folder] = ''
    offices = ROOT / 'KEY-OFFICES.tsv'
    if offices.exists():
        for line in offices.read_text(encoding='utf-8', errors='replace').splitlines()[1:]:
            cells = line.split('\t')
            if not cells or not cells[0].startswith('ciphers/'):
                continue
            folder = cells[0].split('/')[1]
            blobs[folder] = blobs.get(folder, '') + ' ' + line.lower()
    return blobs


def office_match(shelfmarks, blobs):
    # a bare archive abbreviation ('bnf', 'tna', 'Cotton', 'Add MS' with no number) matches almost every
    # ciphers/ folder that cites the same big archive and is not a real shelfmark match -- require a digit
    # (found by hand: without this, 1315 of 1952 image rows "matched", nearly the whole queue; 'fr.3995',
    # 'SP53', 'Add MS 12345' keep matching, 'bnf'/'tna'/'kha'/'Cotton' alone stop).
    tokens = [t.strip().lower() for t in (shelfmarks or '').split(';')
              if len(t.strip()) >= 3 and any(c.isdigit() for c in t)]
    if not tokens:
        return ''
    hits = [folder for folder, blob in blobs.items() if any(tok in blob for tok in tokens)]
    return ','.join(sorted(hits))


def main():
    index = load_index()
    blobs = notes_and_offices_blob()
    text_rows, image_rows = [], []
    pages = sorted(p.name for p in WEB.glob('*.htm'))
    for page in pages:
        path = WEB / page
        try:
            raw_text = h2t.read(path)  # decoded (Shift_JIS/UTF-8), tags still present
        except Exception:
            continue
        tables = len(re.findall(r'<table', raw_text, re.I))
        pre_blocks = len(re.findall(r'<pre', raw_text, re.I))
        tsv_lines = sum(1 for l in raw_text.splitlines() if TSV_LINE_RE.match(l))
        roman_lines = roman_line_count(raw_text)
        score = 5 * tsv_lines + 3 * tables + 2 * pre_blocks + 1 * roman_lines
        text_rows.append(dict(page=page, score=score, tables=tables, pre_blocks=pre_blocks,
                               tsv_lines=tsv_lines, roman_lines=roman_lines))

        scanner = ImageScanner()
        try:
            scanner.feed(raw_text)
        except Exception:
            pass
        shelfmarks = index.get(page, {}).get('shelfmarks', '')
        om = office_match(shelfmarks, blobs)
        for rec in scanner.images:
            image_rows.append(dict(page=page, image_src=rec['src'], alt=rec['alt'], heading=rec['heading'],
                                    caption=rec['caption'], looks_like_key=looks_like_key(rec),
                                    office_match=om))

    text_rows.sort(key=lambda r: (-r['score'], r['page']))
    image_rows.sort(key=lambda r: (r['office_match'] == '', r['looks_like_key'] != 'yes', r['page']))

    text_cols = ['page', 'score', 'tables', 'pre_blocks', 'tsv_lines', 'roman_lines']
    with open(OUT_DIR / 'TEXT-QUEUE.tsv', 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(text_cols)
        for r in text_rows:
            w.writerow([r[c] for c in text_cols])

    image_cols = ['page', 'image_src', 'alt', 'heading', 'caption', 'looks_like_key', 'office_match']
    with open(OUT_DIR / 'IMAGE-QUEUE.tsv', 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(image_cols)
        for r in image_rows:
            w.writerow([r[c] for c in image_cols])

    n_text_table_pages = sum(1 for r in text_rows if r['score'] > 0)
    n_image_rows = len(image_rows)
    n_looks_like_key = sum(1 for r in image_rows if r['looks_like_key'] == 'yes')
    n_office_match = sum(1 for r in image_rows if r['office_match'])
    print(f'pages scanned: {len(text_rows)}')
    print(f'text-table pages (score>0): {n_text_table_pages}')
    print(f'image rows: {n_image_rows}')
    print(f'image rows looks_like_key=yes: {n_looks_like_key}')
    print(f'image rows with office_match: {n_office_match}')
    print('top 10 TEXT-QUEUE pages: ' + ', '.join(f"{r['page']}({r['score']})" for r in text_rows[:10]))


if __name__ == '__main__':
    main()
