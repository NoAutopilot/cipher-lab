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

C column and the board (PROGRESS-SYNC, 9 Oct 2026, owner: "This isn't full"): C x means the board counts it, nothing else.
`--check-board` re-derives tools/build_dashboard.py counted() from status.json (plaintext_novelty N3+, audit_status two or
more audits, claim_scope recovered-passages/completed-reading, depth D2+, no qa_flag; copied here, not imported, because
build_dashboard.py renders on import) and compares it with each row: a row's C must be x exactly when a counted result of its
folder matches it, and every counted result must match some row. A row matches a result through its optional `board` column,
a case-insensitive regex searched in the result's title + documents; blank means every result of the folder, allowed only
when the folder has one row; `-` means "matches nothing" (a leaf with no counted result of its own). Catches: a C typed
before depth D2 was required, and a counted target with no row. Must NOT block: a row whose folder has no counted result
and whose C is '.' (most rows); an uncounted result in a folder that has rows (D1 fragments, N0-N2 readings).

Usage: python3 tools/progress_block.py [--tsv PROGRESS.tsv] [--check] [--no-notes] [--check-board [--status status.json]]
(--check exits 1 on a malformed row; --no-notes drops the long notes for the chat update; --check-board exits 1 on a mismatch)
"""
import argparse, csv, json, re, sys

STAGES = ["F", "K", "R", "1", "2", "C", "S"]
MARKS = {"x", "~", "."}
KSRC = {"o": "o", "p": "p", "b": "b", "p+o": "P", "b+o": "B", "b+p": "M", "?": "?", "-": "?", "": "?"}
TXT = {"k", "n", "?"}


def load(path):
    with open(path, encoding="utf-8") as fh:
        lines = [l for l in fh if not l.startswith("#") and l.strip()]
    return list(csv.DictReader(lines, delimiter="\t"))


TWO_PLUS = ("two audits", "three audits", "four audits")
READING_SCOPES = ("recovered-passages", "completed-reading")


def _n(r, field):
    m = re.search(r"N([0-5])", r.get(field, "") or "")
    return int(m.group(1)) if m else None


def result_counted(r):
    """tools/build_dashboard.py counted() for a result that carries claim_scope; rows without it keep the old rule there
    but none of those can pass the depth test, so they are never counted."""
    m = re.match(r"\s*D([0-4])", str(r.get("depth") or ""))
    return (not r.get("qa_flag") and "claim_scope" in r and (_n(r, "plaintext_novelty") or 0) >= 3
            and r.get("audit_status") in TWO_PLUS and r["claim_scope"] in READING_SCOPES
            and m is not None and int(m.group(1)) >= 2)


def counted_results(status):
    """[(folder, haystack text)] for every counted result in status.json."""
    out = []
    for r in status.get("results", []):
        if not result_counted(r):
            continue
        m = re.search(r"ciphers/([\w.-]+)", r.get("link", ""))
        docs = r.get("documents") or [r.get("document_id") or ""]
        out.append((m.group(1) if m else "", r.get("title", "") + " | " + " | ".join(map(str, docs))))
    return out


def check_board(rows, status):
    """Mismatch lines between each row's C mark and the board's counted set (empty list = in step)."""
    counted = counted_results(status)
    per_folder = {}
    for r in rows:
        per_folder[r["folder"]] = per_folder.get(r["folder"], 0) + 1
    bad, covered = [], set()
    for r in rows:
        f, b = r["folder"], (r.get("board") or "").strip()
        if not b and per_folder[f] > 1:
            bad.append(f"{r['name']}: folder {f} has {per_folder[f]} rows, set `board` (regex, or - for none)")
            continue
        hits = [i for i, (cf, txt) in enumerate(counted)
                if cf == f and b != "-" and (not b or re.search(b, txt, re.I))]
        covered.update(hits)
        want = "x" if hits else "."
        if (r.get("C") or "").strip() != want:
            bad.append(f"{r['name']}: C is {(r.get('C') or '').strip()!r}, board says {want!r} ({len(hits)} counted result(s))")
    for i, (cf, txt) in enumerate(counted):
        if i not in covered:
            bad.append(f"counted but no row: {cf} :: {txt[:90]}")
    return bad


def render(rows, notes=True):
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
        note = r.get("note", "").strip()
        if total <= 0:
            if not notes:
                note = re.split(r"[;,(]", note)[0].strip()[:28]
            out.append(f"{star}{r['name']:<{w}} {note}")
            continue
        n = min(10, firm * 10 // total)
        bar = "[" + "#" * n + "." * (10 - n) + "]"
        frac = f"{firm}/{total}"
        line = f"{star}{r['name']:<{w}} {bar} {frac:>10} read  " + " ".join(marks)
        if notes and note:
            line += "   (" + note + ")"
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
    ap.add_argument("--no-notes", action="store_true", help="omit the notes (the chat update's default)")
    ap.add_argument("--check-board", action="store_true", help="compare each row's C with status.json's counted set; exit 1 on a mismatch")
    ap.add_argument("--status", default="status.json")
    a = ap.parse_args()
    rows = load(a.tsv)
    text, problems = render(rows, notes=not a.no_notes)
    print(text)
    for p in problems:
        print("PROBLEM:", p, file=sys.stderr)
    bad = []
    if a.check_board:
        with open(a.status, encoding="utf-8") as fh:
            bad = check_board(rows, json.load(fh))
        for b in bad:
            print("BOARD MISMATCH:", b, file=sys.stderr)
        print(f"check-board: {len(rows)} rows, {len(bad)} mismatch(es)", file=sys.stderr)
    if (a.check and problems) or bad:
        sys.exit(1)


if __name__ == "__main__":
    main()
