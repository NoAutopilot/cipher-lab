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
"""
import argparse
import hashlib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent

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
    return rows


def write_tsv(rows, out: Path):
    cols = ["code", "mark", "meaning", "class", "source", "grade", "note"]
    header_lines = [
        "# TNA SP 106/6 no. 32 (Tomokiyo's numbering, sources/cryptiana/web/chauran.htm), the",
        "# Chauran/Wickfort French encoding table. DECODE records 509 (TNA_SP106/6_CharlesII_",
        "# (0099-0101), pages 3711-3713) and 506 (TNA_SP106/6_CharlesII_(0096), page 3705).",
        "# Transcriber AP, DECODE, 10/13 Aug 2020. Fetched 24 Oct 2026 (job KEY32-TSV-PROMOTE,",
        "# .claude/briefs/runs/2026-10-24-acct4-research-director-49.md). Grade H: DECODE's own",
        "# transcription of a period key document, not a cryptanalytic recovery (rule 4). The",
        "# 'word'/'syllable' class split is this script's own heuristic (see its docstring),",
        "# not part of DECODE's or Tomokiyo's description -- read it as descriptive, not graded.",
        "# Regenerate: python3 build_key_no32.py build --doc2952 .. --doc2953 .. --doc2951 ..",
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
    cols = ["code", "mark", "meaning", "class", "source", "grade", "note"]
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
