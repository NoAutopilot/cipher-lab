#!/usr/bin/env python3
"""build_catalogue.py -- a reader-facing catalogue of the audited readings, generated from the audit files (CATALOGUE-SITE-1, 9 Oct 2026).

MOCK-UP ONLY. Nothing this writes is published: the owner decides after reading the mock-up (owner, 9 Oct 2026 22:1x UTC). The
default output directory is research/mockups/catalogue/; writing under docs/ (the GitHub Pages folder) is refused.

Inputs: status.json `results` (every row the board counts, by the board's own rules, read from tools/build_dashboard.py's source
with ast so the board itself is never run and never rewritten), each target's AUDIT.md (the safe sentence, matched to the row),
N4-READINGS.md `links:` lines, the folder's NOTES.md (first image link), specs/<slug>.json (language).

Outputs: <out>/index.html (counts in documents by the board's five classes, then one row per item), <out>/items/<n>-<slug>.html per
item, <out>/how-to-read.html, <out>/credits.html; with --mockup FILE, one self-contained page holding the index and three item
pages inline (--mockup-items picks them by title substring). Pages are plain HTML with inline CSS, no scripts, no remote assets,
no embedded images (images are linked, never copied).

Content rules applied mechanically: internal job names (hyphenated capital tokens such as AUDIT2-MANT), session ids, worker and
cost words are stripped from every sentence taken from the register (sanitize(); the offline test fails on any survivor);
folders named in RESTRICTED (Debosnys) are never listed; open or blocked targets appear only as a count.

Must catch (offline test): a job name or session id in a register sentence; a row the board counts missing from the catalogue;
an output path under docs/. Must not block: shelfmarks and edition references with capitals and hyphens of their own
(e.g. "OR I/32 pt 3", "WVO 5797", "KHA A 11/XIV B/41-42") -- sanitize() only removes tokens with two or more capital-led
hyphenated parts that carry a capital run, and the test checks those references survive.

Usage: python3 tools/build_catalogue.py [--out DIR] [--mockup FILE] [--mockup-items "A" "B" "C"]
"""
import argparse
import ast
import glob
import html
import json
import os
import re
import sys
from collections import Counter

E = html.escape
REPO_BLOB = "https://github.com/NoAutopilot/cipher-lab/blob/main/"
REPO_TREE = "https://github.com/NoAutopilot/cipher-lab/tree/main/"
RESTRICTED = ("debosnys",)  # folders whose material is restricted by the holder (CONTRIBUTIONS.md 28 Sept 2026): never listed
BOARD_FUNCS = {"nclass", "audits", "novelty", "docs_of", "depth", "counted", "counted_fragments", "held_depth",
               "counted_novelty", "counted_key", "counted_contrib", "n_docs", "folder_of"}
BOARD_CONSTS = {"REPO", "AUDIT_STATUS", "TWO_PLUS", "READING_SCOPES", "_heuristic_rows"}

CLASSES = [  # (key, heading, one-line explanation)
    ("recovered-passages", "Recovered passages",
     "Cipher passages read inside a document whose clear parts or context were already known."),
    ("completed-reading", "Completed readings",
     "Short cipher texts (mostly telegrams) read in full."),
    ("fragments", "Fragments read",
     "Scattered words and short phrases read; not yet a connected passage."),
    ("key", "Keys to known text",
     "A key or mapping recovered for a cipher whose plain text was already in print."),
    ("contrib", "Contributions",
     "Identifications, corrections and checked material handed on; no new reading claimed."),
]
NWORDS = {
    0: "Already known: this item's plain text and its decipherment were already on record.",
    1: "Plain text already in print; our reading is an independent re-decipherment.",
    2: "Plain text known elsewhere; no earlier mapping of this cipher text to it was found.",
    3: "No earlier plain text or decipherment located after a logged search.",
    4: "No prior decipherment located; the principal editions, catalogues and project pages were searched "
       "(unpublished or archival work is not excluded).",
    5: "Confirmed by the holding archive or a specialist.",
}
NSHORT = {0: "already known", 1: "text in print; read again independently", 2: "text known; mapping not found before",
          3: "no prior reading located", 4: "no prior decipherment located (editions searched)", 5: "confirmed by holder or specialist"}
DEPTH_WORDS = {0: "key ranked first; nothing reads yet", 1: "fragments read", 2: "partially deciphered",
               3: "largely deciphered", 4: "deciphered"}
KEY_WORDS = {"ours": "key recovered by us", "period": "period key, rebuilt by us from a decipherment or key sheet of the time",
             "published": "a key published by someone else, applied by us (credited)"}
LANG = {"fr": "French", "fr16": "French", "fr17": "French", "fr18": "French", "en": "English", "en18": "English",
        "en19": "English", "nl": "Dutch", "de": "German", "it": "Italian", "es": "Spanish", "es17c": "Spanish",
        "pt": "Portuguese", "pt18": "Portuguese", "la": "Latin", "sv": "Swedish"}

# A job name: two or more hyphen-joined parts, capital-led, at least one part with two capitals running (AUDIT2-MANT,
# N8-GRA2, DEPTH-MH, R9-MANTV). Shelfmarks such as "B/41-42" or "OR I/32" have no such run on both sides of a hyphen.
JOB = re.compile(r"\b(?=[A-Z0-9]*[A-Z]{2})[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+\b|\b[A-Z][A-Z0-9]+-[A-Z][A-Z0-9]*\b")
SESSION = re.compile(r"session_[A-Za-z0-9]+")
INTERNAL_WORDS = re.compile(r"\b(?:worker|orchestrator|lane|LANE|cost|USD|account[- ]?\d)\b")


def sanitize(s):
    """Strip internal job names, session ids and the brackets they leave; keep shelfmarks and edition references."""
    s = SESSION.sub("", s or "")
    s = re.sub(r"\bLANE [A-Z0-9-]+(?:\s*\([^)]*\))?(?:\s+round \d+)?\s*:?\s*", "", s)
    # a bracket whose content is mostly a job reference goes whole: "(DEPTH-MH 8 Oct 2026)", "(R9-MANTV 6 Oct 2026, was 24)"
    def drop_bracket(m):
        inner = m.group(1)
        return "" if JOB.search(inner) or INTERNAL_WORDS.search(inner) else m.group(0)
    for _ in range(2):
        s = re.sub(r"\s*\(([^()]*)\)", drop_bracket, s)
    s = JOB.sub("", s)
    s = re.sub(r"\b(?:[Aa]n?|[Tt]he|[Tt]his|[Oo]ur) (?:[\w-]+ ){0,2}worker(?:'s)?\b", "we", s)
    s = re.sub(r"(^|[.!?]\s+)we\b", lambda m: m.group(1) + "We", s)
    s = re.sub(r"\s+([,;.:])", r"\1", s)
    s = re.sub(r"([,;])\s*([,;.])", r"\2", s)
    s = re.sub(r"\(\s*[,;]?\s*\)", "", s)
    s = re.sub(r"\s{2,}", " ", s)
    return s.strip(" ;,")


def board_rules(path="tools/build_dashboard.py"):
    """The board's own counting functions, lifted from its source with ast (the board script writes files when run)."""
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", SyntaxWarning)
        tree = ast.parse(open(path, encoding="utf-8").read())
    keep = [n for n in tree.body if (isinstance(n, ast.FunctionDef) and n.name in BOARD_FUNCS)
            or (isinstance(n, ast.Assign) and any(getattr(t, "id", None) in BOARD_CONSTS for t in n.targets))]
    ns = {"re": re, "sys": sys}
    exec(compile(ast.Module(body=keep, type_ignores=[]), path, "exec"), ns)
    return ns


def class_of(r, ns):
    if ns["counted"](r):
        return r.get("claim_scope", "recovered-passages")
    if ns["counted_fragments"](r):
        return "fragments"
    if ns["counted_key"](r):
        return "key"
    if ns["counted_contrib"](r):
        return "contrib"
    return None


def folder(r):
    m = re.search(r"ciphers/([\w.-]+)", r.get("link", ""))
    return m.group(1) if m else ""


def slugify(s, n=60):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:n].strip("-")


def nval(r, field):
    m = re.search(r"N([0-5])", str(r.get(field) or ""))
    return int(m.group(1)) if m else None


def item_n(r, cls):
    if cls == "key":
        return nval(r, "mapping_novelty")
    v = nval(r, "plaintext_novelty")
    if v is None:
        m = re.search(r"\bN([0-5])\b", r.get("grade", ""))
        v = int(m.group(1)) if m else None
    return v


def depth_words(r):
    m = re.match(r"\s*D([0-4])", str(r.get("depth") or ""))
    if not m:
        return ""
    d = int(m.group(1))
    w = DEPTH_WORDS[d]
    pct = r.get("depth_pct")
    if d in (2, 3) and isinstance(pct, (int, float)):
        w += f" (about {round(pct)}% of the cipher text)"
    return w


def key_words(r):
    k = str(r.get("key") or "")
    parts = [KEY_WORDS[p.strip()] for p in re.split(r"\s*\+\s*", k) if p.strip() in KEY_WORDS]
    return "; ".join(parts)


# ------------------------------------------------------------------ per-folder readers

_audit_cache, _notes_cache = {}, {}


def safe_sentences(fold):
    """Every quoted safe sentence in the folder's AUDIT.md, in file order (later = more recent)."""
    if fold not in _audit_cache:
        p = os.path.join("ciphers", fold, "AUDIT.md")
        txt = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
        out = []
        # labels seen: 'Safe sentence:', 'Safe sentence (current):', '**5797, safe:**', '**Safe (unchanged from ...):**'
        lab = re.compile(r"(?:\*\*[^*\n]{0,80}?\b[Ss]afe\b[^*\n]{0,120}?\*\*|\b[Ss]afe sentence\b[^\n:\"\u201c]{0,80}:)"
                         r"[\s:*]*[\"\u201c](.+?)[\"\u201d]", re.S)
        for m in lab.finditer(txt):
            pre = txt[max(0, m.start() - 3):m.start() + 12].lower()
            if "unsafe" in pre:
                continue
            c = re.sub(r"\s+", " ", m.group(1)).strip()
            if len(c) >= 60:
                out.append(c)
        _audit_cache[fold] = (txt, out)
    return _audit_cache[fold]


def words(s):
    return set(w for w in re.findall(r"[a-z0-9]{3,}", (s or "").lower()))


def best_safe_sentence(r):
    """The AUDIT.md safe sentence that best matches this row (title + register line), or ('', 0)."""
    _, cands = safe_sentences(folder(r))
    target = words(r.get("line", "")) | words(r.get("title", "")) | words(r.get("document_id", ""))
    scored = [(len(words(c) & target) / len(words(c)), i, c) for i, c in enumerate(cands) if words(c)]
    if not scored:
        return "", 0.0
    top = max(sc for sc, _, _ in scored)
    # near-ties go to the later sentence: AUDIT.md is appended in order, so later is the more recent revision
    sc, _, c = max((x for x in scored if x[0] >= top - 0.1), key=lambda x: x[1])
    return c, sc


def audits_on_file(fold):
    txt, _ = safe_sentences(fold)
    out = []
    for m in re.finditer(r"^#{1,3} (.*(?:[Aa]udit|AUDIT|[Vv]erif).*)$", txt, re.M):
        h = m.group(1)
        d = re.search(r"\b(\d{1,2} (?:Sept?|Oct|Nov|Dec|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug)\w* \d{4})", h)
        out.append(d.group(1) if d else "")
    return out


def notes_head(fold):
    if fold not in _notes_cache:
        p = os.path.join("ciphers", fold, "NOTES.md")
        _notes_cache[fold] = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
    return _notes_cache[fold]


IMG = re.compile(r"https?://(?:gallica\.bnf\.fr/ark:/12148/[\w/.]+|hdl\.huntington\.org/digital/[\w/.]+|"
                 r"resources\.huygens\.knaw\.nl/media/wvo/[\w/.-]+|[\w.-]+/iiif/[\w/.:%-]+|"
                 r"[\w.-]*archiv[\w.-]*/[\w/.?=&%-]+)")


def first_image(fold):
    m = IMG.search(notes_head(fold))
    return m.group(0).rstrip(".,);") if m else ""


def load_memo_links():
    out = []
    if not os.path.exists("N4-READINGS.md"):
        return out
    txt = open("N4-READINGS.md", encoding="utf-8").read()
    for sec in re.split(r"\n(?=## )", txt):
        m = re.match(r"## ciphers/([\w.-]+)\s*(.*)", sec)
        ml = re.search(r"^links:\s*(.+)$", sec, re.M)
        if not (m and ml):
            continue
        links = {}
        for part in ml.group(1).split(";"):
            if "=" in part:
                k, v = part.split("=", 1)
                links[k.strip()] = v.strip()
        out.append((m.group(1), m.group(2), links))
    return out


def memo_links_for(r, memo):
    toks = set(re.findall(r"\b(?:wvo\s*\d+|f\.\s*\d+[rv]?|e\d+|p\d+|bla\s*\d+)\b", r.get("title", "").lower()))
    for fold, head, links in memo:
        if fold == folder(r) and toks & set(re.findall(r"\b(?:wvo\s*\d+|f\.\s*\d+[rv]?|e\d+|p\d+|bla\s*\d+)\b", head.lower())):
            return links
    return {}


def language(fold):
    p = os.path.join("specs", fold + ".json")
    if os.path.exists(p):
        try:
            sp = json.load(open(p, encoding="utf-8"))
            for c in (sp.get("judge") or {}).get("lang"), *(sp.get("language_candidates") or []):
                if c and str(c).split("-")[0] in LANG:
                    return LANG[str(c).split("-")[0]]
        except (ValueError, TypeError):
            pass
    return ""


def reading_and_script(fold, title=""):
    d = os.path.join("ciphers", fold)
    files = sorted(os.listdir(d)) if os.path.isdir(d) else []
    reads = [f for f in files if re.match(r"reading.*\.(txt|md)$", f)]
    nums = re.findall(r"\d{2,}", title)
    reading = next((f for f in reads if any(n in f for n in nums)), "") or (reads[0] if len(reads) == 1 or "reading.txt" not in reads
                                                                          else "reading.txt") if reads else ""
    script = ("decode.py" if "decode.py" in files else "decode.json (run with tools/decode_key.py)" if "decode.json" in files else "")
    return reading, script


def md(s):
    """Escape, then render the two inline marks AUDIT.md sentences carry: *italic* and `code`."""
    t = E(s or "")
    t = re.sub(r"\*([^*\n]+)\*", r"<i>\1</i>", t)
    return re.sub(r"`([^`\n]+)`", r"\1", t)


def link_or_text(v):
    v = (v or "").strip()
    m = re.match(r"(https?://\S+)(.*)", v)
    if m:
        return f'<a href="{E(m.group(1))}">{E(m.group(1))}</a>{E(sanitize(m.group(2)))}'
    return E(sanitize(v)) if v else ""


# ------------------------------------------------------------------ items

def build_items(results, ns):
    memo = load_memo_links()
    items = []
    for r in results:
        cls = class_of(r, ns)
        if not cls:
            continue
        fold = folder(r)
        if any(x in fold.lower() for x in RESTRICTED):
            continue
        n = item_n(r, cls)
        safe, score = best_safe_sentence(r)
        links = memo_links_for(r, memo)
        reading, script = reading_and_script(fold, r.get("title", ""))
        items.append({
            "row": r, "cls": cls, "folder": fold, "n": n,
            "title": sanitize(r.get("title", "")),
            "holder": sanitize(r.get("document_id", "")),
            "lang": language(fold),
            "depth": depth_words(r),
            "key": key_words(r),
            "gist": sanitize(r.get("depth_sentence", "")),
            "safe": sanitize(safe) if score >= 0.5 else "",
            "register": sanitize(r.get("line", "")),
            "audits": [sanitize(a) for a in (r.get("audit_refs") or [])],
            "audit_status": r.get("audit_status", ""),
            "audit_dates": [d for d in audits_on_file(fold) if d],
            "result_date": r.get("date", ""),
            "image": links.get("image") or first_image(fold),
            "edition": links.get("edition", ""),
            "reading": links.get("reading") or (REPO_BLOB + f"ciphers/{fold}/{reading}" if reading else ""),
            "script": script,
            "docs": len(ns["docs_of"](r)),
        })
    for i, it in enumerate(items, 1):
        it["file"] = f"{i:03d}-{slugify(it['folder'] + ' ' + it['title'], 70)}.html"
    return items


def target_counts(targets=None, root="ciphers"):
    """Status words from the head of every ciphers/*/NOTES.md (rule 5 vocabulary); only a count is shown."""
    c = Counter()
    for p in glob.glob(os.path.join(root, "*", "NOTES.md")):
        if any(x in p.lower() for x in RESTRICTED):
            continue
        head = open(p, encoding="utf-8", errors="replace").read(3000).splitlines()[:15]
        for ln in head:
            m = re.match(r"\s*(?:-\s*)?(?:\*\*)?(?:status:?)?(?:\*\*)?:?\s*`?(open|partial|solved|closed-negative|found-solved|blocked|offline-only)\b",
                         ln, re.I)
            if m:
                c[m.group(1).lower()] += 1
                break
    return c


# ------------------------------------------------------------------ HTML

CSS = """
:root{--bg:#fbfaf7;--fg:#1d1d1f;--muted:#55565c;--rule:#d9d6cf;--card:#ffffff;--accent:#0b3d91;--accent2:#8a4b00;--tint:#eef2fa}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#141518;--fg:#ececef;--muted:#a9abb3;--rule:#33353b;
 --card:#1c1e22;--accent:#9cc2ff;--accent2:#f2b46b;--tint:#1f2633}}
:root[data-theme="dark"]{--bg:#141518;--fg:#ececef;--muted:#a9abb3;--rule:#33353b;--card:#1c1e22;--accent:#9cc2ff;--accent2:#f2b46b;--tint:#1f2633}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 Georgia,"Iowan Old Style","Palatino Linotype",serif}
main{max-width:980px;margin:0 auto;padding:24px 16px 64px}
h1{font-size:1.9rem;line-height:1.2;margin:.2em 0 .3em}
h2{font-size:1.3rem;margin:1.8em 0 .5em;border-bottom:1px solid var(--rule);padding-bottom:.2em}
h3{font-size:1.05rem;margin:1.2em 0 .3em}
a{color:var(--accent)}
nav.top{font:14px/1.4 system-ui,sans-serif;display:flex;gap:16px;flex-wrap:wrap;border-bottom:1px solid var(--rule);padding-bottom:8px}
.lede{color:var(--muted);max-width:44em}
.mock{font:13px/1.4 system-ui,sans-serif;border:2px dashed var(--accent2);color:var(--fg);padding:8px 12px;margin:12px 0}
.counts{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:10px;margin:16px 0}
.count{background:var(--card);border:1px solid var(--rule);padding:10px 12px}
.count b{display:block;font-size:1.7rem;font-family:system-ui,sans-serif}
.count span{font:13px/1.35 system-ui,sans-serif;color:var(--muted)}
.item{background:var(--card);border:1px solid var(--rule);border-left:4px solid var(--accent);padding:10px 14px;margin:10px 0}
.item h3{margin:0 0 4px}
.meta{font:13px/1.45 system-ui,sans-serif;color:var(--muted);margin:2px 0}
.meta b{color:var(--fg);font-weight:600}
.gist{margin:6px 0 0}
.gist em{font:12px system-ui,sans-serif;color:var(--muted);font-style:normal}
blockquote{margin:8px 0;padding:8px 12px;background:var(--tint);border-left:4px solid var(--accent2)}
dl{display:grid;grid-template-columns:minmax(120px,190px) 1fr;gap:6px 14px;font:14px/1.45 system-ui,sans-serif}
dt{color:var(--muted)} dd{margin:0;overflow-wrap:anywhere}
.small{font:13px/1.45 system-ui,sans-serif;color:var(--muted)}
details summary{cursor:pointer;color:var(--accent);font:14px system-ui,sans-serif}
section.page{border-top:3px double var(--rule);margin-top:40px;padding-top:8px}
@media (max-width:560px){dl{grid-template-columns:1fr}dt{margin-top:6px}h1{font-size:1.5rem}}
"""
MARKS = {"accent": "#0b3d91", "accent2": "#8a4b00"}  # navy + brown-orange (Okabe-Ito-safe pair); meaning always carried by text


def page(title, body, mock=True, nav_prefix=""):
    banner = ('<p class="mock">Mock-up for review, generated 9 October 2026 from the repository\'s audit files. Not published, '
              'not linked from anywhere; wording and layout are for the owner to judge.</p>') if mock else ""
    nav = (f'<nav class="top"><a href="{nav_prefix}index.html">Catalogue</a><a href="{nav_prefix}how-to-read.html">How to read this</a>'
           f'<a href="{nav_prefix}credits.html">Credits</a><a href="{REPO_TREE}">Repository</a></nav>')
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{E(title)}</title><style>{CSS}</style></head><body><main>{nav}{banner}{body}</main></body></html>\n')


def count_cards(items, ns, results):
    out = ['<div class="counts">']
    for key, head, expl in CLASSES:
        docs = {d for it in items if it["cls"] == key for d in ns["docs_of"](it["row"])}
        out.append(f'<div class="count"><b>{len(docs)}</b>{E(head)}<br><span>{E(expl)}</span></div>')
    out.append("</div>")
    return "".join(out)


def index_row(it, href):
    n = it["n"]
    meta = []
    if it["holder"]:
        meta.append(f'<b>Held:</b> {E(it["holder"])}')
    if it["lang"]:
        meta.append(f'<b>Language:</b> {E(it["lang"])}')
    if n is not None:
        meta.append(f'<b>Search result:</b> N{n}, {E(NSHORT[n])}')
    if it["depth"]:
        meta.append(f'<b>Depth:</b> {E(it["depth"])}')
    if it["key"]:
        meta.append(f'<b>Key:</b> {E(it["key"])}')
    gist = (f'<p class="gist">{md(it["gist"])} <em>(interpretation)</em></p>' if it["gist"] else "")
    return (f'<div class="item"><h3><a href="{E(href)}">{E(it["title"])}</a></h3>'
            + "".join(f'<p class="meta">{m}</p>' for m in meta) + gist + "</div>")


def index_body(items, ns, results, targets, href_of):
    tc = target_counts(targets)
    body = ['<h1>Cipher letters read from the archives</h1>',
            '<p class="lede">Historical cipher letters, mostly sixteenth- to nineteenth-century diplomatic and military '
            'correspondence, read by a small research project working with AI agents. Every entry below comes from an audit '
            'file in the public repository: a separate session tried to find each reading already in print and logged where it '
            'looked. Counts are in documents. Readings are partial unless the depth line says otherwise.</p>',
            count_cards(items, ns, results),
            f'<p class="small">{tc["open"] + tc["blocked"] + tc["partial"]} targets in work (open, partial or blocked); only audited results are listed here. '
            '<a href="how-to-read.html">How to read this catalogue</a>.</p>']
    for key, head, expl in CLASSES:
        group = [it for it in items if it["cls"] == key]
        if not group:
            continue
        nd = len({d for it in group for d in ns["docs_of"](it["row"])})
        ne = f"{len(group)} {'entry' if len(group) == 1 else 'entries'}" + (f", {nd} documents" if nd != len(group) else "")
        body.append(f'<h2>{E(head)} <span class="small">({ne})</span></h2><p class="small">{E(expl)}</p>')
        if len(group) > 25:
            body.append(f'<details><summary>Show all {len(group)} entries</summary>')
            body.extend(index_row(it, href_of(it)) for it in group)
            body.append("</details>")
        else:
            body.extend(index_row(it, href_of(it)) for it in group)
    return "".join(body)


def stale_counts(safe, register):
    """True when the register line restates the safe sentence with different numbers (a count revised after the audit)."""
    nums = lambda x: set(re.findall(r"\b\d+\b", x))
    w = words(safe)
    return bool(w) and len(w & words(register)) / len(w) >= 0.8 and bool(nums(safe) - nums(register))


def item_body(it):
    n = it["n"]
    head = [f'<h1>{E(it["title"])}</h1>']
    if it["gist"]:
        head.append(f'<p class="lede">{md(it["gist"])} <em class="small">(interpretation of the reading, in English)</em></p>')
    if it["safe"]:
        head.append(f'<h2>What can be said</h2><blockquote>{md(it["safe"])}</blockquote>'
                    '<p class="small">Quoted from the verifier\'s safe sentence in AUDIT.md (internal job names removed).'
                    + (' Some counts in it predate a later revision; the current counts are in the register line below.'
                       if stale_counts(it["safe"], it["register"]) else "") + '</p>')
    else:
        head.append(f'<h2>What can be said</h2><blockquote>{md(it["register"])}</blockquote>'
                    '<p class="small">From the project\'s results register; no matching safe sentence was found in AUDIT.md for this '
                    'entry, so read the audit before quoting it.</p>')
    dl = []
    def row(k, v):
        if v:
            dl.append(f"<dt>{E(k)}</dt><dd>{v}</dd>")
    row("Held", E(it["holder"]))
    row("Language", E(it["lang"]))
    row("Outcome", E(dict((k, h) for k, h, _ in CLASSES)[it["cls"]]))
    row("Search result", E(f"N{n}: {NWORDS[n]}") if n is not None else "")
    row("Depth", E(it["depth"]))
    row("Key", E(it["key"]))
    aud = it["audit_status"] or ""
    row("Audits", E(f"{aud}; each verified by a separate session" if aud else "")
        + (f'<br><span class="small">audit entries in this folder\'s AUDIT.md dated {E(", ".join(dict.fromkeys(it["audit_dates"])))}</span>' if it["audit_dates"] else ""))
    row("Result recorded", E(it["result_date"]))
    head.append("<h2>Record</h2><dl>" + "".join(dl) + "</dl>")
    links = []
    def lk(k, v):
        if v:
            links.append(f"<dt>{E(k)}</dt><dd>{v}</dd>")
    lk("Primary source (image or holder's record)", link_or_text(it["image"]) or "linked from the folder's NOTES.md")
    lk("Printed edition", link_or_text(it["edition"]))
    lk("Repository folder", f'<a href="{REPO_TREE}ciphers/{E(it["folder"])}">ciphers/{E(it["folder"])}</a>')
    lk("Audit and search log", f'<a href="{REPO_BLOB}ciphers/{E(it["folder"])}/AUDIT.md">AUDIT.md</a>')
    lk("Reading", link_or_text(it["reading"]))
    lk("Decode script", E(it["script"]) + (" (regenerates the reading and fails if it is stale)" if it["script"] else ""))
    head.append("<h2>Check it yourself</h2><dl>" + "".join(links) + "</dl>")
    head.append(f'<h2>Register line</h2><p class="small">{md(it["register"])}</p>')
    return "".join(head)


HOWTO = """<h1>How to read this catalogue</h1>
<h2>Search result (N0 to N5)</h2><p>Before a reading is described anywhere as new, a separate session, not the one that made the
reading, searches for it in print: the standard editions and calendars, the writer's and recipient's printed correspondence, the
holding archive's catalogue, full-text libraries and the scholarship indexes. It logs every source family it searched. The class
records what that search found; it is a search result, never a claim of discovery.</p><dl>{nw}</dl>
<p>A reading is counted in the catalogue's headline figures only after two such audits, and only from depth D2 up.</p>
<h2>Depth (D0 to D4)</h2><dl>
<dt>Fragments read (D1)</dt><dd>Scattered words, no connected stretch long enough to rule out chance.</dd>
<dt>Partially deciphered (D2)</dt><dd>At least one connected clause reads, and the verifier can state one true, specific sentence about the content. The percentage is the share of cipher signs read from a key, a known text or a controlled cryptanalytic step.</dd>
<dt>Largely deciphered (D3)</dt><dd>80% or more of the cipher signs read that way, the gaps mostly names and code groups, with an outside check.</dd>
<dt>Deciphered (D4)</dt><dd>Every cipher letter read; only listed name codes left, with a fresh independent re-derivation.</dd></dl>
<h2>Key</h2><dl>
<dt>Key recovered by us</dt><dd>By cryptanalysis, by lining up a plain copy, or by identifying the code book.</dd>
<dt>Period key</dt><dd>Rebuilt from a decipherment, key sheet or cipher book of the time.</dd>
<dt>Published key</dt><dd>Someone else's modern key, applied by us and credited on the item page and in the audit.</dd></dl>
<h2>The one-line gist</h2><p>Marked "(interpretation)": an English paraphrase of what the read passage says, written by the verifier.
It is not a translation of the whole letter, and unread groups are not guessed.</p>
<h2>Where this comes from</h2><p>Every page is generated by a script from the repository's audit files and results register; nothing is
written by hand here. Each item links its primary image, the printed edition where one exists, the audit with its search log, the
reading and the script that regenerates it.</p>"""

CREDITS = """<h1>Credits</h1>
<p>This work stands on other people's keys, catalogues and methods.</p><dl>
<dt>Satoshi Tomokiyo</dt><dd>Cryptiana (<a href="http://cryptiana.web.fc2.com/code/crypto.htm">cryptiana.web.fc2.com</a>): the lists of
historical ciphers this project started from, and published keys, among them the 1572 Nevers-Birago key used for several entries.</dd>
<dt>David Bourdeau</dt><dd><a href="https://github.com/dbourdeau/cyphersolver">cyphersolver</a> (code MIT, text CC BY 4.0): verified keys and
a catalogue whose shape this one follows; cited, not copied.</dd>
<dt>Ahmet Aymeloglu</dt><dd><a href="https://github.com/aaymeloglu/unsolved-ciphers">unsolved-ciphers</a>: status records consulted before
work began; cited, no code used.</dd>
<dt>George Lasry, Norbert Biermann and Satoshi Tomokiyo</dt><dd>"Deciphering Mary Stuart's lost letters from 1578-1584", <i>Cryptologia</i>
47 (2023): the method followed for key sheets, nomenclature and pile work.</dd>
<dt>Published and period keys</dt><dd>{keys}</dd>
<dt>Holding archives</dt><dd>The Bibliothèque nationale de France (Gallica), the Huntington Library, the Huygens Institute (Willem van
Oranje correspondence), the Sächsisches Hauptstaatsarchiv Dresden and the other holders named on each item page, whose images are linked,
never copied.</dd></dl>"""


KEY_CREDITS = [  # (pattern, credit) -- a published key is credited when the row or its AUDIT.md key-source lines name its maker
    (r"Krauske", "Dr. Krauske's 1893 manuscript key table (SHStA Dresden, Loc. 694/10)"),
    (r"Tomokiyo", "Satoshi Tomokiyo's published keys (Cryptiana)"),
    (r"Lasry", "George Lasry's published key"),
    (r"Bourdeau", "David Bourdeau's verified keys (cyphersolver)"),
]


def keys_credit(items):
    used = Counter()
    for it in items:
        if "published" not in str(it["row"].get("key")):
            continue
        txt, _ = safe_sentences(it["folder"])
        keylines = "\n".join(l for l in txt.splitlines() if re.search(r"key source|from a key source|key:", l, re.I))
        hay = " ".join(str(it["row"].get(k, "")) for k in ("grade", "title", "line")) + "\n" + keylines
        for pat, credit in KEY_CREDITS:
            if re.search(pat, hay):
                used[credit] += 1
    return "; ".join(f"{c} (applied in {n} {'entry' if n == 1 else 'entries'})" for c, n in used.most_common()) \
        or "named on each item page"


def write_site(out, items, ns, results, targets):
    if os.path.abspath(out).startswith(os.path.abspath("docs")):
        sys.exit("refused: docs/ is the GitHub Pages folder; the catalogue is a mock-up (owner, 9 Oct 2026)")
    os.makedirs(os.path.join(out, "items"), exist_ok=True)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(
        page("Cipher letters read", index_body(items, ns, results, targets, lambda it: "items/" + it["file"])))
    for it in items:
        open(os.path.join(out, "items", it["file"]), "w", encoding="utf-8").write(
            page(it["title"][:80], item_body(it), nav_prefix="../"))
    nw = "".join(f"<dt>N{k}</dt><dd>{E(v)}</dd>" for k, v in NWORDS.items())
    open(os.path.join(out, "how-to-read.html"), "w", encoding="utf-8").write(page("How to read this", HOWTO.format(nw=nw)))
    open(os.path.join(out, "credits.html"), "w", encoding="utf-8").write(page("Credits", CREDITS.format(keys=E(keys_credit(items)))))


def write_mockup(path, items, ns, results, targets, picks):
    chosen = []
    for p in picks:
        hit = next((it for it in items if p.lower() in it["title"].lower()), None)
        if hit is None:  # a named row the board does not count: render it anyway, labelled
            r = next((r for r in results if p.lower() in r.get("title", "").lower()), None)
            if r is None:
                sys.exit(f"--mockup-items: no result row matches {p!r}")
            extra = build_items([r], {**ns, "counted": lambda x: False, "counted_fragments": lambda x: False,
                                     "counted_key": lambda x: True})[0]
            extra["file"] = "x-" + slugify(extra["title"], 40) + ".html"
            extra["not_counted"] = True
            hit = extra
        chosen.append(hit)
    ids = {it["file"]: "item-" + str(i) for i, it in enumerate(chosen)}
    href = lambda it: "#" + ids[it["file"]] if it["file"] in ids else "#not-in-mockup"
    body = [index_body(items, ns, results, targets, href)]
    for it in chosen:
        note = ('<p class="mock">This entry is not among the board\'s counted items (a key checked against a text already in print, '
                'audited but below the counting rule). Shown because the review asked for it.</p>') if it.get("not_counted") else ""
        body.append(f'<section class="page" id="{ids[it["file"]]}"><p class="small">Item page, shown inline</p>{note}{item_body(it)}</section>')
    nw = "".join(f"<dt>N{k}</dt><dd>{E(v)}</dd>" for k, v in NWORDS.items())
    body.append(f'<section class="page" id="not-in-mockup">{HOWTO.format(nw=nw)}</section>')
    body.append(f'<section class="page">{CREDITS.format(keys=E(keys_credit(items)))}</section>')
    html_ = page("Cipher letters read (mock-up)", "".join(body)).replace('href="index.html"', 'href="#"') \
        .replace('href="how-to-read.html"', 'href="#not-in-mockup"').replace('href="credits.html"', 'href="#credits"')
    html_ = html_.replace('<section class="page"><h1>Credits', '<section class="page" id="credits"><h1>Credits')
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w", encoding="utf-8").write(html_)
    return chosen


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="research/mockups/catalogue/")
    ap.add_argument("--status", default="status.json")
    ap.add_argument("--mockup", default="")
    ap.add_argument("--mockup-items", nargs="*", default=["Gramont to Montmorency", "Loc. 694/08 f.410", "WVO 5797"])
    a = ap.parse_args(argv)
    for p in (a.out, a.mockup):
        if p and os.path.abspath(p).startswith(os.path.abspath("docs") + os.sep):
            sys.exit("refused: docs/ is the GitHub Pages folder; the catalogue is a mock-up (owner, 9 Oct 2026)")
    st = json.load(open(a.status, encoding="utf-8"))
    results, targets = st.get("results", []), st.get("targets", [])
    ns = board_rules()
    items = build_items(results, ns)
    write_site(a.out, items, ns, results, targets)
    counts = {k: len({d for it in items if it["cls"] == k for d in ns["docs_of"](it["row"])}) for k, _, _ in CLASSES}
    msg = (f"catalogue: {len(items)} entries -> {a.out}; documents: " + " / ".join(f"{counts[k]} {h.lower()}" for k, h, _ in CLASSES)
           + f"; safe sentence matched in AUDIT.md for {sum(1 for it in items if it['safe'])} of {len(items)}")
    if a.mockup:
        chosen = write_mockup(a.mockup, items, ns, results, targets, a.mockup_items)
        msg += f"; mock-up {a.mockup} with {len(chosen)} item pages"
    print(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
