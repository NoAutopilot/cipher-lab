#!/usr/bin/env python3
"""shelfmark.py: one normaliser for item identity -- volume, folio, canvas and record ids (PRIOR-WORK v1, 8 Oct 2026).

    python3 tools/shelfmark.py "BnF fr.16104 f.102r, canvas 211, DECODE R9502"     print the parsed keys
    python3 tools/shelfmark.py --match "fr.3040 f.18r" "Tomokiyo: f.18 (no.6) in BnF fr.3040, deciphered"

Why: tools/prior_work.py, tools/premise_check.py, tools/solver_repo_diff.py and tools/decode_neighbours_exclude.py
each parsed shelfmarks and folios their own way, and premise_check's leaf_of() keys on the folio alone -- which is
how fr.16104 and fr.16105 crops, or fr.3252 and fr.4702 ff.36-37, cross-matched in one folder
(research/PRIOR-WORK-LEAK-2026-10-08.md, "A later step on the same leaf"). A unit is volume + folio + canvas, never
the folio alone. Volume keys come from decode_neighbours_exclude.volume_keys() (the normalisation validated on the
23 Sept 2026 neighbour sweep: fr./francais, Clair., Colbert, Baluze, Dupuy, NAF, BL Add/Cotton/Harley, TNA SP/PRO,
RAH 9/, AGS, ASV, BNE ...), plus the forms it lacks: bare 'fr3040' (slugs and file names), HStAM, NLA, Nationaal
Archief inv. numbers, Huntington mss collections, LOC mss numbers, Dresden Loc., abbreviated Cotton presses (Calig.,
Vesp., ...), WVO briefnr (comma lists too: 'WVO 5811, 5810, 4503'), Huntington pointers, DECODE R-ids (ids_in()),
Birch/Thurloe P-numbers and short entry labels (E78, N2-BQ, O9-BA).

A folio is bound to the volume named nearest before it in the same clause (else the nearest after it in that clause):
a line is never a bag of keys, so 'fr.16104 f.98r and fr.16105 f.102r' names fr.16105 f.102r, not fr.16104 f.102r.

API (all pure, no I/O):
  parse(text) -> Keys(vols, leaves, canvases, ids)      every identifier a text names
  mentions(text) -> [Mention(kind, start, end, leaves, canvases, ids, vol)]   each folio/canvas/id mention, vol bound
  unit(shelfmark, folio, canvas, ids)  -> Keys          an item's own identity
  match(unit_keys, text, multi_volume=False, tol=0, context_vols=None)  'exact' | 'fuzzy' | 'ambiguous' | None
      'exact'     the text names one of the unit's ids (and no other volume), or its folio (side-compatible) bound
                  to its volume
      'fuzzy'     folio within +-tol (different foliation systems: ink, finding aid, Tomokiyo); never KNOWN
      'ambiguous' the folio matches but no volume is bound to it and the folder holds several volumes (or the text
                  names another volume elsewhere, or the unit itself names no volume)
      None        nothing, or the folio matches in a DIFFERENT volume (fr.16104 vs fr.16105)
  names_other(unit_keys, text)   True when the text names a folio, canvas or id that is not the unit's

Must catch: 'fr.3040 f.18r' against 'f.18 (no.6) ... BnF fr.3040' (exact); 'R9502' against 'DECODE R9502';
'WVO 5810' against 'WVO 5811, 5810, 4503'; f.229v against 'f.229r-v'.
Must NOT match: fr.16104 f.102r against 'fr.16105 f.102r', a crop named 'c105_f102r_L01.jpg', or 'fr.16104 f.98r and
fr.16105 f.102r'; f.18r against 'f.18v' (another page of the leaf); a bare year or a dollar figure as a folio;
Colbert 127 against a line about Colbert 159 that cites the same DECODE id.
Offline test: tools/tests/test_prior_work.py (shelfmark section).
"""
import os
import re
import sys
import unicodedata
from collections import namedtuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decode_neighbours_exclude import ids_in, volume_keys as _volume_keys  # noqa: E402

Keys = namedtuple("Keys", "vols leaves canvases ids")
Mention = namedtuple("Mention", "kind start end leaves canvases ids vol")

# f.18, f.18r, fol. 18v, folio 18, ff.36-37, fos 16-56, f.229r-v; also f18r / _f102r_ inside file names (side required)
LEAF_RE = re.compile(r"(?<![A-Za-z0-9])(?:ff?|fol|fols|fos?|folios?)\.?\s*(\d{1,4})\s*([rv])?(?:\s*[-–/]\s*(v)(?![A-Za-z0-9]))?"
                     r"(?:\s*[-–]\s*(\d{1,4})\s*([rv])?)?(?![0-9])", re.I)
FILE_LEAF_RE = re.compile(r"(?<![A-Za-z0-9])f(\d{1,4})([rv])(?![a-z0-9])", re.I)
CANVAS_RE = re.compile(r"\bcanvas(?:es)?\s*(\d{1,4})\b", re.I)
PTR_RE = re.compile(r"\b(?:ptr|pointer)\.?\s*(\d{4,5})(?:/(\d))?\b|\b(\d{4,5})/(\d)\b", re.I)
WVO_RE = re.compile(r"\b(?:WVO|briefnr\.?|brief\s*nr\.?)\s*(\d{1,5}(?:\s*(?:,|&|/|\band\b|\ben\b)\s*\d{3,5}(?![\d/.]))*)", re.I)
LABEL_RE = re.compile(r"\b((?:E|T|P|N2-|O9-)\d{1,3}|N2-[A-Z]{1,2}|O9-[A-Z]{1,2})\b")
FILE_VOL_RE = re.compile(r"(?<![A-Za-z0-9])(?:c|fr)(\d{3,5})_", re.I)   # c105_f102r_, fr3040_f18r
COTTON = {"calig": "caligula", "vesp": "vespasian", "galb": "galba", "galba": "galba", "otho": "otho",
          "cleop": "cleopatra", "faust": "faustina", "tib": "tiberius", "jul": "julius", "claud": "claudius",
          "dom": "domitian", "aug": "augustus", "tit": "titus", "nero": "nero"}
YEARLIKE = range(1400, 1951)


def _fold(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s or "") if not unicodedata.combining(c)).lower()


def volume_keys(text):
    """decode_neighbours_exclude.volume_keys() plus the forms it misses (bare 'fr3040', HStAM, NLA, NA inv.,
    Huntington mss, LOC mss, Dresden Loc., abbreviated Cotton presses)."""
    s = text or ""
    keys = _volume_keys(s)
    f = _fold(s)
    for m in re.finditer(r"(?<![a-z0-9])fr(\d{3,5})(?![0-9])", f):
        keys.add(f"bnf français {m.group(1)}")
    for m in re.finditer(r"\bhstam\.?\s*(\d{1,3})\s*([a-z])?\.?\s*(?:nr\.?|no\.?)?\s*(\d{1,6})\b", f):
        keys.add(f"hstam {m.group(1)}{m.group(2) or ''} nr {m.group(3)}")
    for m in re.finditer(r"\bnla\b([^,;()]{0,30}?)\bnr\.?\s*(\d{1,6})\b", f):
        keys.add("nla " + " ".join(re.findall(r"[a-z0-9]+", m.group(1))) + f" nr {m.group(2)}")
    for m in re.finditer(r"\bna,?\s*(\d(?:\.\d{2}){1,5})\s*,?\s*(?:inv\.?\s*(?:nr\.?)?|invnr\.?|inventarisnummer)\s*(\d{1,6})\b", f):
        keys.add(f"na {m.group(1)} inv {m.group(2)}")
    for m in re.finditer(r"\bmss\s?(de|hm|ec|lo|br|st|pf|ad)\s?(\d{1,6})\b", f):
        keys.add(f"huntington mss{m.group(1)} {m.group(2)}")
    for m in re.finditer(r"\bmss(\d{5})\b", f):
        keys.add(f"loc mss {m.group(1)}")
    for m in re.finditer(r"\bloc\.\s*(\d{1,5})\s*/\s*(\d{1,3})\b", f):
        keys.add(f"dresden loc {m.group(1)}/{m.group(2)}")
    for m in re.finditer(r"(?:\bcott(?:on)?\.?\s*(?:ms\.?\s*)?)?\b(calig|vesp|galba|galb|otho|cleop|faust|tib|jul|claud|dom|aug|tit|nero)"
                         r"[a-z]*\.?,?\s*([a-e])\.?,?\s*([ivx]+)\b", f):
        if m.group(0).startswith("cott") or m.group(1) in ("calig", "vesp", "galba", "galb", "otho", "cleop", "faust"):
            keys.add(f"bl cotton {COTTON[m.group(1)]} {m.group(2)} {m.group(3)}")
    return keys


def _leaf(n, side):
    return (int(n), (side or "").lower())


def _leaf_match_set(m):
    a, sa, rv, b, sb = m.groups()
    out = set()
    if b and 0 < int(b) - int(a) <= 40:
        out |= {(i, "") for i in range(int(a), int(b) + 1)}
        out.add(_leaf(a, sa))
        out.add(_leaf(b, sb))
    else:
        out.add(_leaf(a, sa))
    if rv and (sa or "").lower() == "r":
        out.add((int(a), "v"))
    return out


def leaves(text):
    """{(folio_number, side)} named in text; ranges of up to 40 leaves are expanded (sides dropped inside a range);
    'f.229r-v' names both sides."""
    out = set()
    for m in LEAF_RE.finditer(text or ""):
        out |= _leaf_match_set(m)
    for m in FILE_LEAF_RE.finditer(text or ""):
        out.add(_leaf(*m.groups()))
    return out


def _wvo_numbers(group):
    return [int(n) for n in re.findall(r"\d+", group)]


def ids(text):
    """Record ids: DECODE R-ids, Huntington pointers (ptr:9714, ptr:9714/1), WVO numbers, short entry labels."""
    s = text or ""
    out = set(ids_in(s))
    for m in PTR_RE.finditer(s):
        p, e = (m.group(1), m.group(2)) if m.group(1) else (m.group(3), m.group(4))
        out.add(f"ptr:{p}")
        if e is not None:
            out.add(f"ptr:{p}/{e}")
    for m in WVO_RE.finditer(s):
        nums = _wvo_numbers(m.group(1))
        out |= {f"wvo:{n}" for i, n in enumerate(nums) if i == 0 or n not in YEARLIKE}
    out |= {f"label:{m.group(1)}" for m in LABEL_RE.finditer(s)}
    return out


def parse(text):
    s = text or ""
    vols = volume_keys(s)
    for m in FILE_VOL_RE.finditer(s):
        vols.add(f"hint:{m.group(1)}")
    return Keys(vols, leaves(s), {int(c) for c in CANVAS_RE.findall(s)}, ids(s))


def unit(shelfmark="", folio="", canvas="", extra_ids=()):
    """An item's own identity from its items.tsv fields."""
    lv = leaves(f"f.{folio}") if folio else set()
    cv = {int(canvas)} if str(canvas).strip().isdigit() else set()
    return Keys(volume_keys(shelfmark or ""), lv, cv, set(extra_ids))


# ------------------------------------------------------------------ positions: clauses, volume mentions, mentions

def clause_spans(text):
    """(start, end) of clauses: split at ';', '|', ' -- ', ' - ', a dash, a line break and a sentence end (not after an
    abbreviation such as f. / fol. / no. / vol.), outside brackets."""
    s, out, start, depth = text or "", [], 0, 0
    i = 0
    while i < len(s):
        c = s[i]
        if c in "([":
            depth += 1
        elif c in ")]":
            depth = max(0, depth - 1)
        cut = 0
        if depth == 0:
            if c in ";|\n":
                cut = 1
            elif s.startswith((" -- ", " — ", " – "), i):
                cut = 3 if s[i + 1] != "-" else 4
            elif s.startswith(" - ", i) and i > 0:
                cut = 3
            elif c in ".!?" and i + 1 < len(s) and s[i + 1] == " " and (i + 2 >= len(s) or s[i + 2].isupper()
                                                                       or s[i + 2] in "\"'(*"):
                if not re.search(r"(?:^|[\s(\[])(?:f|ff|fol|fols|fo|fos|no|nos|nr|vol|vols|p|pp|cf|ms|mss|inv|invnr|add|"
                                 r"fr|esp|clair|ser|pt|st|mr|dr|gen|col|lt|capt|e\.g|i\.e|c|ca|viz|jr|sr|calig|vesp|mel)$",
                                 s[max(0, i - 8):i], re.I):
                    cut = 1
        if cut:
            out.append((start, i + (1 if c in ".!?" else 0)))
            start = i + cut
            i += cut
            continue
        i += 1
    out.append((start, len(s)))
    spans = []
    for a, b in out:
        if b - a > 600 and depth:            # an unbalanced bracket: split that stretch again without depth
            return _flat_spans(s)
        if s[a:b].strip():
            spans.append((a, b))
    return spans


def _flat_spans(s):
    out, start = [], 0
    for m in re.finditer(r"[;|\n]|\s--?\s|(?<=[.!?])\s(?=[A-Z])", s):
        out.append((start, m.start()))
        start = m.end()
    out.append((start, len(s)))
    return [(a, b) for a, b in out if s[a:b].strip()]


def clauses(text):
    return [text[a:b] for a, b in clause_spans(text)]


def vol_mentions(text):
    """[(start, end, key)] for each volume named in text (a key per mention, so repeats keep their positions)."""
    s, out = text or "", []
    for m in FILE_VOL_RE.finditer(s):
        out.append((m.start(), m.end(), f"hint:{m.group(1)}"))
    pat = r"\d+(?:\.\d+)*" + (r"|\b[ivx]+\b" if re.search(r"cott|calig|vesp|galba|otho|cleop|faust", s, re.I) else "")
    for m in re.finditer(pat, s, re.I):
        tok = m.group(0).lower()
        window = s[max(0, m.start() - 60):m.end()]
        for key in volume_keys(window):
            last = re.split(r"[ /]", key)[-1]
            if last == tok:
                out.append((m.start(), m.end(), key))
    return sorted(set(out))


def _bind(spans, vms, pos):
    """The volume key bound to a mention at pos: nearest before it in its clause, else nearest after it there."""
    a, b = next(((x, y) for x, y in spans if x <= pos < y), (0, 10 ** 9))
    before = [v for v in vms if a <= v[0] < pos]
    if before:
        return before[-1][2]
    after = [v for v in vms if pos < v[0] < b]
    return after[0][2] if after else None


def mentions(text):
    """Every folio, canvas and id mention, each with the volume key bound to it (or None)."""
    s = text or ""
    spans, vms = clause_spans(s), vol_mentions(s)
    out = []
    for m in LEAF_RE.finditer(s):
        out.append(Mention("leaf", m.start(), m.end(), _leaf_match_set(m), set(), set(), _bind(spans, vms, m.start())))
    for m in FILE_LEAF_RE.finditer(s):
        out.append(Mention("leaf", m.start(), m.end(), {_leaf(*m.groups())}, set(), set(), _bind(spans, vms, m.start())))
    for m in CANVAS_RE.finditer(s):
        out.append(Mention("canvas", m.start(), m.end(), set(), {int(m.group(1))}, set(), _bind(spans, vms, m.start())))
    for rx in (PTR_RE, WVO_RE, LABEL_RE):
        for m in rx.finditer(s):
            out.append(Mention("id", m.start(), m.end(), set(), set(), ids(m.group(0)), _bind(spans, vms, m.start())))
    for m in re.finditer(r"\bR\d{1,5}(?:\s*[-–]\s*R?\d{1,5})?\b", s):
        out.append(Mention("id", m.start(), m.end(), set(), set(), set(ids_in(m.group(0))), _bind(spans, vms, m.start())))
    return sorted(out, key=lambda x: x.start)


def _vol_ok(unit_vols, text_vols):
    """True/False when the text names a volume (a file-name hint 'c105' matches 'bnf français 16105' by suffix),
    None when it names none."""
    real = {v for v in text_vols if not v.startswith("hint:")}
    hints = {v[5:] for v in text_vols if v.startswith("hint:")}
    if real:
        return bool(unit_vols & real)
    if hints:
        nums = {v.rsplit(" ", 1)[-1] for v in unit_vols}
        return any(n.endswith(h) for n in nums for h in hints)
    return None


def _wvo_bare(u, text):
    """A WVO unit named by its bare number (lodewijk NOTES write '4612' without 'WVO'): four or five digits, never a
    year-like number (a bare '126' is too common to key on)."""
    for i in u.ids:
        if i.startswith("wvo:") and i[4:].isdigit() and int(i[4:]) not in YEARLIKE and int(i[4:]) >= 1000:
            if re.search(rf"(?<![\w./$-]){i[4:]}(?![\w/-]|\.\d)", text):
                return True
    return False


def _leaf_hit(u, lv, tol):
    best = None
    for n, side in u.leaves:
        for m, s2 in lv:
            if n == m and side and s2 and side != s2:
                continue
            if n == m:
                return "exact"
            if abs(n - m) <= tol and best is None:
                best = "fuzzy"
    return best


def _mention_hit(u, mt, tol):
    """'exact' | 'fuzzy' | None: does this one mention name the unit's folio, canvas or id (volume aside)?"""
    if mt.kind == "id":
        return "exact" if u.ids & mt.ids else None
    if mt.kind == "canvas":
        return "exact" if u.canvases & mt.canvases else None
    return _leaf_hit(u, mt.leaves, tol)


def match(u, text, multi_volume=False, tol=0, context_vols=None):
    """How a text names the unit u (see the module docstring)."""
    k = parse(text)
    text_real = {v for v in k.vols if not v.startswith("hint:")}
    if u.ids and ((u.ids & k.ids) or _wvo_bare(u, text)):
        if not u.vols or not text_real or (u.vols & text_real):
            return "exact"
    if not (_leaf_hit(u, k.leaves, tol) or (u.canvases & k.canvases)):
        return None
    levels = []
    for mt in mentions(text):
        if mt.kind == "id":
            continue
        hit = _mention_hit(u, mt, tol)
        if not hit:
            continue
        if mt.vol is not None:
            ok = _vol_ok(u.vols, {mt.vol})
            if not u.vols:
                levels.append("ambiguous")
            elif ok:
                levels.append(hit)
            continue
        if u.vols & text_real:
            levels.append(hit)
        elif text_real or not u.vols:
            levels.append("ambiguous" if (text_real or multi_volume) else hit)
        elif context_vols:
            ctx_real = {v for v in context_vols if not v.startswith("hint:")}
            levels.append(hit if ctx_real and ctx_real <= u.vols else ("ambiguous" if ctx_real else hit))
        elif multi_volume:
            levels.append("ambiguous")
        else:
            levels.append(hit)
    for lvl in ("exact", "fuzzy", "ambiguous"):
        if lvl in levels:
            return lvl
    return None


def mention_is_unit(u, mt):
    """True when this one mention names the unit (its folio, canvas or id, in its volume or with none bound)."""
    if mt.kind == "id":
        return bool(mt.ids & u.ids)
    return _mention_hit(u, mt, 0) == "exact" and (mt.vol is None or not u.vols or bool(_vol_ok(u.vols, {mt.vol})))


def bare_wvo_positions(u, text):
    """[(start, is_unit)] for bare numbers in a list beside the unit's own bare WVO number ('4610,4611,4612')."""
    out = []
    own = {i[4:] for i in u.ids if i.startswith("wvo:")}
    if not own:
        return out
    for m in re.finditer(r"(?<![\w./$-])(\d{3,5})(?![\w/-]|\.\d)", text or ""):
        n = m.group(1)
        if int(n) in YEARLIKE and n not in own:
            continue
        out.append((m.start(), n in own))
    if not any(x for _, x in out):
        return []
    units = [p for p, x in out if x]
    return [(p, x) for p, x in out if x or any(abs(p - q) <= 12 for q in units)]


def _id_kind(i):
    return "R" if re.fullmatch(r"R\d+", i) else i.split(":")[0]


def names_other(u, text):
    """True when the text names a folio, canvas or id that is not one of the unit's: a leaf of the same folio but the
    other side, a folio bound to another volume, or an id of a kind the unit has (another R-id, WVO nr, pointer or
    label). Folios are not compared for a unit keyed by ids only, nor ids of a kind the unit lacks."""
    kinds = {_id_kind(i) for i in u.ids}
    if _wvo_bare(u, text) and any(not x for _, x in bare_wvo_positions(u, text)):
        return True                     # '4610,4611,4612,4616': a list of letters, not this one alone
    for mt in mentions(text):
        if mt.kind == "id":
            if not (mt.ids & u.ids) and any(_id_kind(i) in kinds for i in mt.ids):
                return True
            continue
        if not (u.leaves or u.canvases):
            continue
        if _mention_hit(u, mt, 0) == "exact" and (mt.vol is None or not u.vols or _vol_ok(u.vols, {mt.vol})):
            continue
        return True
    return False


def main(argv=None):
    a = list(sys.argv[1:] if argv is None else argv)
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if a[0] == "--match" and len(a) == 3:
        k = parse(a[1])
        print(match(Keys(k.vols, k.leaves, k.canvases, k.ids), a[2]))
        return 0
    k = parse(" ".join(a))
    print(f"vols={sorted(k.vols)} leaves={sorted(k.leaves)} canvases={sorted(k.canvases)} ids={sorted(k.ids)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
