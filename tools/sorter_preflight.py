#!/usr/bin/env python3
"""Pre-publish gate for a sign-sorter page (SORTER-PREFLIGHT, 6 Oct 2026; CLAUDE.md Usage 8a: a rule broken twice
becomes a tool). Exits non-zero unless the page is fit to put in front of the owner.

  python3 tools/sorter_preflight.py SORTER.html [--cipher-lines FILE] [--expect-owner-account] [--sheet OUT.png]
  python3 tools/sorter_preflight.py --inputs DIR [--cipher-lines FILE]      (text inputs: signs.tsv, labels.tsv,
        focus.tsv, optional pages/ -- before a build, or where the images may not leave a private clone)

Why (owner, 6 Oct 2026, "how do we prevent this in the future?"): the Oldenbarnevelt A/C2 sorter (R7-OLDSORT) cut its
tiles with boxes the full height of the strip, reaching into the line above and below, and tiled the clear Spanish
opening of line A1; the Dinteville f.23r sorter (ASKS 112) put 268 of 303 tiles in one UNREAD pile and asked 21
"Check these first" questions ("pass A D, pass B -; which sheet label?") whose labels had no pile to tap; the MLH
page reached the owner on a template without "Fix the cut". Each was found by the owner, after publishing.

Checks (each prints one line; the verdict is PASS only if all four pass):
 1. template  the page carries the "Fix the cut" control (id="ctxFix") and the current template's version marker
              (<meta name="sign-sorter-template" content=...> in tools/sign_sorter/template.html). An older page is
              re-rendered with tools/sorter_rerender.py. Not applicable with --inputs.
 2. answerable  the focus box is non-empty; every focus sid is a tile on the page; the page has >= 2 named piles
              (placeholders such as UNREAD, unsorted, '?', '_' and piles starting '?' are not named) so a tile can go
              somewhere other than where it is; and every sign label a focus question offers in the reader-split
              forms ("pass A x", "readers x / y", "draft x", "the x pile") is a pile on the page. '-' (a reader saw
              nothing) is answered by the template's own "Not a letter", so it needs no pile.
 3. right line  every tile's page/line id is in the cipher-line list (--cipher-lines, or cipher_lines.tsv /
              segment_pages.txt beside the inputs), and inside that line's cipher x-range when the list gives one
              (a mixed line: clear words before the cipher). Any tile off the list fails the run. Then three shape
              counts, failing above 5% of tiles together: ink ratio outside 3-60% (a blank or solid-black box; needs
              the page images), width over 2.5x the median sign width (merged signs), and a box touching both the top
              and bottom edge of its strip (a strip-height box reaches into the neighbouring lines -- the
              Oldenbarnevelt v1 shape).
 4. contact sheet  writes <page stem>.preflight.png (or --sheet): 24 random tiles (--seed) each beside its line
              strip with the box drawn, for a person or a separate session to eye in 30 seconds. Fails only if it
              cannot be drawn when page images exist; with no images (text-only inputs) it is skipped and says so.
 --expect-owner-account  also fail unless CIPHERLAB_ACCOUNT is 'owner' (ASKS 145: a page published from another
              account is private to it, and the owner gets "deleted or not available").

Must NOT block (each has an offline test in tools/tests/test_sorter_preflight.py):
 - a page whose focus tiles are legitimately all one family or one pile (Ferdinand's 25 t / tt / e questions): the
   gate counts named piles on the page, never the spread of the focus tiles' own piles;
 - a focus question in free prose that names no reader split ("tt or a single crossed t?"): only the explicit
   reader-split forms are parsed for labels;
 - a reader split with '-' on one side ("pass A -, pass B 4"): Not a letter answers it;
 - a tall sign that touches one strip edge (an ascender reaching the top): only a box touching BOTH edges counts.
It is a shape gate, not a reading check: a PASS says the page can be answered and shows cipher signs, never that
the starting piles are right.
"""
import argparse, base64, csv, io, json, os, random, re, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, 'sign_sorter', 'template.html')
MARKER_RE = re.compile(r'<meta name="sign-sorter-template" content="([^"]+)"')
PLACEHOLDER = {'', '_', '?', 'unread', 'unsorted', 'unknown', 'none', 'bad-cut', 'not-a-letter', 'nonletter'}
PROSE = {'sign', 'signs', 'word', 'words', 'blind', 'label', 'labels', 'pile', 'piles', 'here', 'reading', 'this', 'that', 'which'}
NOTHING = {'-', '—', '–', 'nothing', 'none', '(none)', '0-'}
SPLIT_FORMS = [
    re.compile(r"\bpass\s+[A-Z0-9]+:?\s+(\S+?)(?=[,;)]|\s|$)"),
    re.compile(r"\breaders?\s+(?:split\s+)?(\S+?)\s*/\s*(\S+?)(?=[,;.)]?(?:\s|$))"),
    re.compile(r"(?<![Nn]o )\bdraft\s+(\S+?)(?=[,;)]|\s|$)"),
    re.compile(r"\bthe\s+(\S+)\s+pile\b"),
]
INK_LO, INK_HI, WIDE, MAX_BAD = 0.03, 0.60, 2.5, 0.05


def current_marker():
    m = MARKER_RE.search(open(TEMPLATE).read())
    return m.group(1) if m else None


def named(pile):
    p = (pile or '').strip()
    return not (p.lower() in PLACEHOLDER or p.startswith('?'))


def offered_labels(q):
    out = []
    for rx in SPLIT_FORMS:
        for m in rx.finditer(q):
            out += [g for g in m.groups() if g]
    out = [l.strip('"\'') for l in out]
    return [l for l in out if l and l.lower() not in NOTHING and l.lower() not in PROSE]


# ---------- loading: a built page, or the text inputs ----------
def load_html(path):
    """-> (data, html). DATA is the JSON the template embeds as `const DATA = {...};`."""
    html = open(path, encoding='utf-8').read()
    i = html.find('const DATA = ')
    if i < 0:
        sys.exit(f'{path}: no "const DATA = " -- not a sign_sorter.py page')
    data, _ = json.JSONDecoder().raw_decode(html, i + len('const DATA = '))
    return data, html


def page_images_from_data(data):
    from PIL import Image
    out = {}
    for p, b64 in (data.get('pages') or {}).items():
        try:
            out[p] = Image.open(io.BytesIO(base64.b64decode(b64))).convert('L')
        except Exception:
            pass
    return out, float(data.get('pageScale') or 1.0)


def load_inputs(d):
    def tsv(p):
        return list(csv.DictReader(open(p, newline=''), delimiter='\t'))
    signs = {r['sid']: r for r in tsv(os.path.join(d, 'signs.tsv'))}
    piles = {}
    for r in tsv(os.path.join(d, 'labels.tsv')):
        s = signs.get(r['sid'])
        if not s:
            continue
        piles.setdefault(r['sign'], []).append({'sid': r['sid'], 'p': s['page'],
                                                'b': [int(float(s[k])) for k in ('x', 'y', 'w', 'h')]})
    focus = []
    fp = os.path.join(d, 'focus.tsv')
    if os.path.exists(fp):
        for l in open(fp, encoding='utf-8'):
            r = l.rstrip('\n').split('\t')
            if len(r) >= 2 and r[0] != 'sid':
                focus.append({'sid': r[0], 'q': r[1]})
    data = {'piles': [{'id': k, 'items': v} for k, v in piles.items()], 'focus': focus}
    imgs = {}
    pd = os.path.join(d, 'pages')
    if os.path.isdir(pd):
        from PIL import Image
        for p in {it['p'] for v in piles.values() for it in v}:
            for e in ('.png', '.jpg', '.jpeg'):
                if os.path.exists(os.path.join(pd, p + e)):
                    imgs[p] = Image.open(os.path.join(pd, p + e)).convert('L'); break
    return data, imgs, 1.0


def read_cipher_lines(path):
    """-> {line_id: (x0, x1) or None}. Accepts: one id per line, optionally TAB x0 [TAB x1] (the cipher part of a mixed
    line, in strip pixels; '#' comments); or a glyph_atlas segment_pages.txt (`--page ID=...`)."""
    txt = open(path, encoding='utf-8').read()
    if '--page ' in txt:
        return {m.group(1): None for m in re.finditer(r'--page\s+([^=\s]+)=', txt)}
    out = {}
    for l in txt.splitlines():
        l = l.split('#', 1)[0].strip()
        if not l:
            continue
        r = re.split(r'\s+', l)
        if r[0] in ('line', 'page', 'id'):
            continue
        x0 = float(r[1]) if len(r) > 1 and r[1] not in ('', '-') else None
        x1 = float(r[2]) if len(r) > 2 and r[2] not in ('', '-') else None
        out[r[0]] = (x0, x1) if (x0 is not None or x1 is not None) else None
    return out


def find_cipher_lines(*dirs):
    for d in dirs:
        for n in ('cipher_lines.tsv', 'cipher_lines.txt', 'segment_pages.txt'):
            p = os.path.join(d, n)
            if os.path.exists(p):
                return p
    return None


# ---------- checks ----------
def check_template(html):
    if html is None:
        return None, 'template: n/a (text inputs, no page)'
    cur = current_marker()
    has_fix = 'id="ctxFix"' in html
    m = MARKER_RE.search(html)
    got = m.group(1) if m else None
    ok = has_fix and got is not None and got == cur
    why = []
    if not has_fix:
        why.append('no "Fix the cut" (ctxFix)')
    if got != cur:
        why.append(f'template marker {got or "missing"} != current {cur}')
    return ok, 'template: ' + ('ok, Fix the cut present, marker ' + str(cur) if ok else
                               '; '.join(why) + ' -- re-render with tools/sorter_rerender.py')


def check_answerable(data):
    piles = {p['id'] for p in data['piles']}
    sids = {it['sid'] for p in data['piles'] for it in p['items']}
    names = sorted(p for p in piles if named(p))
    focus = data.get('focus') or []
    bad, msgs = [], []
    if not focus:
        msgs.append('focus box empty')
    if len(names) < 2:
        msgs.append(f'{len(names)} named pile(s) {names} -- a tile has nowhere to go')
    for f in focus:
        if f['sid'] not in sids:
            bad.append(f['sid']); msgs.append(f'{f["sid"]}: not a tile on the page'); continue
        miss = [l for l in dict.fromkeys(offered_labels(f.get("q", ""))) if l not in piles]
        if miss:
            bad.append(f['sid']); msgs.append(f'{f["sid"]}: question offers {", ".join(miss)}, no such pile')
    ok = bool(focus) and len(names) >= 2 and not bad
    head = f'answerable: {len(focus)} focus tiles, {len(names)} named piles of {len(piles)}, {len(bad)} unanswerable'
    if msgs:
        head += ' -- ' + '; '.join(msgs[:6]) + (f'; ... {len(msgs) - 6} more' if len(msgs) > 6 else '')
    return ok, head


def ink_ratio(im, box, scale):
    x, y, w, h = (round(v * scale) for v in box)
    x0, y0, x1, y1 = max(0, x), max(0, y), min(im.width, x + max(1, w)), min(im.height, y + max(1, h))
    if x1 <= x0 or y1 <= y0:
        return None
    h = im.crop((x0, y0, x1, y1)).histogram()[:256]
    return sum(h[:otsu(im)]) / max(1, sum(h))


_OTSU = {}
def otsu(im):
    k = id(im)
    if k not in _OTSU:
        hist = im.histogram()[:256]; tot = sum(hist); sm = sum(i * c for i, c in enumerate(hist))
        wb = sb = 0; best, t = -1, 128
        for i in range(256):
            wb += hist[i]
            if wb == 0: continue
            wf = tot - wb
            if wf == 0: break
            sb += i * hist[i]
            mb, mf = sb / wb, (sm - sb) / wf
            v = wb * wf * (mb - mf) ** 2
            if v > best: best, t = v, i
        _OTSU[k] = t + 1
    return _OTSU[k]


def check_lines(data, imgs, scale, cl):
    items = [it for p in data['piles'] for it in p['items']]
    n = len(items)
    if not n:
        return False, 'right line: no tiles', {}
    flags = {}
    off = []
    if cl is None:
        line_msg = 'no cipher-line list (give --cipher-lines, or put cipher_lines.tsv beside the inputs)'
        line_ok = False
    else:
        for it in items:
            if it['p'] not in cl:
                off.append(it['sid']); flags[it['sid']] = 'off-list line ' + it['p']; continue
            rng = cl[it['p']]
            if rng:
                cx = it['b'][0] + it['b'][2] / 2
                if (rng[0] is not None and cx < rng[0]) or (rng[1] is not None and cx > rng[1]):
                    off.append(it['sid']); flags[it['sid']] = 'outside cipher x-range of ' + it['p']
        line_ok = not off
        lines_off = sorted({it['p'] for it in items if it['sid'] in off})
        unused = sorted(set(cl) - {it['p'] for it in items})
        line_msg = (f'{len(off)} tile(s) off the cipher lines' + (f' ({", ".join(lines_off[:8])})' if off else '')
                    + f', {len(cl) - len(unused)} of {len(cl)} listed lines have tiles'
                    + (f' (none on {", ".join(unused[:8])})' if unused else ''))
    med = statistics.median(it['b'][2] for it in items) or 1
    wide = [it['sid'] for it in items if it['b'][2] > WIDE * med]
    strip_h = {p: im.height / scale for p, im in imgs.items()}
    # needs the strip image's own height: inferred from the boxes, every top-touching box would "reach the bottom"
    full = [it['sid'] for it in items if it['p'] in imgs and it['b'][1] <= 1
            and it['b'][1] + it['b'][3] >= strip_h[it['p']] - 1]
    ink_bad, ink_n = [], 0
    for it in items:
        im = imgs.get(it['p'])
        if im is None:
            continue
        r = ink_ratio(im, it['b'], scale)
        if r is None:
            ink_bad.append(it['sid']); continue
        ink_n += 1
        if r < INK_LO or r > INK_HI:
            ink_bad.append(it['sid'])
    for s in wide: flags.setdefault(s, 'wide')
    for s in full: flags.setdefault(s, 'strip-height box')
    for s in ink_bad: flags.setdefault(s, 'ink outside 3-60%')
    shape_bad = set(wide) | set(full) | set(ink_bad)
    frac = len(shape_bad) / n
    ok = line_ok and frac <= MAX_BAD
    ink_txt = f'{len(ink_bad)} ink outside 3-60% of {ink_n} measured' if imgs else 'ink not measured (no page images)'
    msg = (f'right line: {n} tiles; {line_msg}; shape: {len(wide)} wide (>{WIDE}x median {med:g} px), '
           + (f'{len(full)} strip-height boxes' if imgs else 'strip-height not measured') + f', {ink_txt}; {len(shape_bad)} = {100 * frac:.1f}% (limit {100 * MAX_BAD:.0f}%)')
    return ok, msg, flags


def contact_sheet(data, imgs, scale, out, flags, seed=20261006, k=24):
    from PIL import Image, ImageDraw
    items = [it for p in data['piles'] for it in p['items'] if it['p'] in imgs]
    if not items:
        return None, 'contact sheet: skipped (no page images in the inputs)'
    rnd = random.Random(seed)
    pick = rnd.sample(items, min(k, len(items)))
    pile_of = {it['sid']: p['id'] for p in data['piles'] for it in p['items']}
    CW, CH, TW = 560, 110, 90
    cols = 2; rows = (len(pick) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * (CW + TW + 16), rows * (CH + 22) + 8), 'white')
    g = ImageDraw.Draw(sheet)
    for i, it in enumerate(pick):
        im = imgs[it['p']]
        x, y, w, h = (round(v * scale) for v in it['b'])
        ox, oy = (i % cols) * (CW + TW + 16) + 6, (i // cols) * (CH + 22) + 4
        # the line strip: a window 4x the strip height wide around the tile, whole strip height
        win = max(w * 6, im.height * 4)
        x0 = max(0, min(x + w // 2 - win // 2, im.width - win)); x1 = min(im.width, x0 + win)
        strip = im.crop((x0, 0, x1, im.height)).convert('RGB')
        d = ImageDraw.Draw(strip); d.rectangle((x - x0, y, x - x0 + w, y + h), outline=(200, 30, 30), width=max(2, im.height // 60))
        strip.thumbnail((CW, CH)); sheet.paste(strip, (ox + TW + 6, oy + 18))
        tile = im.crop((max(0, x - 4), max(0, y - 4), min(im.width, x + w + 4), min(im.height, y + h + 4))).convert('RGB')
        tile.thumbnail((TW, CH)); sheet.paste(tile, (ox, oy + 18))
        lab = f"{it['sid']}  [{pile_of.get(it['sid'], '')}]" + (f"  ! {flags[it['sid']]}" if it['sid'] in flags else '')
        g.text((ox, oy + 3), lab, fill=(0, 0, 0) if it['sid'] not in flags else (200, 30, 30))
    sheet.save(out)
    return True, f'contact sheet: {len(pick)} tiles beside their line strips -> {out} (seed {seed}; eye it before publishing)'


def run(page=None, inputs=None, cipher_lines=None, expect_owner=False, sheet=None, seed=20261006, quiet=False, search=()):
    """-> (ok, lines). Used by tools/sign_sorter.py after a build."""
    html = None
    if page:
        data, html = load_html(page)
        imgs, scale = page_images_from_data(data)
        base = os.path.dirname(os.path.abspath(page))
    else:
        data, imgs, scale = load_inputs(inputs)
        base = os.path.abspath(inputs)
    clp = cipher_lines or find_cipher_lines(base, *search)
    cl = read_cipher_lines(clp) if clp else None
    res = []
    res.append(check_template(html)[:2])
    res.append(check_answerable(data))
    ok3, m3, flags = check_lines(data, imgs, scale, cl)
    res.append((ok3, m3 + (f' [list: {os.path.relpath(clp)}]' if clp else '')))
    out = sheet or (os.path.splitext(page)[0] + '.preflight.png' if page else os.path.join(base, 'preflight.png'))
    res.append(contact_sheet(data, imgs, scale, out, flags, seed))
    if expect_owner:
        acct = os.environ.get('CIPHERLAB_ACCOUNT', '')
        res.append((acct == 'owner', f'account: CIPHERLAB_ACCOUNT={acct or "unset"}' +
                    ('' if acct == 'owner' else ' -- publish from the owner account, or the owner cannot open it (ASKS 145)')))
    ok = all(r[0] is not False for r in res)
    lines = [('PASS ' if r[0] else 'n/a  ' if r[0] is None else 'FAIL ') + r[1] for r in res]
    partial = [w for w, gone in (('template', html is None), ('ink, strip-height, contact sheet', not imgs)) if gone]
    lines.append(f'preflight: {"PASS" if ok else "FAIL"}' + (f' (not checked: {"; ".join(partial)})' if partial else ''))
    if not quiet:
        print('\n'.join(lines))
    return ok, lines


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0], formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=__doc__.split('\n', 2)[2])
    ap.add_argument('page', nargs='?', help='the built sorter page (HTML)')
    ap.add_argument('--inputs', help='instead of a page: a folder with signs.tsv, labels.tsv, focus.tsv [, pages/]')
    ap.add_argument('--cipher-lines', help='the cipher-line list (ids, optional x0 x1); default cipher_lines.tsv or segment_pages.txt beside the page/inputs')
    ap.add_argument('--expect-owner-account', action='store_true')
    ap.add_argument('--sheet', help='contact sheet path (default <page stem>.preflight.png)')
    ap.add_argument('--seed', type=int, default=20261006)
    a = ap.parse_args(argv)
    if bool(a.page) == bool(a.inputs):
        ap.error('give a page or --inputs DIR')
    ok, _ = run(a.page, a.inputs, a.cipher_lines, a.expect_owner_account, a.sheet, a.seed)
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
