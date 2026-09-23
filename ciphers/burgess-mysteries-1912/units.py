#!/usr/bin/env python3
"""Text units of Gelett Burgess, The Master of Mysteries (Bobbs-Merrill, 1912), from Internet Archive OCR.

Written 23 Sept 2026 for the third-hidden-message search. Own code; nothing copied from
github.com/aaymeloglu/unsolved-ciphers (no licence; cited only).

Sources (text/manifest.json): two independent scans of the 1912 first edition, both with word coordinates.
  UC  = masterofmysterie00burgrich (University of California copy, 500 ppi)  -- primary: complete
  CU  = cu31924022342871 (Cornell copy, 300 ppi)                              -- second pass; its pp. 355-358
        are missing from the scan (the four leaves carry only colour-bar noise), so it is a check, not a base.

Structures built by load(src):
  book.pages     printed pages 1..480 with body lines (running heads and folios removed), plus
                 introduction pages (label 'intro1'..'intro3'); each line keeps its printed words.
  book.chapters  24 stories (title, first page) + the Introduction ('INTRO') with:
                   lines       printed lines, in order   (each: page, idx, words, text, indent, x0, x1)
                   paragraphs  word lists (hyphenated line-breaks joined), from indentation
                   sentences   word lists, split on . ! ? before a capital
                   words       all words (hyphens at line end joined)
  book.plates    plate captions (leaves without a running head outside the text)
  book.contents  the contents page lines

Printed-line units keep what is printed on the line (the fragment before a line-end hyphen is the line's
last word); word, sentence and paragraph units use the joined word. OCR noise is left in place: nothing is
repaired except the join of line-end hyphens.

python3 units.py [UC|CU] prints a summary and the two known acrostics as a self-test.
"""
import json
import re
import sys
import xml.etree.ElementTree as ET
from functools import lru_cache
from pathlib import Path
from statistics import median

HERE = Path(__file__).resolve().parent
TEXT = HERE / "text"
SOURCES = {"UC": "masterofmysterie00burgrich_djvu.xml", "CU": "cu31924022342871_djvu.xml"}

# Contents page (leaf 12 of CU), titles as printed, with first page.
TITLES = [
    ("Missing John Hudson", 1), ("The Stolen Shakespeare", 23), ("The MacDougal Street Affair", 44),
    ("The Fanshawe Ghost", 65), ("The Denton Boudoir Mystery", 83), ("The Lorsson Elopement", 103),
    ("The Calendon Kidnaping Case", 128), ("Miss Dalrymple's Locket", 148), ("Number Thirteen", 165),
    ("The Trouble with Tulliver", 186), ("Why Mrs. Burbank Ran Away", 203), ("Mrs. Selwyn's Emerald", 225),
    ("The Assassins' Club", 247), ("The Luck of the Meeringtons", 271), ("The Count's Comedy", 291),
    ("Priscilla's Presents", 311), ("The Heir to Soothold", 326), ("The Two Miss Mannings", 344),
    ("Van Asten's Visitor", 365), ("The Middlebury Murder", 384), ("Vengeance of the Pi Rho Nu", 407),
    ("The Lady in Taupe", 428), ("Mrs. Stellery's Letters", 443), ("Black Light", 465),
]
LAST_PAGE = 480
KNOWN = {"first": "THEAUTHORISGELETTBURGESS", "last": "FALSETOLIFEANDFALSETOART"}

ABBREV = {"mr", "mrs", "dr", "st", "mme", "messrs", "prof", "rev", "ps", "vol", "no", "jr", "sr", "co", "ave",
          "capt", "col", "gen", "lieut", "hon", "etc", "vs", "p", "pp"}


def letters(s):
    return re.sub(r"[^A-Za-z]", "", s)


def upper_ratio(s):
    L = letters(s)
    return sum(c.isupper() for c in L) / len(L) if L else 0.0


def clean_word(tok):
    """Printed token -> word (letters and inner apostrophes); '' if no letters."""
    w = re.sub(r"[^A-Za-z'\-]", "", tok).strip("'-")
    return w if letters(w) else ""


def _parse(src):
    root = ET.parse(TEXT / SOURCES[src]).getroot()
    leaves = []
    for i, obj in enumerate(root.iter("OBJECT")):
        lines = []
        for ln in obj.iter("LINE"):
            ws = [w for w in ln.iter("WORD") if (w.text or "").strip()]
            if not ws:
                continue
            c0 = [int(v) for v in ws[0].get("coords").split(",")]
            c1 = [int(v) for v in ws[-1].get("coords").split(",")]
            toks = [t for w in ws for t in w.text.split()]
            lines.append({"toks": toks, "text": " ".join(toks), "x0": c0[0], "x1": c1[2], "y": c0[3],
                          "x0_2": int(ws[1].get("coords").split(",")[0]) if len(ws) > 1 else None})
        leaves.append({"leaf": i, "width": int(obj.get("width")), "lines": lines})
    return leaves


def _norm_title(s):
    return letters(s).upper()


def _is_running_head(line, titles_norm):
    t = line["text"]
    L = letters(t)
    if len(L) < 4:
        return False
    if upper_ratio(t) < 0.75:
        return False
    n = L.upper()
    return "MASTER" in n or "MYSTER" in n or "INTRODUCTION" in n or any(
        _sim(n, tn) > 0.7 for tn in titles_norm)


def _sim(a, b):
    """Crude similarity: share of b's letter bigrams present in a."""
    if not a or not b:
        return 0.0
    bg = lambda s: {s[i:i + 2] for i in range(len(s) - 1)}
    B = bg(b)
    return len(bg(a) & B) / max(1, len(B))


def _title_match(text, want):
    return _sim(_norm_title(text), _norm_title(want)) > 0.6


class Book:
    pass


@lru_cache(maxsize=None)
def _load_src(src):
    leaves = _parse(src)
    titles_norm = [_norm_title(t) for t, _ in TITLES]
    book = Book()
    book.src = src
    # --- locate contents and introduction by their headings
    contents_leaf = next(l for l in leaves if l["lines"] and letters(l["lines"][0]["text"]).upper() == "CONTENTS")
    intro_leaves = [l for l in leaves if l["lines"] and letters(l["lines"][0]["text"]).upper() == "INTRODUCTION"]
    book.contents = [ln["text"] for ln in contents_leaf["lines"]]
    # --- walk the body: from the leaf opening chapter 1
    start = next(l["leaf"] for l in leaves if l["leaf"] > intro_leaves[-1]["leaf"] and any(
        _title_match(ln["text"], TITLES[0][0]) and upper_ratio(ln["text"]) > 0.75 for ln in l["lines"][:3]))
    pages, plates = [], []
    ch = -1
    pageno = 0
    for l in leaves[start:]:
        lines = l["lines"]
        if not lines:
            continue
        # chapter opening?  a mostly-upper line among the first three that matches the next title
        opening = False
        if ch + 1 < len(TITLES):
            head = " ".join(ln["text"] for ln in lines[:3]
                            if upper_ratio(ln["text"]) > 0.75 and not re.search(r"\d", ln["text"]))
            opening = _sim(_norm_title(head), titles_norm[ch + 1]) > 0.6
        has_head = _is_running_head(lines[0], titles_norm)
        if not opening and not has_head:
            if pageno >= LAST_PAGE:
                continue
            plates.append({"leaf": l["leaf"], "after_page": pageno, "text": " / ".join(x["text"] for x in lines)})
            continue
        pageno += 1
        if opening:
            ch += 1
            # drop heading lines: 'The Master of Mysteries' half-title and the title (1-2 lines, upper case)
            k = 0
            while k < len(lines) and (upper_ratio(lines[k]["text"]) > 0.75 or
                                      _norm_title(lines[k]["text"]) == "THEMASTEROFMYSTERIES"):
                k += 1
            body = lines[k:]
            # folio at foot of an opening page
            if body and len(letters(body[-1]["text"])) <= 3 and len(body[-1]["text"]) <= 5:
                body = body[:-1]
        else:
            body = lines[1:]
        # drop junk lines with fewer than two letters (OCR specks), e.g. a lone guillemet
        body = [ln for ln in body if len(letters(ln["text"])) >= 2]
        pages.append({"page": pageno, "leaf": l["leaf"], "chapter": ch, "opening": opening, "lines": body,
                      "head": lines[0]["text"]})
    book.plates = plates
    # --- introduction pages
    intro_pages = [{"page": f"intro{j + 1}", "leaf": l["leaf"], "chapter": "INTRO", "opening": j == 0,
                    "lines": [ln for ln in l["lines"][1:] if len(letters(ln["text"])) >= 2], "head": "INTRODUCTION"}
                   for j, l in enumerate(intro_leaves)]
    book.intro_pages, book.body_pages = intro_pages, pages
    return book


def _finish(book):
    """Normalise tokens, restore drop capitals, build chapters."""
    pages = book.intro_pages + book.body_pages
    for p in pages:
        for ln in p["lines"]:
            ln["toks"] = _norm_toks(ln["toks"])
            ln["text"] = " ".join(ln["toks"])
    last = book.body_pages[-1]
    if last["lines"] and letters(last["lines"][-1]["text"]).upper() == "THEEND":
        last["lines"] = last["lines"][:-1]
    book.pages = pages
    book.chapters = [_build_chapter("INTRODUCTION", book.intro_pages, None)] + [
        _build_chapter(TITLES[c][0], [p for p in book.body_pages if p["chapter"] == c], DROPCAP.get(c))
        for c in range(len(TITLES))]
    book.stories = book.chapters[1:]
    return book


# First word of each story whose opening letter is a two-line drop capital that the OCR cannot read.
# The word is fixed by the letters that survive in either OCR pass and by sense (grade I, inferred; see NOTES.md).
DROPCAP = {4: "UNDERNEATH", 7: "OH", 9: "I", 10: "SURELY", 11: "GASPING", 12: "EVERY", 13: "LATE",
           17: "BE", 18: "UNLESS", 20: "GRACIOUS", 21: "EXCUSE", 22: "SHE"}
SMALL_OK = {"a", "an", "as", "at", "be", "by", "do", "he", "if", "in", "is", "it", "me", "my", "no", "of", "oh",
            "on", "or", "so", "to", "up", "us", "we", "the", "and", "you", "she", "her", "his"}


def _norm_toks(toks):
    out = []
    for t in toks:
        for part in re.split(r"(—|--)", t):
            if not part:
                continue
            if part in ("—", "--"):
                out.append("—")
                continue
            # an exclamation mark read as I or 1 after a word ("wonderful I\"", "schemer 1")
            if re.fullmatch(r"[I1][\"\u201d']*|1", part) and out and re.search(r"[a-z]$", out[-1]) and (
                    part != "I" or False):
                out.append("!" + part[1:])
                continue
            out.append(part)
    return out


def _dropcap(lines, word):
    """Replace the OCR debris of a drop capital on the first two printed lines by the restored word."""
    if not lines:
        return
    toks = lines[0]["toks"]
    tail = word[1:]
    k = None
    for i, t in enumerate(toks[:4]):
        L = letters(t).upper()
        if not L:
            continue
        cmp = L[-len(tail):] if tail else ""
        if tail and len(L) >= len(tail) and sum(a != b for a, b in zip(cmp, tail)) <= 1 and len(L) <= len(word) + 1:
            k = i
            break
    lead = '"' if toks and toks[0].startswith(('"', '\u201c', "'")) else ""
    if k is None:
        # nothing recognisable (e.g. the capital and its word both lost): drop leading debris, insert the word
        i = 0
        while i < len(toks) and (not letters(toks[i]) or (len(letters(toks[i])) <= 2 and letters(toks[i]).isupper()
                                                            and letters(toks[i]).lower() not in SMALL_OK)):
            i += 1
        rest = toks[i:]
        if rest and letters(rest[0]).upper() == word:
            rest = rest[1:]
        new = [lead + word + ("," if rest and rest[0].startswith(",") else "")] + [
            r for r in rest if not (r == "," and rest.index(r) == 0)]
    else:
        new = [lead + word + re.sub(r"^.*[A-Za-z]", "", toks[k])] + toks[k + 1:]
    lines[0]["toks"] = new
    lines[0]["text"] = " ".join(new)
    if len(lines) > 1:
        t2 = lines[1]["toks"]
        i = 0
        while i < len(t2) - 1 and len(t2[i]) <= 4 and not re.fullmatch(r"[a-z']+[,.;:!?]*", t2[i]) and \
                letters(t2[i]).lower() not in SMALL_OK - {"a"}:
            i += 1
        lines[1]["toks"] = t2[i:]
        lines[1]["text"] = " ".join(t2[i:])


def _align(a, b, band=4):
    """Banded global alignment of two lists of line texts; returns list of (i or None, j or None)."""
    import difflib
    na, nb = len(a), len(b)
    key = lambda s: letters(s).lower()
    A, B = [key(x) for x in a], [key(x) for x in b]
    INF = -1e9
    S = {(0, 0): (0.0, None)}
    for i in range(na + 1):
        for j in range(max(0, i - band - abs(na - nb)), min(nb, i + band + abs(na - nb)) + 1):
            if (i, j) == (0, 0):
                continue
            best = (INF, None)
            if i and j and (i - 1, j - 1) in S:
                r = difflib.SequenceMatcher(None, A[i - 1], B[j - 1], autojunk=False).ratio()
                best = max(best, (S[(i - 1, j - 1)][0] + (r - 0.5) * 2, (i - 1, j - 1)))
            if i and (i - 1, j) in S:
                best = max(best, (S[(i - 1, j)][0] - 0.4, (i - 1, j)))
            if j and (i, j - 1) in S:
                best = max(best, (S[(i, j - 1)][0] - 0.4, (i, j - 1)))
            S[(i, j)] = best
    path, cur = [], (na, nb)
    while cur != (0, 0):
        prev = S[cur][1]
        di, dj = cur[0] - prev[0], cur[1] - prev[1]
        path.append((cur[0] - 1 if di else None, cur[1] - 1 if dj else None))
        cur = prev
    return path[::-1]


@lru_cache(maxsize=None)
def vocab():
    from collections import Counter
    c = Counter()
    for src in SOURCES:
        b = _load_src(src)
        for p in b.intro_pages + b.body_pages:
            for ln in p["lines"]:
                c.update(letters(t).lower() for t in ln["toks"] if letters(t))
    return {w for w, n in c.items() if n >= 3}


def _goodness(line, V):
    ws = [letters(t).lower() for t in line["toks"] if letters(t)]
    junk = sum(bool(re.search(r"[A-Za-z]", t) and re.search(r"[0-9^\\|~<>{}\[\]_]", t)) for t in line["toks"])
    return sum(w in V for w in ws) - 0.5 * sum(w not in V for w in ws) - 0.3 * junk


@lru_cache(maxsize=None)
def reconcile_log():
    return _reconcile()[1]


@lru_cache(maxsize=None)
def _reconciled():
    return _reconcile()[0]


def _reconcile():
    """UC is the base; CU fills lines UC lost and replaces a UC line when CU's reading has more known words."""
    import copy
    uc, cu = _load_src("UC"), _load_src("CU")
    V = vocab()
    book = copy.deepcopy(uc)
    book.src = "R"
    cu_pages = cu.intro_pages + cu.body_pages
    key = lambda p: letters(" ".join(l["text"] for l in p["lines"])).lower()
    import difflib
    log = {"pages": 0, "lines_aligned": 0, "lines_differ": 0, "cu_chosen": 0, "uc_only": 0, "cu_inserted": 0,
           "pages_without_cu": []}
    ci = 0
    for p in book.intro_pages + book.body_pages:
        # the matching CU page: best text similarity among the next few CU pages
        cands = [(difflib.SequenceMatcher(None, key(p)[:400], key(q)[:400], autojunk=False).ratio(), k)
                 for k, q in enumerate(cu_pages[ci:ci + 6], start=ci)]
        r, k = max(cands) if cands else (0, None)
        if r < 0.6:
            log["pages_without_cu"].append(p["page"])
            continue
        ci = k + 1
        q = cu_pages[k]
        log["pages"] += 1
        out = []
        for i, j in _align([l["text"] for l in p["lines"]], [l["text"] for l in q["lines"]]):
            if i is not None and j is not None:
                a, b = p["lines"][i], q["lines"][j]
                log["lines_aligned"] += 1
                if letters(a["text"]) != letters(b["text"]):
                    log["lines_differ"] += 1
                    if _goodness(b, V) > _goodness(a, V):
                        a = dict(a, toks=b["toks"], text=b["text"], src="CU")
                        log["cu_chosen"] += 1
                a = dict(a, alt=b["text"])
                out.append(a)
            elif i is not None:
                log["uc_only"] += 1
                out.append(p["lines"][i])
            else:
                # a line only CU has: keep it when it is real text (UC dropped it); geometry from CU
                b = q["lines"][j]
                if _goodness(b, V) >= 1 and len(letters(b["text"])) >= 4:
                    log["cu_inserted"] += 1
                    out.append(dict(b, src="CU"))
        p["lines"] = out
    return book, log


def load(src="R"):
    """src: 'R' reconciled (default), 'UC' or 'CU' single OCR pass."""
    import copy
    if src == "R":
        return _finish(copy.deepcopy(_reconciled()))
    return _finish(copy.deepcopy(_load_src(src)))


_cache = {}


def get(src="R"):
    if src not in _cache:
        _cache[src] = load(src)
    return _cache[src]


def _margin(page):
    xs = [ln["x0"] for ln in page["lines"]]
    return median(xs) if xs else 0


def _build_chapter(title, pages, dropcap):
    ch = {"title": title, "pages": [p["page"] for p in pages], "lines": []}
    if dropcap and pages:
        _dropcap(pages[0]["lines"], dropcap)
    idx = 0
    for p in pages:
        # left margin = lower quartile of line starts (most lines are flush left)
        xs = sorted(ln["x0"] for ln in p["lines"])
        m = xs[len(xs) // 4] if xs else 0
        width_ref = max((ln["x1"] for ln in p["lines"]), default=1)
        for j, ln in enumerate(p["lines"]):
            ch["lines"].append({"page": p["page"], "idx": idx, "row": j, "toks": ln["toks"], "text": ln["text"],
                                "indent": ln["x0"] - m, "x0": ln["x0"], "x1": ln["x1"], "right": width_ref})
            idx += 1
    # paragraph starts: first line of the chapter; or a line indented 1.5-8 % of the text width whose
    # predecessor does not end with a hyphen (OCR boxes for words after a hyphen break are unreliable);
    # or any line after a short line on the same page (inset letters, lists, verse)
    lines = ch["lines"]
    for k, ln in enumerate(lines):
        textw = max(1, ln["right"] - (ln["x0"] - ln["indent"]))
        prev = lines[k - 1] if k else None
        hyph_prev = prev is not None and re.search(r"[A-Za-z]-$", prev["toks"][-1] or "")
        ind = ln["indent"] / textw
        prev_short = prev is not None and prev["page"] == ln["page"] and \
            prev["x1"] < prev["right"] - 0.15 * textw
        ln["para_start"] = k == 0 or (not hyph_prev and letters(ln["text"])[:1] != "" and (
            0.015 <= ind <= 0.09 or prev_short))
    # words with line-end hyphens joined; each word remembers its line
    words = []  # (word, line_idx)
    carry = None
    for ln in lines:
        toks = [t for t in ln["toks"]]
        for ti, t in enumerate(toks):
            last = ti == len(toks) - 1
            if carry is not None:
                w = clean_word(carry[0] + t)
                if w:
                    words.append((w, carry[1]))
                carry = None
                continue
            if last and re.search(r"[A-Za-z]-$", t):
                carry = (t[:-1], ln["idx"])
                continue
            w = clean_word(t)
            if w:
                words.append((w, ln["idx"]))
        ln["words"] = [clean_word(t) for t in toks if clean_word(t)]
    if carry:
        words.append((clean_word(carry[0]), carry[1]))
    ch["words"] = [w for w, _ in words]
    # paragraphs
    paras, cur = [], []
    starts = {ln["idx"] for ln in lines if ln["para_start"]}
    seen_lines = set()
    for w, li in words:
        if li in starts and li not in seen_lines and cur:
            paras.append(cur)
            cur = []
        seen_lines.add(li)
        cur.append(w)
    if cur:
        paras.append(cur)
    ch["paragraphs"] = paras
    # sentences (from the raw token stream so punctuation is visible)
    ch["sentences"] = _sentences(lines)
    return ch


def _sentences(lines):
    toks = []
    carry = None
    for ln in lines:
        for ti, t in enumerate(ln["toks"]):
            if carry is not None:
                t = carry + t
                carry = None
            elif ti == len(ln["toks"]) - 1 and re.search(r"[A-Za-z]-$", t):
                carry = t[:-1]
                continue
            toks.append(t)
    sents, cur = [], []
    for i, t in enumerate(toks):
        w = clean_word(t)
        if w:
            cur.append(w)
        end = re.search(r"[.!?][\"'”’)]*$", t) or t in ("!", "?", ".", "!\"", "?\"")
        if end and cur:
            base = letters(t).lower()
            if base in ABBREV or (len(base) == 1 and base.isalpha() and t[0].isupper() and t.endswith(".")):
                continue
            nxt = toks[i + 1] if i + 1 < len(toks) else ""
            nl = re.sub(r"^[\"'“‘(]+", "", nxt)
            if not nxt or nl[:1].isupper() or nl[:1].isdigit():
                sents.append(cur)
                cur = []
    if cur:
        sents.append(cur)
    return sents


def first_letter(w):
    return letters(w)[:1].upper()


def last_letter(w):
    return letters(w)[-1:].upper()


def known_acrostics(book):
    first = "".join(first_letter(c["words"][0]) for c in book.stories)
    last = "".join(last_letter(c["words"][-1]) for c in book.stories)
    return first, last


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "R"
    b = get(src)
    if src == "R":
        print("reconcile:", {k: v for k, v in reconcile_log().items()})
    print(f"source {src}: {len([p for p in b.pages if isinstance(p['page'], int)])} printed pages, "
          f"{len(b.plates)} plates")
    for c in b.chapters:
        print(f"  {c['title'][:28]:28s} pp {c['pages'][0]}-{c['pages'][-1]}  lines {len(c['lines']):4d}  "
              f"paras {len(c['paragraphs']):4d}  sents {len(c['sentences']):4d}  words {len(c['words']):5d}  "
              f"first={c['words'][0]} last={c['words'][-1]}")
    f, l = known_acrostics(b)
    print("first letters:", f, "OK" if f == KNOWN["first"] else "MISMATCH")
    print("last letters: ", l, "OK" if l == KNOWN["last"] else "MISMATCH")
