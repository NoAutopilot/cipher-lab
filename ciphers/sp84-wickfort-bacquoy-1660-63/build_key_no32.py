#!/usr/bin/env python3
"""Build key.tsv for TNA SP 106/6 no. 32 (the Chauran/Wickfort encoding table) from
DECODE's own 2020 text transcriptions of records 509 (TNA_SP106/6_CharlesII_(0099-0101),
pages 3711-3713) and 506 (TNA_SP106/6_CharlesII_(0096), page 3705).

Grade H throughout: every value is DECODE's own transcription (transcriber "AP", 2020) of
the period key document, not a cryptanalytic recovery (CLAUDE.md rule 4). This script does
not decode anything and is never given a ciphertext.

Usage:
  python3 build_key_no32.py build --doc2952 PATH --doc2953 PATH --doc2951 PATH [--out key.tsv]
      Parse the three raw DECODE documents and write key.tsv.
  python3 build_key_no32.py --check --doc2952 PATH --doc2953 PATH --doc2951 PATH
      Rebuild in memory and diff against the committed key.tsv; exit 1 if it differs
      (CLAUDE.md rule 7). Requires the three raw documents (not committed to this repo;
      re-fetch with tools/decode_browser_login.js per sources/decode/NOTES.md).
  python3 build_key_no32.py --check-hash --doc2952 PATH --doc2953 PATH --doc2951 PATH
      No parsing: just sha256 each given path and compare against the sha256 already
      recorded in sources/decode/2026-10-24-sp106-6-keys/{509,506}/manifest.json, so a later
      session can confirm it fetched byte-identical text before trusting a diff against the
      committed key.tsv.

The three source documents:
  doc2952 = DOC_R509_D2952_2952.txt  (record 509, pages 3712-3713: letter alphabet, person/
            ville/royaume codes, and the A-L word/syllable homophone lists)
  doc2953 = DOC_R509_D2953_2953.txt  (record 509, page 3711: the M-Z word/syllable homophone
            lists continuation, plus the null row)
  doc2951 = DOC_R506_D2951_2951.txt  (record 506, page 3705: a second, overlapping copy of
            the letter alphabet and person/ville/royaume codes)

Class heuristic: "letter" (A-Z minus J/U homophones), "person", "ville", "royaume" are read
directly from DECODE's own section markers (<CLEARTEXT FR Villes>, <CLEARTEXT FR Royaulmes>,
the double-underscore/primed person-name block). The remaining homophone-class entries after
Royaulmes are "word" or "syllable" and DECODE does not mark which is which; this script uses
a short, named, closed list of common French one-to-three-letter syllable fragments (see
SYLLABLE_FRAGMENTS below) to split them -- a descriptive heuristic for this key.tsv's own
class column, not a cryptanalytic judgement, and is stated as such in NOTES.md.
Conflict classification (job KEY32-CONFLICTS, 24 Oct 2026,
.claude/briefs/runs/2026-10-24-acct4-research-director-50.md): build() always fills a
row's conflict_kind for the conflict-flagged rows (so a future --check rebuild from
raw docs stays consistent with the committed file), using classify_conflict_group()
below. conflicts.py (same folder) is the offline entry point: it reads the already-
committed key.tsv (no raw documents needed -- every meaning a conflict needs is
already in the table) via read_committed_rows(), recomputes conflict_kind the same
way, writes conflicts.tsv, and calls retag_conflict_kinds() here to rewrite key.tsv
in place with the new column -- the single script that writes key.tsv (rule 7) stays
the only writer; conflicts.py never hand-edits key.tsv itself.
"""
import argparse
import hashlib
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent

# Whole tokens dropped before comparing two meanings for "identical after
# normalisation" -- titles, honorific abbreviations and articles that this
# key's transcriptions render inconsistently (M^r vs m^r <abbr monsieur>,
# "le Duc" vs "le d.", "De" vs "d'"). Dropping them can only ever make two
# strings look MORE alike, never less, so it cannot manufacture a false
# "identical" between two genuinely different referents on its own -- the
# Levenshtein spelling-variant check below still applies to what is left.
TITLE_TOKENS = {
    "mr", "mre", "me", "mrs", "abbr", "monsieur", "madame", "mademoiselle",
    "le", "la", "les", "de", "du", "des", "d",
    "duc", "d.", "comte", "c", "cal", "cardinal", "prince", "p",
    "roy", "royne",
}


def strip_tags(s: str) -> str:
    return re.sub(r"<[^>]*>", "", s)


def strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def normalize_meaning(raw: str) -> str:
    """Fold case, accents, the caret superscript marker, u/v and i/j
    (period orthography treats them as interchangeable), punctuation and
    whitespace, title/article tokens, and one trailing 's', per the
    identical-after-normalisation definition in conflicts.py's docstring."""
    s = strip_tags(raw)
    s = s.lower()
    s = strip_accents(s)
    s = s.replace("^", "")
    s = re.sub(r"[.,;:!?\"'’`]", "", s)
    s = s.replace("v", "u").replace("j", "i")
    s = re.sub(r"\s+", " ", s).strip()
    tokens = [t for t in s.split(" ") if t and t not in TITLE_TOKENS]
    joined = "".join(tokens)
    joined = re.sub(r"s$", "", joined)
    return joined


def levenshtein(a: str, b: str) -> int:
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i] + [0] * len(b)
        for j, cb in enumerate(b, 1):
            cost = 0 if ca == cb else 1
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost)
        prev = cur
    return prev[-1]

# Listed period variants that survive normalize_meaning() more than 2 edits
# apart but are a documented same-referent spelling pair (CLAUDE.md rule 4:
# a conflict is logged, never resolved by majority -- this list only ever
# relabels the *kind*, never the meaning itself, and both key.tsv rows keep
# their own grade-H text unchanged).
VARIANT_PAIRS = set()


def is_spelling_variant(norm_a: str, norm_b: str) -> bool:
    if not norm_a or not norm_b:
        return False
    if levenshtein(norm_a, norm_b) <= 2:
        return True
    return frozenset((norm_a, norm_b)) in VARIANT_PAIRS


def _side_of(source: str):
    """'509 p2-3' -> '509'; '506' -> '506'; '509 p1' -> None (matches build()'s
    own exclusion of 509 p1 from the by_key cross-check: it is a different
    page reusing the same small 1-100 code range for the M-Z continuation of
    the word/syllable list, not a second copy of 509 p2-3's own A-L codes --
    folding it into '509' produced 65 spurious within-source 'duplicates'
    that were really page-boundary code reuse, not a real transcription
    conflict; caught by testing against the committed key.tsv before this
    job's first commit)."""
    if source == "506":
        return "506"
    if source == "509 p2-3":
        return "509"
    return None


def classify_conflict_groups(rows):
    """Group rows by (class, code, mark), find every group build()'s own
    cross-check would flag `conflict` (509 and 506 both present, >1 distinct
    raw meaning), and return {group_key: (kind, note)}. Read-only: never
    mutates rows. Works identically whether rows came fresh from build() or
    from read_committed_rows() on the already-committed key.tsv, since the
    classification only needs (class, code, mark, meaning, source) -- already
    in the table either way, no raw DECODE document required."""
    by_key = {}
    for r in rows:
        side = _side_of(r["source"])
        if side is None:
            continue
        by_key.setdefault((r["class"], r["code"], r["mark"]), {"509": [], "506": []})[side].append(r["meaning"])

    # Reverse index per side per class: normalised meaning -> set of codes,
    # for the same-meaning-different-code cross-reference.
    index = {"509": {}, "506": {}}
    for (cls, code, mark), sides in by_key.items():
        for side in ("509", "506"):
            for meaning in sides[side]:
                norm = normalize_meaning(meaning)
                if not norm:
                    continue
                index[side].setdefault(cls, {}).setdefault(norm, set()).add((code, mark))

    kinds = {}
    for key, sides in by_key.items():
        cls, code, mark = key
        m509 = sorted(set(sides["509"]))
        m506 = sorted(set(sides["506"]))
        if not m509 or not m506:
            continue  # not a 509-vs-506 pair at all (509-p1-only or similarly excluded)
        if len(m509) == 1 and len(m506) == 1 and m509[0].strip().lower() == m506[0].strip().lower():
            continue  # not actually conflicting (build()'s own case-sensitive check can over-flag; rare)
        if len(m509) > 1 or len(m506) > 1:
            kinds[key] = ("other", f"within-source duplicate: 509={m509!r} 506={m506!r}")
            continue
        a, b = m509[0], m506[0]
        a_blank = a.strip() in ("", "?", "<NULL>")
        b_blank = b.strip() in ("", "?", "<NULL>")
        if a_blank or b_blank:
            kinds[key] = ("one-side-blank", f"509={a!r} 506={b!r}")
            continue
        na, nb = normalize_meaning(a), normalize_meaning(b)
        if na == nb:
            kinds[key] = ("identical-after-normalisation", f"509={a!r} 506={b!r} -> {na!r}")
            continue
        if is_spelling_variant(na, nb):
            kinds[key] = ("spelling-variant", f"509={a!r} 506={b!r} ({na!r} vs {nb!r})")
            continue
        found_a_elsewhere = any(
            other != (code, mark) for other in index["506"].get(cls, {}).get(na, set())
        )
        found_b_elsewhere = any(
            other != (code, mark) for other in index["509"].get(cls, {}).get(nb, set())
        )
        if found_a_elsewhere or found_b_elsewhere:
            kinds[key] = ("same-meaning-different-code", f"509={a!r} 506={b!r}")
            continue
        kinds[key] = ("same-code-different-meaning", f"509={a!r} 506={b!r}")
    return kinds


def apply_conflict_kinds(rows):
    """Set row['conflict_kind'] in place for every row (default '', filled
    only for rows in a classify_conflict_groups() group); returns the kinds
    dict for the caller (conflicts.py) to also write conflicts.tsv from."""
    kinds = classify_conflict_groups(rows)
    for r in rows:
        r["conflict_kind"] = ""
    for r in rows:
        side = _side_of(r["source"])
        if side is None:
            continue
        key = (r["class"], r["code"], r["mark"])
        if key in kinds:
            r["conflict_kind"] = kinds[key][0]
    return kinds


def read_committed_rows(path: Path):
    """Read an already-committed key.tsv back into the row-dict shape
    build()/write_tsv() use (skipping '#' header comment lines), for a pass
    (conflicts.py) that enriches the file without the raw DECODE documents."""
    text = path.read_text(encoding="utf-8")
    lines = [l for l in text.splitlines() if l and not l.startswith("#")]
    header = lines[0].split("\t")
    rows = []
    for line in lines[1:]:
        vals = line.split("\t")
        vals += [""] * (len(header) - len(vals))
        rows.append(dict(zip(header, vals)))
    return rows

SYLLABLE_FRAGMENTS = {
    "le", "la", "de", "du", "ge", "ji", "ri", "lu", "bo", "co", "fi", "gi", "hi", "ho",
    "ja", "jo", "ma", "mi", "mo", "mu", "na", "ne", "ni", "no", "pa", "pe", "pi", "po",
    "pu", "qua", "qui", "quo", "quu", "quil", "quel", "quelque", "ra", "re", "ri", "ru",
    "sa", "se", "si", "so", "su", "ta", "te", "ti", "to", "tu", "va", "ve", "vi", "vo",
    "vu", "xa", "xe", "xi", "xo", "xu", "ba", "ca", "ci", "da", "di", "do", "fa", "fo",
    "ga", "go", "gu", "ha", "ka", "ke", "ki", "ko", "ku", "li", "lo", "me", "oulre",
}


def classify_word(meaning: str) -> str:
    first = meaning.split(",")[0].split("?")[0].strip().lower()
    first = re.sub(r"[^a-zàâäéèêëïîôöùûüç]", "", first)
    if first and len(first) <= 3 and first in SYLLABLE_FRAGMENTS:
        return "syllable"
    return "word"


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_person_code(raw: str):
    """'2__0__' -> '20'; '5__1__^'\'' -> ('51', \"'\"); '1^\\'2' -> ('12', \"'\") best-effort.
    Returns (code, mark) where mark is '' for a plain double-underscore person code, or the
    trailing/embedded diacritic token otherwise, with the raw string preserved as a fallback
    if the digits cannot be cleanly recovered (never silently dropped)."""
    m = re.fullmatch(r"(\d)__(\d)__(\^.*)?", raw)
    if m:
        d1, d2, mark = m.group(1), m.group(2), m.group(3) or ""
        mark = mark.lstrip("^")
        return d1 + d2, mark
    m = re.fullmatch(r"(\d)\^'(\d)", raw)
    if m:
        return m.group(1) + m.group(2), "'"
    m = re.fullmatch(r"(\d{1,3})\^'", raw)
    if m:
        return m.group(1), "'"
    return raw, "RAW"


def split_entry(line: str):
    """Split one 'CODE[S] - MEANING' line. CODE[S] may be several '|'-joined alternates."""
    if " - " not in line:
        return None
    code_part, meaning = line.split(" - ", 1)
    codes = [c.strip() for c in code_part.strip().split("|") if c.strip()]
    return codes, meaning.strip()


def parse_letter_line(codes, meaning, source_tag, rows, seen_letters):
    """codes like ['23^m', '18^co', 'InvertedLazySWithCurledEnds'] all -> same letter."""
    for c in codes:
        m = re.fullmatch(r"(\d+)\^(m|co)", c)
        if m:
            rows.append({"code": m.group(1), "mark": m.group(2), "meaning": meaning,
                         "class": "letter", "source": source_tag, "grade": "H", "note": ""})
        else:
            rows.append({"code": c, "mark": "", "meaning": meaning,
                         "class": "letter", "source": source_tag, "grade": "H", "note": ""})
    seen_letters.setdefault(meaning, []).append((source_tag, codes))


def parse_plain_marked_code(raw: str):
    """'79^^' -> ('79','^'); '1^..' -> ('1','..'); '45^\\'\\'' -> ('45', \"''\"); '28' -> ('28','').
    Trailing '^'-introduced mark token is whatever follows '^' to end of string."""
    m = re.fullmatch(r"(\d+)\^(.+)", raw)
    if m:
        return m.group(1), m.group(2)
    m = re.fullmatch(r"(\d+)", raw)
    if m:
        return m.group(1), ""
    return raw, "RAW"


def parse_document(text: str, source_tag: str, rows, seen, is_2953=False):
    lines = [l.rstrip() for l in text.splitlines()]
    section = "word" if is_2953 else "letter"  # 2953 is pure continuation word list
    for raw_line in lines:
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line == "<CLEARTEXT FR Villes>":
            section = "ville"
            continue
        if line == "<CLEARTEXT FR Royaulmes>":
            section = "royaume"
            continue
        split = split_entry(line)
        if split is None:
            continue
        codes, meaning = split
        if "<NULL>" in meaning:
            for c in codes:
                code, mark = parse_plain_marked_code(c)
                rows.append({"code": code, "mark": mark, "meaning": "<NULL>",
                             "class": "other", "source": source_tag, "grade": "H", "note": "null"})
            continue
        if section == "letter":
            if not is_2953 and not any("__" in c or c.startswith(tuple("0123456789")) and "'" in c for c in codes):
                pass
            # letter section ends once we hit the first double-underscore person code
            if any(re.fullmatch(r"\d__\d__(\^.*)?", c) for c in codes):
                section = "person"
            else:
                parse_letter_line(codes, meaning, source_tag, rows, seen.setdefault("letter", {}))
                continue
        if section == "person":
            # person section ends at the <CLEARTEXT FR Villes> marker (handled above); but
            # also ends (503/506) when a plain small-integer word code starts appearing
            # immediately after Royaulmes -- that transition is handled by the explicit
            # Villes/Royaulmes markers so nothing extra needed here.
            for c in codes:
                code, mark = parse_person_code(c)
                rows.append({"code": code, "mark": mark, "meaning": meaning,
                             "class": "person", "source": source_tag, "grade": "H", "note": ""})
            continue
        if section == "ville":
            for c in codes:
                code, mark = parse_person_code(c) if ("__" in c or "^'" in c) else parse_plain_marked_code(c)
                rows.append({"code": code, "mark": mark or "'", "meaning": meaning,
                             "class": "ville", "source": source_tag, "grade": "H", "note": ""})
            continue
        if section == "royaume":
            # Royaulmes block (90'-108') is immediately followed, with no header, by the
            # A-L word/syllable homophone lists (chauran.htm's own description groups these
            # as a separate table) -- detect the switch by mark: a '-prefixed/suffixed code
            # with a two/three-digit number >=90 near the top, falling to '..'/'^'/'"'/quoted
            # marks or plain numbers signals the word list has begun.
            if "'" in codes[0] or re.fullmatch(r"\d{1,3}\^'", codes[0]) or re.search(r"\^'", codes[0]):
                for c in codes:
                    code, mark = parse_person_code(c) if ("__" in c or "'" in c) else parse_plain_marked_code(c)
                    rows.append({"code": code, "mark": mark or "'", "meaning": meaning,
                                 "class": "royaume", "source": source_tag, "grade": "H", "note": ""})
                continue
            else:
                section = "word"
        # word / syllable homophone lists
        cls_guess = classify_word(meaning)
        for c in codes:
            code, mark = parse_plain_marked_code(c)
            rows.append({"code": code, "mark": mark, "meaning": meaning,
                         "class": cls_guess, "source": source_tag, "grade": "H", "note": ""})


def build(doc2952: Path, doc2953: Path, doc2951: Path):
    rows = []
    seen = {}
    parse_document(doc2952.read_text(encoding="utf-8", errors="replace"), "509 p2-3", rows, seen)
    parse_document(doc2953.read_text(encoding="utf-8", errors="replace"), "509 p1", rows, seen, is_2953=True)
    parse_document(doc2951.read_text(encoding="utf-8", errors="replace"), "506", rows, seen)

    # cross-check 509 vs 506 on overlapping (class, code) pairs for conflicting meanings
    by_key = {}
    for r in rows:
        if r["source"] == "509 p1":
            continue  # 3711 has no 506 counterpart (506 is a single page, person/letter/ville only)
        k = (r["class"], r["code"], r["mark"])
        by_key.setdefault(k, []).append(r)
    for k, group in by_key.items():
        sources = {r["source"] for r in group}
        if "509 p2-3" in sources and "506" in sources:
            meanings = {r["meaning"].strip().lower() for r in group}
            if len(meanings) > 1:
                for r in group:
                    others = sorted(m for m in meanings if m != r["meaning"].strip().lower())
                    r["note"] = ("conflict: " + r["source"] + "=" + r["meaning"] + " vs " +
                                  ",".join(o for o in others)) if r["note"] == "" else r["note"] + "; conflict"
    apply_conflict_kinds(rows)
    return rows


KEY_COLS = ["code", "mark", "meaning", "class", "source", "grade", "note", "conflict_kind"]


def write_tsv(rows, out: Path):
    cols = KEY_COLS
    header_lines = [
        "# TNA SP 106/6 no. 32 (Tomokiyo's numbering, sources/cryptiana/web/chauran.htm), the",
        "# Chauran/Wickfort French encoding table. DECODE records 509 (TNA_SP106/6_CharlesII_",
        "# (0099-0101), pages 3711-3713) and 506 (TNA_SP106/6_CharlesII_(0096), page 3705).",
        "# Transcriber AP, DECODE, 10/13 Aug 2020. Fetched 24 Oct 2026 (job KEY32-TSV-PROMOTE,",
        "# .claude/briefs/runs/2026-10-24-acct4-research-director-49.md). Grade H: DECODE's own",
        "# transcription of a period key document, not a cryptanalytic recovery (rule 4). The",
        "# 'word'/'syllable' class split is this script's own heuristic (see its docstring),",
        "# not part of DECODE's or Tomokiyo's description -- read it as descriptive, not graded.",
        "# conflict_kind (job KEY32-CONFLICTS, 24 Oct 2026) classifies each conflict-flagged row's",
        "# 509-vs-506 disagreement by classify_conflict_groups() in this script; see conflicts.tsv",
        "# and NOTES.md '## Conflicts'. Non-conflicting rows carry conflict_kind = ''.",
        "# Regenerate: python3 build_key_no32.py build --doc2952 .. --doc2953 .. --doc2951 ..",
        "# (conflict_kind is filled by build() itself); or, offline, python3 conflicts.py to",
        "# retag conflict_kind on the already-committed key.tsv without the raw documents.",
    ]
    lines = header_lines + ["\t".join(cols)]
    for r in rows:
        lines.append("\t".join(r.get(c, "") for c in cols))
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def read_committed(out: Path):
    if not out.exists():
        return None
    return out.read_text(encoding="utf-8")


def rows_to_text(rows):
    out_lines = []
    cols = KEY_COLS
    for r in rows:
        out_lines.append("\t".join(r.get(c, "") for c in cols))
    return "\n".join(out_lines)


MANIFESTS = {
    "doc2952": (REPO / "sources/decode/2026-10-24-sp106-6-keys/509/manifest.json", "DOC_R509_D2952_2952.txt"),
    "doc2953": (REPO / "sources/decode/2026-10-24-sp106-6-keys/509/manifest.json", "DOC_R509_D2953_2953.txt"),
    "doc2951": (REPO / "sources/decode/2026-10-24-sp106-6-keys/506/manifest.json", "DOC_R506_D2951_2951.txt"),
}


def check_hash(args):
    import json
    ok = True
    for key, path in (("doc2952", args.doc2952), ("doc2953", args.doc2953), ("doc2951", args.doc2951)):
        if not path:
            continue
        manifest_path, filename = MANIFESTS[key]
        manifest = json.loads(manifest_path.read_text())
        expected = next((e["sha256"] for e in manifest if e["file"] == filename), None)
        actual = sha256_of(Path(path))
        status = "OK" if actual == expected else "MISMATCH"
        if status != "OK":
            ok = False
        print(f"{key} ({filename}): expected={expected} actual={actual} {status}")
    sys.exit(0 if ok else 1)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("mode", nargs="?", default="build", choices=["build"])
    p.add_argument("--doc2952")
    p.add_argument("--doc2953")
    p.add_argument("--doc2951")
    p.add_argument("--out", default=str(HERE / "key.tsv"))
    p.add_argument("--check", action="store_true")
    p.add_argument("--check-hash", action="store_true")
    args = p.parse_args()

    if args.check_hash:
        check_hash(args)
        return

    if not (args.doc2952 and args.doc2953 and args.doc2951):
        print("need --doc2952 --doc2953 --doc2951 (raw DECODE documents; not committed, "
              "re-fetch per sources/decode/NOTES.md and tools/decode_browser_login.js)",
              file=sys.stderr)
        sys.exit(2)

    rows = build(Path(args.doc2952), Path(args.doc2953), Path(args.doc2951))
    new_text = rows_to_text(rows)

    out = Path(args.out)
    if args.check:
        old = read_committed(out)
        if old is None:
            print("no committed key.tsv to check against", file=sys.stderr)
            sys.exit(1)
        old_body = "\n".join(l for l in old.splitlines() if not l.startswith("#"))
        old_body = old_body[1:] if old_body.startswith("\n") else old_body
        # drop header row for comparison
        old_rows = old_body.splitlines()[1:] if old_body.splitlines() else []
        old_norm = "\n".join(old_rows).strip()
        new_norm = new_text.strip()
        if old_norm != new_norm:
            print("STALE: committed key.tsv differs from a fresh re-derivation", file=sys.stderr)
            sys.exit(1)
        print("OK: committed key.tsv matches a fresh re-derivation")
        return

    write_tsv(rows, out)
    classes = {}
    conflicts = 0
    for r in rows:
        classes[r["class"]] = classes.get(r["class"], 0) + 1
        if "conflict" in r["note"]:
            conflicts += 1
    print(f"wrote {len(rows)} rows to {out}")
    print("by class:", classes)
    print("conflicts:", conflicts)


if __name__ == "__main__":
    main()
