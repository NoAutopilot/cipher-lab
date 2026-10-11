#!/usr/bin/env python3
"""Re-render an already-built sign-sorter page on the current tools/sign_sorter/template.html.

A4-SORTFIX (5 Oct 2026): owner-facing sorter pages built before SORTER-NUDGE (4 Oct) lack "Fix the cut" and the
step-2 Place screen, and some cannot be rebuilt from the repository alone (Sicily's lines live in a scratch folder,
Juan Manuel's and Lancosme's pages need a DECODE login or a Gallica refetch). This tool takes the page HTML itself --
the published artifact read back (Artifact action read saves it) or a committed index.html -- pulls out its embedded
DATA object, <title> and lede, and renders them again with tools/sign_sorter.render(). Tiles, sids, piles, clusters,
focus questions and page strips are carried over byte for byte, so choices the owner already saved in the page's db
(keyed by sid and pile id) still apply after a republish to the same URL.

    python3 tools/sorter_rerender.py OLD.html --out NEW.html [--title T] [--lede L] [--focus-note N] [--no-focus-to-tray] [--key box|none]

--focus-to-tray (template 2026-10-09.1): the "Check these first" / "Most useful first" tiles open in the "Taken out" tray and
the page lands on step 2; --no-focus-to-tray keeps them in their piles (the old layout). The option is a page setting outside
DATA, so DATA is still carried over byte for byte. With neither flag the setting is carried over from OLD.html's own
`const OPTS = {...};` line, so a page the owner is part-way through keeps its layout on a republish; a page built before
2026-10-09.1 has no such line and gets the default, on. The run prints which source decided.

--key box (template 2026-10-09.6): the box-check key ("What to do: a key", drawn examples) under the lede, as tools/sign_sorter.py
--key box builds it; a page built without it gains it here. --key none takes it off. With neither, the old page's own setting is
kept: its OPTS 'key', or, for a page hand-patched by the 10 Oct 2026 scratch script box_key.py (a `<style id="boxKeyCss">` block
after the lede, which this re-render drops along with the rest of the old page outside DATA, title and lede), 'box'. The run
prints which source decided.

A page with a whole-page region (DATA.region.src, sign_sorter.py --region) loads that image from a file beside the page; --out into
another folder copies it there (same name, since DATA names it), and says so. If the image is not beside OLD.html either, the run
warns on stderr and exits 3 (adversarial check, 11 Oct 2026, template 09.7: a re-render into another folder quietly lost the Whole page
view, opened in Line strips, and still passed the preflight). --allow-missing-region writes the page anyway (exit 0, warned).

Exit 2 when the page carries no `const DATA = {...};` line. Offline test: tools/tests/test_sorter_rerender.py.
Scope: re-renders a page that sign_sorter.py built (any template version); it does NOT re-cut tiles or change piles,
and it must not be used on a page whose DATA a person edited by hand (it would carry the edit over unchecked).
"""
import argparse, html, json, os, re, shutil, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sign_sorter  # noqa: E402


def extract(page):
    m = re.search(r'^const DATA = (\{.*\});\s*$', page, re.M)
    if not m:
        return None
    data = json.loads(m.group(1).replace('<\\/', '</'))
    t = re.search(r'<title>(.*?)</title>', page, re.S)
    l = re.search(r'<p class="lede"[^>]*>(.*?)</p>', page, re.S)
    return data, html.unescape(t.group(1)) if t else 'Sign Sorter', html.unescape(l.group(1)) if l else ''


def page_opts(page):
    """The page options a 2026-10-09.1-or-later page carries (`const OPTS = {...};`), or None for an older page."""
    m = re.search(r'^const OPTS = (\{.*?\});', page, re.M)
    try:
        return json.loads(m.group(1)) if m else None
    except ValueError:
        return None


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('page'); ap.add_argument('--out', required=True)
    ap.add_argument('--title'); ap.add_argument('--lede'); ap.add_argument('--focus-note')
    ap.add_argument('--focus-to-tray', action=argparse.BooleanOptionalAction, default=None,
                    help='question tiles start in the "Taken out" tray, page opens on step 2 (default: as OLD.html has it; on for a page '
                    'built before 2026-10-09.1)')
    ap.add_argument('--key', choices=sign_sorter.KEYS + ('none',),
                    help='box: the box-check key under the lede; none: no key (default: as OLD.html has it)')
    ap.add_argument('--allow-missing-region', action='store_true',
                    help="write the page even when its region image (DATA.region.src) is not beside OLD.html (warned; exit 0)")
    a = ap.parse_args(argv)
    page = open(a.page, encoding='utf-8').read()
    got = extract(page)
    if not got:
        print(f'{a.page}: no "const DATA = {{...}};" line', file=sys.stderr); return 2
    data, title, lede = got
    if a.focus_note is not None:
        data['focusNote'] = a.focus_note
    old = page_opts(page)
    if a.focus_to_tray is not None:
        tray, src = a.focus_to_tray, 'the flag'
    elif old is not None and 'focusToTray' in old:
        tray, src = bool(old['focusToTray']), 'the old page'
    else:
        tray, src = True, 'the default (old page has no OPTS line)'
    if a.key is not None:
        key, ksrc = (None if a.key == 'none' else a.key), 'the flag'
    elif old is not None and old.get('key') in sign_sorter.KEYS:
        key, ksrc = old['key'], 'the old page'
    elif 'id="boxKeyCss"' in page:
        key, ksrc = 'box', 'the old page (a box_key.py patch)'
    else:
        key, ksrc = None, 'the old page' if old is not None else 'the default'
    out = sign_sorter.render(data, a.title or title, a.lede if a.lede is not None else lede, focus_to_tray=tray, key=key)
    open(a.out, 'w', encoding='utf-8').write(out)
    rc = 0
    rsrc = (data.get('region') or {}).get('src')
    if rsrc and not re.match(r'^(data:|https?:)', rsrc):
        have = os.path.join(os.path.dirname(os.path.abspath(a.page)), rsrc)
        want = os.path.join(os.path.dirname(os.path.abspath(a.out)), rsrc)
        if os.path.exists(want) and (not os.path.exists(have) or os.path.samefile(have, want)):
            print(f'region image {rsrc}: beside the new page already')
        elif os.path.exists(have):
            shutil.copyfile(have, want); print(f'region image {rsrc}: copied beside the new page (publish it with the page)')
        else:
            print(f'WARNING: region image {rsrc} is not beside {a.page}: the new page will open in Line strips, without its Whole page view',
                  file=sys.stderr)
            rc = 0 if a.allow_missing_region else 3
    n = sum(len(p['items']) for p in data['piles'])
    print(f"{len(data['piles'])} piles, {n} tiles, {len(data.get('focus', []))} focus, focus-to-tray {'on' if tray else 'off'} (from {src}), "
          f"key {key or 'none'} (from {ksrc}), {len(out) // 1024} KB -> {a.out}")
    return rc


if __name__ == '__main__':
    sys.exit(main())
