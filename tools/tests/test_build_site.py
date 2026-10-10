#!/usr/bin/env python3
"""Offline test for research/mockups/site/build_site.py (SITE-SHIP-1, 10 Oct 2026).

Builds the whole private preview site into a temp dir from the repository's own status.json and audit files, then checks:
  - every internal href/src on every page resolves to a file in the build (anchors '#x' must exist on the target page), except a
    portrait named in assets/portraits/manifest.tsv that the desk runner has not dropped yet (its placeholder shows; counted);
  - every page carries the top bar (all seven entries), the footer line, and a breadcrumb unless it is the front door;
  - every item page has prev/next where it should, and the display items carry "Back to the display";
  - each display page links to at least one item page ("See the evidence");
  - no leading-slash path, no remote script, and no rule-10 phrase in any page the site writes itself (the front door, displays,
    browse pages, sitemap); phrases inside an item page's quoted audit log are reported by the builder, not failed here;
  - an --out or --preview under docs/ is refused;
  - (SITE-ITEMS-1) every item page carries the four sections in the display's order (What it says, The reading, Who where when,
    How we know) inside an <article data-interest=...>; a "Context" slot appears only where data-interest is 2 or 3; the
    English-pending marker count and the people-index size are reported; every people/ page is reachable from people/index.html.
Must catch: a broken relative link after a path change; a page missing the shell. Must NOT block: external https links, data: URIs,
mailto, and in-page anchors. Run: python3 tools/tests/test_build_site.py
"""
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT = os.path.join(ROOT, "research", "mockups", "site", "build_site.py")
NAV = ["Exhibit", "All readings", "By century", "By archive", "By language", "How to read", "People", "Credits"]
SECTIONS = ["what-it-says", "reading", "who", "how"]
LINK = re.compile(r'(?:href|src)="([^"]+)"')
IDS = re.compile(r'\bid="([^"]+)"')


def fail(msg):
    print("FAIL:", msg)
    sys.exit(1)


def main():
    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, "site")
        prev = os.path.join(tmp, "preview.html")
        r = subprocess.run([sys.executable, SCRIPT, "--out", out, "--preview", prev, "--date", "1 January 2000"],
                           capture_output=True, text=True, cwd=ROOT)
        if r.returncode:
            fail("build failed: " + r.stderr[-800:])
        print(r.stdout.strip().splitlines()[0])
        pages = [os.path.relpath(os.path.join(dp, f), out) for dp, _, fs in os.walk(out) for f in fs if f.endswith(".html")]
        if len(pages) < 10 or "index.html" not in pages or "sitemap.html" not in pages:
            fail(f"too few pages or front door/sitemap missing: {len(pages)}")
        ids = {p: set(IDS.findall(open(os.path.join(out, p), encoding="utf-8").read())) for p in pages}
        broken, checked, pending = [], 0, set()
        mani = open(os.path.join(out, "assets", "portraits", "manifest.tsv"), encoding="utf-8").read()
        sitemap = open(os.path.join(out, "sitemap.html"), encoding="utf-8").read()
        for p in pages:
            txt = open(os.path.join(out, p), encoding="utf-8").read()
            for n in NAV:
                if f">{n}</a>" not in txt:
                    fail(f"{p}: top bar lacks {n!r}")
            if "Private preview, 1 January 2000." not in txt or "Nothing here is called first, new or unpublished." not in txt:
                fail(f"{p}: footer line missing")
            if p != "index.html" and 'class="crumbs"' not in txt:
                fail(f"{p}: breadcrumb missing")
            if re.search(r'<script[^>]+src=', txt):
                fail(f"{p}: remote or external script")
            if f'href="{p}"' not in sitemap and p != "sitemap.html":
                fail(f"sitemap does not list {p}")
            for u in LINK.findall(txt):
                if re.match(r"(?:https?:|data:|mailto:)", u):
                    continue
                if u.startswith("/"):
                    fail(f"{p}: leading-slash path {u}")
                path, _, frag = u.partition("#")
                tgt = os.path.normpath(os.path.join(os.path.dirname(p), path)) if path else p
                checked += 1
                if not os.path.exists(os.path.join(out, tgt)):
                    # a portrait the desk runner has not dropped yet: allowed only if manifest.tsv names the file (placeholder shows)
                    if tgt.startswith("assets/portraits/") and "\t" + os.path.basename(tgt) in mani:
                        pending.add(os.path.basename(tgt))
                    else:
                        broken.append((p, u))
                elif frag and tgt.endswith(".html") and frag not in ids.get(tgt, set()):
                    broken.append((p, u))
            if p.startswith("items/"):
                if 'rel="next"' not in txt and 'rel="prev"' not in txt:
                    fail(f"{p}: no prev/next")
            if p.startswith("exhibit/") and "See the evidence" not in txt:
                fail(f"{p}: no 'See the evidence' links")
        pend_en, tiers = 0, {}
        for p in pages:
            if not p.startswith("items/"):
                continue
            txt = open(os.path.join(out, p), encoding="utf-8").read()
            m = re.search(r'<article data-interest="([^"]+)"', txt)
            if not m:
                fail(f"{p}: no <article data-interest>")
            tiers[m.group(1)] = tiers.get(m.group(1), 0) + 1
            pos = [txt.find(f'<section class="part" id="{s_}">') for s_ in SECTIONS]
            if min(pos) < 0 or pos != sorted(pos):
                fail(f"{p}: the four sections are missing or out of order: {dict(zip(SECTIONS, pos))}")
            has_ctx = 'id="context"' in txt
            if has_ctx != (m.group(1) in ("2", "3")):
                fail(f"{p}: Context slot {'present' if has_ctx else 'absent'} at interest {m.group(1)}")
            pend_en += txt.count('data-pending="english"')
        people = [p for p in pages if p.startswith("people/") and p != "people/index.html"]
        pidx = open(os.path.join(out, "people", "index.html"), encoding="utf-8").read()
        for p in people:
            if f'href="{os.path.basename(p)}"' not in pidx:
                fail(f"people/index.html does not list {p}")
        backs = sum("Back to the display" in open(os.path.join(out, p), encoding="utf-8").read() for p in pages if p.startswith("items/"))
        if backs < 3:
            fail(f"only {backs} item pages carry 'Back to the display'")
        if broken:
            fail(f"{len(broken)} broken internal links, e.g. {broken[:5]}")
        sys.path.insert(0, os.path.dirname(SCRIPT))
        import build_site as S
        own = [h for h in S.rule10_hits(out) if not h[0].startswith("items/") and h[0] not in ("how-to-read.html",)]
        if own:
            fail(f"rule-10 phrase in a site-written page: {own[:3]}")
        # the preview's item links resolve relative to its own folder
        ptxt = open(prev, encoding="utf-8").read()
        for u in LINK.findall(ptxt):
            if re.match(r"(?:https?:|data:|mailto:|#)", u):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(tmp, u.partition("#")[0]))):
                fail(f"preview: broken link {u}")
        for bad in (["--out", os.path.join(ROOT, "docs", "x")], ["--out", out, "--preview", os.path.join(ROOT, "docs", "p.html")]):
            r = subprocess.run([sys.executable, SCRIPT] + bad, capture_output=True, text=True, cwd=ROOT)
            if r.returncode == 0 or "refused" not in (r.stderr + r.stdout):
                fail(f"docs/ not refused for {bad}")
        print(f"ok: {len(pages)} pages, {checked} internal links checked, 0 broken; {backs} item pages link back to a display; "
              f"docs/ refused; {len(pending)} portrait files pending (placeholders)")
        print(f"ok: item pages carry the four sections; English pending on {pend_en} item pages; people index {len(people)} pages; "
              "interest tiers " + ", ".join(f"{k}: {v}" for k, v in sorted(tiers.items())))


if __name__ == "__main__":
    main()
