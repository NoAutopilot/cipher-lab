#!/usr/bin/env python3
"""Classify the 429 rows key.tsv already flags `conflict` (the 210 (class,
code, mark) keys where DECODE records 509 and 506 disagree on the meaning --
CLAUDE.md rule 4 keeps both rather than resolving by majority) by what KIND
of disagreement each one is. Job KEY32-CONFLICTS, 24 Oct 2026,
.claude/briefs/runs/2026-10-24-acct4-research-director-50.md.

Offline, no network, no login, no images: every meaning a conflict needs is
already in the committed key.tsv (one row per source per code) -- the raw
DECODE documents that originally produced it are not required to classify
the *kind* of a disagreement already on file, only to re-derive the meanings
themselves (that is build_key_no32.py's own --check job, unchanged).

What this script does NOT do: it never decodes, never touches any other
folder, never resolves a conflict to one value, and never hand-edits
key.tsv -- the new conflict_kind column is written back through
build_key_no32.write_tsv() (the one script build_key_no32.py already is for
this key, CLAUDE.md rule 7), using the same classify_conflict_groups()
function that build() itself now calls, so a future rebuild from the raw
documents (python3 build_key_no32.py build --doc2952 .. --doc2953 ..
--doc2951 .. --check) stays consistent with what this pass wrote.

Usage:
  python3 conflicts.py [--key key.tsv] [--out conflicts.tsv]
      Read key.tsv, classify every conflict-flagged key, write conflicts.tsv,
      rewrite key.tsv in place with the conflict_kind column, and print the
      per-kind counts and the per-class sanity table.
"""
import argparse
from pathlib import Path

import build_key_no32 as bk

HERE = Path(__file__).resolve().parent

# chauran.htm's own qualitative range description (NOTES.md "## Key"), for
# the sanity-table check: a disagreement with these ranges is a finding to
# report, never silently corrected.
EXPECTED_RANGES = {
    "person": (9, 76),   # double-underscore 20-76 plus primed 9'-60', one range here
    "ville": (61, 89),
    "royaume": (90, 108),
}

PAGE_LABEL = {"509": "509 pp.3712-3713", "506": "506 p.3705"}


def local_order_note(rows, cls, code, side):
    """Is `side`'s own value at (cls, code) alphabetically between its two
    numeric neighbours *within that same side's own listing*? This never
    picks a winner (rule 3/4: a conflict is logged, not resolved) -- it is
    one more fact for the next reader, same as the brief asks for ("which
    copy is internally consistent with its own neighbours")."""
    try:
        code_i = int(code)
    except ValueError:
        return "code not numeric, order check skipped"
    seq = sorted(
        (int(r["code"]), bk.normalize_meaning(r["meaning"]))
        for r in rows
        if r["class"] == cls and bk._side_of(r["source"]) == side and r["code"].isdigit()
    )
    by_code = {c: m for c, m in seq}
    prev_m = by_code.get(code_i - 1)
    next_m = by_code.get(code_i + 1)
    this_m = by_code.get(code_i)
    if this_m is None or (prev_m is None and next_m is None):
        return "no same-side neighbour at code-1/code+1 to compare"
    ok_prev = prev_m is None or prev_m <= this_m
    ok_next = next_m is None or this_m <= next_m
    return "locally alphabetical" if (ok_prev and ok_next) else "breaks local alphabetical order"


def build_conflicts_tsv(rows, kinds):
    by_key = {}
    for r in rows:
        side = bk._side_of(r["source"])
        if side is None:
            continue
        by_key.setdefault((r["class"], r["code"], r["mark"]), {"509": [], "506": []})[side].append(r["meaning"])

    out_rows = []
    for (cls, code, mark), (kind, note) in sorted(kinds.items(), key=lambda kv: (kv[0][0], int(kv[0][1]) if kv[0][1].isdigit() else 0, kv[0][2])):
        sides = by_key[(cls, code, mark)]
        meaning_509 = "; ".join(sorted(set(sides["509"])))
        meaning_506 = "; ".join(sorted(set(sides["506"])))
        extra_note = note
        if kind in ("same-code-different-meaning", "same-meaning-different-code"):
            o509 = local_order_note(rows, cls, code, "509")
            o506 = local_order_note(rows, cls, code, "506")
            extra_note = f"{note}; order-509: {o509}; order-506: {o506}"
        out_rows.append({
            "code": code, "mark": mark, "class": cls,
            "meaning_509": meaning_509, "meaning_506": meaning_506,
            "kind": kind, "note": extra_note,
        })
    return out_rows


def write_conflicts_tsv(out_rows, path: Path):
    cols = ["code", "mark", "class", "meaning_509", "meaning_506", "kind", "note"]
    lines = [
        "# 509-vs-506 disagreements in key.tsv, classified by kind (job KEY32-CONFLICTS,",
        "# 24 Oct 2026, .claude/briefs/runs/2026-10-24-acct4-research-director-50.md).",
        "# One row per (class, code, mark) key that key.tsv flags `conflict`; 509/506 pages",
        "# are 509 pp.3712-3713 / 506 p.3705. Never a resolution -- both key.tsv rows keep",
        "# their own grade-H meaning unchanged (CLAUDE.md rule 4).",
        "# Regenerate: python3 conflicts.py",
    ]
    lines.append("\t".join(cols))
    for r in out_rows:
        lines.append("\t".join(r[c] for c in cols))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def sanity_table(rows):
    by_class = {}
    for r in rows:
        if not r["code"].isdigit():
            continue
        c = int(r["code"])
        d = by_class.setdefault(r["class"], {"codes": [], "conflicts": 0, "total": 0})
        d["codes"].append(c)
        d["total"] += 1
        if r.get("conflict_kind"):
            d["conflicts"] += 1
    lines = []
    for cls in sorted(by_class):
        d = by_class[cls]
        lo, hi = min(d["codes"]), max(d["codes"])
        share = d["conflicts"] / d["total"] * 100 if d["total"] else 0.0
        flag = ""
        expected = EXPECTED_RANGES.get(cls)
        if expected and (lo < expected[0] or hi > expected[1]):
            flag = f"  ** disagrees with chauran.htm's stated range {expected} **"
        lines.append(f"{cls}: code range {lo}-{hi}, {d['total']} rows, {d['conflicts']} conflict-flagged "
                     f"({share:.1f}%){flag}")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--key", default=str(HERE / "key.tsv"))
    p.add_argument("--out", default=str(HERE / "conflicts.tsv"))
    args = p.parse_args()

    key_path = Path(args.key)
    rows = bk.read_committed_rows(key_path)
    kinds = bk.apply_conflict_kinds(rows)  # sets row['conflict_kind'] in place

    out_rows = build_conflicts_tsv(rows, kinds)
    write_conflicts_tsv(out_rows, Path(args.out))

    bk.write_tsv(rows, key_path)  # rewrite key.tsv in place with conflict_kind (never hand-edited)

    from collections import Counter
    group_kinds = Counter(k for k, _ in kinds.values())
    row_kinds = Counter(r["conflict_kind"] for r in rows if r["conflict_kind"])
    print(f"conflicting keys: {len(kinds)}; conflict-flagged rows: {sum(row_kinds.values())}")
    print("by kind (keys / rows):")
    for kind in ("identical-after-normalisation", "spelling-variant", "same-code-different-meaning",
                 "same-meaning-different-code", "one-side-blank", "other"):
        print(f"  {kind}: {group_kinds.get(kind, 0)} keys / {row_kinds.get(kind, 0)} rows")
    print()
    print("sanity table:")
    print(sanity_table(rows))


if __name__ == "__main__":
    main()
