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

Sample layout v2 (owner's review, 9 Oct 2026 22:4x UTC; SHOWCASE): for the three review items the page opens on line crops of the
cipher (research/mockups/catalogue/img/, cut from the folders' own crops or, for WVO 5797, from the Huygens PDF) with the reading
token by token under each line (blue band = read H/C/S, vermilion = uncertain M, grey dashed = unread U; the letter is printed too),
then the claim, the gist, a context strip (events and names marked "context" where they come from general history, not the audit),
badges, a grade bar and one-line links. Every other item keeps the v1 layout until the owner chooses.

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
    s = re.sub(r"\bworker [A-Z0-9]+(?:'s)?", "an earlier pass", s)
    s = re.sub(r"\b[A-Z]{1,3}\d{1,3}[A-Z]?'s\b", "an earlier", s)
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
    def idt(x):  # item identifiers: frame, folio, number, WVO, day+month (years are shared by siblings, so not used)
        ids = set(re.findall(r"\b(?:frame \d{4}|f\.\s?\d+[rv]?|no\.\s?\d+|WVO \d+|E\d+)\b", x))
        ids |= {f"{d} {m[:3].lower()}" for d, m in re.findall(rf"\b(\d{{1,2}}) ({MONTHS})", x)}
        return ids
    tid = idt(r.get("title", "") + " " + r.get("document_id", ""))
    # a sentence that names other items (frames, folios, numbers) and none of this one's belongs to a sibling item
    cands = [c for c in cands if not (idt(c) and tid and not (idt(c) & tid))]
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
.filters{display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;font:14px system-ui,sans-serif;margin:12px 0}
.filters select{font:inherit;padding:2px 4px;max-width:260px}
table.cat{width:100%;border-collapse:collapse;font:14px/1.4 system-ui,sans-serif}
table.cat th{text-align:left;border-bottom:2px solid var(--rule);padding:6px 6px;font-weight:600}
table.cat td{border-bottom:1px solid var(--rule);padding:6px;vertical-align:top}
blockquote.claim{font-size:1.08rem}
details{border:1px solid var(--rule);background:var(--card);margin:6px 0;padding:6px 10px}
details .det{font:14px/1.5 system-ui,sans-serif;padding:4px 0}
code{font:13px ui-monospace,Menlo,monospace;background:var(--tint);padding:1px 4px;overflow-wrap:anywhere}
@media (max-width:760px){table.cat thead{display:none}table.cat tr{display:block;border:1px solid var(--rule);background:var(--card);margin:8px 0;padding:4px 8px}
 table.cat td{display:block;border:0;padding:2px 0}table.cat td:empty{display:none}table.cat td::before{content:attr(data-l) ": ";color:var(--muted);font-size:12px}}
@media (max-width:560px){dl{grid-template-columns:1fr}dt{margin-top:6px}h1{font-size:1.5rem}}
"""
MARKS = {"accent": "#0b3d91", "accent2": "#8a4b00"}  # navy + brown-orange (Okabe-Ito-safe pair); meaning always carried by text


def page(title, body, mock=True, nav_prefix=""):
    banner = ('<p class="mock">Mock-up for review, generated 9 October 2026 from the repository\'s audit files. Not published, '
              'not linked from anywhere; wording and layout are for the owner to judge.</p>') if mock else ""
    nav = (f'<nav class="top"><a href="{nav_prefix}index.html">Catalogue</a><a href="{nav_prefix}attention.html">Readings worth attention</a><a href="{nav_prefix}how-to-read.html">How to read this</a>'
           f'<a href="{nav_prefix}credits.html">Credits</a><a href="{REPO_TREE}">Repository</a></nav>')
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{E(title)}</title><style>{CSS}{CSS_V2}</style></head><body><main>{nav}{banner}{body}</main></body></html>\n')


ARCHIVES = [  # (pattern in holder/title/folder, archive label) -- first match wins
    (r"\bBnF\b|Bibliothèque nationale|\bfr\.\s?\d|Clairambault|Baluze|Mélanges de Colbert|Espagnol 14", "Bibliothèque nationale de France"),
    (r"SHStA|Dresden", "Sächsisches Hauptstaatsarchiv Dresden"),
    (r"Huntington|\bmss[A-Z]{2}|eckert", "Huntington Library"),
    (r"\bWVO\b|\bKHA\b|nassau|saksen", "Royal House Archive, The Hague"),
    (r"Nationaal Archief", "Nationaal Archief, The Hague"),
    (r"\bBL\b|British Library", "British Library"),
    (r"Birch|Thurloe", "printed in Birch, Thurloe State Papers (1742)"),
    (r"Oxenstierna", "printed in Rikskanslern Axel Oxenstiernas skrifter"),
    (r"Linhares|ANTT|Torre do Tombo", "Torre do Tombo, Lisbon"),
    (r"Hellen|Frederick", "Geheimes Staatsarchiv, Berlin"),
]
MONTHS = r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?"


def archive_of(it):
    hay = " ".join((it["holder"], it["title"], it["folder"]))
    for pat, label in ARCHIVES:
        if re.search(pat, hay, re.I if pat.islower() else 0):
            return label
    return ""


def year_of(it):
    m = re.search(r"\b(1[4-8]\d\d)\b", it["title"] + " " + it["holder"])
    return int(m.group(1)) if m else None


def parties(it):
    """(sender, recipient, place, date) read from the item's title; blanks where the title does not say."""
    t = re.sub(r"^[^:]*?\b(?:BnF|SHStA|BL)\b[^,:]*?(?:,|:)\s*", "", it["title"]) if re.match(r"^(?:BnF|SHStA|BL)\b", it["title"]) else it["title"]
    t = t.split(":")[0]
    m = re.match(r"\s*(?P<f>[^,()]+?) to (?P<t>[^,()]+?)(?:,\s*(?P<rest>.*))?$", t)
    if not m:
        return "", "", "", ""
    rest = m.group("rest") or ""
    d = re.search(rf"((?:c\.\s*|about\s+)?(?:\d{{1,2}}(?:/\d{{1,2}})?\s+)?(?:{MONTHS}\s+)?\[?\d{{4}}\]?)", rest)
    date = d.group(1) if d else ""
    place = rest[:d.start()].strip(" ,") if d else ""
    place = re.sub(r"\(.*", "", place).strip(" ,")
    if re.search(r"\d", place) or len(place) > 40:
        place = ""
    return m.group("f").strip(), m.group("t").strip(), place, date


def thumb(it, inline):
    sc = showcase_for(it)
    if not sc:
        return ""
    src = img_src(sc["crops"][0][0][0], inline)
    return f'<img class="thumb" alt="cipher line" src="{src if inline else src.replace("../img/", "img/")}">'


def ten_words(s, n=10):
    w = (s or "").split()
    return " ".join(w[:n]) + (" ..." if len(w) > n else "")


def count_cards(items, ns, results):
    out = ['<div class="counts">']
    for key, head, expl in CLASSES:
        docs = {d for it in items if it["cls"] == key for d in ns["docs_of"](it["row"])}
        out.append(f'<div class="count"><b>{len(docs)}</b>{E(head)}<br><span>{E(expl)}</span></div>')
    out.append("</div>")
    return "".join(out)


FILTER_JS = """<script>
(function(){var f=document.querySelectorAll('select[data-f]');function go(){var v={};f.forEach(function(s){v[s.dataset.f]=s.value});
var n=0;document.querySelectorAll('tr[data-century]').forEach(function(r){var ok=Object.keys(v).every(function(k){return !v[k]||r.dataset[k]===v[k]});
r.hidden=!ok;if(ok)n++});document.getElementById('shown').textContent=n}f.forEach(function(s){s.addEventListener('change',go)});})();
</script>"""


def index_body(items, ns, results, targets, href_of, inline=False):
    tc = target_counts(targets)
    cls_head = dict((k, h) for k, h, _ in CLASSES)
    rows, cents, archs = [], Counter(), Counter()
    for it in items:
        y = year_of(it)
        cent = f"{(y - 1) // 100 + 1}th century" if y else "undated"
        arch = archive_of(it) or "other"
        cents[cent] += 1
        archs[arch] += 1
        f, t, place, date = parties(it)
        n = it["n"]
        rows.append(
            f'<tr data-century="{E(cent)}" data-archive="{E(arch)}" data-outcome="{E(it["cls"])}">'
            f'<td data-l="Date">{E(date or (str(y) if y else ""))}</td>'
            f'<td data-l="From / to">{E(f) + " &rarr; " + E(t) if f else ""}</td>'
            f'<td data-l="Place">{E(place)}</td>'
            f'<td data-l="Held">{E(arch)}<br><span class="small">{E(ten_words(it["holder"], 14))}</span></td>'
            f'<td data-l="Language">{E(it["lang"])}</td>'
            f'<td data-l="What it says">{thumb(it, inline)}<a href="{E(href_of(it))}">{E(ten_words(it["gist"]) or ten_words(it["title"], 12))}</a></td>'
            f'<td data-l="Outcome">{E(cls_head[it["cls"]])}</td>'
            f'<td data-l="Search result">{E("N%d" % n if n is not None else "")}</td>'
            f'<td data-l="Depth">{E(it["depth"].split(" (")[0])}</td></tr>')
    sel = lambda name, label, opts: (f'<label>{E(label)} <select data-f="{name}"><option value="">all</option>'
                                     + "".join(f'<option value="{E(k)}">{E(lab)} ({c})</option>' for k, lab, c in opts) + "</select></label>")
    filters = ('<div class="filters">'
               + sel("century", "Century", [(k, k, c) for k, c in sorted(cents.items())])
               + sel("archive", "Archive", [(k, k, c) for k, c in archs.most_common()])
               + sel("outcome", "Outcome", [(k, h, sum(1 for it in items if it["cls"] == k)) for k, h, _ in CLASSES])
               + f'<span class="small"><span id="shown">{len(items)}</span> of {len(items)} entries shown</span></div>')
    return "".join([
        '<h1>Cipher letters read from the archives</h1>',
        '<p class="lede">Each entry is a historical cipher letter we read, in part or in full. On every item page the claim comes '
        'first, in one plain sentence, and the proof sits directly underneath it: which signs were read and how, the script that '
        'regenerates the reading, the control it had to beat, the two independent audits that searched for it in print, and links '
        'to the manuscript image and the printed edition, so that a reader can check each step from their own desk.</p>',
        count_cards(items, ns, results),
        f'<p class="small">Counts are in documents. {tc["open"] + tc["blocked"] + tc["partial"]} targets in work (open, partial or '
        'blocked); only audited results are listed here. <a href="attention.html">Readings worth a historian\'s attention</a> &middot; '
        '<a href="how-to-read.html">How to read this</a>.</p>',
        filters,
        '<table class="cat"><thead><tr><th>Date</th><th>From / to</th><th>Place</th><th>Held</th><th>Language</th>'
        '<th>What it says</th><th>Outcome</th><th>Search result</th><th>Depth</th></tr></thead><tbody>',
        "".join(rows), "</tbody></table>", FILTER_JS])


def stale_counts(safe, register):
    """True when the register line restates the safe sentence with different numbers (a count revised after the audit)."""
    nums = lambda x: set(re.findall(r"\b\d+\b", x))
    w = words(safe)
    return bool(w) and len(w & words(register)) / len(w) >= 0.8 and bool(nums(safe) - nums(register))


GRADE_KEY = ("H read from a key of the time or a published key; C from a known plain text; S by cryptanalysis that beat a "
             "matched control; M uncertain; I inferred or repaired; U not read.")


def grade_counts(r):
    hay = " ".join(str(r.get(k) or "") for k in ("grade", "completeness", "depth_note", "line", "unresolved_spans"))
    best = []
    for m in re.finditer(r"(?:\b[HCSMIU] ?\d+(?:[,;]| and)? ?){2,}", hay):
        pairs = re.findall(r"\b([HCSMIU]) ?(\d+)", m.group(0))
        if len(pairs) > len(best):
            best = pairs
    return best


def control_lines(r):
    hay = ". ".join(str(r.get(k) or "").rstrip(". ") for k in ("grade", "depth_check", "line"))
    out = []
    for c in re.split(r";\s+|\.\s+(?=[A-Z0-9])", hay):
        if re.search(r"shuffl|control|null|\bp9[59]\b|beats? \d+ of \d+", c, re.I):
            c = sanitize(c)
            if c and c not in out:
                out.append(c)
    return out[:4]


def search_log(fold, limit=10):
    txt, _ = safe_sentences(fold)
    searched, unreach = [], []
    for ln in txt.splitlines():
        s = ln.strip(" -*|")
        if len(s) < 25:
            continue
        if re.search(r"unreachable|not reachable|could not (?:be )?open|403|429|Cloudflare", s, re.I):
            unreach.append(sanitize(s)[:240])
        elif re.search(r"\*\*Searched|\bSearched\b|searched in full|read page by page|full-text", ln):
            searched.append(sanitize(s)[:240])
    dedup = lambda xs: list(dict.fromkeys(x for x in xs if x))[:limit]
    return dedup(searched), dedup(unreach)


def files_of(fold):
    d = os.path.join("ciphers", fold)
    fs = sorted(os.listdir(d)) if os.path.isdir(d) else []
    pick = lambda pat: [f for f in fs if re.match(pat, f) and os.path.isfile(os.path.join(d, f))][:4]
    return pick(r"ciphertext.*\.(txt|tsv)$"), pick(r"key.*\.(tsv|md)$")


def other_solvers(fold):
    txt = notes_head(fold) + safe_sentences(fold)[0]
    return sorted(set(re.findall(r"https?://dbourdeau\.github\.io/cyphersolver/[\w-]+\.html", txt))
                  - {"https://dbourdeau.github.io/cyphersolver/catalogue.html"})[:3]


def det(summary, inner, open_=False):
    return f'<details{" open" if open_ else ""}><summary>{E(summary)}</summary><div class="det">{inner}</div></details>'


def item_body(it, howto="how-to-read.html", credits="credits.html"):
    r, n, fold = it["row"], it["n"], it["folder"]
    f, t, place, date = parties(it)
    out = [f'<h1>{E(it["title"])}</h1>']
    # 1. the claim
    if it["safe"]:
        claim = (f'<blockquote class="claim">{md(it["safe"])}</blockquote><p class="small">The verifier\'s safe sentence, quoted from '
                 f'<a href="{REPO_BLOB}ciphers/{E(fold)}/AUDIT.md">AUDIT.md</a>.'
                 + (' Some counts in it predate a later revision; the current ones are in the grades below.'
                    if stale_counts(it["safe"], it["register"]) else "") + "</p>")
    else:
        claim = (f'<blockquote class="claim">{md(it["register"])}</blockquote><p class="small">From the results register; no '
                 'matching safe sentence was found in AUDIT.md for this entry, so read the audit before quoting it.</p>')
    out.append('<h2>The claim</h2>' + claim)
    if it["gist"]:
        out.append(f'<p class="gist">{md(it["gist"])} <em>(interpretation: the verifier\'s English paraphrase of the read passage)</em></p>')
    # the letter, plain
    dl = []
    def row(k, v):
        if v:
            dl.append(f"<dt>{E(k)}</dt><dd>{v}</dd>")
    row("From", E(f)); row("To", E(t)); row("Place", E(place)); row("Date", E(date))
    row("Held", E(archive_of(it)) + (f'<br><span class="small">{E(it["holder"])}</span>' if it["holder"] else ""))
    row("Language", E(it["lang"]))
    row("Manuscript image", link_or_text(it["image"]) or "linked from the folder's NOTES.md")
    row("Printed edition", link_or_text(it["edition"]))
    row("Outcome", E(dict((k, h) for k, h, _ in CLASSES)[it["cls"]]))
    row("Search result", (E(f"N{n}: {NWORDS[n]}") if n is not None else "") + f' <a class="small" href="{howto}#n-class">what this means</a>')
    row("Depth", E(it["depth"]) + f' <a class="small" href="{howto}#depth">what this means</a>' if it["depth"] else "")
    row("Key", E(it["key"]) + f' <a class="small" href="{howto}#key">what this means</a>' if it["key"] else "")
    out.append("<h2>The letter</h2><dl>" + "".join(dl) + "</dl>")
    # 2. the proof
    proof = []
    g = grade_counts(r)
    if g:
        tot = sum(int(v) for _, v in g)
        proof.append(det(f"Signs read, by grade: " + ", ".join(f"{k} {v}" for k, v in g) + f" (of {tot})",
                         f'<p>{E(GRADE_KEY)}</p><p class="small">Counted by the decode script over every cipher token; '
                         'the reading and its per-token grades are in the repository.</p>'))
    ct, keys = files_of(fold)
    reg = [f'<li>Transcription: ' + ", ".join(f'<a href="{REPO_BLOB}ciphers/{E(fold)}/{E(x)}">{E(x)}</a>' for x in ct) + "</li>" if ct else "",
           f'<li>Key: ' + ", ".join(f'<a href="{REPO_BLOB}ciphers/{E(fold)}/{E(x)}">{E(x)}</a>' for x in keys) + "</li>" if keys else "",
           f'<li>Reading: {link_or_text(it["reading"])}</li>' if it["reading"] else ""]
    cmd = (f"python3 ciphers/{fold}/decode.py --check" if it["script"].startswith("decode.py")
           else f"python3 tools/decode_key.py ciphers/{fold} --check" if it["script"] else "")
    proof.append(det("How the reading regenerates", "<ul>" + "".join(reg) + "</ul>"
                     + (f'<p>Run <code>{E(cmd)}</code> from a clone of the repository: it rebuilds the reading from the transcription '
                        'and the key, and exits with an error if the committed reading is stale.</p>' if cmd else
                        '<p>No decode script is recorded in this folder; see AUDIT.md.</p>')))
    cl = control_lines(r)
    proof.append(det("The control it had to beat", ("<ul>" + "".join(f"<li>{md(c)}</li>" for c in cl) + "</ul>"
                     '<p class="small">A reading counts only beside a matched control: the same method run on shuffled keys or a '
                     'synthetic text of the same kind, with both numbers reported.</p>') if cl else
                     '<p>No control figure is recorded on the register row; the audit file gives the checks used.</p>'))
    searched, unreach = search_log(fold)
    aud = it["audit_status"] or "no audit status recorded"
    dates = ", ".join(dict.fromkeys(it["audit_dates"]))
    proof.append(det(f"Audits: {aud}, each by a separate session",
                     f'<p>Each audit was written by a session that did not make the reading and tried to find it already in print. '
                     f'Audit entries in this folder are dated {E(dates) or "as recorded in AUDIT.md"}.</p>'
                     + (f'<p><b>Searched</b> (from this folder\'s audit log; the full log is in '
                        f'<a href="{REPO_BLOB}ciphers/{E(fold)}/AUDIT.md">AUDIT.md</a>):</p><ul>'
                        + "".join(f"<li>{md(s)}</li>" for s in searched) + "</ul>" if searched else "")
                     + ('<p><b>Unreachable or blocked</b>:</p><ul>' + "".join(f"<li>{md(s)}</li>" for s in unreach) + "</ul>"
                        if unreach else "")))
    others = other_solvers(fold)
    proof.append(det("Whose key, and credit",
                     f'<p>{E(it["key"] or "not recorded")}. Credits for published keys are on the <a href="{credits}">credits page</a>.</p>'
                     + ("<p>Other solvers' pages cited in this folder: " + ", ".join(f'<a href="{E(u)}">{E(u)}</a>' for u in others)
                        + ". Where another solver read this item first, the audit says so and our reading is an independent "
                          "re-reading.</p>" if others else "")))
    out.append('<h2>The proof</h2><p class="small">Open each line for the evidence. Nothing is hidden; the repository holds every file.</p>'
               + "".join(proof))
    out.append(f'<p class="small">Repository folder: <a href="{REPO_TREE}ciphers/{E(fold)}">ciphers/{E(fold)}</a> &middot; '
               f'result recorded {E(it["result_date"])}.</p>')
    return "".join(out)


STORIES = [  # (title substring of the item, heading, story). Each story says only what the item's audit and register license;
    # checked against the safe sentence and the register row on 9 Oct 2026. Anything outside them is marked (context).
    ("Elector August to Orange, Torgau 18 Nov 1561", "An imperial election, asked for in secret (1561)",
     "In November 1561 Elector August of Saxony wrote to William of Orange from Torgau and put part of the letter in a cipher "
     "enclosure. It reads with the key of Orange's 1562 cipher, rebuilt from a sibling letter's contemporary decipherment, as secret "
     "news that the Emperor had asked August to elect Maximilian King of the Romans in the Emperor's own lifetime. No prior "
     "decipherment or printed plain text was located; the printed summary of the letter covers only its clear text. August's own "
     "minute in Dresden has not been seen and may carry the enclosure in clear."),
    ("Gramont to Villandry, Rome, 20 May 1530", "Gramont in Rome, May 1530",
     "Gabriel de Gramont, bishop of Tarbes, wrote from Rome on 20 May 1530 to Villandry. Read with the published Gramont 1530 key "
     "(its values come from George Lasry's and Satoshi Tomokiyo's work, credited in the audit), the cipher passage gives several "
     "lines of continuous French: Gramont has given the bearer an article set apart, addressed to Villandry though meant for the "
     "King, and calls it 'le total fondement'. The same key, checked against Gramont's letter to Montmorency of 28 March 1530, whose "
     "period decipherment Le Grand printed in 1688, agrees with the printed text far above chance. No printed plain text or "
     "decipherment of the 20 May passage was located after two logged searches."),
    ("Loc. 694/08 f.410", "Manteuffel, Berlin, November 1712: the Queen of England",
     "Manteuffel's reports to Flemming in Dresden were deciphered in 1893 by Dr. Krauske, whose key table survives unprinted in the "
     "same archive. Applied to the postscript of a November 1712 report that carries no decipherment between its lines, the table "
     "gives French in stretches (about two thirds of the code groups). The Queen of England is named three times: once in a phrase "
     "reading 'touchant le prince', and once followed, after two unread groups, by 'ne fera rien pour lui, mais luy'. The passage is "
     "not among the printed extracts of these reports that the audits searched."),
    ("WVO 5797", "The blanks in Groen's edition (1573)",
     "When Groen van Prinsterer printed the Nassau brothers' letter to William of Orange of 22 October 1573, he left several cipher "
     "passages blank. Two of those blanks now read in part: the brothers name the Landgrave beside the Duke of Saxony, and say of the "
     "Elector Palatine that he 'helt sich wol und thut in warheit viel'. The spot was located with a letter table we recovered by "
     "cryptanalysis, and the two names come from a contemporary gloss on a sibling letter. No prior decipherment of these blanks was "
     "located; the rest of the letter is Groen's."),
    ("no.86, Lodovico Birago to the Duke of Nevers, Saluzzo, 27 August 1572", "Birago at Saluzzo, 27 August 1572",
     "Lodovico Birago wrote to the Duke of Nevers from Saluzzo on 27 August 1572, three days after the massacre of St Bartholomew in "
     "Paris (context). Read in part with Satoshi Tomokiyo's published 1572 key (629 of 758 signs read by cryptanalysis that beat its "
     "control, the rest uncertain or unread), the letter names the Huguenots, Carmagnola and the Baron des Adrets, and Birago fears "
     "that by doing service he may earn the ill favour of others. No prior decipherment was located; both volumes of the 1665 "
     "Mémoires de Nevers were searched."),
    ("Barneton", "Mercy's instruction, Barneton, 6 June 1648",
     "An instruction to the Baron de Mercy in BnF Espagnol 144 is written in a numeric code. Under a key we recovered by "
     "cryptanalysis it reads only in fragments, but the fragments are specific: Mercy is to go to Cleves to see the Elector of "
     "Brandenburg and his High Chamberlain and to propose raising three thousand infantry in two or three regiments in that country. "
     "No prior decipherment was located; the reading is fragmentary and is marked so."),
    ("Stamford to Thurloe", "Stamford at Calais, March 1655",
     "Thomas Birch printed William Stamford's letter from Calais of 13 March 1655 with its cipher numbers and no decipherment. We "
     "read it with the key given by Birch's own printed decipherments of Stamford's later letters. Thurloe's office deciphered this "
     "system in 1655, and Satoshi Tomokiyo has since reconstructed and published it; our table agrees with his on every value in this "
     "letter. The cipher says the matter came to Stamford's knowledge 'by meere chance' and 'without the least injunction of secrecy'. "
     "No prior decipherment of this letter was located, and eleven lines are still partly incoherent."),
]


def attention_body(items, href_of):
    out = ['<h1>Readings worth a historian\'s attention</h1>',
           '<p class="lede">A few readings that say something specific. Each story keeps to what the item\'s audit licenses; '
           'the item page carries the proof. Anything not in the audit is marked (context).</p>']
    for sub, head, story in STORIES:
        it = next((x for x in items if sub.lower() in x["title"].lower()), None)
        if it is None:
            continue
        out.append(f'<div class="item"><h3>{E(head)}</h3><p>{E(story)}</p><p class="meta"><b>Search result:</b> '
                   f'N{it["n"]} &middot; <b>Depth:</b> {E(it["depth"])} &middot; <a href="{E(href_of(it))}">claim and proof</a></p></div>')
    return "".join(out)


# ------------------------------------------------------------------ v2 sample pages (Amendment 4: the cipher first, context, no prose)

# Three colour families only (cvd_check PASS on both page backgrounds, 9 Oct 2026); the grade letter under every token says which
# kind of read it is, so meaning never rests on hue: blue = read (H/C/S), vermilion = uncertain (M/I), grey dashed = unread (U).
GRADE_COL = {"H": "#0072b2", "C": "#0072b2", "S": "#0072b2", "M": "#d55e00", "I": "#d55e00", "U": "#7a7a7a"}
GRADE_NAME = {"H": "key", "C": "known text", "S": "cryptanalysis", "M": "uncertain", "I": "inferred", "U": "unread"}
LICENCE = "Licence: not recorded as public domain or CC (a public version links instead)."


def _tsv(path):
    out = []
    for ln in open(path, encoding="utf-8"):
        if ln.startswith("#") or not ln.strip():
            continue
        out.append(ln.rstrip("\n").split("\t"))
    return out


def tokens_manteuffel(line):
    rows = _tsv("ciphers/sachsstaatsarchiv-manteuffel-1712/reading_tokens.tsv")
    return [(r[2], r[4].replace("?", "") or "", r[5]) for r in rows if r[0] == f"694-08_0511_f410_{line}"]


def tokens_gramont(row):
    key = {r[0]: (r[1], r[2]) for r in _tsv("ciphers/fr2980-gramont/key.tsv")[1:] if len(r) >= 3}
    codes = next(r[1] for r in _tsv("ciphers/fr2980-gramont/n12gra/recon_settled.tsv") if r[0] == row).split()
    return [(c, *(key.get(c, ("", "U")) if c != "?" else ("", "U"))) for c in codes]


def tokens_lodewijk(spot):
    fold = "ciphers/lodewijk-van-nassau-1573-74/"
    read = {(r[0], r[1]): (r[3], r[4]) for r in _tsv(fold + "reading_5797_full_tokens.tsv")[1:]}
    out = []
    for r in _tsv(fold + "ciphertext_5797.tsv"):
        if r[0] != spot:
            continue
        if r[2].startswith("="):
            out.append((r[2][1:], "(clear)", ""))
        else:
            v, g = read.get((r[0], r[1]), ("", "U"))
            out.append((r[2], "" if v in ("?",) else ("(null)" if v == "NULL" else v), g))
    return out


SHOWCASE = {
    "Gramont to Montmorency": {
        "short": "Gramont to Montmorency, Bologna, 28 March 1530",
        "who": ("Gabriel de Gramont, bishop of Tarbes", "Anne de Montmorency, grand maître", "Bologna ('Boulogne')", "28 March 1530"),
        "crops": [(["fr3040_f18rB_L04_a.jpg", "fr3040_f18rB_L04_b.jpg"], lambda: tokens_gramont("f18rB_L04"),
                   "BnF fr.3040 f.18r, cipher line 4 (two halves)")],
        "image": "https://gallica.bnf.fr/ark:/12148/btv1b9059870w/f33.item",
        "events": [("24 Feb 1530", "Clement VII crowns Charles V emperor at Bologna", True),
                   ("1529-1530", "Henry VIII's divorce suit pending before the Pope", True),
                   ("1688", "Le Grand prints this letter's period decipherment (Histoire du divorce III, pp.454-457)", False)],
        "people": [("Rochefort", "Thomas Boleyn, Henry VIII's envoy", True), ("the Pope", "Clement VII", True),
                   ("the King of England", "Henry VIII, seeking an annulment", True),
                   ("Montmorency", "Francis I's grand maître; addressee", False)],
        "edition": "Le Grand, Histoire du divorce III (1688), pp.454-457",
    },
    "Loc. 694/08 f.410": {
        "short": "Manteuffel to Flemming, Berlin, November 1712 (postscript)",
        "who": ("Ernst Christoph von Manteuffel, Saxon envoy", "Jacob Heinrich von Flemming, Saxon minister", "Berlin", "November 1712"),
        "crops": [(["f410_L13.jpg"], lambda: tokens_manteuffel("L13"), "SHStA Dresden Loc. 694/08 f.410, cipher line 13"),
                  (["f410_L14.jpg"], lambda: tokens_manteuffel("L14"), "SHStA Dresden Loc. 694/08 f.410, cipher line 14")],
        "image": "https://www.archiv.sachsen.de/archiv/bestand.jsp?guid=3a83f921-9a43-485f-874b-34653ed59b68",
        "events": [("Jan 1712 onward", "Peace congress at Utrecht", True),
                   ("1712", "Great Northern War: allied armies in Swedish Pomerania", True),
                   ("1893", "Dr. Krauske compiles the key table, never printed (Loc. 694/10)", False)],
        "people": [("the Queen of England", "Queen Anne", True), ("the prince", "not identified by the reading", False),
                   ("the Swedes", "Charles XII's side in the war", True), ("Stettin", "Swedish-held port in Pomerania", True)],
        "aside": "Oxford and Bolingbroke appear in a sibling postscript of 13 Oct 1712, not on this leaf.",
        "edition": "not in Acta Borussica, Behördenorganisation I (1894) or Droysen IV.1 (searched)",
    },
    "WVO 5797": {
        "short": "Jan and Lodewijk van Nassau to William of Orange, Dillenburg, 22 October 1573",
        "who": ("Jan and Lodewijk van Nassau", "William of Orange, their brother", "Dillenburg", "22 October 1573"),
        "crops": [(["wvo5797_p5_bey.jpg"], lambda: tokens_lodewijk("p5_spot3"), "KHA A 3, 895/I (WVO 5797), p.5: Groen's blank 'Bey ...'"),
                  (["wvo5797_p7_helt.jpg"], lambda: tokens_lodewijk("p7_spot2"), "KHA A 3, 895/I (WVO 5797), p.7: Groen's blank before 'helt sich wol'")],
        "image": "https://resources.huygens.knaw.nl/media/wvo/images/05000-05999/05797.pdf",
        "events": [("8 Oct 1573", "Spanish siege of Alkmaar lifted", True),
                   ("11 Oct 1573", "Battle of the Zuiderzee; Bossu captured", True),
                   ("1837", "Groen van Prinsterer prints the letter with the cipher left blank (Archives IV, no. CDXLIV)", False)],
        "people": [("the Landgrave", "of Hesse, Protestant prince", True), ("the Duke of Saxony", "Elector August", True),
                   ("the Pfaltzgraf", "Elector Palatine Frederick III", True), ("Groen van Prinsterer", "editor of the Orange archives", False)],
        "edition": "Groen van Prinsterer, Archives IV (1837), no. CDXLIV, pp.217-226",
    },
}


def showcase_for(it):
    """The v2 sample layout for the three review items; only when that item's own folder (and its crops) are present."""
    sc = next((v for k, v in SHOWCASE.items() if k.lower() in it["title"].lower()), None)
    if sc is None or not os.path.isdir(os.path.join("research/mockups/catalogue/img")):
        return None
    try:
        for _, toks, _ in sc["crops"]:
            toks()
    except (OSError, StopIteration):
        return None
    return sc


def token_strip(toks):
    cells = []
    for sign, val, g in toks:
        col = GRADE_COL.get(g, "#8c8c8c")
        lab = f'{g}' if g else ""
        dash = ";border-bottom-style:dashed" if g == "U" else ""
        cells.append(f'<span class="tk" style="border-bottom-color:{col}{dash}" title="{E(GRADE_NAME.get(g, "clear text"))}">'
                     f'<span class="cs">{E(sign)}</span><span class="pv">{E(val) or "&nbsp;"}</span>'
                     f'<span class="gr">{E(lab)}</span></span>')
    return '<div class="strip">' + "".join(cells) + "</div>"


def grade_bar(r):
    g = grade_counts(r)
    if not g:
        return ""
    tot = sum(int(v) for _, v in g) or 1
    segs = "".join(f'<span style="width:{100 * int(v) / tot:.1f}%;background:{GRADE_COL.get(k, "#8c8c8c")}"></span>' for k, v in g if int(v))
    leg = " &middot; ".join(f'<b>{k}</b> {v} {GRADE_NAME.get(k, "")}' for k, v in g)
    return f'<div class="bar">{segs}</div><p class="small">{leg} (of {tot} signs)</p>'


def img_src(name, inline):
    path = os.path.join("research/mockups/catalogue/img", name)
    if inline and os.path.exists(path):
        import base64
        return "data:image/jpeg;base64," + base64.b64encode(open(path, "rb").read()).decode()
    return "../img/" + name


def item_body_v2(it, sc, howto="how-to-read.html", inline=False):
    r, n, fold = it["row"], it["n"], it["folder"]
    out = [f'<h1>{E(sc["short"])}</h1>']
    for imgs, toks, cap in sc["crops"]:
        out.append('<figure class="cipher">' + "".join(f'<img alt="{E(cap)}" src="{img_src(x, inline)}">' for x in imgs)
                   + token_strip(toks()) + f'<figcaption>{E(cap)} &middot; our crop &middot; {E(LICENCE)}</figcaption></figure>')
    out.append('<p class="legend"><span class="lg" style="border-color:#0072b2">read: <b>H</b> key, <b>C</b> known text, '
               '<b>S</b> cryptanalysis</span><span class="lg" style="border-color:#d55e00"><b>M</b> uncertain</span>'
               '<span class="lg" style="border-color:#7a7a7a;border-bottom-style:dashed"><b>U</b> unread</span>'
               + f' &middot; <a href="{E(sc["image"])}">whole page at the holder</a></p>')
    stale = it["safe"] and stale_counts(it["safe"], it["register"])
    out.append(f'<blockquote class="claim">{md(it["safe"] or it["register"])}</blockquote>'
               + ('<p class="small">Counts in this audited sentence were revised since; current counts in the bar below.</p>' if stale else "")
               + ("" if it["safe"] else '<p class="small">Results-register line: no safe sentence in AUDIT.md matched this entry.</p>'))
    if it["gist"]:
        out.append(f'<p class="gist">{md(it["gist"])} <em>(interpretation)</em></p>')
    f, t, place, date = sc["who"]
    out.append(f'<div class="ctx"><div><span class="k">From</span> {E(f)}</div><div><span class="k">To</span> {E(t)}</div>'
               f'<div><span class="k">At</span> {E(place)}</div><div><span class="k">Date</span> {E(date)}</div></div>')
    ctxmark = lambda c: ' <span class="cx">context</span>' if c else ""
    out.append('<div class="two"><div><h3>Around it</h3><ul class="tl">'
               + "".join(f'<li><b>{E(d)}</b> {E(e)}{ctxmark(c)}</li>' for d, e, c in sc["events"]) + '</ul></div>'
               '<div><h3>Named in the cipher</h3><ul class="tl">'
               + "".join(f'<li><b>{E(p)}</b> {E(w)}{ctxmark(c)}</li>' for p, w, c in sc["people"]) + "</ul>"
               + (f'<p class="small">{E(sc["aside"])}</p>' if sc.get("aside") else "") + "</div></div>")
    dates = list(dict.fromkeys(it["audit_dates"]))
    badges = [f'<a class="badge" href="{howto}#n-class">N{n} {E(NSHORT[n])}</a>' if n is not None else "",
              f'<a class="badge" href="{howto}#depth">{E(it["depth"])}</a>' if it["depth"] else "",
              f'<a class="badge" href="{howto}#key">{E(it["key"])}</a>' if it["key"] else ""]
    badges += [f'<span class="badge">audit {E(d)}</span>' for d in dates[:2]]
    out.append('<p class="badges">' + "".join(badges) + "</p>" + grade_bar(r))
    cmd = (f"python3 ciphers/{fold}/decode.py --check" if it["script"].startswith("decode.py")
           else f"python3 tools/decode_key.py ciphers/{fold} --check")
    cl = control_lines(r)
    searched, unreach = search_log(fold, 30)
    out.append('<ul class="links">'
               f'<li>Regenerate: <code>{E(cmd)}</code></li>'
               + (f'<li>Control: {md(cl[0])}</li>' if cl else "")
               + f'<li>Edition: {E(sc["edition"])}</li>'
               f'<li><a href="{REPO_TREE}ciphers/{E(fold)}">Folder</a> &middot; <a href="{REPO_BLOB}ciphers/{E(fold)}/AUDIT.md">Audit</a>'
               + (f' &middot; <a href="{E(it["reading"])}">Reading</a>' if it["reading"].startswith("http") else "") + "</li></ul>")
    out.append(det(f"Search log from AUDIT.md ({len(searched)} search lines, {len(unreach)} on blocked or unreachable hosts)",
                   "<ul>" + "".join(f"<li>{md(s)}</li>" for s in searched) + "</ul>"
                   + ("<p><b>Unreachable</b></p><ul>" + "".join(f"<li>{md(s)}</li>" for s in unreach) + "</ul>" if unreach else "")))
    return "".join(out)


CSS_V2 = """
figure.cipher{margin:14px 0;background:var(--card);border:1px solid var(--rule);padding:8px}
figure.cipher img{display:block;width:100%;height:auto;background:#fff}
figcaption{font:12px/1.4 system-ui,sans-serif;color:var(--muted);margin-top:6px}
.strip{display:flex;flex-wrap:wrap;gap:3px;margin-top:8px}
.tk{display:inline-flex;flex-direction:column;align-items:center;min-width:34px;padding:2px 3px 0;border:1px solid var(--rule);border-bottom-width:5px;background:var(--bg)}
.tk .cs{font:12px ui-monospace,Menlo,monospace;color:var(--muted)}
.tk .pv{font:600 14px Georgia,serif}
.tk .gr{font:10px system-ui,sans-serif;color:var(--muted)}
.legend{font:12px system-ui,sans-serif}.lg{border-bottom:4px solid;padding:0 4px;margin-right:6px}
.ctx{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:6px;font:14px system-ui,sans-serif;background:var(--tint);padding:8px 10px}
.k{color:var(--muted);font-size:12px;display:block}
.two{display:grid;grid-template-columns:1fr 1fr;gap:18px}.two h3{margin:.8em 0 .3em}
ul.tl{list-style:none;padding:0;margin:0;font:14px/1.45 system-ui,sans-serif}ul.tl li{margin:3px 0}
.cx{font-size:11px;color:var(--muted);border:1px solid var(--rule);padding:0 4px}
.badges{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0 6px}
.badge{font:13px system-ui,sans-serif;border:1px solid var(--accent);padding:2px 8px;text-decoration:none;color:var(--fg)}
.bar{display:flex;height:12px;border:1px solid var(--rule)}.bar span{display:block}
img.thumb{display:block;max-width:220px;height:auto;margin-bottom:3px;background:#fff}
ul.links{font:14px/1.6 system-ui,sans-serif;padding-left:18px}
@media (max-width:640px){.two{grid-template-columns:1fr}}
"""


HOWTO = """<h1 id="how">How to read this catalogue</h1>
<h2 id="n-class">Search result (N0 to N5)</h2><p>Before a reading is described anywhere as new, a separate session, not the one that made the
reading, searches for it in print: the standard editions and calendars, the writer's and recipient's printed correspondence, the
holding archive's catalogue, full-text libraries and the scholarship indexes. It logs every source family it searched. The class
records what that search found; it is a search result, never a claim of discovery.</p><dl>{nw}</dl>
<p>A reading is counted in the catalogue's headline figures only after two such audits, and only from depth D2 up.</p>
<h2 id="depth">Depth (D0 to D4)</h2><dl>
<dt>Fragments read (D1)</dt><dd>Scattered words, no connected stretch long enough to rule out chance.</dd>
<dt>Partially deciphered (D2)</dt><dd>At least one connected clause reads, and the verifier can state one true, specific sentence about the content. The percentage is the share of cipher signs read from a key, a known text or a controlled cryptanalytic step.</dd>
<dt>Largely deciphered (D3)</dt><dd>80% or more of the cipher signs read that way, the gaps mostly names and code groups, with an outside check.</dd>
<dt>Deciphered (D4)</dt><dd>Every cipher letter read; only listed name codes left, with a fresh independent re-derivation.</dd></dl>
<h2 id="key">Key</h2><dl>
<dt>Key recovered by us</dt><dd>By cryptanalysis, by lining up a plain copy, or by identifying the code book.</dd>
<dt>Period key</dt><dd>Rebuilt from a decipherment, key sheet or cipher book of the time.</dd>
<dt>Published key</dt><dd>Someone else's modern key, applied by us and credited on the item page and in the audit.</dd></dl>
<h2>The one-line gist</h2><p>Marked "(interpretation)": an English paraphrase of what the read passage says, written by the verifier.
It is not a translation of the whole letter, and unread groups are not guessed.</p>
<h2>Where this comes from</h2><p>Every page is generated by a script from the repository's audit files and results register; nothing is
written by hand here. Each item links its primary image, the printed edition where one exists, the audit with its search log, the
reading and the script that regenerates it.</p>"""

CREDITS = """<h1 id="credits">Credits</h1>
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
    w = lambda name, html_: open(os.path.join(out, name), "w", encoding="utf-8").write(html_)
    w("index.html", page("Cipher letters read", index_body(items, ns, results, targets, lambda it: "items/" + it["file"])))
    for it in items:
        sc = showcase_for(it)
        body = (item_body_v2(it, sc, "../how-to-read.html") if sc else item_body(it, "../how-to-read.html", "../credits.html"))
        w(os.path.join("items", it["file"]), page(it["title"][:80], body, nav_prefix="../"))
    nw = "".join(f"<dt>N{k}</dt><dd>{E(v)}</dd>" for k, v in NWORDS.items())
    w("how-to-read.html", page("How to read this", HOWTO.format(nw=nw)))
    w("credits.html", page("Credits", CREDITS.format(keys=E(keys_credit(items)))))
    w("attention.html", page("Readings worth attention", attention_body(items, lambda it: "items/" + it["file"])))


def write_mockup(path, items, ns, results, targets, picks):
    chosen = []
    for p in picks:
        hit = next((it for it in items if p.lower() in it["title"].lower()), None)
        if hit is None:  # a named row the board does not count: render it anyway, labelled
            r = next((r for r in results if p.lower() in r.get("title", "").lower()), None)
            if r is None:
                sys.exit(f"--mockup-items: no result row matches {p!r}")
            hit = build_items([r], {**ns, "counted": lambda x: False, "counted_fragments": lambda x: False,
                                    "counted_key": lambda x: True})[0]
            hit["file"] = "x-" + slugify(hit["title"], 40) + ".html"
            hit["not_counted"] = True
        chosen.append(hit)
    ids = {it["file"]: "item-" + str(i) for i, it in enumerate(chosen)}
    href = lambda it: "#" + ids.get(it["file"], "not-in-mockup")
    body = [f'<section id="top">{index_body(items, ns, results, targets, href, inline=True)}</section>',
            f'<section class="page" id="attention">{attention_body(items, href)}</section>']
    for it in chosen:
        note = ('<p class="mock">This entry is not among the board\'s counted items (a key checked against a text already in print, '
                'audited but below the counting rule). Shown because the review asked for it.</p>') if it.get("not_counted") else ""
        body.append(f'<section class="page" id="{ids[it["file"]]}"><p class="small">Item page, shown inline</p>{note}'
                    f'{item_body_v2(it, showcase_for(it), "#how", inline=True) if showcase_for(it) else item_body(it, "#how", "#credits")}</section>')
    nw = "".join(f"<dt>N{k}</dt><dd>{E(v)}</dd>" for k, v in NWORDS.items())
    body.append('<section class="page" id="not-in-mockup"><p class="small">In the full site every row opens its own item page; this '
                'single-file mock-up carries three of them.</p></section>')
    body.append(f'<section class="page">{HOWTO.format(nw=nw)}</section>')
    body.append(f'<section class="page">{CREDITS.format(keys=E(keys_credit(items)))}</section>')
    html_ = page("Cipher letters read (mock-up)", "".join(body))
    for a_, b_ in (('href="index.html"', 'href="#top"'), ('href="attention.html"', 'href="#attention"'),
                   ('href="how-to-read.html"', 'href="#how"'), ('href="credits.html"', 'href="#credits"'),
                   ('href="#how#', 'href="#')):
        html_ = html_.replace(a_, b_)
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
