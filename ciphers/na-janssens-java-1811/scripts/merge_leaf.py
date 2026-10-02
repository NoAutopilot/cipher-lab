#!/usr/bin/env python3
"""Merge one reconciled gloss leaf (leaf, order, code, gloss, note) into key.tsv incrementally.

Usage: python3 scripts/merge_leaf.py leaf192_reconciled.tsv --key key.tsv --conflicts conflicts.tsv [--dry-run]

Why not rerun build_key.py: key.tsv carries hand edits that a from-scratch rebuild loses (VX-RD02C: the five No.5
plain-copy codes 597/748/904/456/244 and the 168/527 regrade), and build_key.py's own merge drops accent-only
disagreements (NOTES.md, VX-RD02C (1)). This script touches only the codes the new leaf attests, and never lowers
an existing row's evidence:

  code absent from key.tsv        -> new row: value = gloss, n = 1, pages = <leaf>, grade C when the cell is clean,
                                     M (note names why) when the only occurrence is corrected/uncertain/placement-unclear
  code present, same value        -> n += 1, pages gains <leaf>; grade unchanged (an M row stays M: one more clean
                                     occurrence of ONE variant is logged in note, not used to silently promote)
  code present, different value   -> grade M, note "ambiguous: <old> (n=.., pages=..); <new> (n=1, pages=<leaf>)",
                                     a conflicts.tsv row added or extended; the key's value column keeps the old
                                     (majority) value unless the new count exceeds it
  gloss crossed-out               -> skipped (a struck draft word is not a reading of the code)
  code empty (signature line)     -> skipped
Same-value test: build_key.py's glossnorm (case, trailing punctuation, apostrophe style) PLUS accent folding, so
"expedition"/"expédition" is agreement (the VX-RD02C bug), with the key's accented surface kept.
Prints one line per change and a summary; --dry-run prints without writing.
"""
import argparse
import csv
import unicodedata
from collections import OrderedDict


def norm(s):
    return (s or "").strip()


def glossnorm(s):
    s = norm(s).lower().replace("’", "'")
    s = s.rstrip(".,;:!?- ")
    # accent fold for comparison only
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
    return s


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("leaf_tsv")
    ap.add_argument("--key", default="key.tsv")
    ap.add_argument("--conflicts", default="conflicts.tsv")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    rows = load(a.leaf_tsv)
    key_rows = load(a.key)
    key = OrderedDict((r["code"], r) for r in key_rows)
    conflicts = OrderedDict((r["code"], r) for r in load(a.conflicts))

    added = same = conflict = skipped = 0
    for r in rows:
        code, gloss, note = norm(r["code"]), norm(r["gloss"]), norm(r.get("note", ""))
        leaf = norm(r["leaf"])
        if not code or not gloss or "crossed-out" in note:
            skipped += 1
            continue
        shaky = any(w in note for w in ("corrected", "uncertain", "placement unclear"))
        if code not in key:
            grade = "M" if shaky else "C"
            key[code] = {"code": code, "value": gloss, "n": "1", "pages": leaf, "grade": grade,
                         "note": (f"single occurrence, cell {note} (leaf {leaf})" if shaky else "")}
            added += 1
            print(f"ADD  {code} -> {gloss!r} grade {grade}{' ('+note+')' if note else ''}")
            continue
        k = key[code]
        pages = [p for p in k["pages"].split(",") if p]
        if leaf not in pages:
            pages.append(leaf)
        if glossnorm(gloss) == glossnorm(k["value"]):
            k["n"] = str(int(k["n"]) + 1)
            k["pages"] = ",".join(pages)
            if k["grade"] == "M" or shaky:
                tag = f"leaf {leaf}: {gloss} ({'clean' if not shaky else note})"
                k["note"] = (k["note"] + "; " if k["note"] else "") + tag
            same += 1
            print(f"SAME {code} {gloss!r} (n now {k['n']}, pages {k['pages']})")
            continue
        # different value
        old_n = int(k["n"])
        old_note = k["note"]
        variants = f"{k['value']} (n={old_n}, pages={','.join(p for p in pages if p != leaf)}); {gloss} (n=1, pages={leaf})"
        k["n"] = str(old_n + 1)
        k["pages"] = ",".join(pages)
        k["grade"] = "M"
        k["note"] = "ambiguous: " + variants + (f" [earlier note: {old_note}]" if old_note and not old_note.startswith("ambiguous") else "")
        if old_note.startswith("ambiguous"):
            k["note"] = old_note + f"; {gloss} (n=1, pages={leaf})"
        if code in conflicts:
            conflicts[code]["variants"] += f"; {gloss} (n=1, pages={leaf})"
        else:
            conflicts[code] = {"code": code, "variants": variants, "decision": ""}
        conflict += 1
        print(f"CONF {code} key {k['value']!r} vs leaf {gloss!r} -> M")

    print(f"summary: rows {len(rows)} added {added} same-value {same} conflicts {conflict} skipped {skipped}; key now {len(key)} codes")
    if a.dry_run:
        return
    with open(a.key, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["code", "value", "n", "pages", "grade", "note"], delimiter="\t")
        w.writeheader()
        for code in sorted(key, key=int):
            w.writerow(key[code])
    with open(a.conflicts, "w", newline="", encoding="utf-8") as f:
        # decision column (GAPS3, 2 Oct 2026): scripts/apply_regrades.py writes one decision per code; a later merge
        # that re-opens a code keeps the old decision text beside the new variant, for the next regrade to read
        w = csv.DictWriter(f, fieldnames=["code", "variants", "decision"], delimiter="\t", extrasaction="ignore")
        w.writeheader()
        for code in sorted(conflicts, key=int):
            w.writerow({"decision": "", **conflicts[code]})


if __name__ == "__main__":
    main()
