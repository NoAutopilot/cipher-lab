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
RAH 9/, AGS, ASV, BNE ...), plus the forms it lacks: bare 'fr3040' (slugs and file names), WVO briefnr, Huntington
pointers, DECODE R-ids (ids_in()), Birch/Thurloe P-numbers and short entry labels (E78, N2-BQ, O9-BA).

API (all pure, no I/O):
  parse(text) -> Keys(vols, leaves, canvases, ids)      every identifier a text names
  unit(shelfmark, folio, canvas, ids)  -> Keys          an item's own identity
  match(unit_keys, text, multi_volume=False, tol=0)     'exact' | 'fuzzy' | 'ambiguous' | None
      'exact'     the text names one of the unit's ids, or its folio (side-compatible) in its volume
      'fuzzy'     folio within +-tol (different foliation systems: ink, finding aid, Tomokiyo); never KNOWN
      'ambiguous' the folio matches but the text names no volume and the folder holds several volumes
      None        nothing, or the folio matches in a DIFFERENT volume (fr.16104 vs fr.16105)

Must catch: 'fr.3040 f.18r' against 'f.18 (no.6) ... BnF fr.3040' (exact); 'R9502' against 'DECODE R9502'.
Must NOT match: fr.16104 f.102r against 'fr.16105 f.102r' or a crop named 'c105_f102r_L01.jpg'; f.18r against
'f.18v' (another page of the leaf); a bare year or a dollar figure as a folio.
Offline test: tools/tests/test_prior_work.py (shelfmark section).
"""
import os
import re
import sys
from collections import namedtuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decode_neighbours_exclude import ids_in, volume_keys as _volume_keys  # noqa: E402

Keys = namedtuple("Keys", "vols leaves canvases ids")

# f.18, f.18r, fol. 18v, folio 18, ff.36-37, fos 16-56; also f18r / _f102r_ inside file names (side required there)
LEAF_RE = re.compile(r"(?<![A-Za-z0-9])(?:ff?|fol|fols|fos?|folios?)\.?\s*(\d{1,4})\s*([rv])?"
                     r"(?:\s*[-–]\s*(\d{1,4})\s*([rv])?)?(?![0-9])", re.I)
FILE_LEAF_RE = re.compile(r"(?<![A-Za-z0-9])f(\d{1,4})([rv])(?![a-z0-9])", re.I)
CANVAS_RE = re.compile(r"\bcanvas(?:es)?\s*(\d{1,4})\b", re.I)
PTR_RE = re.compile(r"\b(?:ptr|pointer)\.?\s*(\d{4,5})(?:/(\d))?\b|\b(\d{4,5})/(\d)\b", re.I)
WVO_RE = re.compile(r"\b(?:WVO|briefnr\.?|brief\s*nr\.?)\s*(\d{1,5})\b", re.I)
LABEL_RE = re.compile(r"\b((?:E|T|P|N2-|O9-)\d{1,3}|N2-[A-Z]{1,2}|O9-[A-Z]{1,2})\b")
FILE_VOL_RE = re.compile(r"(?<![A-Za-z0-9])(?:c|fr)(\d{3,5})_", re.I)   # c105_f102r_, fr3040_f18r


def volume_keys(text):
    """decode_neighbours_exclude.volume_keys() plus the bare 'fr3040' form it misses."""
    keys = _volume_keys(text or "")
    for m in re.finditer(r"(?<![A-Za-z0-9])fr(\d{3,5})(?![0-9])", text or "", re.I):
        keys.add(f"bnf français {m.group(1)}")
    return keys


def _leaf(n, side):
    return (int(n), (side or "").lower())


def leaves(text):
    """{(folio_number, side)} named in text; ranges of up to 40 leaves are expanded (sides dropped inside a range)."""
    out = set()
    for m in LEAF_RE.finditer(text or ""):
        a, sa, b, sb = m.groups()
        if b and 0 < int(b) - int(a) <= 40:
            out |= {(i, "") for i in range(int(a), int(b) + 1)}
            out.add(_leaf(a, sa))
            out.add(_leaf(b, sb))
        else:
            out.add(_leaf(a, sa))
    for m in FILE_LEAF_RE.finditer(text or ""):
        out.add(_leaf(*m.groups()))
    return out


def ids(text):
    """Record ids: DECODE R-ids, Huntington pointers (ptr:9714, ptr:9714/1), WVO numbers, short entry labels."""
    s = text or ""
    out = set(ids_in(s))
    for m in PTR_RE.finditer(s):
        p, e = (m.group(1), m.group(2)) if m.group(1) else (m.group(3), m.group(4))
        out.add(f"ptr:{p}")
        if e is not None:
            out.add(f"ptr:{p}/{e}")
    out |= {f"wvo:{m.group(1)}" for m in WVO_RE.finditer(s)}
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


def match(u, text, multi_volume=False, tol=0):
    """How a text names the unit u (see the module docstring)."""
    k = parse(text)
    if u.ids and (u.ids & k.ids):
        return "exact"
    best = None
    for n, side in u.leaves:
        for m, s2 in k.leaves:
            if (side and s2 and side != s2) and n == m:
                continue
            if n == m:
                best = "exact"
            elif abs(n - m) <= tol and best is None:
                best = "fuzzy"
    if best is None and u.canvases and (u.canvases & k.canvases):
        best = "exact"
    if best is None:
        return None
    ok = _vol_ok(u.vols, k.vols)
    if ok is False:
        return None
    if ok is None and multi_volume:
        return "ambiguous"
    return best


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
