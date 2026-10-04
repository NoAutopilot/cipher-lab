#!/usr/bin/env python3
"""Render the owner's progress block from PROGRESS.tsv (owner's format, 2 Oct 2026; hub-seed/CHECKIN-PROMPT.md).

One line per live target: optional `*` (a note about the finding was already sent or posted), short name, a 10-slot bar
(# per 10% of the letter's cipher tokens read firmly, rounded down), firm/total, then the seven stage columns
F K R 1 2 C S under a header row, and a two-line legend at the foot. The block is only as true as PROGRESS.tsv: every
row names the file it was read from in `source`, and the orchestrator edits a row only from a file on disk.

Catches: a row whose bar or stage marks were typed from memory (the 2 Oct 2026 August-of-Saxony row left out its
second audit, board count and send). Must NOT block: a row with total 0 (found-solved or not yet transcribed) renders
its note instead of a bar; a row with an unknown mark is rendered as `?` and reported, never dropped.

K cell and T column (KEYSOURCE-COL, 4 Oct 2026, owner's "do we denote when we make the key?"): when K is x or ~ and the
row's `ksrc` is set, the K cell shows whose key it is -- o ours, p period, b published, P period + ours, B published + ours,
M published + period, ? not recorded; K '.' stays '.'. The T column after S is `txt`: k plaintext known (in print or on
the leaf), n not located in print (N3+), ? not recorded. A row without these columns renders ? (old TSVs still load).

Usage: python3 tools/progress_block.py [--tsv PROGRESS.tsv] [--check]   (--check exits 1 on a malformed row)
"""
import argparse, csv, sys

STAGES = ["F", "K", "R", "1", "2", "C", "S"]
MARKS = {"x", "~", "."}
KSRC = {"o": "o", "p": "p", "b": "b", "p+o": "P", "b+o": "B", "b+p": "M", "?": "?", "-": "?", "": "?"}
TXT = {"k", "n", "?"}


def load(path):
    with open(path, encoding="utf-8") as fh:
        lines = [l for l in fh if not l.startswith("#") and l.strip()]
    return list(csv.DictReader(lines, delimiter="\t"))


def render(rows):
    out, problems = [], []
    w = max([len(r["name"]) for r in rows] + [10]) + 1
    out.append(" " * (1 + w + 1 + 12 + 1 + 10 + 7) + " ".join(STAGES) + " T")
    for r in rows:
        star = "*" if r.get("sent_star", "").strip() == "*" else " "
        try:
            firm, total = int(r["firm"]), int(r["total"])
        except (ValueError, KeyError):
            problems.append(f"{r.get('name')}: firm/total not numbers")
            firm, total = 0, 0
        marks = []
        for s in STAGES:
            m = (r.get(s) or "").strip()
            if m not in MARKS:
                problems.append(f"{r.get('name')}: stage {s} mark {m!r}")
                m = "?"
            if s == "K" and m in ("x", "~"):
                ks = (r.get("ksrc") or "").strip()
                if ks not in KSRC:
                    problems.append(f"{r.get('name')}: ksrc {ks!r}")
                m = KSRC.get(ks, "?")
            marks.append(m)
        t = (r.get("txt") or "?").strip() or "?"
        if t not in TXT:
            problems.append(f"{r.get('name')}: txt {t!r}")
            t = "?"
        marks.append(t)
        if total <= 0:
            out.append(f"{star}{r['name']:<{w}} {r.get('note', '').strip()}")
            continue
        n = min(10, firm * 10 // total)
        bar = "[" + "#" * n + "." * (10 - n) + "]"
        frac = f"{firm}/{total}"
        line = f"{star}{r['name']:<{w}} {bar} {frac:>10} read  " + " ".join(marks)
        if r.get("note", "").strip():
            line += "   (" + r["note"].strip() + ")"
        out.append(line)
    out.append("")
    out.append("F Found  K Key  R Read  1 Audit 1  2 Audit 2  C Counted  S Sent  T Text")
    out.append("K key: o ours, p period, b published (P period+ours, B published+ours, M published+period, ? unrecorded); "
               "T text: k known (in print or on the leaf), n not found in print, ? unrecorded")
    out.append("x done  ~ partial  . not yet   # = 10% of tokens read firmly   * = finding already emailed/posted")
    return "\n".join(out), problems


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--tsv", default="PROGRESS.tsv")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    text, problems = render(load(a.tsv))
    print(text)
    for p in problems:
        print("PROBLEM:", p, file=sys.stderr)
    if a.check and problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
