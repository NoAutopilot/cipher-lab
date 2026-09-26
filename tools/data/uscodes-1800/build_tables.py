#!/usr/bin/env python3
"""Parse the raw fetched code tables in raw/ into value->plaintext TSVs.

Offline: reads only files already committed under raw/. Re-run after any raw/ file changes
to regenerate the TSVs; `--check` exits non-zero if a committed TSV is stale (CLAUDE.md rule 7).
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
RAW = HERE / "raw"


def write_tsv(path, rows):
    lines = ["value\tplaintext\tgrade\tsource_line"]
    for value, plaintext, grade, source_line in rows:
        lines.append(f"{value}\t{plaintext}\t{grade}\t{source_line}")
    text = "\n".join(lines) + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.write_text(text, encoding="utf-8")
    return True


def parse_we028():
    """WE028.txt: 'value;plaintext' per line, 1600 entries, one code (Monroe<->Madison).
    Served by cryptiana.web.fc2.com (a Japanese host) as Shift-JIS, not UTF-8 -- a handful of
    entries (e.g. 1261-1267, punctuation; 375, a Japanese gloss) are non-ASCII."""
    rows = []
    src = RAW / "WE028.txt"
    for i, line in enumerate(src.read_bytes().decode("shift_jis").splitlines(), start=1):
        line = line.strip()
        if not line:
            continue
        value, _, plaintext = line.partition(";")
        rows.append((value.strip(), plaintext.strip(), "H", f"raw/WE028.txt:{i}"))
    return rows


def parse_key972_bourdeau():
    """key972.js: JS object literal that is valid JSON (BOM-prefixed), value: [plaintext, grade]."""
    src = RAW / "key972_bourdeau.js"
    text = src.read_text(encoding="utf-8-sig")
    m = re.search(r"\{.*\}", text, re.S)
    data = json.loads(m.group(0))
    rows = []
    for value, (plaintext, grade) in data.items():
        rows.append((value, plaintext, grade, "raw/key972_bourdeau.js:1"))
    rows.sort(key=lambda r: int(r[0]))
    return rows


def parse_code972_partial_tomokiyo():
    """code972_partial.json: value -> list of candidate readings (raw harvest, pre-Bourdeau cleanup).
    Grade M if any reading carries a '?' or '...' uncertainty marker or a bracketed alternative, else C
    (Tomokiyo's own convention, per madison.htm's Legend: readings are from a single known-plaintext letter)."""
    src = RAW / "code972_partial_tomokiyo.json"
    data = json.loads(src.read_text(encoding="utf-8"))
    rows = []
    for value, readings in data.items():
        plaintext = readings[0]
        grade = "M" if any(("?" in r or "..." in r) for r in readings) else "C"
        rows.append((value, plaintext, grade, "raw/code972_partial_tomokiyo.json:1"))
    rows.sort(key=lambda r: int(r[0]))
    return rows


def parse_madison_the972_tomokiyo():
    """madison_THE_972.txt: ';'-comment header then 'value;plaintext' lines, Tomokiyo's own cleaned
    95-entry partial table (cryptiana.web.fc2.com/code/madison_THE_972.txt)."""
    rows = []
    src = RAW / "madison_THE_972_tomokiyo.txt"
    for i, line in enumerate(src.read_text(encoding="utf-8").splitlines(), start=1):
        line = line.strip()
        if not line or line.startswith(";"):
            continue
        value, _, plaintext = line.partition(";")
        rows.append((value.strip(), plaintext.strip(), "C", f"raw/madison_THE_972_tomokiyo.txt:{i}"))
    return rows


TABLES = {
    "WE028.tsv": parse_we028,
    "THE972_bourdeau.tsv": parse_key972_bourdeau,
    "THE972_tomokiyo_partial.tsv": parse_code972_partial_tomokiyo,
    "THE972_tomokiyo_clean.tsv": parse_madison_the972_tomokiyo,
}


def main():
    check = "--check" in sys.argv
    stale = []
    for name, fn in TABLES.items():
        rows = fn()
        changed = write_tsv(HERE / name, rows)
        if changed and check:
            stale.append(name)
        print(f"{name}: {len(rows)} entries" + (" (rewritten)" if changed else ""))
    if check and stale:
        print("STALE:", ", ".join(stale))
        sys.exit(1)


if __name__ == "__main__":
    main()
