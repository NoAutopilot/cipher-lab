#!/usr/bin/env python3
"""decipher_sheet.py -- key sheets and reading sheets rendered from a target folder's own graded data (MQS-SHEETS, 9 Oct 2026).

  python3 tools/decipher_sheet.py key ciphers/<t> [--config CONFIG] [--job NAME] [--tiles boxes|lines|none|auto]
        [--variants 3] [--mi-panel] --out DIR/STEM-key.html [--png] [--pdf] [--check] [--tile-report TSV]
  python3 tools/decipher_sheet.py reading ciphers/<t> [--config CONFIG] --job NAME [--lines L01-L12]
        [--highlight CODE[,CODE]] [--annotate notes.tsv] --out DIR/STEM-reading.html [--png] [--pdf] [--check]

Layout after Lasry, Biermann and Tomokiyo 2023, Figs 5-14 and B24 (pp.112-127, 200), DESCRIBED, never copied (the paper is
CC BY-NC-ND): a key table (A-Z homophone header, a code under its letter with exemplar glyphs, the code, its count n and
grade) and an interlinear reading (line crop, token row, value row, edited text). Glyphs are always cut from the manuscript
images on disk (committed, no network), never from anyone's drawn table.

Loads the config, key, exceptions and grades through tools/decode_key.py's own functions (it parses no key format itself).
Tiles, in this order per line: (a) per-sign boxes (--atlas DIR with signs.tsv + pages.json, --box-map TSV with columns
sid,line,pos[,op] e.g. Birago's atlas/no87_box_token.tsv); (b) line crops with a known token order (--line-images TSV:
line,image[,x0,y0,x1,y1]; the sheet then says "token row not aligned to the image"); (c) none (codes in monospace).
--tokens-tsv FILE (columns line,pos,sign,value,grade[,gloss]) stands in for a decode config where a target has none
(a word-code ledger such as Eckert's); --key-tsv FILE the key for it. --exemplar-tsv FILE (code,image[,x0,y0,x1,y1]) lists
exemplar crops for a key sheet whose target has no box map.

Key exemplars: for each code with >= 2 secure boxes (grade H/C/S) glyph_atlas.pick_spread (medoid, then farthest point,
after trimming the farthest 0.2) picks --variants tiles, the same selection as `glyph_atlas.py atlas --from-truth ... --spread`
(imported, not re-implemented). --mi-panel: each M/I-graded boxed token beside its three nearest S-graded exemplars,
PROMOTED from ciphers/moray-wood-1568/no804/refsheet/build_refsheet.py (RUN1-MOR, 4 Oct 2026; transcription labels there are
Aymeloglu's, cited, no code copied from unsolved-ciphers). Similarity is Dice overlap of 32x32 binarised ink masks, best of
+-2 px shifts, kept over glyph_atlas.classify's HOG features because the Moray crops are not on disk to test the latter on
and RUN4-MOR measured Dice at leave-one-out top-1 0.513 against a label-shuffle p99 of 0.128; one metric only. It is a script
ranking for a person looking at the glyphs, not a reading; no grade changes.

Grades by form first, colour second (palette cvd_check.PALETTES['sheets_light'], checked in the test): H and C bold capitals
with a superscript letter; S capitals with a solid blue underline; M lower case, dashed dark-orange underline, trailing '?';
I lower-case italic in [brackets], dotted ink underline; U <code> in grey monospace; NULL a middle dot. No red, no green.

Output: one self-contained HTML (tiles as JPEG data URIs, quality 70, at most 3 MB; a warning above that), PNG/PDF through
tools/browser_fetch.js. Each HTML embeds a sha256 of every input; --check re-renders and exits 1 when stale (rule 7); the render
time and commit in the footer are volatile and ignored by --check. --tile-report TSV: per tile, crop non-empty, ink share inside
[INK_LO, INK_HI] (pre-registered in tools/tests/PREREG-MQS-SHEETS.md G4), and label/value agreement; used by A2's K3.
Refuses a folder carrying RESTRICTED.md and any path under restricted/, and any target whose key family has an open blind sort
in tools/data/sorter_families.tsv (open_blind_sorts non-empty; TRANSCRIPTION.md blind first, MQS-SHEET-REFUSAL 9 Oct 2026): the
family is --key-family, else KEY_FAMILY_TARGETS by folder, else the folder holding a key path the job uses. --families TSV reads
another register (tests). Must catch: the Birago 1572 family (ASKS 118). Must NOT block: Gramont, Danzay (no open sort).

Scope (Usage 8a). Meant to catch: a sheet built from a tile map that places an image at the wrong box (R-K1/KM tests), a stale
sheet after a key edit (--check), a blank crop (--tile-report). Must NOT flag: a sheet with no swap record (no "or vice versa"
brace is ever drawn from a key_conflicts-style count file); a target with no boxes (tiles fall back to lines or none, with the
"not aligned" notice). Tests: tools/tests/test_decipher_sheet.py (offline).
"""
import argparse, base64, collections, csv, datetime, hashlib, html, io, json, os, re, subprocess, sys, types

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import decode_key, cvd_check

PAL = cvd_check.PALETTES['sheets_light']
INK, BLUE, ORANGE, GREY = PAL['marks']
BG = PAL['bg']
DARK = cvd_check.PALETTES['dark']
INK_LO, INK_HI = 0.02, 0.65       # K3 programmatic floor and ceiling (PREREG-MQS-SHEETS G4)
MIN_TILE_PX = 8
MAX_BYTES = 3 * 1024 * 1024
LAYOUT_CREDIT = 'Layout after Lasry, Biermann and Tomokiyo 2023, Figs 12-14 (pp.125-127); no figure reproduced.'

# grade -> non-colour properties (tuple order is the property set that must differ between every pair of grades)
GRADE_FORMS = {
    'H': dict(case='upper', weight='bold', style='normal', ul='none', wrap='', suffix='', sup='H', mono=False),
    'C': dict(case='upper', weight='bold', style='normal', ul='none', wrap='', suffix='', sup='C', mono=False),
    'S': dict(case='upper', weight='normal', style='normal', ul='solid', wrap='', suffix='', sup='', mono=False),
    'M': dict(case='lower', weight='normal', style='normal', ul='dashed', wrap='', suffix='?', sup='', mono=False),
    'I': dict(case='lower', weight='normal', style='italic', ul='dotted', wrap='[]', suffix='', sup='', mono=False),
    'U': dict(case='asis', weight='normal', style='normal', ul='none', wrap='<>', suffix='', sup='', mono=True),
    'NULL': dict(case='asis', weight='normal', style='normal', ul='none', wrap='', suffix='', sup='', mono=False, dot=True),
}
COLOUR = {'H': INK, 'C': INK, 'S': INK, 'M': INK, 'I': INK, 'U': GREY, 'NULL': GREY}
UL_COLOUR = {'solid': BLUE, 'dashed': ORANGE, 'dotted': INK, 'none': 'transparent'}

FOOTERS = {  # whose key, per target (brief, Unit 3 Footer)
    'fr2980-gramont': dict(key='Key: published by S. Tomokiyo and G. Lasry (Gramont 1530 key), page https://www.cryptiana.web.fc2.com/ (Tomokiyo, cryptiana)',
                           img='Source gallica.bnf.fr / BnF, ark:/12148/btv1b9059991d'),
    'fr20140-danzay-1557': dict(key="Key: S. Tomokiyo's 2026 reconstruction (danzay.htm, first posted 22 Feb 2026)",
                                img='Source gallica.bnf.fr / BnF, ark:/12148/btv1b52521512h'),
    'nevers-birago-fr3251-1572': dict(key="Key: Tomokiyo's Nevers-Birago 1572 table (nevers.htm)",
                                      img='Source gallica.bnf.fr / BnF, ark:/12148/btv1b9060248g'),
    'eckert-1864': dict(key='Key: the cipher book (Huntington mssEC 41), as used in the ledger mssEC 19',
                        img='Thomas T. Eckert Papers, mssEC 19, The Huntington Library, San Marino, California; '
                            'rights statement: ciphers/eckert-1864/images/README.md "Rights"'),
}
FAMILIES = os.path.join(ROOT, 'tools', 'data', 'sorter_families.tsv')
KEY_FAMILY_TARGETS = {  # sorter family -> target folders keyed in it (birago-nevers-1571 is the Nov 1571 numerical key: not here)
    'nevers-birago-1572': ('nevers-birago-fr3251-1572', 'birago-fr3252-1571-72'),
}
FUNCTION_WORDS = set('de la le les et que qui du des en un une a au aux ne se ce il elle sa son ses par pour sur avec the and of to in is that'.split())
TITLE_WORDS = set('roy roi reyne reine monsieur madame seigneur duc comte cardinal pape prince king queen lord duke earl'.split())


# ---------------------------------------------------------------- data

def refuse_restricted(target):
    t = os.path.abspath(target)
    if os.path.exists(os.path.join(t, 'RESTRICTED.md')) or 'restricted' in t.split(os.sep):
        raise SystemExit(f'decipher_sheet: {target} is restricted material (RESTRICTED.md or a restricted/ path); refused')


def key_family(target, key_paths=(), explicit=None):
    if explicit:
        return explicit
    dirs = {os.path.basename(os.path.abspath(target))} | {os.path.basename(os.path.dirname(os.path.abspath(k))) for k in key_paths}
    return next((f for f, ts in KEY_FAMILY_TARGETS.items() if dirs & set(ts)), None)

def refuse_open_sort(target, key_paths=(), explicit=None, fam_path=None):
    fam = key_family(target, key_paths, explicit)
    if not fam:
        return
    with open(fam_path or FAMILIES, encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r.get('family') == fam and (r.get('open_blind_sorts') or '').strip():
                raise SystemExit(f'decipher_sheet: key family {fam!r} has open blind sorts ({r["open_blind_sorts"].strip()}) in '
                                 f'tools/data/sorter_families.tsv; no key or reading sheet until they are landed (TRANSCRIPTION.md, '
                                 f'blind first); refused')

def select_job(jobs, name):
    if not name:
        if len(jobs) == 1:
            return jobs[0]
        raise SystemExit('decipher_sheet: this config has several jobs; give --job NAME (a substring of the ciphertext, reading or "name")')
    hit = [j for j in jobs if name in ' '.join(str(j.get(k, '')) for k in ('name', 'ciphertext', 'reading', 'tokens'))]
    if len(hit) != 1:
        raise SystemExit(f'decipher_sheet: --job {name!r} matches {len(hit)} jobs')
    return hit[0]


def graded(target, job):
    """The graded token records of one decode job -- decode_key's own loaders and grader, as run_job does."""
    ct = job.get('ciphertext') or next((f for f in ('ciphertext.tsv', 'ciphertext.txt')
                                        if os.path.exists(os.path.join(target, f))), 'ciphertext.tsv')
    path = os.path.join(target, ct)
    recs = decode_key.LOADERS[job.get('format') or decode_key.detect_format(path)](path, job)
    key = decode_key.load_keys(target, job.get('key', 'key.tsv'))
    exc = decode_key.load_exceptions(os.path.join(target, job.get('exceptions', 'exceptions.tsv')), job)
    decode_key.grade_tokens(recs, key, exc, decode_key.load_votes(target, job), job)
    return recs, key, ct


def load_tsv(path):
    rows = [l.rstrip('\n').split('\t') for l in open(path, encoding='utf-8') if l.strip() and not l.startswith('#')]
    h = rows[0]
    return [dict(zip(h, r)) for r in rows[1:]]


def tokens_from_tsv(path, key_path=None):
    """--tokens-tsv: line,pos,sign,value,grade[,gloss] -> records shaped like decode_key's graded ones."""
    recs, seen = [], set()
    for r in load_tsv(path):
        ln = r['line']
        if ln not in seen:
            seen.add(ln); recs.append(dict(folio='', line=ln, label=ln, pos=None, kind='line'))
        g = r['grade']
        recs.append(dict(folio='', line=ln, label=ln, pos=int(r['pos']), raw=r['sign'], sign=r['sign'], conf='', gloss=r.get('gloss', ''),
                         kind='clear' if g == 'clear' else 'sign', value=r['value'], grade=g, null=r['value'] in ('NULL', 'null')))
    key = {}
    if key_path:
        for r in load_tsv(key_path):
            key[r.get('code') or r.get('sign')] = dict(value=r['value'], grade=r.get('grade', ''), source=r.get('source', ''), note=r.get('note', ''))
    return recs, key


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()


def status_result(doc_substr):
    if not doc_substr:
        return None
    st = json.load(open(os.path.join(ROOT, 'status.json'), encoding='utf-8'))
    hits = [r for r in st['results'] if doc_substr in (r.get('document_id', '') + ' ' + r.get('title', ''))]
    return hits[0] if hits else None


def depth_words(r):
    """Rule 4a outward words from a status.json result (None for D0 or missing: no reading sheet at D0)."""
    d, pct = (r or {}).get('depth'), (r or {}).get('depth_pct')
    try:
        pct = round(float(pct))
    except (TypeError, ValueError):
        pct = None
    if d == 'D1':
        w = 'fragments read'
    elif d == 'D2':
        w = f'partially deciphered (about {pct}%)' if pct is not None else 'partially deciphered'
    elif d == 'D3':
        w = f'largely deciphered (about {pct}%)' if pct is not None else 'largely deciphered'
    elif d == 'D4':
        w = 'deciphered'
        un = (r.get('depth_unread') or {})
        un = un if isinstance(un, dict) else {}
        try:
            n = int(un.get('names_codes', 0))
        except (TypeError, ValueError):
            n = 0
        if n:
            w += f'; {n} name codes unidentified'
    else:
        return None
    if r.get('key') in ('period', 'published'):
        w += f'; key identified ({r["key"]})'
    return w


# ---------------------------------------------------------------- grade forms

def form_signature(g):
    f = GRADE_FORMS[g]
    return tuple((k, f.get(k)) for k in ('case', 'weight', 'style', 'ul', 'wrap', 'suffix', 'sup', 'mono', 'dot'))


def token_text(value, grade, null=False, code=''):
    """(display string, grade key) following the declared form of the grade."""
    if null:
        return '·', 'NULL'
    g = grade if grade in GRADE_FORMS else 'M'
    f = GRADE_FORMS[g]
    if g == 'U':
        return '<' + (code or value) + '>', g
    v = value.lstrip('=')
    v = v.upper() if f['case'] == 'upper' else v.lower()
    if f['wrap']:
        v = f['wrap'][0] + v + f['wrap'][1]
    return v + f['suffix'], g


def token_html(value, grade, null=False, code='', hl=None):
    s, g = token_text(value, grade, null, code)
    f = GRADE_FORMS[g]
    sup = f'<sup>{f["sup"]}</sup>' if f['sup'] else ''
    cls = f'g{g}' + (' hl hl%d' % hl[0] if hl else '')
    badge = f'<b class="bd">{hl[1]}</b>' if hl else ''
    return f'<span class="{cls}">{html.escape(s)}{sup}{badge}</span>'


# ---------------------------------------------------------------- images

def _np():
    import numpy as np
    return np


def tile_stats(img):
    """Programmatic tile check: size, non-empty, ink share (fraction darker than the crop's Otsu threshold)."""
    import cv2
    np = _np()
    a = np.array(img.convert('L'))
    h, w = a.shape[:2]
    if h < MIN_TILE_PX or w < MIN_TILE_PX:
        return dict(w=w, h=h, nonempty=False, ink=0.0, ink_ok=False)
    if a.max() == a.min():
        return dict(w=w, h=h, nonempty=False, ink=0.0, ink_ok=False)
    t, _ = cv2.threshold(a, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    ink = float((a < t).mean())
    return dict(w=w, h=h, nonempty=True, ink=ink, ink_ok=INK_LO <= ink <= INK_HI)


def data_uri(img, height=None, quality=70):
    from PIL import Image
    im = img.convert('L')
    if height and im.height != height:
        im = im.resize((max(1, round(im.width * height / im.height)), height), Image.LANCZOS)
    b = io.BytesIO()
    im.save(b, 'JPEG', quality=quality)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()


class Boxes:
    """Per-sign boxes: atlas dir (signs.tsv, pages.json, bitmaps.npz) + a box-to-token map."""

    def __init__(self, atlas, box_map):
        import glyph_atlas
        self.ga, self.atlas = glyph_atlas, atlas
        self.signs = {r['sid']: r for r in glyph_atlas.read(atlas, 'signs.tsv')}
        self.order = [r['sid'] for r in glyph_atlas.read(atlas, 'signs.tsv')]
        self.cache = {}
        self.by_tok = collections.defaultdict(list)       # (line label, pos) -> [(sid, op)]
        self.rows = load_tsv(box_map)
        for r in self.rows:
            self.by_tok[(r['line'], int(r['pos']))].append((r['sid'], r.get('op', '1:1')))

    def grey(self, page):
        return self.ga._page_grey(self.atlas, page, self.cache)

    def cut(self, sids, scale_h=None):
        """PIL tile around one box (or the union of two) with glyph_atlas._tile's margins (marks above are kept)."""
        from PIL import Image
        rs = [self.signs[s] for s in sids]
        g = self.grey(rs[0]['page'])
        x0 = min(int(r['x']) for r in rs); y0 = min(int(r['y']) for r in rs)
        x1 = max(int(r['x']) + int(r['w']) for r in rs); y1 = max(int(r['y']) + int(r['h']) for r in rs)
        w, h = x1 - x0, y1 - y0
        m, top = int(0.2 * max(w, h)), int(0.6 * max(w, h))
        return Image.fromarray(g[max(0, y0 - top):y1 + m, max(0, x0 - m):x1 + m])

    def token_box(self, rec):
        return self.by_tok.get((f"{rec['folio']}_{rec['line']}" if rec['folio'] else rec['line'], rec['pos'])) or \
            self.by_tok.get((rec['line'], rec['pos']))


def exemplar_ids(atlas, by_code, per, trim=0.2, min_secure=2):
    """The key sheet's exemplar picker: exactly glyph_atlas `atlas --from-truth ... --spread --trim` (cmd_atlas_truth), imported.
    by_code: {code: [sid, ...]} of securely read boxes. Returns {code: [sid, ...]} (fewer than min_secure -> none)."""
    import glyph_atlas as ga
    np = _np()
    signs = ga.read(atlas, 'signs.tsv')
    idx = {r['sid']: i for i, r in enumerate(signs)}
    bm = np.load(os.path.join(atlas, 'bitmaps.npz'))['signs']
    X = ga.feats(bm, signs, pca_scale='shared')
    out = {}
    for c, sids in by_code.items():
        ids = [idx[s] for s in sids if s in idx]
        if len(ids) >= min_secure:
            out[c] = [signs[ids[k]]['sid'] for k in ga.pick_spread(X[ids], per, True, trim)]
    return out


# --- promoted from ciphers/moray-wood-1568/no804/refsheet/build_refsheet.py (RUN1-MOR, 4 Oct 2026)
def ink_mask(im):
    from PIL import Image
    np = _np()
    a = np.array(im.convert('L')) < 150
    ys, xs = np.nonzero(a)
    if len(xs) == 0:
        return np.zeros((32, 32), bool)
    a = a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    h, w = a.shape
    s = max(h, w)
    sq = np.zeros((s, s), bool)
    sq[(s - h) // 2:(s - h) // 2 + h, (s - w) // 2:(s - w) // 2 + w] = a
    return np.array(Image.fromarray(sq.astype(np.uint8) * 255).resize((32, 32), Image.BILINEAR)) > 100


def dice(a, b):
    np = _np()
    best = 0.0
    for dy in range(-2, 3):
        for dx in range(-2, 3):
            bb = np.roll(np.roll(b, dy, 0), dx, 1)
            i, s = (a & bb).sum(), a.sum() + bb.sum()
            best = max(best, 2 * i / s if s else 0)
    return best


def nearest_s(mi_tile, s_tiles, k=3):
    """The k S-graded exemplars (id -> PIL) with the highest Dice to one M/I tile: [(dice, id)]."""
    m = ink_mask(mi_tile)
    return sorted(((dice(m, ink_mask(t)), i) for i, t in s_tiles.items()), reverse=True)[:k]


# ---------------------------------------------------------------- sheet building

CSS = f"""
:root{{--ink:{INK};--bg:{BG};--blue:{BLUE};--orange:{ORANGE};--grey:{GREY};--rule:#bbbbbb;--tint:#F0E442;--tint2:#56B4E9;--ontint:#24211c}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--ink:{DARK['marks'][0]};--bg:{DARK['bg']};--blue:{DARK['marks'][1]};--orange:{DARK['marks'][2]};--grey:#a9a39a;--rule:#4a4640;--ontint:#1b1916}}}}
:root[data-theme="dark"]{{--ink:{DARK['marks'][0]};--bg:{DARK['bg']};--blue:{DARK['marks'][1]};--orange:{DARK['marks'][2]};--grey:#a9a39a;--rule:#4a4640;--ontint:#1b1916}}
body{{background:var(--bg);color:var(--ink);font:15px/1.4 Georgia,serif;margin:0 auto;max-width:1100px;padding:16px}}
h1{{font-size:1.25rem;margin:.2em 0}} h2{{font-size:1.05rem;margin:1.2em 0 .3em;border-bottom:1px solid var(--rule)}}
.meta,.foot,.note{{font-size:.82rem;color:var(--ink)}} .foot{{border-top:1px solid var(--rule);margin-top:1.5em;padding-top:.6em}}
code,.mono{{font-family:ui-monospace,Menlo,monospace;font-size:.8rem}}
.gH,.gC{{font-weight:bold}} .gS{{text-decoration:underline solid var(--blue);text-decoration-thickness:2px;text-underline-offset:3px}}
.gM{{text-decoration:underline dashed var(--orange);text-decoration-thickness:2px;text-underline-offset:3px}}
.gI{{font-style:italic;text-decoration:underline dotted var(--ink);text-underline-offset:3px}}
.gU{{font-family:ui-monospace,Menlo,monospace;color:var(--grey)}} .gNULL{{color:var(--grey)}}
sup{{font-size:.6em}} .legend span{{margin-right:1em;white-space:nowrap}}
.letter{{display:inline-block;vertical-align:top;border:1px solid var(--rule);margin:3px;padding:3px 5px;min-width:90px}}
.letter>.L{{font-weight:bold;font-size:1.1rem}} .code{{display:block;margin:2px 0;border-top:1px dotted var(--rule);padding-top:2px}}
.code img{{height:44px;margin-right:2px;border:1px solid var(--rule);vertical-align:middle}}
.strip{{border:1px solid var(--rule);padding:4px;margin:6px 0}}
.line{{margin:8px 0;border-top:1px solid var(--rule);padding-top:4px}} .line img.crop{{max-width:100%;display:block}}
.row{{display:flex;flex-wrap:wrap;align-items:flex-end}} .tk{{text-align:center;margin:0 2px 4px;min-width:26px}}
.tk img{{height:40px;display:block;margin:0 auto 2px;border:1px solid var(--rule)}} .tk .c{{font-family:ui-monospace,Menlo,monospace;font-size:.68rem}}
.tk.x img{{border:1px dashed var(--ink)}} .tk .v{{font-size:1.05rem}}
.hl{{outline:2px solid var(--ink);outline-offset:1px}} .hl1{{outline-color:var(--blue)}} .hl2{{outline-color:var(--orange);outline-style:dashed}} .hl3{{outline-color:var(--ink);outline-style:dotted}}
.bd{{font:bold .6rem sans-serif;border:1px solid var(--ink);border-radius:8px;padding:0 3px;margin-left:2px}}
.tint{{background:var(--tint);color:var(--ontint);padding:0 3px}} .edited{{font-size:1rem;margin:.3em 0}}
.callout{{border:1px solid var(--ink);padding:2px 6px;margin:2px 0;font-size:.85rem}} .callout b{{margin-right:.4em}}
.mi{{display:flex;align-items:center;gap:6px;margin:3px 0}} .mi img{{height:46px;border:1px solid var(--rule)}}
"""


def legend_html():
    parts = [f'{token_html("a", g)} = {d}' for g, d in
             (('H', 'read from a key source'), ('C', 'known plaintext'), ('S', 'cryptanalytic, with a control'),
              ('M', 'uncertain'), ('I', 'inferred or repaired'))]
    parts.append(f'{token_html("", "U", code="code")} = sign not in the key')
    parts.append(f'{token_html("", "NULL", null=True)} = null')
    return '<p class="legend note">' + ' '.join(f'<span>{p}</span>' for p in parts) + '</p>'


def git_short():
    try:
        return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], cwd=ROOT, text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return 'unknown'


def footer(slug, a, inputs):
    f = dict(FOOTERS.get(slug, {}))
    key = a.key_credit or f.get('key') or 'Key: see the target folder'
    img = a.image_credit or f.get('img') or ''
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%-d %b %Y %H:%M UTC')
    link = f' <a href="{html.escape(a.leaf_url)}">leaf</a>' if a.leaf_url else ''
    ins = '; '.join(f'{os.path.basename(p)} {h[:10]}' for p, h in inputs)
    return (f'<div class="foot"><p>{html.escape(key)}{link}.</p><p>{html.escape(img)}</p>'
            f'<p>Repository commit <span class="vol">{git_short()}</span>, rendered <span class="vol">{now}</span>. '
            f'Inputs (sha256): {html.escape(ins)}.</p><p>{html.escape(LAYOUT_CREDIT)}</p></div>')


def key_classes(key):
    """Group key rows: letters (I/J, U/V merged), null, and nomenclature by value class."""
    letters = collections.defaultdict(list)
    special, classes = [], collections.defaultdict(list)
    for code, row in key.items():
        v = row['value']
        vl = v.lstrip('=')
        if v in ('NULL', 'null', ''):
            special.append(code)
        elif len(vl) == 1 and vl.isalpha():
            L = vl.upper()
            L = {'J': 'I/J', 'I': 'I/J', 'U': 'U/V', 'V': 'U/V'}.get(L, L)
            letters[L].append(code)
        elif vl.isdigit():
            classes['numbers'].append(code)
        elif vl.lower() in FUNCTION_WORDS:
            classes['function words'].append(code)
        elif vl.lower() in TITLE_WORDS:
            classes['titles'].append(code)
        elif vl[:1].isupper():
            classes['persons and places'].append(code)
        elif len(vl) <= 3:
            classes['syllables'].append(code)
        else:
            classes['words'].append(code)
    return letters, special, classes


def best_grade(g_counts, key_row):
    if g_counts:
        return g_counts.most_common(1)[0][0]
    return (key_row.get('grade') or 'H')


def build_key_html(ctx):
    recs, key, boxes, a = ctx['recs'], ctx['key'], ctx['boxes'], ctx['args']
    counts = collections.Counter(r['sign'] for r in recs if r['kind'] == 'sign')
    gcount = collections.defaultdict(collections.Counter)
    by_code = collections.defaultdict(list)
    for r in recs:
        if r['kind'] != 'sign':
            continue
        gcount[r['sign']][r['grade']] += 1
        bx = boxes.token_box(r) if boxes else None
        if bx and len(bx) == 1 and bx[0][1] == '1:1' and r['grade'] in ('H', 'C', 'S'):
            by_code[r['sign']].append(bx[0][0])
    ex = exemplar_ids(boxes.atlas, by_code, a.variants) if boxes and a.tiles != 'none' else {}
    ex_tiles = {}
    tiles_report = ctx['tile_report']
    exf = {}
    if a.exemplar_tsv:
        from PIL import Image
        for r in load_tsv(a.exemplar_tsv):
            im = Image.open(os.path.join(os.path.dirname(os.path.abspath(a.exemplar_tsv)), r['image'])).convert('L')
            if r.get('x0'):
                im = im.crop(tuple(int(r[k]) for k in ('x0', 'y0', 'x1', 'y1')))
            exf.setdefault(r['code'], []).append(im)

    def cell(code):
        row = key[code]
        g = best_grade(gcount.get(code), row)
        imgs = []
        for sid in ex.get(code, []):
            im = boxes.cut([sid]); imgs.append((sid, im))
        for k, im in enumerate(exf.get(code, [])[:a.variants]):
            imgs.append((f'{code}#x{k}', im))
        for sid, im in imgs:
            st = tile_stats(im)
            tiles_report.append(dict(kind='exemplar', tile=sid, code=code, token='', key_value=row['value'], row_value='', **st, agree=''))
        tiles = ''.join(f'<img alt="" src="{data_uri(im, 44)}">' for _, im in imgs)
        n = counts.get(code, 0)
        gl = token_html(row['value'], g, code=code)
        return (f'<span class="code">{tiles}<span class="mono">{html.escape(code)}</span> '
                f'<span class="mono">n={n}</span> {gl}</span>'), n

    letters, special, classes = key_classes(key)
    out = []
    atl = [L for L in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I/J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U/V', 'X', 'Y', 'Z']]
    if 'W' in letters:
        atl.insert(atl.index('X'), 'W')
    out.append('<h2>Letters</h2><div>')
    for L in atl:
        cs = sorted(letters.get(L, []), key=lambda c: (-counts.get(c, 0), c))
        if not cs:
            continue
        shown = [cell(c)[0] for c in cs if counts.get(c, 0)]
        if shown:
            out.append(f'<div class="letter"><div class="L">{L}</div>{"".join(shown)}</div>')
    out.append('</div>')
    if special:
        out.append('<h2>Special symbols</h2><div class="strip">' + ''.join(cell(c)[0] for c in sorted(special)) + '</div>')
    for name in ('persons and places', 'titles', 'words', 'syllables', 'function words', 'numbers'):
        cs = [c for c in classes.get(name, []) if counts.get(c, 0)]
        if cs:
            out.append(f'<h2>{name.capitalize()}</h2><div class="strip">' + ''.join(cell(c)[0] for c in sorted(cs, key=lambda c: -counts[c])) + '</div>')
    unatt = [c for c in key if not counts.get(c, 0)]
    if unatt:
        out.append(f'<h2>Keyed but not attested here ({len(unatt)})</h2><div class="strip note">' +
                   '; '.join(f'<span class="mono">{html.escape(c)}</span> = {token_html(key[c]["value"], key[c].get("grade") or "H", code=c)}'
                             for c in sorted(unatt)) + '</div>')
    if a.mi_panel:
        out.append(mi_panel_html(ctx))
    ctx['n_codes'] = len(key)
    ctx['n_attested'] = sum(1 for c in key if counts.get(c, 0))
    return ''.join(out)


def mi_panel_html(ctx):
    recs, boxes = ctx['recs'], ctx['boxes']
    if not boxes:
        return '<h2>M/I tokens beside S exemplars</h2><p class="note">No per-sign boxes for this target: panel not drawn.</p>'
    s_tiles, mi = {}, []
    for r in recs:
        if r['kind'] != 'sign':
            continue
        bx = boxes.token_box(r)
        if not bx or len(bx) != 1 or bx[0][1] != '1:1':
            continue
        t = (bx[0][0], r)
        if r['grade'] == 'S':
            s_tiles[bx[0][0]] = (boxes.cut([bx[0][0]]), r)
        elif r['grade'] in ('M', 'I'):
            mi.append(t)
    if not mi or not s_tiles:
        return '<h2>M/I tokens beside S exemplars</h2><p class="note">No M/I token with a box, or no S exemplar: panel not drawn.</p>'
    rows = ['<h2>M/I tokens beside their three nearest S exemplars</h2><p class="note">Dice overlap of 32x32 ink masks, best of &plusmn;2 px shifts; a ranking for a person to look at, not a reading.</p>']
    for sid, r in mi[:ctx['args'].mi_max]:
        near = nearest_s(boxes.cut([sid]), {k: v[0] for k, v in s_tiles.items()})
        cells = f'<img alt="" src="{data_uri(boxes.cut([sid]), 46)}"> {token_html(r["value"], r["grade"], code=r["sign"])} &nbsp;&rarr;&nbsp;'
        for d, k in near:
            cells += f'<img alt="" src="{data_uri(s_tiles[k][0], 46)}"> <span class="mono">{html.escape(s_tiles[k][1]["sign"])} {d:.2f}</span> '
        rows.append(f'<div class="mi">{cells}</div>')
    return ''.join(rows)


def parse_line_range(spec, labels):
    if not spec:
        return labels
    m = re.match(r'^([A-Za-z]*)(\d+)-([A-Za-z]*)(\d+)$', spec)
    if not m:
        return [l for l in labels if spec in l]
    pre, lo, hi = m.group(1), int(m.group(2)), int(m.group(4))
    out = []
    for l in labels:
        mm = re.search(r'(\d+)$', l)
        if mm and lo <= int(mm.group(1)) <= hi:
            out.append(l)
    return out


def build_reading_html(ctx):
    recs, key, boxes, a = ctx['recs'], ctx['key'], ctx['boxes'], ctx['args']
    job = ctx['job']
    lines = list(decode_key.lines_of(recs))
    sel = set(parse_line_range(a.lines, [L['label'] for L in lines]))
    hl = {}
    for n, c in enumerate([c for c in (a.highlight or '').split(',') if c], 1):
        hl[c] = (((n - 1) % 3) + 1, n)
    ann = {}
    if a.annotate:
        for r in load_tsv(a.annotate):
            ann.setdefault(r['category'], []).append(r)
    lineimg = ctx['line_images']
    out, non11, unaligned = [], collections.Counter(), []
    for L in lines:
        if L['label'] not in sel:
            continue
        toks = [r for r in L['toks'] if r['kind'] in ('sign', 'clear')]
        lkey = L['label'].replace(' ', '_')
        boxed = [boxes.token_box(r) for r in toks if boxes] if boxes else []
        has_boxes = any(boxed)
        out.append(f'<div class="line"><div class="note"><b>{html.escape(L["label"])}</b></div>')
        li = lineimg.get(lkey) or lineimg.get(L['label'])
        if li is not None:
            st = tile_stats(li)
            ctx['tile_report'].append(dict(kind='line', tile=lkey, code='', token='', key_value='', row_value='', agree='', **st))
            out.append(f'<img class="crop" alt="line crop" src="{data_uri(li, min(li.height, 120))}">')
            if not has_boxes:
                out.append('<p class="note">Token row not aligned to the image.</p>')
        if not has_boxes and (boxes or lineimg) and a.tiles != 'none':
            unaligned.append(L['label'])
        out.append('<div class="row">')
        for r in toks:
            if r['kind'] == 'clear':
                out.append(f'<div class="tk"><div class="v">{html.escape("{"+r["value"]+"}")}</div></div>')
                continue
            bx = boxes.token_box(r) if boxes else None
            img, cls = '', ''
            if bx:
                op = bx[0][1]
                sids = [s for s, _ in bx] if op == '2:1' else [bx[0][0]]
                if op != '1:1':
                    non11[op] += 1; cls = ' x'
                im = boxes.cut(sids)
                st = tile_stats(im)
                kv = key.get(r['sign'], {}).get('value', '')
                ctx['tile_report'].append(dict(kind='token', tile=sids[0], code=r['sign'], token=f"{L['label']}:{r['pos']}",
                                               key_value=kv, row_value=r['value'], **st,
                                               agree=('' if not kv else str(kv == r['value']))))
                img = f'<img alt="" src="{data_uri(im, 40)}">'
            h = hl.get(r['sign'])
            out.append(f'<div class="tk{cls}">{img}<div class="c">{html.escape(r.get("raw", r["sign"]))}</div>'
                       f'<div class="v">{token_html(r["value"], r["grade"], bool(r.get("null")), r["sign"], h)}</div></div>')
        out.append('</div>')
        ed = decode_key.render_case([dict(kind='line', label=L['label'])] + L['toks'], job)
        out.append(f'<p class="edited mono">{html.escape(ed[0].split(chr(9), 1)[1]) if ed else ""}</p></div>')
    notes = []
    if unaligned:
        notes.append(f'No per-sign boxes for {len(unaligned)} line(s) ({", ".join(unaligned)}): token row not aligned to the image'
                     + (' (codes only, no tile).' if not lineimg else '.'))
    if non11:
        notes.append('Box-to-token rows not 1:1 (dashed tile border): ' + ', '.join(f'{k} x{v}' for k, v in sorted(non11.items())) + '.')
    if ann:
        out.append('<h2>Annotations</h2>')
        for cat in ann:
            for r in ann[cat]:
                out.append(f'<div class="callout"><b>{html.escape(cat)}</b>token {html.escape(r["token"])}: {html.escape(r["text"])}</div>')
    tr = ctx.get('translation')
    if tr:
        out.append('<h2>Translation (as held in the folder, not generated here)</h2><pre class="note">' + html.escape(tr) + '</pre>')
    return ''.join(out) + ''.join(f'<p class="note">{html.escape(n)}</p>' for n in notes)


def header_html(ctx, kind):
    a, r, recs = ctx['args'], ctx['result'], ctx['recs']
    cnt = collections.Counter(x['grade'] for x in recs if x['kind'] == 'sign')
    title = a.title or (r or {}).get('document_id') or os.path.basename(os.path.abspath(a.target))
    bits = []
    if r:
        bits.append(f'Novelty class: {html.escape(str(r.get("grade", "")))}; key source: {html.escape(str(r.get("key", "")))}')
        dw = depth_words(r)
        if dw:
            bits.append('Depth: ' + html.escape(dw))
    for kv in a.meta or []:
        bits.append(html.escape(kv.replace('=', ': ', 1)))
    gl = ', '.join(f'{g} {cnt[g]}' for g in 'HCSMIU' if cnt[g])
    bits.append(f'Tokens {sum(cnt.values())}: {gl}')
    conv = ('Editing: capitals are H/C/S grades, lower case M, [brackets] inferred or corrected, &lt;code&gt; not in the key; '
            'u/v and i/j are shown as the key gives them; nomenclature spellings are the key\'s own (the 2023 paper does the same at p.136 n.95).')
    return (f'<h1>{html.escape(title)} &mdash; {kind} sheet</h1><div class="meta">' + '<br>'.join(bits) + f'</div>'
            f'<p class="note">{conv}</p>' + legend_html())


def build(a):
    refuse_restricted(a.target)
    refuse_open_sort(a.target, explicit=a.key_family, fam_path=a.families)
    os.chdir(ROOT)
    inputs = []
    note = lambda p: inputs.append((os.path.relpath(p, ROOT) if os.path.isabs(p) else p, sha(p)))
    target = os.path.abspath(a.target)
    if a.tokens_tsv:
        refuse_open_sort(target, [a.key_tsv] if a.key_tsv else [], a.key_family, a.families)
        recs, key = tokens_from_tsv(a.tokens_tsv, a.key_tsv); job = {}
        note(a.tokens_tsv)
        if a.key_tsv:
            note(a.key_tsv)
        ct = os.path.basename(a.tokens_tsv)
    else:
        ns = types.SimpleNamespace(config=a.config, ciphertext=None, key=None, exceptions=None, style=None, reading=None, tokens=None)
        jobs = decode_key.load_config(target, ns)
        job = select_job(jobs, a.job)
        recs, key, ct = graded(target, job)
        if a.config:
            note(a.config)
        elif os.path.exists(os.path.join(target, 'decode.json')):
            note(os.path.join(target, 'decode.json'))
        note(os.path.join(target, ct))
        ks = job.get('key', 'key.tsv')
        refuse_open_sort(target, [os.path.normpath(os.path.join(target, k)) for k in ([ks] if isinstance(ks, str) else ks)],
                         a.key_family, a.families)
        for k in ([ks] if isinstance(ks, str) else ks):
            note(os.path.join(target, k))
        ex = os.path.join(target, job.get('exceptions', 'exceptions.tsv'))
        if os.path.exists(ex):
            note(ex)
    # boxes
    boxes = None
    atlas = a.atlas or (os.path.join(target, 'atlas') if os.path.exists(os.path.join(target, 'atlas', 'signs.tsv')) else None)
    bmap = a.box_map or (os.path.join(target, 'atlas', 'no87_box_token.tsv') if atlas and os.path.exists(os.path.join(target, 'atlas', 'no87_box_token.tsv')) else None)
    if a.tiles in ('auto', 'boxes') and atlas and bmap:
        boxes = Boxes(atlas, bmap)
        for p in (os.path.join(atlas, 'signs.tsv'), bmap):
            note(p)
    line_images = {}
    if a.line_images and a.tiles != 'none':
        from PIL import Image
        for r in load_tsv(a.line_images):
            p = os.path.join(os.path.dirname(os.path.abspath(a.line_images)), r['image'])
            im = Image.open(p).convert('L')
            if r.get('x0'):
                im = im.crop(tuple(int(r[k]) for k in ('x0', 'y0', 'x1', 'y1')))
            line_images[r['line']] = im
        note(a.line_images)
    if a.exemplar_tsv:
        note(a.exemplar_tsv)
    result = status_result(a.result)
    if a.result and not result:
        raise SystemExit(f'decipher_sheet: no status.json result matches {a.result!r}')
    if result:
        inputs.append(('status.json:result', hashlib.sha256(json.dumps(result, sort_keys=True).encode()).hexdigest()))
    if a.mode == 'reading' and result and depth_words(result) is None and not a.allow_d0:
        raise SystemExit('decipher_sheet: no reading sheet at depth D0 (or no depth recorded); nothing to show')
    tr = None
    for n in ('translation.txt', 'translation.md'):
        if os.path.exists(os.path.join(target, n)):
            tr = open(os.path.join(target, n), encoding='utf-8').read(); note(os.path.join(target, n))
    ctx = dict(args=a, recs=recs, key=key, job=job, boxes=boxes, line_images=line_images, result=result,
               tile_report=[], translation=tr)
    body = build_key_html(ctx) if a.mode == 'key' else build_reading_html(ctx)
    slug = os.path.basename(target.rstrip('/'))
    head = header_html(ctx, a.mode)
    inm = ''.join(f'<meta name="input-sha256" content="{html.escape(p)} {h}">' for p, h in inputs)
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>{html.escape(a.title or slug)} {a.mode} sheet</title>{inm}<style>{CSS}</style></head><body>'
           f'{head}{body}{footer(slug, a, inputs)}</body></html>')
    return doc, ctx


def normalise(doc):
    return re.sub(r'<span class="vol">.*?</span>', '<span class="vol"></span>', doc)


def write_report(path, rows):
    cols = ['kind', 'tile', 'code', 'token', 'w', 'h', 'nonempty', 'ink', 'ink_ok', 'key_value', 'row_value', 'agree']
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(('%.3f' % r[c]) if c == 'ink' else str(r.get(c, '')) for c in cols) + '\n')
    n = len(rows)
    bad = collections.Counter()
    for r in rows:
        bad['blank'] += not r['nonempty']
        bad['ink_out_of_range'] += (r['nonempty'] and not r['ink_ok'])
        bad['label_value_mismatch'] += (r['agree'] == 'False')
    print(f'tile report: {n} tiles; failing: ' + ', '.join(f'{k} {v}' for k, v in bad.items()) + f' -> {path}')
    return bad


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('mode', choices=['key', 'reading'])
    ap.add_argument('target')
    ap.add_argument('--config'); ap.add_argument('--job'); ap.add_argument('--result', help='substring of the status.json result document_id/title')
    ap.add_argument('--tiles', choices=['auto', 'boxes', 'lines', 'none'], default='auto')
    ap.add_argument('--atlas'); ap.add_argument('--box-map'); ap.add_argument('--line-images'); ap.add_argument('--exemplar-tsv')
    ap.add_argument('--tokens-tsv'); ap.add_argument('--key-tsv')
    ap.add_argument('--variants', type=int, default=3); ap.add_argument('--mi-panel', action='store_true'); ap.add_argument('--mi-max', type=int, default=24)
    ap.add_argument('--lines'); ap.add_argument('--highlight'); ap.add_argument('--annotate')
    ap.add_argument('--title'); ap.add_argument('--meta', action='append'); ap.add_argument('--leaf-url')
    ap.add_argument('--key-credit'); ap.add_argument('--image-credit'); ap.add_argument('--allow-d0', action='store_true')
    ap.add_argument('--out', required=True); ap.add_argument('--png', action='store_true'); ap.add_argument('--pdf', action='store_true')
    ap.add_argument('--key-family', help='sorter key family of this target (default: KEY_FAMILY_TARGETS, then key paths)')
    ap.add_argument('--families', help='sorter family register (default tools/data/sorter_families.tsv; tests)')
    ap.add_argument('--check', action='store_true'); ap.add_argument('--tile-report')
    a = ap.parse_args(argv)
    if a.config:
        a.config = os.path.abspath(a.config)
    for k in ('atlas', 'box_map', 'line_images', 'exemplar_tsv', 'tokens_tsv', 'key_tsv', 'annotate'):
        if getattr(a, k):
            setattr(a, k, os.path.abspath(getattr(a, k)))
    a.out = os.path.abspath(a.out)
    doc, ctx = build(a)
    if a.check:
        old = open(a.out, encoding='utf-8').read() if os.path.exists(a.out) else None
        stale = old is None or normalise(old) != normalise(doc)
        print('STALE: ' + a.out if stale else 'sheet up to date')
        return 1 if stale else 0
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, 'w', encoding='utf-8').write(doc)
    size = len(doc.encode())
    print(f'{a.out}: {size / 1e6:.2f} MB' + ('  WARNING: over the 3 MB limit' if size > MAX_BYTES else ''))
    if a.tile_report:
        write_report(a.tile_report, ctx['tile_report'])
    if a.png or a.pdf:
        cmd = ['node', os.path.join(ROOT, 'tools', 'browser_fetch.js'), 'file://' + a.out, a.out + '.render.html']
        if a.png:
            cmd += ['--shot', os.path.splitext(a.out)[0] + '.png']
        if a.pdf:
            cmd += ['--pdf', os.path.splitext(a.out)[0] + '.pdf']
        env = dict(os.environ, NODE_PATH=subprocess.check_output(['npm', 'root', '-g'], text=True).strip())
        subprocess.run(cmd, check=False, env=env)
        try:
            os.remove(a.out + '.render.html')
        except OSError:
            pass
    return 0


if __name__ == '__main__':
    sys.exit(main())
