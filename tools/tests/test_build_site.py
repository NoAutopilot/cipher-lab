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
  - an --out or --preview under docs/ is refused without --public (docs/readings included);
  - (--public, 10 Oct 2026) with --public only an --out under docs/readings/ is accepted: docs/ itself, docs/x, docs/readingsX,
    a path outside docs/ and any --preview are refused; the public build (made in-process with the module's DOCS pointed at a temp
    folder, so the test never writes the real docs/) carries no "Private preview" banner or footer on any page, carries the public
    note and the repository link on every page, resolves every internal link, and shows no held curator paragraph while
    data/context_approved is absent;
  - (READINGS-PUBLIC, 11 Oct 2026, the three-lens audit) the public build copies no holder crop (no assets/exhibit-img or
    assets/cat-img, no <img> pointing there) and no page says "mock-up", "before any publication", "never copied", "ASKS row" or a
    credential variable name; credits say the holders' images are not reproduced; every quoted safe sentence is free of placeholders
    ("<print, page>", "[or: ...]", "page as above"), no safe sentence is quoted on two item pages, no N3+ reading page quotes a
    sentence saying the text is "already in print", "plain text is known" or "text printed in"; no claim or h1 claims more depth than
    the page's depth badge; a key-to-known-text item carries the "Key N" and "text N" badges; the count card no longer says "read
    in full" and the lede no longer promises two audits for every entry; the Torgau display no longer says "what is not in print";
  - (SITE-ITEMS-1) every item page carries the four sections in the display's order (What it says, The reading, Who where when,
    How we know) inside an <article data-interest=...>; a "Context" slot appears only where data-interest is 2 or 3; the
    English-pending marker count and the people-index size are reported; every people/ page is reachable from people/index.html;
  - (SITE-ITEMS-3) a page never shows another item's signs: every token table's data-item equals the page's own file name, no two
    item pages in one folder show the same table lines, and four known cases hold (Manteuffel frames 0390/0485/0214 have no rows in
    the shared table, so no table; Baluze 170 f.228 and f.229 each show their own per-folio table).
Must catch: a broken relative link after a path change; a page missing the shell; a shared token table shown whole on a sibling's
page. Must NOT block: external https links, data: URIs,
mailto, and in-page anchors. Run: python3 tools/tests/test_build_site.py
"""
import html
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


TOKENS = re.compile(r'<div class="tokens" data-item="([^"]*)" data-folder="([^"]*)" data-file="([^"]*)" data-lines="([^"]*)"')
H1 = re.compile(r"<h1>(.*?)</h1>", re.S)
KNOWN = [("frame 0390", None), ("frame 0485", None), ("frame 0214", None),
         ("Baluze 170 f.228r-v", "reading_tokens_b170f228.tsv"), ("Baluze 170 f.229r-v", "reading_tokens_b170f229.tsv")]


def check_tokens(out, items_dir="items"):
    """SITE-ITEMS-3: token tables belong to the page they sit on. Returns the number of tables checked."""
    seen, n, titles = {}, 0, {}
    d = os.path.join(out, items_dir)
    for f in sorted(os.listdir(d)):
        txt = open(os.path.join(d, f), encoding="utf-8").read()
        h = H1.search(txt)
        titles[f] = html.unescape(h.group(1)) if h else ""
        for item, folder, tf, lines in TOKENS.findall(txt):
            n += 1
            if item != f[:-5]:
                fail(f"items/{f}: token table belongs to {item!r}, not this page")
            key = (folder, tf, lines)
            if lines and key in seen:
                fail(f"items/{f}: shows the same table lines as items/{seen[key]} ({tf}: {lines[:60]})")
            seen[key] = f
        titles[f] = (titles[f], [m[2] for m in TOKENS.findall(txt)])
    for sub, want in KNOWN:
        hit = [v for k, v in titles.items() if sub in v[0]]
        if len(hit) != 1:
            fail(f"known case {sub!r}: {len(hit)} item pages carry it in their title")
        got = hit[0][1]
        if (want is None and got) or (want is not None and got != [want]):
            fail(f"known case {sub!r}: token table {got}, expected {want or 'none'}")
    return n


def link_problems(out, pages):
    """(broken [(page, url)], links checked, pending portrait files) over every internal href/src of `pages` under `out`."""
    ids = {p: set(IDS.findall(open(os.path.join(out, p), encoding="utf-8").read())) for p in pages}
    mani_p = os.path.join(out, "assets", "portraits", "manifest.tsv")
    mani = open(mani_p, encoding="utf-8").read() if os.path.exists(mani_p) else ""
    broken, checked, pending = [], 0, set()
    for p in pages:
        for u in LINK.findall(open(os.path.join(out, p), encoding="utf-8").read()):
            if re.match(r"(?:https?:|data:|mailto:)", u):
                continue
            if u.startswith("/"):
                broken.append((p, u + " (leading slash)"))
                continue
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
    return broken, checked, pending


def html_pages(out):
    return [os.path.relpath(os.path.join(dp, f), out) for dp, _, fs in os.walk(out) for f in fs if f.endswith(".html")]


def held_paragraphs():
    """The curator paragraphs' own text (context column, 40+ characters), which must not appear before approval."""
    p = os.path.join(os.path.dirname(SCRIPT), "data", "context_paragraphs.tsv")
    out = []
    for ln in open(p, encoding="utf-8") if os.path.exists(p) else []:
        c = ln.rstrip("\n").split("\t")
        if len(c) >= 4 and c[0] != "item" and not c[0].startswith("#") and len(c[2]) >= 40:
            out.append(html.escape(c[2][:80]))
    return out


def check_public(S, tmp):
    """--public: path rules (subprocess, real docs/), then one in-process build into a temp docs/readings."""
    docs = os.path.join(ROOT, "docs")
    for bad in (["--out", docs], ["--out", os.path.join(docs, "x")], ["--out", os.path.join(docs, "readingsX")],
                ["--out", os.path.join(tmp, "elsewhere")],
                ["--out", os.path.join(docs, "readings"), "--preview", os.path.join(tmp, "p.html")]):
        r = subprocess.run([sys.executable, SCRIPT, "--public"] + bad, capture_output=True, text=True, cwd=ROOT)
        if r.returncode == 0 or "refused" not in (r.stderr + r.stdout):
            fail(f"--public did not refuse {bad}")
    if S.path_refusal(os.path.join(docs, "readings"), "", True) or S.path_refusal(os.path.join(docs, "readings", "sub"), "", True):
        fail("--public refuses docs/readings")
    S.DOCS, S.READINGS = os.path.join(tmp, "docs"), os.path.join(tmp, "docs", "readings")
    out = S.READINGS
    if S.main(["--public", "--out", out, "--date", "2 January 2000"]):
        fail("public build failed")
    pages = html_pages(out)
    held = held_paragraphs()
    for p in pages:
        txt = open(os.path.join(out, p), encoding="utf-8").read()
        if "Private preview" in txt or 'class="mock">Private preview' in txt:
            fail(f"public {p}: private-preview banner or footer still present")
        if S.E(S.PUBLIC_NOTE.split(" see ")[0]) not in txt or f'href="{S.REPO_URL}"' not in txt:
            fail(f"public {p}: public note or repository link missing")
        if "Built 2 January 2000." not in txt:
            fail(f"public {p}: footer date missing")
        for n in NAV:
            if f">{n}</a>" not in txt:
                fail(f"public {p}: top bar lacks {n!r}")
        if not os.path.exists(os.path.join(os.path.dirname(SCRIPT), "data", "context_approved")):
            for h in held:
                if h in txt:
                    fail(f"public {p}: shows a held curator paragraph")
    broken, checked, _pending = link_problems(out, pages)
    if broken:
        fail(f"public: {len(broken)} broken internal links, e.g. {broken[:5]}")
    nq = check_public_claims(S, out, pages)
    print(f"ok: --public refuses docs/, docs/x, docs/readingsX, a path outside docs/ and --preview; accepts docs/readings; "
          f"{len(pages)} public pages carry the note and repository link, no private banner, {checked} internal links 0 broken, "
          f"{len(held)} held curator paragraphs absent; no holder crop copied; {nq} quoted safe sentences pass the claim checks")


BANNED = re.compile(r"mock-up|before any publication|never copied|what is not in print|\bASKS\b|SITE-ITEMS|"
                    r"\$?\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)*_(?:KEY|PASS|USER|TOKEN|SECRET)\b")
PLACEHOLDER = re.compile(r"&lt;[^&]{1,40}&gt;|\[or:|page as above")
IN_PRINT = re.compile(r"already in print|plain ?text is known|text printed in", re.I)
CLAIM = re.compile(r'<blockquote class="claim">(.*?)</blockquote><p class="small">(.*?)</p>', re.S)


def check_public_claims(S, out, pages):
    """The three-lens audit's checks on the public build (rights, claims, privacy minors). Returns quoted safe sentences checked."""
    C = S.C
    a = os.path.join(out, "assets")
    for d in S.HOLDER_IMG_DIRS:
        if os.path.exists(os.path.join(a, d)):
            fail(f"public: holder crops copied into assets/{d}")
    depth_of = {w: d for d, w in C.DEPTH_WORDS.items()}
    quoted, n = {}, 0
    for p in pages:
        txt = open(os.path.join(out, p), encoding="utf-8").read()
        if re.search(r'<img[^>]+src="[^"]*(?:exhibit-img|cat-img)/', txt):
            fail(f"public {p}: embeds a holder crop")
        body = re.sub(r"<(style|script)[^>]*>.*?</\1>", "", txt, flags=re.S)
        m = BANNED.search(re.sub(r"<[^>]+>", " ", body))
        if m:
            fail(f"public {p}: says {m.group(0)!r}")
        if not p.startswith("items/"):
            continue
        how = txt[txt.find('id="how"'):]
        c = CLAIM.search(how)
        if not c:
            fail(f"public {p}: no claim in How we know")
        claim, note = c.group(1), c.group(2)
        badges = re.findall(r'class="badge"[^>]*>([^<]*)<', how)
        dep = next((depth_of[b.split(" (")[0]] for b in badges if b.split(" (")[0] in depth_of), None)
        h1 = html.unescape(re.sub(r"<[^>]+>", "", H1.search(txt).group(1)))
        for what, t in (("claim", html.unescape(re.sub(r"<[^>]+>", "", claim))), ("h1", h1)):
            cd = C.claimed_depth(t)
            if dep is not None and cd is not None and cd > dep:
                fail(f"public {p}: {what} claims D{cd} words on a D{dep} page: {t[:120]!r}")
        if any(b.startswith("text N") for b in badges) and not any(b.startswith("Key N") for b in badges):
            fail(f"public {p}: text class shown without the key class")
        if "quoted from AUDIT.md" not in note:
            continue
        n += 1
        if PLACEHOLDER.search(claim):
            fail(f"public {p}: quoted safe sentence carries a placeholder: {claim[:120]!r}")
        if claim in quoted:
            fail(f"public {p}: quotes the same safe sentence as {quoted[claim]}")
        quoted[claim] = p
        nb = next((int(b[1]) for b in badges if re.match(r"N[0-5] ", b)), None)
        if nb is not None and nb >= 3 and IN_PRINT.search(claim):
            fail(f"public {p}: N{nb} page quotes a sentence saying the text is known: {claim[:120]!r}")
    keys = [it for it in S.load()[0] if it["cls"] == "key"]
    for it in keys:
        if "Key N" not in open(os.path.join(out, "items", it["file"]), encoding="utf-8").read():
            fail(f"public items/{it['file']}: key item lacks its Key N badge")
    idx = open(os.path.join(out, "index.html"), encoding="utf-8").read()
    if "read in full" in idx or "the two independent audits" in idx:
        fail("public index: count card or lede over-claims")
    cr = open(os.path.join(out, "credits.html"), encoding="utf-8").read()
    if "not reproduced on this site" not in cr:
        fail("public credits: holders' images not said to be linked, not reproduced")
    return n


def main():
    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, "site")
        prev = os.path.join(tmp, "preview.html")
        r = subprocess.run([sys.executable, SCRIPT, "--out", out, "--preview", prev, "--date", "1 January 2000"],
                           capture_output=True, text=True, cwd=ROOT)
        if r.returncode:
            fail("build failed: " + r.stderr[-800:])
        print(r.stdout.strip().splitlines()[0])
        pages = html_pages(out)
        if len(pages) < 10 or "index.html" not in pages or "sitemap.html" not in pages:
            fail(f"too few pages or front door/sitemap missing: {len(pages)}")
        broken, checked, pending = link_problems(out, pages)
        sitemap = open(os.path.join(out, "sitemap.html"), encoding="utf-8").read()
        for p in pages:
            txt = open(os.path.join(out, p), encoding="utf-8").read()
            for n in NAV:
                if f">{n}</a>" not in txt:
                    fail(f"{p}: top bar lacks {n!r}")
            if "Private preview, 1 January 2000." not in txt or "Nothing here is called first, new or unpublished." not in txt:
                fail(f"{p}: footer line missing")
            if "Private preview for review. Not published, not linked from anywhere." not in txt:
                fail(f"{p}: private-preview banner missing without --public")
            if p != "index.html" and 'class="crumbs"' not in txt:
                fail(f"{p}: breadcrumb missing")
            if re.search(r'<script[^>]+src=', txt):
                fail(f"{p}: remote or external script")
            if f'href="{p}"' not in sitemap and p != "sitemap.html":
                fail(f"sitemap does not list {p}")
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
        for bad in (["--out", os.path.join(ROOT, "docs", "x")], ["--out", os.path.join(ROOT, "docs", "readings")],
                    ["--out", out, "--preview", os.path.join(ROOT, "docs", "p.html")]):
            r = subprocess.run([sys.executable, SCRIPT] + bad, capture_output=True, text=True, cwd=ROOT)
            if r.returncode == 0 or "refused" not in (r.stderr + r.stdout):
                fail(f"docs/ not refused for {bad}")
        print(f"ok: {len(pages)} pages, {checked} internal links checked, 0 broken; {backs} item pages link back to a display; "
              f"docs/ refused; {len(pending)} portrait files pending (placeholders)")
        print(f"ok: item pages carry the four sections; English pending on {pend_en} item pages; people index {len(people)} pages; "
              "interest tiers " + ", ".join(f"{k}: {v}" for k, v in sorted(tiers.items())))
        print(f"ok: {check_tokens(out)} token tables each on their own item page; known cases {len(KNOWN)}/{len(KNOWN)}")
        flag = os.path.join(os.path.dirname(SCRIPT), "data", "context_approved")
        held = sum('data-pending="context"' in open(os.path.join(out, "items", f), encoding="utf-8").read()
                   for f in os.listdir(os.path.join(out, "items")))
        if not os.path.exists(flag) and held != tiers.get("2", 0) + tiers.get("3", 0):
            fail(f"curator paragraphs shown before data/context_approved exists ({held} slots held)")
        print(f"ok: Context slots held {held} (flag {'present' if os.path.exists(flag) else 'absent'})")
        check_public(S, tmp)


if __name__ == "__main__":
    main()
