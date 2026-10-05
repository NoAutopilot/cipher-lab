#!/usr/bin/env python3
"""Re-render an already-built sign-sorter page on the current tools/sign_sorter/template.html.

A4-SORTFIX (5 Oct 2026): owner-facing sorter pages built before SORTER-NUDGE (4 Oct) lack "Fix the cut" and the
step-2 Place screen, and some cannot be rebuilt from the repository alone (Sicily's lines live in a scratch folder,
Juan Manuel's and Lancosme's pages need a DECODE login or a Gallica refetch). This tool takes the page HTML itself --
the published artifact read back (Artifact action read saves it) or a committed index.html -- pulls out its embedded
DATA object, <title> and lede, and renders them again with tools/sign_sorter.render(). Tiles, sids, piles, clusters,
focus questions and page strips are carried over byte for byte, so choices the owner already saved in the page's db
(keyed by sid and pile id) still apply after a republish to the same URL.

    python3 tools/sorter_rerender.py OLD.html --out NEW.html [--title T] [--lede L] [--focus-note N]

Exit 2 when the page carries no `const DATA = {...};` line. Offline test: tools/tests/test_sorter_rerender.py.
Scope: re-renders a page that sign_sorter.py built (any template version); it does NOT re-cut tiles or change piles,
and it must not be used on a page whose DATA a person edited by hand (it would carry the edit over unchecked).
"""
import argparse, html, json, os, re, sys

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


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('page'); ap.add_argument('--out', required=True)
    ap.add_argument('--title'); ap.add_argument('--lede'); ap.add_argument('--focus-note')
    a = ap.parse_args(argv)
    got = extract(open(a.page, encoding='utf-8').read())
    if not got:
        print(f'{a.page}: no "const DATA = {{...}};" line', file=sys.stderr); return 2
    data, title, lede = got
    if a.focus_note is not None:
        data['focusNote'] = a.focus_note
    out = sign_sorter.render(data, a.title or title, a.lede if a.lede is not None else lede)
    open(a.out, 'w', encoding='utf-8').write(out)
    n = sum(len(p['items']) for p in data['piles'])
    print(f"{len(data['piles'])} piles, {n} tiles, {len(data.get('focus', []))} focus, {len(out) // 1024} KB -> {a.out}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
