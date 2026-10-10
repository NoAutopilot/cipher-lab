#!/usr/bin/env python3
"""build_site.py -- one private preview site: the exhibit as the front door, the full catalogue behind it (SITE-SHIP-1, 10 Oct 2026).

PRIVATE MOCK-UP. Nothing this writes is published; the owner decides later whether and where (owner, 10 Oct 2026 01:0x UTC: "ship the
rest, along with useful navigation"). Writing under docs/ (the GitHub Pages folder) is refused, as tools/build_catalogue.py refuses it.

It calls the two approved builders rather than copying them: tools/build_catalogue.py (items, index, item pages, how-to-read, credits,
readings worth attention) and research/mockups/exhibit/build_exhibit2.py (the three displays). This script adds only the site shell:
one top bar on every page, breadcrumbs, prev/next in catalogue order, "Back to the display" and "See the evidence" cross-links, a text
filter on All readings, three browse pages (century, holding archive, language), a sitemap and a footer.

Outputs (default --out research/mockups/site/): index.html (front door: three displays with their three-layer lines, then All readings),
exhibit/<slug>.html, items/<file>.html, all-readings.html, browse/{century,archive,language}.html, attention.html, how-to-read.html,
credits.html, sitemap.html, assets/ (exhibit crops, catalogue crops, portraits copied from research/mockups/exhibit/portraits/ at build
time, so files the desk runner drops there fill the faces on the next build). With --preview FILE, one self-contained page (front door
with images embedded; item links relative into the site folder). All paths relative, none with a leading slash.

Usage: python3 research/mockups/site/build_site.py [--out DIR] [--preview FILE] [--date "10 October 2026"]
"""
import argparse
import base64
import html
import json
import os
import re
import shutil
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, os.path.join(ROOT, "research", "mockups", "exhibit"))
os.chdir(ROOT)  # both builders read repository-relative paths
import build_catalogue as C  # noqa: E402
import build_exhibit2 as X  # noqa: E402

B = X.B
E = html.escape
EXHIBIT_DIR = os.path.join(ROOT, "research", "mockups", "exhibit")
CAT_IMG = os.path.join(ROOT, "research", "mockups", "catalogue", "img")

# Which catalogue items each display rests on (title substrings, all must match). The first is the display's main item.
DISPLAY_ITEMS = {
    "washington-1864": [("to John A. Kennedy", "30 Nov 1864"), ("C. A. Dana to Wallace", "7 Nov 1864"),
                        ("Turner for the Secretary of War to Dix", "26 May 1864")],
    "breda-torgau-1561": [("Elector August to Orange, Torgau 18 Nov 1561",), ("WVO 53",)],
    "berlin-1712": [("frame 0391",)],
}
# Language where the catalogue loader finds none in specs/: taken from what the display builders show the reading in (Eckert:
# English code words; Manteuffel and Gramont: French; August: German) or from the spec's own free-text "language" field. Everything
# else is "not recorded", never guessed.
LANG_FALLBACK = {"eckert-1864": "English", "eckert-1862": "English", "sachsstaatsarchiv-manteuffel-1712": "French",
                 "august-van-saksen-1561-64": "German", "fr2980-gramont": "French"}
FORBIDDEN = re.compile(r"first decipherment|previously unread|newly (?:recovered|read|deciphered)|\bunpublished\b|never (?:been )?printed",
                       re.I)

CAVEAT = re.compile(r"(?:internal or )?unpublished (?:or archival )?work (?:is )?not excluded", re.I)

SITE_CSS = """
nav.site{font:14px/1.4 system-ui,sans-serif;display:flex;gap:6px 14px;flex-wrap:wrap;align-items:center;padding:10px 0;
 border-bottom:2px solid var(--rule)}
nav.site a{text-decoration:none;padding:2px 0}nav.site a[aria-current=page]{font-weight:700;border-bottom:2px solid currentColor}
nav.site .brand{font-weight:700;margin-right:6px;color:inherit}
.crumbs{font:13px/1.4 system-ui,sans-serif;color:var(--muted);margin:10px 0 0}.crumbs a{color:inherit}
.pager{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;font:14px/1.4 system-ui,sans-serif;margin:16px 0;
 padding:10px 0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.pager a{max-width:46%}.pager .mid{text-align:center}
.backlink{font:14px system-ui,sans-serif;border:1px solid var(--rule);border-left:4px solid var(--accent2);padding:8px 12px;margin:12px 0}
.evidence{font:14px/1.5 system-ui,sans-serif;border:1px solid var(--rule);border-left:4px solid var(--accent);padding:8px 14px;margin:18px 0}
.evidence ul{margin:6px 0 0;padding-left:20px}
footer.site{font:12px/1.5 system-ui,sans-serif;color:var(--muted);border-top:1px solid var(--rule);margin-top:40px;padding-top:10px}
.qf{font:inherit;padding:4px 8px;min-width:260px;max-width:100%}
ul.browse{list-style:none;padding:0}ul.browse li{margin:8px 0;padding:6px 0;border-bottom:1px solid var(--rule)}
ul.browse .one{display:block;color:var(--muted);font-size:.95em}
.toc{font:14px system-ui,sans-serif;display:flex;flex-wrap:wrap;gap:6px 14px}
.door{border-top:3px double var(--rule);margin-top:36px;padding-top:6px}
.dsum{border:1px solid var(--rule);padding:10px 14px;margin:16px 0}
@media (max-width:560px){.qf{min-width:0;width:100%}.pager a{max-width:100%}}
"""

TEXT_FILTER_JS = """<script>
(function(){var q=document.getElementById('q'),f=document.querySelectorAll('select[data-f]');
function go(){var v={},t=(q&&q.value||'').toLowerCase().split(/\\s+/).filter(Boolean),n=0;f.forEach(function(s){v[s.dataset.f]=s.value});
document.querySelectorAll('tr[data-century]').forEach(function(r){var txt=(r.dataset.text||r.textContent).toLowerCase();
var ok=Object.keys(v).every(function(k){return !v[k]||r.dataset[k]===v[k]})&&t.every(function(w){return txt.indexOf(w)>=0});
r.hidden=!ok;if(ok)n++});var s=document.getElementById('shown');if(s)s.textContent=n}
f.forEach(function(s){s.addEventListener('change',go)});if(q)q.addEventListener('input',go);})();
</script>"""

NAV = [("index.html", "Exhibit"), ("all-readings.html", "All readings"), ("browse/century.html", "By century"),
       ("browse/archive.html", "By archive"), ("browse/language.html", "By language"), ("how-to-read.html", "How to read"),
       ("people/index.html", "People"), ("credits.html", "Credits")]


def top_bar(prefix, current):
    return ('<nav class="site" aria-label="Site"><a class="brand" href="%sindex.html">What the cipher said</a>' % prefix
            + "".join(f'<a href="{prefix}{h}"{" aria-current=page" if t == current else ""}>{E(t)}</a>' for h, t in NAV) + "</nav>")


def crumbs(prefix, trail):
    parts = [f'<a href="{prefix}index.html">Home</a>'] + [f'<a href="{prefix}{h}">{E(t)}</a>' if h else E(t) for t, h in trail]
    return '<p class="crumbs">' + " &rsaquo; ".join(parts) + "</p>"


def footer(date, prefix):
    return (f'<footer class="site">Private preview, {E(date)}. Readings graded per CLAUDE.md rule 4; novelty classes per rule 10 '
            '(verifier\'s verdict). Nothing here is called first, new or unpublished. '
            f'<a href="{prefix}sitemap.html">Sitemap</a></footer>')


def shell(title, body, prefix, current, trail, date, desc="", exhibit=False):
    """The one wrapper every page uses. Catalogue CSS first, exhibit CSS after (exhibit pages only), site CSS last."""
    css = C.CSS + C.CSS_V2 + ((B.CSS + X.CSS2) if exhibit else "") + SITE_CSS + ITEM_CSS
    js = f"<script>{B.JS}</script>" if exhibit else ""
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{E(title)}</title>' + (f'<meta name="description" content="{E(desc)}">' if desc else "")
            + f'<style>{css}</style></head><body><main>{top_bar(prefix, current)}{crumbs(prefix, trail) if trail else ""}'
            '<p class="mock">Private preview for review. Not published, not linked from anywhere.</p>'
            f'{body}{footer(date, prefix)}</main>{js}</body></html>\n')


def load():
    st = json.load(open("status.json", encoding="utf-8"))
    results, targets = st.get("results", []), st.get("targets", [])
    ns = C.board_rules()
    items = C.build_items(results, ns)
    per = {}
    for it in items:
        per[it["folder"]] = per.get(it["folder"], 0) + 1
    _cache["per_folder"] = per
    rd = {}
    for it in items:
        rd[it.get("reading")] = rd.get(it.get("reading"), 0) + 1
    _cache["per_reading"] = rd
    for it in items:
        if not it["lang"]:
            it["lang"] = LANG_FALLBACK.get(it["folder"]) or spec_language(it["folder"])
    return items, ns, results, targets


def spec_language(fold):
    for p in sorted(os.listdir("specs")) if os.path.isdir("specs") else []:
        if not p.endswith(".json"):
            continue
        try:
            sp = json.load(open(os.path.join("specs", p), encoding="utf-8"))
        except (ValueError, OSError):
            continue
        if fold not in json.dumps(sp.get("source", "")) + json.dumps(sp.get("folder", "")) + json.dumps(sp.get("target", "")):
            continue
        m = re.match(r"\s*(Italian|French|German|Spanish|Portuguese|English|Latin|Dutch)\b", str(sp.get("language") or ""))
        if m:
            return m.group(1)
    return ""


def find_item(items, subs):
    return next((it for it in items if all(s.lower() in it["title"].lower() for s in subs)), None)


def display_map(items):
    out = {}
    for slug, wants in DISPLAY_ITEMS.items():
        got = [find_item(items, w) for w in wants]
        out[slug] = [g for g in got if g]
    return out


def selection_lines():
    """item quote from SELECTION.md's table (column 'the one thing the reading says'), keyed by its own text."""
    p = os.path.join(EXHIBIT_DIR, "SELECTION.md")
    quotes = []
    for line in open(p, encoding="utf-8") if os.path.exists(p) else []:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 7 and cells[0].isdigit():
            m = re.search(r'"([^"]{20,})"', cells[6])
            if m:
                quotes.append(m.group(1))
    return quotes


def one_line(it, quotes):
    gist = it["gist"] or ""
    norm = lambda s: re.sub(r"\W+", " ", s).lower().strip()
    g = norm(gist)
    for q in quotes:
        head = norm(q.split("...")[0])[:60]
        if len(head) > 25 and head in g:
            return q, "from SELECTION.md"
    return C.ten_words(gist, 30) or C.ten_words(it["title"], 14), "the depth sentence"


def century_of(it):
    y = C.year_of(it)
    return (f"{(y - 1) // 100 + 1}th century", y) if y else ("undated", None)


def copy_assets(out):
    a = os.path.join(out, "assets")
    for src, dst in ((os.path.join(EXHIBIT_DIR, "img"), "exhibit-img"), (CAT_IMG, "cat-img"),
                     (os.path.join(EXHIBIT_DIR, "portraits"), "portraits")):
        d = os.path.join(a, dst)
        if os.path.isdir(d):
            shutil.rmtree(d)
        if os.path.isdir(src):
            shutil.copytree(src, d)
        else:
            os.makedirs(d, exist_ok=True)


def emb(path):
    with open(path, "rb") as f:
        mime = "image/png" if path.endswith(".png") else "image/jpeg"
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()


def display_section(d, img, pdir, evidence_links):
    body = X.display_html(d, img, pdir)
    body = body.replace(" their pages are not shown here.", " their pages are linked under “See the evidence” below.")
    ev = ('<div class="evidence"><b>See the evidence.</b> The item pages this display rests on, each with its claim, grades, audits '
          'and links:<ul>' + "".join(f'<li><a href="{h}">{E(t)}</a></li>' for t, h in evidence_links) + "</ul></div>")
    return body.replace("<h2>Faces</h2>", ev + "<h2>Faces</h2>", 1) if "<h2>Faces</h2>" in body else body + ev


def door_html(img, href_display, href_item, dmap):
    """Front door: the exhibit intro, then each display's headline and its three-layer lines (behind a reveal)."""
    out = [X.intro(img, href_display)]
    for d in X.DISPLAYS:
        fix = [(img(s), t, a, b) for s, t, a, b in d["lines"]]
        ev = " &middot; ".join(f'<a href="{href_item(it)}">see the evidence</a>' for it in dmap.get(d["slug"], [])[:1])
        out.append(f'<div class="dsum" id="door-{d["slug"]}"><div class="kicker">{E(d["kicker"])}</div><h2 style="margin-top:4px">'
                   f'<a href="{href_display(d)}">{E(d["title"])}</a></h2><p class="headline">{E(d["headline"])}</p>'
                   f'<button data-reveal="door-r-{d["slug"]}" aria-expanded="false">Show the lines: cipher, as read, English</button>'
                   f'<div id="door-r-{d["slug"]}" class="reveal" style="margin-top:12px">{B.legend()}{X.lines_html(fix, d["lang"])}</div>'
                   f'<p class="small"><a href="{href_display(d)}">Open the display</a>' + (f" &middot; {ev}" if ev else "") + "</p></div>")
    return "".join(out)


def readings_index(items, ns, results, targets, href, inline=False):
    body = C.index_body(items, ns, results, targets, href, inline=inline)
    # one row's searchable text: sender, recipient, year, archive, language, class, depth are already its cells; add the N-class words
    box = ('<label class="small">Find <input id="q" class="qf" type="search" placeholder="sender, recipient, year, archive, '
           'language, class, depth" aria-label="Filter the readings"></label> ')
    body = body.replace('<div class="filters">', '<div class="filters">' + box, 1)
    body = body.replace(C.FILTER_JS, TEXT_FILTER_JS)
    body = body.replace("<h1>Cipher letters read from the archives</h1>", '<h1 id="all">All readings</h1>', 1)
    if not inline:
        body = body.replace('src="img/', 'src="assets/cat-img/')
    # language: the catalogue writes it from it["lang"], already filled with the fallback in load()
    return body


def browse_page(items, kind, quotes, href):
    groups = {}
    for it in items:
        if kind == "century":
            k, _ = century_of(it)
        elif kind == "archive":
            k = C.archive_of(it) or "holder not matched to an archive name"
        else:
            k = it["lang"] or "language not recorded"
        groups.setdefault(k, []).append(it)
    if kind == "century":
        order = sorted(groups, key=lambda k: (k == "undated", int(re.match(r"\d+", k).group()) if k[0].isdigit() else 0))
    else:
        order = sorted(groups, key=lambda k: (-len(groups[k]), k))
    head = {"century": "By century", "archive": "By holding archive", "language": "By language"}[kind]
    note = {"century": "Century from the year in the item's title or shelfmark.",
            "archive": "Holding archive matched from the item's shelfmark and title.",
            "language": "Language as the item's spec or its display records it; “not recorded” where neither says."}[kind]
    out = [f"<h1>{head}</h1><p class=\"small\">{note} Under each link: what the reading says, quoted from the exhibit's selection notes "
           "where they cover the item, otherwise the verifier's depth sentence (an interpretation).</p>",
           '<p class="toc">' + " ".join(f'<a href="#g{i}">{E(k)} ({len(groups[k])})</a>' for i, k in enumerate(order)) + "</p>"]
    for i, k in enumerate(order):
        lis = []
        for it in sorted(groups[k], key=lambda it: (C.year_of(it) or 9999, it["file"])):
            line, _src = one_line(it, quotes)
            lis.append(f'<li><a href="{href(it)}">{E(C.ten_words(it["title"], 16))}</a><span class="one">{E(line)}</span></li>')
        out.append(f'<h2 id="g{i}">{E(k)} <span class="small">({len(groups[k])})</span></h2><ul class="browse">{"".join(lis)}</ul>')
    return "".join(out)


def write_site(out, date):
    if os.path.abspath(out).startswith(os.path.abspath("docs") + os.sep) or os.path.abspath(out) == os.path.abspath("docs"):
        sys.exit("refused: docs/ is the GitHub Pages folder; the site is a private preview (owner, 10 Oct 2026)")
    items, ns, results, targets = load()
    dmap = display_map(items)
    item_display = {it["file"]: d for d in X.DISPLAYS for it in dmap.get(d["slug"], [])}
    quotes = selection_lines()
    for sub in ("exhibit", "items", "browse", "people"):
        os.makedirs(os.path.join(out, sub), exist_ok=True)
    copy_assets(out)
    pages = []

    def w(rel, html_):
        p = os.path.join(out, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "w", encoding="utf-8").write(html_)
        pages.append(rel)

    # front door
    door = door_html(lambda p: "assets/exhibit-" + p, lambda d: f"exhibit/{d['slug']}.html", lambda it: "items/" + it["file"], dmap)
    idx = readings_index(items, ns, results, targets, lambda it: "items/" + it["file"])
    w("index.html", shell("What the cipher said", door + f'<section class="door">{idx}</section>', "", "Exhibit", None, date,
                          "Three cipher displays, then every audited reading (private preview).", exhibit=True))
    w("all-readings.html", shell("All readings", idx, "", "All readings", [("All readings", "")], date))
    # displays
    for d in X.DISPLAYS:
        ev = [(it["title"], "../items/" + it["file"]) for it in dmap.get(d["slug"], [])]
        body = display_section(d, lambda p: "../assets/exhibit-" + p, "../assets/portraits/", ev)
        w(f"exhibit/{d['slug']}.html", shell(d["short"] + " cipher display", body, "../", "Exhibit",
                                             [("Exhibit", "index.html"), (d["short"], "")], date, d["headline"], exhibit=True))
    # items (SITE-ITEMS-1: one data-driven template)
    main_of = {dmap[d["slug"]][0]["file"]: d for d in X.DISPLAYS if dmap.get(d["slug"])}
    people, stats = {}, {"pending_en": 0, "tiers": {}}
    for i, it in enumerate(items):
        sc = C.showcase_for(it)
        dsp = main_of.get(it["file"])
        body, pend, names, sel = item_page(it, sc, dsp, "../", lambda n: "../people/" + person_slug(n) + ".html")
        stats["pending_en"] += pend
        tier = str(sel["score"]) if sel and sel["score"] is not None else "unscored"
        stats["tiers"][tier] = stats["tiers"].get(tier, 0) + 1
        for n in names:
            people.setdefault(person_slug(n), (n, []))[1].append(it)
        prev_, next_ = (items[i - 1] if i else None), (items[i + 1] if i + 1 < len(items) else None)
        pager = ('<div class="pager">'
                 + (f'<a rel="prev" href="{prev_["file"]}">&larr; {E(C.ten_words(prev_["title"], 8))}</a>' if prev_ else "<span></span>")
                 + f'<span class="mid">{i + 1} of {len(items)} &middot; <a href="../all-readings.html">All readings</a></span>'
                 + (f'<a rel="next" href="{next_["file"]}">{E(C.ten_words(next_["title"], 8))} &rarr;</a>' if next_ else "<span></span>")
                 + "</div>")
        d = item_display.get(it["file"])
        back = (f'<p class="backlink">This reading is shown in the exhibit: <a href="../exhibit/{d["slug"]}.html">Back to the display '
                f'&ldquo;{E(d["short"])}&rdquo;</a></p>') if d else ""
        w("items/" + it["file"], shell(it["title"][:80], back + pager + body + pager, "../", "All readings",
                                       [("All readings", "all-readings.html"), (C.ten_words(it["title"], 8), "")], date,
                                       exhibit=bool(dsp)))
    # people and places named in the readings
    ppages, pidx = people_pages({n: its for n, its in people.values()}, lambda it: "../items/" + it["file"])
    for slug, (n, body) in ppages.items():
        w(f"people/{slug}.html", shell(n, body, "../", "People", [("People and places", "people/index.html"), (n, "")], date))
    w("people/index.html", shell("People and places", pidx, "../", "People", [("People and places", "")], date))
    stats["people"] = len(ppages)
    # browse
    for kind, label in (("century", "By century"), ("archive", "By archive"), ("language", "By language")):
        w(f"browse/{kind}.html", shell(label, browse_page(items, kind, quotes, lambda it: "../items/" + it["file"]), "../", label,
                                       [(label, "")], date))
    # reference pages
    nw = "".join(f"<dt>N{k}</dt><dd>{E(v)}</dd>" for k, v in C.NWORDS.items())
    w("how-to-read.html", shell("How to read", C.HOWTO.format(nw=nw), "", "How to read", [("How to read", "")], date))
    w("credits.html", shell("Credits", C.CREDITS.format(keys=E(C.keys_credit(items))) + PORTRAIT_CREDIT, "", "Credits",
                            [("Credits", "")], date))
    w("attention.html", shell("Readings worth attention", C.attention_body(items, lambda it: "items/" + it["file"]), "", "",
                              [("Readings worth attention", "")], date))
    # sitemap last, listing every page including itself
    pages.append("sitemap.html")
    groups = [("Exhibit", [p for p in pages if p == "index.html" or p.startswith("exhibit/")]),
              ("Catalogue", [p for p in pages if p in ("all-readings.html", "attention.html") or p.startswith("browse/")]),
              ("Reference", [p for p in pages if p in ("how-to-read.html", "credits.html", "sitemap.html")]),
              ("Item pages (catalogue order)", [p for p in pages if p.startswith("items/")]),
              ("People and places", [p for p in pages if p.startswith("people/")])]
    titles = {"items/" + it["file"]: it["title"] for it in items}
    titles.update({f"exhibit/{d['slug']}.html": d["short"] + " (display)" for d in X.DISPLAYS})
    titles.update({f"people/{slug}.html": n for slug, (n, _b) in ppages.items()})
    sm = [f"<h1>Sitemap</h1><p class=\"small\">{len(pages)} pages.</p>"]
    for g, ps in groups:
        sm.append(f"<h2>{E(g)} ({len(ps)})</h2><ul>" + "".join(f'<li><a href="{p}">{E(titles.get(p, p))}</a></li>' for p in ps) + "</ul>")
    pages.pop()
    w("sitemap.html", shell("Sitemap", "".join(sm), "", "", [("Sitemap", "")], date))
    return items, dmap, pages, stats


# ------------------------------------------------------------------ item pages (SITE-ITEMS-1, 10 Oct 2026)
# Every item page has the displays' structure from data already on disk, with only as much story as the audited reading supports:
# (1) What it says, (2) The reading in layers, (3) Who, where, when + names linked to people/<slug>.html, (4) How we know;
# (5) the interest tier is a data attribute only (score >= 2 adds an empty "Context" slot for SITE-ITEMS-3, nothing else changes).

ENGLISH_TSV = os.path.join(HERE, "data", "english_lines.tsv")  # written by SITE-ITEMS-2: item, line id, original, english, grades, date
PENDING_EN = "English line: pending (SITE-ITEMS-2)"
ECKERT_READINGS = ("reading.md", "reading-no2.md", "reading-no9.md")
BLOCK = re.compile(r"^\*\*([A-Z0-9][A-Z0-9-]*) \| [^\n]*\*\*\n\n(.+?)\n\n(Code-word tokens:[^\n]*)", re.M | re.S)
TITLES = {"genl", "gen", "general", "maj", "major", "col", "colonel", "capt", "captain", "lt", "lieut", "brig", "adm", "admiral", "mr",
          "dr", "supt", "sec", "secy", "hon", "genl", "commander", "count", "duke", "prince", "king", "queen", "milord", "lord", "monsieur", "madame"}
NOT_NAMES = {"january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november",
             "december", "abandon", "capture", "entrench", "equip", "equipage", "fort", "gunboat", "illegible", "rail", "road",
             "reconnoissance", "repulsed", "siege", "transport", "sic", "inland", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "jan", "feb", "mar", "apr",
             "jun", "jul", "aug", "sep", "sept", "oct", "nov", "dec", "null", "clear", "the", "and", "les", "der", "die", "das", "und"}
OFFICES = {"adjt", "president", "secretary", "master", "qr", "treasury", "chief", "in", "of", "the", "war", "navy", "state"}
_cache = {}


def common_words():
    """Lower-case words seen at least twice in the English judge corpora (en, en18, en_vdrop) or once in lower case in the Eckert
    readings (the clerks' plain words, which carry the military vocabulary the novels lack): a decoded value made only of these is
    not listed as a name."""
    if "common" not in _cache:
        cnt = {}
        for sub in ("en", "en18", "en_vdrop"):
            for dp, _, fs in os.walk(os.path.join(ROOT, "tools", "data", sub)):
                for f in sorted(fs):
                    if f.endswith(".txt"):
                        for w in re.findall(r"\b[a-z]{2,}\b", open(os.path.join(dp, f), encoding="utf-8", errors="ignore").read()):
                            cnt[w] = cnt.get(w, 0) + 1
        words = {w for w, n in cnt.items() if n >= 2}
        for f in ECKERT_READINGS:
            p = os.path.join(ROOT, "ciphers", "eckert-1864", f)
            if os.path.exists(p):
                words |= set(re.findall(r"\b[a-z]{3,}\b", open(p, encoding="utf-8").read()))
        _cache["common"] = words
    return _cache["common"]


def name_like(v):
    """True for a decoded value that reads as a proper name (person or place). Conservative: a name that is also an ordinary English
    word (Grant, Butler, Post) is missed rather than a common word being listed; a rank before a capitalised word counts as a name."""
    v = re.sub(r"[\[\]?#()*]", "", v or "").strip(" .,;:")
    ws = re.findall(r"[A-Za-zÀ-ÿ]+", v)
    if not ws or not ws[0][0].isupper() or len(v) < 3 or len(v) > 40:
        return False
    low = [w.lower() for w in ws]
    if all(w in NOT_NAMES or w in TITLES or w in OFFICES or len(w) == 1 for w in low) or "illegible" in low or "sic" in low:
        return False
    for i, w in enumerate(low):
        if w in TITLES and i + 1 < len(ws) and ws[i + 1][0].isupper():
            return True
    com = common_words()
    return any(len(w) >= 3 and w not in com and w not in TITLES and w not in OFFICES and w not in NOT_NAMES
               and ws[i][0].isupper()
               for i, w in enumerate(low))


def eckert_blocks():
    """{entry id: (derived text, grade-count line, reading file)} from the decode scripts' derived blocks."""
    if "eckert" not in _cache:
        out = {}
        for f in ECKERT_READINGS:
            p = os.path.join(ROOT, "ciphers", "eckert-1864", f)
            if os.path.exists(p):
                for m in BLOCK.finditer(open(p, encoding="utf-8").read()):
                    out.setdefault(m.group(1), (m.group(2).strip(), m.group(3).strip(), f))
        _cache["eckert"] = out
    return _cache["eckert"]


def eckert_entry(it):
    r = it["row"]
    blocks = eckert_blocks()
    for hay in (r.get("document_id") or "", r.get("title") or "", r.get("line") or ""):
        for tok in re.findall(r"\b[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*\b", hay):
            if tok in blocks:
                return tok
    return ""


def ids_of(title):
    t = title.replace(" ", "")
    ids = set(re.findall(r"\d{2,}", title))
    ids |= {x.lower().replace(".", "") for x in re.findall(r"\b[fc]\.?\d+[rv]?", t)}
    ids |= {re.sub(r"[.\s]", "", x).lower() for x in re.findall(r"\b[fc]\.\s?\d+[rv]?", title)}  # "fr.2980 f.30r" keeps f30r
    return ids


def tokens_file(it):
    """The folder's token table for this item: the one whose name carries the item's own number or folio (the title's ids first, then
    the document id's, a unique best match only), else the reading's sibling table, else the folder's only table. A folder with several
    items and one shared table hands that table on; token_rows then keeps only the rows whose line ids carry this item's frame or folio
    (SITE-ITEMS-3: a page never shows another item's signs)."""
    d = os.path.join(ROOT, "ciphers", it["folder"])
    fs = sorted(f for f in os.listdir(d) if re.match(r"reading.*tokens.*\.tsv$", f)) if os.path.isdir(d) else []
    if not fs:
        return ""
    rd = os.path.basename(it.get("reading") or "")
    stem = rd.rsplit(".", 1)[0] if rd else ""
    sibs = [x for x in (stem + "_full_tokens.tsv", stem + "_tokens.tsv", stem.replace("reading", "reading_tokens", 1) + ".tsv") if stem and x in fs]
    if sibs and _cache.get("per_reading", {}).get(it.get("reading"), 1) == 1:  # the item's own reading, used by no other item
        return sibs[0]
    for hay in (it["title"].split(":")[0], it["title"] + " " + (it["row"].get("document_id") or "")):
        ids = {i for i in ids_of(hay) if not re.fullmatch(r"1[0-9]{3}", i)}
        score = {f: sum(1 for i in ids if re.search(rf"(?<![0-9]){re.escape(i)}(?![0-9])", f.lower())) for f in fs}
        best = max(score.values())
        hit = [f for f in fs if score[f] == best] if best else []
        if len(hit) > 1:  # prefer the fullest version of the same piece
            hit = [f for f in hit if "full" in f] or hit
        if len(hit) == 1 or (hit and all("full" in f for f in hit)):
            return hit[0]
    if sibs:  # a shared reading's table: token_rows narrows it to this item's frame or folio, or shows nothing
        return sibs[0]
    if len(fs) == 1:
        return fs[0]
    return "reading_tokens.tsv" if "reading_tokens.tsv" in fs and folder_items(it["folder"]) == 1 else ""


def folder_items(folder):
    return _cache.get("per_folder", {}).get(folder, 1)


def token_rows(it, path):
    """[(line id, sign, value, grade)] from a token table, header-driven; rows narrowed to the item's folio or frame when its lines
    carry one."""
    rows = [ln.rstrip("\n").split("\t") for ln in open(path, encoding="utf-8") if ln.strip() and not ln.startswith("#")]
    if not rows:
        return []
    h = [c.strip().lower() for c in rows[0]]
    pick = lambda *names: next((h.index(n) for n in names if n in h), None)
    li, si, vi, gi = pick("line", "record", "folio", "page"), pick("sign", "code", "token", "group"), pick("value", "letter"), pick("grade")
    if None in (si, vi, gi):
        return []
    out = []
    for r in rows[1:]:
        if len(r) <= max(si, vi, gi):
            continue
        ln = r[li] if li is not None else ""
        if li is not None and h[li] in ("folio", "page") and "line" in h and len(r) > h.index("line"):
            ln = r[li] + "_" + r[h.index("line")]
        out.append((ln, r[si], r[vi], r[gi]))
    if folder_items(it["folder"]) == 1 or _cache.get("per_reading", {}).get(it.get("reading"), 1) == 1:
        return out  # the item's own table: nothing to narrow (a date's "21" once cut a table to the rows of line 21)
    ids = {i for i in ids_of(it["title"]) if not re.fullmatch(r"1[0-9]{3}", i)}  # years are shared by siblings
    ids = {i for i in ids if len(i) >= 3}  # a day of the month ("10 Oct") is not a line number (L10)
    keys = [x[0].lower().replace(".", "") for x in out]
    has = lambda i, k: re.search(rf"(?<![0-9]){re.escape(i)}(?![0-9])", k)
    disc = {i for i in ids if not all(has(i, k) for k in keys)}  # an id every row carries (a bundle number) tells nothing
    narrowed = [x for x, k in zip(out, keys) if any(has(i, k) for i in disc)]
    if narrowed:
        return narrowed
    # a table shared by several items whose rows carry a frame or folio this item does not: none of them are this item's signs
    if folder_items(it["folder"]) > 1 and any(re.search(r"(?<![0-9])\d{3,4}[rv]?(?![0-9])|f\d+", k) for k in keys) \
            and os.path.basename(path) == "reading_tokens.tsv":
        return []
    return out


def english_lines():
    if "en" not in _cache:
        out = {}
        if os.path.exists(ENGLISH_TSV):
            for ln in open(ENGLISH_TSV, encoding="utf-8"):
                c = ln.rstrip("\n").split("\t")
                if len(c) >= 4 and c[0] != "item" and not c[0].startswith("#"):
                    out.setdefault(c[0], []).append((c[1], c[2], c[3]))
        _cache["en"] = out
    return _cache["en"]


def selection_rows():
    """SELECTION.md rows: (quote, ids from the item cell, score, thin, family row?)."""
    if "sel" not in _cache:
        rows = []
        p = os.path.join(EXHIBIT_DIR, "SELECTION.md")
        for line in open(p, encoding="utf-8") if os.path.exists(p) else []:
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(c) >= 11 and c[0].isdigit():
                q = re.search(r'"([^"]{20,})"', c[6])
                sc = re.search(r"[0-3]", c[9])
                fam = "family" in c[1].lower() or "about" in c[1].lower() and "telegrams" in c[1].lower()
                ids = set(re.findall(r"\b(?:E\d+|WVO \d+|BLA \d+|frame \d{4}|f\.\s?\d+[rv]?|no\.\s?\d+)\b", c[1].replace("*", "")))
                ids |= {f"WVO {n}" for n in re.findall(r"\b(\d{4})\b", c[1]) if c[1].startswith("Lodewijk")}
                rows.append({"quote": q.group(1) if q else "", "ids": ids, "score": int(sc.group()) if sc else None,
                             "thin": len(c) > 10 and "thin" in c[-1], "family": fam, "item": c[1].replace("*", "")})
        _cache["sel"] = rows
    return _cache["sel"]


def selection_for(it):
    """The SELECTION.md row for this item: by its quoted sentence inside the depth sentence, else by an identifier in its item cell;
    Eckert telegrams in the scored pool that no row names get the family row (row 11's own scope). None outside the pool."""
    norm = lambda s: re.sub(r"\W+", " ", s or "").lower().strip()
    g = norm(it["gist"])
    rows = selection_rows()
    for r in rows:
        head = norm(r["quote"].split("...")[0])[:60]
        if not r["family"] and len(head) > 25 and head in g:
            return r
    hay = it["title"] + " " + (it["row"].get("document_id") or "")
    for r in rows:
        if not r["family"] and any(re.search(rf"(?<![\w.]){re.escape(i)}(?!\d)", hay) for i in r["ids"]):
            return r
    d = re.match(r"\s*D([0-4])", str(it["row"].get("depth") or ""))
    if it["folder"] == "eckert-1864" and (it["n"] or 0) >= 3 and d and int(d.group(1)) >= 2:
        return next((r for r in rows if r["family"]), None)
    return None


def what_it_says(it, sel):
    if sel and sel["quote"] and not sel["family"]:
        return sel["quote"], "quoted in the exhibit's selection notes from the verifier's depth sentence"
    if it["gist"]:
        return it["gist"], "the verifier's depth sentence (an English paraphrase of the read passage)"
    n = f"N{it['n']}" if it["n"] is not None else "an unrecorded class"
    kind = dict((k, h) for k, h, _ in C.CLASSES).get(it["cls"], "reading").lower()
    return f"A {kind} read at grade {n}; the reading is below the content bar.", "no depth sentence on file"


def reading_section(it, sc, dsp, pfx):
    """Three layers where a crop and an English line exist; otherwise the graded original and an English slot marked pending."""
    out, pend = [], 0
    if dsp:  # the display's own lines: crop, graded original, English
        fix = [(pfx + "assets/exhibit-" + s, t, a, b) for s, t, a, b in dsp["lines"]]
        out.append(B.legend() + X.lines_html(fix, dsp["lang"])
                   + f'<p class="small">The same lines, with the story around them: <a href="{pfx}exhibit/{dsp["slug"]}.html">the display</a>.</p>')
        return "".join(out), 0
    if sc:
        for imgs, toks, cap, eng in sc["crops"]:
            en = (f'<p class="en"><span class="k">English (translation, interpretation)</span>{E(eng)}</p>' if eng else
                  '<p class="en none">Reads as letters with gaps: no English is given for this line.</p>')
            out.append('<figure class="cipher">' + "".join(f'<img alt="{E(cap)}" src="{pfx}assets/cat-img/{E(x)}">' for x in imgs)
                       + '<p class="k layer">As read, sign by sign, with grades</p>' + C.token_strip(toks()) + en
                       + f'<figcaption>{E(cap)} &middot; our crop &middot; {E(C.LICENCE)}</figcaption></figure>')
        return "".join(out), 0
    en = english_lines().get(it["file"][:-5], [])
    entry = eckert_entry(it) if it["folder"] == "eckert-1864" else ""
    if entry:
        text, counts, rf = eckert_blocks()[entry]
        body = E(text)
        body = re.sub(r"\[([^\]]+)\]", r'<mark class="cw" title="code word, decoded from the cipher book">\1</mark>', body)
        body = re.sub(r"\{(\w+): ([^}]+)\}", r'<span class="small">[\1: \2]</span>', body)
        out.append(f'<div class="tokens" data-item="{E(it["file"][:-5])}" data-folder="eckert-1864" data-file="{E(rf)}" '
                   f'data-lines="{E(entry)}"></div>')
        out.append(f'<p class="k layer">As read, entry {E(entry)} (English; <mark class="cw">highlighted</mark> words are code words '
                   f'decoded from the period cipher book, plain words are what the clerk wrote)</p><p class="orig">{body}</p>'
                   f'<p class="small">{E(counts)} {E(C.GRADE_KEY)} Regenerated by <a href="{C.REPO_BLOB}ciphers/eckert-1864/{E(rf)}">'
                   f'{E(rf)}</a>.</p>')
    else:
        tf = tokens_file(it)
        rows = token_rows(it, os.path.join(ROOT, "ciphers", it["folder"], tf)) if tf else []
        if rows:
            lines = list(dict.fromkeys(r[0] for r in rows))
            first = [l_ for l_ in lines if any(lid and (lid == l_ or l_.endswith(lid) or lid.startswith(l_ + "-")) for lid, _o, _e in en)]
            shown = (first + [l_ for l_ in lines if l_ not in first])[:8]  # the English line's own lines lead
            out.append(f'<div class="tokens" data-item="{E(it["file"][:-5])}" data-folder="{E(it["folder"])}" data-file="{E(tf)}" '
                       f'data-lines="{E(",".join(shown))}">')
            out.append(f'<p class="k layer">{E(it["lang"] or "Original language")} as read, sign by sign, with grades '
                       f'({len(shown)} of {len(lines)} lines; the whole table is <a href="{C.REPO_BLOB}ciphers/{E(it["folder"])}/{E(tf)}">'
                       f'{E(tf)}</a>)</p>')
            for ln in shown:
                toks = [(s, "(null)" if v.upper() == "NULL" else ("" if v == "?" else v), g) for l_, s, v, g in rows if l_ == ln][:80]
                out.append(f'<div class="rline"><span class="small">line {E(ln)}</span>{C.token_strip(toks)}</div>')
            out.append("</div>")
        else:
            link = (f' The reading is in the repository: {C.link_or_text(it["reading"])}.' if it["reading"] else "")
            out.append(f'<p class="small" data-pending="original">Graded original: no per-sign table on file for this item.{link}</p>')
    out.append('<p class="small" data-pending="crop">Cipher crop: not cut for this page (crops are cut from the folder\'s own images '
               'when an English line is written).</p>')
    if en:
        out.append("".join(f'<p class="en"><span class="k">English (translation, interpretation), line {E(lid)}</span>{E(eng)}</p>'
                           for lid, _o, eng in en))
    else:
        out.append(f'<p class="en none" data-pending="english">{PENDING_EN}</p>')
        pend = 1
    return "".join(out), pend


def names_of(it, sc, dsp):
    """Names of persons and places as the reading itself decodes them (code words, nomenclature values), de-duplicated."""
    vals = []
    if dsp:
        vals += [v for line in dsp["lines"] for v, g, _s in line[1] if g not in ("clear",)]
    elif sc:
        vals += [p for p, _w, _c in sc["people"]]
    elif it["folder"] == "eckert-1864":
        e = eckert_entry(it)
        if e:
            vals += re.findall(r"\[([^\]]+)\]", eckert_blocks()[e][0])
    else:
        tf = tokens_file(it)
        if tf:
            vals += [v for _l, _s, v, g in token_rows(it, os.path.join(ROOT, "ciphers", it["folder"], tf)) if g in "HCSM"]
    out = []
    for v in vals:
        v = re.sub(r"\s*\((?:-ed|-ing)[^)]*\)|\[[#?]\]|[\[\]?]", "", v).strip(" .,;:")
        if (sc and not dsp) or name_like(v):
            if v and v not in out:
                out.append(v)
    return out[:24]


def portraits():
    if "por" not in _cache:
        rows = []
        p = os.path.join(EXHIBIT_DIR, "portraits", "manifest.tsv")
        if os.path.exists(p):
            lines = open(p, encoding="utf-8").read().splitlines()
            h = lines[0].split("\t")
            for ln in lines[1:]:
                c = dict(zip(h, ln.split("\t")))
                if c.get("person") and c.get("file"):
                    rows.append(c)
        _cache["por"] = rows
    return _cache["por"]


def portrait_for(name):
    """A manifest row whose person's surname (last word) is a word of the name; None otherwise (a placeholder shows)."""
    ws = set(re.findall(r"[A-Za-z]{3,}", name or ""))
    for c in portraits():
        sur = re.findall(r"[A-Za-z]{3,}", re.sub(r",.*|\(.*", "", c["person"]))
        if sur and sur[-1] in ws:
            return c
    return None


def person_slug(n):
    return C.slugify(n, 50) or "x"


def who_of(it):
    """(from, to, place, date) as the item's title states them: the catalogue's own parser, retried on the part after a heading
    colon with parentheticals dropped ("Eckert 1864 (Fort Monroe ledger): Ingalls (City Point) to Webster, 27 Aug 1864")."""
    got = C.parties(it)
    if got[0] and got[1]:
        return got
    t = it["title"]
    for part in ([t.split(": ", 1)[1]] if ": " in t else []) + [t]:
        part = re.sub(r"\s*\([^)]*\)", "", part)
        alt = C.parties({"title": part})
        if alt[0] and alt[1] and len(alt[0]) < 80 and len(alt[1]) < 120:
            return alt
    return got


def place_ok(p):
    """A place as the title gives it: capitalised words (particles allowed), not a role or a description."""
    ws = (p or "").replace(",", " ").split()
    return bool(ws) and all(w[0].isupper() or w in ("de", "la", "le", "van", "am", "an", "der", "di", "du", "sur") for w in ws)


def badge_block(it, pfx):
    n, r, fold = it["n"], it["row"], it["folder"]
    st = it["audit_status"] or ""
    two = "yes" if st in ("two audits", "three audits") else ("no, one audit" if st == "one audit" else "not recorded")
    b = [f'<a class="badge" href="{pfx}how-to-read.html#n-class">N{n} {E(C.NSHORT[n])}</a>' if n is not None else "",
         f'<a class="badge" href="{pfx}how-to-read.html#depth">{E(it["depth"])}</a>' if it["depth"] else "",
         f'<a class="badge" href="{pfx}how-to-read.html#key">{E(it["key"])}</a>' if it["key"] else "",
         f'<span class="badge">two audits: {two}</span>']
    claim = (f'<blockquote class="claim">{C.md(it["safe"])}</blockquote><p class="small">The verifier\'s safe sentence, quoted from '
             'AUDIT.md.</p>' if it["safe"] else
             f'<blockquote class="claim">{C.md(it["register"])}</blockquote><p class="small">From the results register; no safe sentence '
             'in AUDIT.md matched this entry, so read the audit before quoting it.</p>')
    ct, keys = C.files_of(fold)
    script = ("decode.py" if it["script"].startswith("decode.py") else "decode.json" if it["script"] else "")
    links = [f'<a href="{C.REPO_BLOB}ciphers/{E(fold)}/AUDIT.md">AUDIT.md</a>',
             f'decode script <a href="{C.REPO_BLOB}ciphers/{E(fold)}/{script}">{script}</a>' if script else "decode script: none recorded",
             "key " + ", ".join(f'<a href="{C.REPO_BLOB}ciphers/{E(fold)}/{E(k)}">{E(k)}</a>' for k in keys) if keys else "key file: none in folder",
             f'image source {C.link_or_text(it["image"])}' if it["image"] else "image source: see the folder's NOTES.md",
             f'<a href="{C.REPO_TREE}ciphers/{E(fold)}">folder</a>']
    searched, unreach = C.search_log(fold, 30)
    cl = C.control_lines(r)
    cmd = (f"python3 ciphers/{fold}/decode.py --check" if script == "decode.py" else
           f"python3 tools/decode_key.py ciphers/{fold} --check" if script else "")
    return ("".join(claim) + '<p class="badges">' + "".join(b) + "</p>" + C.grade_bar(r)
            + '<ul class="links"><li>' + " &middot; ".join(links) + "</li>"
            + (f"<li>Regenerate: <code>{E(cmd)}</code></li>" if cmd else "")
            + (f"<li>Control: {C.md(cl[0])}</li>" if cl else "") + "</ul>"
            + C.det(f"Search log from AUDIT.md ({len(searched)} search lines, {len(unreach)} on blocked or unreachable hosts)",
                    "<ul>" + "".join(f"<li>{C.md(s)}</li>" for s in searched) + "</ul>"
                    + ("<p><b>Unreachable</b></p><ul>" + "".join(f"<li>{C.md(s)}</li>" for s in unreach) + "</ul>" if unreach else "")))


ITEM_CSS = """
section.part{margin:22px 0}section.part>h2{font:600 13px system-ui,sans-serif;letter-spacing:.06em;text-transform:uppercase;
 color:var(--muted);border-bottom:1px solid var(--rule);padding-bottom:4px}
.says1{font:19px/1.45 Georgia,serif;margin:6px 0}
p.orig{font:16px/1.7 Georgia,serif}mark.cw{background:var(--tint);color:inherit;border-bottom:2px solid var(--accent);padding:0 2px}
.rline{margin:8px 0}.names{display:flex;flex-wrap:wrap;gap:6px;list-style:none;padding:0}
.names a{font:14px system-ui,sans-serif;border:1px solid var(--rule);padding:2px 8px;text-decoration:none}
.faces1{display:flex;flex-wrap:wrap;gap:12px}.faces1 .face{width:120px;font:12px/1.3 system-ui,sans-serif}
.faces1 .pf{position:relative;width:120px;height:140px}.faces1 .pf img,.faces1 .pf svg{position:absolute;inset:0;width:120px;height:140px;object-fit:cover}
.ctxslot{border:1px dashed var(--rule);padding:8px 12px;color:var(--muted);font:14px system-ui,sans-serif}
"""


def item_page(it, sc, dsp, pfx, people_href):
    """The one item-page template: returns (body, pending English count)."""
    sel = selection_for(it)
    says, src = what_it_says(it, sel)
    out = [f'<article data-interest="{sel["score"] if sel and sel["score"] is not None else "unscored"}"'
           f' data-thin="{"yes" if sel and sel["thin"] else "no"}">',
           f'<h1>{E(sc["short"] if sc else it["title"])}</h1>']
    out.append(f'<section class="part" id="what-it-says"><h2>What it says</h2><p class="says1">{C.md(says)}</p>'
               f'<p class="small">Source: {E(src)}.</p></section>')
    rd, pend = reading_section(it, sc, dsp, pfx)
    out.append(f'<section class="part" id="reading"><h2>The reading</h2>{rd}</section>')
    f, t, place, date = sc["who"] if sc else who_of(it)
    place = place if sc or place_ok(place) else ""
    names = names_of(it, sc, dsp)
    who = [f'<div class="ctx"><div><span class="k">From</span> {E(f) or "not given in the record"}</div>'
           f'<div><span class="k">To</span> {E(t) or "not given in the record"}</div>'
           f'<div><span class="k">At</span> {E(place) or "not given in the record"}</div>'
           f'<div><span class="k">Date</span> {E(date) or "not given in the record"}</div>'
           f'<div><span class="k">Held</span> {E(C.archive_of(it) or it["holder"] or "not recorded")}</div></div>']
    if names:
        who.append('<p class="k layer">Named in the reading (persons and places as the cipher decodes them)</p><ul class="names">'
                   + "".join(f'<li><a href="{people_href(n)}">{E(n)}</a></li>' for n in names) + "</ul>")
    else:
        who.append('<p class="small">No person or place name is decoded in the cipher text of this item (names in clear, or none).</p>')
    faces = []
    for n in [f, t] + names:
        c = portrait_for(n)
        if c and c["person"] not in [x["person"] for x in faces]:
            faces.append(c)
    if faces:
        who.append('<div class="faces1">' + "".join(X.face_html(c["person"], c.get("role_five_words", ""), "", c["file"],
                                                                pfx + "assets/portraits/") for c in faces[:6]) + "</div>")
    out.append('<section class="part" id="who"><h2>Who, where, when</h2>' + "".join(who) + "</section>")
    out.append(f'<section class="part" id="how"><h2>How we know</h2>{badge_block(it, pfx)}</section>')
    if sel and sel["score"] is not None and sel["score"] >= 2:
        out.append('<section class="part" id="context"><h2>Context</h2><p class="ctxslot" data-pending="context">Context: to be '
                   'written from printed sources on file, labelled context (SITE-ITEMS-3).</p></section>')
    out.append("</article>")
    return "".join(out), pend, names, sel


def people_pages(index, href_item):
    """people/<slug>.html per name, and people/index.html. index: {name: [item, ...]}."""
    pages = {}
    for n, its in index.items():
        c = portrait_for(n)
        face = ('<div class="faces1">' + X.face_html(c["person"], c.get("role_five_words", ""), "", c["file"], "../assets/portraits/")
                + "</div>") if c else ""
        lis = "".join(f'<li><a href="{href_item(it)}">{E(C.ten_words(it["title"], 16))}</a></li>' for it in its)
        pages[person_slug(n)] = (n, f'<h1>{E(n)}</h1>{face}<p class="small">As the decoded cipher text names it. Every item whose '
                                    f'reading decodes this name ({len(its)}):</p><ul class="browse">{lis}</ul>')
    order = sorted(index, key=lambda n: (-len(index[n]), n.lower()))
    idx = ('<h1>People and places</h1><p class="small">Names as the cipher text decodes them (code words and nomenclature entries), one '
           'page each, listing every item that names them. Picked from the decoded values by a word-list filter: a name that is also an '
           'ordinary English word (Grant, Butler, Post) is not listed, and a person and a place are not told apart.</p><ul class="browse">'
           + "".join(f'<li><a href="{person_slug(n)}.html">{E(n)}</a> <span class="small">({len(index[n])})</span></li>' for n in order)
           + "</ul>")
    return pages, idx


PORTRAIT_CREDIT = ('<h2>Portraits</h2><p>Faces in the displays are public-domain paintings and prints from Wikimedia Commons, named with '
                   'artist, date and licence in <code>assets/portraits/manifest.tsv</code> once a file arrives; until then each face '
                   'is a labelled placeholder. No non-free image is used.</p>')


def write_preview(path, out, date):
    """One self-contained front door: displays with embedded images, then All readings; item links point into the site folder."""
    items, ns, results, targets = load()
    dmap = display_map(items)
    rel = os.path.relpath(out, os.path.dirname(os.path.abspath(path)) or ".").replace(os.sep, "/").rstrip("/") + "/"
    img = lambda p: emb(os.path.join(EXHIBIT_DIR, p))
    door = door_html(img, lambda d: f"{rel}exhibit/{d['slug']}.html", lambda it: rel + "items/" + it["file"], dmap)
    idx = C.index_body(items, ns, results, targets, lambda it: rel + "items/" + it["file"], inline=True)
    box = ('<label class="small">Find <input id="q" class="qf" type="search" placeholder="sender, recipient, year, archive, '
           'language, class, depth" aria-label="Filter the readings"></label> ')
    idx = idx.replace('<div class="filters">', '<div class="filters">' + box, 1).replace(C.FILTER_JS, TEXT_FILTER_JS)
    idx = idx.replace("<h1>Cipher letters read from the archives</h1>", '<h1 id="all">All readings</h1>', 1)
    for a in ("attention.html", "how-to-read.html"):
        idx = idx.replace(f'href="{a}"', f'href="{rel}{a}"')
    html_ = shell("What the cipher said (preview)", door + f'<section class="door">{idx}</section>', rel, "Exhibit", None, date,
                  "Three cipher displays, then every audited reading (private preview, single file).", exhibit=True)
    html_ = html_.replace(f'href="{rel}index.html">Exhibit', 'href="#top">Exhibit')
    open(path, "w", encoding="utf-8").write(html_)
    return len(html_)


def rule10_hits(out):
    hits = []
    for dp, _, fs in os.walk(out):
        for f in fs:
            if f.endswith(".html"):
                txt = open(os.path.join(dp, f), encoding="utf-8").read()
                txt = re.sub(r"<footer.*?</footer>", "", txt, flags=re.S)
                txt = re.sub(r"<[^>]+>", " ", re.sub(r"<(style|script)[^>]*>.*?</\1>", "", txt, flags=re.S))
                txt = CAVEAT.sub(" ", txt)  # the N4 definition's own caveat is a limit, not a claim
                for m in FORBIDDEN.finditer(txt):
                    hits.append((os.path.relpath(os.path.join(dp, f), out), txt[max(0, m.start() - 60):m.end() + 40].strip()))
    return hits


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="research/mockups/site/")
    ap.add_argument("--preview", default="")
    ap.add_argument("--date", default=time.strftime("%-d %B %Y", time.gmtime()))
    a = ap.parse_args(argv)
    for p in (a.out, a.preview):
        if p and (os.path.abspath(p) + os.sep).startswith(os.path.abspath("docs") + os.sep):
            sys.exit("refused: docs/ is the GitHub Pages folder; the site is a private preview (owner, 10 Oct 2026)")
    items, dmap, pages, stats = write_site(a.out, a.date)
    msg = (f"site: {len(pages)} pages ({len(items)} item pages, {len(X.DISPLAYS)} displays, {stats['people']} people pages) -> {a.out}"
           f"; English pending {stats['pending_en']} of {len(items)}; interest tiers "
           + ", ".join(f"{k}: {v}" for k, v in sorted(stats["tiers"].items())))
    missing = [s for s, w in DISPLAY_ITEMS.items() if len(dmap.get(s, [])) < len(w)]
    if missing:
        msg += "; display items not matched: " + ", ".join(missing)
    if a.preview:
        msg += f"; preview {a.preview} ({write_preview(a.preview, a.out, a.date) // 1024} KB)"
    hits = rule10_hits(a.out)
    msg += (f"; rule-10 phrase hits: {len(hits)}, all in item pages' quoted audit logs" if hits and all(h[0].startswith("items/")
            for h in hits) else f"; rule-10 phrase hits: {len(hits)}")
    print(msg)
    for h in hits[:10]:
        print("  rule-10:", h[0], "::", h[1])
    return 0


if __name__ == "__main__":
    sys.exit(main())
