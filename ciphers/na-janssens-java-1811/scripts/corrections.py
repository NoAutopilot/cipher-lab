#!/usr/bin/env python3
"""Read corrections.tsv rows that apply to one pass/leaf TSV (JAV-CORR, 15 Oct 2026).

corrections.tsv columns: line pos token corrected value grade read_grade source reason file. A row applies to a pass file
when its `file` column (';'-separated) names that file's basename; the pass files stay as transcribed (CLAUDE.md Layout)
and the correction is applied in memory at read time. Keying is (line, pos) as in decode_key.py's exceptions: for the
gloss-pass files (leaf, order, code, gloss, note) the line label is the leaf, written bare ("200") or with a prefix
naming the source ("keysource-200": the part after the last '-'), and pos is the pass's own `order` column. A row whose
`file` is ciphertext.tsv (decode_key.py's business) never applies here.

apply(rows, corr) replaces `code` on each keyed row; a keyed row whose code is not the correction's `token` is a stale
correction (the pass was re-read or renumbered) and raises, so a rebuild cannot silently skip it, and a correction that
matches no row raises too.
"""
import csv
import os


def load(corrections_path, pass_path):
    """{(leaf, order): row} for corrections.tsv rows naming pass_path's basename; {} when the file is absent."""
    if not corrections_path or not os.path.exists(corrections_path):
        return {}
    base = os.path.basename(pass_path)
    out = {}
    with open(corrections_path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            files = [x.strip() for x in (r.get("file") or "").split(";") if x.strip()]
            if base not in files:
                continue
            leaf = r["line"].strip().rsplit("-", 1)[-1]
            out[(leaf, r["pos"].strip())] = r
    return out


def apply(rows, corr, label=""):
    """Apply corrections in place to pass rows (dicts with leaf, order, code); returns the list of (leaf, order, old, new)."""
    done = []
    seen = set()
    for row in rows:
        k = (row["leaf"].strip(), row["order"].strip())
        c = corr.get(k)
        if c is None:
            continue
        if row["code"].strip() != c["token"].strip():
            raise SystemExit(f"stale correction {label} {k}: pass reads {row['code']!r}, corrections.tsv expects "
                             f"{c['token']!r} -> {c['corrected']!r}")
        row["code"] = c["corrected"].strip()
        done.append((k[0], k[1], c["token"].strip(), row["code"]))
        seen.add(k)
    missing = sorted(set(corr) - seen)
    if missing:
        raise SystemExit(f"corrections.tsv rows for {label} match no pass row: {missing}")
    return done
