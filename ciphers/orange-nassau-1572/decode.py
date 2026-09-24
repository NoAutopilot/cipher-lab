#!/usr/bin/env python3
"""Mechanically apply Nepveu tot Ameyde's 1842 key to this target's ciphertext(s).

Reproducible per CLAUDE.md rule 7: regenerates reading.txt (and reading_2.txt, if
ciphertext_2.txt is present) from the ciphertext file(s) and key_nepveu.tsv.
--check recomputes both in memory and exits non-zero if either committed reading
file is stale (does not overwrite anything in --check mode).

What this script does NOT do: it does not apply nepveu_corrections.tsv's 7 footnoted
numeral corrections for CCCLXXXV to ciphertext.txt. Those corrections cite the
printed 1836 numerals as Nepveu himself read them from the original; this file's
ciphertext.txt is a DIFFERENT, independent OCR pass (Google/Internet Archive) of the
same print, and an exact-string search for each correction's "as printed" value in
ciphertext.txt found no match (the two OCR passes misread the same digits
differently). Locating them would require comparing against the page image, which
is solver work this script's brief does not cover -- see NOTES.md.

Grading (per this target's brief, not the general CLAUDE.md rule-4 scale):
  H  Nepveu's key gives the value directly: the printed numeral, after only the
     OCR-digit-misread normalisation ciphertext.txt's own header sanctions
     (lowercase l/i for "1", "o" for "0"), parses to an integer 1-99, which
     key_nepveu.tsv resolves to a letter (multiple of 3, 3-72) or, per Nepveu's
     own stated rule ("de overige cijfers zijn non-valeurs"), to a null.
  M  uncertain: the token parses to a clean integer only after also stripping a
     single stray, clearly non-digit typographic character (a bracket, caret,
     asterisk, apostrophe) that is not part of the sanctioned substitution --
     flagged, not decoded (no letter is emitted into reading.txt for these).
  U  unread: the token does not parse under either rule above.
A token containing a literal "^" or a fragment of "1572"/"1567"/"septembre" is
margin/running-head bleed (the lost two-column layout), not a cipher group at all;
these are counted separately and never graded H/M/U.
"""
import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (ciphertext filename, reading-output filename, footnote line-ranges to exclude from
# group-scanning -- Groen's own editorial footnotes citing other works, 1-indexed
# inclusive, matching the committed file -- and a short label for the report)
TARGETS = [
    ("ciphertext.txt", "reading.txt",
     [(110, 116), (157, 164), (189, 201), (233, 238), (367, 382)],
     "CCCLXXXV (main target)"),
    ("ciphertext_2.txt", "reading_2.txt", [],
     "CCCLXXXVII (companion letter)"),
]

MARGIN_RE = re.compile(r"\^|1572|1567|ptem", re.IGNORECASE)
NOISE_CHARS_RE = re.compile(r"[\]\[\^'’*‸,]")
SKIPPABLE_RE = re.compile(r"^[\(\[][A-Za-z0-9]{1,3}[\)\]]\.?$")
DIGIT_SUBST = str.maketrans({"i": "1", "I": "1", "l": "1", "L": "1", "o": "0", "O": "0"})


def load_key(path):
    key = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if row.get("group"):
                key[int(row["group"])] = row["value"]
    return key


def strip_core(token):
    """Strip trailing punctuation Nepveu's own group-separator convention uses
    (periods, stray asterisks) to get the bare group text."""
    return token.strip().rstrip("*").rstrip(".").rstrip("*")


def classify(core):
    """Return (kind, value) for a stripped token core: kind in {H, M, U, margin}."""
    if MARGIN_RE.search(core):
        return "margin", None
    normalized = core.translate(DIGIT_SUBST)
    if normalized.isdigit() and normalized != "":
        return "H", int(normalized)
    denoised = NOISE_CHARS_RE.sub("", normalized)
    if denoised and denoised.isdigit() and denoised != normalized:
        return "M", int(denoised)
    return "U", None


def is_group_token(token):
    core = strip_core(token)
    return 1 <= len(core) <= 3 and token.rstrip().endswith((".", "*"))


def find_runs(tokens, excluded_lines):
    """tokens: list of (lineno, token). Returns list of index-lists, each a run of
    >=2 consecutive group-candidate tokens (skipping footnote-marker tokens like
    "(1)" and tokens on excluded lines, which both break/exclude a run)."""
    runs = []
    n = len(tokens)
    i = 0
    while i < n:
        lineno, tok = tokens[i]
        if lineno in excluded_lines or not is_group_token(tok):
            i += 1
            continue
        members = [i]
        j = i + 1
        while j < n:
            jl, jt = tokens[j]
            if jl in excluded_lines:
                break
            if is_group_token(jt):
                members.append(j)
                j += 1
            elif SKIPPABLE_RE.match(jt):
                j += 1
            else:
                break
        if len(members) >= 2:
            runs.append(members)
        i = j if j > i + 1 else i + 1
    return runs


def load_body(ciphertext_path):
    """Return list of (lineno, line_text) for non-comment lines, 1-indexed to match
    the committed file exactly."""
    lines = ciphertext_path.read_text(encoding="utf-8").split("\n")
    out = []
    for idx, line in enumerate(lines, start=1):
        if line.strip().startswith("#"):
            continue
        out.append((idx, line))
    return out


def decode_target(ciphertext_path, key, excluded_lines):
    body_lines = load_body(ciphertext_path)
    # (lineno, token, start, end) so we can splice replacements back into each line
    tokens = []
    for lineno, line in body_lines:
        for m in re.finditer(r"\S+", line):
            tokens.append((lineno, m.group(0), m.start(), m.end()))
    tok_only = [(t[0], t[1]) for t in tokens]
    excluded = set()
    for a, b in excluded_lines:
        excluded.update(range(a, b + 1))
    runs = find_runs(tok_only, excluded)
    run_index = {idx: r for r in runs for idx in r}

    grades = Counter()
    unread_freq = Counter()
    margin_count = 0
    group_count = 0
    letters_out = []

    line_text = {lineno: line for lineno, line in body_lines}
    replacements = {}  # (lineno, start, end) -> replacement text

    for i, (lineno, tok, start, end) in enumerate(tokens):
        if i not in run_index:
            continue
        core = strip_core(tok)
        kind, value = classify(core)
        group_count += 1
        if kind == "margin":
            margin_count += 1
            continue
        grades[kind] += 1
        if kind == "H":
            letter = key.get(value, "·")  # middle dot = non-valeur/null
            if letter not in ("·",):
                letters_out.append(letter.split("/")[0])
            replacements[(lineno, start, end)] = f"[{letter}]"
        elif kind == "M":
            replacements[(lineno, start, end)] = f"[M:{core}]"
        else:
            unread_freq[core] += 1
            replacements[(lineno, start, end)] = f"[U:{core}]"

    # rebuild text, line by line, splicing in replacements at exact spans
    out_lines = []
    for lineno, line in body_lines:
        spans = sorted((s, e, r) for (ln, s, e), r in replacements.items() if ln == lineno)
        if not spans:
            out_lines.append(line)
            continue
        pieces = []
        cursor = 0
        for s, e, r in spans:
            pieces.append(line[cursor:s])
            pieces.append(r)
            cursor = e
        pieces.append(line[cursor:])
        out_lines.append("".join(pieces))

    reading_text = "\n".join(out_lines) + "\n"
    return reading_text, grades, unread_freq, margin_count, group_count, len(runs)


def build_report(label, grades, unread_freq, margin_count, group_count, run_count):
    total = sum(grades.values())
    lines = [
        f"# Mechanical decode report -- {label}",
        f"# generated by decode.py; do not hand-edit",
        f"# {run_count} numeral runs, {group_count} group tokens scanned "
        f"({margin_count} excluded as margin/running-head bleed, not cipher)",
        f"# graded: H={grades.get('H', 0)} M={grades.get('M', 0)} "
        f"U={grades.get('U', 0)} (of {total} graded groups)",
    ]
    if unread_freq:
        lines.append("# unread (U) groups by frequency:")
        for tok, n in sorted(unread_freq.items(), key=lambda kv: (-kv[1], kv[0])):
            lines.append(f"#   {tok!r}: {n}")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                     help="verify committed reading file(s) are up to date; exit "
                          "non-zero if stale; never writes")
    args = ap.parse_args()

    key = load_key(HERE / "key_nepveu.tsv")
    stale = False
    any_target = False

    for cipher_name, reading_name, excluded, label in TARGETS:
        cipher_path = HERE / cipher_name
        if not cipher_path.exists():
            continue
        any_target = True
        reading_text, grades, unread_freq, margin_count, group_count, run_count = (
            decode_target(cipher_path, key, excluded)
        )
        report = build_report(label, grades, unread_freq, margin_count, group_count, run_count)
        full_text = report + "#\n" + reading_text
        reading_path = HERE / reading_name

        if args.check:
            if not reading_path.exists() or reading_path.read_text(encoding="utf-8") != full_text:
                print(f"STALE: {reading_name} does not match a fresh decode of {cipher_name}",
                      file=sys.stderr)
                stale = True
            else:
                print(f"OK: {reading_name} matches {cipher_name}")
        else:
            reading_path.write_text(full_text, encoding="utf-8")
            print(f"wrote {reading_name}: H={grades.get('H', 0)} M={grades.get('M', 0)} "
                  f"U={grades.get('U', 0)} margin={margin_count} runs={run_count}")

    if not any_target:
        print("no ciphertext files found", file=sys.stderr)
        sys.exit(2)
    if args.check and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
